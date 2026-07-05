# MCP Server — Agent Price API (reference copy)

Expose AgentShare as MCP tools for Cursor, Claude Desktop, etc.

**Live catalog:** **10 tools** · version **1.0.8** · Polymarket tools **not** on public MCP.

**AI agent onboarding (repo root):** see [`../../AGENTS.md`](../../AGENTS.md) and [`../../AI_DISCOVERY.json`](../../AI_DISCOVERY.json).

**Remote (Streamable HTTP):** `https://agentshare.dev/mcp` — send `X-API-Key` or `Authorization: Bearer` (see [MCP docs](https://agentshare.dev/docs)).

## Quick Start (stdio, local)

```bash
pip install -r requirements.txt
export API_KEY=your_key
python integrations/mcp_server/server.py
```

Prefer **Node bridge** (`server/bridge.mjs` or `agentshare-commerce-mcp/`) for Cursor — see [README](../../README.md).

## Tools (public MCP — 10)

| Tool | Auth | Description |
|------|------|-------------|
| `search_products` | Yes | Search product prices |
| `best_offer` | Yes | Cheapest offer for query |
| `best_offer_under_budget` | Yes | Best offer within budget |
| `product_detail` | Yes | Product detail by id from search |
| `commerce_quote` | Yes | ACP / agent-buyer listings envelope |
| `service_meta` | No* | API capabilities |
| `dex_overview` | No | DEX protocol rankings (DefiLlama) |
| `dex_top_movers` | No | DEX volume-change movers (DefiLlama) |
| `solana_dex_brief` | No | Solana DEX ecosystem brief |
| `meteora_brief` | Yes | Meteora DLMM pool brief |

\*Connecting to MCP over HTTP still requires an API key per site policy; `service_meta` upstream REST is public once connected.

**Not on public MCP:** `polymarket_markets`, `polymarket_market_detail`, `polymarket_top_movers`, `polymarket_brief`.

## Env

- `API_KEY` — required for price tools
- `BASE_URL` — default: https://agentshare.dev

## Cursor Setup

See [agentshare-commerce-mcp/README.md](../../agentshare-commerce-mcp/README.md) and [docs/CURSOR_DIRECTORY.md](../../docs/CURSOR_DIRECTORY.md).
