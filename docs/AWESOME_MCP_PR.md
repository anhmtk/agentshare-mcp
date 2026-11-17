# PR: awesome-mcp-servers (E-Commerce / Agents)

**Target repo:** [github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)  
**Section:** `### 🛒 E-Commerce` (or Agents / Payments if a better fit)  
**Prerequisite:** Server listed on [Glama](https://glama.ai/mcp/servers/anhmtk/agentshare-mcp) with passing score badge.

---

## Steps

1. Fork `punkpeye/awesome-mcp-servers`
2. Branch: `add-anhmtk-agentshare-mcp`
3. Edit `README.md` — find `### 🛒 E-Commerce`
4. Insert **one line** alphabetically after `[agentlux/agentlux-mcp]` and before `[BuyWhere/buywhere-mcp]`:

```markdown
- [anhmtk/agentshare-mcp](https://github.com/anhmtk/agentshare-mcp) [![anhmtk/agentshare-mcp MCP server](https://glama.ai/mcp/servers/anhmtk/agentshare-mcp/badges/score.svg)](https://glama.ai/mcp/servers/anhmtk/agentshare-mcp) 📇 ☁️ 🍎 🪟 🐧 - Curated MCP registry. Live server `agentshare-registry`: `search_listing`, `check_health`, `evidence_pack`, then connect to `mcp_url` yourself. 15 tools at [agentshare.dev/mcp](https://agentshare.dev/mcp). Start building: [agentshare.dev/signup](https://agentshare.dev/signup).
```

5. Open PR with title:

```text
Add anhmtk/agentshare-mcp (AgentShare agent-paid MCP) 🤖🤖🤖
```

The `🤖🤖🤖` suffix opts into [fast-track for agent PRs](https://github.com/punkpeye/awesome-mcp-servers/blob/main/CONTRIBUTING.md) (optional).

6. If bot comments **missing-glama**: confirm Glama listing URL matches `anhmtk/agentshare-mcp` and badge renders.
7. If bot comments **missing-emoji**: line already includes `📇 ☁️ 🍎 🪟 🐧`.

---

## Glama badge URL

If your Glama path differs (check your Glama dashboard), update both badge URLs in the line:

```text
https://glama.ai/mcp/servers/anhmtk/agentshare-mcp/badges/score.svg
https://glama.ai/mcp/servers/anhmtk/agentshare-mcp
```

**Remote connector** (hosted MCP): also list at [glama.ai/mcp/connectors](https://glama.ai/mcp/connectors) with `https://agentshare.dev/mcp`.

---

## Verify before PR

```bash
cd agentshare-commerce-mcp
npm ci --omit=dev
npm run verify
```
