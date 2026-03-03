# SITE XAV

Portfolio statique de Xavier Deguercy en HTML, CSS et JavaScript natif.

## Objectif

- Presenter un profil hybride: pilotage, data et developpement.
- Garder une base simple a maintenir, sans framework ni build obligatoire.
- Prioriser le progressive enhancement: le contenu principal reste lisible sans JavaScript.

## Stack

- HTML semantique par page
- CSS centralise dans `css/style.css`
- JavaScript ESM pour les seules ameliorations non critiques (`js/main.js`)

## Structure utile

```text
.
|-- AUDIT.md
|-- REFACTOR_PLAN.md
|-- README.md
|-- index.html
|-- a-propos.html
|-- portfolio.html
|-- widgets.html
|-- css/
|   `-- style.css
|-- js/
|   |-- main.js
|   `-- modules/
|       |-- navigation.js
|       `-- year.js
|-- lab/
|   `-- lab.html
|-- projets/
|   |-- Projet_Dice_Roller.html
|   |-- Projet_DIGICHEESE.html
|   `-- _template.html
`-- assets/
    |-- docs/
    `-- img/
```

## Demarrage local

Le site est statique. Un simple serveur HTTP suffit:

```bash
py -m http.server 8000
```

Puis ouvrir:

```text
http://localhost:8000/index.html
```

## Scripts npm

Les dependances front sont deja declarees dans `package.json`.

```bash
npm run lint
npm run format
```

## Ce que fait le JavaScript

Le bootstrap `js/main.js` ne porte que des enhancements:

- marquer le lien actif dans la navigation
- synchroniser l'annee affichee dans le footer

Le rendu principal (navigation, contenu, footer) ne depend plus d'un chargement dynamique.

## Pages disponibles

- `index.html`: page d'accueil
- `a-propos.html`: positionnement et parcours
- `portfolio.html`: vue d'ensemble des projets
- `projets/*.html`: pages detail projet
- `widgets.html`: page utilitaire pour verifier les composants
- `lab/lab.html`: zone de test hors parcours principal
