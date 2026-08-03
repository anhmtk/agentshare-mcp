# DeFi positioning (honest)

Canonical live page: **https://agentshare.dev/coverage**  
JSON for agents: **https://agentshare.dev/coverage?format=json**

This note mirrors the live coverage map. Prefer the live URL if wording diverges.

## What AgentShare is

AgentShare wraps public upstreams (Meteora DLMM data API, DefiLlama) into **decision-shaped JSON for autonomous agents**: ranked briefs, verdict / risk / momentum heuristics, `meta.freshness`, and dual-auth (API key or x402).

Primary surface: Solana / Meteora DLMM scout briefs + Solana DEX / DefiLlama macro tools over REST and MCP.

## What we do not claim

- Deepest tick / OHLCV / trade-tape coverage vs Birdeye-class feeds
- Proven trading alpha — `verdict` / `risk_score` are AgentShare heuristics on upstream metrics
- Full multi-chain DeFi depth today (Solana-first; other chains are roadmap)

## How we check quality

**Method:** OpenClaw paper trade  
**Status:** ongoing

Brief quality and heuristics are continuously exercised via OpenClaw paper trading and iterated. Numbers and verdicts can be wrong. Always read `meta.freshness`. Outputs are informational decision aids — **not financial advice**.

## Vs common alternatives

| Alternative | They excel at | AgentShare is for |
|-------------|---------------|-------------------|
| DefiLlama (raw API / site) | Broad multi-chain TVL/volume aggregates | Same macro scout shaped for agents (REST/MCP) plus Solana/Meteora decision briefs — not a DefiLlama replacement |
| Meteora DLMM Data API (official) | Canonical pool/position/portfolio endpoints | Opinionated ranked briefs + risk/momentum envelope + freshness/billing metadata for agent workflows |
| Birdeye / terminal-grade Solana market data | Cross-DEX trades, OHLCV depth, holders, VWAP-style views | Lightweight Meteora/Solana scout for agents that need a short brief and micropayment-friendly access — not Bloomberg-for-Solana |

## Choose AgentShare when

- You need a Meteora/Solana scout brief an agent can act on without writing your own ranking rules
- You want MCP + `agent.json` discovery and optional x402 pay-per-request
- You prefer explicit cache/live disclosure (`meta.freshness`) over opaque feeds

## Choose someone else when

- You need full Solana trade history, multi-venue VWAP, or institutional market-data SLAs
- You only need raw DefiLlama/Meteora JSON with no agent envelope

## Commerce (secondary)

Product search / offers for AI hardware, robotics, mini PCs, robot power — see the same `/coverage` page (`#commerce`) and `focus_categories` in the JSON.
