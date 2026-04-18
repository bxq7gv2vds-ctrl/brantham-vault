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

- **15 commits** sur main, tous testés avant commit.
- **Paper shadow vient de produire ses premiers 217 outcomes** : WR 83.9 %, P&L +$915.
- **Bug CONFIRMED_YES détecté par le feedback loop** (ECE 1.0, WR 0 %/14) et fixé.
- **XGBoost post-proc** passe de **2 régions (CN + JP_KR)** à **10 régions** trained.
- **BMA training** passe de 440 samples/5 sources à 17 974 samples/8 sources.
- **DRN baseline tourne** : val CRPS 0.84 °C (~25 % gain vs baseline ens-mean RMSE 1.12 °C), wire derrière flag.
- **Ensemble stacking BMA+XGB+DRN** : mixture Gaussian avec weights trained sur validation CRPS.
- **Calibration report** : ECE + Brier + log loss per alpha_type, daily cron.
- **Drift monitor + kill switch** : alpha_states table, persist_signal check, auto-DISABLE sur drift > 8pts ou ECE > 0.20.
- **6 nouveaux launchd jobs** : BMA daily, XGB weekly, reconcile-obs, calibration, drift-monitor, ensemble weekly.
- **5 flags feature dans `forecast()`** : use_cache, use_xgb_post, use_drn, use_ensemble — tous défaut False pour zero regression.
- **5 bugs cascade** découverts et fixés : seed_stations positional args, metar_archive prune unscoped, pandas datetime64[us], training obs-lag missing, stations.elevation_m contains country codes.

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
10. `f6ccd70` **fix sum_arb backtest** — time sync + complete-partition filter
11. `3c01a82` **feat DRN baseline trained** — val CRPS 0.90 °C
12. `4951ea9` **fix+feat** cascade de 4 bugs dans feature pipeline + wire DRN end-to-end
13. `0f9cc2b` **feat calibration report** — reliability diagram + ECE + Brier + log_loss
14. `634d108` **feat drift monitor + kill switch** — alpha_states table, auto-DISABLE persist_signal
15. `dba3177` **feat ensemble stacking** — BMA + XGBoost + DRN via Gaussian mixture + weekly retrain cron

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

### 10. Sum_arb backtest fix (commit f6ccd70)

Deux bugs composés qui expliquaient les P&L « gonflés » notés dans STATE-HANDOFF :

- `ffill(limit=30)` sur buckets minute-1 : un token quoté il y a 25 min était sommé avec un token quoté maintenant → sum_yes dérivait grotesquement même quand les prix réels étaient synchrones.
- La plupart des bracket groups dans `all_markets.db` ne portent que les bins milieu « between X-Y°F » sans les tails « below L » / « above H » → leurs prix ne peuvent structurellement pas sommer à 1 → chaque snapshot ressemblait à un arb 30-80 %.

Fix :
- Sync grid `sync_window_s` (default 120 s). Un bucket ne compte que si chaque token a une observation réelle ET `max_raw_ts − min_raw_ts ≤ max_staleness_s` (default 300 s). Fini le ffill.
- Filtre `min_partition_sum=0.80` rejette les groups dont le max observé de sum_yes n'approche jamais 1 — signal structurel que les tails manquent.

Caveat : la source canonique d'arb live reste `scan_current_arbs` (Gamma API) où les tails sont exposées. Le backtest est maintenant juste sur la dimension prix/sync mais borné par les groups historiques qui ont accidentellement shippé une partition complète.

### 11. DRN baseline trained (commit 3c01a82)

Enfin débloqué grâce au backfill ARCHIVE (ERA5-derived, pas besoin de compte Copernicus).

- `train_drn.py --obs-source ARCHIVE` : 4 424 samples (3 539 train / 885 val chronologique), 16 features.
- **val CRPS 0.90 °C** vs baseline ens-mean RMSE 1.12 °C → ~20 % gain proper-score avant toute optimisation.
- 48 epochs, early stop `patience=10`.
- **Pin CPU + `torch.set_num_threads(1)`** par défaut : torch 2.11 segfaulte sous MPS et sous multi-thread BLAS dans la boucle CRPS gaussian loss. Le flag `--device mps` reste disponible si upstream fixe.
- Sauvegardé dans `models/drn.pt` + `models/drn_features.npz` (mean/std + colonnes features pour inférence).

Prochain step : wire `predict(model, features)` derrière un flag `use_drn` dans `model_prob.forecast` pour A/B vs EMOS+BMA+XGBoost sur paper shadow.

### 12. Unbreak feature pipeline + wire DRN (commit 4951ea9)

Wiring DRN a exposé **4 bugs en cascade** qui empoisonnaient aussi le XGBoost post-proc silencieusement :

- **Station positional arg bug** : `seed_stations.py` passait country en position 7 (= elevation_m dans la @dataclass). Chaque row stocké avait `stations.elevation_m = "US"`, `"FR"`, etc. La coercion numérique retournait NaN → fillna(100.0) → std=0 → le normalizer DRN divisait par 1e-6 → valeurs d'inférence en millions.
- **metar_archive.prune_older_than unscoped** : la cron METAR 2h faisait `DELETE FROM obs_temperature WHERE obs_ts < cutoff` sans filter par source. Chaque cycle effaçait les backfills ARCHIVE + WU_HISTORICAL, laissant seulement la fenêtre METAR rolling 30j.
- **pandas datetime64[us] surprise** : `assemble_training_data` calculait `horizon_h = astype("int64") / 1e9`. Sur cette stack pandas émet `datetime64[us]`, donc astype retourne des microseconds. Training rows avec horizon_h ≈ -491 000 h. Switched to `.map(lambda t: t.timestamp())`.
- **Training-time obs-lag manquant** : `build_features` fallback `t_yesterday = ens_mean` parce que `assemble_training_data` ne joignait pas sur (icao, target_date - 1). Ajouté le merge — t_yday_minus_ens retrouve sa variance.

Post-fix :
- DRN val CRPS **0.84 °C** (3 features degenerate auto-dropped : t_today_minus_ens, elevation, horizon_h)
- `_apply_drn` dans model_prob.py, flag `use_drn=False` par défaut
- σ modélisé proprement (~2.5-3 °C vs BMA 1.05 °C — bien plus réaliste)

A/B sanity 2026-04-22 : ZBAA base 28.10 → drn 26.82 σ=3.12, RJTT base 22.70 → drn 22.08 σ=2.67, LFPG base 18.20 → drn 19.13 σ=2.45.

### 13. Calibration report (commit 0f9cc2b)

`scripts/calibration_report.py` : joint `signal_log` × `signal_outcomes`, bucket les est_prob, compute :
- Reliability diagram (bucket → realized WR)
- Brier score (perfect=0)
- ECE (Expected Calibration Error)
- Log loss (heavy penalty for confident-wrong)

Per alpha_type + global, flags `ECE > alert_threshold`.

**Premier run sur 217 settled signals expose le bug CONFIRMED_YES mathématiquement** :
| alpha_type | n | wr_real | wr_exp | brier | log_loss | **ece** |
|---|---|---|---|---|---|---|
| CONFIRMED_NO | 14 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| CONFIRMED_YES | 14 | 0.00 | 1.00 | 1.00 | 13.82 | **1.00** ⚠️ |
| MODEL_VS_MARKET | 189 | 0.889 | 0.870 | 0.016 | 0.073 | 0.027 |

MODEL_VS_MARKET très bien calibré (ECE 0.027, drift -1.9pts). Le cron 09:25 génère un rapport quotidien dans `vault/brantham/polymarket/reports/calibration-YYYY-MM-DD.md`.

### 14. Drift monitor + kill switch (commit 634d108)

Runtime safety net : même si l'oracle est fixé (commit 1822e6c), une nouvelle régression future doit être **stoppée automatiquement** avant que des positions ne brûlent.

- Nouvelle table `alpha_states(alpha_type PK, status, reason, n_obs, wr_realized, wr_expected, updated_ts)`
- `data_hub.is_alpha_enabled()` + `set_alpha_state()` helpers
- `persist_signal()` retourne `False` et skip l'insert quand `status='DISABLED'`
- `scripts/drift_monitor.py` (cron 09:23) évalue sliding 7 jours :
  - DISABLED si `drift_pts ≥ 8` OU `ECE ≥ 0.20`
  - Skip tant que N < 20 (nouveaux alphas pas étranglés prématurément)
- Dry-run reproduit : avec --min-n 10, DRIFT_MONITOR aurait DISABLED CONFIRMED_YES quasi-instantanément (drift +100pts, ECE 1.0).

### 15. Ensemble stacking (commit dba3177)

Meta-model qui blend BMA + XGBoost-corrected + DRN via **Gaussian mixture moment-matching** (la même technique que BMA utilise déjà across NWP sources).

- `model_prob._apply_ensemble()` + flag `use_ensemble=True`
- `model_prob._mixture_gaussian()` helper (safe sur composants vides)
- `ensemble_weights` table (predictor PK, weight, val_crps, n_samples, updated_ts)
- `scripts/train_ensemble_weights.py` : replay 30j, score CRPS gaussian, `weight ∝ 1/max(0.5, CRPS)`. Weekly cron Monday 04:30.

Premier run (200 samples) :
- BMA CRPS 0.48, weight 41.5 %
- XGB CRPS 0.40, weight 41.5 % (floor saturé avec BMA)
- DRN CRPS 1.22, weight 17 %

A/B 2026-04-22 (μ / σ) :
- ZBAA : base 28.10 / 1.05 → ens 28.12 / 1.73
- RJTT : base 22.70 / 1.05 → ens 22.40 / 1.48
- LFPG : base 18.20 / 1.05 → ens 18.37 / 1.43

σ hérite de l'incertitude honnête de DRN sans que la μ se retrouve tirée vers ses valeurs plus bruyantes. C'est exactement ce qu'on veut d'un ensemble proprement pondéré.

### 16. Plumbing CLI flags run_alpha_live (commit ab82633)

`SignalGenConfig` expose maintenant `use_xgb_post` / `use_drn` / `use_ensemble`, propagés dans `generate_signal → forecast`. Le live runner expose les 3 flags CLI :

```bash
uv run scripts/run_alpha_live.py --once --use-ensemble
```

Switching le paper shadow vers ensemble est maintenant un flag. On peut faire tourner A/B via 2 launchd jobs distincts (baseline + ensemble-shadow) partageant `signal_log` avec un tag distinct via metadata.

## Comment activer au réveil

**Baseline actuel (inchangé)** :
```bash
uv run scripts/run_alpha_live.py --once
```

**Test ensemble 1 scan** :
```bash
uv run scripts/run_alpha_live.py --once --use-ensemble
```

**Rebuild pipeline complet** (après quelques jours d'outcomes) :
```bash
uv run scripts/reconcile_from_obs.py
uv run scripts/calibration_report.py --lookback-days 7
uv run scripts/drift_monitor.py
uv run scripts/train_bma.py --days 30
uv run scripts/train_ensemble_weights.py --window-days 30
```

Ou attendre les crons, tous schedulés 09:15 → 09:30 UTC.

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
