# REFACTOR PLAN

## Lot 1 - Structure

**Objectif**  
Reduire le bruit structurel et preparer un shell front plus lisible.

**Taches**
- Ajouter `AUDIT.md` et `REFACTOR_PLAN.md`.
- Introduire une entree JS ESM (`js/main.js`) et des modules dedies.
- Nettoyer les fichiers vides ou obsoletes non relies au site.
- Mettre a jour `package.json` pour exposer les scripts de qualite.

**Fichiers impactes**
- `AUDIT.md`
- `REFACTOR_PLAN.md`
- `package.json`
- `js/`
- fichiers vides / heritage identifies pendant l'audit

**Risques**
- Suppression d'un stub que l'utilisateur comptait reutiliser.

**Definition of Done**
- La structure cible est explicite.
- Les nouveaux points d'entree sont presents et documentes.
- Les fichiers manifestement orphelins sont supprimes ou assumes.

## Lot 2 - HTML

**Objectif**  
Rendre chaque page semantique, autonome et utilisable sans JavaScript.

**Taches**
- Inliner un `header` + `footer` directement dans chaque page publique.
- Normaliser `main#contenu`, les skip-links, les titres et les meta descriptions.
- Corriger les placeholders de liens visibles.
- Recentrer `a-propos.html` et `widgets.html` sur le portfolio reel.

**Fichiers impactes**
- `index.html`
- `a-propos.html`
- `portfolio.html`
- `widgets.html`
- `lab/lab.html`
- `projets/*.html`

**Risques**
- Divergence future entre shell des pages racine et shell des pages imbriquees.

**Definition of Done**
- Aucune page publique ne depend de `fetch()` pour afficher la navigation.
- Aucun `href="#"` visible ne subsiste.
- Les skip-links ont tous une cible valide.

## Lot 3 - CSS

**Objectif**  
Unifier le design system autour de tokens et de composants couverts par les pages existantes.

**Taches**
- Reorganiser `css/style.css` par sections stables (tokens, base, layout, composants, pages).
- Ajouter les styles manquants pour les composants utilises.
- Supprimer les `!important` et les styles inline remplaces par des classes.
- Garder un rendu proche de l'existant, sans refonte visuelle gratuite.

**Fichiers impactes**
- `css/style.css`
- pages HTML qui consomment les nouvelles classes

**Risques**
- Regression responsive si des classes historiques sont oubliees.

**Definition of Done**
- Les composants visibles du site ont un style centralise.
- Les pages n'utilisent plus de styles inline evitables.
- Le menu actif et les etats focus sont visibles.

## Lot 4 - JS

**Objectif**  
Passer d'un script global de chargement a des modules ESM d'amelioration progressive.

**Taches**
- Remplacer `js/includes.js` par un bootstrap ESM.
- Isoler la logique de navigation active et de synchronisation de l'annee.
- Ajouter des commentaires pedagogiques JSDoc sur les contrats durables.

**Fichiers impactes**
- `js/main.js`
- `js/modules/*.js`
- pages HTML qui chargent le script

**Risques**
- Mauvais chemin relatif entre pages racine et pages imbriquees.

**Definition of Done**
- Aucun symbole global n'est requis pour le rendu de base.
- La navigation active et l'annee fonctionnent comme enhancements.
- Le site reste lisible si le JS ne charge pas.

## Lot 5 - Tooling et documentation

**Objectif**  
Laisser une base maintenable, documentee et verifiable.

**Taches**
- Ajouter une configuration ESLint browser/ESM minimale.
- Mettre `README.md` a jour selon la structure finale.
- Produire `CHANGELOG_REFACTOR.md` avec l'historique des lots et des validations.

**Fichiers impactes**
- `eslint.config.js`
- `README.md`
- `CHANGELOG_REFACTOR.md`

**Risques**
- Documentation qui derive si les derniers ajustements ne sont pas reportes.

**Definition of Done**
- Les scripts npm utiles sont documentes.
- La doc de structure correspond au depot reel.
- Le changelog de refactor permet de rejouer les decisions.

## Ordre de commits recommande

1. `docs: add baseline audit and refactor plan`
2. `chore: clean dead frontend stubs and add lint scaffolding`
3. `refactor: inline shared site shell for progressive enhancement`
4. `refactor: normalize portfolio pages and remove placeholder links`
5. `refactor: rebuild design system styles around shared components`
6. `refactor: replace global includes script with esm enhancements`
7. `docs: refresh README and add refactor changelog`
