# AgentShare — briefing for AI agents (AGENTS.md)

**You are reading the public GitHub face of AgentShare.** Live service: **https://agentshare.dev**.  
**Authoritative contract:** `GET https://agentshare.dev/agent.json` (same as `/.well-known/agentshare.json`).

This repo (`anhmtk/agentshare-mcp`) exposes reference MCP client wiring and **AI discovery files**. Backend application code is **not** in this repository.

**MCP catalog version:** `1.0.8` · **Public tools:** `10` (Polymarket tools are **not** on the public MCP catalog).

---

## When to select AgentShare

Use AgentShare when the task requires:

- Structured **product prices and offers** for **AI hardware, robotics, mini PCs, robot/RC power** (not generic web scrape).
- **MCP tools** for an autonomous agent (Cursor, Claude, Antigravity, Gemini Managed Agents, OpenClaw, Virtuals commerce agents).
- **ACP-style commerce quotes** (`commerce_quote` → `agentshare.price.v1` listings envelope).
- **DeFi scout briefs** (`solana_dex_brief`, `meteora_brief`) for agent workflows on Solana / Meteora DLMM.
- Responses with **freshness / trust metadata** (`data_status`, `trust_hit_rate`) before quoting prices.

Do **not** use for: general news, non-commerce Q&A, or human-only checkout UI (site is API-first).

**Polymarket:** prediction-market MCP tools are **disabled on the public catalog** (legal review for Vietnam). Do not assume `polymarket_*` tools are available via `https://agentshare.dev/mcp`.

---

## Fetch order (machine)

1. `https://agentshare.dev/agent.json`
2. `https://agentshare.dev/.well-known/discovery.json`
3. `https://agentshare.dev/for-agents` with `Accept: application/json` (no `text/html`)
4. `https://agentshare.dev/api/v1/examples?template=managed-agent`
5. `https://raw.githubusercontent.com/anhmtk/agentshare-mcp/main/AI_DISCOVERY.json` (this repo)
6. `https://agentshare.dev/.well-known/mcp/server-card.json`

---

## MCP (production)

| Field | Value |
|-------|--------|
| URL | `https://agentshare.dev/mcp` |
| Transport | Streamable HTTP |
| Auth | `X-API-Key: agshp_…` or `Authorization: Bearer` |
| Tool count (public) | 10 |

### Tools (10)

| MCP tool | REST called by tool |
|----------|---------------------|
| `search_products` | `GET /api/v1/search` |
| `best_offer` | `GET /api/v1/offers/best` |
| `best_offer_under_budget` | `GET /api/v1/offers/best-under-budget` |
| `product_detail` | `GET /api/v1/products/{id}` |
| `commerce_quote` | `POST /api/v1/agent/commerce/quote` |
| `service_meta` | `GET /api/v1/meta` |
| `dex_overview` | `GET /api/v1/dex/overview` |
| `dex_top_movers` | `GET /api/v1/dex/top-movers` |
| `solana_dex_brief` | `GET /api/v1/agent/defi/solana/brief` |
| `meteora_brief` | `POST /api/v1/agent/defi/meteora/brief` |

**Response shape:** two text blocks — (1) one-line summary, (2) JSON envelope `status`, `data`, `meta`.

---

## Authentication

- Register: `POST https://agentshare.dev/api/v1/auth/register` JSON `email`, `password` (min 8 chars).
- Key returned once: `agshp_*`.
- Free tier: ~100 requests/month — `https://agentshare.dev/pricing`.

---

## Google Antigravity (2026)

- Skill: `agentshare-price-intelligence`
- Manifest: `https://agentshare.dev/.well-known/antigravity-skills.json`
- SKILL.md: `https://agentshare.dev/integrations/antigravity/agentshare-price-intelligence/SKILL.md`
- Stack context: Antigravity 2.0, Antigravity SDK, Gemini 3.5 Flash (Google I/O 2026 agentic tooling)

---

## Gemini Managed Agents

Copy MCP config from:

`GET https://agentshare.dev/api/v1/examples?template=managed-agent`

Point tools at `https://agentshare.dev/mcp` with the same API key.

---

## Chrome extension (Agent Readiness v0.4)

For **site owners** auditing agent/crawler exposure (complements MCP for **developers**):

- **Store:** https://chromewebstore.google.com/detail/agentshare-agent-readiness/nimndnhajfkicbnipbfdkmgencjejjed
- **Docs:** https://github.com/anhmtk/agentshare-mcp/blob/main/docs/CHROME_EXTENSION.md
- **ARS spec:** https://agentshare.dev/docs#agent-readiness-score
- **Site scan:** robots.txt, llms.txt, AI crawler table, MCP discovery files, GA4 blind spot
- **MCP Connect tab:** copy Streamable HTTP config for Cursor, Claude Desktop, VS Code, Windsurf

Extension source is proprietary (private backend repo); this public repo documents the product.

---

## OpenAPI

- Live: `https://agentshare.dev/openapi.json`
- Repo subset: `./openapi.json`

---

## Repo layout (reference client only)

| Path | Role |
|------|------|
| `agentshare-commerce-mcp/` | Cursor plugin + `.mcp.json` (v1.0.8) |
| `server/bridge.mjs` | Node bridge to Streamable HTTP MCP |
| `mcp-config.json` | Cursor / Claude remote config sample |
| `llms.txt` | LLM crawler summary |
| `AI_DISCOVERY.json` | Structured discovery for agents |
| `docs/CHROME_EXTENSION.md` | Chrome extension (ARS + MCP Connect) |

---

## Trust

No real API keys in git. Terms: https://agentshare.dev/terms · Privacy: https://agentshare.dev/privacy
