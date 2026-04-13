---
name: Synthese flotte automobile Allianz
description: Note interne 5 vehicules assures Allianz - 3 Mercedes + 1 Peugeot + 1 Mini - total annuel ~7 540 EUR TTC
type: reference
doc_source: 86/3-MOYENS/ASSURANCES/Synthese assurance flotte automobile Allianz.pdf
pages: 1
date_doc: ~mars 2026
---

# Doc 24 — Synthese contrats flotte Allianz

## Nature
Note interne INGEBIME pour dataroom — tableau synthetique de la flotte automobile assuree

## Tableau des 5 vehicules

| Vehicule | Immatriculation | Assureur | N° contrat | Couverture | Prime trimestrielle |
|---|---|---|---|---|---|
| Mercedes Classe A | **FJ-826-BK** | Allianz | AF419064473 | Tous risques | 285,95 EUR |
| Mercedes Classe A | **FJ-768-BK** | Allianz | AF419064515 | Tous risques | 285,95 EUR |
| Mercedes Classe A | **FJ-805-BK** | Allianz | AF419064461 | Tous risques | 285,95 EUR |
| Peugeot 3008 | **GT-956-GE** | Allianz | AF414699472 | Tous risques | 539,95 EUR |
| Mini Countryman | **FW-027-LP** | Allianz | AF419332205 | Tous risques | 488,13 EUR (mensualise) |

## Observations listees
- **Nombre total : 5 vehicules**
- **Assureur unique** : Allianz
- Flotte **integralement en tous risques**
- **Intermediaire unique** : Allianz Nanterre (LAROZA & GERONDEAU)
- Prime Mini Cooper **mensualisee** et presentee en equivalent trimestriel

## Calcul des cumuls
- Total trimestriel : 285,95 × 3 + 539,95 + 488,13 = **1 885,93 EUR/trim**
- **Total annuel : ~7 543,72 EUR TTC**

## Points notables bruts (CRITIQUE — INCOHERENCES MULTIPLES)

### 1. 3eme Mercedes revelee : **FJ-768-BK**
- **Vehicule non mentionne** dans l'etat d'endettement greffe (doc 03)
- **Contrat Allianz AF419064515** : nouveau N° contrat non present dans les autres docs
- **Vehicule present dans le releve sinistres CIC** (doc 23) avec 4 sinistres bris de glace / circulation / stationnement entre 2022-2024
- **Probable hypothese** : vehicule repris en LLD ou achete cash — credit-bail non inscrit au greffe
- **Total flotte = 5 vehicules** (pas 4 comme l'etat d'endettement laissait penser)

### 2. Incoherences de primes vs docs 14/15/16/17
| Vehicule | Doc 24 (synthese) | Docs 14-17 (appels reels) | Ecart |
|---|---|---|---|
| **FJ-805-BK Mercedes** | 285,95 EUR/trim | **633,06 EUR/trim** | x2,2 |
| **FJ-826-BK Mercedes** | 285,95 EUR/trim | **440,69 EUR/trim** | x1,5 |
| **FJ-768-BK Mercedes** | 285,95 EUR/trim | Aucun appel dans dataroom | ? |
| **Peugeot 3008** | 539,95 EUR/trim | **539,95 EUR/trim** | OK |
| **Mini Countryman** | 488,13 EUR/trim | Remboursement -1 138 EUR / mens 162,71 EUR | differents |

- **INGEBIME a declare des primes sous-evaluees** pour les 2 Mercedes dans la synthese
  - Pour les FJ-805-BK et FJ-826-BK, la note affiche **285,95 EUR** alors que les appels reels sont 633 et 441 EUR
  - **Sous-declaration significative** : la flotte est presentee avec une prime totale annuelle d'environ **7 544 EUR TTC**, alors que le cumul reel des appels actuels est probablement plutot **10 000-12 000 EUR/an**
  - Probable ERREUR de copie de donnees ou volontaire minimisation

### 3. Equivalent trimestriel Mini
- La note dit "prime Mini mensualisee equivalent trimestriel 488,13 EUR"
- **162,71 EUR × 3 = 488,13 EUR** : OK coherent avec le doc 16 (mensualite future apres remboursement)
- Mais c'est la prime **APRES** le remboursement de 1 138 EUR — la prime anterieure devait etre bien plus elevee

### 4. Reconciliation vehicules
- **Etat d'endettement greffe (doc 03)** : 4 vehicules inscrits en credit-bail (Mercedes GLB 2020, Mercedes GLB 2021, Mini, Mercedes EQE, Peugeot) — mais Mercedes EQE et GLB ne sont PAS les memes immatriculations que les FJ-805/826/768-BK !
  - Les 2 Mercedes GLB du doc 03 (2020 et 2021) : soldes a 0 — probablement les 2 FJ-805-BK et FJ-826-BK
  - Mais le doc 03 parle de **Mercedes-AMG EQE 43 4MATIC** (nouveau, credit-bail janvier 2024) — **ce vehicule n'est pas dans la synthese flotte doc 24** ! Vehicule de luxe probablement restitue ou cede rapidement
- **Nouveaux vehicules inconnus du doc 03** :
  - FJ-768-BK (3eme Mercedes Classe A) — hors credit-bail ou achete cash
- **Vehicule du doc 03 absent de la flotte actuelle** :
  - Mercedes-AMG EQE 43 4MATIC (credit-bail 05/01/2024 MBFS)

### 5. Autres points
- **Pas de Kia GB-397-WR** dans la synthese — coherent avec resiliation CIC et apparent non-rassurance Allianz (vehicule vraisemblablement restitue apres resiliation CIC)
- Gestion "centralisee" via LAROZA & GERONDEAU Nanterre = agent general Allianz (pas un veritable courtier)
- **Documents justificatifs** : appels de cotisation en annexe (docs 14-17 + 20)

## Related
- [[brantham/deals/active/ingebime/docs/03-etat-endettement]]
- [[brantham/deals/active/ingebime/docs/14-assurance-mercedes-FJ-805-BK]]
- [[brantham/deals/active/ingebime/docs/15-assurance-mercedes-FJ-826-BK]]
- [[brantham/deals/active/ingebime/docs/16-assurance-mini-cooper-FW-027-LP]]
- [[brantham/deals/active/ingebime/docs/17-assurance-peugeot-3008]]
- [[brantham/deals/active/ingebime/docs/20-avis-reglement-allianz]]
- [[brantham/deals/active/ingebime/docs/23-releve-sinistres-cic]]
