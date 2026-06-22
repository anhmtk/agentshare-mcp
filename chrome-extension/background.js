/**
 * MV3 service worker — toolbar badge from public stats (optional pulse).
 */
import { BADGE_ALARM_MINUTES, statsUrl } from "./config.js";

const ALARM_NAME = "agentshare-traffic-poll";

async function getApiBase() {
  const stored = await chrome.storage.sync.get(["apiBase"]);
  const base = stored.apiBase;
  return typeof base === "string" && base.trim() ? base.trim().replace(/\/$/, "") : undefined;
}

async function refreshBadge() {
  const url = statsUrl(await getApiBase());
  try {
    const res = await fetch(url, {
      credentials: "omit",
      headers: { Accept: "application/json" },
    });
    if (!res.ok) throw new Error(String(res.status));
    const json = await res.json();
    const data = json?.data;
    const total = Number(data?.total_requests ?? 0);
    const text = total > 0 ? (total > 99 ? "99+" : String(total)) : "";
    await chrome.action.setBadgeText({ text });
    await chrome.action.setBadgeBackgroundColor({ color: total > 0 ? "#15803d" : "#64748b" });
    await chrome.storage.local.set({
      lastStats: data ?? null,
      lastFetchOk: true,
      lastFetchAt: Date.now(),
    });
  } catch {
    await chrome.action.setBadgeText({ text: "!" });
    await chrome.action.setBadgeBackgroundColor({ color: "#dc2626" });
    await chrome.storage.local.set({ lastFetchOk: false, lastFetchAt: Date.now() });
  }
}

chrome.runtime.onInstalled.addListener(() => {
  chrome.alarms.create(ALARM_NAME, { periodInMinutes: BADGE_ALARM_MINUTES });
  void refreshBadge();
});

chrome.alarms.onAlarm.addListener((alarm) => {
  if (alarm.name === ALARM_NAME) void refreshBadge();
});

chrome.runtime.onStartup.addListener(() => {
  void refreshBadge();
});
