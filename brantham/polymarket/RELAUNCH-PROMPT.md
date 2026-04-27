---
name: Relaunch Prompt — Polymarket session
description: Prompt à coller après /clear pour reprendre la session Polymarket sans perte de contexte
type: prompt
updated: 2026-04-20
---

# Prompt de relance après /clear

Copier-coller exactement ce qui suit après `/clear` :

---

Projet **Polymarket Hedge Fund** — `/Users/paul/polymarket-hedge/`. On attaque le modèle weather trading.

Lire en premier dans cet ordre (OBLIGATOIRE avant toute action) :

1. `vault/brantham/polymarket/STATE-HANDOFF.md` — état complet du système
2. `vault/brantham/polymarket/sessions/2026-04-20-feature-engineering-burst.md` — dernière session
3. `vault/brantham/polymarket/audit-hedge-fund-grade.md` — gap analysis 10 dimensions

**TL;DR** : 35 launchd jobs actifs. Pipeline alpha avec 12 sources NWP (dont GraphCast + AIFS + NBM + UKMO + CMA), 37 features engineered (climato + lags + UHI + diurnal + synoptic ENSO/NAO + soil moisture), 46 per-station XGB, 11 per-city calibrators, 4 regime HMM, tail filter critique, calibration per-city post-ablation.

**Score** : 82/100 hedge fund grade générique, 30/100 vs énorme hedge fund (gap = data privée + real money + équipe).

## Sanity checks à faire en reprise

```bash
cd /Users/paul/polymarket-hedge

# 1. Launchd (attendre 35)
launchctl list | grep polymarket-alpha | wc -l

# 2. Validator 8/8
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/validate_strategy.py --skip-pytest

# 3. Freshness
sqlite3 alpha_data_hub.db "SELECT source, status, datetime(last_success,'unixepoch','localtime') FROM data_freshness;"

# 4. Circuit breaker
sqlite3 alpha_data_hub.db "SELECT alpha_type, status, reason FROM alpha_states;"

# 5. Live scan test
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/run_alpha_live.py --once --no-telegram --min-edge 0.05 --bankroll 1000
```

## Priorité immédiate

**Pangu-Weather ONNX** : user doit drop le fichier à `/Users/paul/polymarket-hedge/models/pangu_24h.onnx`.

Scaffold déjà en place : `src/pmhedge/alpha/pangu_forecaster.py`.

Une fois le fichier dropé :
1. `pmhedge.alpha.pangu_forecaster.available()` retourne True
2. Wire dans `nwp_sources.RegionalFetcher.build()` (5 min)
3. Backfill 365 jours via `backfill_nwp_history.py --models pangu_24h`
4. Retrain BMA pour absorber weights Pangu
5. Re-run ablation pour mesurer +15-20% CRPS attendu

## Ce qui attend ensuite (si Pangu pas encore fourni)

Par ROI décroissant :
1. **Aurora Microsoft ONNX** (HuggingFace microsoft/aurora, 1 jour integration)
2. **Transformer temporel MPS fit** sur 1 an (5-10h)
3. **CI/CD GitHub Actions** pytest + ruff (3h)
4. **Docker compose full stack** pour deploy portable (4h)
5. **Per-city layer config** (stocker best ablation per ville dans city_config)
6. **Refine tail filter** (NYC climato_std trop large donc tail bets NYC pas filtrés)

## Bloqué user (rappeler si besoin)

1. **Pangu ONNX file** (promis cette session)
2. **ERA5 Copernicus** account + `~/.cdsapirc` — débloque DRN SOTA
3. **Polymarket wallet** funded + `POLY_PRIVATE_KEY` + `uv add py-clob-client`
4. **Avocat crypto FR** before $10k real

## Ne PAS refaire

- Ablation (déjà 3 fois) sauf si nouveau model
- Backfill NWP/obs historical (déjà 365j coverage)
- Training BMA/EMOS/XGB station (déjà à jour)
- Wiring des features (déjà dans enrich_features)
- Diagnostic Tokyo/Chicago (déjà identifié : tail filter + per-city calibrator)

## Rappels

- Toujours `KMP_DUPLICATE_LIB_OK=TRUE` avant scripts avec XGBoost + torch (libomp conflict)
- `use_calibration=True` par défaut (post-ablation validated +23%)
- `use_quantile=False` par défaut (ablation shows it hurts Brier 24%)
- `use_volatility_filter=True` par défaut
- `use_tail_filter=True` par défaut
- `use_regime_hmm=True` par défaut
- DRN weight hardcoded 0 tant que pas ERA5

## Commandes pratiques à retenir

```bash
# Retrain tout après nouvelle feature/data
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/train_emos_per_station.py && \
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/train_bma.py --days 365 && \
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/train_xgb_per_station.py && \
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/train_calibrators.py && \
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/train_city_calibrators.py && \
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/train_regime_hmm.py && \
uv run scripts/audit_per_city.py --apply --quiet

# Ablation global
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/ablation_study.py --max-rows 400

# MLflow UI
uv run mlflow ui --backend-store-uri file:/Users/paul/polymarket-hedge/models/mlflow --port 5000
```

---

**Langue** : français conversation, anglais code. Pas d'emojis, pas de violet, design sobre.

**Autonomie** : procéder sans demander confirmation sauf git push / delete / deploy prod / destructif.

**Style** : réponses courtes, directes, pas de blabla. Tester avant de dire "fait".
## Related
