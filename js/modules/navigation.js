/**
 * Marks the active navigation link from the current page context.
 * Pages can override the default match with `data-nav-context` on <body>.
 */
export function syncActiveNavigation(root = document) {
  const links = root.querySelectorAll("[data-nav-link]");
  if (!links.length) {
    return;
  }

  const currentUrl = new URL(window.location.href);
  const defaultRoute = currentUrl.pathname.split("/").pop() || "index.html";
  const currentRoute =
    root.body?.dataset.navContext?.trim().toLowerCase() || defaultRoute;

  links.forEach((link) => {
    const linkRoute = (link.dataset.navLink || "").trim().toLowerCase();
    const isActive = linkRoute === currentRoute;

    link.classList.toggle("is-active", isActive);
    if (isActive) {
      link.setAttribute("aria-current", "page");
      return;
    }

    link.removeAttribute("aria-current");
  });
}
