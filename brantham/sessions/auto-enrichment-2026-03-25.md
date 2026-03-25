---
type: session
project: brantham
date: 2026-03-25
tags: [scraping, aj, auto-enrichment, pipeline]
---

# Auto-Enrichment AJ -- 2026-03-25

## Scan Summary

| Metric | Value |
|--------|-------|
| Sites scraped | 24/31 (7 vides, 0 erreurs) |
| Opportunites totales | 456 |
| Expirees supprimees | 348 |
| Avec CA identifie | 127/456 |
| CA >= 1M EUR | 75 |
| Avec effectif identifie | 143/456 |
| Procedures cession | 338 |
| Procedures RJ | 112 |
| Procedures LJ | 4 |
| Statut | Toutes "nouveau" (premier scan) |

Fichier JSON: `/tmp/aj_scan_20260325_1704.json`
Cache API: `/Users/paul/Desktop/brantham-partners/api/aj_annonces.json`

## Top 5 Opportunites

### #1 -- Papier et electricite (Score 100/100)

- **Source AJ**: Abitbol & Rousselet
- **CA**: 204,4 M EUR
- **Effectif**: 268 salaries
- **Secteur**: Groupe specialise dans la production papetiere, l'exploitation et la valorisation forestiere, production d'electricite a partir de biomasse (usine pate a papier, turbines)
- **Procedure**: Cession
- **Dataroom**: https://www.abitbol-rousselet.fr/recherche-d-acquereur
- **Analyse**: Tres gros dossier industriel. CA exceptionnel (204M). Potentiel eleve mais complexite certaine (actifs industriels lourds, enjeux environnementaux). A investiguer en priorite.

### #2 -- Produits electroniques (Score 72/100)

- **Source AJ**: Abitbol & Rousselet
- **CA**: 30,7 M EUR
- **Effectif**: 20 salaries
- **Secteur**: Reconditionnement et revente de produits electroniques
- **Procedure**: Recherche d'investisseurs en capital / prepack cession (L.642-2)
- **Dataroom**: https://www.abitbol-rousselet.fr/recherche-d-acquereur
- **Analyse**: Profil tres interessant -- CA/employe eleve (1.5M/tete), secteur porteur (reconditionne/economie circulaire), prepack = processus plus rapide. A contacter rapidement.

### #3 -- GROUPE JOTT - JOTT OPERATIONS (Score 65/100)

- **Source AJ**: Ajilink Provence
- **CA**: Plus de 10 M EUR
- **Effectif**: Plus de 250
- **Secteur**: Commerce d'habillement specialise
- **Localisation**: 13 Bouches-du-Rhone
- **Procedure**: Cession
- **Date limite**: 05/02/2026 (EXPIREE?)
- **Dataroom**: https://provence.ajilink.fr/anonym/reprise/detail/10137672209
- **Analyse**: Marque connue (JOTT = Just Over The Top, doudounes). Gros dossier mais date limite potentiellement passee. Verifier si encore ouvert.

### #4 -- POLYTECHNYL (Score 65/100)

- **Source AJ**: AJ UP
- **CA**: Plus de 10 M EUR
- **Effectif**: Plus de 250
- **Secteur**: Fabrication d'intermediaires chimiques (sel de nylon, polyamide 6.6) et transformation
- **Localisation**: 69 Rhone
- **Procedure**: Cession
- **Date limite**: 23/02/2026 (EXPIREE?)
- **Dataroom**: https://dataroom.ajup.fr/anonym/reprise/detail/10189076469
- **Analyse**: Industrie chimique specialisee, probablement filiale d'un groupe. Date potentiellement passee. A verifier.

### #5 -- Commerce d'articles de sport (Score 47/100)

- **Source AJ**: Ajilink IHDF
- **CA**: Plus de 10 M EUR
- **Effectif**: De 50 a 250
- **Secteur**: Commerce de detail d'articles de sport, nature, loisirs, chasse, peche, equitation
- **Localisation**: 17 Charente-Maritime
- **Procedure**: Cession
- **Date limite**: 07/04/2026 (OUVERTE)
- **Dataroom**: https://ihdf.ajilink.fr/anonym/reprise/detail/10133566369
- **Analyse**: Opportunite encore ouverte (deadline 7 avril). Multi-activite loisirs/sport. Bonne taille (50-250 employes, CA>10M). A prioriser car deadline proche.

## Mentions honorables (#6-10)

| # | Entreprise | CA | Effectif | Procedure | Score |
|---|-----------|-----|----------|-----------|-------|
| 6 | RELAIS COLIS | >10M | 50-250 | Cession | 47 |
| 7 | PSE AR.VAL | >10M | 50-250 | Cession | 47 |
| 8 | SOGRAN | >10M | 50-250 | Cession | 47 |
| 9 | FONDERIE DE NIEDERBRONN | >10M | 50-250 | Cession | 47 |
| 10 | SILICONES ALIMENTAIRES | >10M | 50-250 | Cession | 47 |

## Recommandations

1. **Priorite #1**: Commerce d'articles de sport (#5) -- deadline 7 avril, encore actionnable
2. **Priorite #2**: Produits electroniques (#2) -- prepack, secteur porteur, contacter l'AJ
3. **Investigation**: Papier et electricite (#1) -- verifier si le dossier est a notre portee (204M = gros)
4. **Verification deadlines**: JOTT (#3) et POLYTECHNYL (#4) ont des dates passees -- verifier statut
5. **Batch #6-10**: 5 dossiers CA>10M a screener rapidement

## Next Steps

- [ ] Ouvrir les datarooms des top 5 et evaluer la documentation disponible
- [ ] Qualifier via LLM (`scraper_aj.py --llm`) pour un scoring plus fin
- [ ] Contacter les AJ pour les dossiers prioritaires
- [ ] Integrer dans le pipeline Director pour analyse automatisee

---

## Batch Enrichissement DB -- Procedures sans bilans (score > 50)

**Date**: 2026-03-25
**Source API**: recherche-entreprises.api.gouv.fr (fallback, Pappers rate-limited)
**Procedures enrichies**: 20/20
**Erreurs**: 0

### Observations cles

- **Concentration geographique**: 33 (8), 69 (5), 75 (4), 67 (1), 974 (1), 63 (1)
- **Sections NAF**: I (18), H (2)
- **Chaines identifiees**: CAFEINCUP (5 entites), SANTOSHA (3 entites) -- probable groupe unique par chaine, risque de doublon dans le scoring
- **Toutes PME** (categorie_entreprise)
- **Pappers API token a atteint sa limite journaliere** -- donnees financieres (CA, resultat, bilans) non disponibles via cette source. A retenter demain ou utiliser l'API officielle payante.

### Tableau synthetique

| # | SIREN | Denomination | Score | Dept | Dirigeant | Nature Jur. | Cree | Etabs |
|---|-------|-------------|-------|------|-----------|-------------|------|-------|
| 1 | 852385046 | PTIT BISTROY (PTIT BISTROY) | 87.41 | 69 VILLEURBANNE | GUY-PIERRE TURCO (Gérant) | 5499 | 2019-06-28 | 1/1 |
| 2 | 902617554 | FABAMERICA (WAB S BURGER) | 87.31 | 69 FONTAINES-SUR-SAONE | PM: FABIOLI DEVELOPPEMENT (Président de SAS) | 5710 | 2021-08-25 | 1/1 |
| 3 | 892222993 | FURAHAA RESTAURATION | 87.0 | 75 PARIS | PM: FURAHAA GROUP (Président de SAS) | 5710 | 2021-01-01 | 1/2 |
| 4 | 852328293 | CAFEINCUP COMBES | 86.9 | 33 BORDEAUX | JIMMY LOUIS THIRANT (Gérant) | 5499 | 2019-07-10 | 1/2 |
| 5 | 909850893 | B.J. TRANSPORTS ET POMPAGES | 86.6 | 67 MUTTERSHOLTZ | BENJAMIN GAUCHE (Directeur Général) | 5710 | 2022-01-17 | 1/1 |
| 6 | 885275008 | LA RESIDENCE LEONIE | 86.24 | 974 SAINT-DENIS | JEAN PATRICK GARAIOS (Gérant) | 5499 | 2020-07-01 | 1/1 |
| 7 | 909825887 | CAFEINCUP ARCACHON | 86.2 | 33 BORDEAUX | JIMMY THIRANT (Président de SAS) | 5710 | 2022-02-01 | 2/2 |
| 8 | 823783899 | MARECHAL | 86.18 | 69 LYON | BRIEUC PIERRE OGER RUBY (OGER) (Président de SAS) | 5710 | 2016-11-15 | 1/2 |
| 9 | 919299719 | PELICAN | 85.95 | 75 PARIS | PM: LA FONCIERE DE SHERY (Gérant et associé indéfiniment et solidairement responsable) | 5202 | 2022-09-13 | 2/2 |
| 10 | 880031893 | WASSIMA SOCIETY (WASSIMA SOCIETY) | 85.81 | 69 LYON | JALIL LITON AHMED (Président de SAS) | 5710 | 2019-12-19 | 1/2 |
| 11 | 881467385 | CAFEINCUP LE BOUSCAT | 85.7 | 33 BORDEAUX | JIMMY LOUIS THIRANT (Gérant) | 5499 | 2020-01-21 | 2/2 |
| 12 | 918078528 | CAFEINCUP PESSAC | 85.7 | 33 PESSAC | JIMMY LOUIS THIRANT (Gérant) | 5499 | 2022-08-03 | 1/1 |
| 13 | 818313447 | CAFEINCUP (CAFEINCUP) | 85.7 | 33 BORDEAUX | JIMMY LOUIS THIRANT (Gérant) | 5499 | 2016-02-09 | 1/2 |
| 14 | 845239888 | PRANA (PRANA RESTAURANT) | 85.6 | 69 LYON | PIERRE VAROUJAN BARONIAN (Président de SAS) | 5710 | 2019-01-04 | 1/1 |
| 15 | 851395012 | SUBMART (PARTAGE BRASSERIE) | 85.58 | 75 PARIS | MATHIEU PIERRE MICHEL SUBRAN (Président de SAS) | 5710 | 2019-05-31 | 1/1 |
| 16 | 753489012 | ABBOUFFE (CAVALINO) | 85.5 | 75 PARIS | VANESSA VIRGINIE JEANINE SIMON (Gérant) | 5499 | 2012-07-01 | 1/1 |
| 17 | 912262698 | LES DEMENAGEURS DE LA LIMAGNE (LES DEMENAGEURS DE LA LIMAGNE) | 85.44 | 63 CLERMONT-FERRAND | SEBASTIEN STEPHANE BERNARD BOTTIN (Gérant) | 5499 | 2022-02-22 | 3/4 |
| 18 | 841689300 | SANTOSHA TALENCE (SANTOSHA TALENCE) | 85.4 | 33 TALENCE | EMMANUEL MEURET (Gérant) | 5499 | 2018-08-13 | 1/1 |
| 19 | 842433989 | SANTOSHA PESSAC | 85.4 | 33 BORDEAUX | EMMANUEL MEURET (Gérant) | 5499 | 2018-09-14 | 2/2 |
| 20 | 850858259 | SANTOSHA SAINT MEDARD EN JALLES | 85.4 | 33 BORDEAUX | BENOIT GERMANEAU (Gérant) | 5499 | 2019-05-14 | 3/3 |

### Detail par entreprise

#### 1. PTIT BISTROY (PTIT BISTROY) (852385046)
- **Score**: 87.41
- **Procedure ID**: 103434
- **Categorie**: PME
- **Nature juridique**: 5499
- **Date creation**: 2019-06-28
- **Etat admin**: A
- **NAF**: 5630Z (section I)
- **Effectif DB**: 3-5 | Tranche INSEE: 02 (annee 2023)
- **Etablissements**: 1 ouverts / 1 total
- **Siege**: 44 AVENUE MARC SANGNIER 69100 VILLEURBANNE
- **GPS**: 45.760433, 4.875
- **Convention collective (IDCC)**: 1979
- **Dirigeants** (1):
  - GUY-PIERRE TURCO -- Gérant

#### 2. FABAMERICA (WAB S BURGER) (902617554)
- **Score**: 87.31
- **Procedure ID**: 104610
- **Categorie**: PME
- **Nature juridique**: 5710
- **Date creation**: 2021-08-25
- **Etat admin**: A
- **NAF**: 5610A (section I)
- **Effectif DB**: 3-5 | Tranche INSEE: 02 (annee 2023)
- **Etablissements**: 1 ouverts / 1 total
- **Siege**: 7 AVENUE DU CAMP 69270 FONTAINES-SUR-SAONE
- **GPS**: 45.816185, 4.864096
- **Convention collective (IDCC)**: 1979
- **Dirigeants** (1):
  - [PM] FABIOLI DEVELOPPEMENT -- Président de SAS

#### 3. FURAHAA RESTAURATION (892222993)
- **Score**: 87.0
- **Procedure ID**: 162319
- **Categorie**: PME
- **Nature juridique**: 5710
- **Date creation**: 2021-01-01
- **Etat admin**: A
- **NAF**: 5610C (section I)
- **Effectif DB**: 3-5 | Tranche INSEE: 02 (annee 2023)
- **Etablissements**: 1 ouverts / 2 total
- **Siege**: 78 RUE REAUMUR 75002 PARIS
- **GPS**: 48.866528, 2.351657
- **Convention collective (IDCC)**: 1501
- **Dirigeants** (1):
  - [PM] FURAHAA GROUP -- Président de SAS

#### 4. CAFEINCUP COMBES (852328293)
- **Score**: 86.9
- **Procedure ID**: 112730
- **Categorie**: PME
- **Nature juridique**: 5499
- **Date creation**: 2019-07-10
- **Etat admin**: A
- **NAF**: 5610C (section I)
- **Effectif DB**: 6-9 | Tranche INSEE: 03 (annee 2023)
- **Etablissements**: 1 ouverts / 2 total
- **Siege**: 15-17 15 RUE DES ARGENTIERS 33000 BORDEAUX
- **GPS**: 44.8393, -0.570077
- **Dirigeants** (1):
  - JIMMY LOUIS THIRANT -- Gérant

#### 5. B.J. TRANSPORTS ET POMPAGES (909850893)
- **Score**: 86.6
- **Procedure ID**: 115164
- **Categorie**: PME
- **Nature juridique**: 5710
- **Date creation**: 2022-01-17
- **Etat admin**: A
- **NAF**: 4941B (section H)
- **Effectif DB**: 6-9 | Tranche INSEE: 03 (annee 2023)
- **Etablissements**: 1 ouverts / 1 total
- **Siege**: Z.A LES SAULES 21 RUE DES TULIPES 67600 MUTTERSHOLTZ
- **GPS**: 48.259938, 7.532267
- **Dirigeants** (2):
  - BENJAMIN GAUCHE -- Directeur Général
  - JEREMY OECHSEL -- Président de SAS

#### 6. LA RESIDENCE LEONIE (885275008)
- **Score**: 86.24
- **Procedure ID**: 103919
- **Categorie**: PME
- **Nature juridique**: 5499
- **Date creation**: 2020-07-01
- **Etat admin**: A
- **NAF**: 5510Z (section I)
- **Effectif DB**: 6-9 | Tranche INSEE: 03 (annee 2023)
- **Etablissements**: 1 ouverts / 1 total
- **Siege**: 35 CHEMIN DE LA GLACIERE 97400 SAINT-DENIS
- **GPS**: -20.912042, 55.455626
- **Convention collective (IDCC)**: 1979
- **Dirigeants** (1):
  - JEAN PATRICK GARAIOS -- Gérant

#### 7. CAFEINCUP ARCACHON (909825887)
- **Score**: 86.2
- **Procedure ID**: 169617
- **Categorie**: PME
- **Nature juridique**: 5710
- **Date creation**: 2022-02-01
- **Etat admin**: A
- **NAF**: 5610C (section I)
- **Effectif DB**: 3-5 | Tranche INSEE: 02 (annee 2023)
- **Etablissements**: 2 ouverts / 2 total
- **Siege**: 15-17 15 RUE DES ARGENTIERS 33000 BORDEAUX
- **GPS**: 44.8393, -0.570077
- **Dirigeants** (1):
  - JIMMY THIRANT -- Président de SAS

#### 8. MARECHAL (823783899)
- **Score**: 86.18
- **Procedure ID**: 143306
- **Categorie**: PME
- **Nature juridique**: 5710
- **Date creation**: 2016-11-15
- **Etat admin**: A
- **NAF**: 5610C (section I)
- **Effectif DB**: 3-5 | Tranche INSEE: 02 (annee 2023)
- **Etablissements**: 1 ouverts / 2 total
- **Siege**: 9 RUE DU BAT D'ARGENT 69001 LYON
- **GPS**: 45.766165, 4.835315
- **Convention collective (IDCC)**: 1501
- **Dirigeants** (1):
  - BRIEUC PIERRE OGER RUBY (OGER) -- Président de SAS

#### 9. PELICAN (919299719)
- **Score**: 85.95
- **Procedure ID**: 174072
- **Categorie**: PME
- **Nature juridique**: 5202
- **Date creation**: 2022-09-13
- **Etat admin**: A
- **NAF**: 5510Z (section I)
- **Effectif DB**: 3-5 | Tranche INSEE: 02 (annee 2023)
- **Etablissements**: 2 ouverts / 2 total
- **Siege**: 5 RUE LINCOLN 75008 PARIS
- **GPS**: 48.870059, 2.302538
- **Convention collective (IDCC)**: 1979
- **Dirigeants** (3):
  - [PM] LA FONCIERE DE SHERY -- Gérant et associé indéfiniment et solidairement responsable
  - [PM] HOLDING FONCIERE DE L'IMMOBILIER -- Associé indéfiniment et solidairement responsable
  - [PM] HOLDING SHERYNE -- Associé indéfiniment et solidairement responsable

#### 10. WASSIMA SOCIETY (WASSIMA SOCIETY) (880031893)
- **Score**: 85.81
- **Procedure ID**: 157082
- **Categorie**: PME
- **Nature juridique**: 5710
- **Date creation**: 2019-12-19
- **Etat admin**: A
- **NAF**: 5610C (section I)
- **Effectif DB**: 3-5 | Tranche INSEE: 02 (annee 2023)
- **Etablissements**: 1 ouverts / 2 total
- **Siege**: 188 GRANDE RUE DE LA GUILLOTIERE 69007 LYON
- **GPS**: 45.748725, 4.853991
- **Convention collective (IDCC)**: 1501
- **Dirigeants** (1):
  - JALIL LITON AHMED -- Président de SAS

#### 11. CAFEINCUP LE BOUSCAT (881467385)
- **Score**: 85.7
- **Procedure ID**: 157791
- **Categorie**: PME
- **Nature juridique**: 5499
- **Date creation**: 2020-01-21
- **Etat admin**: A
- **NAF**: 5610C (section I)
- **Effectif DB**: 6-9 | Tranche INSEE: 03 (annee 2023)
- **Etablissements**: 2 ouverts / 2 total
- **Siege**: 15-17 15 RUE DES ARGENTIERS 33000 BORDEAUX
- **GPS**: 44.8393, -0.570077
- **Convention collective (IDCC)**: 1501
- **Dirigeants** (1):
  - JIMMY LOUIS THIRANT -- Gérant

#### 12. CAFEINCUP PESSAC (918078528)
- **Score**: 85.7
- **Procedure ID**: 173436
- **Categorie**: PME
- **Nature juridique**: 5499
- **Date creation**: 2022-08-03
- **Etat admin**: A
- **NAF**: 5610C (section I)
- **Effectif DB**: 6-9 | Tranche INSEE: 03 (annee 2023)
- **Etablissements**: 1 ouverts / 1 total
- **Siege**: PROGRAMME COEUR BRESOL - KIOSQUE C 28 AVENUE GUSTAVE EIFFEL 33600 PESSAC
- **GPS**: 44.780963, -0.651343
- **Dirigeants** (1):
  - JIMMY LOUIS THIRANT -- Gérant

#### 13. CAFEINCUP (CAFEINCUP) (818313447)
- **Score**: 85.7
- **Procedure ID**: 140976
- **Categorie**: PME
- **Nature juridique**: 5499
- **Date creation**: 2016-02-09
- **Etat admin**: A
- **NAF**: 5610C (section I)
- **Effectif DB**: 6-9 | Tranche INSEE: 03 (annee 2023)
- **Etablissements**: 1 ouverts / 2 total
- **Siege**: 15-17 15 RUE DES ARGENTIERS 33000 BORDEAUX
- **GPS**: 44.8393, -0.570077
- **Convention collective (IDCC)**: 1501
- **Dirigeants** (1):
  - JIMMY LOUIS THIRANT -- Gérant

#### 14. PRANA (PRANA RESTAURANT) (845239888)
- **Score**: 85.6
- **Procedure ID**: 74774
- **Categorie**: PME
- **Nature juridique**: 5710
- **Date creation**: 2019-01-04
- **Etat admin**: A
- **NAF**: 5610A (section I)
- **Effectif DB**: 3-5 | Tranche INSEE: 02 (annee 2023)
- **Etablissements**: 1 ouverts / 1 total
- **Siege**: 5 RUE DUHAMEL 69002 LYON
- **GPS**: 45.750394, 4.829325
- **Convention collective (IDCC)**: 1979
- **Dirigeants** (1):
  - PIERRE VAROUJAN BARONIAN -- Président de SAS

#### 15. SUBMART (PARTAGE BRASSERIE) (851395012)
- **Score**: 85.58
- **Procedure ID**: 10198
- **Categorie**: PME
- **Nature juridique**: 5710
- **Date creation**: 2019-05-31
- **Etat admin**: A
- **NAF**: 5610A (section I)
- **Effectif DB**: 3-5 | Tranche INSEE: 02 (annee 2023)
- **Etablissements**: 1 ouverts / 1 total
- **Siege**: 79 RUE DIDOT 75014 PARIS
- **GPS**: 48.829487, 2.317832
- **Dirigeants** (1):
  - MATHIEU PIERRE MICHEL SUBRAN -- Président de SAS

#### 16. ABBOUFFE (CAVALINO) (753489012)
- **Score**: 85.5
- **Procedure ID**: 109435
- **Categorie**: PME
- **Nature juridique**: 5499
- **Date creation**: 2012-07-01
- **Etat admin**: A
- **NAF**: 5610A (section I)
- **Effectif DB**: 3-5 | Tranche INSEE: 02 (annee 2023)
- **Etablissements**: 1 ouverts / 1 total
- **Siege**: 96 AVENUE DAUMESNIL 75012 PARIS
- **GPS**: 48.843304, 2.383244
- **Convention collective (IDCC)**: 1979
- **Dirigeants** (1):
  - VANESSA VIRGINIE JEANINE SIMON -- Gérant

#### 17. LES DEMENAGEURS DE LA LIMAGNE (LES DEMENAGEURS DE LA LIMAGNE) (912262698)
- **Score**: 85.44
- **Procedure ID**: 115395
- **Categorie**: PME
- **Nature juridique**: 5499
- **Date creation**: 2022-02-22
- **Etat admin**: A
- **NAF**: 4941B (section H)
- **Effectif DB**: 6-9 | Tranche INSEE: 03 (annee 2023)
- **Etablissements**: 3 ouverts / 4 total
- **Siege**: 4 RUE LOUIS ROSIER 63000 CLERMONT-FERRAND
- **GPS**: 45.764441, 3.132566
- **Convention collective (IDCC)**: 0016
- **Dirigeants** (2):
  - SEBASTIEN STEPHANE BERNARD BOTTIN -- Gérant
  - SYLVAIN RENE ALBERT KREMER -- Gérant

#### 18. SANTOSHA TALENCE (SANTOSHA TALENCE) (841689300)
- **Score**: 85.4
- **Procedure ID**: 150143
- **Categorie**: PME
- **Nature juridique**: 5499
- **Date creation**: 2018-08-13
- **Etat admin**: A
- **NAF**: 5610A (section I)
- **Effectif DB**: 3-5 | Tranche INSEE: 02 (annee 2023)
- **Etablissements**: 1 ouverts / 1 total
- **Siege**: 337-349-RESIDENCE LES NOBEL 337 COURS DE LA LIBERATION 33400 TALENCE
- **GPS**: 44.809948, -0.591471
- **Convention collective (IDCC)**: 1979
- **Dirigeants** (2):
  - EMMANUEL MEURET -- Gérant
  - THOMAS QUEAU -- Gérant

#### 19. SANTOSHA PESSAC (842433989)
- **Score**: 85.4
- **Procedure ID**: 150510
- **Categorie**: PME
- **Nature juridique**: 5499
- **Date creation**: 2018-09-14
- **Etat admin**: A
- **NAF**: 5610A (section I)
- **Effectif DB**: 3-5 | Tranche INSEE: 02 (annee 2023)
- **Etablissements**: 2 ouverts / 2 total
- **Siege**: 2 PLACE FERNAND LAFARGUE 33000 BORDEAUX
- **GPS**: 44.837044, -0.571563
- **Convention collective (IDCC)**: 1979
- **Dirigeants** (2):
  - EMMANUEL MEURET -- Gérant
  - FRANCOIS REYNOSO -- Gérant

#### 20. SANTOSHA SAINT MEDARD EN JALLES (850858259)
- **Score**: 85.4
- **Procedure ID**: 153909
- **Categorie**: PME
- **Nature juridique**: 5499
- **Date creation**: 2019-05-14
- **Etat admin**: A
- **NAF**: 5610A (section I)
- **Effectif DB**: 3-5 | Tranche INSEE: 02 (annee 2023)
- **Etablissements**: 3 ouverts / 3 total
- **Siege**: 2 PLACE FERNAND LAFARGUE 33000 BORDEAUX
- **GPS**: 44.837044, -0.571563
- **Convention collective (IDCC)**: 1979
- **Dirigeants** (2):
  - BENOIT GERMANEAU -- Gérant
  - SAMER HOBLOSS -- Gérant

### Donnees JSON brutes

```json
[
  {
    "procedure_id": 103434,
    "siren": "852385046",
    "raison_sociale_db": "PTIT BISTROY",
    "score_global": 87.41,
    "code_naf_db": "5630Z",
    "effectif_db": "3-5",
    "denomination": "PTIT BISTROY (PTIT BISTROY)",
    "categorie_entreprise": "PME",
    "nature_juridique": "5499",
    "date_creation": "2019-06-28",
    "date_fermeture": null,
    "etat_administratif": "A",
    "section_activite": "I",
    "tranche_effectif": "02",
    "annee_effectif": "2023",
    "nb_etablissements": 1,
    "nb_etablissements_ouverts": 1,
    "siege": {
      "adresse": "44 AVENUE MARC SANGNIER 69100 VILLEURBANNE",
      "code_postal": "69100",
      "commune": "VILLEURBANNE",
      "departement": "69",
      "latitude": "45.760433",
      "longitude": "4.875"
    },
    "dirigeants": [
      {
        "nom": "TURCO",
        "prenoms": "GUY-PIERRE",
        "qualite": "Gérant",
        "type": "personne physique",
        "denomination": null
      }
    ],
    "convention_collective": [
      "1979"
    ]
  },
  {
    "procedure_id": 104610,
    "siren": "902617554",
    "raison_sociale_db": "FABAMERICA",
    "score_global": 87.31,
    "code_naf_db": "5610A",
    "effectif_db": "3-5",
    "denomination": "FABAMERICA (WAB S BURGER)",
    "categorie_entreprise": "PME",
    "nature_juridique": "5710",
    "date_creation": "2021-08-25",
    "date_fermeture": null,
    "etat_administratif": "A",
    "section_activite": "I",
    "tranche_effectif": "02",
    "annee_effectif": "2023",
    "nb_etablissements": 1,
    "nb_etablissements_ouverts": 1,
    "siege": {
      "adresse": "7 AVENUE DU CAMP 69270 FONTAINES-SUR-SAONE",
      "code_postal": "69270",
      "commune": "FONTAINES-SUR-SAONE",
      "departement": "69",
      "latitude": "45.816185",
      "longitude": "4.864096"
    },
    "dirigeants": [
      {
        "nom": null,
        "prenoms": null,
        "qualite": "Président de SAS",
        "type": "personne morale",
        "denomination": "FABIOLI DEVELOPPEMENT"
      }
    ],
    "convention_collective": [
      "1979"
    ]
  },
  {
    "procedure_id": 162319,
    "siren": "892222993",
    "raison_sociale_db": "FURAHAA RESTAURATION",
    "score_global": 87.0,
    "code_naf_db": "5610C",
    "effectif_db": "3-5",
    "denomination": "FURAHAA RESTAURATION",
    "categorie_entreprise": "PME",
    "nature_juridique": "5710",
    "date_creation": "2021-01-01",
    "date_fermeture": null,
    "etat_administratif": "A",
    "section_activite": "I",
    "tranche_effectif": "02",
    "annee_effectif": "2023",
    "nb_etablissements": 2,
    "nb_etablissements_ouverts": 1,
    "siege": {
      "adresse": "78 RUE REAUMUR 75002 PARIS",
      "code_postal": "75002",
      "commune": "PARIS",
      "departement": "75",
      "latitude": "48.866528",
      "longitude": "2.351657"
    },
    "dirigeants": [
      {
        "nom": null,
        "prenoms": null,
        "qualite": "Président de SAS",
        "type": "personne morale",
        "denomination": "FURAHAA GROUP"
      }
    ],
    "convention_collective": [
      "1501"
    ]
  },
  {
    "procedure_id": 112730,
    "siren": "852328293",
    "raison_sociale_db": "CAFEINCUP COMBES",
    "score_global": 86.9,
    "code_naf_db": "5610C",
    "effectif_db": "6-9",
    "denomination": "CAFEINCUP COMBES",
    "categorie_entreprise": "PME",
    "nature_juridique": "5499",
    "date_creation": "2019-07-10",
    "date_fermeture": null,
    "etat_administratif": "A",
    "section_activite": "I",
    "tranche_effectif": "03",
    "annee_effectif": "2023",
    "nb_etablissements": 2,
    "nb_etablissements_ouverts": 1,
    "siege": {
      "adresse": "15-17 15 RUE DES ARGENTIERS 33000 BORDEAUX",
      "code_postal": "33000",
      "commune": "BORDEAUX",
      "departement": "33",
      "latitude": "44.8393",
      "longitude": "-0.570077"
    },
    "dirigeants": [
      {
        "nom": "THIRANT",
        "prenoms": "JIMMY LOUIS",
        "qualite": "Gérant",
        "type": "personne physique",
        "denomination": null
      }
    ],
    "convention_collective": null
  },
  {
    "procedure_id": 115164,
    "siren": "909850893",
    "raison_sociale_db": "B.J. TRANSPORTS ET POMPAGES",
    "score_global": 86.6,
    "code_naf_db": "4941B",
    "effectif_db": "6-9",
    "denomination": "B.J. TRANSPORTS ET POMPAGES",
    "categorie_entreprise": "PME",
    "nature_juridique": "5710",
    "date_creation": "2022-01-17",
    "date_fermeture": null,
    "etat_administratif": "A",
    "section_activite": "H",
    "tranche_effectif": "03",
    "annee_effectif": "2023",
    "nb_etablissements": 1,
    "nb_etablissements_ouverts": 1,
    "siege": {
      "adresse": "Z.A LES SAULES 21 RUE DES TULIPES 67600 MUTTERSHOLTZ",
      "code_postal": "67600",
      "commune": "MUTTERSHOLTZ",
      "departement": "67",
      "latitude": "48.259938",
      "longitude": "7.532267"
    },
    "dirigeants": [
      {
        "nom": "GAUCHE",
        "prenoms": "BENJAMIN",
        "qualite": "Directeur Général",
        "type": "personne physique",
        "denomination": null
      },
      {
        "nom": "OECHSEL",
        "prenoms": "JEREMY",
        "qualite": "Président de SAS",
        "type": "personne physique",
        "denomination": null
      }
    ],
    "convention_collective": null
  },
  {
    "procedure_id": 103919,
    "siren": "885275008",
    "raison_sociale_db": "LA RESIDENCE LEONIE",
    "score_global": 86.24,
    "code_naf_db": "5510Z",
    "effectif_db": "6-9",
    "denomination": "LA RESIDENCE LEONIE",
    "categorie_entreprise": "PME",
    "nature_juridique": "5499",
    "date_creation": "2020-07-01",
    "date_fermeture": null,
    "etat_administratif": "A",
    "section_activite": "I",
    "tranche_effectif": "03",
    "annee_effectif": "2023",
    "nb_etablissements": 1,
    "nb_etablissements_ouverts": 1,
    "siege": {
      "adresse": "35 CHEMIN DE LA GLACIERE 97400 SAINT-DENIS",
      "code_postal": "97400",
      "commune": "SAINT-DENIS",
      "departement": "974",
      "latitude": "-20.912042",
      "longitude": "55.455626"
    },
    "dirigeants": [
      {
        "nom": "GARAIOS",
        "prenoms": "JEAN PATRICK",
        "qualite": "Gérant",
        "type": "personne physique",
        "denomination": null
      }
    ],
    "convention_collective": [
      "1979"
    ]
  },
  {
    "procedure_id": 169617,
    "siren": "909825887",
    "raison_sociale_db": "CAFEINCUP ARCACHON",
    "score_global": 86.2,
    "code_naf_db": "5610C",
    "effectif_db": "3-5",
    "denomination": "CAFEINCUP ARCACHON",
    "categorie_entreprise": "PME",
    "nature_juridique": "5710",
    "date_creation": "2022-02-01",
    "date_fermeture": null,
    "etat_administratif": "A",
    "section_activite": "I",
    "tranche_effectif": "02",
    "annee_effectif": "2023",
    "nb_etablissements": 2,
    "nb_etablissements_ouverts": 2,
    "siege": {
      "adresse": "15-17 15 RUE DES ARGENTIERS 33000 BORDEAUX",
      "code_postal": "33000",
      "commune": "BORDEAUX",
      "departement": "33",
      "latitude": "44.8393",
      "longitude": "-0.570077"
    },
    "dirigeants": [
      {
        "nom": "THIRANT",
        "prenoms": "JIMMY",
        "qualite": "Président de SAS",
        "type": "personne physique",
        "denomination": null
      }
    ],
    "convention_collective": null
  },
  {
    "procedure_id": 143306,
    "siren": "823783899",
    "raison_sociale_db": "MARECHAL",
    "score_global": 86.18,
    "code_naf_db": "5610C",
    "effectif_db": "3-5",
    "denomination": "MARECHAL",
    "categorie_entreprise": "PME",
    "nature_juridique": "5710",
    "date_creation": "2016-11-15",
    "date_fermeture": null,
    "etat_administratif": "A",
    "section_activite": "I",
    "tranche_effectif": "02",
    "annee_effectif": "2023",
    "nb_etablissements": 2,
    "nb_etablissements_ouverts": 1,
    "siege": {
      "adresse": "9 RUE DU BAT D'ARGENT 69001 LYON",
      "code_postal": "69001",
      "commune": "LYON",
      "departement": "69",
      "latitude": "45.766165",
      "longitude": "4.835315"
    },
    "dirigeants": [
      {
        "nom": "OGER RUBY (OGER)",
        "prenoms": "BRIEUC PIERRE",
        "qualite": "Président de SAS",
        "type": "personne physique",
        "denomination": null
      }
    ],
    "convention_collective": [
      "1501"
    ]
  },
  {
    "procedure_id": 174072,
    "siren": "919299719",
    "raison_sociale_db": "PELICAN",
    "score_global": 85.95,
    "code_naf_db": "5510Z",
    "effectif_db": "3-5",
    "denomination": "PELICAN",
    "categorie_entreprise": "PME",
    "nature_juridique": "5202",
    "date_creation": "2022-09-13",
    "date_fermeture": null,
    "etat_administratif": "A",
    "section_activite": "I",
    "tranche_effectif": "02",
    "annee_effectif": "2023",
    "nb_etablissements": 2,
    "nb_etablissements_ouverts": 2,
    "siege": {
      "adresse": "5 RUE LINCOLN 75008 PARIS",
      "code_postal": "75008",
      "commune": "PARIS",
      "departement": "75",
      "latitude": "48.870059",
      "longitude": "2.302538"
    },
    "dirigeants": [
      {
        "nom": null,
        "prenoms": null,
        "qualite": "Gérant et associé indéfiniment et solidairement responsable",
        "type": "personne morale",
        "denomination": "LA FONCIERE DE SHERY"
      },
      {
        "nom": null,
        "prenoms": null,
        "qualite": "Associé indéfiniment et solidairement responsable",
        "type": "personne morale",
        "denomination": "HOLDING FONCIERE DE L'IMMOBILIER"
      },
      {
        "nom": null,
        "prenoms": null,
        "qualite": "Associé indéfiniment et solidairement responsable",
        "type": "personne morale",
        "denomination": "HOLDING SHERYNE"
      }
    ],
    "convention_collective": [
      "1979"
    ]
  },
  {
    "procedure_id": 157082,
    "siren": "880031893",
    "raison_sociale_db": "WASSIMA SOCIETY",
    "score_global": 85.81,
    "code_naf_db": "5610C",
    "effectif_db": "3-5",
    "denomination": "WASSIMA SOCIETY (WASSIMA SOCIETY)",
    "categorie_entreprise": "PME",
    "nature_juridique": "5710",
    "date_creation": "2019-12-19",
    "date_fermeture": null,
    "etat_administratif": "A",
    "section_activite": "I",
    "tranche_effectif": "02",
    "annee_effectif": "2023",
    "nb_etablissements": 2,
    "nb_etablissements_ouverts": 1,
    "siege": {
      "adresse": "188 GRANDE RUE DE LA GUILLOTIERE 69007 LYON",
      "code_postal": "69007",
      "commune": "LYON",
      "departement": "69",
      "latitude": "45.748725",
      "longitude": "4.853991"
    },
    "dirigeants": [
      {
        "nom": "AHMED",
        "prenoms": "JALIL LITON",
        "qualite": "Président de SAS",
        "type": "personne physique",
        "denomination": null
      }
    ],
    "convention_collective": [
      "1501"
    ]
  },
  {
    "procedure_id": 157791,
    "siren": "881467385",
    "raison_sociale_db": "CAFEINCUP LE BOUSCAT",
    "score_global": 85.7,
    "code_naf_db": "5610C",
    "effectif_db": "6-9",
    "denomination": "CAFEINCUP LE BOUSCAT",
    "categorie_entreprise": "PME",
    "nature_juridique": "5499",
    "date_creation": "2020-01-21",
    "date_fermeture": null,
    "etat_administratif": "A",
    "section_activite": "I",
    "tranche_effectif": "03",
    "annee_effectif": "2023",
    "nb_etablissements": 2,
    "nb_etablissements_ouverts": 2,
    "siege": {
      "adresse": "15-17 15 RUE DES ARGENTIERS 33000 BORDEAUX",
      "code_postal": "33000",
      "commune": "BORDEAUX",
      "departement": "33",
      "latitude": "44.8393",
      "longitude": "-0.570077"
    },
    "dirigeants": [
      {
        "nom": "THIRANT",
        "prenoms": "JIMMY LOUIS",
        "qualite": "Gérant",
        "type": "personne physique",
        "denomination": null
      }
    ],
    "convention_collective": [
      "1501"
    ]
  },
  {
    "procedure_id": 173436,
    "siren": "918078528",
    "raison_sociale_db": "CAFEINCUP PESSAC",
    "score_global": 85.7,
    "code_naf_db": "5610C",
    "effectif_db": "6-9",
    "denomination": "CAFEINCUP PESSAC",
    "categorie_entreprise": "PME",
    "nature_juridique": "5499",
    "date_creation": "2022-08-03",
    "date_fermeture": null,
    "etat_administratif": "A",
    "section_activite": "I",
    "tranche_effectif": "03",
    "annee_effectif": "2023",
    "nb_etablissements": 1,
    "nb_etablissements_ouverts": 1,
    "siege": {
      "adresse": "PROGRAMME COEUR BRESOL - KIOSQUE C 28 AVENUE GUSTAVE EIFFEL 33600 PESSAC",
      "code_postal": "33600",
      "commune": "PESSAC",
      "departement": "33",
      "latitude": "44.780963",
      "longitude": "-0.651343"
    },
    "dirigeants": [
      {
        "nom": "THIRANT",
        "prenoms": "JIMMY LOUIS",
        "qualite": "Gérant",
        "type": "personne physique",
        "denomination": null
      }
    ],
    "convention_collective": null
  },
  {
    "procedure_id": 140976,
    "siren": "818313447",
    "raison_sociale_db": "CAFEINCUP",
    "score_global": 85.7,
    "code_naf_db": "5610C",
    "effectif_db": "6-9",
    "denomination": "CAFEINCUP (CAFEINCUP)",
    "categorie_entreprise": "PME",
    "nature_juridique": "5499",
    "date_creation": "2016-02-09",
    "date_fermeture": null,
    "etat_administratif": "A",
    "section_activite": "I",
    "tranche_effectif": "03",
    "annee_effectif": "2023",
    "nb_etablissements": 2,
    "nb_etablissements_ouverts": 1,
    "siege": {
      "adresse": "15-17 15 RUE DES ARGENTIERS 33000 BORDEAUX",
      "code_postal": "33000",
      "commune": "BORDEAUX",
      "departement": "33",
      "latitude": "44.8393",
      "longitude": "-0.570077"
    },
    "dirigeants": [
      {
        "nom": "THIRANT",
        "prenoms": "JIMMY LOUIS",
        "qualite": "Gérant",
        "type": "personne physique",
        "denomination": null
      }
    ],
    "convention_collective": [
      "1501"
    ]
  },
  {
    "procedure_id": 74774,
    "siren": "845239888",
    "raison_sociale_db": "PRANA",
    "score_global": 85.6,
    "code_naf_db": "5610A",
    "effectif_db": "3-5",
    "denomination": "PRANA (PRANA RESTAURANT)",
    "categorie_entreprise": "PME",
    "nature_juridique": "5710",
    "date_creation": "2019-01-04",
    "date_fermeture": null,
    "etat_administratif": "A",
    "section_activite": "I",
    "tranche_effectif": "02",
    "annee_effectif": "2023",
    "nb_etablissements": 1,
    "nb_etablissements_ouverts": 1,
    "siege": {
      "adresse": "5 RUE DUHAMEL 69002 LYON",
      "code_postal": "69002",
      "commune": "LYON",
      "departement": "69",
      "latitude": "45.750394",
      "longitude": "4.829325"
    },
    "dirigeants": [
      {
        "nom": "BARONIAN",
        "prenoms": "PIERRE VAROUJAN",
        "qualite": "Président de SAS",
        "type": "personne physique",
        "denomination": null
      }
    ],
    "convention_collective": [
      "1979"
    ]
  },
  {
    "procedure_id": 10198,
    "siren": "851395012",
    "raison_sociale_db": "SUBMART",
    "score_global": 85.58,
    "code_naf_db": "5610A",
    "effectif_db": "3-5",
    "denomination": "SUBMART (PARTAGE BRASSERIE)",
    "categorie_entreprise": "PME",
    "nature_juridique": "5710",
    "date_creation": "2019-05-31",
    "date_fermeture": null,
    "etat_administratif": "A",
    "section_activite": "I",
    "tranche_effectif": "02",
    "annee_effectif": "2023",
    "nb_etablissements": 1,
    "nb_etablissements_ouverts": 1,
    "siege": {
      "adresse": "79 RUE DIDOT 75014 PARIS",
      "code_postal": "75014",
      "commune": "PARIS",
      "departement": "75",
      "latitude": "48.829487",
      "longitude": "2.317832"
    },
    "dirigeants": [
      {
        "nom": "SUBRAN",
        "prenoms": "MATHIEU PIERRE MICHEL",
        "qualite": "Président de SAS",
        "type": "personne physique",
        "denomination": null
      }
    ],
    "convention_collective": null
  },
  {
    "procedure_id": 109435,
    "siren": "753489012",
    "raison_sociale_db": "ABBOUFFE",
    "score_global": 85.5,
    "code_naf_db": "5610A",
    "effectif_db": "3-5",
    "denomination": "ABBOUFFE (CAVALINO)",
    "categorie_entreprise": "PME",
    "nature_juridique": "5499",
    "date_creation": "2012-07-01",
    "date_fermeture": null,
    "etat_administratif": "A",
    "section_activite": "I",
    "tranche_effectif": "02",
    "annee_effectif": "2023",
    "nb_etablissements": 1,
    "nb_etablissements_ouverts": 1,
    "siege": {
      "adresse": "96 AVENUE DAUMESNIL 75012 PARIS",
      "code_postal": "75012",
      "commune": "PARIS",
      "departement": "75",
      "latitude": "48.843304",
      "longitude": "2.383244"
    },
    "dirigeants": [
      {
        "nom": "SIMON",
        "prenoms": "VANESSA VIRGINIE JEANINE",
        "qualite": "Gérant",
        "type": "personne physique",
        "denomination": null
      }
    ],
    "convention_collective": [
      "1979"
    ]
  },
  {
    "procedure_id": 115395,
    "siren": "912262698",
    "raison_sociale_db": "LES DEMENAGEURS DE LA LIMAGNE",
    "score_global": 85.44,
    "code_naf_db": "4941B",
    "effectif_db": "6-9",
    "denomination": "LES DEMENAGEURS DE LA LIMAGNE (LES DEMENAGEURS DE LA LIMAGNE)",
    "categorie_entreprise": "PME",
    "nature_juridique": "5499",
    "date_creation": "2022-02-22",
    "date_fermeture": null,
    "etat_administratif": "A",
    "section_activite": "H",
    "tranche_effectif": "03",
    "annee_effectif": "2023",
    "nb_etablissements": 4,
    "nb_etablissements_ouverts": 3,
    "siege": {
      "adresse": "4 RUE LOUIS ROSIER 63000 CLERMONT-FERRAND",
      "code_postal": "63000",
      "commune": "CLERMONT-FERRAND",
      "departement": "63",
      "latitude": "45.764441",
      "longitude": "3.132566"
    },
    "dirigeants": [
      {
        "nom": "BOTTIN",
        "prenoms": "SEBASTIEN STEPHANE BERNARD",
        "qualite": "Gérant",
        "type": "personne physique",
        "denomination": null
      },
      {
        "nom": "KREMER",
        "prenoms": "SYLVAIN RENE ALBERT",
        "qualite": "Gérant",
        "type": "personne physique",
        "denomination": null
      }
    ],
    "convention_collective": [
      "0016"
    ]
  },
  {
    "procedure_id": 150143,
    "siren": "841689300",
    "raison_sociale_db": "SANTOSHA TALENCE",
    "score_global": 85.4,
    "code_naf_db": "5610A",
    "effectif_db": "3-5",
    "denomination": "SANTOSHA TALENCE (SANTOSHA TALENCE)",
    "categorie_entreprise": "PME",
    "nature_juridique": "5499",
    "date_creation": "2018-08-13",
    "date_fermeture": null,
    "etat_administratif": "A",
    "section_activite": "I",
    "tranche_effectif": "02",
    "annee_effectif": "2023",
    "nb_etablissements": 1,
    "nb_etablissements_ouverts": 1,
    "siege": {
      "adresse": "337-349-RESIDENCE LES NOBEL 337 COURS DE LA LIBERATION 33400 TALENCE",
      "code_postal": "33400",
      "commune": "TALENCE",
      "departement": "33",
      "latitude": "44.809948",
      "longitude": "-0.591471"
    },
    "dirigeants": [
      {
        "nom": "MEURET",
        "prenoms": "EMMANUEL",
        "qualite": "Gérant",
        "type": "personne physique",
        "denomination": null
      },
      {
        "nom": "QUEAU",
        "prenoms": "THOMAS",
        "qualite": "Gérant",
        "type": "personne physique",
        "denomination": null
      }
    ],
    "convention_collective": [
      "1979"
    ]
  },
  {
    "procedure_id": 150510,
    "siren": "842433989",
    "raison_sociale_db": "SANTOSHA PESSAC",
    "score_global": 85.4,
    "code_naf_db": "5610A",
    "effectif_db": "3-5",
    "denomination": "SANTOSHA PESSAC",
    "categorie_entreprise": "PME",
    "nature_juridique": "5499",
    "date_creation": "2018-09-14",
    "date_fermeture": null,
    "etat_administratif": "A",
    "section_activite": "I",
    "tranche_effectif": "02",
    "annee_effectif": "2023",
    "nb_etablissements": 2,
    "nb_etablissements_ouverts": 2,
    "siege": {
      "adresse": "2 PLACE FERNAND LAFARGUE 33000 BORDEAUX",
      "code_postal": "33000",
      "commune": "BORDEAUX",
      "departement": "33",
      "latitude": "44.837044",
      "longitude": "-0.571563"
    },
    "dirigeants": [
      {
        "nom": "MEURET",
        "prenoms": "EMMANUEL",
        "qualite": "Gérant",
        "type": "personne physique",
        "denomination": null
      },
      {
        "nom": "REYNOSO",
        "prenoms": "FRANCOIS",
        "qualite": "Gérant",
        "type": "personne physique",
        "denomination": null
      }
    ],
    "convention_collective": [
      "1979"
    ]
  },
  {
    "procedure_id": 153909,
    "siren": "850858259",
    "raison_sociale_db": "SANTOSHA SAINT MEDARD EN JALLES",
    "score_global": 85.4,
    "code_naf_db": "5610A",
    "effectif_db": "3-5",
    "denomination": "SANTOSHA SAINT MEDARD EN JALLES",
    "categorie_entreprise": "PME",
    "nature_juridique": "5499",
    "date_creation": "2019-05-14",
    "date_fermeture": null,
    "etat_administratif": "A",
    "section_activite": "I",
    "tranche_effectif": "02",
    "annee_effectif": "2023",
    "nb_etablissements": 3,
    "nb_etablissements_ouverts": 3,
    "siege": {
      "adresse": "2 PLACE FERNAND LAFARGUE 33000 BORDEAUX",
      "code_postal": "33000",
      "commune": "BORDEAUX",
      "departement": "33",
      "latitude": "44.837044",
      "longitude": "-0.571563"
    },
    "dirigeants": [
      {
        "nom": "GERMANEAU",
        "prenoms": "BENOIT",
        "qualite": "Gérant",
        "type": "personne physique",
        "denomination": null
      },
      {
        "nom": "HOBLOSS",
        "prenoms": "SAMER",
        "qualite": "Gérant",
        "type": "personne physique",
        "denomination": null
      }
    ],
    "convention_collective": [
      "1979"
    ]
  }
]
```

## Cycle 17:10

- **Scrape AJ** : lancement...

## Cycle 17:11

- **Scrape AJ** : lancement...
  - OK : 456 opportunites scrapees
