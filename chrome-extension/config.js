/**
 * Shared defaults — background + popup.
 */
export const DEFAULT_API_BASE = "https://agentshare.dev";
export const STATS_PATH = "/api/v1/public/bot-traffic/stats";
export const POLL_MS = 12000;
export const BADGE_ALARM_MINUTES = 1;

export function statsUrl(apiBase = DEFAULT_API_BASE) {
  return `${apiBase.replace(/\/$/, "")}${STATS_PATH}`;
}
