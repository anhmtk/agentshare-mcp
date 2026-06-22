/**
 * Popup controller — polls public bot-traffic stats API.
 */
import { POLL_MS, statsUrl } from "./config.js";

let pollTimer = null;

function esc(s) {
  return String(s ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

function formatUtcTime(iso) {
  if (!iso) return "—";
  const d = new Date(iso);
  if (Number.isNaN(d.getTime())) return "—";
  return d.toISOString().slice(11, 19) + " UTC";
}

function setLiveState(state) {
  const dot = document.getElementById("liveDot");
  if (!dot) return;
  dot.classList.remove("ok", "err");
  if (state === "ok") dot.classList.add("ok");
  if (state === "err") dot.classList.add("err");
}

function renderLists(data) {
  const intentsEl = document.getElementById("listIntents");
  const clientsEl = document.getElementById("listClients");
  const intents = data.top_intents || [];
  const clients = data.top_clients || [];

  if (intentsEl) {
    intentsEl.innerHTML = intents.length
      ? intents
          .map(
            (r) =>
              `<li>${esc(r.intent)} <span class="count">(${r.count})</span></li>`,
          )
          .join("")
      : '<li class="empty">No intents yet</li>';
  }
  if (clientsEl) {
    clientsEl.innerHTML = clients.length
      ? clients
          .map(
            (r) =>
              `<li>${esc(r.client)} <span class="count">(${r.count})</span></li>`,
          )
          .join("")
      : '<li class="empty">No clients yet</li>';
  }
}

function renderBreakdown(data) {
  const el = document.getElementById("breakdown");
  if (!el) return;
  const b = data.traffic_breakdown || {};
  el.innerHTML = [
    `<span class="pill pill-good">Good ${b.good || 0}</span>`,
    `<span class="pill pill-suspicious">Suspicious ${b.suspicious || 0}</span>`,
    `<span class="pill pill-malicious">Malicious ${b.malicious || 0}</span>`,
    b.human ? `<span class="pill pill-human">Human ${b.human}</span>` : "",
  ].join("");
}

function renderCountries(data) {
  const el = document.getElementById("countryChips");
  if (!el) return;
  const countries = (data.countries || []).slice(0, 8);
  el.innerHTML = countries.length
    ? countries
        .map((c) => {
          const name = c.country_name || c.country || "?";
          return `<span class="chip" title="${esc(c.last_intent || "")}">${esc(name)} ${c.count}</span>`;
        })
        .join("")
    : '<span class="chip">No geo data yet</span>';
}

function renderMetrics(data) {
  const totalEl = document.getElementById("metricTotal");
  const keysEl = document.getElementById("metricKeys");
  const windowEl = document.getElementById("metricWindow");
  const statusEl = document.getElementById("statusLine");

  if (totalEl) totalEl.textContent = String(data.total_requests ?? "—");
  if (keysEl) keysEl.textContent = String(data.unique_authenticated_agents ?? "—");
  if (windowEl) {
    windowEl.textContent = `last ${data.window_minutes ?? 15} min`;
  }
  if (statusEl) {
    const ts = data.generated_at;
    statusEl.textContent = ts
      ? `Updated ${formatUtcTime(ts)} · refreshes every ${Math.round(POLL_MS / 1000)}s`
      : "Updated just now";
  }
}

function applyData(data) {
  if (!data) return;
  renderMetrics(data);
  renderBreakdown(data);
  renderLists(data);
  renderCountries(data);
  setLiveState("ok");
}

async function getApiBase() {
  try {
    const stored = await chrome.storage.sync.get(["apiBase"]);
    if (stored.apiBase && typeof stored.apiBase === "string") {
      return stored.apiBase.replace(/\/$/, "");
    }
  } catch {
    /* */
  }
  return undefined;
}

async function fetchStats() {
  const apiBase = await getApiBase();
  const url = statsUrl(apiBase);
  try {
    const res = await fetch(url, {
      credentials: "omit",
      headers: { Accept: "application/json" },
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const json = await res.json();
    applyData(json?.data);
    await chrome.storage.local.set({
      lastStats: json?.data ?? null,
      lastFetchOk: true,
      lastFetchAt: Date.now(),
    });
  } catch (e) {
    setLiveState("err");
    const statusEl = document.getElementById("statusLine");
    if (statusEl) {
      statusEl.textContent = `Unable to load (${e instanceof Error ? e.message : String(e)})`;
    }
    await chrome.storage.local.set({ lastFetchOk: false, lastFetchAt: Date.now() });
  }
}

function startPolling() {
  if (pollTimer) clearInterval(pollTimer);
  void fetchStats();
  pollTimer = setInterval(() => void fetchStats(), POLL_MS);
}

document.addEventListener("DOMContentLoaded", () => {
  void chrome.storage.local.get(["lastStats"]).then((hit) => {
    if (hit.lastStats) applyData(hit.lastStats);
  });
  startPolling();
});

document.addEventListener("visibilitychange", () => {
  if (document.hidden && pollTimer) {
    clearInterval(pollTimer);
    pollTimer = null;
  } else if (!document.hidden) {
    startPolling();
  }
});
