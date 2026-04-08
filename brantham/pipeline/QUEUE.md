# QUEUE — Opportunites en attente de traitement

> Mise a jour : 2026-04-06 (auto-enrichment session)

## TOP 10 nouvelles opportunites traitees (2026-04-04)

| Slug | Nom | CA | Source | SIREN | Statut |
|------|-----|-----|--------|-------|--------|
| ajire-ecole-de-conduite-prezeau | ECOLE DE CONDUITE PREZEAU | 85M est. | Ajire | 339957037 | enrichi |
| trajectoire-cyfac-meral | CYFAC & MERAL Cycles | N/A | Trajectoire | N/D | enrichi partiel |
| ajilink-sudouest-sas-mgmv | SAS MGMV (FRENCH DISORDER) | N/A | Ajilink SO | 989826672 | enrichi |
| ajilink-sudouest-h-a-location | H&A LOCATION (barriques) | N/A | Ajilink SO | N/D | enrichi partiel |
| ajup-sas-abeil | SAS ABEIL (literie) | N/A | AJ UP | 533134698 | enrichi |
| aj-specialises-2133 | Entreprise sante DOM/TOM | 5.76M | AJ Specialises | N/D | anon |
| aj-specialises-2092 | Infrastructures portuaires | 5.3M | AJ Specialises | N/D | anon |
| aj-specialises-2230 | Charcuterie industrielle Var | 3.6M | AJ Specialises | N/D | anon |
| aj-specialises-2144 | Reseau pharmaceutique | 2.36M | AJ Specialises | N/D | anon |
| aj-specialises-2091 | Mobilier Agencement CHR | ~3M | AJ Specialises | N/D | anon |

---


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

---

## Session auto-enrichment — 2026-04-05

10 nouvelles opportunites ajoutees (sans dossier existant, meilleur signal disponible) :

| # | Nom | Source | Secteur | CA | Slug |
|---|-----|--------|---------|-----|------|
| 1 | IPSOMEDIC | AJ Specialises | Pharmacie / R&D | n/d | aj-specialises-ipsomedic |
| 2 | BS OUTDOOR | AJ Specialises | Fabrication equipement | 2,1 M€ | aj-specialises-bs-outdoor |
| 3 | PROFAST | AJ Specialises | Transport messagerie | 1,1 M€ | aj-specialises-profast |
| 4 | Negoce semi-remorque | Meynet | Transport | n/d | meynet-cession-d-une-activit-de-n-goce-de-semi-remorque |
| 5 | EPIFURIEU | AJ Specialises | Boulangerie | 733 K€ | aj-specialises-epifurieu |
| 6 | Chantier naval Bormes | AJ Specialises | Construction navale | 1,3 M€ | aj-specialises-1937-chantier-naval-a-bormes-les-mimosas |
| 7 | 7 TECH | AJ Specialises | Machines speciales | n/d | aj-specialises-7-tech |
| 8 | Minuteurs EDDO | AJ Specialises | IoT / electronique | n/d | aj-specialises-concepteur-et-fabricant-de-minuteurs-de-douch |
| 9 | Connectique | AJ Specialises | Composants electroniques | n/d | aj-specialises-vente-d-entreprise-de-connectique |
| 10 | BLUE & PASTEL | FHBX | Biotechnologie pigments | n/d | fhbx-blue-pastel-le-reve-bleu |

Dossiers crees : deals/{slug}/enrichment.json + analyse.md + acheteurs.json (API gouv hors ligne - 0 repreneurs trouves)

---

## Auto-enrichment 2026-04-08 — Nouvelles opportunites

| Entreprise | AJ | CA (~M€) | Secteur | Slug |
|---|---|---|---|---|
| OOGARDEN | Meynet | 54 | Commerce de detail | meynet-oogarden |
| DAUPHITRANS | Meynet | 9.2 | Transport | meynet-dauphitrans |
| IMEX 360 | Meynet | 5.6 | Commerce de gros | meynet-imex-360 |
| D.UNIFLEXO | Meynet | 5.6 | Industrie | meynet-d-uniflexo |
| RENNARD | Meynet | 4.2 | Industrie | meynet-rennard |
| REGIS VAUTE | Meynet | 3.9 | Agriculture | meynet-regis-vaute |
| EVOLUTION | Meynet | 3.3 | BTP | meynet-evolution |
| GOUDET FERRIER | Meynet | 2.9 | Commerce de gros | meynet-goudet-ferrier |
| Papier & Electricite | Abitol | 151 | Industrie papetiere | abitol-rousselet-papier-et-electricite |

