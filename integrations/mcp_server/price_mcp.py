"""
Shared FastMCP app for Agent Price API — tools + factory for stdio / Streamable HTTP.

Tool handlers return list[TextContent]: (1) one-line summary, (2) JSON envelope with full payload.
"""
from __future__ import annotations

import asyncio
import os
from contextvars import ContextVar
from pathlib import Path
from typing import Annotated, Any

import requests
from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings
from mcp.types import TextContent, ToolAnnotations
from pydantic import Field

from integrations.mcp_server.mcp_tool_format import tool_result_from_api_dict

# Per-request API key for Streamable HTTP (set by ASGI wrapper on /mcp)
mcp_request_api_key: ContextVar[str | None] = ContextVar("mcp_request_api_key", default=None)

# MCP spec hints: read-only tools; marketplace tools interact with open-world marketplaces
ANN_MARKETPLACE = ToolAnnotations(readOnlyHint=True, openWorldHint=True, idempotentHint=True)
ANN_SERVICE_META = ToolAnnotations(readOnlyHint=True, openWorldHint=False, idempotentHint=True)


def _load_dotenv() -> None:
    """Load .env from mcp_server dir or project root."""
    here = Path(__file__).resolve().parent
    project_root = here.parent.parent
    for p in (here / ".env", project_root / ".env"):
        if p.exists():
            with open(p) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, _, v = line.partition("=")
                        k, v = k.strip(), v.strip().strip('"').strip("'")
                        if k and k not in os.environ:
                            os.environ[k] = v
            break


def _effective_api_key() -> str:
    """HTTP MCP uses ContextVar; stdio uses env. Glama may inject X-API-Key / Authorization."""
    ctx = (mcp_request_api_key.get() or "").strip()
    if ctx:
        return ctx
    for name in ("API_KEY", "X_API_KEY", "X-API-Key"):
        v = (os.getenv(name) or "").strip()
        if v:
            return v
    auth = (os.getenv("Authorization") or "").strip()
    if auth.lower().startswith("bearer "):
        return auth[7:].strip()
    return ""


def _call_api_dict(path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
    """
    Call Agent Price REST API; return the JSON object from the wire (success or error body).

    Blocking I/O — must not run on the asyncio event loop when BASE_URL points at this same
    process (Streamable HTTP MCP on uvicorn): FastMCP invokes sync tools directly on the loop,
    which would deadlock a single worker until MCP_UPSTREAM_TIMEOUT_SEC. Tool handlers wrap
    this in asyncio.to_thread.
    """
    base = os.getenv("BASE_URL", "https://agentshare.dev").rstrip("/")
    key = _effective_api_key()
    headers: dict[str, str] = {"Accept": "application/json"}
    if key:
        headers["X-API-Key"] = key
    timeout_sec = float(os.getenv("MCP_UPSTREAM_TIMEOUT_SEC", "120"))
    try:
        r = requests.get(
            f"{base}{path}",
            params=params or {},
            headers=headers,
            timeout=timeout_sec,
        )
        try:
            data = r.json()
        except requests.JSONDecodeError:
            return {
                "status": "error",
                "error": {
                    "code": "INVALID_RESPONSE",
                    "message": "Server did not return JSON",
                    "detail": (r.text or "")[:500],
                },
            }
        if not isinstance(data, dict):
            return {
                "status": "error",
                "error": {"code": "UNEXPECTED_SHAPE", "message": "Expected a JSON object from the API"},
            }
        return data
    except requests.RequestException as e:
        return {"status": "error", "error": {"code": "TRANSPORT", "message": str(e)}}
    except Exception as e:
        return {"status": "error", "error": {"code": "INTERNAL", "message": str(e)}}


def create_price_mcp() -> FastMCP:
    """
    Build FastMCP with Streamable HTTP path '/' (mount app at /mcp in FastAPI).

    transport_security: DNS rebinding disabled so diverse MCP clients (CLI, cloud)
    behind Cloudflare / custom domains are not blocked by Host/Origin checks.
    """
    _load_dotenv()

    mcp = FastMCP(
        "agent-price-api",
        instructions=(
            "AgentShare exposes marketplace price intelligence as structured JSON over REST and MCP. "
            "Production path emphasizes the official AliExpress integration; other leading e-commerce "
            "platforms will be linked when contractual and technical conditions are met. "
            "Use search_products for multi-listing comparison; best_offer when the user wants a single "
            "cheapest in-stock option; best_offer_under_budget when they specify a maximum price; "
            "service_meta for discovery without credentials. "
            "Data scope (AI hardware, mini PCs, components, robotics, robot/RC batteries) is documented at "
            "GET /coverage on the site — same sources as REST. "
            "Each tool returns two text blocks: a one-line summary, then a JSON envelope "
            "(status, data, meta). "
            "Authenticate HTTP MCP with X-API-Key or Authorization: Bearer. "
            "Documentation: https://agentshare.dev/docs#mcp"
        ),
        website_url="https://agentshare.dev",
        streamable_http_path="/",
        stateless_http=True,
        transport_security=TransportSecuritySettings(
            enable_dns_rebinding_protection=False,
        ),
    )

    @mcp.tool(
        title="Search product listings",
        description=(
            "Search connected marketplaces and return structured offers (prices, sources, freshness). "
            "Use when the user wants to compare options, browse multiple listings, or explore a product "
            "category or model—not when they only need one definitive 'cheapest' pick (use best_offer). "
            "Works for robotics parts, robot/drone batteries, and AI hardware — see /coverage for focus areas. "
            "Accepts free-text queries in any language."
        ),
        annotations=ANN_MARKETPLACE,
        structured_output=False,
    )
<<<<<<< HEAD
    def search_products(
=======
    async def search_products(
>>>>>>> 31819e8 (docs: README for Anthropic extension + align MCP tools (search_products, annotations))
        query: Annotated[
            str,
            Field(
                description="Keywords: product name, model number, brand, or category.",
                min_length=1,
            ),
        ],
        limit: Annotated[
            int,
            Field(
                description="Maximum rows to return (higher = broader scan, more tokens).",
                ge=1,
                le=50,
            ),
        ] = 10,
    ) -> list[TextContent]:
        raw = await asyncio.to_thread(_call_api_dict, "/api/v1/search", {"q": query, "limit": limit})
        return tool_result_from_api_dict(raw, tool_name="search_products")

    @mcp.tool(
        title="Best single offer",
        description=(
            "Return the single best current offer for a product intent: typically lowest price among "
            "in-stock listings the API trusts. "
            "Use when the user asks where to buy something cheapest, 'best deal', or one clear recommendation. "
            "For side‑by‑side comparison of many listings, prefer search_products."
        ),
        annotations=ANN_MARKETPLACE,
        structured_output=False,
    )
    async def best_offer(
        query: Annotated[
            str,
            Field(
                description="What to buy, e.g. product name + model or distinguishing keywords.",
                min_length=1,
            ),
        ],
    ) -> list[TextContent]:
        raw = await asyncio.to_thread(_call_api_dict, "/api/v1/offers/best", {"q": query})
        return tool_result_from_api_dict(raw, tool_name="best_offer")

    @mcp.tool(
        title="Best offer under budget",
        description=(
            "Find the best offer for a product query with a maximum price ceiling. "
            "Use when the user gives a budget, 'under $X', 'below …', or 'no more than …'. "
            "Pass max_price in the same numeric unit the deployed API expects for that field (see API docs). "
            "Do not use for open-ended comparison without a cap—use search_products or best_offer."
        ),
        annotations=ANN_MARKETPLACE,
        structured_output=False,
    )
    async def best_offer_under_budget(
        query: Annotated[
            str,
            Field(description="Product or deal to find within the budget.", min_length=1),
        ],
        max_price: Annotated[
            float,
            Field(
                description=(
                    "Strict upper bound on price, using the same numeric scale as the API's pricing fields "
                    "for your environment (see /api/v1/meta or site docs)."
                ),
                gt=0,
            ),
        ],
    ) -> list[TextContent]:
        raw = await asyncio.to_thread(
            _call_api_dict,
            "/api/v1/offers/best-under-budget",
            {"q": query, "max_price": max_price},
        )
        return tool_result_from_api_dict(raw, tool_name="best_offer_under_budget")

    @mcp.tool(
        title="Service metadata",
        description=(
            "Return API capabilities, rate limits, and integration hints. "
            "Safe to call without an API key when the deployment allows it. "
            "Use for onboarding, capability checks, or answering 'what can this API do?' before calling paid tools."
        ),
        annotations=ANN_SERVICE_META,
        structured_output=False,
    )
    async def service_meta() -> list[TextContent]:
        raw = await asyncio.to_thread(_call_api_dict, "/api/v1/meta")
        return tool_result_from_api_dict(raw, tool_name="service_meta")

    return mcp
