"""ASGI wrapper: copy X-API-Key / Bearer into ContextVar for MCP tools."""
from __future__ import annotations

from typing import Any

from integrations.mcp_server.price_mcp import mcp_request_api_key


def _parse_api_key_from_scope(scope: dict[str, Any]) -> str | None:
    if scope.get("type") != "http":
        return None
    key: str | None = None
    for hk, hv in scope.get("headers", []):
        if hk.lower() == b"x-api-key":
            key = hv.decode("latin-1").strip()
            break
    if key:
        return key
    for hk, hv in scope.get("headers", []):
        if hk.lower() == b"authorization":
            auth = hv.decode("latin-1").strip()
            if auth.lower().startswith("bearer "):
                return auth[7:].strip()
            break
    return None


def wrap_mcp_app_with_request_api_key(inner):
    """Starlette/FastMCP ASGI app wrapper."""

    async def app(scope: dict[str, Any], receive: Any, send: Any) -> None:
        key = _parse_api_key_from_scope(scope)
        token = mcp_request_api_key.set(key) if key else None
        try:
            await inner(scope, receive, send)
        finally:
            if token is not None:
                mcp_request_api_key.reset(token)

    return app
