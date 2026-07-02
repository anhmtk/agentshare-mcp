# Submit to Cursor Directory

Cursor Marketplace is **limited** for new publishers (2026). Cursor team directs submissions to **[cursor.directory](https://cursor.directory)** for community visibility.

## Prerequisites

- Public repo: `https://github.com/anhmtk/agentshare-mcp`
- Root **`.mcp.json`** and **`agentshare-commerce-mcp/.mcp.json`** (Streamable HTTP)
- Free API key: [agentshare.dev/signup](https://agentshare.dev/signup) (`agshp_…`)

---

## 1. MCP server listing (recommended first)

**Form:** [cursor.directory/mcp/new](https://cursor.directory/mcp/new)

Sign in with **GitHub** (same account as repo).

| Field | Paste this |
|-------|------------|
| **Name** | `AgentShare` |
| **Description** | `Live marketplace prices for AI agents: search, best offer, budget deals & ACP commerce_quote. Free tier at agentshare.dev.` |
| **Link to install instructions** | `https://github.com/anhmtk/agentshare-mcp/blob/main/agentshare-commerce-mcp/README.md` |
| **Cursor Deep Link** | See below |
| **Logo** | Upload `agentshare-commerce-mcp/assets/icon.png` |

### One-click install deep link (Streamable HTTP)

Users replace `YOUR_AGENTSHARE_API_KEY` with their `agshp_…` key after install.

```
cursor://anysphere.cursor-deeplink/mcp/install?name=agentshare&config=eyJ1cmwiOiJodHRwczovL2FnZW50c2hhcmUuZGV2L21jcCIsImhlYWRlcnMiOnsiWC1BUEktS2V5IjoiWU9VUl9BR0VOVFNIQVJFX0FQSV9LRVkifX0=
```

Decoded config:

```json
{
  "url": "https://agentshare.dev/mcp",
  "headers": {
    "X-API-Key": "YOUR_AGENTSHARE_API_KEY"
  }
}
```

Regenerate after changing URL/headers:

```bash
node scripts/cursor-deeplink.mjs
```

---

## 2. Plugin listing (Open Plugins auto-detect)

**Form:** [cursor.directory/plugins/new](https://cursor.directory/plugins/new)

| Field | Value |
|-------|--------|
| **Repository URL** | `https://github.com/anhmtk/agentshare-mcp` |

Auto-detected from repo:

- `.cursor-plugin/marketplace.json` → plugin `agentshare-commerce-mcp`
- `agentshare-commerce-mcp/.mcp.json` → MCP wiring
- `agentshare-commerce-mcp/.cursor-plugin/plugin.json` → manifest

---

## 3. Manual MCP config (Customize)

**Streamable HTTP (simplest):**

| Field | Value |
|-------|--------|
| URL | `https://agentshare.dev/mcp` |
| Header | `X-API-Key: agshp_YOUR_KEY` |

**Node bridge** (from cloned plugin folder):

```bash
cd agentshare-commerce-mcp
npm install --omit=dev
node server/bridge.mjs https://agentshare.dev/mcp --header X-API-Key:agshp_YOUR_KEY
```

---

## 4. After submit

- Test **Add to Cursor** from directory listing if available.
- Reply to Cursor marketplace email: *Submitted to cursor.directory — thanks for the pointer.*
- Continue [Glama](https://glama.ai/mcp/servers) + [awesome-mcp-servers PR](./AWESOME_MCP_PR.md).
