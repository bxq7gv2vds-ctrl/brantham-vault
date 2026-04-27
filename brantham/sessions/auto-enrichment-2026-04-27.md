---
date: 2026-04-27
type: session
projet: brantham
tags: [enrichment, aj-scrape, pipeline]
---

# Session Auto-Enrichment — 2026-04-27

## Résumé

| Métrique | Valeur |
|----------|--------|
| Opportunités scrapées | 461 (40 sites AJ) |
| Qualifiées CA>500K ou score>60 | 19 |
| Sans dossier existant | 14 |
| Deals créés | 10 |
| Enrichissement API gouvernement | 5/10 réussis |
| Enrichissement pappers | 0 (pas de SIREN dans les annonces) |
| Erreurs | Rate limit API gov sur 5 requêtes |
| Repreneurs identifiés | 0 (API gov rate-limitée) |

## Deals traités

| # | Nom | CA | Effectif | AJ | Dossier |
|---|-----|-----|---------|-----|---------|
| 1 | Papier et électricité | 204,4 M€ | 268 salariés | Abitbol & Rousselet | `abitbol-rousselet-papier-et-electricite` |
| 2 | Produits électroniques | 30,7 M€ | 20 salariés | Abitbol & Rousselet | `abitbol-rousselet-produits-electroniques` |
| 3 | Viticulture | 14 M€ | 140 salariés | Abitbol & Rousselet | `abitbol-rousselet-viticulture` |
| 4 | Editeur du titre de presse professi | 8,2 M€ | 97 salariés | 2M&Associés | `2m-associes-editeur-du-titre-de-presse-p` |
| 5 | Clinique de soins médicaux et de ré | 6,6 M€ | 90 salariés | Abitbol & Rousselet | `abitbol-rousselet-clinique-de-soins-medi` |
| 6 | Transport routier, fret de proximit | 4 316 K€ | 26 salariés | AJ UP | `aj-up-transport-routier-fret-de-proximit` |
| 7 | Restauration | 3,4 M€ | 34 salariés | Abitbol & Rousselet | `abitbol-rousselet-restauration` |
| 8 | Pâtisserie | 2,8 M€ | 39 salariés | Abitbol & Rousselet | `abitbol-rousselet-patisserie` |
| 9 | Société de conseil spécialisée dans | 2 646 K€ | 15 salariés | AJ Associés | `aj-associes-societe-de-conseil-specialis` |
| 10 | Cloud Computing | 2,3 M€ | 40 salariés | Abitbol & Rousselet | `abitbol-rousselet-cloud-computing` |

## Scraper AJ
- Fichier : `/Users/paul/Desktop/brantham-partners/api/aj_annonces.json`
- Âge avant relance : 8.1h (seuil 3h)
- Scrape déclenché : oui
- Résultat : 461 opportunités (était 1853 dans l'ancien format)

## Problèmes rencontrés
- API gouvernement rate-limitée après 5 requêtes (HTTP 429)
- Pas de SIREN disponible dans les annonces AJ scrapeées
- FastAPI backend down (port 8000) — matching repreneurs 4D impossible
- Enrichissement Pappers non effectué (pas de SIREN)

## Actions recommandées
- Relancer `enrich_v2.py --batch 10` une fois les SIREN identifiés
- Démarrer FastAPI : `cd /Users/paul/Desktop/brantham-partners/api && uvicorn main:app`
- Lancer matching repreneurs via `/api/deals/{slug}/matching-repreneurs`

## Related
- [[brantham/_MOC]]
- [[brantham/pipeline/QUEUE]]
