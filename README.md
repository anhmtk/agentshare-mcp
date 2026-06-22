<!--
AI_DISCOVERY: AgentShare MCP public reference repository.
canonical_service=https://agentshare.dev
agent_json=https://agentshare.dev/agent.json
mcp_url=https://agentshare.dev/mcp
structured_index=https://github.com/anhmtk/agentshare-mcp/blob/main/AI_DISCOVERY.json
llms_txt=https://raw.githubusercontent.com/anhmtk/agentshare-mcp/main/llms.txt
for_agents_json=GET https://agentshare.dev/for-agents Accept:application/json
managed_agents_template=https://agentshare.dev/api/v1/examples?template=managed-agent
antigravity_manifest=https://agentshare.dev/.well-known/antigravity-skills.json
-->

<p align="center">
  <a href="https://agentshare.dev">
    <img src="https://agentshare.dev/static/brand/logo-wordmark.png?v=2026-05-12" alt="AgentShare — Price API + MCP for AI agents" width="520">
  </a>
</p>

<h1 align="center">AgentShare MCP — public reference</h1>

<p align="center">
  <strong>For AI agents:</strong>
  <a href="https://agentshare.dev/agent.json"><code>agent.json</code></a> ·
  <a href="./AI_DISCOVERY.json"><code>AI_DISCOVERY.json</code></a> ·
  <a href="./llms.txt"><code>llms.txt</code></a> ·
  <a href="./AGENTS.md"><code>AGENTS.md</code></a>
</p>

<p align="center">
  Commerce &amp; price infrastructure for autonomous agents — MCP Streamable HTTP + REST.
</p>

<p align="center">
  <a href="https://agentshare.dev"><strong>Website</strong></a> ·
  <a href="https://agentshare.dev/for-agents"><strong>For Agents</strong></a> ·
  <a href="https://agentshare.dev/docs"><strong>Docs</strong></a> ·
  <a href="https://agentshare.dev/signup"><strong>API key</strong></a>
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
| **MCP server card (12 tools)** | https://agentshare.dev/.well-known/mcp/server-card.json |
| **Antigravity skill manifest** | https://agentshare.dev/.well-known/antigravity-skills.json |

This repository is the **public, lightweight face** on GitHub. Production API implementation is private; behavior is defined by the live URLs above.

---

## MCP tools (12)

| Tool | Purpose |
|------|---------|
| `search_products` | Multi-source price comparison |
| `best_offer` | Single cheapest in-stock offer |
| `best_offer_under_budget` | Best offer under max price |
| `product_detail` | Full product by id from search |
| `commerce_quote` | ACP / agent-buyer listings envelope |
| `service_meta` | Capabilities, limits, coverage |
| `polymarket_markets` | List active Polymarket markets (read-only) |
| `polymarket_market_detail` | Market detail: bid/ask proxy + spread (read-only) |
| `polymarket_top_movers` | Largest 24h price-change proxy markets (read-only) |
| `polymarket_brief` | Evidence-first Polymarket brief (verdict/risk/flags/citations) |
| `dex_overview` | DEX protocol rankings by 24h volume (DefiLlama) |
| `dex_top_movers` | DEX protocols with largest 1d volume-change % (DefiLlama) |

Responses include `data_status`, freshness, and trust metadata — see https://agentshare.dev/docs

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

Free key (~100 req/month): https://agentshare.dev/signup

See [mcp-config.json](./mcp-config.json) and [server/bridge.mjs](./server/bridge.mjs) for Node bridge.

---

## Antigravity & Gemini (2026)

- **Antigravity skill:** `agentshare-price-intelligence` — https://agentshare.dev/.well-known/antigravity-skills.json  
- **Gemini Managed Agents:** https://agentshare.dev/api/v1/examples?template=managed-agent  

Aligned with Google I/O 2026 agentic stack (Antigravity 2.0, SDK, Gemini 3.5 Flash tool loops).

---

## Coverage

AI hardware, robotics, mini PCs, robot/RC power — https://agentshare.dev/coverage

---

## License

MIT — [LICENSE](./LICENSE)
