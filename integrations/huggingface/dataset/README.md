---
license: mit
task_categories:
  - other
language:
  - en
tags:
  - defi
  - solana
  - meteora
  - dlmm
  - agents
  - mcp
  - x402
  - multi-chain
pretty_name: AgentShare Multi-Chain DeFi Intelligence (Sample)
size_categories:
  - n<1K
---

# AgentShare — Multi-Chain DeFi Intelligence (Sample Dataset)

**Sample / schema-oriented** exports that illustrate how [AgentShare](https://agentshare.dev) structures DeFi intelligence for **AI agents**.

> This is **not** a live dump of production pools. Live data is served via REST + MCP with freshness metadata and optional **x402** USDC pay-per-request.

## Product

| | |
|---|---|
| Live API | https://agentshare.dev |
| Docs | https://agentshare.dev/docs |
| MCP | https://agentshare.dev/mcp |
| x402 discovery | https://agentshare.dev/.well-known/x402 |
| x402scan | https://www.x402scan.com/server/65b3e822-068a-4e51-a8bb-2ade6d5f0b32 |
| Gradio Space | https://huggingface.co/spaces/anhmtk/agentshare-multi-chain-defi |
| Source | https://github.com/anhmtk/agentshare-mcp |

**Positioning:** payment + data rails for autonomous agents. **Today’s depth:** Solana (Meteora DLMM, DEX scout). **Roadmap:** same agent contract across more chains (Base DeFi analytics, etc.) as coverage ships.

## Files

| File | Description |
|------|-------------|
| `meteora_brief.sample.json` | Example `meteora_brief` style payload (ranked DLMM pools + billing meta shape) |
| `solana_dex_brief.sample.json` | Example Solana DEX ecosystem scout payload |
| `dex_overview.sample.json` | Example macro DEX overview (`chain=solana`) |
| `service_meta.sample.json` | Example service capability / discovery envelope |

## How agents use the live API

```bash
# Free key (quota) OR x402 USDC on HTTP 402
curl -s -X POST "https://agentshare.dev/api/v1/agent/defi/meteora/brief" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: YOUR_KEY" \
  -d '{"limit":5,"window":"5m","format":"compact"}'
```

Dynamic pricing on `meteora_brief`: always read the live quote from `PAYMENT-REQUIRED` / `meta.billing` — do not hard-code.

## Citation

```bibtex
@misc{agentshare_defi_sample,
  title        = {AgentShare Multi-Chain DeFi Intelligence Sample},
  author       = {AgentShare},
  year         = {2026},
  howpublished = {\\url{https://huggingface.co/datasets/anhmtk/agentshare-multi-chain-defi}},
  note         = {Sample schemas for agent-native DeFi APIs; live data at agentshare.dev}
}
```
