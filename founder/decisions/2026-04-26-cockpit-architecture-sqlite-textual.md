---
date: 2026-04-26
projet: brantham
type: decision
tags: [architecture, cockpit, sqlite, textual]
---

# Décision — Architecture cockpit AJ : SQLite + TUI Textual

## Contexte
Paul a besoin d'une vue unique pour trier toutes les opportunités AJ en cours, sans rien rater (DLDO obligatoire), et y greffer ensuite la recherche de repreneurs.

## Alternatives évaluées
1. **Dashboard web React** — celui qui existe dans `brantham-pipeline/server.js` (port 3000). Pro : déjà partiellement codé. Con : nécessite stack Node + React build, latence d'usage en solo, pas de raccourcis clavier puissants, surface code énorme à maintenir.
2. **Excel via `export_excel.py`** (existant). Pro : zéro nouveau code. Con : pas d'actions interactives (status updates), pas de live re-enrich, format figé.
3. **TUI Textual + SQLite locale** — choix retenu.

## Décision : SQLite + Textual
- **DB SQLite locale** (`~/.brantham/cockpit.db`, WAL + foreign keys) = source unique de vérité pour opps + repreneurs + contacts + events.
- **TUI Textual** pour le triage (raccourcis 1 char, persistance immédiate, modals pour notes/recherche).
- Modules Python découplés : `db.py` (schéma), `import_scan.py` (upsert depuis JSON scraper), `enrich_dldo.py` (parallèle), `tui.py` (UI).

## Pourquoi
- **Vélocité d'usage solo** : `j/k/s/d/o` battent n'importe quel clic souris.
- **Source unique** : le scraper, l'enrich, et bientôt les hunters repreneurs partagent la même DB. Pas de désync entre JSON files.
- **Karpathy: simplicité** : pas de microservices, pas de framework web, pas d'API. Un seul process, un seul fichier DB.
- **Persistance triviale** : `UPDATE` immédiat, pas besoin de save explicite.
- **Extensible Phase B/C** : ajouter table `repreneurs` + vue détail dans le TUI = quelques heures.

## Trade-off accepté
- **Pas multi-user** : si Soren veut accéder, il faut soit shipper la DB, soit un layer API. Pour l'instant, Paul est seul opérateur.
- **Pas de remote** : DB locale, pas accessible via web. Si besoin mobile → re-évaluer Phase D.

## Conséquences
- L'ancien `OPPORTUNITIES.md` du pipeline OpenClaw n'est plus la source de vérité — il devient un artefact secondaire pour les agents Scout/Director si on les réactive.
- Les statuts utilisateur (shortlist/poubelle/note) sont préservés entre re-imports du scraper grâce à l'upsert conditionnel.

## Validé par
Paul — session 2026-04-26.

## Related
- [[_system/MOC-decisions]]
- [[brantham/_MOC]]
- [[brantham/sessions/2026-04-26-cockpit-aj]]
- [[brantham/patterns/cockpit-tui-triage]]
