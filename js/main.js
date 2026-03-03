import { syncActiveNavigation } from "./modules/navigation.js";
import { syncCurrentYear } from "./modules/year.js";

/**
 * Bootstraps only non-essential behaviors.
 * The HTML stays fully usable if this module never runs.
 */
function initSiteEnhancements() {
  syncActiveNavigation();
  syncCurrentYear();
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initSiteEnhancements, {
    once: true
  });
} else {
  initSiteEnhancements();
}
