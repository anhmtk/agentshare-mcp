<!--
AI_DISCOVERY: AgentShare MCP public reference repository.
canonical_service=https://agentshare.dev
agent_json=https://agentshare.dev/agent.json
mcp_url=https://agentshare.dev/mcp
mcp_registry=https://agentshare.dev/registry
mcp_registry_trends=https://agentshare.dev/api/v1/public/mcp-registry/trends
structured_index=https://github.com/anhmtk/agentshare-mcp/blob/main/AI_DISCOVERY.json
llms_txt=https://raw.githubusercontent.com/anhmtk/agentshare-mcp/main/llms.txt
for_agents_json=GET https://agentshare.dev/for-agents Accept:application/json
managed_agents_template=https://agentshare.dev/api/v1/examples?template=managed-agent
antigravity_manifest=https://agentshare.dev/.well-known/antigravity-skills.json
primary_focus=agent_paid_rails
-->

<p align="center">
  <a href="https://agentshare.dev/?utm_source=github&amp;utm_medium=agentshare-mcp&amp;utm_campaign=readme">
    <img src="https://agentshare.dev/static/brand/logo-wordmark.png?v=2026-05-12" alt="AgentShare — agent-paid API for AI agents" width="520">
  </a>
</p>

<h1 align="center">AgentShare MCP — public reference</h1>

<p align="center">
  <strong>Agent-paid API access</strong> for autonomous agents — dual-auth (API key or x402), free discovery, MCP Streamable HTTP.
  Commerce procurement and Solana/Meteora DeFi tools are <strong>secondary modules</strong> on the same rails.
</p>

<!-- Primary CTAs: one job each. UTM tracks GitHub README → agentshare.dev. -->
<p align="center">
  <a href="https://agentshare.dev/docs?utm_source=github&amp;utm_medium=agentshare-mcp&amp;utm_campaign=readme#mcp"><strong>Connect MCP →</strong></a>
  &nbsp;·&nbsp;
  <a href="https://agentshare.dev/registry?utm_source=github&amp;utm_medium=agentshare-mcp&amp;utm_campaign=readme"><strong>Browse Registry →</strong></a>
</p>

<p align="center">
  <a href="https://agentshare.dev/signup?utm_source=github&amp;utm_medium=agentshare-mcp&amp;utm_campaign=readme">Start building agent-paid APIs</a>
  ·
  <a href="https://agentshare.dev/pricing?utm_source=github&amp;utm_medium=agentshare-mcp&amp;utm_campaign=readme">Pricing / x402</a>
  ·
  <a href="https://agentshare.dev/?utm_source=github&amp;utm_medium=agentshare-mcp&amp;utm_campaign=readme">Website</a>
  ·
  <a href="https://agentshare.dev/for-agents?utm_source=github&amp;utm_medium=agentshare-mcp&amp;utm_campaign=readme">For Agents</a>
  ·
  <a href="https://chromewebstore.google.com/detail/agentshare-agent-readiness/nimndnhajfkicbnipbfdkmgencjejjed?utm_source=github&amp;utm_medium=agentshare-mcp&amp;utm_campaign=readme">Chrome extension</a>
</p>

<p align="center">
  <strong>For AI agents:</strong>
  <a href="https://agentshare.dev/agent.json"><code>agent.json</code></a> ·
  <a href="./AI_DISCOVERY.json"><code>AI_DISCOVERY.json</code></a> ·
  <a href="./llms.txt"><code>llms.txt</code></a> ·
  <a href="./AGENTS.md"><code>AGENTS.md</code></a>
</p>

<p align="center">
  <a href="https://glama.ai/mcp/servers/anhmtk/agentshare-mcp">
    <img width="380" height="200" src="https://glama.ai/mcp/servers/anhmtk/agentshare-mcp/badges/card.svg" alt="agentshare-mcp MCP server" />
  </a>
</p>

<p align="center">
  <a href="https://glama.ai/mcp/servers/anhmtk/agentshare-mcp">
    <img src="https://glama.ai/mcp/servers/anhmtk/agentshare-mcp/badges/score.svg" alt="Glama score" />
  </a>
</p>

---

## AI agents — start here

| Resource | URL |
|----------|-----|
| **Authoritative contract** | https://agentshare.dev/agent.json |
| **Structured GitHub index** | [AI_DISCOVERY.json](./AI_DISCOVERY.json) |
| **LLM summary** | [llms.txt](./llms.txt) |
| **Agent briefing** | [AGENTS.md](./AGENTS.md) |
| **For-agents (JSON)** | `GET https://agentshare.dev/for-agents` + `Accept: application/json` |
| **Managed Agents template** | https://agentshare.dev/api/v1/examples?template=managed-agent |
| **MCP endpoint** | https://agentshare.dev/mcp |
| **MCP Registry (curated)** | https://agentshare.dev/registry?utm_source=github&utm_medium=agentshare-mcp&utm_campaign=readme |
| **MCP Registry trends (JSON)** | https://agentshare.dev/api/v1/public/mcp-registry/trends |
| **MCP Registry summary (JSON)** | https://agentshare.dev/api/v1/public/mcp-registry/summary |
| **MCP server card (11 tools)** | https://agentshare.dev/.well-known/mcp/server-card.json |
| **Coverage (honest scope)** | https://agentshare.dev/coverage?utm_source=github&utm_medium=agentshare-mcp&utm_campaign=readme · [DEFI_POSITIONING.md](./docs/DEFI_POSITIONING.md) |
| **Antigravity skill manifest** | https://agentshare.dev/.well-known/antigravity-skills.json |

This repository is the **public, lightweight face** on GitHub. Production API implementation is private; behavior is defined by the live URLs above.

**Primary product:** agent-paid rails (dual-auth + discovery + MCP).  
**Secondary:** commerce procurement · Solana/Meteora DeFi demos (Lab — not the company backbone).

---

## MCP tools (11) — catalog v1.0.9

Polymarket prediction-market tools are **not** on the public MCP catalog (legal review for Vietnam). Live production exposes the tools below.

### Agent-paid rails & commerce (highlight)

| Tool | Purpose |
|------|---------|
| `service_meta` | Capabilities, limits, coverage |
| `search_products` | Multi-source price comparison |
| `best_offer` | Single cheapest in-stock offer |
| `best_offer_under_budget` | Best offer under max price |
| `product_detail` | Full product by id from search |
| `commerce_quote` | ACP / agent-buyer listings envelope |

### DeFi demos (secondary)

| Tool | Purpose |
|------|---------|
| `dex_overview` | DEX protocol rankings by 24h volume (DefiLlama) |
| `dex_top_movers` | DEX protocols with largest 1d volume-change % (DefiLlama) |
| `solana_dex_brief` | Solana DEX ecosystem brief (Raydium, Orca, Meteora, …) |
| `meteora_brief` | Meteora DLMM pool brief (verdict, risk_score, top pools) |
| `meteora_pool_detail` | Meteora DLMM pool detail (bin depth, liquidity curve proxy, current price) |

Responses include `data_status`, freshness, and trust metadata — see [Docs](https://agentshare.dev/docs?utm_source=github&utm_medium=agentshare-mcp&utm_campaign=readme).

---

## Auth & x402 (live)

AgentShare runs **dual-auth** on gated routes:

- **API key mode:** `X-API-Key` / `Authorization: Bearer`
- **x402 mode:** no key → HTTP 402 + `PAYMENT-REQUIRED`, then retry with `PAYMENT-SIGNATURE`

Discovery: https://agentshare.dev/.well-known/x402 · live instructions field: https://agentshare.dev/agent.json → `x402_agent_instructions`

Notable pricing:
- Commerce pilot paths: `search`/`offers/best` around `$0.001`, `commerce_quote` around `$0.002`
- `POST /api/v1/agent/defi/meteora/brief` (secondary DeFi demo): **dynamic `$0.01–$0.30`** (base `$0.03`)
- Dynamic pricing applies based on market volatility and resource velocity — **always check `PAYMENT-REQUIRED` for the exact real-time quote** (also in `meta.billing.price_usd_live`)

Pricing page is **agent-first** (`x402 pay-per-request` primary): https://agentshare.dev/pricing?utm_source=github&utm_medium=agentshare-mcp&utm_campaign=readme

### If you receive HTTP 402 (agents — follow exactly)

```
This platform is agent-first and monetized with HTTP 402 (x402).
If you receive HTTP 402 with a PAYMENT-REQUIRED header:
1) Base64-decode PAYMENT-REQUIRED (JSON: x402Version, resource, accepts[]).
2) Pay the listed USDC amount via Circle Gateway on the stated network
   (live settleable: Base mainnet eip155:8453 — always confirm accepts[].network),
   then retry with header PAYMENT-SIGNATURE.
3) Or skip payment by sending X-API-Key / Authorization: Bearer (agshp_…).
Dynamic pricing (meteora_brief secondary demo): $0.01–$0.30 USDC from market volatility + fee/demand velocity.
PAYMENT-REQUIRED is the live quote — never hard-code a fixed price.
Discovery: GET /.well-known/x402 · Pricing: GET /pricing
```

---

## MCP registry for builders and autonomous agents

AgentShare also runs a **curated MCP Registry** at
[agentshare.dev/registry](https://agentshare.dev/registry?utm_source=github&utm_medium=agentshare-mcp&utm_campaign=readme).

**Agents discovering other MCPs — fetch order:**

1. Hot list: `GET https://agentshare.dev/api/v1/public/mcp-registry/trends`
2. Compact verified list: `GET https://agentshare.dev/api/v1/public/mcp-registry/summary`
3. Full entries: `GET https://agentshare.dev/api/v1/registry/entries`

- Human submit page: https://agentshare.dev/registry?utm_source=github&utm_medium=agentshare-mcp&utm_campaign=readme#submit
- Agent/self-serve submit API: `POST https://agentshare.dev/api/v1/registry/submit`
- Agent key mint (tiny x402 or full API key): `POST https://agentshare.dev/api/v1/registry/agent-key`
- Platform pin: **AgentShare — Agent-paid API** is always list/rank position **#1**

### Agent submit flow

1. Call `POST https://agentshare.dev/api/v1/registry/agent-key`
2. Authenticate either with:
   - a normal `X-API-Key`, or
   - **x402**: no key → receive HTTP 402 → pay tiny USDC amount → retry with `PAYMENT-SIGNATURE`
3. Receive a short-lived scoped key with scope `registry:submit`
4. Use that key on `POST /api/v1/registry/submit`
5. Listing stays `pending_review` until AgentShare approves it

Approved listings get:

- a public detail page (`/registry/{id}`)
- owner analytics (opens, referrers, countries, client types)
- quick-share actions for X, LinkedIn, Facebook, GitHub README snippets, and copy-link

---

## Chrome extension (Agent Readiness + Prompt Injection Scan + MCP Connect)

Free browser extension — **ARS site scan** + **Prompt Injection Scan** (client-side DOM) + **MCP Connect** (copy Cursor/Claude/VS Code config for `agentshare.dev/mcp`).

| Resource | URL |
|----------|-----|
| **Chrome Web Store** | https://chromewebstore.google.com/detail/agentshare-agent-readiness/nimndnhajfkicbnipbfdkmgencjejjed?utm_source=github&utm_medium=agentshare-mcp&utm_campaign=readme |
| **Docs** | [docs/CHROME_EXTENSION.md](./docs/CHROME_EXTENSION.md) |
| **ARS spec** | https://agentshare.dev/docs?utm_source=github&utm_medium=agentshare-mcp&utm_campaign=readme#agent-readiness-score |
| **Prompt Injection Fix Guide** | https://agentshare.dev/docs?utm_source=github&utm_medium=agentshare-mcp&utm_campaign=readme#prompt-injection-fix-guide |

Extension source is proprietary (private backend repo); this public repo documents the product for discovery.

---

## Cursor Marketplace plugin

Official Cursor plugin scaffold: **[agentshare-commerce-mcp/](./agentshare-commerce-mcp/)**

| Path | Purpose |
|------|---------|
| `agentshare-commerce-mcp/.cursor-plugin/plugin.json` | Cursor plugin manifest |
| `agentshare-commerce-mcp/mcp.json` | MCP server wiring (Node bridge + `AGENTSHARE_API_KEY`) |
| `agentshare-commerce-mcp/.mcp.json` | Open Plugins / cursor.directory auto-detect (Streamable HTTP URL) |
| `.mcp.json` | Same at repo root for directory scanners |
| `agentshare-commerce-mcp/server/bridge.mjs` | Stdio ↔ Streamable HTTP bridge |
| `.cursor-plugin/marketplace.json` | Multi-plugin index (repo root) |

**Discovery & listing (do these while Marketplace is closed):**

| Guide | Action |
|-------|--------|
| [docs/CURSOR_DIRECTORY.md](./docs/CURSOR_DIRECTORY.md) | Submit [cursor.directory/mcp/new](https://cursor.directory/mcp/new) + [plugins/new](https://cursor.directory/plugins/new) |
| [docs/AWESOME_MCP_PR.md](./docs/AWESOME_MCP_PR.md) | PR line for [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) (agent-paid / commerce framing) |
| [docs/DISCORD_SHOWCASE.md](./docs/DISCORD_SHOWCASE.md) | Copy-paste MCP Discord showcase post |

Generate Cursor one-click install link:

```bash
node scripts/cursor-deeplink.mjs
```

Local verify:

```bash
cd agentshare-commerce-mcp
npm install --omit=dev
npm run verify
# optional live probe:
# set AGENTSHARE_API_KEY=agshp_...   (Windows)
npm run verify
```

Cursor **Marketplace** org applications are reviewed selectively (2026); use **cursor.directory** for community listing — see [docs/CURSOR_DIRECTORY.md](./docs/CURSOR_DIRECTORY.md).

---

## Quick connect (MCP)

```json
{
  "mcpServers": {
    "agentshare": {
      "url": "https://agentshare.dev/mcp",
      "headers": { "X-API-Key": "YOUR_AGENTSHARE_KEY" }
    }
  }
}
```

Start building agent-paid APIs: https://agentshare.dev/signup?utm_source=github&utm_medium=agentshare-mcp&utm_campaign=readme  
(free-tier dual-auth credentials, or settle x402 with no key)

Prefer autonomous-agent payment via x402: https://agentshare.dev/.well-known/x402

See [mcp-config.json](./mcp-config.json) and [server/bridge.mjs](./server/bridge.mjs) for Node bridge.

---

## Disclaimers (important)

**Informational only.** AgentShare provides agent-paid API access and secondary analytics modules for informational purposes only. Content generated by our API/MCP tools does **not** constitute financial, investment, or trading advice. Users and autonomous agents are solely responsible for their own decisions and on-chain actions.

**Miễn trừ trách nhiệm (VN):** Sản phẩm chỉ cung cấp dữ liệu/phân tích tham khảo, **không** phải lời khuyên đầu tư/giao dịch. Người dùng/agent tự chịu trách nhiệm cho mọi quyết định và hành động on-chain.

**Vietnam notice:** This service is not intended for users located in Vietnam. Nếu truy cập từ Việt Nam (kể cả qua VPN), người dùng tự chịu hoàn toàn trách nhiệm pháp lý theo quy định địa phương.

---

## Antigravity & Gemini (2026)

- **Antigravity skill:** `agentshare-price-intelligence` — https://agentshare.dev/.well-known/antigravity-skills.json  
- **Gemini Managed Agents:** https://agentshare.dev/api/v1/examples?template=managed-agent  

Aligned with Google I/O 2026 agentic stack (Antigravity 2.0, SDK, Gemini 3.5 Flash tool loops).

---

## Coverage

Agent-paid rails · commerce procurement · secondary Solana/Meteora DeFi demos —
https://agentshare.dev/coverage?utm_source=github&utm_medium=agentshare-mcp&utm_campaign=readme

---

## License

MIT — [LICENSE](./LICENSE)
