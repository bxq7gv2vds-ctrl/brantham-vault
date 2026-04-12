---
date: 2026-04-12
type: session
tags: [auto-enrichment, scraping, pipeline]
---

# Session auto-enrichment — 2026-04-12 22:08

## Résumé d'exécution

| Étape | Résultat |
|-------|---------|
| Scraping AJ | OK — 436 opportunités (355 expirées supprimées) |
| Sites scrapés | 22 OK / 8 vides / 1 erreur |
| Opportunités éligibles CA >= 1M€ | 54 |
| Sans dossier existant | 0 — tous déjà traités |
| Nouveaux dossiers créés | 0 |
| Enrichissements Pappers | 0 |
| Matching repreneurs | 0 |
| Erreurs | Aucune |

## Détails scraping

- Fichier mis à jour : /Users/paul/Desktop/brantham-partners/api/aj_annonces.json
- Ancienne version : 09:14:16 (>12h) — relancé
- Nouvelle version : 2026-04-12 22:08
- 436 opportunités actives après suppression des 355 expirées

## Observation

Pipeline à jour. Les 54 opportunités éligibles (CA >= 1M€) ont toutes un dossier dans deals/. Aucune nouvelle opportunité à enrichir.

Note : le format ca_estime est en tranches textuelles ("De 1 à 3", "Plus de 10") dans le nouveau scraper, différent de l'ancien format avec montants précis.

## Related

- [[brantham/_MOC]]
- [[brantham/sessions/auto-health-2026-04-12]]
