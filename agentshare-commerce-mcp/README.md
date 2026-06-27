# AgentShare — AI Commerce Price MCP

Connect Cursor to **live marketplace price intelligence** for AI agents. Search products, find the best offer, run budget-constrained procurement quotes, and drill into product details—all through MCP tools backed by [agentshare.dev](https://agentshare.dev).

**Free tier:** [Sign up](https://agentshare.dev/signup) for **100 API requests/month** (no credit card).

---

## Features

### Commerce & pricing tools

| Tool | Description |
|------|-------------|
| **`search_products`** | Search connected marketplaces; returns structured listings with prices, sources, URLs, and freshness metadata. Best for comparing multiple options. |
| **`best_offer`** | Return the single best current offer (typically lowest price among in-stock listings the API trusts). |
| **`best_offer_under_budget`** | Best offer within a maximum price you specify. |
| **`product_detail`** | Full product details and per-source prices by numeric `product_id` from a prior search. |
| **`commerce_quote`** | **ACP / agent-buyer** quote envelope (`agentshare.price.v1`). Use `mode=search` for multiple listings or `mode=best_offer` for one pick; optional `max_price_usd` for budget agents. |
| **`service_meta`** | API capabilities, rate limits, and integration hints (calls public `GET /api/v1/meta`). |

### Macro scout (optional context)

| Tool | Description |
|------|-------------|
| **`dex_overview`** | Rank decentralized exchange protocols by 24h volume (DefiLlama). |
| **`dex_top_movers`** | DEX protocols with the largest absolute 1d volume change %. |

### Response format (every price tool)

Each tool returns **two MCP text blocks**:

1. **Summary** — One line in English, e.g. `Search: 5 listing(s) — freshness: fresh — data_status=fresh — trust=71% (n=40)`.
2. **JSON envelope** — Full payload mirroring REST: `status`, `data`, `meta` (includes `mcp_format_version`, `data_status`, trust fields when available).

Agents can parse block 2 programmatically; humans read block 1 in the chat.

### Data quality signals

- **`data_status`** — Freshness / quality hint (`fresh`, `stale`, etc.).
- **`freshness_status` / `data_age_seconds`** — How old the underlying crawl is.
- **`no_data` / `pending_crawl`** — Honest empty state instead of invented prices.
- **Coverage** — Product scope is defined at [agentshare.dev/coverage](https://agentshare.dev/coverage).

---

## How to install

### From Cursor Marketplace (recommended)

1. Open **Cursor** → **Customize** (left sidebar) → **Plugins** or **MCP**.
2. Search for **AgentShare** or **AI Commerce Price MCP**.
3. Click **Install**.
4. When prompted, paste your **AgentShare API key** (`agshp_…` from [signup](https://agentshare.dev/signup)).
5. Confirm MCP status is **Connected** and **8 tools** are listed.

### Manual MCP setup (Customize → Add MCP server)

**Option A — Streamable HTTP (fastest)**

| Field | Value |
|-------|--------|
| **URL** | `https://agentshare.dev/mcp` |
| **Header** | `X-API-Key: agshp_YOUR_KEY` |

Or: `Authorization: Bearer agshp_YOUR_KEY`

**Option B — Node bridge (if HTTP/OAuth is flaky)**

Requires **Node.js 18+**. From this plugin directory:

```bash
npm install --omit=dev
node server/bridge.mjs https://agentshare.dev/mcp --header X-API-Key:agshp_YOUR_KEY
```

In **Customize → MCP → Add server** (when installing manually from Git clone):

| Field | Value |
|-------|--------|
| **Command** | `node` |
| **Args** | `server/bridge.mjs` `https://agentshare.dev/mcp` `--header` `X-API-Key:agshp_YOUR_KEY` |
| **Cwd** | Path to this `agentshare-commerce-mcp/` folder |

Or set env **`AGENTSHARE_API_KEY`** and use the bundled `mcp.json` (see repo root `.cursor-plugin/marketplace.json`).

### Verify installation

1. Open **Agent** chat.
2. Ask: *"Call service_meta and summarize capabilities."*
3. You should see a successful tool call and JSON metadata.

---

## Authentication

### Get an API key

1. Go to [agentshare.dev/signup](https://agentshare.dev/signup).
2. Complete signup (email verification if enabled).
3. Copy your key — it starts with **`agshp_`**.
4. Store it in Cursor plugin settings or MCP headers — **never commit it to Git**.

### How the key is used

- Sent on **every** MCP request as `X-API-Key` (or `Authorization: Bearer`).
- Tied to your **monthly quota** (100 free requests/month on the free plan).
- Revoke or rotate keys from your AgentShare account dashboard if compromised.

### Errors you may see

| Symptom | Action |
|---------|--------|
| `401` / `MISSING_API_KEY` | Add header or env `AGENTSHARE_API_KEY` in plugin settings. |
| `401` / `INVALID_API_KEY` | Regenerate key at signup; check for typos or extra spaces. |
| `monthly_quota_exceeded` | Upgrade at [agentshare.dev/pricing](https://agentshare.dev/pricing) or wait for monthly reset. |
| Empty / `pending_crawl` | Normal for new SKUs; try `search_products` with broader keywords or check [coverage](https://agentshare.dev/coverage). |

---

## Example prompts

Paste these into **Cursor Agent** chat after MCP is connected.

### 1. Budget procurement (single best offer)

```text
You are a procurement agent. Use AgentShare MCP only.

Find the best in-stock offer for "Raspberry Pi 5 8GB kit" under $120 USD.
Call commerce_quote with mode=best_offer, max_price_usd=120, currency=USD.

Reply with: product title, price, data_status, and affiliate_url.
If no_data or pending_crawl, call search_products with limit=5 and summarize alternatives.
```

### 2. Compare multiple listings

```text
Compare prices for "LiPo 3S 5000mAh" drone batteries.

Use commerce_quote with mode=search, limit=8, currency=USD.

Return a table: title | price | source | data_status | link.
Recommend one pick and explain why (price + freshness).
```

### 3. Search then drill into product detail

```text
1) Call search_products with query="mini PC 16GB RAM" and limit=5.
2) Pick the listing with the best data_status (prefer fresh).
3) Call product_detail with that product_id and currency=USD.
4) Summarize for a purchase approval memo (specs, price, link).
```

### 4. Quick capability check

```text
Call service_meta and list which commerce tools I should use for hardware price comparison vs single-SKU best price.
```

---

## Tool selection guide

| User intent | Preferred tool |
|-------------|----------------|
| "Compare options" / "show me listings" | `search_products` or `commerce_quote` (`mode=search`) |
| "Cheapest" / "where to buy" | `best_offer` or `commerce_quote` (`mode=best_offer`) |
| "Under $X" / budget cap | `best_offer_under_budget` or `commerce_quote` + `max_price_usd` |
| "Tell me more about listing #3" | `product_detail` with `product_id` from search |
| "What can this API do?" | `service_meta` |

---

## Requirements

- **Cursor** 3.8+ with MCP / Customize support (recommended).
- **Network** access to `https://agentshare.dev`.
- **Node.js 18+** only if using the Node bridge install path.
- **AgentShare API key** (`agshp_…`).

---

## Links

| Resource | URL |
|----------|-----|
| Website | [agentshare.dev](https://agentshare.dev) |
| Signup / API key | [agentshare.dev/signup](https://agentshare.dev/signup) |
| Pricing | [agentshare.dev/pricing](https://agentshare.dev/pricing) |
| Coverage (data scope) | [agentshare.dev/coverage](https://agentshare.dev/coverage) |
| OpenAPI | [agentshare.dev/openapi.json](https://agentshare.dev/openapi.json) |
| MCP catalog | [agentshare.dev/mcp.json](https://agentshare.dev/mcp.json) |
| Server card (tools + schemas) | [agentshare.dev/.well-known/mcp/server-card.json](https://agentshare.dev/.well-known/mcp/server-card.json) |
| Full docs | [agentshare.dev/docs](https://agentshare.dev/docs) |
| Issues | [github.com/anhmtk/agentshare-mcp/issues](https://github.com/anhmtk/agentshare-mcp/issues) |

---

## Privacy & affiliate disclosure

Price responses may include **merchant URLs** with **affiliate or tracking parameters** when affiliate programs are active. See [Terms](https://agentshare.dev/terms) and [Privacy](https://agentshare.dev/privacy). Your API key identifies your account for quota and billing only—it is not shared with marketplaces.

---

## License

MIT — see repository `LICENSE`.
