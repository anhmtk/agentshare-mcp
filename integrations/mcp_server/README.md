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

Prefer **`.mcpb`** or **Node bridge** for Claude when you do not need Python stdio — see [README](../../README.md).

## Tools

| Tool | Auth | Description |
|------|------|-------------|
| `search_products` | Yes | Search product prices |
| `best_offer` | Yes | Cheapest offer for query |
| `best_offer_under_budget` | Yes | Best offer within budget (VND) |
| `product_detail` | Yes | Product detail by id from search |
| `commerce_quote` | Yes | ACP / agent-buyer listings envelope |
| `service_meta` | No | API capabilities |
| `polymarket_markets` | No | List active Polymarket markets (read-only) |
| `polymarket_market_detail` | No | Polymarket market detail by market_id (read-only) |
| `polymarket_top_movers` | No | Polymarket top movers (24h) (read-only) |
| `polymarket_brief` | No | Evidence-first Polymarket brief (read-only) |
| `dex_overview` | No | DEX protocol rankings by 24h volume (DefiLlama) |
| `dex_top_movers` | No | DEX protocols with largest 1d volume-change % (DefiLlama) |

## Env

- `API_KEY` — required for price tools
- `BASE_URL` — default: https://agentshare.dev

## Cursor Setup

See [Cursor MCP setup](https://agentshare.dev/docs) (MCP section) or repo [README](../../README.md).
