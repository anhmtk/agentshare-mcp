"""
AgentShare — Solana DeFi tools as a Gradio MCP Space (Hugging Face).

Deploy on Hugging Face Spaces (Gradio SDK). Set Space secret:
  AGENTSHARE_API_KEY = your free/paid key from https://agentshare.dev/get-key

Optional:
  AGENTSHARE_BASE_URL = https://agentshare.dev

Enable MCP in launch() so the Space gets an MCP badge and can be added
from https://huggingface.co/settings/mcp
"""
from __future__ import annotations

import json
import os
from typing import Any

import gradio as gr
import httpx

BASE_URL = (os.environ.get("AGENTSHARE_BASE_URL") or "https://agentshare.dev").rstrip("/")
API_KEY = (os.environ.get("AGENTSHARE_API_KEY") or "").strip()
TIMEOUT = float(os.environ.get("AGENTSHARE_HTTP_TIMEOUT", "60") or 60)


def _headers() -> dict[str, str]:
    h = {"Accept": "application/json", "User-Agent": "agentshare-hf-space/1.0"}
    if API_KEY:
        h["X-API-Key"] = API_KEY
    return h


def _pretty(data: Any) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False)


def _error_payload(exc: Exception) -> str:
    if isinstance(exc, httpx.HTTPStatusError):
        body: Any
        try:
            body = exc.response.json()
        except Exception:
            body = exc.response.text[:2000]
        return _pretty(
            {
                "error": True,
                "status_code": exc.response.status_code,
                "detail": body,
                "hint": (
                    "402 = x402 payment required (set AGENTSHARE_API_KEY on this Space, "
                    "or pay via x402 from your own agent). "
                    "Get a key: https://agentshare.dev/get-key"
                ),
            }
        )
    return _pretty({"error": True, "message": str(exc)})


def meteora_brief(limit: int = 5, window: str = "5m", format: str = "compact") -> str:
    """
    Ranked Meteora DLMM pool brief for Solana (momentum, fee velocity, SAFE/CAUTION/AVOID).

    Primary AgentShare DeFi endpoint for autonomous agents. Live data from agentshare.dev.
    """
    limit = max(1, min(int(limit), 20))
    window = (window or "5m").strip() or "5m"
    fmt = (format or "compact").strip().lower()
    if fmt not in ("compact", "full"):
        fmt = "compact"
    url = f"{BASE_URL}/api/v1/agent/defi/meteora/brief"
    payload = {"limit": limit, "window": window, "format": fmt}
    try:
        with httpx.Client(timeout=TIMEOUT) as client:
            r = client.post(url, headers=_headers(), json=payload)
            r.raise_for_status()
            return _pretty(r.json())
    except Exception as exc:
        return _error_payload(exc)


def solana_dex_brief(limit: int = 10) -> str:
    """
    Solana DEX ecosystem brief (macro venue rankings via DefiLlama-style aggregation).

    Public-friendly scout before diving into Meteora pool-level briefs.
    """
    limit = max(1, min(int(limit), 50))
    url = f"{BASE_URL}/api/v1/agent/defi/solana/brief"
    try:
        with httpx.Client(timeout=TIMEOUT) as client:
            r = client.get(url, headers=_headers(), params={"limit": limit})
            r.raise_for_status()
            return _pretty(r.json())
    except Exception as exc:
        return _error_payload(exc)


def dex_overview(chain: str = "solana", limit: int = 15) -> str:
    """
    Macro DEX protocol rankings by 24h volume (DefiLlama aggregated).

    Use chain=solana for AgentShare's primary focus; other chains may be available upstream.
    """
    chain = (chain or "solana").strip().lower() or "solana"
    limit = max(1, min(int(limit), 50))
    url = f"{BASE_URL}/api/v1/dex/overview"
    try:
        with httpx.Client(timeout=TIMEOUT) as client:
            r = client.get(url, headers=_headers(), params={"chain": chain, "limit": limit})
            r.raise_for_status()
            return _pretty(r.json())
    except Exception as exc:
        return _error_payload(exc)


def service_meta() -> str:
    """
    AgentShare service metadata: capabilities, discovery URLs, billing hints for agents.
    """
    url = f"{BASE_URL}/api/v1/meta"
    try:
        with httpx.Client(timeout=TIMEOUT) as client:
            r = client.get(url, headers=_headers())
            r.raise_for_status()
            return _pretty(r.json())
    except Exception as exc:
        return _error_payload(exc)


INTRO = """
# AgentShare — Agent-paid API for AI Agents

Live tools from **[agentshare.dev](https://agentshare.dev)** — dual-auth (API key or x402), commerce procurement, and secondary Solana/Meteora DeFi demos.

| | |
|---|---|
| Docs | https://agentshare.dev/docs |
| Start building | https://agentshare.dev/signup |
| MCP (production) | https://agentshare.dev/mcp |
| x402 discovery | https://agentshare.dev/.well-known/x402 |
| x402scan | https://www.x402scan.com/server/65b3e822-068a-4e51-a8bb-2ade6d5f0b32 |
| GitHub | https://github.com/anhmtk/agentshare-mcp |

This Space exposes AgentShare tools over **Gradio MCP** (`mcp_server=True`).
Add it from [Hugging Face MCP settings](https://huggingface.co/settings/mcp) when the MCP badge is visible.

**Space secret:** set `AGENTSHARE_API_KEY` (https://agentshare.dev/signup) so tool calls succeed without a browser wallet.
"""

with gr.Blocks(title="AgentShare Agent-paid API") as demo:
    gr.Markdown(INTRO)
    with gr.Tab("Meteora brief"):
        lim = gr.Slider(1, 20, value=5, step=1, label="limit")
        win = gr.Dropdown(["5m", "1h", "6h", "24h"], value="5m", label="window")
        fmt = gr.Dropdown(["compact", "full"], value="compact", label="format")
        out_m = gr.Code(language="json", label="response")
        gr.Button("Run meteora_brief", variant="primary").click(
            meteora_brief, inputs=[lim, win, fmt], outputs=out_m
        )
    with gr.Tab("Solana DEX brief"):
        lim2 = gr.Slider(1, 50, value=10, step=1, label="limit")
        out_s = gr.Code(language="json", label="response")
        gr.Button("Run solana_dex_brief", variant="primary").click(
            solana_dex_brief, inputs=[lim2], outputs=out_s
        )
    with gr.Tab("DEX overview"):
        chain = gr.Textbox(value="solana", label="chain")
        lim3 = gr.Slider(1, 50, value=15, step=1, label="limit")
        out_d = gr.Code(language="json", label="response")
        gr.Button("Run dex_overview", variant="primary").click(
            dex_overview, inputs=[chain, lim3], outputs=out_d
        )
    with gr.Tab("Service meta"):
        out_meta = gr.Code(language="json", label="response")
        gr.Button("Run service_meta", variant="primary").click(service_meta, outputs=out_meta)


if __name__ == "__main__":
    demo.launch(mcp_server=True)
