<p align="center">
  <a href="https://agentshare.dev">
    <img src="https://agentshare.dev/static/brand/logo-wordmark.png?v=2026-05-12" alt="AgentShare — Price API + MCP for AI agents" width="520">
  </a>
</p>

<h1 align="center">AgentShare MCP Server</h1>

<p align="center">
  The data layer for agent commerce — structured price and offer data for AI agents,
  over MCP Streamable HTTP and REST.
</p>

<p align="center">
  <a href="https://agentshare.dev"><strong>Website</strong></a> ·
  <a href="https://agentshare.dev/docs"><strong>Docs</strong></a> ·
  <a href="https://agentshare.dev/pricing"><strong>Pricing</strong></a> ·
  <a href="https://agentshare.dev/signup"><strong>Get free API key</strong></a>
</p>

---

## What it does

Exposes the [AgentShare Price API](https://agentshare.dev) as **four MCP tools** any MCP-compatible client (Claude Desktop, Cursor, Continue.dev, …) can call directly:

| Tool | Returns |
|---|---|
| `search_products` | Multi-source price comparison for a product query |
| `best_offer` | The single cheapest in-stock offer for a query |
| `best_offer_under_budget` | Cheapest offer under a max price |
| `service_meta` | Live coverage, freshness, and pricing metadata |

Backed by the same JSON contract as `https://agentshare.dev/api/v1/*` — every response includes `freshness_status`, `data_status`, `trust_*` signals so agents can reason about staleness.

---

## Quick install

### Claude Desktop / Cursor / any Streamable-HTTP MCP client

Add to your MCP config (e.g. `~/.cursor/mcp.json` or Claude Desktop config):

\`\`\`json
{
  "mcpServers": {
    "agentshare": {
      "url": "https://agentshare.dev/mcp",
      "headers": {
        "X-API-Key": "YOUR_AGENTSHARE_KEY"
      }
    }
  }
}
\`\`\`

Get a free key (100 requests/month, no card): https://agentshare.dev/signup

### Local stdio (Python)

\`\`\`bash
git clone https://github.com/anhmtk/agentshare-mcp.git
cd agentshare-mcp
pip install -r requirements.txt
export AGENTSHARE_API_KEY=your_key_here
python -m integrations.mcp_server.server
\`\`\`

---

## Discovery files (for AI search)

| URL | Purpose |
|---|---|
| https://agentshare.dev/agent.json | Agent-native discovery manifest |
| https://agentshare.dev/llm.txt | LLM-readable summary |
| https://agentshare.dev/openapi.json | OpenAPI 3 schema |
| https://agentshare.dev/.well-known/mcp.json | MCP endpoint announcement |
| https://agentshare.dev/coverage | Data coverage spec (categories we cover well) |

---

## Read more

- 📖 Blog: [Your API ranks on Google. But does it rank for AI agents?](https://dev.to/anhmtk/your-api-ranks-on-google-but-does-it-rank-for-ai-agents-1hg)
- 🧭 Data scope: https://agentshare.dev/coverage — AI hardware, mini PCs, components, robotics, robot/RC power.
- 🛂 Trust + freshness: https://agentshare.dev/docs#data-quality

---

## License

MIT — see [LICENSE](LICENSE).

---

*Built solo from Vietnam 🇻🇳 by [@anhmtk](https://github.com/anhmtk).*
