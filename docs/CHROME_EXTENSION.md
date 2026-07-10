# AgentShare Agent Readiness — Chrome extension

**Chrome Web Store:** [AgentShare Agent Readiness](https://chromewebstore.google.com/detail/agentshare-agent-readiness/nimndnhajfkicbnipbfdkmgencjejjed)  
**Version:** 0.5.0 (upload package built from private `agent-price-api` repo)  
**ARS spec:** https://agentshare.dev/docs#agent-readiness-score  
**Prompt Injection Fix Guide:** https://agentshare.dev/docs#prompt-injection-fix-guide

Free Chromium extension (Chrome / Edge) for **site owners and developers** — not required to use AgentShare MCP, but pairs well with it.

---

## What it does

### Site scan (ARS v1)

Client-side scan of **the tab you have open**:

- `robots.txt` — AI crawler allow/disallow on `/`
- Agent discovery files — `llms.txt`, `llm.txt`, `ai.txt`
- **MCP discovery** (v0.4+) — `/.well-known/mcp/server-card.json`, `.mcp.json`, `/mcp.json`
- Homepage headers, Cloudflare Markdown for Agents probe
- **Agent Readiness Score** (0–100) with explainable findings
- GA4 blind spot — why server-side bots and MCP clients do not appear in analytics

No login. Scan results are not uploaded to AgentShare servers in this version.

### Prompt Injection Scan (v0.5+)

Client-side **DOM scan** of the active tab (via `scripting` permission on user action):

- Detects hidden or instruction-like text that may hijack AI agents reading the page
- Risk levels: **Clean** / **Suspicious** / **High Risk**
- Skips `<code>`, `<pre>`, `<script>`, `<style>`, and common a11y patterns (`sr-only`, `aria-hidden`)
- **No page content uploaded** — pattern-based heuristics only; verify findings manually

**Fix guide:** https://agentshare.dev/docs#prompt-injection-fix-guide — site-owner checklist + three defense levels for agent builders (data isolation, tool limits, input sanitization).

### MCP Connect tab (v0.4+)

Copy **multi-platform** install snippets for **AgentShare MCP** (`https://agentshare.dev/mcp`):

- Cursor (Streamable HTTP + one-click deeplink)
- Claude Desktop
- VS Code
- Windsurf
- Generic HTTP client

Placeholder API key only — get a free key at https://agentshare.dev/signup

**MCP catalog:** 10 tools — commerce prices, ACP `commerce_quote`, DefiLlama DEX, Solana & Meteora briefs. See [agentshare-mcp README](../README.md).

---

## Source code

Extension source is maintained in the private **agent-price-api** repository (proprietary). This public repo documents the product and MCP wiring only.

**Feedback / issues:** [github.com/anhmtk/agentshare-mcp/issues](https://github.com/anhmtk/agentshare-mcp/issues)

---

## Related

| Resource | URL |
|----------|-----|
| Website | https://agentshare.dev |
| MCP endpoint | https://agentshare.dev/mcp |
| Bot traffic map | https://agentshare.dev/public/bot-traffic |
| Share ARS score | https://agentshare.dev/scan |
| Prompt Injection Fix Guide | https://agentshare.dev/docs#prompt-injection-fix-guide |
| Crawler Fix Guide (llms.txt / robots.txt) | https://agentshare.dev/docs#bot-fix-guide |
