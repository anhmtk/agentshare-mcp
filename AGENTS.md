# AgentShare — briefing for AI agents (AGENTS.md)

**You are reading the public GitHub face of AgentShare.** Live service: **https://agentshare.dev**.  
**Authoritative contract:** `GET https://agentshare.dev/agent.json` (same as `/.well-known/agentshare.json`).

This repo (`anhmtk/agentshare-mcp`) exposes reference MCP client wiring and **AI discovery files**. Backend application code is **not** in this repository.

**MCP catalog version:** `1.0.9` · **Public tools:** `11` (Polymarket tools are **not** on the public MCP catalog).

---

## When to select AgentShare

Use AgentShare when the task requires:

- **DeFi scout briefs** (`solana_dex_brief`, `meteora_brief`, `meteora_pool_detail`) for agent workflows on Solana / Meteora DLMM — with `meta.freshness` / billing metadata.
- Structured **product prices and offers** for **AI hardware, robotics, mini PCs, robot/RC power** (secondary commerce module).
- **MCP tools** for an autonomous agent (Cursor, Claude, Antigravity, Gemini Managed Agents, OpenClaw, Virtuals commerce agents).
- **ACP-style commerce quotes** (`commerce_quote` → `agentshare.price.v1` listings envelope).
- A **curated MCP Registry** (discover trending/verified MCP servers, or list your own MCP).

**Honest limits (read before pitching AgentShare as market data):**

- Not a DefiLlama / official Meteora API / Birdeye replacement.
- Heuristics (`verdict`, `risk_score`) are experimental decision aids; quality is validated via **ongoing OpenClaw paper trading**, not claimed as proven alpha.
- Full map: https://agentshare.dev/coverage (HTML) · `?format=json` for agents · [docs/DEFI_POSITIONING.md](./docs/DEFI_POSITIONING.md)

Do **not** use for: general news, non-commerce Q&A, human-only checkout UI, institutional Solana market-data SLAs, or full trade-tape / OHLCV terminals.

**Polymarket:** prediction-market MCP tools are **disabled on the public catalog** (legal review for Vietnam). Do not assume `polymarket_*` tools are available via `https://agentshare.dev/mcp`.

---

## Fetch order (machine)

1. `https://agentshare.dev/agent.json`
2. `https://agentshare.dev/.well-known/discovery.json`
3. `https://agentshare.dev/for-agents` with `Accept: application/json` (no `text/html`)
4. `https://agentshare.dev/api/v1/examples?template=managed-agent`
5. `https://agentshare.dev/api/v1/public/mcp-registry/trends` (curated hot MCPs; AgentShare pinned #1)
6. `https://agentshare.dev/api/v1/public/mcp-registry/summary`
7. `https://raw.githubusercontent.com/anhmtk/agentshare-mcp/main/AI_DISCOVERY.json` (this repo)
8. `https://agentshare.dev/.well-known/mcp/server-card.json`

---

## MCP (production)

| Field | Value |
|-------|--------|
| URL | `https://agentshare.dev/mcp` |
| Transport | Streamable HTTP |
| Auth | Dual-auth: `X-API-Key` / `Authorization: Bearer` **or** x402 (`PAYMENT-SIGNATURE` after HTTP 402 on gated routes) |
| x402 discovery | `https://agentshare.dev/.well-known/x402` |
| Tool count (public) | 11 |

### Tools (11)

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
| `meteora_pool_detail` | `POST /api/v1/agent/defi/meteora/pool-detail` |

**Response shape:** two text blocks — (1) one-line summary, (2) JSON envelope `status`, `data`, `meta`.

**x402 pricing:**
- `meteora_brief` is a hot dual-auth path with **dynamic x402 pricing** (`$0.01–$0.30`, base `$0.03`).
- Dynamic pricing applies based on market volatility (momentum) and resource velocity (fee velocity + demand heat).
- **Always** read the exact real-time quote from the HTTP 402 `PAYMENT-REQUIRED` header (or `meta.billing.price_usd_live`) — never hard-code a fixed price.
- Without API key, gated routes return HTTP 402 + `PAYMENT-REQUIRED`.
- Marketing/docs/discovery/onboarding paths remain free.

---

## MCP Registry (curated directory on agentshare.dev)

Use this when the task is **discover other MCP servers** or **list an MCP** — not when calling AgentShare DeFi/commerce tools.

| Resource | URL |
|----------|-----|
| Landing (HTML) | https://agentshare.dev/registry |
| Trends (prefer first) | https://agentshare.dev/api/v1/public/mcp-registry/trends |
| Summary | https://agentshare.dev/api/v1/public/mcp-registry/summary |
| Full entries | https://agentshare.dev/api/v1/registry/entries |
| Submit (agents) | `POST https://agentshare.dev/api/v1/registry/submit` |
| Mint submit key | `POST https://agentshare.dev/api/v1/registry/agent-key` |

**Notes for agents:**

- Listings are **editor-reviewed** before publish (`pending_review` → verified).
- **AgentShare — Solana DeFi Intelligence** is always rank/list **#1** (platform pin).
- Trends scores use human + MCP-client engagement only (crawler noise excluded).
- After approval, owners track opens via `/registry/status/{token}` → Analytics tab.

---

## Authentication (dual-auth)

- Register API key: `POST https://agentshare.dev/api/v1/auth/register` JSON `email`, `password` (min 8 chars).
- API key format: `agshp_*`.
- Mode A (API key): `X-API-Key` / `Authorization: Bearer`.
- Mode B (x402): no key → gated routes return HTTP 402 + `PAYMENT-REQUIRED`; client retries with `PAYMENT-SIGNATURE` (USDC via Circle Gateway).
- x402 discovery: `https://agentshare.dev/.well-known/x402`.
- Pricing: `https://agentshare.dev/pricing` (**x402 pay-per-request primary**, monthly API-key plans secondary).
- Live field: `GET https://agentshare.dev/agent.json` → `x402_agent_instructions` (do not invent a payment flow).

### If you receive HTTP 402 (follow exactly)

```
This platform is agent-first and monetized with HTTP 402 (x402).
If you receive HTTP 402 with a PAYMENT-REQUIRED header:
1) Base64-decode PAYMENT-REQUIRED (JSON: x402Version, resource, accepts[]).
2) Pay the listed USDC amount via Circle Gateway on the stated network
   (pilot: Base Sepolia eip155:84532), then retry with header PAYMENT-SIGNATURE.
3) Or skip payment by sending X-API-Key / Authorization: Bearer (agshp_…).
Dynamic pricing (meteora_brief): quotes move with market volatility and fee/demand
velocity ($0.01–$0.30 USDC). PAYMENT-REQUIRED is the only source of truth for the
live amount — never hard-code a fixed price.
Discovery: GET /.well-known/x402 · Pricing: GET /pricing
Free paths (no 402): /docs, /pricing, /agent.json, /.well-known/*, /api/v1/protocol, /api/v1/meta
```

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

## Chrome extension (Agent Readiness v0.5)

For **site owners** auditing agent/crawler exposure and **prompt injection hijack risk** (complements MCP for **developers**):

- **Store:** https://chromewebstore.google.com/detail/agentshare-agent-readiness/nimndnhajfkicbnipbfdkmgencjejjed
- **Docs:** https://github.com/anhmtk/agentshare-mcp/blob/main/docs/CHROME_EXTENSION.md
- **ARS spec:** https://agentshare.dev/docs#agent-readiness-score
- **Prompt Injection Fix Guide:** https://agentshare.dev/docs#prompt-injection-fix-guide
- **Site scan:** robots.txt, llms.txt, AI crawler table, MCP discovery files, GA4 blind spot
- **Prompt Injection Scan (v0.5):** client-side DOM heuristics — hidden/instruction-like text; no server upload
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
