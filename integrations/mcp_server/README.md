# MCP Server — Agent Price API

Expose Agent Price API as MCP tools for Cursor, Claude Desktop, etc.

**Remote (Streamable HTTP):** `https://agentshare.dev/mcp` — send `X-API-Key` or `Authorization: Bearer` (see [docs/MCP_QUICKSTART.md](../../docs/MCP_QUICKSTART.md)).

## Quick Start (stdio, local)

```bash
pip install -r requirements.txt   # from repo root, or integrations/mcp_server/requirements.txt
export API_KEY=your_key
python integrations/mcp_server/server.py
```

## Tools

| Tool | Auth | Description |
|------|------|-------------|
| `price_search` | Yes | Search product prices |
| `best_offer` | Yes | Cheapest offer for query |
| `best_offer_under_budget` | Yes | Best offer within budget (VND) |
| `service_meta` | No | API capabilities |

## Env

- `API_KEY` — required for price tools
- `BASE_URL` — default: https://agentshare.dev

## Cursor Setup

See [docs/MCP_CURSOR_SETUP.md](../../docs/MCP_CURSOR_SETUP.md) for manual Cursor configuration steps.
