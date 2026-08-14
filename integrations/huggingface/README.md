---
title: AgentShare Agent-paid API
emoji: ◎
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: "5.49.1"
app_file: app.py
pinned: false
tags:
  - mcp-server-track
  - agent
  - agent-paid
  - x402
  - commerce
  - defi
  - solana
  - meteora
short_description: Agent-paid API (dual-auth / x402) + commerce + secondary Solana/Meteora demos via AgentShare
---

# AgentShare — Agent-paid API (Gradio + MCP)

Live tools backed by **[agentshare.dev](https://agentshare.dev)**:

**Primary rails:** dual-auth (API key or x402), discovery, MCP  
**Secondary · commerce:** search / best offer / quote  
**Secondary · DeFi demos:**

- `meteora_brief` — Meteora DLMM pool rankings for agents  
- `solana_dex_brief` — Solana DEX ecosystem scout  
- `dex_overview` — macro DEX volume rankings  
- `service_meta` — discovery / capabilities  

## MCP

This Space launches with `mcp_server=True`. After deploy, add it from  
https://huggingface.co/settings/mcp (look for the MCP badge).

Production MCP (always on): `https://agentshare.dev/mcp`

## Secrets

In **Settings → Variables and secrets** add:

| Name | Value |
|------|--------|
| `AGENTSHARE_API_KEY` | Credentials from https://agentshare.dev/signup |

Optional: `AGENTSHARE_BASE_URL=https://agentshare.dev`

## Links

- Docs: https://agentshare.dev/docs  
- Pricing / x402: https://agentshare.dev/pricing · https://agentshare.dev/.well-known/x402  
- x402scan: https://www.x402scan.com/server/65b3e822-068a-4e51-a8bb-2ade6d5f0b32  
- Source: https://github.com/anhmtk/agentshare-mcp/tree/main/integrations/huggingface  
