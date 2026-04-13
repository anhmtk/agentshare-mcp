"""
MCP server for Agent Price API (stdio transport).

For remote Streamable HTTP on the same API, use:
  https://agentshare.dev/mcp
See docs/MCP_QUICKSTART.md

Run from repo root: python integrations/mcp_server/server.py
Or: python integrations/mcp_server/run.py
"""
import sys
from pathlib import Path

_root = Path(__file__).resolve().parents[2]
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

from integrations.mcp_server.price_mcp import create_price_mcp

mcp = create_price_mcp()

if __name__ == "__main__":
    mcp.run(transport="stdio")
