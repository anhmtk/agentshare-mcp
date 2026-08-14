---
license: mit
task_categories:
  - other
language:
  - en
tags:
  - agent-paid
  - x402
  - agents
  - mcp
  - defi
  - solana
  - meteora
  - dlmm
pretty_name: AgentShare Agent-paid API — DeFi demo samples
size_categories:
  - n<1K
configs:
  - config_name: meteora_brief
    default: true
    data_files:
      - split: train
        path: meteora_brief.sample.json
  - config_name: solana_dex_brief
    data_files:
      - split: train
        path: solana_dex_brief.sample.json
  - config_name: dex_overview
    data_files:
      - split: train
        path: dex_overview.sample.json
  - config_name: service_meta
    data_files:
      - split: train
        path: service_meta.sample.json
---

# AgentShare — Agent-paid API (DeFi demo sample schemas)

**Sample / schema-oriented** exports that illustrate how [AgentShare](https://agentshare.dev) structures **secondary DeFi demos** for AI agents on the same agent-paid rails (dual-auth / x402).

> This is **not** a live dump of production pools. Live data is served via REST + MCP with freshness metadata and optional **x402** USDC pay-per-request. **Primary product** is agent-paid API access — not a DeFi data company.

## Product

| | |
|---|---|
| Live API | https://agentshare.dev |
| Start building | https://agentshare.dev/signup |
| Docs | https://agentshare.dev/docs |
| MCP | https://agentshare.dev/mcp |
| x402 discovery | https://agentshare.dev/.well-known/x402 |
| x402scan | https://www.x402scan.com/server/65b3e822-068a-4e51-a8bb-2ade6d5f0b32 |
| Gradio Space | https://huggingface.co/spaces/anhmtk/agentshare-multi-chain-defi |
| Source | https://github.com/anhmtk/agentshare-mcp |

**Positioning:** agent-paid rails first. **Secondary demos today:** Solana (Meteora DLMM, DEX scout). **Roadmap:** more coverage as it ships — still secondary to dual-auth / discovery / MCP.

## Files / subsets

Each sample JSON is a **separate subset** (Hub Dataset Viewer → **Subset** dropdown). Do not load them as one table — the envelopes have different schemas.

| Subset | File | Description |
|--------|------|-------------|
| `meteora_brief` (default) | `meteora_brief.sample.json` | Ranked DLMM pools + billing meta shape |
| `solana_dex_brief` | `solana_dex_brief.sample.json` | Solana DEX ecosystem scout payload |
| `dex_overview` | `dex_overview.sample.json` | Macro DEX overview (`chain=solana`) |
| `service_meta` | `service_meta.sample.json` | Service capability / discovery envelope |

## How agents use the live API

```bash
# Dual-auth credentials OR x402 USDC on HTTP 402
curl -s -X POST "https://agentshare.dev/api/v1/agent/defi/meteora/brief" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: YOUR_KEY" \
  -d '{"limit":5,"window":"5m","format":"compact"}'
```

Dynamic pricing on `meteora_brief`: always read the live quote from `PAYMENT-REQUIRED` / `meta.billing` — do not hard-code.

## Citation

```bibtex
@misc{agentshare_defi_sample,
  title        = {AgentShare Agent-paid API DeFi Demo Samples},
  author       = {AgentShare},
  year         = {2026},
  howpublished = {\\url{https://huggingface.co/datasets/anhmtk/agentshare-multi-chain-defi}},
  note         = {Sample schemas for secondary DeFi demos on agent-paid rails; live data at agentshare.dev}
}
```
