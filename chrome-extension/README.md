# AgentShare Live Traffic — Chrome / Edge extension (draft)

Real-time **AI agent & bot traffic** on [agentshare.dev](https://agentshare.dev) — a lightweight “GA4 for API/MCP-first” pulse in your browser toolbar.

Part of the open [agentshare-mcp](https://github.com/anhmtk/agentshare-mcp) repo. Production API: `GET https://agentshare.dev/api/v1/public/bot-traffic/stats` (sanitized, no IPs or API keys).

## Load unpacked (dev)

1. Chrome → `chrome://extensions` (Edge → `edge://extensions`)
2. Enable **Developer mode**
3. **Load unpacked** → select this folder (`chrome-extension/`)
4. Pin **AgentShare Live Traffic** → click icon for popup

## What it shows

- Requests & authenticated agents (rolling ~15 min window)
- Traffic mix: good / suspicious / malicious
- Top intents & client types (MCP, Python, Node, …)
- Country chips + link to full map dashboard

Toolbar **badge** = request count (updates every minute via service worker).

## Files

| File | Role |
|------|------|
| `manifest.json` | MV3 manifest |
| `popup.html` / `popup.css` / `popup.js` | Toolbar popup UI |
| `background.js` | Badge polling |
| `config.js` | API URL defaults |
| `icons/` | Extension icons (from AgentShare brand assets) |

## Roadmap (not in v0.1)

- Public 24h trend sparkline
- Optional `apiBase` in `chrome.storage.sync` for self-hosted mirrors
- Chrome Web Store listing + donate link

## Feedback

[GitHub Issues](https://github.com/anhmtk/agentshare-mcp/issues) — tag `chrome-extension`.

## License

MIT — same as parent repository.
