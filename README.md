# AgentShare

![Production Ready](https://img.shields.io/badge/status-production--ready-brightgreen)
[![MCP Server](https://img.shields.io/badge/MCP-Streamable%20HTTP-5C6BC0?style=flat)](https://agentshare.dev/mcp/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![REST API](https://img.shields.io/badge/API-agentshare.dev-20BE86?style=flat)](https://agentshare.dev/openapi.json)
[![Docs](https://img.shields.io/badge/docs-agentshare.dev-5865F2?style=flat)](https://agentshare.dev/docs)

## Description

**AgentShare** provides **structured marketplace prices and offers for AI agents** via a JSON **REST API** and **MCP** ([Streamable HTTP](https://agentshare.dev/mcp/)). This repository contains the **stdio MCP server** (Python) used with Claude Desktop, Cursor, and other MCP clients, plus minimal REST examples. The production API, pricing, and full docs live at **https://agentshare.dev**.

All MCP tools are **read-only**: they fetch data from the AgentShare API and do not modify your accounts or remote marketplace listings.

| | |
|---|---|
| **Site & docs** | https://agentshare.dev |
| **MCP endpoint (remote)** | `https://agentshare.dev/mcp/` |
| **Discovery** | [`/agent.json`](https://agentshare.dev/agent.json) · [`/mcp.json`](https://agentshare.dev/mcp.json) · [`llm.txt`](https://agentshare.dev/llm.txt) / [`llms.txt`](https://agentshare.dev/llms.txt) |

---

## For AI agents (machine readable)

- **[`AGENTS.md`](AGENTS.md)** — mission, tool names, auth, response envelope, copy-paste MCP JSON, and links to OpenAPI.
- **[`llms.txt`](llms.txt)** — same essentials in a **short, crawl-friendly** single file (for LLM / GEO workflows).
- **[`openapi.json`](openapi.json)** — OpenAPI 3.0 spec for the **REST surface used by this MCP** (`/api/v1/search`, `/offers/*`, `/meta`). The **full** production spec (all routes) is always at **https://agentshare.dev/openapi.json** (single source of truth; no duplicate docs repo).
- **[`mcp-config.json`](mcp-config.json)** — ready-to-paste `mcpServers` block for **`npx mcp-remote`** (Claude Desktop / Cursor) pointing at the remote Streamable HTTP endpoint.

---

## Features

- **`search_products`** — Multi-listing product search with prices, sources, and freshness metadata (`readOnlyHint: true`).
- **`best_offer`** — Single best in-stock-style offer for a product intent (`readOnlyHint: true`).
- **`best_offer_under_budget`** — Best offer under a price ceiling (`readOnlyHint: true`).
- **`service_meta`** — API capabilities and limits; safe for discovery (`readOnlyHint: true`).
- **Official AliExpress integration** on the production API; additional leading marketplaces are added when partnerships and policy allow.
- **Freshness metadata** in responses (e.g. `data_age_seconds`, `freshness_status`) for agent reasoning.
- **Affiliate-ready URLs** where configured; see Terms and Privacy on the site.

---

## Getting an API key

To use this MCP server or the REST API, you need an API key. Visit [https://agentshare.dev/pricing](https://agentshare.dev/pricing) to get your free tier key (**100 requests / month** on the public free plan at time of writing — always confirm on the site).

---

## Installation

### Quick install (pip)

```bash
git clone https://github.com/anhmtk/agentshare-mcp.git
cd agentshare-mcp
pip install -r integrations/mcp_server/requirements.txt
export API_KEY=your_api_key   # Windows: $env:API_KEY="..."
# optional: export BASE_URL=https://agentshare.dev
python integrations/mcp_server/server.py
```

Get a key: https://agentshare.dev/pricing

### Claude Desktop (`claude_desktop_config.json`) — stdio

Use a **local stdio** server (Python). Replace the path with the **absolute** path to `server.py` in *your* clone of this repo.

```json
{
  "mcpServers": {
    "agentshare": {
      "command": "python",
      "args": ["/ABSOLUTE/PATH/TO/agentshare-mcp/integrations/mcp_server/server.py"],
      "env": {
        "API_KEY": "your-api-key-here",
        "BASE_URL": "https://agentshare.dev"
      }
    }
  }
}
```

- On Windows, prefer forward slashes in `args`, e.g. `D:/code/agentshare-mcp/integrations/mcp_server/server.py`.

**Remote MCP (Streamable HTTP):** clients that support URL + API key headers can use `https://agentshare.dev/mcp/` with `X-API-Key` or `Authorization: Bearer`. Use **[`mcp-config.json`](mcp-config.json)** for **`npx mcp-remote`**. Details: [MCP Quickstart](https://agentshare.dev/docs) (section MCP).

**Advanced — HTTP via `mcp-remote` (Node / npx):** if you use [`mcp-remote`](https://github.com/geelen/mcp-remote) to bridge HTTPS → stdio, pass your key with `--header` (see troubleshooting in [Cursor MCP setup](https://agentshare.dev/docs)); this repo does **not** publish an `npx agentshare-mcp` package.

The official **Claude Desktop Extension** (`.mcpb`) uses a small Node **bridge** (see the **agent-price-api** repo, `mcpb-bundle/agentshare-price-mcp`) and does **not** rely on `mcp-remote`.

### Clone & run stdio locally

```bash
pip install -r integrations/mcp_server/requirements.txt
export API_KEY=your_api_key
# optional: export BASE_URL=http://localhost:8000
python integrations/mcp_server/server.py
```

Same as `python integrations/mcp_server/run.py`. See [`integrations/mcp_server/README.md`](integrations/mcp_server/README.md) for tools and environment variables.

### Claude Desktop Extension (`.mcpb`)

A packaged extension (**AgentShare — Real-time Price & Offer MCP**) can be installed from the `.mcpb` built in the main **agent-price-api** repo (`mcpb-bundle/agentshare-price-mcp`). That bundle connects to `https://agentshare.dev/mcp` via a small Node bridge. See [MCP Quickstart](https://agentshare.dev/docs) on the site.

---

## Configuration

### Environment variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `API_KEY` | For price tools | — | Sent as `X-API-Key` to the API |
| `BASE_URL` | No | `https://agentshare.dev` | API base URL (e.g. local dev) |
| `MCP_UPSTREAM_TIMEOUT_SEC` | No | `120` | HTTP timeout for upstream API calls |

**Remote MCP (Streamable HTTP):** clients that support URL + headers can call `https://agentshare.dev/mcp/` with `X-API-Key` or `Authorization: Bearer`. Details: [docs](https://agentshare.dev/docs) (MCP section).

---

## Examples

### Example 1: Search for product prices

**User prompt:** “Find me the current price of a Raspberry Pi 5 in Vietnam.”

**Expected behavior:** The assistant uses the **`search_products`** tool. The AgentShare API returns listings from connected sources with prices and freshness metadata.

**Expected output:** A list of offers with source identifier, price (typically in **VND** in API payloads), stock hints when available, and **freshness** fields so the agent can caveat recency.

### Example 2: Best single offer

**User prompt:** “What’s the cheapest NVIDIA Jetson Orin Nano I can buy right now?”

**Expected behavior:** The assistant uses **`best_offer`**. The API returns the single lowest-priced offer the service selects as best, with link and metadata.

**Expected output:** One primary offer: marketplace/source, price, URL, and freshness/stock context where available.

### Example 3: Budget-constrained search

**User prompt:** “I have 2 million VND. Show me the best mini PC I can get.”

**Expected behavior:** The assistant uses **`best_offer_under_budget`** with `max_price=2000000` (VND scale for the deployed API).

**Expected output:** The best offer within budget, or a clear **no match** / **out of budget** style result with reasoning fields from the JSON.

---

## Privacy Policy (extension & API use)

This MCP client requires an **AgentShare API key**. For **Claude Desktop Extensions (`.mcpb`)**, the key is stored in **Claude Desktop’s secure storage** and sent only to **https://agentshare.dev** (or your `BASE_URL`) as **`X-API-Key`** for authenticated endpoints.

**Data collection**

- This repository’s MCP server **does not** add its own analytics or telemetry beyond what your MCP host provides.
- **Search queries and API parameters** are sent to AgentShare to retrieve results.
- AgentShare may log requests for **rate limiting, billing, abuse prevention, and operations** as described on the site.

**Data sharing**

- Data is processed by **AgentShare** to fulfill the API request. AgentShare does not sell personal data from the API for marketing. Details are in the full policy below.

**Retention & full policy**

- Log retention and categories (e.g. API logs) are defined in the **published** privacy policy. **Authoritative text:** **https://agentshare.dev/privacy**

**Terms**

- **https://agentshare.dev/terms**

---

## Support

- **Issues:** [GitHub Issues](https://github.com/anhmtk/agentshare-mcp/issues)
- **Email:** admin@agentshare.dev
- **Website / docs:** https://agentshare.dev · https://agentshare.dev/docs

---

## Code examples (REST)

The [`examples/`](examples/) folder has small scripts that call the public JSON API (`GET /api/v1/search`, …). Useful for testing a key before wiring MCP.

---

## MCP directories & listings

Production discovery (no auth):

| Resource | URL |
|----------|-----|
| `mcp.json` | https://agentshare.dev/mcp.json |
| `agent.json` | https://agentshare.dev/agent.json |
| Server card | https://agentshare.dev/.well-known/mcp/server-card.json |

Third-party indexes (search for **AgentShare** or your listing URL):

- [Smithery](https://smithery.ai/) — MCP server registry  
- [Glama](https://glama.ai/) — MCP / AI gateway directory  

---

## License

MIT — see [LICENSE](LICENSE).

### Scope (honest & forward-looking)

AgentShare aggregates product and offer data from **connected marketplaces and affiliate sources**. Coverage and freshness vary by source; the API returns **freshness metadata** (e.g. `crawled_at`, `data_age_seconds`, `freshness_status`) so agents can judge reliability.

**Direction:** expand toward **global e‑commerce** as integrations mature. Current product focus: **`GET /coverage`** — https://agentshare.dev/coverage

---

## GitHub — CI & repo traffic

- **CI:** validates MCP package imports on push/PR — **Actions** → **CI**.
- **Traffic:** **Insights → Traffic** (maintainers). Weekly snapshots may be posted to run **Summary** from **github-traffic** workflow.
