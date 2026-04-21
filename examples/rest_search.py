#!/usr/bin/env python3
"""
Minimal example: GET /api/v1/search (AgentShare REST API).

Usage:
  export AGENTSHARE_API_KEY=your_key
  python rest_search.py "query here"

Optional: AGENTSHARE_BASE_URL (default https://agentshare.dev)
"""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request


def main() -> None:
    base = (os.environ.get("AGENTSHARE_BASE_URL") or "https://agentshare.dev").rstrip("/")
    key = (os.environ.get("AGENTSHARE_API_KEY") or "").strip()
    if not key:
        print("Set AGENTSHARE_API_KEY to your API key (https://agentshare.dev/pricing).", file=sys.stderr)
        sys.exit(1)

    query = " ".join(sys.argv[1:]).strip() or "raspberry pi"
    params = urllib.parse.urlencode({"q": query, "limit": 5})
    url = f"{base}/api/v1/search?{params}"
    req = urllib.request.Request(
        url,
        headers={
            "X-API-Key": key,
            "Accept": "application/json",
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code}: {e.reason}", file=sys.stderr)
        if e.fp:
            print(e.fp.read().decode("utf-8", errors="replace"), file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Request failed: {e.reason}", file=sys.stderr)
        sys.exit(1)

    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        print(body)
        return

    print(json.dumps(data, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
