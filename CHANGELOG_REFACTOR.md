# CHANGELOG REFACTOR

## Branche de travail

- `audit/portfolio-refactor`

## Commits chronologiques

- `91126a9` `docs: add baseline audit and refactor plan`
- `3bbf0b6` `chore: add frontend lint scaffolding and remove dead stubs`
- `475584c` `refactor: inline site shell and rebuild shared frontend styles`
- `a38c814` `docs: refresh README after frontend refactor`

## Avant / apres par lot

### Lot 0 - Audit

- Avant: aucun livrable d'audit explicite dans le depot.
- Apres: `AUDIT.md` documente les P0/P1/P2, les quick wins et les chantiers structurants.

### Lot 0bis - Plan

- Avant: pas de plan de refactor versionne dedie a ce run.
- Apres: `REFACTOR_PLAN.md` decoupe le travail en lots 1 a 5 avec objectifs, risques et DoD.

### Lot 1 - Structure

- Avant: stubs vides et non relies (`css/weather.css`, `js/weather.js`, `pages`, `readme-Local.md`, `requirements.txt`).
- Apres: stubs supprimes, `package.json` expose `lint`/`format`, `eslint.config.js` et un bootstrap ESM sont en place.

### Lot 2 - HTML

- Avant: pages dependantes de `fetch()` via `js/includes.js`, skip-links partiellement casses, `widgets.html` invalide.
- Apres: chaque page publique embarque son propre `header`/`footer`, `main#contenu`, et les liens placeholders visibles ont disparu.

### Lot 3 - CSS

- Avant: composants utilises mais non styles, redondances, `!important`, styles inline a contourner.
- Apres: `css/style.css` est recentre sur tokens, shell, composants et layouts partages qui couvrent les pages en place.

### Lot 4 - JS

- Avant: script global unique pour injecter des partials et marquer le menu.
- Apres: `js/main.js` orchestre deux modules ESM (`navigation.js`, `year.js`) limites aux enhancements non critiques.

### Lot 5 - Tooling et doc

- Avant: `README.md` decrivait encore le chargement des partials et une structure obsolete.
- Apres: `README.md` decrit le shell statique, les scripts npm utiles et les points d'entree reels.

## Validation executee

- Commande: `.\node_modules\.bin\eslint js --ext .js`
- Resultat: succes (code retour 0)
- Serveur/build: non lances

## Fichiers majeurs impactes

- `AUDIT.md`
- `REFACTOR_PLAN.md`
- `CHANGELOG_REFACTOR.md`
- `README.md`
- `package.json`
- `eslint.config.js`
- `index.html`
- `a-propos.html`
- `portfolio.html`
- `widgets.html`
- `lab/lab.html`
- `projets/Projet_Dice_Roller.html`
- `projets/Projet_DIGICHEESE.html`
- `projets/_template.html`
- `css/style.css`
- `js/main.js`
- `js/modules/navigation.js`
- `js/modules/year.js`

## Notes residuelles

- `arborescence.txt` n'a pas ete remplace pendant ce run: le fichier est encode dans un format non UTF-8 que `apply_patch` n'a pas pu relire proprement.
- Le dossier `partials/` reste present mais vide apres suppression des anciens fragments HTML.
