---
type: session
project: website
date: 2026-05-21
tags: [seo, geo, autopilot, deploy]
---

# Session — Infrastructure domination SEO/GEO

## Objectif
Mettre en place l'infrastructure technique pour ranker #1 Google + citations IA sur reprise entreprise / reprise à la barre.

## Implémenté

### Autopilot (automatisé quotidiennement)
- `internal_links.py` : `apply_links()` branché — 5 liens/jour orphelines → pages fortes
- `llms_sync.py` : regénère `llms-full.txt` à chaque run
- `daily.py` : Google Indexing API sur changed + orphans (si clé GSC présente)
- `vault_report.py` : fix crash CLS None

### Fichiers site
- `llms-full.txt` généré (46 Ko, 134 pages indexées)
- `llms.txt` réécrit (instructions IA + table requêtes)
- `index.html` : schema Organization enrichi (@id, founder, WebSite, ProfessionalService lié)
- `robots.txt` : commentaires llms discovery
- 6 liens internes autopilot appliqués (pages fortes → multiples-ebitda)
- FAQ homepage : liens sourcing-proprietaire + reprise-a-la-barre

### Meta
- `fix_metadesc.py` + `fix_titles_v2.py` exécutés

### Deploy
- 2 deploys prod Vercel OK

## Bloqué (action humaine requise)
- Service account GSC absent → pas de snapshot live, pas d'indexation Google API
- Backlinks / LinkedIn / presse = 60 % de l'effort restant pour #1

## Related
- [[website/strategies/2026-05-21-domination-google-ia-reprise-barre]]
- [[website/bugs/2026-05-21-p0-seo-fixes]]
- [[website/_MOC]]
