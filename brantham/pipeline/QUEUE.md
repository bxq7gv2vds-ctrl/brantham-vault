# QUEUE — Opportunites en attente de traitement

> Mise a jour : 2026-03-30 (auto-enrichment session)

## TOP 10 nouvelles opportunites traitees (2026-03-30)

| Slug | Nom | CA | Source | SIREN | Statut |
|------|-----|-----|--------|-------|--------|
| ajup-michel-liard | MICHEL LIARD | 1-3M€ | AJ UP | 318601507 | enrichi |
| ajup-dome-menuiserie-batiment-dmb | DOME MENUISERIE BATIMENT DMB | 1-3M€ | AJ UP | 342350832 | enrichi |
| ajup-les-affranchis | LES AFFRANCHIS | 1-3M€ | AJ UP | 942314261 | enrichi |
| ajire-pleine-mesure | PLEINE MESURE | 1-3M€ | Ajire | 492009816 | enrichi |
| ajire-psg-loc | PSG LOC | 1-3M€ | Ajire | 819791393 | enrichi |
| ajire-solid-r | SOLID'R | 1-3M€ | Ajire | 928713320 | enrichi |
| p2g-librairie-d-art-et-vente-en-gros-de-livres-soldes | LIBRAIRIE D'ART | 1-3M€ | P2G | N/D | enrichi partiel |
| ascagne-conception-et-fabrication-d-accessoires-et-bijoux-s- | BIJOUX FLORAL | 987K€ | Ascagne | N/D | enrichi partiel |
| ajilink-ihdf-conseil-et-recrutement-de-personnel-pour-l-h-te | Recrutement hotellerie | <1M€ | Ajilink IHDF | N/D | enrichi partiel |
| ajilink-ihdf-groupe-de-promotion-immobili-re | Groupe promotion immo | <1M€ | Ajilink IHDF | 339673410 | enrichi |

## Notes

- 6/10 avec SIREN identifie via Pappers
- Acheteurs identifies via API gouv.fr pour 9/10
- API FastAPI (port 8000) hors ligne — matching 4D non disponible
- Scraper relance en background (fichier avait 7h)
- Plusieurs deadlines depassees (Feb/Mars 2026) — verifier si encore actives

## A faire

- Relancer FastAPI pour matching 4D
- Re-lancer scraper et comparer nouvelles annonces
- Enrichir SIREN manquants manuellement (librairie, bijoux, recrutement)


## Session 2026-04-02

| Slug | Nom | Secteur | CA | Effectif | Region | Statut | Date |
|------|-----|---------|-----|----------|--------|--------|------|
| ajilink-grandest-debos-style | DEBOS'STYLE | Carrosserie | De 1 à 3 | <10 | Alsace | nouveau | 2026-04-02 |
| ajup-i-artisan | I ARTISAN | Artisanat | <1M | 10-50 | IDF | nouveau | 2026-04-02 |
| ajilink-ihdf-recherche-d-veloppement-et-analyse-de-produits- | R&D Pharma Cannabis | Pharma/R&D | <1M | <10 | IDF | nouveau | 2026-04-02 |
| ajilink-ihdf-fabrication-de-conserves-et-de-produits-locaux | Fabrication conserves | Agroalim | <1M | <10 | IDF | nouveau | 2026-04-02 |
| p2g-le-coin-gourmand-boulangerie-patisserie-974 | LE COIN GOURMAND | Boulangerie | <1M | <10 | La Reunion | nouveau | 2026-04-02 |
| ajilink-ihdf-fetish | FETISH | Retail | <1M | <10 | IDF | nouveau | 2026-04-02 |
| ajilink-ihdf-production-de-confitures-traditionnelle-cr-mes- | Confitures traditionnelles | Agroalim | <1M | <10 | IDF | nouveau | 2026-04-02 |
| ajilink-ihdf-production-de-produits-d-picerie-fine | Epicerie fine | Agroalim | <1M | <10 | IDF | nouveau | 2026-04-02 |
| ajilink-ihdf-dda-mpc | DDA-MPC | NC | <1M | <10 | IDF | nouveau | 2026-04-02 |
| ajilink-provence-cap-alliance | CAP ALLIANCE | Services | <1M | <10 | PACA | nouveau | 2026-04-02 |


## Session 2026-04-03 — Auto-enrichment

| Slug | Nom | CA | Enrichment | Analyse |
|------|-----|-----|------------|---------|
| ascagne-boulangerie-situee-a-paris-13e | BOULANGERIE SITUEE A PARIS 13e | 400 604 € | oui | oui |
| meynet-vaise-sports-monts-d-or | VAISE SPORTS MONTS D'OR | 315 720€ | oui | oui |
| ascagne-ventes-d-articles-de-pu-riculture | Ventes d’articles de puériculture | 238.572 € | oui | oui |
| ascagne-coiffeur-barbier | Coiffeur barbier | 175.603 € | oui | oui |
| ascagne-boutique-atelier-de-bijoux-et-accessoires- | BOUTIQUE-ATELIER DE BIJOUX ET ACCESSOIRE | 61.200 € | oui | oui |
| aja-tous-les-secteursautres-secteursactivit-s-cult | Tous les secteursAutres secteursActivité |  | oui | oui |
| aj2m-d-veloppement-et-commercialisation-de-solutio | Développement et commercialisation de so |  | oui | oui |
| aj2m-activite-distribution-alimentaire-dediee-a-la | ACTIVITE : DISTRIBUTION ALIMENTAIRE DEDI |  | oui | oui |
| aj2m-activite-fabrication-de-peintures-et-produits | ACTIVITE : FABRICATION DE PEINTURES ET P |  | oui | oui |
| aj2m-activite-travaux-de-ma-onnerie-generale-et-gr | ACTIVITE : TRAVAUX DE MAÇONNERIE GENERAL |  | oui | oui |
