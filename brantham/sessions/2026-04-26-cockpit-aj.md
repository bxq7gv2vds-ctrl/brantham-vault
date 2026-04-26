---
date: 2026-04-26
projet: brantham
type: session
tags: [cockpit, scraper, dldo, textual, sqlite]
---

# Session — Cockpit AJ + Scraper Fixes

## Contexte
Pain principal de Paul : ne rien rater des opportunités AJ et avoir une vue propre, triable, des deals en cours. Le scraper existant (`scraper_aj.py`, 1734 lignes, 31 sites) n'avait pas tourné depuis le 25 mars → 117 opps loupées en 1 mois.

## Diagnostic
Run du scraper existant : 25/31 sites OK (473 opps), 5 vides, 1 erreur (BVP).
Vérifications avec Obscura/LightPanda + curl :
- Adjust, KSG, MM AJ : vraiment vides (`Aucune reprise`, `No result` dans le HTML rendu)
- AJ Partenaires : vraiment vide (`Il n'y a aucune offre de reprise d'entreprise pour le moment`)
- **Maydaymag** : MISS confirmé — URL erronée + besoin JS rendering. 11 opps réelles ratées.
- BVP : domaine `etude-bpv.fr` mort

## Fixes scraper
1. **BVP désactivé** (`scraper_aj.py:117`) — domaine 404 depuis ≥25 scans
2. **Mayday réécrit** (`scraper_aj.py:138`, `scraper_aj.py:697`) — URL → `/les-entreprises-a-reprendre/`, parser via `lp.fetch_html` (LightPanda), extraction h2/h3 avec filtre sentinelles. **+11 opps réelles**.
3. **AJ Spécialisés URL bug** — concat URL ratait le slash → `aj-specialises.frsociete-fiche.php`. Fix dans `scrape_custom` (4 occurrences via `replace_all`)
4. **Ajilink portail** — 25 faux positifs (liens "bureaux" Aix/Bordeaux/Créteil), désactivé (les vraies offres sont déjà scrapées via les sous-domaines régionaux)

## Architecture cockpit
DB SQLite unique : `~/.brantham/cockpit.db` (WAL, FK enabled).

Module Python : `/Users/paul/Downloads/brantham-pipeline/cockpit/`
- `db.py` — schéma (opportunities, repreneurs, contacts, events) + helpers
- `import_scan.py` — upsert scan JSON → DB (préserve user_status/note entre runs)
- `enrich_dldo.py` — extraction DLDO regex multi-format FR (numérique + lettré), parallèle 8 workers, stratégie 3 niveaux (URL → notes → page détail)
- `tui.py` — Textual app
- `__main__.py` — entry point `python -m cockpit`

## DLDO enrich — 91.3% coverage
Patterns regex couvrent 8 formulations FR + dates numériques (DD/MM/YYYY, DD/MM/YY) et lettrées ("16 avril 2026", "16 avr. 2026").
Bug initial corrigé : alternation `\d{2}|\d{4}` mangeait toujours 2 digits → forcé `\d{4}|\d{2}`.

Sanity check final : refuse seulement >5 ans passé ou >2 ans futur (dates expirées gardées pour le filtre actif/expiré).

## TUI Textual
Tri par défaut : DLDO ascendant (urgences en haut, J-7 rouge gras).
Filtres :
- `f` cycle status : all / nouveau / shortlist / archive
- `x` cycle vie : **actives (défaut)** / expirees / sans_dldo / tout
- `p` toggle bin (poubelle cachée par défaut)
- `/` recherche libre

Actions : `s` shortlist, `d` poubelle, `r` reset, `o` ouvrir URL, `n` note (modal), `e` re-enrich live.

Persistance : tous les changements écrits dans la DB SQLite (statuts survivent aux restarts et aux re-imports).

## Stats finales
- **459 opps** (après cleanup)
- **419 DLDO parsées (91.3%)**
- **200 ACTIVES** / **259 EXPIRÉES** / **47 URGENTES (J-7)**
- 30 sites actifs

## Outils alerting
- `diff_scan.py` étendu avec section **silent_breakage** : site qui passe de N>0 à 0 entre 2 scans (= parser cassé). Affiché en sortie texte + JSON.
- `view_scan.py` : viewer HTML standalone (alternatif au TUI), généré dans `/tmp/`.

## Prochaine étape — Phase B Hunters repreneurs
Pour chaque opp shortlist, identifier les meilleurs repreneurs en 4 angles :
1. Concurrents directs (Pappers MCP par NAF + filtres CA/géo)
2. PE/Holdings sériels (pré-catalogue ~80 acteurs FR)
3. Acquéreurs sériels (BODACC ≥3 acquisitions secteur 3 ans)
4. Verticaux (Pappers cartographie clients/fournisseurs)

Score fit : synergie NAF (30%) + capacité financière (30%) + géo (15%) + activité M&A (25%).

## Décisions
- [[founder/decisions/2026-04-26-cockpit-architecture-sqlite-textual]]

## Patterns nés
- [[brantham/patterns/cockpit-tui-triage]]
- [[brantham/patterns/dldo-extraction-regex-fr]]

## Bugs fixés
- [[brantham/bugs/2026-04-26-mayday-url-js-rendering]]
- [[brantham/bugs/2026-04-26-aj-specialises-url-slash-manquant]]
- [[brantham/bugs/2026-04-26-ajilink-portail-faux-positifs]]

## Related
- [[brantham/_MOC]]
- [[_system/MOC-bugs]]
- [[_system/MOC-patterns]]
