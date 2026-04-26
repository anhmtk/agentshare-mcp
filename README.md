# AgentShare

![Production Ready](https://img.shields.io/badge/status-production--ready-brightgreen)
[![MCP Server](https://img.shields.io/badge/MCP-Streamable%20HTTP-5C6BC0?style=flat)](https://agentshare.dev/mcp/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![REST API](https://img.shields.io/badge/API-agentshare.dev-20BE86?style=flat)](https://agentshare.dev/openapi.json)
[![Docs](https://img.shields.io/badge/docs-agentshare.dev-5865F2?style=flat)](https://agentshare.dev/docs)

**Structured marketplace prices and offers for AI agents** — REST API and [MCP (Streamable HTTP)](https://agentshare.dev/mcp/).

| | |
|---|---|
| **Site & docs** | https://agentshare.dev |
| **MCP endpoint** | `https://agentshare.dev/mcp/` |
| **Discovery** | [`/agent.json`](https://agentshare.dev/agent.json) · [`/mcp.json`](https://agentshare.dev/mcp.json) · [`llm.txt`](https://agentshare.dev/llm.txt) / [`llms.txt`](https://agentshare.dev/llms.txt) |

This repository holds the **stdio MCP server** used with Claude Desktop, Cursor, and other MCP clients, plus **minimal REST examples**. The live API and full integration guides are on the site above.

---

## For AI agents (machine readable)

- **[`AGENTS.md`](AGENTS.md)** — mission, tool names, auth, response envelope, copy-paste MCP JSON, and links to OpenAPI.
- **[`openapi.json`](openapi.json)** — OpenAPI 3.0 spec for the **REST surface used by this MCP** (`/api/v1/search`, `/offers/*`, `/meta`). The **full** production spec (all routes) is always at **https://agentshare.dev/openapi.json**.
- **[`mcp-config.json`](mcp-config.json)** — ready-to-paste `mcpServers` block for **`npx mcp-remote`** (Claude Desktop / Cursor) pointing at the remote Streamable HTTP endpoint.

---

## For humans: quick install (pip)

```bash
git clone https://github.com/anhmtk/agentshare-mcp.git
cd agentshare-mcp
pip install -r integrations/mcp_server/requirements.txt
export API_KEY=your_api_key   # Windows: $env:API_KEY="..."
# optional: export BASE_URL=https://agentshare.dev
python integrations/mcp_server/server.py
```

Get a key: https://agentshare.dev/pricing

---

## Quick install — Claude Desktop (`claude_desktop_config.json`)

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

- Get a key: https://agentshare.dev/pricing  
- On Windows, prefer forward slashes in `args`, e.g. `D:/code/agentshare-mcp/integrations/mcp_server/server.py`.

**Remote MCP (Streamable HTTP):** clients that support URL + API key headers can use `https://agentshare.dev/mcp/` with `X-API-Key` or `Authorization: Bearer`. Use **[`mcp-config.json`](mcp-config.json)** for **`npx mcp-remote`**. Details: [MCP Quickstart](https://agentshare.dev/docs) (section MCP).

**Advanced — HTTP via `mcp-remote` (Node / npx):** if you use [`mcp-remote`](https://github.com/geelen/mcp-remote) to bridge HTTPS → stdio, pass your key with `--header` (see troubleshooting in [Cursor MCP setup](https://agentshare.dev/docs)); this repo does **not** publish an `npx agentshare-mcp` package.

---

## Clone & run the stdio MCP locally

From the repo root:

```bash
pip install -r integrations/mcp_server/requirements.txt
export API_KEY=your_api_key
# optional: export BASE_URL=http://localhost:8000
python integrations/mcp_server/server.py
```

Same as `python integrations/mcp_server/run.py`. See [`integrations/mcp_server/README.md`](integrations/mcp_server/README.md) for tools and env.

---

## Code examples (REST)

The [`examples/`](examples/) folder has small scripts that call the public JSON API (`GET /api/v1/search`, …). Useful for testing a key before wiring MCP.

---

## MCP directories & listings

Production discovery (no auth) — use these URLs when submitting to catalogs:

| Resource | URL |
|----------|-----|
| `mcp.json` | https://agentshare.dev/mcp.json |
| `agent.json` | https://agentshare.dev/agent.json |
| Server card (Smithery-style) | https://agentshare.dev/.well-known/mcp/server-card.json |

Third-party indexes (search for **AgentShare** or your listing URL):

- [Smithery](https://smithery.ai/) — MCP server registry  
- [Glama](https://glama.ai/) — MCP / AI gateway directory  

---

## License

MIT — see [LICENSE](LICENSE).

## GitHub — CI & repo traffic

- **CI:** validates MCP package imports on push/PR — **Actions** → **CI**.
- **Traffic:** GitHub shows aggregate views/clones only (**Insights → Traffic** for maintainers). Weekly **GitHub traffic snapshot** writes API results to the run **Summary** (same idea as Insights).

---

### Scope (honest & forward-looking)

AgentShare aggregates product and offer data from **connected marketplaces and affiliate sources**. Coverage and freshness vary by source; the API returns **freshness metadata** (e.g. `crawled_at`, `data_age_seconds`, `freshness_status`) so agents can judge reliability.

**Direction:** expand toward **global e‑commerce** and major international marketplaces as integrations mature. For the **current** focus, see **`GET /coverage`**: https://agentshare.dev/coverage

---

### Legal

Terms and privacy: https://agentshare.dev/terms · https://agentshare.dev/privacy
