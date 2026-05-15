# QUEUE — Opportunités en attente de traitement

*Mise à jour : 2026-05-09 — auto-enrichment*

## Priorité URGENTE (deadline < 7 jours)

| Slug | Entreprise | CA | Effectif | Deadline | AJ |
|------|-----------|-----|----------|----------|----|
| viticulture | Coopérative viticole Banyuls-Collioure | 14 M€ | 140 | **2026-05-11** | Abitol & Rousselet |
| smr | Clinique SMR Éguilles | 6,6 M€ | 90 | **2026-05-17** | Abitol & Rousselet |
| seralu | SERALU (structures métalliques) | 25,9 M€ | 48 | **2026-05-18** | AjIRE |

## Priorité HAUTE (score ≥ 70)

| Slug | Entreprise | CA | Effectif | Deadline | AJ |
|------|-----------|-----|----------|----------|----|
| almat-bennes-manjot | ALMAT INVES'T / BENNES MANJOT | 1,6 M€ | 50 | 2025-01-20 | Meynet |
| cloud-computing-b2b | Cloud Computing B2B (IDF) | 2,3 M€ | 40 | 2026-04-15 | Abitol & Rousselet |
| oogarden | OOGARDEN (e-commerce jardinerie) | 54 M€ | 100 | 2023-11-16 | Meynet |

## Priorité NORMALE (score 60-70)

| Slug | Entreprise | CA | Effectif | Deadline | AJ |
|------|-----------|-----|----------|----------|----|
| ideal-tiny | IDEAL TINY (tiny houses) | 2,4 M€ | 20 | 2026-06-09 | AjIRE |
| patisserie-paris | Pâtisserie Paris (4 boutiques) | 2,8 M€ | 39 | 2026-03-31 | Abitol & Rousselet |
| equipements-thermiques | Équipements Thermiques | 1,4 M€ | 20 | 2026-04-29 | Abitol & Rousselet |
| industrie-meyzieu-12518 | Industrie Meyzieu #12518 | 20 M€ | 100 | 2022-02-14 | Meynet |

## Statut dossiers

- Tous les dossiers ci-dessus ont été créés dans `api/data/deals/`
- `enrichment.json` + `analyse.md` présents dans chaque dossier
- Enrichissement Pappers : à réaliser (SIREN non disponibles dans le scrape AJ)
- Matching repreneurs : à réaliser (API locale non démarrée)

## Batch auto-enrichment — 2026-05-12

| Slug | Entreprise | CA | Effectif | Localisation | AJ | Pappers | Repreneurs |
|------|-----------|-----|----------|--------------|-----|---------|------------|
| ajilink-ihdf-pse-ar-val | PSE AR.VAL | Plus de 10M€ | De 50 à 250 | 56 Morbihan | Ajilink IHDF | Non | 0 |
| ajilink-provence-prepack-cession | PREPACK CESSION | Plus de 10M€ | N/A | 13 Bouches-du-Rhône | Ajilink Provence | Non | 1 |
| ajup-transpaumance | TRANSPAUMANCE | De 3 à 10M€ | De 10 à 50 | 03 Allier | AJUP | Oui (477582902) | 5 |
| ajire-auroit | AUROIT (Intermarché) | De 3 à 10M€ | De 10 à 50 | 72 Sarthe | AjIRE | Oui (401278379) | 5 |
| ajilink-grandest-ks-securite | KS SECURITE | De 3 à 10M€ | Plus de 250 | 67 Bas-Rhin | Ajilink Grand Est | Oui (792935694) | 5 |
| ajup-recherche-partenaires-dans-le-cadre-d-une-procedure-de- | SAS TROUILLET & CIE | De 3 à 10M€ | De 10 à 50 | 42 Loire | AJUP | Non | 0 |
| ajilink-ihdf-ikomobi | IKOMOBI | De 1 à 3M€ | De 10 à 50 | 59 Nord | Ajilink IHDF | Oui (514418748) | 5 |
| ajup-a-b-loisirs | A-B LOISIRS | De 1 à 3M€ | De 10 à 50 | 42 Loire | AJUP | Oui (380370395) | 0 |
| ajup-secat | SECAT (abattoir) | De 1 à 3M€ | De 10 à 50 | 69 Rhône | AJUP | Oui (523167062) | 0 |
| ajilink-grandest-debos-style | DEBOS'STYLE | De 1 à 3M€ | Moins de 10 | 67 Bas-Rhin | Ajilink Grand Est | Oui (525159877) | 0 |

## Related

- [[brantham/_MOC]]
- [[brantham/pipeline/BOARD]]

## Ajout auto — 2026-05-10

| Slug | Entreprise | CA | Effectif | Source AJ |
|------|-----------|-----|----------|-----------|
| ajrs-la-sarl-james-chague-a-ete-creee-en-7913 | La SARL JAMES CHAGUE | 415.89M | 32 | AJRS |
| aj-specialis-viand-oc-249 | VIAND OC | 199.69M | 9 | AJ Spécialisés |
| meynet-oogarden-13010 | OOGARDEN | 54.00M | 100-199 | Meynet |
| meynet-centre-est-peintures-distribution-14029 | CENTRE EST PEINTURES DISTRIBUTION | 30.38M | 100-199 | Meynet |
| meynet-b-t-t-p-13420 | B.T.T.P. | 24.05M | 20-49 | Meynet |
| meynet-industrie-12518-12518 | Industrie #12518 | 20.00M | 100-199 | Meynet |
| meynet-sas-b-m-c-12457 | SAS B.M.C. | 19.00M | 0-5 | Meynet |
| meynet-commerce-de-detail-14160-14160 | Commerce de détail #14160 | 16.60M | 6-19 | Meynet |
| meynet-via-transports-14177 | VIA TRANSPORTS | 10.00M | 20-49 | Meynet |
| meynet-beaute-services-et-innovation-13241 | BEAUTE SERVICES ET INNOVATION | 9.83M | 6-19 | Meynet |

## Batch auto-enrichment — 2026-05-11 14:03

| Nom | CA | Effectif | Localisation | AJ | Statut |
|-----|----|----|------|-------|--------|
| VIAND OC                            | 1 996 851.00         | 9 salaries      |                           | AJ Spécialisés  | NOUVEAU |
| EPIFURIEU                           | 733 000,00           | 11 salaries     |                           | AJ Spécialisés  | NOUVEAU |
| BEL AIR REALISATIONS                | Plus de 50 M€        | 0 à 50 salariés | Ain, Auvergne-Rhône-Alpes | Maydaymag       | NOUVEAU |
| AYEN                                | Plus de 50 M€        | 0 à 50 salariés | Bretagne, Morbihan        | Maydaymag       | NOUVEAU |
| LE ROYAUME DES DELICES              | Plus de 50 M€        | 0 à 50 salariés | Ile de France, Seine-Sain | Maydaymag       | NOUVEAU |
| AUTO SHINE                          | Plus de 50 M€        | Plus de 500 sal | Ile de France             | Maydaymag       | NOUVEAU |
| YOHETSET                            | Plus de 50 M€        | Plus de 500 sal | Bouches-du-Rhône, Provenc | Maydaymag       | NOUVEAU |
| PFI RAVALEMENTS                     | Plus de 50 M€        | 0 à 50 salariés | Ain, Auvergne-Rhône-Alpes | Maydaymag       | NOUVEAU |
| KOUBA                               | Plus de 50 M€        | Plus de 500 sal | Ain, Auvergne-Rhône-Alpes | Maydaymag       | NOUVEAU |
| OTHAYSSIE                           | Plus de 50 M€        | Plus de 500 sal | Ariège, Occitanie         | Maydaymag       | NOUVEAU |


---

## Batch auto-enrichment — 2026-05-15

| Slug | Entreprise | CA | AJ | Statut |
|------|-----------|-----|-----|--------|
| meynet-commerce-de-d-tail-14160 | Commerce détail #14160 | 16,6 M€ | Meynet | dossier créé |
| meynet-industrie-14566 | Industrie #14566 | 8,2 M€ | Meynet | dossier créé |
| meynet-commerce-de-d-tail-13552 | Commerce détail #13552 | 6,6 M€ | Meynet | dossier créé |
| abitol-and-rousselet-smr | SMR (clinique) | 6,6 M€ | Abitol | dossier créé |
| meynet-anonyme | Anonyme Meynet | 6,2 M€ | Meynet | dossier créé |
| meynet-majolane-de-construction | Majolane Construction | 4,3 M€ | Meynet | dossier créé |
| ajrs-appel-d-offres-dans-le-cadre-d | Appel offres AJRS | 4,1 M€ | AJRS | dossier créé |
| meynet-industrie-12545 | Industrie #12545 | 4 M€ | Meynet | dossier créé |
| meynet-transports-gevaux-sas | Transports Gevaux | 4 M€ | Meynet | dossier créé |
| meynet-anonyme (2) | Anonyme 5M€ | 5 M€ | Meynet | dossier créé |

---

## Batch 2026-05-15 — Nouvelles opportunités identifiées

| Priorité | Deal | CA | Secteur | Localisation | Deadline | Statut |
|----------|------|----|---------|-------------|---------|--------|
| 1 | meynet-sas-groupe-flachet | 2.3M€ | BTP | VILLEURBANNE | 2026-06-01 | A qualifier |
| 2 | aj-specialises-recherche-de-repreneurs-p-tisserie-chocolater | 3M€ | Alimentaire | Pays d'Aix | 2026-06-10 | A qualifier |
| 3 | meynet-solak-energie | 2.5M€ | BTP/Energie | VAULX-EN-VELIN | 2026-06-09 | A qualifier |
| 4 | aj-specialises-2268-reprise-de-deux-fonds-de-commerce-de-joa | 2.3M€ | Joaillerie | NICE | 2026-06-18 | A qualifier |
| 5 | meynet-rfi-sas | 1.3M€ | BTP | Montagnat | 2026-05-26 | URGENT |
| 6 | meynet-repreneurs-activit-de-recrutement-de-talents-et-d-acc | 1.1M€ | RH | Saint-Didier | 2026-05-21 | URGENT |
| 7 | maydaymag-soci-t-sp-cialis-e-dans-l-dition-de-solutions-d-in | 939K€ | SaaS/SIG | N/A | 2026-06-02 | A qualifier |
| 8 | meynet-soci-t-lucca-auberge-d-archamps | 569K€ | HCR | ARCHAMPS | 2026-05-28 | URGENT |

**Actions requises** :
- meynet-rfi-sas et meynet-repreneurs : deadline < 10j, contacter mandataire Meynet en priorité
- meynet-soci-t-lucca : deadline 28/05, HCR avec emplacement à vérifier
- 2 SIRENs résolus : SOLAK ENERGIE (535364798), RFI SAS (818024317)
- Enrichissement Pappers : bilans non disponibles — vérifier INPI manuellement
