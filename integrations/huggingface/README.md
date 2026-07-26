---
title: AgentShare Solana DeFi
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
  - defi
  - solana
  - meteora
  - x402
short_description: Solana DeFi intelligence (Meteora / DEX) for AI agents via AgentShare
---

# AgentShare — Solana DeFi Intelligence (Gradio + MCP)

Live tools backed by **[agentshare.dev](https://agentshare.dev)**:

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
| `AGENTSHARE_API_KEY` | Key from https://agentshare.dev/get-key |

Optional: `AGENTSHARE_BASE_URL=https://agentshare.dev`

## Links

- Docs: https://agentshare.dev/docs  
- x402: https://agentshare.dev/.well-known/x402  
- x402scan: https://www.x402scan.com/server/65b3e822-068a-4e51-a8bb-2ade6d5f0b32  
- Source: https://github.com/anhmtk/agentshare-mcp/tree/main/integrations/huggingface  
