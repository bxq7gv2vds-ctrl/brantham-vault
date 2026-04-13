---
date: 2026-04-13
type: session
project: brantham
tags: [auto-enrichment, scraping, pipeline]
---

# Session Auto-Enrichment — 2026-04-13

## Résumé exécutif

| Métrique | Valeur |
|----------|--------|
| Scraper lancé | Oui (données > 3h) |
| Sites scrapés | 31 |
| Total opportunités scrapées | 463 |
| Opportunités qualifiées (CA>500K ou score>60) | 19 |
| Déjà avec dossier | 19 |
| Nouvelles opportunités identifiées | 10 |
| Dossiers créés | 10 |
| Enrichissement Pappers | 0 (SIREN non disponibles) |
| Erreurs | 0 |

## Opportunités traitées

| Nom | AJ | Type | Dossier |
|-----|----|----|---------|
| ACTIVITE : TRANSPORT SPECIALISE DANS L’A | 2M&Associés | cession | `aj2m-activite-transport-specialise-dans-` |
| Société de fabrication et distribution d | 2M&Associés | cession | `aj2m-soci-t-de-fabrication-et-distributi` |
| Fonds de Commerce | Trajectoire | cession | `trajectoire-fonds-de-commerce` |
| Solutions industrielles pour le réemploi | BCM | cession | `bcm-solutions-industrielles-pour-le-r-em` |
| SELECTION VIANDE DISTRIBUTION | 2M&Associés | redressement | `aj2m-selection-viande-distribution` |
| BEC FIN - Fabrication de conserves et de | Ajilink IHDF | cession | `ajilink-ihdf-bec-fin-fabrication-de-cons` |
| RS PARTICIPATION | AJ UP | cession | `ajup-rs-participation` |
| PHARMACIE COLBERT | Ajilink Provence | cession | `ajilink-provence-pharmacie-colbert` |
| Activité : FABRICATION ET VENTE DE REMOR | 2M&Associés | cession | `aj2m-activit-fabrication-et-vente-de-rem` |
| Commercialisation et distribution d’équi | 2M&Associés | cession | `aj2m-commercialisation-et-distribution-d` |

## Observations

- Toutes les opportunités qualifiées (CA>500K) avaient déjà un dossier existant
- Les 10 nouvelles sélectionnées = meilleurs dossiers sans SIREN parmi les 282 restantes
- Secteurs couverts : transport agroalimentaire, accessoires mode, industrie réemploi, abattoir, pharmacie, remorques agricoles, EPI
- Enrichissement Pappers non effectué : SIRENs non disponibles dans le scrape

## Actions suivantes

- [ ] Identifier les SIRENs via recherche-entreprises.api.gouv.fr
- [ ] Enrichir via pappers.py (max 50 req/jour)
- [ ] Lancer matching repreneurs pour les dossiers qualifiés

## Related

- [[brantham/_MOC]]
- [[brantham/pipeline/QUEUE]]

## Cycle 17:16

- **Scrape AJ** : lancement...
  - OK : 463 opportunites scrapees
