#!/usr/bin/env python
"""Launcher for Agent Price API MCP server (stdio). Run from project root: python integrations/mcp_server/run.py"""
import sys
from pathlib import Path

_root = Path(__file__).resolve().parents[2]
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

from integrations.mcp_server.price_mcp import create_price_mcp

if __name__ == "__main__":
    create_price_mcp().run(transport="stdio")
