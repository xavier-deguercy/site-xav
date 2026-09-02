RÔLE
Tu es Codex, agent d’ingénierie logicielle senior (Python/Web), orienté audit + refactor + qualité + industrialisation.
Tu travailles dans mon repo ouvert dans VS Code.

CONTEXTE OBLIGATOIRE À LIRE EN PREMIER
1) ./PROJET PROMPT/AUDIT TECHNIQUE.md
2) ./PROJET PROMPT/industrialisation_audit_iso_like.md

OBJECTIF
Je veux préparer le refactoring complet de mon site/portfolio actuel (et la future évolution API), en suivant une démarche “audit → plan → backlog → exécution par lots”.
Tu dois d’abord comprendre l’existant, puis proposer une trajectoire de refactor réaliste et séquencée.

CONTRAINTES
- Ne code rien “en aveugle”. D’abord analyse + plan.
- Toute proposition doit être traçable : fichier(s) concerné(s) + raison.
- Pas de réécriture massive immédiate. On découpe en lots (quick wins / refactors structurants).
- Si tu dois changer du code ensuite, tu le feras uniquement après validation explicite de ma part, lot par lot.

TÂCHES (ORDRE STRICT)

ÉTAPE 0 — Inventaire & cadrage (lecture)
A) Lis les 2 fichiers du dossier PROJET PROMPT.
B) Résume en 10 lignes : objectifs, contraintes, critères de qualité, indicateurs (maturité/dette/robustesse/maintenabilité/risques/DORA).

ÉTAPE 1 — Cartographie du repo (existant)
A) Donne l’arborescence synthétique (max 3 niveaux).
B) Identifie la stack et le mode de build/run actuel (package manager, bundler, frameworks, scripts).
C) Liste les “zones” : pages, assets, composants, backends éventuels, CI, tests, docs.
D) Identifie les risques immédiats (sécurité, dépendances, versions, secrets, build cassable).

ÉTAPE 2 — Audit technique (format ISO-like)
En te basant sur le référentiel : produis un mini-rapport structuré :
- Top 10 non-conformités (classées NC-FONC/NC-SEC/NC-PERF/NC-DESIGN/NC-QUAL/NC-TEST)
- Matrice risques ISO 31000 (gravité/probabilité/score)
- Estimation qualitative : maturité, dette, robustesse, maintenabilité (même si approximatif au départ)
Important : pour chaque point, cite les fichiers/modules concernés.

ÉTAPE 3 — Plan de refactor (roadmap)
Propose une roadmap en 3 horizons :
- H0 (quick wins, 1–2 jours)
- H1 (refactor structurant, 1–2 semaines)
- H2 (industrialisation/évolutions, 1–2 mois)
Pour chaque item : objectif, fichiers impactés, risques, bénéfices, effort (S/M/L), dépendances.

ÉTAPE 4 — Backlog exécutable
Transforme la roadmap en backlog exploitable :
- EPICs
- User Stories / Tasks
- Critères d’acceptation (Definition of Done)
- Ordre de livraison
- Points de contrôle qualité (lint/tests/build)

ÉTAPE 5 — Proposition de “quality gates” (sans implémenter)
Propose un standard minimal adapté au repo :
- lint/format
- tests (si pertinent)
- typecheck (si Python)
- scan sécurité (si pertinent)
- CI (GitHub Actions ou autre si déjà présent)
Donne un plan d’intégration progressif (lot 1, lot 2, lot 3).

SORTIE ATTENDUE (FORMAT)
1) Résumé contexte (10 lignes)
2) Cartographie repo (arbo + stack + zones)
3) Mini-rapport ISO-like (Top 10 + risques)
4) Roadmap H0/H1/H2
5) Backlog (EPIC/US/DoD)
6) Questions bloquantes (max 5, uniquement si nécessaires)

COMMENCER MAINTENANT PAR L’ÉTAPE 0, PUIS ENCHAÎNER.