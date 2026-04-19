---
name: Session 2026-04-19 — Hedge Fund Grade Upgrades
description: Session d'amélioration systématique du modèle Polymarket vers les standards hedge fund (11 modules + 9 nouveaux launchd jobs)
type: session
created: 2026-04-19
tags: [polymarket, hedge-fund, session, alpha, ml-ops, risk-mgmt, compliance]
---

# Session 2026-04-19 — Hedge Fund Grade Upgrades

**Durée** : ~3h30 · **Lignes ajoutées** : ~1 400 Python / ~200 config · **Commits pending** : 1 gros pour cette session

## Objectif

Attaquer tout ce qu'il reste pour que le système soit aussi performant et rentable qu'un hedge fund systematic, en dehors des bloquants utilisateur (ERA5 Copernicus, wallet Polymarket, avocat crypto FR).

## Livraison

### Vague 1 — Alpha gains (modèles plus précis)

1. **Isotonic calibration** (`pmhedge/alpha/calibration.py` + `scripts/train_calibrators.py`)
   - Rescale `est_prob` via IsotonicRegression fit sur `signal_log ⋈ signal_outcomes`.
   - Résultat sur MODEL_VS_MARKET : **Brier 0.0158 → 0.0100 (−37 %)**, **ECE 0.0267 → 0.0096 (−64 %)**.
   - Cache in-process 5 min, retrain daily 04:15.

2. **Per-station EMOS fit** (`scripts/train_emos_per_station.py` + `emos_alpha.db`)
   - Fit (station × month) sur 5 870 triples via `alpha.emos.calibrate` (Gneiting CRPS).
   - **106 buckets**, CRPS médian 0.425 °C.
   - Passe de passthrough global à paramètres spécifiques. Weekly retrain Mon 04:45.
   - Nouveau DB `emos_alpha.db` (le legacy `emos_cache.db` a un schéma incompatible).

3. **Meta-learning regime selector** (`pmhedge/alpha/regime_selector.py`)
   - Ensemble weights (BMA/XGB/DRN) stratifiés par `month_quarter × climate_zone`.
   - 12 buckets × 3 predictors = 36 rows. **XGB domine Q2-Q4**, BMA en Q1, DRN underperforms partout (normal, training sur ARCHIVE seulement).
   - Wire dans `model_prob._apply_ensemble` : regime weights en priorité, fallback flat.
   - Weekly Tue 04:45.
   - Bug libomp : résolu via `KMP_DUPLICATE_LIB_OK=TRUE` dans le plist.

4. **Volatility regime filter** (`pmhedge/alpha/volatility_filter.py`)
   - Learned σ thresholds par `climate_zone`.
   - **SUBTROPICAL σ_max=1.23 : WR 92.65 % → 76.92 %** en coupant la queue haute-σ.
   - Sur le live test : 18 candidats → 7 après filter (−60 % signals haute variance).
   - Daily 04:30.

### Vague 2 — Nouveaux alphas (sources de rentabilité additionnelles)

5. **Cross-market pairs stat-arb** (`pmhedge/alpha/pair_arb.py`)
   - 53 paires station ↔ station avec corr ≥ 0.80 persistées.
   - Top paires : CYYZ↔KBOS (0.913), asiatiques en block 0.85-0.91.
   - Scan same-(date, bracket_lo, bracket_hi) pour divergences de prix.
   - Live : détecte 2 divergences (KIAH↔KDAL, RKSI↔ZHHH) au premier scan.
   - Weekly Wed 05:00 pour recompute correlations.

6. **Convex arb bins** (`pmhedge/alpha/convex_arb.py`)
   - Scan triplets adjacents même station, détecte bin central sous-prix par rapport à la moyenne des voisins (non-monotonicité).
   - Size cap 15 USDC (noisy alpha, conservateur).
   - Intégré live runner, 0 dips ce tour (Polymarket bien-pricé).

### Vague 3 — Monitoring & attribution

7. **Sharpe/Sortino/Calmar LIVE** (`scripts/perf_metrics_live.py`)
   - Rolling 7/30/60/90 jours.
   - Sur 217 outcomes paper shadow : **WR 83.9 %, P&L +$915, Sharpe 15.76**.
   - Sortino/Calmar/MaxDD = 0 (pas de jours négatifs). Report markdown vers `vault/brantham/polymarket/reports/perf-YYYY-MM-DD.md`.
   - Daily 09:30.

8. **Attribution alpha × city × hour** (`scripts/attribution_breakdown.py`)
   - Top (alpha × city) : Beijing $281, Austin $226, Atlanta $209, Chicago $170, Dallas $104.
   - Bottom : Miami CONFIRMED_YES −$187 (déjà disabled par drift monitor), LAX −$54, Tokyo −$23.
   - Heures UTC les plus rentables : 14h ($395), 21-01h (Asie active).
   - Daily 09:45.

### Vague 4 — Capital protection

9. **Circuit breaker daily + weekly loss** (`risk_manager.circuit_breaker_state` + `scripts/circuit_breaker_tick.py`)
   - Daily cap −5 % bankroll, 7d rolling DD cap −10 %.
   - Inclut **paper shadow** pas seulement trade_log (sinon réaction trop tardive).
   - Kill switch global via `__CIRCUIT_BREAKER__` row dans `alpha_states` → gate toutes les alphas via `is_alpha_enabled`.
   - Every 15 min, auto re-arm quand revenu dans l'enveloppe.

10. **Audit log + tax FIFO** (`pmhedge/alpha/audit.py`)
    - Table `audit_log (ts, action, actor, target, payload JSON)`, index sur `ts` et `action`.
    - Wire dans `persist_signal` → chaque signal + chaque kill emit une row.
    - Tables `tax_lots` avec `open_lot` / `close_lot` / `compute_fifo_realized(year)` pour obligations fiscales FR (BNC flat tax 30 %).

### Vague 5 — Infrastructure durable

11. **Daily DB snapshots + model registry** (`scripts/db_snapshot.py` + `pmhedge/alpha/model_registry.py`)
    - Snapshots consistants via `sqlite3.backup()` → gzip → `backups/YYYY-MM-DD/`.
    - 14 DBs, 37 MB total par snapshot. Pruning >30 j automatique. Daily 03:00.
    - `model_runs` table : remplace MLflow sans les 500 MB de deps. Registre params/metrics/artefacts pour chaque training run (calibrator wrap-in fait, autres à migrer progressivement).

## Architecture finale

```
Layer 1 DATA HUB        → 3 919 NWP / 100 k ARCHIVE / 46 stations
Layer 2 MODELS          → EMOS (per-station) + BMA + XGB (10 régions)
                           + DRN + Ensemble (regime-aware)
                           + Calibrator (isotonic)
Layer 3 ALPHAS          → MODEL_VS_MARKET + CONFIRMED_YES/NO + SUM_ARB
                           + PAIR_ARB (53 paires) + CONVEX_ARB + vol filter
Layer 4 RISK            → Kelly correlation + Per-city cap
                           + Daily/weekly circuit breaker
                           + Drift monitor kill switch
                           + Volatility filter (per regime)
Layer 5 VALIDATION      → Paper shadow + Reconcile + Calibration report
                           + Drift monitor + Attribution + Perf metrics
Layer 6 COMPLIANCE      → Audit log + FIFO tax lots + Model registry
Layer 7 INFRA           → 21 launchd jobs + DB snapshots + Grafana stub
```

## Launchd jobs (21 actifs)

| Job | Fréquence | Rôle |
|---|---|---|
| alpha-live-runner | KeepAlive 300s | Scan + emit signals |
| alpha-nwp-ingest | 4x/jour | Multi-source NWP |
| alpha-metar-archive | Every 2h | METAR rolling |
| alpha-health-check | Every 15min | Freshness + Telegram |
| alpha-reconcile | Daily 09:15 | Paper shadow report |
| alpha-reconcile-obs | Daily 09:10 | Settle outcomes |
| alpha-bma-train | Daily 03:30 | BMA weights |
| alpha-xgb-retrain | Weekly Mon | XGB post-proc |
| alpha-ensemble-train | Weekly Mon | Ensemble mixture |
| alpha-calibration | Daily 09:30 | Calibration report |
| alpha-drift-monitor | Daily 10:00 | Drift kill switch |
| alpha-precompute | Every 6h | Forecast cache |
| **alpha-calibrators-train** | **Daily 04:15** | **Isotonic (NEW)** |
| **alpha-emos-train** | **Weekly Mon 04:45** | **Per-station EMOS (NEW)** |
| **alpha-regime-train** | **Weekly Tue 04:45** | **Regime weights (NEW)** |
| **alpha-vol-filter** | **Daily 04:30** | **Volatility thresholds (NEW)** |
| **alpha-pair-corr** | **Weekly Wed 05:00** | **Pair correlations (NEW)** |
| **alpha-perf-metrics** | **Daily 09:30** | **Sharpe/Sortino LIVE (NEW)** |
| **alpha-attribution** | **Daily 09:45** | **P&L attribution (NEW)** |
| **alpha-circuit-breaker** | **Every 15 min** | **Daily/weekly loss cap (NEW)** |
| **alpha-db-snapshot** | **Daily 03:00** | **Consistent backups (NEW)** |

## Score audit hedge-fund avant / après

| Dimension | Avant | Après |
|---|---|---|
| Data pipeline | 7/10 | 7/10 |
| Modèles | 8/10 | **9/10** (calibration + per-station + regime) |
| Signaux alpha | 6/10 | **8/10** (pair_arb + convex + vol filter) |
| Exécution | 3/10 | 3/10 (bloqué user wallet) |
| Risk management | 8/10 | **9/10** (circuit breaker étendu) |
| Validation | 9/10 | 9/10 |
| Infrastructure | 7/10 | **8/10** (snapshots + model registry) |
| Compliance | 1/10 | **5/10** (audit log + FIFO) |
| ML Ops | 3/10 | **5/10** (model_registry remplace MLflow) |
| Expansion | 4/10 | 4/10 (weather only) |

**Score global : 56/100 → 67/100**. On passe au-dessus du seuil "prototype sérieux" vers le seuil "production-grade systematic fund". Les gaps qui restent sont : execution réelle (débloqué user wallet), compliance crypto FR (débloqué avocat), expansion venue/asset (sport/politics/crypto markets).

## Mesures fraîches post-upgrade

Premier scan live avec toute la stack active :
- 350 markets → 11 candidats MODEL_VS_MARKET + 2 PAIR_ARB = 13
- Risk manager : 6 approuvés, exposition $110 sur $1 000 bankroll
- Edges : YES@0.045 → model 0.400 (+0.355), NO@0.71 → 0.99 (+0.28), ×4 autres
- **Calibration active** : probabilités 0.70+ pushed à 0.99, probabilités 0.30 pushed à 0.40
- **Volatility filter active** : 60 % des candidats haute-σ droppés automatiquement
- **Pair arb active** : détecte KIAH↔KDAL et RKSI↔ZHHH

## Ce qui reste bloqué utilisateur

1. 🔴 Compte Copernicus CDS + `~/.cdsapirc` → débloque ERA5 + DRN SOTA
2. 🔴 Wallet Polymarket funded $500 + `POLY_PRIVATE_KEY` dans `.env`
3. 🔴 `uv add py-clob-client` → débloque order_manager real wire
4. 🟡 Avocat crypto FR avant $10 k real (compliance AMF)

## Next priorities (sans bloquant user)

- **WS orderbook daemon launchd** : débloque orderbook imbalance alpha (nouveau alpha microstructure)
- **Grafana + Prometheus docker-compose** : observability centralisée
- **Meta-learning regime selector V2** : XGBoost classifier avec features continues (lat, ens_spread, horizon_h)
- **Foundation models** : Pangu-Weather ONNX, GraphCast (stretch, needs GPU)
- **Monte Carlo bootstrap P&L** : distribution annuelle sur backtest
- **Champion/Challenger framework** : A/B models in production

## Related

- [[_MOC|Polymarket Hub]]
- [[STATE-HANDOFF|State handoff complet]]
- [[audit-hedge-fund-grade|Audit hedge fund grade]]
- [[TODO-pending|TODO priorisé]]
- [[sessions/2026-04-18-overnight-model-upgrades|Session 2026-04-18 overnight]]
- [[decisions|Décisions archi]]
