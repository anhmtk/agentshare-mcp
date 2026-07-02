#!/usr/bin/env node
/**
 * Print Cursor MCP one-click install deeplink for agentshare.dev/mcp
 * Usage: node scripts/cursor-deeplink.mjs
 */
const config = {
  url: "https://agentshare.dev/mcp",
  headers: {
    "X-API-Key": "YOUR_AGENTSHARE_API_KEY",
  },
};

const b64 = Buffer.from(JSON.stringify(config)).toString("base64");
const name = "agentshare";
const deeplink = `cursor://anysphere.cursor-deeplink/mcp/install?name=${name}&config=${b64}`;

console.log("Config JSON:");
console.log(JSON.stringify(config, null, 2));
console.log("\nBase64 config:");
console.log(b64);
console.log("\nCursor deep link (paste into cursor.directory or share):");
console.log(deeplink);
