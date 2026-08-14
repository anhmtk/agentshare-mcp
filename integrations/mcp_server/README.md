# MCP Server — AgentShare agent-paid API (reference copy)

Expose AgentShare as MCP tools for Cursor, Claude Desktop, etc.

**Live catalog:** **11 tools** · version **1.0.9** · Polymarket tools **not** on public MCP.  
**Primary:** agent-paid rails (dual-auth / x402 / discovery). **Secondary:** commerce + Solana/Meteora demos.

**AI agent onboarding (repo root):** see [`../../AGENTS.md`](../../AGENTS.md) and [`../../AI_DISCOVERY.json`](../../AI_DISCOVERY.json).

**Remote (Streamable HTTP):** `https://agentshare.dev/mcp` — send `X-API-Key` or `Authorization: Bearer` (see [MCP docs](https://agentshare.dev/docs)). Start building: https://agentshare.dev/signup

## Quick Start (stdio, local)

```bash
pip install -r requirements.txt
export API_KEY=your_key
python integrations/mcp_server/server.py
```

Prefer **Node bridge** (`server/bridge.mjs` or `agentshare-commerce-mcp/`) for Cursor — see [README](../../README.md).

## Tools (public MCP — 11)

| Tool | Auth | Description | Layer |
|------|------|-------------|-------|
| `search_products` | Yes | Search product prices | commerce |
| `best_offer` | Yes | Cheapest offer for query | commerce |
| `best_offer_under_budget` | Yes | Best offer within budget | commerce |
| `product_detail` | Yes | Product detail by id from search | commerce |
| `commerce_quote` | Yes | ACP / agent-buyer listings envelope | commerce |
| `service_meta` | No* | API capabilities | rails |
| `dex_overview` | No | DEX protocol rankings (DefiLlama) | DeFi demo |
| `dex_top_movers` | No | DEX volume-change movers (DefiLlama) | DeFi demo |
| `solana_dex_brief` | No | Solana DEX ecosystem brief | DeFi demo |
| `meteora_brief` | Yes | Meteora DLMM pool brief | DeFi demo |
| `meteora_pool_detail` | Yes | Meteora DLMM pool detail | DeFi demo |

\*Connecting to MCP over HTTP still requires an API key per site policy; `service_meta` upstream REST is public once connected.

**Not on public MCP:** `polymarket_markets`, `polymarket_market_detail`, `polymarket_top_movers`, `polymarket_brief`.

## Env

- `API_KEY` — required for price tools
- `BASE_URL` — default: https://agentshare.dev

## Cursor Setup

See [agentshare-commerce-mcp/README.md](../../agentshare-commerce-mcp/README.md) and [docs/CURSOR_DIRECTORY.md](../../docs/CURSOR_DIRECTORY.md).
