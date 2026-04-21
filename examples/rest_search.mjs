#!/usr/bin/env node
/**
 * Minimal example: GET /api/v1/search (AgentShare REST API).
 *
 * Usage:
 *   export AGENTSHARE_API_KEY=your_key
 *   node rest_search.mjs "query here"
 *
 * Optional: AGENTSHARE_BASE_URL (default https://agentshare.dev)
 * Requires Node.js 18+ (global fetch).
 */
const base = (process.env.AGENTSHARE_BASE_URL || "https://agentshare.dev").replace(/\/$/, "");
const key = (process.env.AGENTSHARE_API_KEY || "").trim();
if (!key) {
  console.error("Set AGENTSHARE_API_KEY (https://agentshare.dev/pricing).");
  process.exit(1);
}

const query = process.argv.slice(2).join(" ").trim() || "raspberry pi";
const url = new URL("/api/v1/search", `${base}/`);
url.searchParams.set("q", query);
url.searchParams.set("limit", "5");

const res = await fetch(url, {
  headers: {
    "X-API-Key": key,
    Accept: "application/json",
  },
});

const text = await res.text();
if (!res.ok) {
  console.error(`HTTP ${res.status}: ${text}`);
  process.exit(1);
}

try {
  console.log(JSON.stringify(JSON.parse(text), null, 2));
} catch {
  console.log(text);
}
