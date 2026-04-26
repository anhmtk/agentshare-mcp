# AgentShare — AI Agent Briefing

**Repository:** [agentshare-mcp](https://github.com/anhmtk/agentshare-mcp) — stdio MCP server that proxies [Agent Price API](https://agentshare.dev) tools. **Implementation path:** `integrations/mcp_server/` (see `price_mcp.py`).

---

## Mission

Provide **structured, production-grade price and offer data** for AI agents, over **MCP** (stdio or Streamable HTTP) and the underlying **REST** API.

---

## Capabilities (MCP tools)

These are the **registered tool names** in this codebase. They map to REST as shown.

| Intent | MCP tool name | REST (behind the tool) |
|--------|-----------------|------------------------|
| Search products by keyword (multi-listing, comparison) | `search_products` | `GET /api/v1/search` |
| Single best in-stock offer for a product intent | `best_offer` | `GET /api/v1/offers/best` |
| Best offer under a max price (budget) | `best_offer_under_budget` | `GET /api/v1/offers/best-under-budget` |
| Discovery: capabilities, limits, no paid tools required when deployment allows | `service_meta` | `GET /api/v1/meta` |

**Response shape:** every tool returns **two** `text` parts: a **one-line English summary**, then a **JSON envelope** with `status` (`ok` / `error`), `data` (when successful), and `meta` (including `mcp_format_version`, and **reliability fields** from the API when present).

---

## Reliability signals (from API → MCP envelope)

- **`freshness_status`** — e.g. `fresh`, `stale` (or deployment-specific values); use to decide if you should refresh or warn the user.
- **`data_age_seconds`** — time since the underlying listing data was observed (per offer or per response `meta`).

**Operational note:** Client-side **health / smoke** runs have been exercised at **~200 requests** with **100% client-observed success** against the public deployment. Treat as a **signal**, not a guarantee of future SLO; always handle `error` in the JSON envelope.

---

## Authentication

- **REST and priced MCP tools:** send **`X-API-Key: <your key>`** (or `Authorization: Bearer <token>` where supported by the client).
- **stdio MCP:** set env `API_KEY` (or `X_API_KEY` / `X-API-Key` as supported by the loader) and optional `BASE_URL` (default `https://agentshare.dev`).
- **Get a key:** https://agentshare.dev/pricing

---

## OpenAPI (machine-readable contract)

- **In this repo (MCP-handy subset, generated from the same paths as the MCP client):** [`openapi.json`](./openapi.json)
- **Canonical full API (live):** https://agentshare.dev/openapi.json

---

## MCP config (copy-paste)

**Claude Desktop / Cursor (remote via `mcp-remote`):** see [`mcp-config.json`](./mcp-config.json) in this repo, or use:

```json
{
  "mcpServers": {
    "agentshare": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://agentshare.dev/mcp",
        "--header",
        "X-API-Key: YOUR_API_KEY"
      ]
    }
  }
}
```

Replace `YOUR_API_KEY` with your key. For **local stdio** (no `npx`), use `python` + `integrations/mcp_server/server.py` — see [README](README.md).

**Streamable HTTP URL:** `https://agentshare.dev/mcp` (trailing slash optional for many clients).

---

## Trust & safety

- Do not commit real API keys, `.env`, or tokens. Use `.env` locally; see `integrations/mcp_server/.env.example`.
- For terms and privacy: https://agentshare.dev/terms · https://agentshare.dev/privacy

---

## Project layout (for code navigation)

| Path | Role |
|------|------|
| `integrations/mcp_server/price_mcp.py` | Tool definitions and REST calls |
| `integrations/mcp_server/mcp_tool_format.py` | Summary + JSON envelope, error mapping |
| `integrations/mcp_server/server.py` | stdio entrypoint |
| `examples/` | Minimal REST examples |
