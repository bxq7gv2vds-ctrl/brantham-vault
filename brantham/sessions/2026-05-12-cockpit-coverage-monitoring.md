---
date: 2026-05-12
project: brantham
type: session
tags: [cockpit, coverage, scraping, monitoring, market-radar]
status: done
---

# Cockpit coverage monitoring

Objectif: rendre le coverage marche observable source par source. Le cockpit ne doit plus seulement deduire la fraicheur depuis `opportunities.last_seen_at`; chaque run de scrape AJ doit laisser une trace auditable.

## Changements

- Ajout de `source_runs` dans `scraper_aj.py` pour capturer, par source AJ: status, found_count, timings, erreurs.
- Ajout des tables `scrape_runs` et `scrape_source_results`.
- `cockpit.import_scan` persiste le run global et les resultats source par source, tout en gardant l'event `scan_import` existant.
- Ajout d'une carte `Coverage scrape` dans l'onglet Aujourd'hui du cockpit web.
- Ajout de `set -o pipefail` dans les scripts daily scrape pour eviter les succes silencieux via `tee`.

## Verification

- Migration `010_scrape_runs.sql` appliquee sur Supabase.
- Dernier scan reimporte: `scan-20260512-0802`, 446 opportunites, 0 nouvelles au second import idempotent, 446 rafraichies.
- Controle source: les compteurs par cabinet correspondent aux volumes trouves.
- Tests pipeline: 59 passed.
- Build cockpit-web: OK apres acces reseau pour `next/font`.

## Note

Bug trouve pendant verification: les anciens scans sans `source_aj_id` recopiaient les compteurs insert/update globaux sur chaque source. Corrige en ne matchant par ID que lorsqu'il existe, sinon fallback par nom de source.

## Related

- [[brantham/_MOC]]
- [[brantham/cockpit/roadmap-2026-05-05]]
- [[brantham/patterns/cockpit-tui-triage]]
- [[brantham/patterns/dldo-extraction-regex-fr]]
