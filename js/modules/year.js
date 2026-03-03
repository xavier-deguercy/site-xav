/**
 * Keeps footer years current while preserving a static fallback in HTML.
 */
export function syncCurrentYear(root = document) {
  const year = String(new Date().getFullYear());

  root.querySelectorAll("[data-current-year]").forEach((node) => {
    node.textContent = year;
  });
}
