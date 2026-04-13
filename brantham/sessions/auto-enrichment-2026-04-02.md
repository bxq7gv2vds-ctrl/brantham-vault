---
date: 2026-04-02
type: session
projet: brantham
---

# Session Auto-Enrichment — 2026-04-02

## Resume

| Metrique | Valeur |
|----------|--------|
| Opportunites scrapees (total JSON) | 454 |
| Nouvelles (sans dossier) | 343 |
| Selectionnees (CA >= 1M ou score > 60) | 10 |
| Dossiers crees | 10 |
| Enrichissements (enrichment.json + analyse.md) | 10 |
| Repreneurs identifies | 0 deals avec resultats |
| Erreurs | 0 |

## Scraper AJ
Rescape lance (background) — fichier date du 2026-04-01 08:15 (>24h)

## Top 10 opportunites traitees

| Slug | Nom | Secteur | CA |
|------|-----|---------|-----|
| ajilink-grandest-debos-style | DEBOS'STYLE | Carrosserie | De 1 a 3M |
| ajup-i-artisan | I ARTISAN | Artisanat | <1M |
| ajilink-ihdf-recherche-d-veloppement-et-analyse-de-produits- | R&D Pharma Cannabis | Pharma/R&D | <1M |
| ajilink-ihdf-fabrication-de-conserves-et-de-produits-locaux | Fabrication conserves | Agroalim | <1M |
| p2g-le-coin-gourmand-boulangerie-patisserie-974 | LE COIN GOURMAND | Boulangerie | <1M |
| ajilink-ihdf-fetish | FETISH | Retail | <1M |
| ajilink-ihdf-production-de-confitures-traditionnelle-cr-mes- | Confitures | Agroalim | <1M |
| ajilink-ihdf-production-de-produits-d-picerie-fine | Epicerie fine | Agroalim | <1M |
| ajilink-ihdf-dda-mpc | DDA-MPC | NC | <1M |
| ajilink-provence-cap-alliance | CAP ALLIANCE | Services | <1M |

## Observations
- Seule DEBOS'STYLE a un CA confirme >= 1M (range "De 1 a 3")
- 343 opportunites nouvelles sans CA documente — enrichissement SIREN necessaire
- API FastAPI hors ligne (port 8000) — matching repreneurs via api.gouv.fr en fallback
- Repreneurs identifies via recherche-entreprises.api.gouv.fr pour 0/10 deals

## Fichiers crees
- deals/*/enrichment.json (10 fichiers)
- deals/*/analyse.md (10 fichiers)
- deals/*/acheteurs.json (10 fichiers)
- vault/brantham/pipeline/QUEUE.md (mis a jour)

## Related
- [[brantham/_MOC]]
- [[brantham/pipeline/QUEUE]]
