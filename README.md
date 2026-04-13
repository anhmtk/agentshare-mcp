# AgentShare

**Structured marketplace prices and offers for AI agents** — REST API and [MCP (Streamable HTTP)](https://agentshare.dev/mcp/).

| | |
|---|---|
| **Site & docs** | https://agentshare.dev |
| **MCP endpoint** | `https://agentshare.dev/mcp/` |
| **Discovery** | [`/agent.json`](https://agentshare.dev/agent.json) · [`/mcp.json`](https://agentshare.dev/mcp.json) |

This repository is a **lightweight public pointer** to the live service and documentation. Implementation is developed privately; releases and integration details are published on the website above.

---

### Scope (honest & forward-looking)

AgentShare aggregates product and offer data from **connected marketplaces and affiliate sources**. Coverage and freshness vary by source; the API returns **freshness metadata** (e.g. `crawled_at`, `data_age_seconds`) so agents can judge reliability.

**Direction:** expand toward **global e‑commerce** and major international marketplaces (e.g. AliExpress, eBay, Amazon) as integrations mature — not limited to a single country. For the **current** focus and category map, see **`GET /coverage`** (no auth):  
https://agentshare.dev/coverage

---

### Integration

- **Docs:** https://agentshare.dev/docs  
- **Pricing / API keys:** https://agentshare.dev/pricing  
- **MCP:** Streamable HTTP; same API key as REST (`X-API-Key` or `Authorization: Bearer`).

---

### Legal

Terms and privacy: https://agentshare.dev/terms · https://agentshare.dev/privacy
