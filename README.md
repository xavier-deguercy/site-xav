```md
# SITE XAV — Portfolio personnel  
**HTML / CSS / JavaScript (site statique modulaire)**

Portfolio de **Xavier Deguercy** présentant le profil, le parcours et une sélection de projets (data / dev / pilotage).  
Le site est volontairement **sans framework**, avec une logique **modulaire et maintenable** inspirée des pratiques de développement logiciel (factorisation, conventions, workflow Git).

---

## 🎯 Objectifs du projet

- Disposer d’un **site simple à maintenir** (éviter le copier-coller du header/footer)
- Rester **100 % statique** (compatible GitHub Pages)
- Avoir un **code lisible et commenté**
- Permettre des **itérations rapides** (UI, contenu, nouvelles pages)
- Appliquer un **process de gestion de projet** (branches, commits, backlog)

---

## 🧱 Stack technique

- **HTML** : pages statiques
- **CSS** : design system léger, responsive
- **JavaScript** : injection des partials (header/footer), menu actif, année

Aucun framework, aucun build obligatoire.

---

## 🗂️ Arborescence du projet

```

.
├── index.html                # page d’accueil
├── a-propos.html             # page “À propos”
├── portfolio.html            # page projets
├── partials/
│   ├── header.html           # header factorisé (navigation)
│   └── footer.html           # footer factorisé (liens, année)
├── css/
│   ├── style.css             # CSS officiel (source de vérité)
│   └── style-v222.css        # (option) variantes / tests
├── js/
│   └── includes.js           # injection des partials + logique UI
├── assets/
│   ├── img/                  # images (portrait, visuels projets)
│   └── docs/                 # CV PDF, documents téléchargeables
├── contenu/                  # contenus ou brouillons (selon usage)
├── lab/                      # bac à sable / tests (non référencé)
├── README.md
└── .gitignore

````

---

## 🚀 Démarrage rapide (local)

### Pourquoi un serveur local ?
Les partials (`header.html`, `footer.html`) sont injectés via `fetch()` (JS).  
`fetch()` **ne fonctionne pas correctement** en `file://` (double-clic).

### Option A — VS Code Live Server (recommandé)
1. Installer l’extension **Live Server**
2. Clic droit sur `index.html` → **Open with Live Server**

### Option B — Python
Depuis la racine du repo :

```bash
py -m http.server 8000
````

Puis ouvrir :

```

```

---

## 🧩 Fonctionnement des partials (header / footer)

Dans chaque page HTML :

```html
<div data-include="partials/header.html"></div>

<main>
  <!-- contenu spécifique de la page -->
</main>

<div data-include="partials/footer.html"></div>

<script src="js/includes.js" defer></script>
```

### Rôle de `js/includes.js`

* Charge et injecte les fichiers `partials/*.html`
* Met en surbrillance le lien actif du menu (`.active`)
* Met à jour l’année si `<span id="year"></span>` est présent

👉 Le menu et le footer ne sont modifiés **qu’une seule fois**.

---

## 🎨 Design system (référence)

### Couleurs

* **Fond principal** : `#0b1020`
* **Surface / cartes** : `#111a33`
* **Texte principal** : `rgba(255,255,255,.92)`
* **Texte secondaire** : `rgba(255,255,255,.72)`
* **Accent primaire** : `#f9ba00`
* **Accent secondaire (hover)** : `#ffcf4a`
* **Succès** : `#35d07f`

### Typographies

* Font stack système (rapide, lisible) :

  ```
  system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Arial
  ```

### Spacing & layout

* Largeur max container : `1100px`
* Rayon standard : `18px`
* Rayon small : `12px`
* Grilles CSS : 1 / 2 / 3 colonnes selon viewport
* Mobile-first + media queries simples

### Composants standard

* `.container`
* `.card`
* `.btn`, `.btn.primary`, `.btn.ghost`
* `.pill`
* `.nav`, `.nav a.active`

---

## 📐 Bonnes pratiques appliquées

* **Un seul CSS officiel** : `css/style.css`
* **Chemins relatifs simples** (compatibles GitHub Pages)
* **Noms de fichiers sans espaces**
* **Code commenté** pour la compréhension
* **Dossier `lab/`** pour les tests (non référencé dans le site)

Optionnel (pour éviter indexation des tests) :

```html
<meta name="robots" content="noindex, nofollow">
```

---

## 🧪 Dépannage rapide

### Header / footer non visibles

* Vérifier que le site est servi via `http://` (pas en double-clic)
* Tester directement :

  ```
  http://localhost:8000/partials/header.html
  ```

### Menu actif non surligné

* Vérifier que `includes.js` est bien chargé
* Vérifier la présence de la classe `.active` dans le CSS

### Année absente dans le footer

* Vérifier la présence de :

  ```html
  <span id="year"></span>
  ```

---

## 🧭 Workflow Git recommandé

* Branche de travail : `dev/xavier`
* Branche stable : `main`
* Commits courts et explicites (Conventional Commits)

Exemple :

```bash
git checkout dev/xavier
git add -A
git commit -m "refactor: standardise css and use header/footer partials"
```

---

## ✅ Définition de Done (DoD)

Une évolution est considérée comme **terminée** si :

* [x] Le site s’affiche correctement via serveur local
* [ ] Aucune page ne duplique le header/footer
* [ ] Tous les liens fonctionnent
* [x] Le CSS utilisé est `css/style.css`
* [ ] Aucun fichier de test n’est référencé (lab)
* [ ] Les commits sont clairs et ciblés
* [ ] La branche est prête à être mergée dans `main`

---

## 🗃️ Mini backlog (issues prêtes à créer)

### UI / UX

* [ ] Uniformiser toutes les pages sur `style.css`
* [ ] Ajouter un état `hover`/`active` visible pour le menu
* [ ] Améliorer l’accessibilité (focus, contrastes)

### Contenu

* [ ] Ajouter un CV PDF dans `assets/docs/`
* [ ] Rédiger des cartes projets (problème → solution → stack)
* [ ] Ajouter une section “Disponibilité / Contact”

### Technique

* [ ] Nettoyer les variantes CSS inutilisées
* [ ] Ajouter une page projet détaillée (template)
* [ ] (Option) Génération statique via script Python (Jinja2)

---

## 📌 Auteur

**Xavier Deguercy**
GitHub : [https://github.com/xavier-deguercy](https://github.com/xavier-deguercy)

---

> Ce repo sert à la fois de **portfolio** et de **support pédagogique** pour appliquer de bonnes pratiques de développement et de gestion de projet.

```
```
