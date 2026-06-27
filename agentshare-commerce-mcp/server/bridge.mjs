/**
 * Stdio (Cursor / Claude Desktop) ↔ Streamable HTTP bridge for AgentShare /mcp.
 *
 * Cursor plugin cwd: agentshare-commerce-mcp/ — run as:
 *   node server/bridge.mjs https://agentshare.dev/mcp --header X-API-Key:agshp_...
 * or set env AGENTSHARE_API_KEY (see mcp.json).
 */
import process from "node:process";
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const ENV_KEY_NAMES = ["AGENTSHARE_API_KEY", "API_KEY", "X_API_KEY"];

function usage() {
  process.stderr.write(
    "Usage: node server/bridge.mjs <https://host/mcp> [--header Name:value] ...\n" +
      "  API key: --header X-API-Key:agshp_...  or  env AGENTSHARE_API_KEY\n"
  );
}

function readEnvApiKey() {
  for (const name of ENV_KEY_NAMES) {
    const v = (process.env[name] || "").trim();
    if (v) {
      return v;
    }
  }
  const auth = (process.env.Authorization || process.env.AUTHORIZATION || "").trim();
  if (auth.toLowerCase().startsWith("bearer ")) {
    return auth.slice(7).trim();
  }
  return "";
}

function parseArgs(argv) {
  /** @type {Record<string, string>} */
  const hdr = {};
  let url = "";
  for (let i = 0; i < argv.length; i += 1) {
    const a = argv[i];
    if (a === "--header" && argv[i + 1]) {
      i += 1;
      const raw = argv[i];
      const colon = raw.indexOf(":");
      if (colon > 0) {
        const k = raw.slice(0, colon).trim();
        const v = raw.slice(colon + 1).trim();
        hdr[k] = v;
      }
    } else if (!url && !a.startsWith("--")) {
      url = a;
    }
  }
  return { url, headers: hdr };
}

/** Resolve ${AGENTSHARE_API_KEY} placeholders and empty header values from env. */
function applyEnvApiKey(headers) {
  const envKey = readEnvApiKey();
  if (!envKey) {
    return headers;
  }
  const out = { ...headers };
  for (const [k, v] of Object.entries(out)) {
    if (!v || v === "${AGENTSHARE_API_KEY}" || v.includes("${AGENTSHARE_API_KEY}")) {
      out[k] = envKey;
    }
  }
  if (!out["X-API-Key"] && !out["Authorization"]) {
    out["X-API-Key"] = envKey;
  }
  return out;
}

function applyProtocolVersion(transport, msg) {
  const r = msg && msg.result;
  if (r && typeof r === "object" && r.protocolVersion != null) {
    transport.setProtocolVersion(String(r.protocolVersion));
  }
}

const { url, headers: parsedHeaders } = parseArgs(process.argv.slice(2));
if (!url) {
  usage();
  process.exit(1);
}

const headers = applyEnvApiKey(parsedHeaders);

const headerInit = new Headers({
  Accept: "application/json, text/event-stream",
});
for (const [k, v] of Object.entries(headers)) {
  if (v) {
    headerInit.set(k, v);
  }
}

const local = new StdioServerTransport();
const remote = new StreamableHTTPClientTransport(new URL(url), {
  requestInit: { headers: headerInit },
});

await remote.start();

local.onmessage = (msg) => {
  try {
    if (msg && msg.method === "initialize" && msg.params && msg.params.clientInfo) {
      const ci = msg.params.clientInfo;
      msg.params.clientInfo = {
        ...ci,
        name: `${ci.name || "cursor"} (agentshare-cursor-plugin)`,
      };
    }
    remote.send(msg).catch((err) => {
      process.stderr.write(`[bridge] remote send error: ${err}\n`);
    });
  } catch (err) {
    process.stderr.write(`[bridge] local onmessage: ${err}\n`);
  }
};

remote.onmessage = (msg) => {
  try {
    applyProtocolVersion(remote, msg);
    local.send(msg).catch((err) => {
      process.stderr.write(`[bridge] local send error: ${err}\n`);
    });
  } catch (err) {
    process.stderr.write(`[bridge] remote onmessage: ${err}\n`);
  }
};

let closing = false;
function shutdown() {
  if (closing) return;
  closing = true;
  remote.close().catch(() => {});
  local.close().catch(() => {});
}

local.onclose = () => shutdown();
remote.onclose = () => shutdown();
local.onerror = (e) => process.stderr.write(`[bridge] local transport error: ${e}\n`);
remote.onerror = (e) => process.stderr.write(`[bridge] remote transport error: ${e}\n`);

process.on("SIGINT", shutdown);
process.on("SIGTERM", shutdown);

await local.start();
