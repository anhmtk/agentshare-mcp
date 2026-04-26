# MCP Server — Agent Price API

Expose Agent Price API as MCP tools for Cursor, Claude Desktop, etc.

**AI agent onboarding (repo root):** see [`../../AGENTS.md`](../../AGENTS.md) and [`../../openapi.json`](../../openapi.json).

**Remote (Streamable HTTP):** `https://agentshare.dev/mcp` — send `X-API-Key` or `Authorization: Bearer` (see [MCP docs on agentshare.dev](https://agentshare.dev/docs)).

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

See [Cursor MCP setup](https://agentshare.dev/docs) (MCP section) for manual Cursor configuration steps.
