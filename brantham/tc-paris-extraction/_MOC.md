---
type: moc
project: brantham
created: 2026-05-15
tags: [tc-paris, distressed, m&a, deal-intel, dataset]
---

# TC Paris — Extraction Greffe (Dataset)

Extraction structurée des offres de reprise déposées au Greffe du Tribunal de commerce de Paris. **94 dossiers** d'entreprises en procédure collective (RJ/LJ/sauvegarde/plan de cession), **545 lignes d'offres** extraites depuis ~300 PDFs.

## Source
- **Folder source** : `/Users/paul/Downloads/Dossiers Entreprises/` (94 sous-dossiers, PDFs + CSVs)
- **Prompt d'extraction** : `Dossiers Entreprises/34 - SAS COSA/PROMPT_EXTRACTION_OFFRES.md`
- **Période** : dossiers 2025-2026, DLDO majoritairement T4 2025 / T1-T2 2026

## Fichiers maîtres

| Fichier | Description | Lignes |
|---|---|---|
| `master-offres.csv` | Toutes les offres consolidées | 545 |
| `master-dossiers.csv` | Métadonnées des sociétés débitrices | 97 |
| `raw-csv/` | Archive des CSV individuels par dossier | 188 |
| `_merge.py` | Script de consolidation (rejouable) | — |

### Schéma `master-offres.csv` (30 colonnes)
`dossier_folder, offre_id, dossier_id, fichier_source, nom_repreneur, forme_juridique_repreneur, capital_repreneur, rcs_repreneur, adresse_repreneur, dirigeant_repreneur, groupe_appartenance, type_offre, date_offre, societe_cessionnaire, prix_total_eur, prix_incorporels_eur, prix_corporels_eur, emplois_repris, perimetre_actifs, exclusions, conditions_suspensives, mode_financement, ca_repreneur_eur, resultat_exploitation_repreneur_eur, resultat_net_repreneur_eur, total_actif_eur, capitaux_propres_eur, validite_offre, avocat_repreneur, notes`

### Schéma `master-dossiers.csv` (24 colonnes)
`dossier_folder, dossier_id, nom_societe, forme_juridique, capital_social_eur, rcs, adresse_siege, nom_commercial, activite, type_procedure, date_ouverture, tribunal, administrateur_judiciaire, cabinet_aj, adresse_aj, mandataire_judiciaire, cabinet_mj, juge_commissaire, dldo, effectif_total, nb_offres_recues, filiales, secteur, notes`

## Analyses

- [[analyses/repreneurs-recurrents]] — Top repreneurs actifs (foncières, consolidateurs, fonds)
- [[analyses/groupes-distressed]] — Groupes en difficulté multi-entités (INNATIS, NEOCAMP, DENTEKA, SYM, COLLEGE DE PARIS)
- [[analyses/data-quality]] — Anomalies, doublons, OCR à refaire, scans illisibles

## Stats clés

- **94 dossiers** analysés (numérotation 01-66, certains numéros avec plusieurs entreprises)
- **545 offres** extraites au total
- **268 offres** avec prix numérique parsable
- **Médiane prix** : 100 000 €
- **Max prix** : 25,2 M€ (Barings Real Estate sur SEGI immobilier)
- **Procédures** : ~75% RJ, reste = sauvegarde/LJ/plan de cession/prepack

## Clusters notables

### Immobilier parisien (35 dossiers — extraction d'origine)
SCI/SNC en RJ avec repreneurs récurrents : **MUVICO** (26 dossiers), **HOUSEBASE** (16), **VERDOSO** (29 lignes), **LABRAX INVEST** (17), **AEB INVEST** (9), **WS HOLDING** (4), **Groupe JADO** (15), **Groupe LALEYE** (4).

### Pôle Val de Loire INNATIS (arboriculture)
11 SCEA/SCA liées, offres indivisibles : `34-LPC`, `35-SICA`, `36-LVL`, `37-COOP`, `57-PLESSE`, `58-LAUNAY`, `59-REINETTE`, `60-DENIOLAY`, `61-BEAUVALLO`, `62-CHAUSSEE`, `66-VAULEARD`. Consortium **CASTEL INVEST + LEROY FRERES + VCAPITAL** (10 offres) vs **SARL CELHER local** (12 offres) vs **LES VERGERS D'ANJOU** (6 offres). Total INNATIS supporté ~6,49 M€.

### Groupe NEOCAMP (hôtellerie de plein air)
8 sociétés liées : `25-ILO`, `26-CHA`, `27-GRANDE-LISSE`, `28-ALPHA`, `29-ESCAPADE`, `30-LORMED`, `31-OCCITANIE`. Repreneurs en concurrence : **FEMINA STYL+MARENGO** (6 offres, ticket max 2 M€), **HOMAIR/ECG**, **HUTTOPIA**, **CAMPALDIA/SLBC PERON** (offres symboliques), **SEASONOVA**, **PLANETE MOBIL HOMES**.

### Réseau DENTEKA (centres dentaires)
3 dossiers : `11-CLAYE`, `14-COLMAR`, `15-ENGHIEN`. Repreneur unique **MEDIVI** (Place Dentaire, Haddouk frères, 9 offres successives).

### Groupe SYM (optique mobile)
3 dossiers : `20-SYM-TECH`, `21-SYM-OPTIC`, `22-SYM-LAB`. Repreneur unique **LOM (Les Opticiens Mobiles)** sur les 3 entités (offre globale 50 k€).

### SEGI (immobilier suisse Paris)
Dossier `03-SEGI` — 19 offres entre 10 M€ et 25,2 M€ : **Barings**, **Eternam**, **JCDecaux Holding**, **EMERIGE**, **PMV1/Compagnie Lebon**, **Trustone REIM**, **Roger Zannier**, **Albin Michel**, etc.

### COLLEGE DE PARIS (EdTech, 49 filiales)
Dossier `45` — 26 offres complexes, 1390 collaborateurs, repreneurs : **UPSTAIRS+Vox Populi**, **GALILEO**, **EUREKA EDUCATION**, **VERDOSO**, **REWORLD MEDIA**, **DELLEN/COMUNDI**, **CONSTELLATIS/GERESO** (2,5 M€), **IGS**, **NOVETUDE**, **SAMARKAND**.

## Workflow de re-extraction

```bash
cd /Users/paul/vault/brantham/tc-paris-extraction
python3 _merge.py  # rejouer la consolidation après mise à jour des CSV sources
```

## Related

- [[brantham/_MOC]]
- [[brantham/context/realite-business]]
- [[brantham/context/process-end-to-end]]
- [[_system/MOC-master]]
