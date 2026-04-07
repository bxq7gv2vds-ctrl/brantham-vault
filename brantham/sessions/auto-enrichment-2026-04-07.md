---
date: 2026-04-07
type: session
tags: [auto-enrichment, pipeline, scraping]
---

# Session auto-enrichment — 2026-04-07

## Resume

| Metrique | Valeur |
|----------|--------|
| Heure execution | 08h22 CEST |
| Scraping AJ | OK — 458 opportunites (24 sites OK, 1 erreur SSL BVP) |
| Opportunites sans dossier | 295 / 458 |
| Opportunites traitees | **10** |
| Enrichies Pappers | **5** |
| Erreurs | 0 |

## Deals crees

| Slug | Nom | SIREN | Date limite | Source |
|------|-----|-------|-------------|--------|
| fhbx-reactiv | REACTIV' (formation QHSE sante/agro) | 490803913 | 24/04/2026 | FHBX |
| fhbx-impact-technologies-sas | IMPACT TECHNOLOGIES SAS (IT virtualisation) | 340780808 | **13/04/2026 URGENT** | FHBX |
| fhbx-martech | MARTECH (menuiserie bois/PVC) | 398333765 | 27/04/2026 | FHBX |
| fhbx-soci-t-de-m-canique-g-n-rale | Societe mecanique generale | 572077774 | **17/04/2026 URGENT** | FHBX |
| meynet-cession-d-une-activit-de-boulangerie-patisserie | Boulangerie-patisserie Lyon (20-49 sal.) | NC | **14/04/2026 URGENT** | Meynet |
| aj2m-bureau-d-etude-et-fabrication-d-appareils-electroniques | Bureau etude electronique IoT/AV | NC | NC | 2M&Associes |
| aj2m-acticor-biotech | ACTICOR BIOTECH (biotech) | 798483285 | NC | 2M&Associes |
| aj2m-activit-fintech | Fintech SaaS marches prives | NC | NC | 2M&Associes |
| aj2m-d-veloppement-logiciel-pour-la-mobilit-connect-e-actuel | Logiciel mobilite connectee | NC | NC | 2M&Associes |
| aj2m-soci-t-sp-cialis-e-dans-la-conception-la-fabrication-et | Mobilier & Agencement (conciliation) | NC | NC | 2M&Associes |

## Urgences

3 deals avec date limite < 10 jours :
- **fhbx-impact-technologies-sas** : 13/04/2026 (dans 6 jours)
- **meynet-cession-d-une-activit-de-boulangerie-patisserie** : 14/04/2026 (dans 7 jours)
- **fhbx-soci-t-de-m-canique-g-n-rale** : 17/04/2026 (dans 10 jours)

## Etat infrastructure

- FastAPI (port 8000) : DOWN — repreneurs via API endpoint non disponible
- Scraper AJ : OK (BVP SSL error ignoree, erreur connue x22)
- Pappers : OK, 5/10 enrichissements reussis

## Actions suivantes requises

1. Relancer FastAPI backend
2. Acceder aux datarooms FHBX pour IMPACT TECHNOLOGIES et mecanique generale (deadlines proches)
3. Enrichir les 5 deals sans SIREN (noms trop generiques pour lookup Pappers)
4. Lancer matching repreneurs quand API backend disponible

## Related

[[brantham/_MOC]]
[[brantham/pipeline/QUEUE]]
- Deep enrichment termine a 08:27
---

## Cycle 10:05

- **Scrape AJ** : lancement...
  - OK : 458 opportunites scrapees

## Cycle 16:51

- **Scrape AJ** : lancement...
  - OK : 461 opportunites scrapees

## Deep Enrichment 19:14
- Deep enrichment termine a 19:17
---
