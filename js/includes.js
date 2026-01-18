/*
  =============================================================
  includes.js
  -------------------------------------------------------------
  Objectif : injecter des "partials" (header/footer) dans
  les pages, pour éviter les copier-coller.

  IMPORTANT :
  - ça fonctionne uniquement via http:// (Live Server / python -m http.server)
  - pas en file:// (double-clic sur le fichier)
  =============================================================
*/

async function injectPartials() {
  const targets = document.querySelectorAll("[data-include]");

  for (const el of targets) {
    const file = el.getAttribute("data-include");
    if (!file) continue;

    try {
      const res = await fetch(file, { cache: "no-cache" });
      if (!res.ok) {
        el.innerHTML = `<!-- include failed: ${file} (${res.status}) -->`;
        continue;
      }
      el.innerHTML = await res.text();
    } catch (err) {
      el.innerHTML = `<!-- include error: ${file} -->`;
    }
  }

  // Une fois le header injecté, on peut marquer le lien actif
  setActiveNavLink();
}

function setActiveNavLink() {
  // Nom du fichier courant (ex: portfolio.html)
  const current = (location.pathname.split("/").pop() || "index.html").toLowerCase();

  // On regarde tous les liens du header injecté
  document.querySelectorAll(".nav a").forEach((a) => {
    const href = a.getAttribute("href") || "";
    const target = href.split("#")[0].split("/").pop().toLowerCase(); // retire l'ancre

    if (target && target === current) {
      a.classList.add("active");
      a.setAttribute("aria-current", "page");
    } else {
      a.classList.remove("active");
      a.removeAttribute("aria-current");
    }
  });
}

document.addEventListener("DOMContentLoaded", injectPartials);
