# Examples — AgentShare

Minimal scripts that call **https://agentshare.dev**.

| File | Requires | Description |
|------|----------|-------------|
| [`rest_search.py`](rest_search.py) | Python 3.10+ (stdlib) + API key | `GET /api/v1/search` |
| [`rest_search.mjs`](rest_search.mjs) | Node.js 18+ (`fetch`) + API key | Same as above |
| [`buy_meteora_x402.py`](buy_meteora_x402.py) | Python 3.10+ + `x402[httpx]` + Base USDC | Pay-per-call Meteora brief via **x402** (no API key) |

---

## API key path (quota plans)

1. Create a key: https://agentshare.dev/pricing  
2. Export (do **not** commit real keys):

```bash
export AGENTSHARE_API_KEY="your_key_here"
# optional:
export AGENTSHARE_BASE_URL="https://agentshare.dev"
```

```powershell
$env:AGENTSHARE_API_KEY="your_key_here"
```

```bash
python rest_search.py "raspberry pi 5"
node rest_search.mjs "raspberry pi 5"
```

---

## x402 buyer path (USDC on Base)

AgentShare gates DeFi/commerce routes with HTTP 402. The official Python buyer SDK
intercepts 402, signs, retries with `PAYMENT-SIGNATURE`.

```bash
pip install "x402[httpx]" eth-account python-dotenv
export EVM_PRIVATE_KEY="0x..."   # Base mainnet wallet with USDC — never commit
python buy_meteora_x402.py
```

- Live discovery: https://agentshare.dev/.well-known/x402  
- OpenAPI: https://agentshare.dev/openapi.json  
- x402scan listing: https://www.x402scan.com/server/65b3e822-068a-4e51-a8bb-2ade6d5f0b32  

`meteora_brief` uses **dynamic** pricing (~$0.01–$0.30 USDC). Always read the live
quote from `PAYMENT-REQUIRED` / `accepts[].amount` (USDC 6 decimals).

Settlement network today: **Base mainnet** (`eip155:8453`) via Circle Gateway.

Full API / MCP docs: https://agentshare.dev/docs
