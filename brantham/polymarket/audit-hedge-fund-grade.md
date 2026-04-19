---
name: Audit Hedge Fund Grade — Polymarket Weather Alpha
description: Audit exhaustif du système actuel vs standards hedge fund institutionnel, avec gap analysis et priorisation ROI
type: audit
created: 2026-04-19
tags: [polymarket, audit, hedge-fund, gap-analysis]
---

# Audit Hedge Fund Grade — 2026-04-19

**Contexte** : Après 18 commits overnight (2026-04-18 → 2026-04-19) qui ont transformé un prototype en système auto-piloté avec feedback loop complet. Audit dans une optique "est-ce prêt pour du capital propriétaire hedge fund de $1k-50k, puis scale $50k+ ?"

## Verdict global

| Dimension | État | Note |
|---|---|---|
| Data pipeline | Solid baseline (8 sources NWP, 100 k ARCHIVE + METAR archive) | 7/10 |
| Modèles | EMOS+BMA+XGB+DRN ensemble calibré | **8/10** |
| Signaux alpha | 1 main (MODEL_VS_MARKET WR 88.9 %) + oracle + sum-arb | 6/10 |
| Exécution | Scaffold présent, pas wired real (bloqué user wallet) | 3/10 |
| Risk management | Kelly, caps, 2 kill switches actifs | **8/10** |
| Validation / backtest | Walk-forward + paper shadow + calibration + drift | **9/10** |
| Infrastructure | 12 launchd autonomes, Telegram, metrics scaffold | 7/10 |
| Compliance / legal | Quasi zéro | 1/10 |
| ML Ops | Embryonnaire (pas de MLflow, pas de feature store) | 3/10 |
| Expansion | Weather only, 1 venue | 4/10 |

**Score global : 56/100**. On est **au-dessus d'un prototype sérieux**, **en dessous d'un hedge fund systematic production-grade**. Les gaps critiques sont : exécution réelle, compliance, ML Ops, et la diversification venue/asset.

## Par dimension

### 1. Data pipeline (7/10)

**En place** :
- 8 sources NWP : GFS / GEFS / ICON / ICON-EU / ECMWF / AIFS / HRRR / JMA (via Open-Meteo endpoints)
- Obs : METAR rolling 30 j + ARCHIVE Open-Meteo 90 j (ERA5-derivé, 100 k rows)
- `nwp_ensemble_blend` unifié (mean/std/p05…p95)
- `data_freshness` monitor + kill switch
- Idempotent ingests (INSERT OR REPLACE)

**Gaps hedge fund grade** :
- [ ] **ERA5 direct via Copernicus CDS** — bloqué user. Nécessaire pour 5 ans d'hourly ground truth (ARCHIVE = dérivé, possible bias).
- [ ] **Mesonet US dense network** — +10 k stations vs 46 METAR. Variance micro-climat capturée.
- [ ] **Radar nowcast MRMS** (NEXRAD) — prédictions <6 h haute résolution spatiale.
- [ ] **Satellite data** — GOES-18 / Himawari-9 / Meteosat pour convection tracking.
- [ ] **Lightning detection** — Earth Networks / ENTLN pour événements extrêmes.
- [ ] **Data quality monitor** — détection drift sur distributions NWP (pas juste freshness).
- [ ] **Private weather feeds** — TheWeatherCompany, Vaisala, Schneider (paid, ~$5-50k/an).

**Priorité** : ERA5 (bloqué) → Mesonet (libre, accroît variance obs) → Satellite nowcast (pour H0-H6 markets).

### 2. Modèles (8/10)

**En place** :
- **EMOS** baseline calibrated.
- **BMA** avec weights learned (47 stations × 8 sources, retrain daily).
- **XGBoost post-proc** 10 régions (RMSE val 0.6-1.4 °C).
- **DRN** baseline (val CRPS 0.84 °C).
- **Ensemble stacking** via Gaussian mixture, weights trained from val CRPS.
- `forecast_cache` write-through, bypass sur stack flags.

**Gaps hedge fund grade** :
- [ ] **DRN ERA5 training** (bloqué user) — dataset propre, CRPS target <0.6 °C.
- [ ] **Meta-learning regime selector** — XGBoost / MLP choisit le best sub-model par synoptic pattern (saison, lat, climatology).
- [ ] **Transformer temporal** — séquences 7-14 j, attention, 5-10 h MPS ou 1-2 h GPU.
- [ ] **Foundation models** :
  - Pangu-Weather (1.4B params, ONNX ~3 GB) via `onnxruntime`.
  - GraphCast (Google) — requires ~8 GB RAM.
  - Aurora 1.3B (Microsoft).
- [ ] **Diffusion GenCast-style** — score-based, 100M+ params, 3+ mois dev.
- [ ] **Model monitoring** — data drift detection (PSI, KL div) sur features.
- [ ] **Isotonic / Platt calibration** — rescale est_prob si ECE > threshold persistent.
- [ ] **Per-station EMOS fit** (actuellement passthrough / global params).

**Priorité** : Regime selector (easy, haute valeur) → Isotonic calibration (réduit drift) → Foundation models (si GPU budget).

### 3. Signaux / Alpha (6/10)

**En place** :
- **MODEL_VS_MARKET** : main alpha, WR 88.9 %, ECE 0.027 sur 189 outcomes.
- **CONFIRMED_YES/NO** : oracle, buggy prev_day fixé, live.
- **sum_arb** : backtest time-sync'd, live scanner via Gamma API.

**Gaps hedge fund grade** :
- [ ] **Orderbook imbalance alpha** — microstructure, dépend WS daemon (bloqué py-clob-client).
- [ ] **Cross-market pairs stat-arb** — NYC↔Boston, JFK↔BOS corrélation ~0.85.
- [ ] **Volatility regime filter** — éviter signaux dans high-vol regimes (détection via NWP ensemble spread).
- [ ] **Convex arb bins** — bins contigus avec prix non-monotones (profitable).
- [ ] **Market-making passive** — poster ordres sur brackets peu liquides, earn spread.
- [ ] **Earnings-like events** — extreme weather forecasts → spike in volume.
- [ ] **Multi-asset expansion** : sports (NBA/NFL), crypto (BTC brackets), politics (elections).

**Priorité** : Orderbook imbalance (débloque beaucoup) → Cross-market pairs (nouveau alpha 0-risk) → Volatility filter (safety).

### 4. Exécution (3/10)

**En place** :
- Latency profiler P50/P95/P99.
- Slippage EMA per-market learner.
- Order manager (stub `_ClobClientStub`).
- Post-only + cancel-replace scaffold.
- Metrics Prometheus exporter :9090.
- FastAPI dashboard :8080.

**Gaps hedge fund grade** :
- [ ] **py-clob-client wire** (bloqué user wallet + POLY_PRIVATE_KEY).
- [ ] **WS orderbook daemon 24/7** — launchd KeepAlive, top 100 markets subscribed.
- [ ] **Multi-RPC supervisor** — Infura + Alchemy + own Polygon node, failover automatique.
- [ ] **Post-only real** — ordre cancel-replace si ahead mover, non pas stub.
- [ ] **MEV protection** — Flashbots / private mempool submission.
- [ ] **Hardware wallet Ledger** — signing offline pour positions >$10 k.
- [ ] **Colocation AWS us-east-1** — latency <50 ms vers Polymarket.
- [ ] **Cross-chain routing** — Polymarket Polygon mainnet + bridging.
- [ ] **Fill prediction model** — predict probability of fill given order depth / spread.
- [ ] **Adaptive order sizing** — shred big orders en N child pour impact minimal.

**Priorité absolue user** : py-clob-client wire + wallet. Sans ça aucun capital ne peut tourner.

### 5. Risk Management (8/10)

**En place** :
- Kelly correlation-adjusted (region + timezone proxies).
- Per-city cap (max N positions).
- Max exposure cap (% of bankroll).
- Kill switch data freshness (NWP down → skip scan).
- **Kill switch alpha drift** (NEW) : `alpha_states` table, disable auto si drift >8 pts ou ECE >0.20.
- `max_edge` cap 0.40 (prévient suspicion signals).
- `min_ensemble_members` 20 (skip si NWP pauvre).

**Gaps hedge fund grade** :
- [ ] **Dynamic Kelly sur realized Sharpe** — scale down après drawdown.
- [ ] **VaR / CVaR live** — 95 %/99 % loss envelope, monitor quotidien.
- [ ] **Circuit breaker daily loss** — kill all si loss > 5 % bankroll.
- [ ] **Portfolio stress tests** — Monte Carlo scenarios (extreme weather, API outage, oracle malfunction).
- [ ] **Correlation matrix live** — monitor si corrélations réalisées divergent des assumptions.
- [ ] **Concentration limits** — max N % par market, par city, par time-to-resolution.
- [ ] **Liquidity risk** — sizing ≤ X % of market depth (currently hardcoded 50 $ min).
- [ ] **Oracle risk hedging** — position inverse sur certain markets pour couvrir cas oracle malfunction.
- [ ] **Regulatory risk** — monitor Polymarket jurisdictional changes (US blocked, EU OK).

**Priorité** : Circuit breaker daily loss (simple, critique) → VaR live → Monte Carlo stress tests.

### 6. Validation / backtest (9/10)

**En place** :
- Walk-forward OOS (rolling windows).
- Paper shadow (217 outcomes settled).
- **Reconcile autonome** (reconcile_from_obs — NEW).
- **Calibration report** (Brier/ECE/log loss — NEW).
- **Drift monitor** (NEW).
- Unified backtest engine (`src/pmhedge/alpha/backtest.py`).
- Slippage model + attribution.

**Gaps hedge fund grade** :
- [ ] **Monte Carlo bootstrap P&L** — 10k scenarios, distribution P&L annuel.
- [ ] **Attribution complète** — par alpha × city × day × hour.
- [ ] **Sharpe / Sortino / Calmar LIVE** — tracker quotidien, pas juste backtest.
- [ ] **Drawdown tracking + max DD monitoring**.
- [ ] **Regime detection** — labeling bull / bear / transition regimes pour attribution.
- [ ] **Feature importance tracking** — explainability per signal.
- [ ] **Out-of-sample vs in-sample degradation alert**.
- [ ] **Pre-execution simulation** — simulate trade dans les conditions actuelles avant live.

**Priorité** : Sharpe/Sortino LIVE dashboard → Attribution complète → Monte Carlo bootstrap.

### 7. Infrastructure (7/10)

**En place** :
- 5 SQLite DBs (alpha_data_hub, bracket_scalper, pmhedge, all_markets, emos_cache).
- **12 launchd jobs** autonomes (6 nouveaux : bma-train, xgb-retrain, reconcile-obs, calibration, drift-monitor, ensemble-train).
- Telegram alerts (freshness, drift, high-edge signals).
- Prometheus exporter scaffold.
- HTML dashboard scaffold.

**Gaps hedge fund grade** :
- [ ] **Grafana stack déployé** — dashboards P&L, latency, drift, Kelly factor, portfolio heatmap.
- [ ] **Daily DB snapshots** vers S3/B2 (incremental, 30 j retention).
- [ ] **Disaster recovery plan** — RTO <1 h, RPO <15 min.
- [ ] **VPS production** — AWS us-east-1 (near Polymarket AWS) ou Hetzner EU (data residency).
- [ ] **GPU infra** — Hetzner GEX44 €200/mo ou RunPod A100 spot pour Transformer/Diffusion.
- [ ] **CI/CD pipeline** — pytest + ruff + mypy sur push, auto-deploy staging.
- [ ] **Secrets manager** — `.env` files → AWS Secrets Manager ou HashiCorp Vault.
- [ ] **Structured logging** — JSON logs, centralisé vers Loki / CloudWatch.
- [ ] **Postgres migration** quand >10 GB SQLite (actuellement ~2 GB).
- [ ] **Docker-compose** pour stack full (reproducible, easy deploy).

**Priorité** : Daily snapshots S3 (data loss protection) → Grafana (observability) → VPS production.

### 8. Compliance / Legal (1/10)

**En place** :
- Nothing beyond `SAS Brantham Partners` juridique (SIREN enregistré).

**Gaps hedge fund grade** (critiques pour real money >$10k) :
- [ ] **Tax lot tracking FIFO** — obligation fiscale française, report capital gains.
- [ ] **Audit log** — qui/quand/quoi sur trades, modifications, emergency stops.
- [ ] **Jurisdiction compliance** — verify Polymarket usage légal FR (KYC required ? DeFi status ?).
- [ ] **KYC/AML** si ever integrated with custodian.
- [ ] **Entity structure** — décision SAS vs SCI vs fund offshore selon taille.
- [ ] **Accounting integration** — export P&L format comptable (compte 4xxx).
- [ ] **Regulatory reporting** — AMF déclaration si > certain seuil.
- [ ] **Insurance** — cyber insurance, D&O si external investors.
- [ ] **Legal opinion** — avocat specialisé crypto/prediction markets.
- [ ] **Privacy / GDPR** — si données clients, pas juste self-custodied.

**Priorité** : Tax lot FIFO (obligation légale dès $1 de gain) → Audit log (traçabilité) → Legal opinion (avant $50k+).

### 9. ML Ops (3/10)

**En place** :
- Training scripts CLI (`train_bma`, `train_xgboost_post`, `train_drn`, `train_ensemble_weights`).
- Model files persisted (`models/*.json`, `models/*.pt`).
- Daily/weekly retrain crons.

**Gaps hedge fund grade** :
- [ ] **MLflow tracking** — experiments, metrics, params, artifacts.
- [ ] **Model versioning + rollback** — tag every retrain, revert si régression.
- [ ] **Feature store** — Feast ou custom, reuse features across models.
- [ ] **Experiment tracking** — A/B tests framework with significance testing.
- [ ] **Training data versioning** — DVC ou LakeFS.
- [ ] **Hyperparameter optimization** — Optuna / Ray Tune.
- [ ] **Model cards** — documentation par modèle (training data, limitations, metrics).
- [ ] **Automated retrain trigger** sur data drift (PSI > threshold).
- [ ] **Champion/Challenger framework** — run 2+ models en parallèle, auto-promote winner.
- [ ] **Pipeline testing** — unit + integration tests sur feature engineering.

**Priorité** : MLflow (free, immediate value) → Champion/Challenger (hedge fund standard) → Feature store.

### 10. Expansion (4/10)

**En place** :
- Weather markets uniquement.
- 1 venue : Polymarket.
- 46 stations / 43 cities.

**Gaps hedge fund grade** :
- [ ] **Sports markets** — NBA / NFL / soccer (Polymarket + Kalshi).
- [ ] **Crypto markets** — BTC price brackets (Polymarket + Kalshi).
- [ ] **Politics markets** — elections, geopolitical (Polymarket strong here).
- [ ] **Multi-venue routing** — Kalshi, Manifold, Polymarket EU.
- [ ] **Cross-venue arbitrage** — same market, different venue.
- [ ] **Create markets** — become market maker on illiquid bins.
- [ ] **Additional weather cities** — expand from 46 to 100+ (easy scale).
- [ ] **Weather-adjacent** — electricity demand, crop yields, cat bonds.

**Priorité** : Cross-venue arb Kalshi + Polymarket (zero model risk) → Sports markets (volume élevé) → Crypto (HF retail appetite).

## Priorisation globale — Next 90 days

### Semaine 1-2 (BLOQUANTS CRITIQUES)

1. 🔴 **User setup Copernicus CDS** → débloque ERA5 + DRN/XGB train propre.
2. 🔴 **User fund Polymarket wallet $500** + `POLY_PRIVATE_KEY` → débloque real money.
3. 🔴 **`uv add py-clob-client` + wire order_manager** → débloque exécution réelle.

### Semaine 2-4 (ROI élevé, non bloqué)

4. 🟠 **Circuit breaker daily loss** (risk mgmt, critique).
5. 🟠 **Tax lot tracking FIFO** (compliance, obligation).
6. 🟠 **Meta-learning regime selector** (modèle, haute valeur).
7. 🟠 **Isotonic calibration** (modèle, réduit drift).
8. 🟠 **WS orderbook daemon** (débloque orderbook imbalance alpha).
9. 🟠 **MLflow tracking** (ML Ops, free tool).
10. 🟠 **Daily DB snapshots S3** (infra, data protection).

### Mois 2

11. 🟡 **ERA5 DRN train + swap** (modèle SOTA).
12. 🟡 **Attribution complète par alpha × city × hour** (validation).
13. 🟡 **Sharpe/Sortino LIVE dashboard** (monitoring).
14. 🟡 **Grafana stack** (observability).
15. 🟡 **Orderbook imbalance alpha** live.
16. 🟡 **Cross-market pairs stat-arb** (nouveau alpha).

### Mois 3

17. 🟢 **Monte Carlo stress tests** (risk mgmt avancé).
18. 🟢 **Champion/Challenger framework** (ML Ops hedge fund).
19. 🟢 **VPS production AWS us-east-1** (infra scale).
20. 🟢 **Cross-venue arb Kalshi** (expansion).

### Stretch (6 mois+)

21. 🔵 **Foundation models** (Pangu / GraphCast / Aurora).
22. 🔵 **Diffusion GenCast-style**.
23. 🔵 **Sports / crypto / politics expansion**.
24. 🔵 **GPU infra Hetzner/RunPod**.
25. 🔵 **Hardware wallet Ledger + MEV protection**.

## Décisions à prendre

1. **Budget GPU** : sans ça Transformer/Diffusion restent théoriques. Hetzner GEX44 ~200 €/mo vs RunPod spot ~$0.30/h (20h/semaine = $24/mo). RunPod wins.
2. **Capital initial real money** : $500 (test) → $2k (validation) → $10k (scale) → $50k (production). Rythme : +30 j par palier si Sharpe > 1.5 et DD < 10 %.
3. **VPS** : Mac local OK jusqu'à 1 k/jour signaux. Si scale >5 k/jour OR real money >$10k, migrer VPS.
4. **Regulatory** : avant $10 k capital real, consulter avocat crypto FR pour compliance AMF / AML.
5. **Data budget** : Open-Meteo gratuit suffit MVP. Paid feeds (Vaisala) justifiable après $50k+ bankroll.

## Success criteria — quand on sait que c'est "hedge fund grade"

- [ ] $10 k+ capital real tourne 30 j sans intervention manuelle
- [ ] Sharpe réalisé > 2.0 sur fenêtre roulante 60 j
- [ ] Max DD < 8 %
- [ ] ECE global < 0.05 sur toutes les alphas actives
- [ ] Latency P95 < 200 ms
- [ ] Uptime > 99.5 % (excluant windows oracle)
- [ ] Rapport quotidien automatique (Grafana + Telegram digest)
- [ ] Audit log complet toutes actions sensibles
- [ ] Disaster recovery testé (restore DB < 1 h)

**Gap actuel vs "hedge fund grade"** : 2-3 mois de dev focused + user actions débloquées.

## Related

- [[_MOC|Polymarket Hub]]
- [[STATE-HANDOFF|State complet]]
- [[TODO-pending|TODO priorisé]]
- [[sessions/2026-04-18-overnight-model-upgrades|Session overnight 2026-04-18]]
- [[architecture|Architecture 4 couches]]
- [[deep-learning-roadmap|Deep Learning roadmap]]
- [[execution-playbook|Execution playbook 16 dimensions]]
