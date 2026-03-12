---
type: reference
project: brantham
updated: 2026-03-12
component: database
---

# Database Schema Reference

PostgreSQL 16, conteneurise dans Docker (`brantham-data-postgres-1`).

## Volumetrie

| Metrique | Volume |
|---|---|
| Tables | 43+ |
| BODACC records | 1.8M |
| Procedures collectives | 184K |
| Bilans financiers | 194K |
| Dossiers complets | 84K |
| Buyer match scores | 841K |
| Backtest scoring | 165K+ lignes |

## Tables Principales

### Core

| Table | Colonnes cles | Description |
|---|---|---|
| `procedure_collective` | id, siren, type_procedure, date_jugement, tribunal, mandataire, statut | Procedures RJ/LJ/SV detectees |
| `entreprise` | siren, denomination, naf, effectif, ca_dernier, adresse, lat, lon, date_creation | Fiches entreprise enrichies |
| `bodacc_annonce` | id, type, siren, date_parution, contenu, source_url | Annonces BODACC brutes |

### Scoring & Predictions

| Table | Colonnes cles | Description |
|---|---|---|
| `score_qualification` | siren, score_total, score_taille, score_secteur, score_procedure, score_fraicheur, score_localisation, score_effectif, score_afdcc, score_mandataire, score_actifs, date_calcul | Scores de qualification (9 composantes) |
| `cox_predictions` | siren, prob_cession_3m, prob_cession_6m, prob_cession_9m, prob_cession_12m, c_index, date_prediction | Predictions de cession (Cox PH) |
| `backtest_scoring` | siren, score_date, score_value, outcome, outcome_date | Backtest historique du scoring |

### Financier

| Table | Colonnes cles | Description |
|---|---|---|
| `bilan_ratios` | siren, exercice, ca, resultat_net, ebitda, ratio_endettement, ratio_liquidite, ratio_solvabilite, bfr, tresorerie | Ratios financiers |
| `transaction_cession` | id, siren, date_cession, prix, type_cession, repreneur_siren | Historique cessions |

### Enrichissement

| Table | Colonnes cles | Description |
|---|---|---|
| `dossier_complet` | siren, denomination, secteur, ca, effectif, score, procedure, mandataire, tribunal, synthese, date_build | Dossiers enrichis complets |
| `sirene_data` | siren, denomination, naf, effectif_tranche, adresse, date_creation | Donnees SIRENE brutes |

### Matching & Intelligence

| Table | Colonnes cles | Description |
|---|---|---|
| `buyer_match_score` | target_siren, buyer_siren, match_score, match_type, sector_fit, size_fit, geo_fit | Scores matching acheteur/cible |
| `stats_mandataire` | mandataire, nb_procedures, nb_cessions, taux_cession, delai_moyen | Stats par mandataire |
| `stats_tribunal` | tribunal, nb_procedures, nb_cessions, taux_cession, secteurs_top | Stats par tribunal |

### Veille & Alertes

| Table | Colonnes cles | Description |
|---|---|---|
| `early_warning` | siren, signal_type, signal_date, severity, details | Signaux d'alerte precoce |
| `ibse_sectoriel` | naf, date, stress_index, nb_procedures, tendance | Indicateur de stress sectoriel |

## Materialized Views

| View | Description | Refresh |
|---|---|---|
| `mv_top_opportunites` | Top opportunites qualifiees (score > 60, procedure active) | Daily |
| `mv_distressed_ma` | Vue consolidee M&A distressed (dossier + score + prediction) | Daily |

## Scoring -- 9 Composantes

| Composante | Poids | Description |
|---|---|---|
| Taille | 30% | CA, effectif, actifs |
| Secteur | 25% | Attractivite du secteur NAF |
| Procedure | 20% | Type et stade de la procedure |
| Fraicheur | 5% | Anciennete de la procedure |
| Localisation | 5% | Bassin economique, accessibilite |
| Effectif | 5% | Taille de l'equipe |
| AFDCC | 5% | Score de defaillance AFDCC |
| Mandataire | 3% | Track record du mandataire |
| Actifs | 2% | Qualite et valeur des actifs |

## Index

Les index principaux sont sur: `siren`, `date_jugement`, `type_procedure`, `score_total`, `naf`, `tribunal`, `mandataire`.
