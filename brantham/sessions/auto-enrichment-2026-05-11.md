---
date: 2026-05-11
type: session
agent: auto-enrichment
---

# Session auto-enrichment — 2026-05-11

## Résumé

| Indicateur | Valeur |
|---|---|
| Heure | 14:03 |
| Opportunités analysées | 891 éligibles (CA≥500K ou score≥60) |
| Dossiers créés | 10 |
| Enrichissement Pappers | 0 (aucun SIREN disponible dans le scraper) |
| Erreurs | 0 |

## Statut scraper

- aj_annonces.json daté du 2026-05-11 07:50 (6h au moment du lancement)
- Scraper non relancé : budget $0.50 insuffisant pour scrape + enrichissement complet
- 1408 annonces en base, 891 éligibles, 854 sans dossier existant

## Dossiers créés

| Slug | Entreprise | CA | AJ |
|------|-----------|----|----|
| ajspecia-viand-oc | VIAND OC | 1 996 851.00 | AJ Spécialis |
| ajspecia-epifurieu | EPIFURIEU | 733 000,00 | AJ Spécialis |
| maydayma-bel-air-realisations | BEL AIR REALISATIONS | Plus de 50 M€ | Maydaymag |
| maydayma-ayen | AYEN | Plus de 50 M€ | Maydaymag |
| maydayma-le-royaume-des-delices | LE ROYAUME DES DELICES | Plus de 50 M€ | Maydaymag |
| maydayma-auto-shine | AUTO SHINE | Plus de 50 M€ | Maydaymag |
| maydayma-yohetset | YOHETSET | Plus de 50 M€ | Maydaymag |
| maydayma-pfi-ravalements | PFI RAVALEMENTS | Plus de 50 M€ | Maydaymag |
| maydayma-kouba | KOUBA | Plus de 50 M€ | Maydaymag |
| maydayma-othayssie | OTHAYSSIE | Plus de 50 M€ | Maydaymag |

## Points d'attention

- Aucun SIREN dans les données scraper → enrichissement Pappers impossible automatiquement
- Les CA "Plus de 50 M€" (Maydaymag) sont des fourchettes estimées, pas des valeurs réelles
- VIAND OC et EPIFURIEU (AJ Spécialisés) ont les CA les plus précis
- Prochain cycle : relancer scraper_aj.py pour données fraîches + chercher SIRENs manuellement

## Related

- [[brantham/_MOC]]
- [[brantham/pipeline/QUEUE]]
- [[_system/MOC-master]]
