/*
  includes.js
  - Injecte partials/header.html et partials/footer.html
  - Met le lien actif dans le menu
  - Met à jour l'année si <span id="year"></span> existe
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
    } catch {
      el.innerHTML = `<!-- include error: ${file} -->`;
    }
  }

  setActiveNavLink();
  setYear();
}

function setActiveNavLink() {
  const current = (location.pathname.split("/").pop() || "index.html").toLowerCase();

  document.querySelectorAll(".nav a").forEach((a) => {
    const href = (a.getAttribute("href") || "").split("#")[0];
    const target = href.split("/").pop().toLowerCase();

    if (target && target === current) {
      a.classList.add("active");
      a.setAttribute("aria-current", "page");
    } else {
      a.classList.remove("active");
      a.removeAttribute("aria-current");
    }
  });
}

function setYear() {
  const y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
}

document.addEventListener("DOMContentLoaded", injectPartials);
