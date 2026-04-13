---
type: reference
project: brantham
updated: 2026-03-12
component: data-pipeline
---

# Data Pipeline -- Map of Content

Pipeline de collecte, enrichissement et scoring des opportunites M&A distressed. Orchestre par Prefect depuis `orchestration/daily.py`.

## Daily Pipeline (9 etapes)

Execute tous les jours a 07h00 via launchd (`com.brantham.daily.plist`).

| Step | Nom | Description |
|---|---|---|
| 0 | `setup_schema` | Verification/migration schema PostgreSQL |
| 1 | `bodacc_collectors` | Collecte BODACC (procedures collectives, ventes, radiations) |
| 2 | `ingest` | Ingestion et deduplication des nouvelles annonces |
| 3 | `sirene_enrichment` | Enrichissement SIRENE (denomination, NAF, effectif, CA) |
| 4 | `geocoding` | Geocodage des adresses entreprises |
| 5 | `scoring` | Calcul des scores de qualification (9 composantes) |
| 6 | `bilan_ratios` | Calcul des ratios financiers depuis bilans INPI |
| 7 | `dossier_complet` | Construction des dossiers enrichis complets |
| 8 | `refresh_views` | Rafraichissement des materialized views |
| 9 | `stats_and_predictions` | Stats mandataires/tribunaux + Cox PH predictions + backtest + early warning + buyer match + IBSE + cleanup |

## Weekly Pipeline

Execute chaque dimanche.

- Matrices de correlation sectorielles
- Full refresh des materialized views
- Analyse de saisonnalite
- Analyses annuelles (tendances, volumes)
- Buyer match re-run (recalcul complet)

## Monthly Pipeline

Execute le 1er de chaque mois.

- IBSE sectoriel (indicateur de stress par secteur)
- Sector stress index update

## Key Scripts

| Script | Chemin relatif | Role |
|---|---|---|
| `orchestration/daily.py` | Pipeline principal Prefect |
| `collectors/bodacc.py` | Collecteur BODACC |
| `enrichment/sirene.py` | Enrichissement SIRENE |
| `enrichment/geocoding.py` | Geocodage adresses |
| `scorers/qualification.py` | Moteur de scoring (9 composantes) |
| `scorers/cox_model.py` | Modele Cox PH (predictions de cession) |
| `scorers/backtest.py` | Backtest du scoring (165K+ lignes) |
| `enrichment/bilan_ratios.py` | Calcul ratios financiers |
| `enrichment/dossier_complet.py` | Construction dossiers |
| `matching/buyer_match.py` | Matching acheteur/cible |

Tous les scripts sont dans `/Users/paul/Desktop/brantham-partners/`.

## Cron Configuration

```xml
<!-- com.brantham.daily.plist -->
<!-- Launchd, execute a 07:00 chaque jour -->
```

## Links

- [[brantham/data-pipeline/schema]] -- Schema database complet
- [[brantham/data-pipeline/scoring]] -- Systeme de scoring detaille
- [[brantham/architecture]] -- Architecture globale
## Related
## Related
