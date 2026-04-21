# Examples — AgentShare REST API

Minimal scripts that call **https://agentshare.dev** (or `AGENTSHARE_BASE_URL`) with an API key.

| File | Requires | Description |
|------|----------|-------------|
| [`rest_search.py`](rest_search.py) | Python 3.10+ (stdlib only) | `GET /api/v1/search` |
| [`rest_search.mjs`](rest_search.mjs) | Node.js 18+ (`fetch`) | Same as above |

## Setup

1. Create a key: https://agentshare.dev/pricing  
2. Export environment variables (do **not** commit real keys):

```bash
export AGENTSHARE_API_KEY="your_key_here"
# optional:
export AGENTSHARE_BASE_URL="https://agentshare.dev"
```

Windows (PowerShell):

```powershell
$env:AGENTSHARE_API_KEY="your_key_here"
```

## Run

```bash
python rest_search.py "raspberry pi 5"
```

```bash
node rest_search.mjs "raspberry pi 5"
```

Full API reference: https://agentshare.dev/docs — MCP tools (`price_search`, …) map to these endpoints on the server side.
