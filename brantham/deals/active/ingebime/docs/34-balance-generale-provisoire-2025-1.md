---
name: Balance générale provisoire 2025 (v1) INGEBIME
description: Balance générale provisoire 2025 — perte 1,156 M€, dettes sociales 1,5 M€, capitaux propres négatifs 1,1 M€, filiale Côte d'Ivoire découverte
type: reference
doc_source: 86/4-COMPTABILITE/balances/Balance générale provisoire 2025-1.pdf
pages: 5
date_doc: édition 09/04/2026 — période 01/01/2025 → 31/12/2025
---

# Doc 34 — Balance générale provisoire 2025 (version 1)

## Nature
**Document de loin le plus critique du data room.** Balance générale comptable provisoire de l'exercice 2025. Révèle la structure complète du bilan + compte de résultat, le passif fiscal et social, et une filiale Côte d'Ivoire non mentionnée ailleurs.

## Synthèse du compte de résultat 2025

| | Montant |
|---|---|
| **Produits (CA)** | **1 141 443,36 €** |
| **Charges** | **2 297 492,57 €** |
| **RÉSULTAT** | **−1 156 049,21 €** |

**Lecture brutale** : perte = 101 % du chiffre d'affaires. Structure opérationnelle intenable à ce niveau de revenu.

> **ATTENTION** : le CA de 1,14 M€ semble **anormalement bas** vs estimation historique ~3 M€ (cohérence à vérifier avec la Balance générale provisoire 2025 "finale" — Doc 35 — et les Bilans 2021-2024). Deux hypothèses :
> - **H1** : la balance est réellement exhaustive et l'activité s'est effondrée en 2025 (perte massive de contrats → cause directe du RJ)
> - **H2** : balance tronquée / partielle au 1er semestre ou 1er trimestre (suffixe "-1" dans le nom de fichier + qualificatif "provisoire")
>
> **À trancher en priorité avec le Doc 35**.

## Structure du passif — où est la dette ?

### Dettes sociales ≈ 1 513 000 €

| Compte | Libellé | Montant |
|---|---|---|
| 43100000 | **Sécurité sociale (URSSAF)** | **825 300,79 €** |
| 43720000 | Humanis prévoyance | 330 619,35 € |
| 42100000 | Salariés (compte général) | 209 918,78 € |
| 42820000 | Dettes provisionnées congés | 60 057,37 € |
| 43730000 | Caisses de retraite | 36 723,84 € |
| 43750000 | Plan santé | 25 434,60 € |
| 43820000 | Charges sociales sur congés à payer | 22 463,32 € |
| 42500000 | Personnel avances acomptes | 10 764,00 € |

**→ La dette URSSAF seule (825 k€) est ~6 mois de cotisations sociales** sur une masse salariale annuelle de 1,65 M€. Signal typique de société qui a arrêté de payer l'URSSAF pour financer le cash courant — **cause n° 1 de déclenchement RJ en France**.

### Dettes fiscales ≈ 878 000 €

| Compte | Libellé | Montant |
|---|---|---|
| 44576000 | TVA collectée à 20 % | 223 944,55 € |
| 44551000 | TVA à décaisser | 196 983,89 € |
| 44588000 | **TVA à régulariser** | **160 653,21 €** |
| 44210000 | Prélèvements à la source (IR salariés) | 110 913,57 € |
| 44230000 | Retenues et prélèvements sur salaires | 93 402,36 € |
| 44400000 | Impôt sur les bénéfices (acomptes) | 38 674,09 € |
| 44571100 | TVA collectée 20 % débits | 35 603,29 € |
| 44571130 | TVA collectée 10 % débits | 14 990,83 € |
| 44700000 | Autres impôts et taxes | 1 320,00 € |
| 44860000 | État charges à payer | 1 130,00 € |

**→ TVA collectée non reversée ≈ 475 k€ + prélèvement à la source ≈ 204 k€ = 679 k€** de dettes privilégiées État. Le Trésor est en première ligne des créanciers post-RJ — **super privilège**.

### Dettes fournisseurs (confirme Doc 33 mais à jour 2025)

| Compte | Libellé | Montant |
|---|---|---|
| 401 | Total fournisseurs | **785 674,65 €** |
| 40800000 | Fournisseurs - factures non parvenues (FNP) | 20 295,14 € |

→ **Dette fournisseurs 2025 = 805 970 €**, soit **+42 %** vs 564 k€ en 2024 (Doc 33). **Dégradation nette** du poste fournisseur en 2025.

### Synthèse du passif exigible

| Nature | Montant |
|---|---|
| Dettes fournisseurs + FNP | 805 970 € |
| Dettes sociales (URSSAF, retraite, prévoyance, santé, salariés) | 1 513 000 € |
| Dettes fiscales (TVA, IR source, IS) | 878 000 € |
| **TOTAL PASSIF EXIGIBLE COURT TERME** | **≈ 3 197 000 €** |

**À comparer avec** :
- Créances clients nettes : 1 144 569 €
- **Trou de trésorerie théorique : ≈ 2,05 M€**

## Actif circulant & immobilisations

### Clients
- **41 — Total 411 Clients** : 1 144 569,37 € (confirme Doc 32)
- **41600000 — Clients douteux ou litigieux : 458 268,32 €** — **40 % des créances sont en procédure / contentieux !**
- **49100000 — Dépréciations comptes clients : 245 502,22 €** (provision)
- **41910000 — Clients avances et acomptes reçus : 107 450,83 €**
- **40910000 — Fournisseurs, avances et acomptes versés : 25 050,00 €**

**Créances clients nettes après provisions** : 1 144 569 − 245 502 = **899 067 €**.

### Immobilisations (valeurs brutes vs amortissements)

| Compte | Libellé | Brut | Amort. | **VNC** |
|---|---|---|---|---|
| 20500000 | Logiciels | 48 524 | 18 345 | **30 179 €** |
| 21550000 | Outillage industriel | 10 034 | 4 478 | **5 556 €** |
| 21810000 | Installations générales, agencements | 169 364 | 92 936 | **76 428 €** |
| 21820000 | Matériel de transport | 96 962 | 33 246 | **63 716 €** |
| 21830000 | Matériel bureau et informatique | 106 062 | 70 339 | **35 723 €** |
| 21840000 | Mobilier | 55 161 | 54 234 | **927 €** |
| | **Sous-total corporel + incorporel** | | | **≈ 212 529 €** |
| 26100000 | **TITRES INGEBIME CÔTE D'IVOIRE** | 39 000 | 0 | **39 000 €** |
| 27400000 | Prêts | 49 000 | 0 | 49 000 € |
| 27430000 | Prêts au personnel | 35 833 | 0 | 35 833 € |
| 27500000 | Dépôts et cautionnements versés | 69 549 | 0 | 69 549 € |

### DÉCOUVERTE MAJEURE — Filiale Côte d'Ivoire (compte 26100000 — 39 000 €)

**Aucun autre document du data room ne mentionne cette filiale.** Ligne "TITRES INGEBIME COTE D'IVOIRE" au bilan.
- Probable **filiale ou participation** dans une société immatriculée en Côte d'Ivoire portant le nom INGEBIME
- Valeur nominale 39 000 € — peut être sous-évaluée si active, ou surévaluée si dormante
- **À demander en priorité à l'AJ** :
  - Statuts de la filiale ivoirienne
  - % de détention, organes dirigeants, comptes sociaux
  - Activité réelle (bureau relais Afrique de l'Ouest ?)
  - Flux financiers inter-companies (management fees ? refacturation ?)
  - État des engagements (caution, garantie, comfort letter ?)
  - **Risque juridique** : engagements post-reprise ?
  - **Opportunité** : si filiale active → actif stratégique à valoriser dans l'offre (présence Afrique francophone, passerelle commerciale)

### Autres comptes anormaux à creuser
- **46700000 — Autres comptes débiteurs ou créditeurs : 364 800,55 €** (débit) — très gros montant non qualifié, à éclater
- **47100000 — Compte d'attente : 32 393,28 €** — écritures non affectées
- **11900000 — Report à nouveau débiteur : 463 394,27 €** (pertes cumulées antérieures déjà inscrites)
- **11000000 — Report à nouveau créditeur : 361 886,41 €** (bénéfices antérieurs capitalisés)

## Capitaux propres

| Poste | Montant |
|---|---|
| Capital social (10130000) | 100 000 € |
| Réserve légale (10610000) | 10 000 € |
| Report à nouveau créditeur (11000000) | +361 886 € |
| Report à nouveau débiteur (11900000) | −463 394 € |
| **Sous-total avant résultat** | **+8 492 €** |
| Résultat 2025 | **−1 156 049 €** |
| **CAPITAUX PROPRES AU 31/12/2025** | **≈ −1 147 557 €** |

**→ Capitaux propres NÉGATIFS de 1,15 M€**. Société en **perte de plus de la moitié du capital** depuis très longtemps → obligation légale de reconstitution ou dissolution non respectée. Cohérent avec l'ouverture RJ.

## Structure des charges 2025 (2,3 M€)

### Masse salariale (poste n°1 — écrasant)

| Compte | Libellé | Montant |
|---|---|---|
| 64110000 | Salaires, appointements | **1 172 088,26 €** |
| 64510000 | Cotisations sociales (personnel) | 280 142,74 € |
| 64530000 | Cotisations caisses de retraite | 86 544,27 € |
| 64120000 | Congés payés | 67 060,26 € |
| 64140000 | Salaires juillet/24 (régul) | 51 099,72 € |
| 64540000 | Cotisations ASSEDIC | 42 530,65 € |
| 64550000 | Salaires janvier/21 (rappel ancien) | 9 281,38 € |
| 64500000 | Salaires mars/24 | 8 877,68 € |
| 64130000 | Primes et gratifications | 905,00 € |
| **Total masse salariale brute** | | **≈ 1 718 530 €** |
| Moins : 64100000 Rémunération personnel (crédit) | | −114 981 € |
| **Masse salariale nette ~** | | **≈ 1 603 549 €** |

**→ Masse salariale = 140 % du CA 2025 (1,14 M€)**. Même à effectif moitié, la société reste déficitaire si le CA ne rebondit pas.

### Autres postes de charges majeurs

| Compte | Libellé | Montant |
|---|---|---|
| 61100000 | **Sous-traitance générale** | **239 931,40 €** |
| 62260000 | Honoraires (avocats, experts, comptables) | 107 543,95 € |
| 61610000 | Multirisque (assurance) | 95 108,23 € |
| 61320000 | Locations immobilières (bail Nanterre) | 42 350,43 € |
| 65100000 | Redevances concessions (licences logicielles) | 36 259,33 € |
| 62510000 | Déplacements, missions, réceptions | 27 305,75 € |
| 62500000 | Déplacements, missions, réceptions (autre) | 16 103,47 € |
| 60400000 | Prestations sous-traitées | 17 144,39 € |
| 62610000 | Télécom / Internet | 14 919,19 € |
| 61500000 | Entretien et réparations | 13 587,17 € |
| 60610000 | Eau, électricité | 12 555,61 € |
| 60630000 | Petit outillage / entretien | 11 513,39 € |
| 61630000 | Assurance transport | 10 965,87 € |
| 62700000 | Services bancaires | 9 724,13 € |
| 63330000 | Formation professionnelle continue | 6 864,59 € |
| 63130000 | Taxe d'apprentissage | 6 404,35 € |
| 61220000 | Crédit-bail mobilier | 5 205,58 € |
| 60100000 | Achats matières premières | 5 250,00 € |
| 62800000 | Divers | 4 800,00 € |
| 61600000 | Assurances, primes versées | 4 089,73 € |
| 61350000 | Locations mobilières | 4 287,24 € |
| 61200000 | Location crédit-bail | 1 248,67 € |
| 66160000 | Intérêts bancaires | 631,27 € |
| 67120000 | **Pénalités, amendes fiscales** | **649,50 €** (anodines) |
| 61642000 | Assurance | 746,21 € |

### Produits
- **70650000 — Prestations de services 20 % : 1 141 443,35 €** (100 % du CA)
- 75800000 — Produits divers : 0,01 €

## Banques
| Compte | Libellé | Montant |
|---|---|---|
| 51220000 | SOGEXIA | 1,66 € débit |
| 51240000 | BNP | 8,72 € crédit |
| 51260002 | **THEMIS** | **54 107,49 € débit** |
| 58000000 | Virements internes | 8 127,99 € débit |

**→ Trésorerie nette ≈ 62 237 €**. Insignifiant face au passif courant. La société était **techniquement en cessation des paiements** depuis longtemps.

## Points à clarifier en priorité avec l'AJ

### URGENT (bloquants pour le chiffrage de l'offre)
- [ ] **Balance 2025 finale vs provisoire** : quelle est la version "définitive" ? Le CA réel 2025 est-il bien 1,14 M€ ou cette balance est partielle ? → comparer avec Doc 35
- [ ] **Filiale Côte d'Ivoire** (26100000 — 39 k€) : statuts, détention, activité, engagements, comptes
- [ ] **46700000 Autres comptes débiteurs 364 800 €** : détail ligne à ligne
- [ ] **47100000 Compte d'attente 32 393 €** : écritures non affectées
- [ ] **41600000 Clients douteux 458 268 €** : liste nominative + provisions + contentieux en cours
- [ ] Déclaration de créance URSSAF (825 k€) et calendrier des majorations
- [ ] Déclaration de créance DGFiP TVA + IR (679 k€)
- [ ] **Répartition du compte salariés 42100000 (209 918 €)** : salaires non payés + arriérés ?

### IMPORTANT (structurant pour la stratégie)
- [ ] **Liste nominative effectifs 2025** (lien avec Doc 46 et 47)
- [ ] Contrats en cours (backlog) pour justifier la projection de CA post-reprise
- [ ] Échéances prévoyance Humanis (330 k€)
- [ ] **Causes de l'effondrement du CA 2025** : perte de contrat majeur ? litige client ? effondrement du secteur HLM ?
- [ ] État des **prêts au personnel** (27430000 — 35 833 €) : avances salariales ou prêts immobiliers garantis ?
- [ ] **Dépôts et cautionnements** (27500000 — 69 549 €) : à récupérer post-reprise ?

## Implications stratégiques pour l'offre de reprise

### 1. Le passif n'est pas le problème du repreneur (en plan de cession)
Tout le passif ci-dessus (~3,2 M€) **reste dans la procédure** — le repreneur ne reprend pas ces dettes. MAIS :
- **URSSAF** : le super-privilège URSSAF peut impacter les négociations si certaines cotisations sont pour des salariés à reprendre
- **TVA** : idem, la DGFiP peut bloquer certaines opérations
- **Clients douteux 458 k€** : **attention, ces contentieux restent à la procédure** mais peuvent empoisonner la relation commerciale que le repreneur hérite

### 2. La masse salariale est le vrai enjeu
- Masse salariale 1,6 M€ vs CA 1,14 M€ → **restructuration indispensable**
- L'offre de reprise doit **chiffrer précisément l'effectif repris** (continuité vs licenciements économiques post-reprise pris en charge par l'AGS)
- **Levier AGS** : les licenciements économiques dans les 21 jours suivant la reprise sont pris en charge par l'AGS → **levier d'économie massif** (quelques centaines de k€)
- **Dimensionnement cible** : effectif à aligner avec un CA cible de ~2-2,5 M€ (taille viable) → calcul de l'effectif cible à faire dès T+1

### 3. Chiffrage indicatif de l'offre
- **Actifs corporels + incorporels (VNC)** : ~212 k€
- **Dépôts et cautionnements récupérables** : ~70 k€
- **Titres filiale CI** : 39 k€ (à valoriser dès qu'on a info)
- **Valeur incorporelle** (clientèle, backlog, marque, contrats en cours) : à déterminer
- **Prix plancher technique** ≈ 250-350 k€
- **Offre réaliste** : fonction du backlog et de la masse salariale reprise

### 4. Trou de trésorerie à combler au jour 1
- **BFR clients** : ~900 k€ de créances nettes à recouvrer (mais non reprises)
- **Fournisseurs critiques à régler cash** les 2 premiers mois : ~100 k€
- **Salaires courants** : ~130 k€/mois
- **Prévoir 500-700 k€ de trésorerie de démarrage** côté repreneur

## Related
- [[brantham/deals/active/ingebime/docs/03-etat-endettement]]
- [[brantham/deals/active/ingebime/docs/04-jugement-ouverture]]
- [[brantham/deals/active/ingebime/docs/31-balance-clients-2024]]
- [[brantham/deals/active/ingebime/docs/32-balance-clients-2025]]
- [[brantham/deals/active/ingebime/docs/33-balance-fournisseurs]]
- [[brantham/deals/active/ingebime/docs/35-balance-generale-provisoire-2025]]
- [[brantham/deals/active/ingebime/docs/36-balance-provisoire-fournisseur-2025]]
- [[brantham/deals/active/ingebime/docs/40-bilan-2024]]
- [[brantham/deals/active/ingebime/docs/46-liste-effectif-2]]
- [[brantham/deals/active/ingebime/docs/47-liste-effectif]]
- [[brantham/deals/active/ingebime/docs/53-etat-du-passif]]
- [[brantham/deals/active/ingebime/docs/00-note-cadre-offre-reprise]]
- [[_system/MOC-deals]]
- [[brantham/_MOC]]
