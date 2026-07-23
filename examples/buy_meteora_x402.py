#!/usr/bin/env python3
"""
Buy AgentShare Meteora DLMM brief with x402 (USDC on Base).

Official buyer SDK handles HTTP 402 → sign → PAYMENT-SIGNATURE → retry.

Install:
  pip install "x402[httpx]" eth-account python-dotenv

Fund a Base mainnet wallet with a little USDC, then:

  export EVM_PRIVATE_KEY=0x...          # Base / EVM key (never commit)
  # optional overrides:
  # export AGENTSHARE_BASE_URL=https://agentshare.dev
  # export AGENTSHARE_METEORA_PATH=/api/v1/agent/defi/meteora/brief

  python buy_meteora_x402.py

Live quote tip: unpaid POST returns HTTP 402; read PAYMENT-REQUIRED
(accepts[].amount is USDC atomic units, 6 decimals) — do not hard-code price.
Discovery: https://agentshare.dev/.well-known/x402
x402scan: https://www.x402scan.com/server/65b3e822-068a-4e51-a8bb-2ade6d5f0b32
"""
from __future__ import annotations

import asyncio
import json
import os
import sys

from eth_account import Account

from x402 import x402Client
from x402.http import x402HTTPClient
from x402.http.clients import x402HttpxClient
from x402.mechanisms.evm import EthAccountSigner
from x402.mechanisms.evm.exact.register import register_exact_evm_client


async def main() -> None:
    key = (os.environ.get("EVM_PRIVATE_KEY") or "").strip()
    if not key:
        print(
            "Set EVM_PRIVATE_KEY to a Base-funded USDC wallet private key.",
            file=sys.stderr,
        )
        sys.exit(1)

    base = (os.environ.get("AGENTSHARE_BASE_URL") or "https://agentshare.dev").rstrip("/")
    path = (
        os.environ.get("AGENTSHARE_METEORA_PATH")
        or "/api/v1/agent/defi/meteora/brief"
    )
    url = f"{base}{path}"

    client = x402Client()
    account = Account.from_key(key)
    register_exact_evm_client(client, EthAccountSigner(account))
    http_helper = x402HTTPClient(client)

    body = {"limit": 3, "window": "5m", "format": "compact"}
    print(f"Buyer: {account.address}")
    print(f"POST {url}  body={body}")

    async with x402HttpxClient(client) as http:
        response = await http.post(url, json=body)
        await response.aread()

    print(f"HTTP {response.status_code}")
    try:
        print(json.dumps(response.json(), indent=2, ensure_ascii=False)[:4000])
    except Exception:
        print(response.text[:4000])

    try:
        settle = http_helper.get_payment_settle_response(
            lambda name: response.headers.get(name)
        )
        print("\nSettlement:", settle.model_dump_json(indent=2))
    except ValueError:
        print("\nNo PAYMENT-RESPONSE header (request may have used another auth path).")


if __name__ == "__main__":
    asyncio.run(main())
