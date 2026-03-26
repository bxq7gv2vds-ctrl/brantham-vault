---
type: session
project: brantham
date: 2026-03-26
tags: [scraping, aj, auto-enrichment, pipeline]
---

# Auto-Enrichment AJ -- 2026-03-26

## Cycle Cron 01:17

- **Scrape AJ** : 466 opportunites sur 25/31 sites (0 erreur, 6 vides)
- **Diff** : 42 nouvelles, 65 disparues
- **Dashboard** : aj_annonces.json mis a jour
- **Enrichissement** : Pappers 0 (rate-limite), API Entreprise 5/7 top opportunites
- Stable vs veille (memes sites actifs, Asteren toujours 40 annonces)


---

## Cycle Deep Enrichment 00:58

- **Procedures identifiees** : 30 avec score > 50 sans bilan (meme liste que veille)
- **Pappers** : 15 requetes executees, 0 avec donnees financieres. Token fonctionne mais ces TPE (restauration, 3-9 salaries) n'ont pas de bilans publics sur Pappers.
- **Constat** : le top scoring est domine par des TPE restauration/hebergement (NAF 56xx/55xx) qui n'ont pas de donnees financieres publiques. L'enrichissement Pappers gratuit ne couvre pas ces petites structures.
- **Fraicheur** : recalculee OK
- **Stats** : 1065 AJ, 2739 MJ, 595 tribunaux, 2030 combinaisons

### Action necessaire
- Le scoring favorise trop la restauration — a recalibrer ou filtrer
- Pour les donnees financieres de TPE, il faudrait un token Pappers payant ou scraper les bilans INPI directement
- Les deals AJ (scan 40 sites) sont plus interessants que le top scoring DB — les gros deals (SFDPE 30M, Fonderie Niederbronn >10M, JOTT >10M) viennent du scraper, pas de la DB


## Cycle 02:13

- **Scrape AJ** : lancement...
  - OK : 466 opportunites scrapees

## Cycle 19:37

- **Scrape AJ** : lancement...
  - OK : 468 opportunites scrapees

## Deep Enrichment 19:39
