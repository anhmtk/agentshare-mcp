"""
MCP tool response helpers: two TextContent blocks (summary + JSON envelope) and ToolAnnotations.
No LLM calls — summaries are template-based from API JSON.
"""
from __future__ import annotations

import json
from typing import Any

from mcp.types import TextContent

MCP_FORMAT_VERSION = 1

# Standard error codes exposed to agents (aligned with project policy)
INVALID_QUERY = "INVALID_QUERY"
NOT_FOUND = "NOT_FOUND"
RATE_LIMITED = "RATE_LIMITED"
STALE_DATA = "STALE_DATA"
UPSTREAM_ERROR = "UPSTREAM_ERROR"


def _fmt_price_vnd(amount: int | float | None) -> str:
    """Format integer price with thousands separators + dong sign (template requested)."""
    if amount is None:
        return "—"
    try:
        n = int(amount)
    except (TypeError, ValueError):
        return str(amount)
    s = f"{abs(n):,}".replace(",", ".")
    return f"{s}₫"


def _pick_stock_emoji(availability: bool | None) -> str:
    if availability is True:
        return "✅"
    if availability is False:
        return "❌"
    return "❓"


def build_summary(api_result: dict[str, Any], *, tool_name: str = "") -> str:
    """
    One-line English summary for TextContent block 1.
    Template when possible: Best price: X₫ on Y — ✅/❌ stock — Data age: Zs
    """
    if api_result.get("status") == "error":
        err = api_result.get("error") or {}
        code = err.get("code", "error")
        msg = (err.get("message") or "Request failed")[:120]
        return f"Error: {code} — {msg}"

    data = api_result.get("data")
    meta = api_result.get("meta") or {}
    fresh = (meta.get("freshness_status") or "unknown").lower()
    stale_prefix = "⚠️ Stale data — " if fresh in ("stale", "expired") else ""

    # --- search (data is a list of products) ---
    if isinstance(data, list) and isinstance(meta, dict) and "total" in meta:
        total = meta.get("total", len(data))
        age = meta.get("data_age_seconds")
        age_s = f"{int(age)}s" if age is not None else "—"
        fr = meta.get("freshness_status") or "unknown"
        return stale_prefix + (
            f"Search: {total} listing(s) — freshness: {fr} — Data age: {age_s}"
        )

    # --- best_offer (single product + best_offer item) ---
    if isinstance(data, dict) and "best_offer" in data and "product" in data and "budget" not in data:
        bo = data.get("best_offer") or {}
        price = bo.get("price")
        src = (bo.get("source") or "unknown").upper()
        av = bo.get("availability")
        age = bo.get("data_age_seconds")
        if age is None:
            age = meta.get("data_age_seconds")
        stock = _pick_stock_emoji(av)
        age_s = f"{int(age)}s" if age is not None else "—"
        line = (
            f"Best price: {_fmt_price_vnd(price)} on {src} — {stock} stock — Data age: {age_s}"
        )
        return stale_prefix + line

    # --- best_under_budget ---
    if isinstance(data, dict) and "budget" in data and "query" in data:
        bo = data.get("best_offer")
        age = meta.get("data_age_seconds")
        age_s = f"{int(age)}s" if age is not None else "—"
        if bo is None:
            return stale_prefix + f"No offer under budget — Data age context: {age_s}"
        price = bo.get("price")
        src = (bo.get("source") or "unknown").upper()
        av = bo.get("availability")
        stock = _pick_stock_emoji(av)
        return stale_prefix + (
            f"Best under budget: {_fmt_price_vnd(price)} on {src} — {stock} stock — Data age: {age_s}"
        )

    # --- service_meta ---
    if isinstance(data, dict) and data.get("service") and data.get("auth"):
        ver = data.get("version") or ""
        svc = data.get("service") or "API"
        return stale_prefix + f"API: {svc} v{ver} — discovery OK (structured endpoints in JSON)."

    # fallback
    return stale_prefix + "OK — see JSON block for full response."


def format_tool_response(summary: str, payload: dict[str, Any]) -> list[TextContent]:
    """Block 1: one-line summary. Block 2: pretty-printed JSON envelope."""
    body = json.dumps(payload, ensure_ascii=False, indent=2)
    return [
        TextContent(type="text", text=summary.strip()),
        TextContent(type="text", text=body),
    ]


def ok(api_result: dict[str, Any], *, extra_meta: dict[str, Any] | None = None, tool_name: str = "") -> list[TextContent]:
    """
    Success envelope:
    { "status": "ok", "data": <full API JSON object>, "meta": { mcp_format_version, ... } }
    """
    meta_out: dict[str, Any] = {"mcp_format_version": MCP_FORMAT_VERSION}
    if extra_meta:
        meta_out.update(extra_meta)
    envelope: dict[str, Any] = {
        "status": "ok",
        "data": api_result,
        "meta": meta_out,
    }
    summary = build_summary(api_result, tool_name=tool_name)
    return format_tool_response(summary, envelope)


def err(
    code: str,
    message: str,
    *,
    retry_after: int | None = None,
    api_raw: dict[str, Any] | None = None,
) -> list[TextContent]:
    """
    Error envelope:
    { "status": "error", "error": { code, message, retry_after? }, "meta": { ... } }
    """
    err_obj: dict[str, Any] = {"code": code, "message": message}
    if retry_after is not None:
        err_obj["retry_after"] = retry_after
    meta_out: dict[str, Any] = {"mcp_format_version": MCP_FORMAT_VERSION}
    if api_raw is not None:
        meta_out["upstream_response"] = api_raw
        rid = api_raw.get("request_id")
        if rid is not None:
            meta_out["request_id"] = rid
    envelope = {
        "status": "error",
        "error": err_obj,
        "meta": meta_out,
    }
    summary = f"Error: {code} — {message}"
    if retry_after is not None:
        summary += f" — retry after {retry_after}s"
    return format_tool_response(summary, envelope)


def _normalize_upstream_code(code: str | None) -> str:
    if not code:
        return UPSTREAM_ERROR
    mapping = {
        "RATE_LIMIT_EXCEEDED": RATE_LIMITED,
        "NOT_FOUND": NOT_FOUND,
        "INVALID_RESPONSE": UPSTREAM_ERROR,
        "TRANSPORT": UPSTREAM_ERROR,
        "INTERNAL": UPSTREAM_ERROR,
        "UNEXPECTED_SHAPE": UPSTREAM_ERROR,
    }
    c = mapping.get(code, code)
    if c in (INVALID_QUERY, NOT_FOUND, RATE_LIMITED, STALE_DATA, UPSTREAM_ERROR):
        return c
    if c == NOT_FOUND:
        return NOT_FOUND
    # Keep recognizable API codes as upstream unless mapped
    if c in ("MISSING_API_KEY", "INVALID_API_KEY", "OUT_OF_CREDITS", "KEY_EXPIRED", "PAYLOAD_TOO_LARGE"):
        return UPSTREAM_ERROR
    return UPSTREAM_ERROR


def tool_result_from_api_dict(
    raw: dict[str, Any],
    *,
    tool_name: str = "",
) -> list[TextContent]:
    """
    Turn raw REST JSON into MCP TextContent list. Does not change fetch logic — only shapes output.
    """
    if raw.get("status") == "error":
        e = raw.get("error") or {}
        code = _normalize_upstream_code(e.get("code"))
        msg = e.get("message") or "Request failed"
        ra = e.get("retry_after")
        return err(code, str(msg), retry_after=ra, api_raw=raw)

    if raw.get("status") == "ok":
        return ok(raw, tool_name=tool_name)

    if not raw:
        return err(UPSTREAM_ERROR, "Empty response from API", api_raw=raw)

    # Unexpected shape — pass through wrapped for debugging
    return ok(
        {"status": "ok", "data": raw, "meta": {}},
        extra_meta={"note": "response_missing_top_level_status"},
        tool_name=tool_name,
    )
