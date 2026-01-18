/*
  =============================================================
  includes.js
  -------------------------------------------------------------
  Objectif : éviter de dupliquer le même header/footer sur
  toutes les pages (logique "modulaire" comme en Python).

  Fonctionnement :
  - dans tes pages, tu mets :
      <div data-include="partials/header.html"></div>
      <div data-include="partials/footer.html"></div>
  - ce script fetch les fichiers et injecte le HTML.

  IMPORTANT :
  - fetch NE marche pas en file:// sur beaucoup de navigateurs.
    -> utilise VSCode Live Server OU :
       python -m http.server 8000
       puis ouvre http://localhost:8000
  =============================================================
*/

async function injectPartials() {
  const targets = document.querySelectorAll('[data-include]');

  for (const el of targets) {
    const file = el.getAttribute('data-include');
    if (!file) continue;

    try {
      const res = await fetch(file, { cache: 'no-cache' });
      if (!res.ok) {
        el.innerHTML = `<!-- include failed: ${file} (${res.status}) -->`;
        continue;
      }
      el.innerHTML = await res.text();
    } catch (err) {
      el.innerHTML = `<!-- include error: ${file} -->`;
    }
  }

  // Une fois le header injecté, on peut marquer la page active dans le menu.
  setActiveNavLink();
}

function setActiveNavLink() {
  // ex: /xav-portfolio/portfolio.html -> portfolio.html
  const current = (location.pathname.split('/').pop() || 'index.html').toLowerCase();

  document.querySelectorAll('a[data-nav]').forEach((a) => {
    const target = (a.getAttribute('data-nav') || '').toLowerCase();

    if (target === current) {
      a.classList.add('active');
      a.classList.add('nav-link');
      a.setAttribute('aria-current', 'page');
    } else {
      a.classList.add('nav-link');
      a.removeAttribute('aria-current');
    }
  });
}

document.addEventListener('DOMContentLoaded', injectPartials);
