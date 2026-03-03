# AUDIT

## Resume executif

- Le depot ne contient pas `agent.md`, `CONTEXT_ARCHITECTURE.md` ni `RHYTHM_REFACTOR_PLAN.md`; le cadrage reel disponible est donc limite a `README.md`, `arborescence.txt` et l'arborescence du projet.
- Le frontend public repose sur 8 pages HTML (`index`, `a-propos`, `portfolio`, `widgets`, `lab`, 2 pages projet, 1 template) et sur un unique CSS (`css/style.css`) avec 2 stubs vides (`css/weather.css`, `js/weather.js`).
- La navigation et le footer dependent de `js/includes.js` et de `fetch()`, ce qui casse la navigation sans JavaScript et contredit l'objectif de progressive enhancement.
- Plusieurs pages utilisent des classes non definies dans `css/style.css` (`.cta`, `.project-grid`, `.project-card`, `.a-propos-main`, `.carre-contenu`, `.form`, `.field`, etc.), ce qui produit des rendus heterogenes et fragiles.
- `index.html` contient un script inline qui ecrit dans `#year`, mais aucun `#year` n'existe dans `partials/footer.html`; le script echoue donc a l'execution.
- `widgets.html` ferme `</body>` avant le footer, ce qui rend le document invalide.
- `portfolio.html` et `a-propos.html` ont un lien d'evitement vers `#contenu` sans cible correspondante.
- Le depot contient des stubs et fichiers orphelins vides (`pages`, `readme-Local.md`, `requirements.txt`, `css/weather.css`, `js/weather.js`) ainsi qu'un `arborescence.txt` non aligne avec l'etat reel.
- Les assets critiques existent, mais plusieurs placeholders (`href="#"`, URLs factices dans `projets/_template.html`) restent exposes dans le code.
- Le repo dispose deja de `eslint` et `prettier` dans `package.json`, mais sans configuration exploitable ni scripts de qualite.

## Priorites

| Priorite | Symptome | Cause constatee | Risque | Solution recommandee | Effort |
| --- | --- | --- | --- | --- | --- |
| P0 | Navigation et footer absents sans JS | Toutes les pages publiques injectent `partials/*.html` via `js/includes.js` et `fetch()` | Site partiellement inutilisable sans JS, UX et SEO affaiblis | Inliner un shell HTML semantique sur chaque page et reserver JS aux seules ameliorations non critiques | M |
| P0 | Erreur JS sur la home | `index.html` execute `document.getElementById("year").textContent = ...`, mais `partials/footer.html` ne contient aucun `#year` | Erreur console, maintenance plus difficile, faux positif de "script OK" | Remplacer par un mecanisme robuste (`data-current-year`) avec fallback statique | S |
| P0 | Documents HTML invalides / accessibilite incomplete | `widgets.html` place le footer hors du `body`; `a-propos.html` et `portfolio.html` n'ont pas de `id="contenu"` | Skip-link casse, structure DOM non fiable | Normaliser le shell de page (`header`, `main#contenu`, `footer`) | S |
| P1 | Styles manquants pour des classes deja utilisees | `css/style.css` ne definit pas `.cta`, `.project-grid`, `.project-card`, `.project-actions`, `.a-propos-main`, `.carre-contenu`, `.form`, `.field`, `.widget`, `.lien-icone`, `.active` | Rendus incoherents selon les pages, maintenance diffusee en inline styles | Reorganiser `style.css` en tokens + composants, supprimer les styles inline, couvrir tous les composants existants | M |
| P1 | Etat actif du menu sans effet visuel | `js/includes.js` ajoute `.active`, mais `css/style.css` ne stylise pas cette classe | Retour de navigation confus | Ajouter un style explicite pour `aria-current` / lien actif et le gerer depuis un module ESM | S |
| P1 | Liens placeholders exposes | `index.html`, `portfolio.html` et un commentaire dans `Projet_Dice_Roller.html` contiennent encore `href="#"`; `projets/_template.html` expose des URLs fictives | Impasses UX, impression de site inacheve | Remplacer par de vrais liens, du texte desactive, ou des placeholders non cliquables | S |
| P1 | Contenu "A propos" incoherent avec le reste du portfolio | `a-propos.html` reutilise encore un template orienté photo | Perte de credibilite, message brouille | Realigner la page sur le positionnement present dans `index.html` et `README.md` | M |
| P1 | Contradiction entre code et documentation | `README.md` annonce un footer avec annee dynamique et une arborescence differente de `arborescence.txt` et du depot reel | Onboarding trompeur, dette documentaire | Mettre a jour la doc structurelle apres refactor | S |
| P2 | CSS difficile a faire evoluer | Redondances dans `.pill*`, 4 usages de `!important`, grande feuille unique sans separation nette des composants | Cout de maintenance croissant | Consolider les tokens, dedoublonner les variantes et supprimer `!important` | M |
| P2 | Fichiers morts / stubs vides dans le repo | `css/weather.css`, `js/weather.js`, `pages`, `readme-Local.md`, `requirements.txt` sont vides et non relies au site | Bruit structurel, doute sur la source de verite | Supprimer ou documenter explicitement ce qui reste en attente | S |
| P2 | Tooling front sous-utilise | `package.json` n'expose qu'un `npm test` placeholder; aucun fichier de config ESLint/Prettier | Qualite non outillee, verifications manuelles | Ajouter des scripts `lint`/`format` et une config ESLint adaptee au navigateur | S |

## Quick wins (<= 1h)

- Supprimer l'appel inline a `#year` et introduire un fallback statique dans le footer.
- Corriger `widgets.html` pour remettre le footer dans le `body`.
- Ajouter `id="contenu"` sur chaque `main` cible des skip-links.
- Remplacer les `href="#"` visibles par des elements non cliquables ou de vrais liens.
- Ajouter le style du lien de navigation actif et retirer les `!important` du footer.
- Eliminer les imports Google Fonts non utilises ou les aligner avec le CSS reel.

## Chantiers structurants

- Remplacer le chargement dynamique des partials par un shell HTML semantique et resilient sans JS.
- Recomposer `css/style.css` autour de tokens, layout, composants et utilitaires documentes.
- Passer la couche JS front a un point d'entree ESM (`js/main.js`) avec modules explicites pour les enhancements.
- Nettoyer la structure du depot (stubs vides, fichiers heritage non relies, documentation stale).
- Mettre `README.md` et la documentation de refactor en phase avec la structure livree.
