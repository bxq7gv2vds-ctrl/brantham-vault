---
type: reference
project: brantham
updated: 2026-03-12
component: scoring
---

# Scoring System Reference

Systeme de scoring pour qualifier les opportunites de cession M&A distressed. Implementation dans `scorers/qualification.py`.

## Fonction Principale

```python
compute_score(siren: str) -> QualificationScore
```

Calcule un score composite sur 100 a partir de 9 composantes ponderees.

## 9 Composantes

| # | Composante | Poids | Range | Description |
|---|---|---|---|---|
| 1 | **Taille** | 30% | 0-100 | CA, effectif, total bilan. Favorise PME 1-50M EUR |
| 2 | **Secteur** | 25% | 0-100 | Attractivite du code NAF. Industrie/agro > services |
| 3 | **Procedure** | 20% | 0-100 | Type (LJ > RJ > SV) et stade |
| 4 | **Fraicheur** | 5% | 0-100 | Jours depuis jugement. <30j = 100, >180j = 0 |
| 5 | **Localisation** | 5% | 0-100 | Bassin economique, densite industrielle |
| 6 | **Effectif** | 5% | 0-100 | Taille equipe. 10-100 salaries optimal |
| 7 | **AFDCC** | 5% | 0-100 | Score de defaillance AFDCC (si disponible) |
| 8 | **Mandataire** | 3% | 0-100 | Track record du mandataire (taux cession, volume) |
| 9 | **Actifs** | 2% | 0-100 | Qualite et valeur des actifs identifies |

## Score Total

```
score_total = sum(composante_i * poids_i for i in 1..9)
```

Range: 0-100.

## Seuils de Decision

| Score | Action | Description |
|---|---|---|
| **75+** | URGENT | Lancement immediat du pipeline complet (Analyst + Writer + Hunter) |
| **60-74** | LAUNCH | Lancement pipeline standard |
| **50-59** | WATCH | Surveillance, pas de lancement auto |
| **<50** | ARCHIVE | Archivage, pas d'action |

## Estimation Valeur d'Entreprise (VE)

Le scoring inclut une estimation de la VE:

| Metrique | Description |
|---|---|
| `ve_min` | Estimation basse (liquidatif) |
| `ve_median` | Estimation mediane (comparables) |
| `ve_max` | Estimation haute (going concern) |

Methodes: multiples sectoriels, actifs nets, DCF simplifie (si bilans disponibles).

## Cox Proportional Hazards -- Predictions de Cession

Modele de survie pour predire la probabilite de cession dans le temps.

| Metrique | Description |
|---|---|
| `prob_cession_3m` | Probabilite de cession a 3 mois |
| `prob_cession_6m` | Probabilite de cession a 6 mois |
| `prob_cession_9m` | Probabilite de cession a 9 mois |
| `prob_cession_12m` | Probabilite de cession a 12 mois |
| **C-index** | **0.84** (discrimination excellente) |

Variables du modele Cox: type_procedure, ca, effectif, secteur, age_entreprise, localisation, mandataire_track_record.

## Backtest

- 165K+ lignes dans `backtest_scoring`
- Comparaison score a date T vs outcome reel (cession oui/non, delai)
- Permet d'ajuster les poids et seuils

## Pipeline Integration

```
BODACC → Ingest → SIRENE Enrichment → compute_score()
                                            |
                                     score >= 60 → Launch Agent Pipeline
                                     score >= 75 → URGENT flag
                                     score < 50  → Archive
```

## Related
- [[brantham/_MOC]]
