---
type: batch_log
batch_id: batch_15_dossiers_15_19_24
created: 2026-05-15
project: brantham
tags: [tc-paris, extraction, grilles, gros-dossiers]
---

# Batch 15 — Gros dossiers TC Paris (3 dossiers, 17 offres)

## Dossiers traités

### 15 - ASSOCIATION MEDICO DENTAIRE D'ENGHIEN LES BAINS
- **Type** : RJ Réseau DENTEKA - 1 candidat unique (MEDIVI/Place Dentaire)
- **PDFs** : 8 (4 originaux gd*.pdf + 4 doublons "26_*offre*.pdf" - tailles identiques, contenu identique). Lu offre_02 (15-04 finale) intégralement + offre_03 partielle via CSV.
- **Offres extraites** : 15-01 à 15-05 (5 fichiers JSON)
  - 15-01 : offre initiale 12/01 (prix placeholder [3] EUR)
  - 15-02 : offre améliorée 27/01 (texte absent des PDFs, référence indirecte)
  - 15-03 : offre améliorée 04/02 (1.300 EUR)
  - 15-04 : offre finale 11/02 (2.600 EUR, après observations Tribunal 09/02) — **offre de référence**
  - 15-05 : offre liée indivisible Colmar 68 (hors stricto sensu dossier 15)

### 19 - SCI LE LOFT
- **Type** : RJ portefeuille Foncière Melot-Gouband "Affaire Balthazar" - 26+ entités consolidées FHBX
- **PDFs** : 8 PDFs lus + croisés avec CSV (qui contenait imprécisions). Identifications corrigées :
  - offre1 = HOUSEBASE mal classé (cible SNC ADONIA)
  - offre2 = UNKNOWN dans CSV → identifié LABRAX INVEST initiale 21.025.000 EUR
  - offre3 = annoncé MUVICO dans CSV → identifié **CORTONA FRANCE** (27 EUR symbolique + L.642-12 al.4)
  - offre4 = MUVICO initiale 260k SCI LE LOFT (portefeuille 13.9M)
  - offre5 = MUVICO améliorée 270k (portefeuille 14M)
  - offre6 = LABRAX finale 21M + appartement Paris 16e
  - offre7 = ARCANGE améliorative 460k SCI LE LOFT (portefeuille 8.713M TTC)
  - offre8 = HOUSEBASE dédiée 10k pour Bagnolet
- **Offres extraites** : LE_LOFT-01 à LE_LOFT-08 (8 fichiers JSON)
- **8 candidats distincts** : HOUSEBASE, LABRAX, MUVICO, ARCANGE, CORTONA (et HOUSEBASE mal classé)
- **Fourchette pour SCI LE LOFT seul** : 10k (HOUSEBASE) → 460k (ARCANGE) → MUVICO 270k

### 24 - SAS LA BELLE FORÊT
- **Type** : Sauvegarde marché carbone volontaire LBC - 4 offres uniques (les 4 PDFs "43_*" sont doublons des "offre_0X_gd*")
- **PDFs** : 8 dont 4 doublons. Lu les 4 originaux intégralement.
- **Offres extraites** : 24-01 à 24-04 (4 fichiers JSON)
  - 24-01 OKLIMA (EDF) : 30k EUR / 0 emplois
  - 24-02 Stock CO2 : 10k EUR / reprise majoritaire (lettre intention non engageante)
  - 24-03 Reforest'Action (B Corp) : 50k EUR / 0 emplois
  - 24-04 Piccolo 5 (Goupille) : 23.432 EUR / 6 emplois sur 8 + plan d'affaires détaillé 2026-2030

## Fichiers produits

```
grilles/dossiers/
├── 15.json  (Enghien RJ)
├── 19.json  (Le Loft RJ - portefeuille FHBX)
└── 24.json  (La Belle Forêt sauvegarde)

grilles/offres/
├── 15-01.json à 15-05.json  (5 offres MEDIVI)
├── LE_LOFT-01.json à LE_LOFT-08.json  (8 offres / 5 candidats distincts)
└── 24-01.json à 24-04.json  (4 offres)
```

**Total : 3 fiches dossier + 17 fiches offre = 20 JSONs**

## Anomalies / Corrections par rapport au CSV master

1. **LE_LOFT-01** : CSV annonçait "HOUSEBASE hors périmètre cible SNC ADONIA" — confirmé : PDF mal classé physiquement
2. **LE_LOFT-02** : CSV indiquait "À identifier - UNKNOWN" — identifié comme **LABRAX INVEST offre initiale 09/02/2026** (21.025.000 EUR portefeuille 28 actifs)
3. **LE_LOFT-03** : CSV indiquait "MUVICO 260k" — corrigé : **CORTONA FRANCE** (Alexandre Molimard, groupe NL) - prix 27 EUR symbolique avec charges augmentatives L.642-12 al.4 estimées 12.5M EUR
4. **LE_LOFT-07** : CSV indiquait "À identifier" — identifié comme **GROUPE ARCANGE améliorative** (Michael SFEDJ)
5. **15-02** : Texte de l'offre 27/01 NON présent dans les PDFs - reference indirecte uniquement (confidence low)

## Signaux faibles intéressants pour Phase 2

- **MEDIVI Enghien** (15-04) : seule candidate sur le centre dentaire mais OFFRE PRIX SYMBOLIQUE 2.600 EUR ferme face à charges augmentatives MASSIVES (~207k cumulés : 50k résiliation bail + 146k cession bail Nanterre + 11k poursuite exploitation + congés payés repris). Pattern "prix nominal + charges augmentatives lourdes" similaire à CORTONA Loft.
- **CORTONA Loft** (LE_LOFT-03) : stratégie radicale 27 EUR + transfert hypothèques L.642-12 al.4 ~12.5M EUR. Pari sur retraitement déclarations de créances (doublons identifiés CIC + Crédit Mutuel).
- **LABRAX Loft** (LE_LOFT-06) : seule offre SANS conditions suspensives (sauf droit applicable vente immeuble) — différenciation crédibilité majeure face à ARCANGE/CORTONA/MUVICO qui sont tous "sous conditions visite+audits".
- **Piccolo 5 La Belle Forêt** (24-04) : seule offre avec **plan d'affaires 5 ans chiffré et détaillé** (tableau 1) + maintien 6/8 salariés + storytelling humain "70 employés recrutés sur 15 ans, 0 licenciement, 0 démission". Probablement gagnante malgré prix moyen.
- **Reforest'Action La Belle Forêt** (24-03) : prix le plus élevé (50k) mais 0 reprise salariés et validité offre courte (31/01/2026) - signaux mitigés.

## Patterns rhétoriques identifiés

1. **"Prix symbolique + charges augmentatives lourdes"** : MEDIVI Enghien (2,6k + 207k), CORTONA Loft (27 EUR + 12,5M)
2. **"Asset deal sans CS"** : LABRAX Loft (différenciation forte vs concurrents)
3. **"Storytelling humain + track record dirigeant"** : Piccolo 5 (Sylvain Goupille 25 ans finance climatique)
4. **"Membership association du débiteur"** : Piccolo 5 mentionne que La Belle Forêt est membre OBC co-présidée par Goupille - création d'un lien légitime/préemption morale
5. **"Lettre d'intention non engageante"** vs "offre ferme" : Stock CO2 (non engageante) vs Reforest'Action (ferme et définitive) — différenciation crédibilité juridique majeure

## Champs prioritaires - couverture

| Champ | 15 (Enghien) | 19 (Loft) | 24 (La Belle Forêt) |
|---|---|---|---|
| issue.cette_offre_retenue | en_attente | en_attente | en_attente |
| motifs_tribunal_verbatim | OUI (15-04) | non | non |
| profil_repreneur.forme | societe_existante | mix | mix |
| track_record_reprises | OUI fort | OUI fort | OUI fort |
| pct_reprise | 77.8% (7/9) | 0% asset deal | 0% à 75% selon offre |
| structure_prix.prix_total_eur | OUI | OUI | OUI |
| charges_augmentatives_eur | OUI fort | partiel | non |
| diagnostic_qualification | OUI | OUI | OUI |
| BP 3 ans présent | partiel | non | OUI Piccolo |
| aucune_cs | non | OUI LABRAX | non |
| agressivite | aucune | aucune | modérée |
| exec_summary | non | partiel | non |
| personnalisation | étude_contrats | étude_contrats | étude_contrats + rencontre Piccolo |

## Suggestions Phase 2

- Croiser avec **gagnants-tribunal.md** quand issue connue (DENTEKA, FHBX Balthazar, La Belle Forêt).
- Analyser le pattern "prix symbolique + L.642-12 al.4" comme stratégie radicale (CORTONA + MEDIVI) vs prix réaliste (ARCANGE, LABRAX).
- Étudier la diff offre initiale → améliorée → finale pour MEDIVI Enghien (4 versions !) : variable prix passe de [3] symbolique → 1.300 → 2.600 avec densification continue des charges augmentatives. Pattern "escalade contrôlée sous observations tribunal".
- ARCANGE et MUVICO sont les seuls candidats avec ventilation **par actif** (vs LABRAX/CORTONA qui font portefeuille global) — différence stratégique de positionnement à creuser.

## Related

- [[brantham/_MOC]]
- [[brantham/tc-paris-extraction/grilles/_workflow]]
- [[brantham/tc-paris-extraction/analyses/decortique-offres-gagnantes]]
- [[brantham/tc-paris-extraction/analyses/gagnants-tribunal]]
- [[_system/MOC-master]]
