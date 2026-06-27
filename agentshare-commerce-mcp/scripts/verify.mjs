/**
 * Local verification for Cursor plugin scaffold (no secrets required for base checks).
 * With AGENTSHARE_API_KEY set, also probes production /mcp initialize.
 */
import { spawn } from "node:child_process";
import { fileURLToPath } from "node:url";
import path from "node:path";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

function fail(msg) {
  process.stderr.write(`FAIL: ${msg}\n`);
  process.exit(1);
}

function ok(msg) {
  process.stdout.write(`OK: ${msg}\n`);
}

// 1) SDK import (same path as bridge.mjs)
try {
  await import("@modelcontextprotocol/sdk/client/streamableHttp.js");
  await import("@modelcontextprotocol/sdk/server/stdio.js");
  ok("MCP SDK imports");
} catch (e) {
  fail(`MCP SDK import: ${e}`);
}

// 2) Bridge syntax check (no execution)
import { spawnSync } from "node:child_process";
const syntax = spawnSync(process.execPath, ["--check", "server/bridge.mjs"], {
  cwd: root,
  encoding: "utf8",
});
if (syntax.status !== 0) {
  fail(`bridge syntax: ${syntax.stderr || syntax.stdout}`);
}
ok("bridge.mjs syntax (--check)");

// 3) Bridge exits 1 without URL
await new Promise((resolve) => {
  const child = spawn(process.execPath, ["server/bridge.mjs"], {
    cwd: root,
    stdio: ["ignore", "pipe", "pipe"],
  });
  let err = "";
  child.stderr.on("data", (d) => {
    err += d.toString();
  });
  child.on("close", (code) => {
    if (code !== 1) {
      fail(`bridge without args expected exit 1, got ${code}`);
    }
    if (!err.includes("Usage:")) {
      fail(`bridge stderr missing usage: ${err}`);
    }
    ok("bridge usage guard (exit 1 without URL)");
    resolve(undefined);
  });
});

// 4) Required files
import fs from "node:fs";
const required = [
  ".cursor-plugin/plugin.json",
  "mcp.json",
  "server/bridge.mjs",
  "assets/icon.png",
  "README.md",
  "package.json",
];
for (const rel of required) {
  if (!fs.existsSync(path.join(root, rel))) {
    fail(`missing ${rel}`);
  }
}
ok("plugin file layout");

// 5) plugin.json + mcp.json parse
const plugin = JSON.parse(fs.readFileSync(path.join(root, ".cursor-plugin/plugin.json"), "utf8"));
const mcp = JSON.parse(fs.readFileSync(path.join(root, "mcp.json"), "utf8"));
if (plugin.name !== "agentshare-commerce-mcp") {
  fail("plugin.json name mismatch");
}
if (!mcp.mcpServers?.agentshare?.args?.includes("server/bridge.mjs")) {
  fail("mcp.json must reference server/bridge.mjs relative to plugin root");
}
ok("plugin.json + mcp.json schema");

// 6) Live server card (public, no key)
const cardRes = await fetch("https://agentshare.dev/.well-known/mcp/server-card.json", {
  headers: { Accept: "application/json" },
});
if (!cardRes.ok) {
  fail(`server card HTTP ${cardRes.status}`);
}
const card = await cardRes.json();
const tools = card?.tools ?? card?.capabilities?.tools ?? [];
const toolCount = Array.isArray(tools) ? tools.length : 0;
if (toolCount < 6) {
  fail(`expected >= 6 tools on server card, got ${toolCount}`);
}
ok(`production server card (${toolCount} tools)`);

// 7) Optional: MCP POST initialize with API key
const apiKey = (process.env.AGENTSHARE_API_KEY || process.env.API_KEY || "").trim();
if (apiKey) {
  const initBody = JSON.stringify({
    jsonrpc: "2.0",
    id: 1,
    method: "initialize",
    params: {
      protocolVersion: "2024-11-05",
      capabilities: {},
      clientInfo: { name: "verify-script", version: "1.0.0" },
    },
  });
  const mcpRes = await fetch("https://agentshare.dev/mcp", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
      "X-API-Key": apiKey,
    },
    body: initBody,
  });
  if (mcpRes.status === 401) {
    fail("AGENTSHARE_API_KEY rejected (401) — check key");
  }
  if (!mcpRes.ok && mcpRes.status !== 406) {
    const t = (await mcpRes.text()).slice(0, 200);
    fail(`MCP initialize HTTP ${mcpRes.status}: ${t}`);
  }
  ok(`MCP initialize probe HTTP ${mcpRes.status}`);
} else {
  process.stdout.write("SKIP: set AGENTSHARE_API_KEY for live /mcp initialize probe\n");
}

process.stdout.write("\nAll plugin verification checks passed.\n");
