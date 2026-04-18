---
name: Overnight Model Upgrades — 2026-04-18
description: Session nocturne — fix OPEN_METEO, BMA training réel, XGBoost bootstrap + wire, backfill historique, reconcile paper shadow autonome, bug CONFIRMED_YES identifié et corrigé
type: session
date: 2026-04-18
tags: [polymarket, session, model-upgrade, bma, xgboost, reconcile]
---

# Session — 2026-04-18 Overnight Model Upgrades

Paul est allé dormir en disant « upgrade le modèle, sois ultra minutieux ». Huit commits plus tard, le pipeline est passé de « infra posée, pas entraînée » à « infra entraînée, validée par paper shadow, premier bug de logique détecté et corrigé ».

## TL;DR

- **8 commits** sur main, tous testés avant commit.
- **Paper shadow vient de produire ses premiers 199 outcomes** : WR 84.4 %, P&L +$882.
- **Bug CONFIRMED_YES détecté par le feedback loop** (WR 0 % sur 10 signaux) et fixé.
- **XGBoost post-proc** passe de **2 régions (CN + JP_KR)** à **10 régions** trained.
- **BMA training** passe de 440 samples/5 sources à 17 974 samples/8 sources.
- **3 nouveaux launchd jobs** : BMA daily, XGB weekly, reconcile-obs daily.
- `use_xgb_post=False` par défaut — zero regression risk tant que Paul n'active pas le flag.

## Commits (ordre chronologique)

1. `350eb2b` **fix OPEN_METEO freshness monitor** — le tag mismatch DOWN-depuis-toujours
2. `69cd582` **feat BMA training** (`scripts/train_bma.py`) + cron daily 09:30
3. `678b961` **feat XGBoost bootstrap depuis mega_dataset** + cron weekly + models CN/JP_KR
4. `4d20956` **fix write-through cache** dans `forecast()`
5. `52c2c36` **feat wire XGBoost residual** avec flag `use_xgb_post`
6. `ab44442` **feat backfill Open-Meteo** historique (obs 100 k + forecasts 18 k + 10 régions trained)
7. `5b51a59` **feat reconcile_from_obs** — signal_outcomes enfin populé
8. `1822e6c` **fix CONFIRMED prev_day fallback** (bug détecté par le reconcile)
9. `23cbb5c` ops launchd reconcile-obs cron 09:20

## Par tâche

### 1. Fix OPEN_METEO freshness (commit 350eb2b)

**Problème** : `data_freshness` table montrait `OPEN_METEO_ENS` et `OPEN_METEO_DET` DOWN depuis l'epoch 1970, alors que 45 k+ rows OPEN_METEO étaient ingérées fraîchement chaque jour.

**Root cause** : dans `scripts/ingest_nwp_daily.py`, le freshness monitor comptait les rows avec `source IN ('OPEN_METEO_ENS', 'OPEN_METEO_DET')`. Mais `nwp_sources._model_tag()` tag les rows avec le nom du modèle sous-jacent (`GEFS_ENS`, `ICON_ENS`, `GEFS`, `ICON`, `AIFS`, etc.). → 0 match → DOWN.

**Fix** : bucket les tags DB par source logique sans toucher au schéma d'ingestion (BMA a besoin des tags par modèle pour pondérer).

```python
source_groups = {
    "OPEN_METEO_ENS": ("GEFS_ENS", "ICON_ENS", "GEM_ENS", "ECMWF_ENS"),
    "OPEN_METEO_DET": ("GEFS", "ICON", "ECMWF", "GEM", "AIFS"),
    "HRRR":           ("HRRR",),
    "ICON_EU":        ("ICON_EU",),
}
```

**Vérification** : OPEN_METEO_ENS montre 11 523 rows/1 h, OPEN_METEO_DET 522/1 h, tous OK.

### 2. BMA training réel (commit 69cd582)

**Problème** : `src/pmhedge/alpha/bma.py` avait toutes les primitives (EWMA updater, Gaussian mixture combine, per-station load) **mais aucun script de training**. Chaque station fallback sur `DEFAULT_WEIGHTS_GLOBAL` statique → BMA = passthrough.

**Fix** : `scripts/train_bma.py` qui joint `nwp_forecasts` × `obs_temperature` sur (icao, UTC target_date), moyenne les ensemble members par (source, icao, date), puis compute `weights ∝ 1 / max(0.5, MAE)` per station + global.

**Gotcha résolu** : `emos_cache.db` avait un schéma legacy `bma_weights` (city, season, colonnes par source). Renommé `bma_weights_legacy` pour préserver les 192 rows historiques, puis la nouvelle table (station, source, long format) se crée automatiquement.

**Résultat initial** (30 jours, min-n=2) :
- 47 stations + GLOBAL
- 440 samples
- GLOBAL : ICON 21.8 %, ICON_ENS 21.6 %, GEFS_ENS 21.3 %, GEFS 20.5 %, AIFS 14.8 %
- Per-station best source varie par région (ICON Europe/China, GEFS SE Asia/tropics)

**Launchd** : `com.paul.polymarket-alpha-bma-train` quotidien 09:30.

### 3. XGBoost post-proc bootstrap (commit 678b961)

**Problème** : `scripts/train_xgboost_post.py` nécessitait ERA5 (compte Copernicus user bloqué) ou 30+ jours de METAR (archive seulement 3 jours).

**Fix** : **importer `mega_dataset.db`** — déjà sur disque avec ~1 an d'obs + forecasts pour 6 villes asiatiques.

- `scripts/import_mega_to_alpha_hub.py` map city → ICAO (beijing→ZBAA, chengdu→ZUUU, …), convertit `wu_daily` → `obs_temperature` (source='WU_HISTORICAL'), et `nwp_forecasts` → `nwp_ensemble_blend` agrégeant mean/std/p05..p95 sur les 4 modèles.
- Rendement : 2 288 obs + 8 640 forecasts + 2 160 blends.
- `assemble_training_data` traite WU_HISTORICAL/ERA5 comme pré-agrégés (pas de filter intra-day).
- `build_features` coerce lat/lon/elevation en numeric (legacy bug : `stations.elevation_m` contient le country code pour plein de stations).

**Résultat** :
- CN : 1 441 samples, RMSE val 1.31 °C
- JP_KR : 721 samples, RMSE val 1.41 °C

**Launchd** : `com.paul.polymarket-alpha-xgb-retrain` weekly, dimanche 04:00.

### 4. Write-through cache (commit 4d20956)

Petit fix : `forecast()` lisait le cache mais ne l'écrivait pas en cache miss → get_or_compute écrivait, forecast() direct payait ~6 ms à chaque fois. Now write-through après compute.

**Bench ZBAA** : cold 6.3 ms → first-cache 0.8 ms → hits 0.4 ms (15× speedup).

### 5. Wire XGBoost (commit 52c2c36)

**Pipeline** :
```
NWP → EMOS per source → BMA combine → (μ, σ)
     → if use_xgb_post: μ += xgb.predict(features)
     → ProbabilityForecast
```

`_apply_xgb_correction()` :
- Map icao → city → region via `risk_manager._city_region`
- Load model lazy-cached (`_XGB_MODEL_CACHE: dict[region → model|None]`)
- Build features (ens_mean, std, spread, skew, lags, temporal sin/cos, geo)
- `pf.mu_c += residual` — sigma **non touchée** pour v1 (plus safe)
- Feature flag `use_xgb_post=False` par défaut — **aucune regression**
- Propagé dans `get_or_compute` et `precompute_all`

**Deltas mesurés** (2026-04-20/21) :
- ZSPD (CN) : +2.13 °C
- ZBAA (CN) : −0.20 °C
- RJTT (JP_KR) : +0.49 °C
- KDEN (US_WEST avant backfill) : +0.00 °C, correctly skipped

### 6. Backfill historique Open-Meteo (commit ab44442)

Deux outils indépendants pour débloquer le training sans ERA5 :

**`scripts/backfill_obs_archive.py`** : Open-Meteo Archive API (ERA5-based, pas de clé, ~10 k req/jour limite). 46 stations × 90 jours → **100 464 rows en 0.8 s**. Source='ARCHIVE'.

**`scripts/backfill_nwp_history.py`** : Open-Meteo Historical-Forecast API, 5 models (GFS/ICON/ICON-EU/ECMWF/JMA). 46 stations × 90 jours → **17 927 nwp_forecasts + 4 186 blends en 3.7 s**. run_ts pinné à midnight UTC pour idempotence.

**Impact aval** :

XGBoost (avec `--obs-source ARCHIVE`) :
| Region | Samples | RMSE val |
|---|---|---|
| CN | 673 | 1.12 °C |
| EU_CENTRAL | 289 | 0.71 °C |
| EU_EAST | 290 | 0.95 °C |
| EU_WEST | 483 | 0.87 °C |
| IN_ME | 287 | 1.03 °C |
| JP_KR | 287 | 2.21 °C (overfitting visible) |
| LATAM | 288 | 1.09 °C |
| **TW_SEA** | 384 | **0.61 °C** (best) |
| US_EAST | 772 | 1.34 °C |
| US_WEST | 479 | 0.74 °C |

Skipped : CA (96 samples), OCEANIA (96 samples) — ≥1-2 stations seulement.

BMA : 440 → 17 974 samples, 5 → 8 sources. GLOBAL weights dominés maintenant par **ICON_EU (19.4 %, MAE 0.67 °C)** et **ECMWF (18.3 %, MAE 0.71 °C)**.

**Caveat** : ARCHIVE obs sont ERA5 reanalysis → possiblement biaisés bas vs METAR réel. Quand l'archive METAR rolling aura ≥30 jours (dans ~4 semaines), il faudra ré-entraîner avec METAR comme vérité.

### 7. Reconcile autonome (commit 5b51a59)

**Problème** : `signal_outcomes` vide malgré 1 176 signaux émis. `reconcile_and_report.py` joint `signal_log.market_id` contre `pmhedge.db:market_resolutions` (1 886 rows, mais pour 2026-04-06 et avant — 0 overlap avec markets actifs).

**Fix** : `scripts/reconcile_from_obs.py` auto-suffisant. Pour chaque signal > min_age_hours :
- Lit (icao, target_date, bracket_lo_c, bracket_hi_c) depuis metadata (MODEL_VS_MARKET)
- Parse `∈ [lo, hi]` / `∉ [lo, hi]` depuis `reason` pour CONFIRMED (avant patch)
- Get `MAX(temp_c) FROM obs_temperature WHERE icao=? AND date(obs_ts)=target_date`
- Compute won + paper P&L + insert signal_outcomes

**Premier run réel** (min-age-hours=12) :
| Alpha | N | Won | WR | P&L |
|---|---|---|---|---|
| MODEL_VS_MARKET | 179 | 158 | **88.3 %** | +$998.56 |
| CONFIRMED_NO | 10 | 10 | 100 % | +$20.70 |
| **CONFIRMED_YES** | **10** | **0** | **0 %** ⚠️ | **−$136.84** |

### 8. Fix CONFIRMED_YES bug détecté par le reconcile (commit 1822e6c)

Le paper shadow vient littéralement d'attraper un bug que le backtest n'aurait jamais trouvé.

**Root cause** : dans `confirmed_oracle._get_tmax_for_market`, quand `t_max_per_utc_day(icao, target_date)` retourne None (target_date UTC n'est pas encore complète dans METAR), le code fallback sur `prev_day = target_date - 1`. Pour un signal émis le 2026-04-18 02:04 UTC pour un market « April 18 », il lisait T_max du 2026-04-17 → signal basé sur T_max d'hier, pas sur celui du target.

**Biais asymétrique** :
- CONFIRMED_YES : "yesterday's peak ∈ today's 1° bin" → faux presque toujours → YES perd.
- CONFIRMED_NO : "yesterday's peak ∉ today's 1° bin" → vrai presque toujours par chance → NO gagne sur du mauvais raisonnement.

Les deux mentent sur leur « certitude ».

**Fix** : prev_day fallback **seulement si target_date UTC < today UTC**. Sinon "target_date UTC not yet complete", pas de signal.

**Bonus** : ajouté `bracket_lo_c` / `bracket_hi_c` dans metadata CONFIRMED (plus de regex sur reason).

**Vérification manuelle KMIA** :
- Today UTC → `labeled_date=2026-04-18` (avec ARCHIVE backfill, on a maintenant des obs)
- Ancient → None
- Yesterday → `labeled_date=2026-04-17`

### 9. Launchd reconcile-obs (commit 23cbb5c)

Cron quotidien 09:20, entre `alpha-reconcile` (09:15, legacy path) et `alpha-bma-train` (09:30). Log dans `logs/alpha-reconcile-obs.log`.

## État du système au coucher (2026-04-18 ~15:00)

### Launchd actifs (9 jobs)

| Job | Cadence |
|---|---|
| alpha-live-runner | KeepAlive 300 s |
| alpha-nwp-ingest | 4×/jour |
| alpha-metar-archive | every 2 h |
| alpha-health-check | every 15 min |
| alpha-reconcile | daily 09:15 (legacy) |
| alpha-reconcile-obs | daily 09:20 **(NEW)** |
| alpha-bma-train | daily 09:30 **(NEW)** |
| alpha-precompute | 4×/jour |
| alpha-xgb-retrain | weekly Sunday 04:00 **(NEW)** |

### Fraîcheur data (data_freshness)

| Source | Status | Last success |
|---|---|---|
| OPEN_METEO_ENS | **OK** | 2026-04-18 14:50 (était DOWN) |
| OPEN_METEO_DET | **OK** | 2026-04-18 14:50 (était DOWN) |
| HRRR | OK | 2026-04-18 14:50 |
| ICON_EU | OK | 2026-04-18 14:50 |
| METAR | OK | 2026-04-18 04:49 |

### Données en DB

- `nwp_forecasts` : **63 555 rows** (45 k live + 18 k historical + 8 k imported mega_dataset)
- `nwp_ensemble_blend` : **6 346 blends** (500 recent + 4 186 historical + 2 160 imported)
- `obs_temperature` : **104 732 rows** (100 k ARCHIVE + 2 k METAR + 2 k WU_HISTORICAL)
- `signal_log` : 1 176 signaux
- `signal_outcomes` : **199 settled** (premier batch du paper shadow)
- `forecast_cache` : 230 entries
- `bma_weights` : 190 rows (47 stations × sources + GLOBAL)
- `bma_weights_legacy` : 192 rows préservées

### Models on disk

`models/xgb_postproc_{region}.json` pour 10 régions (CN, EU_CENTRAL, EU_EAST, EU_WEST, IN_ME, JP_KR, LATAM, TW_SEA, US_EAST, US_WEST).

## Prochaines étapes recommandées

### Immédiat (5-15 min)
1. **Re-run reconcile avec min-age=30 h demain** — les 30 jours accumulés donneront une baseline drift-free.
2. **Activer le flag `use_xgb_post=True`** dans `run_alpha_live.py` pour un A/B de 7 jours — déjà prêt côté code.

### Court terme (1-3 sessions)
3. **Sum_arb fix** (tâche #8 pending) — prix pas synchronisés, backtest gonflé.
4. **Orderbook imbalance alpha** (tâche #9 pending) — bloqué tant que le WS daemon ne tourne pas (py-clob-client pas installé).
5. **CONFIRMED oracle : étendre à labeled_date once target_date UTC had 12+ obs** (plus robuste que "past day").

### Moyen terme
6. Wire `use_xgb_post=True` en prod après A/B validé.
7. Training XGBoost réel sur ERA5 dès que compte Copernicus disponible (≫ ARCHIVE quality).
8. **DRN / Transformer** training avec le nouveau dataset 100 k obs (pas besoin d'ERA5 pour baseline si ARCHIVE).

## Related

- [[_MOC]]
- [[STATE-HANDOFF]]
- [[TODO-pending]]
- [[findings|Findings diagnostic]]
- [[decisions|Décisions archi]]
- [[../../_system/MOC-patterns|Patterns]]
- [[../../_system/MOC-bugs|Bugs]]
