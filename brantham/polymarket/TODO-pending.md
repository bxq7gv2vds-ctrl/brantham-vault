---
name: TODO Pending — Prochaines étapes Polymarket Hedge Fund
description: Liste exhaustive des tâches restantes, priorisées par ROI × feasibility × criticality
type: todo
created: 2026-04-18
updated: 2026-04-19
tags: [polymarket, todo, backlog]
---

# TODO Pending

**Lire [[STATE-HANDOFF]] d'abord, puis [[audit-hedge-fund-grade|audit hedge fund grade]] pour la vue gap-analysis.**

> **Ce qu'on vient de livrer (2026-04-18 overnight + 2026-04-19 morning) — voir [[sessions/2026-04-18-overnight-model-upgrades]]**
> 18 commits. Fix OPEN_METEO freshness, BMA training réel + daily cron, XGBoost post-proc bootstrap
> 10 régions + weekly cron, write-through cache, wire XGBoost flag, backfill Open-Meteo Archive
> 100 k obs + 18 k forecasts, reconcile_from_obs autonome (217 outcomes, WR 84 %), fix
> CONFIRMED_YES prev_day bug, DRN baseline trained val CRPS 0.84 °C + wire, unbreak 4 bugs
> cascade (seed_stations, prune scope, pandas datetime64[us], training lag), sum_arb backtest
> time-sync + partition filter, calibration & reliability report + daily cron, drift monitor
> + alpha_states kill switch, ensemble stacking BMA+XGB+DRN mixture + weekly cron, CLI flags
> dans live runner, fix cache leakage quand use_ensemble actif.

---

## 🔴 BLOQUANTS USER (sans ça le reste n'a pas de sens)

- [ ] **Compte Copernicus CDS** — [https://cds.climate.copernicus.eu/](https://cds.climate.copernicus.eu/), accepter license ERA5 hourly single levels, `~/.cdsapirc`.
- [ ] **`uv add cdsapi xarray netCDF4`** puis `uv run scripts/backfill_era5.py --years 5` (~1-3 h download, 5-10 GB).
- [ ] **Funder Polymarket wallet** ($500 initial → scale).
- [ ] **`.env`** : `POLY_PRIVATE_KEY=0x...` + optional `POLY_API_KEY` pour rebates.
- [ ] **`uv add py-clob-client`** → débloque `order_manager.py` real wire.
- [ ] **`ANTHROPIC_API_KEY`** si activation `llm_reasoning`.
- [ ] **Avocat crypto FR** (avant $10 k real) — AMF compliance, AML, jurisdiction FR/EU.

---

## 🟠 HIGH ROI (2 semaines, non bloqué)

### Risk & compliance (critiques, simples)
- [ ] **Circuit breaker daily loss** — kill all positions si daily P&L < -5 % bankroll.
- [ ] **Tax lot tracking FIFO** — obligation fiscale dès 1 € de gain.
- [ ] **Audit log** — table `audit_log` (ts, action, actor, target, payload).

### Modèles (gain performance immédiat)
- [ ] **Meta-learning regime selector** — XGBoost/MLP pick best sub-model par (month, lat, climate_type, recent_variance).
- [ ] **Isotonic / Platt calibration** — rescale est_prob si ECE > 0.05 sur 7 j.
- [ ] **Per-station EMOS fit** — actuellement passthrough global; fit per (icao, month).
- [ ] **Data drift monitor** — PSI / KL div sur NWP feature distributions.

### Exécution (bloquent en partie WS daemon)
- [ ] **WS orderbook daemon launchd** — `scripts/run_orderbook_daemon.py`, KeepAlive, top 100 markets.
- [ ] **Orderbook imbalance alpha** — `(bid_depth - ask_depth) / (bid+ask)`, threshold + min liquidity.

### Validation / monitoring
- [ ] **Sharpe / Sortino / Calmar LIVE** — tracker rolling 30 j, dashboard.
- [ ] **Attribution complète** — `by alpha × city × day × hour`.
- [ ] **Daily DB snapshots S3/B2** — incremental, 30 j retention, test restore.

### ML Ops (free tools, high leverage)
- [ ] **MLflow tracking** — `uv add mlflow`, wrap training scripts.
- [ ] **Feature store SQLite** — table `feature_store (signal_id, feature, value)`, reusable.
- [ ] **Model cards** — per modèle, training data, limitations, metrics.

---

## 🟡 MEDIUM ROI (mois 1-2)

### ML SOTA
- [ ] **DRN training sur ERA5** (bloqué user) — target val CRPS < 0.6 °C, `--epochs 200 --device mps`.
- [ ] **XGBoost training sur ERA5** (bloqué user) — remplace les models ARCHIVE-based.
- [ ] **Swap EMOS → DRN** dans `model_prob.py` baseline, A/B 7 j.
- [ ] **Transformer temporal** — sequences 7-14 j, attention, 5-10 h MPS ou GPU cloud.
- [ ] **Foundation model : Pangu-Weather ONNX** — HF `LFIBSULBYV/pangu-weather`, onnxruntime local.
- [ ] **Foundation model : GraphCast** — Google Earth Engine ou self-host ONNX.

### Alpha layers nouveaux
- [ ] **Cross-market pairs stat-arb** — NYC↔Boston, JFK↔BOS corrélation ~0.85.
- [ ] **Volatility regime filter** — éviter signaux dans high-vol regimes (ensemble spread > threshold).
- [ ] **Convex arb bins** — bins contigus avec prix non-monotones.
- [ ] **Market-making passive** — poster ordres sur brackets peu liquides.

### Exécution réelle (post user wallet)
- [ ] **py-clob-client wire `order_manager.py`** — replace `_ClobClientStub`.
- [ ] **Multi-RPC supervisor** Polygon — Infura + Alchemy + own node, failover auto.
- [ ] **Post-only + cancel-replace real** — pas juste scaffold.
- [ ] **Fill prediction model** — predict P(fill) vs order depth/spread.
- [ ] **Adaptive order shredding** — N child orders pour impact minimal.

### Infrastructure
- [ ] **Grafana + Prometheus** stack — docker-compose, dashboards P&L / latency / drift.
- [ ] **Structured logging JSON** — centralisé Loki ou CloudWatch.
- [ ] **Docker-compose** full stack — reproducible, easy deploy.
- [ ] **CI/CD pipeline** — pytest + ruff + mypy sur push.

### Validation avancée
- [ ] **Monte Carlo bootstrap P&L** — 10 k scenarios, distribution P&L annuel.
- [ ] **Regime detection + labeling** — bull/bear/transition pour attribution.
- [ ] **Feature importance live** — explainability per signal.
- [ ] **Champion/Challenger framework** — 2+ models parallel, auto-promote winner.

### Compliance étendu
- [ ] **Position reconciliation DB ↔ wallet** (après live).
- [ ] **Regulatory reporting template** — format AMF.
- [ ] **Accounting integration** — export P&L compte 4xxx.

---

## 🟢 LOW ROI / STRETCH (mois 3+)

### Data sources additionnelles
- [ ] **Mesonet US dense** — +10 k stations vs 46 METAR.
- [ ] **Radar MRMS NEXRAD** — nowcast <6 h haute résolution.
- [ ] **Satellite GOES/Himawari/Meteosat** — convection tracking.
- [ ] **Lightning ENTLN** — événements extrêmes.
- [ ] **Private feeds** TheWeatherCompany / Vaisala (paid, après $50 k+).

### Modèles très lourds
- [ ] **Diffusion GenCast-style** — score-based, 100M+ params, 3+ mois dev.
- [ ] **Aurora 1.3B** (Microsoft) — via HF hub, 8 GB+ VRAM.
- [ ] **PPO execution agent** — stable-baselines3, simulated orderbook env.

### Expansion
- [ ] **Sports markets** (NBA/NFL/soccer) — Polymarket + Kalshi.
- [ ] **Crypto markets** (BTC brackets) — Polymarket + Kalshi.
- [ ] **Politics markets** (elections, geopolitical).
- [ ] **Cross-venue routing** (Kalshi, Manifold, Polymarket EU).
- [ ] **Cross-venue arbitrage** (same market, different venue).
- [ ] **Market-making create** — become MM on illiquid bins.
- [ ] **Weather-adjacent** — electricity demand, crop yields, cat bonds.

### Infrastructure hard-core
- [ ] **VPS production AWS us-east-1** — latency <50 ms, colocation Polymarket.
- [ ] **GPU infra Hetzner GEX44 €200/mo** ou RunPod A100 spot.
- [ ] **Own Polygon validator node** — direct mempool submission.
- [ ] **Hardware wallet Ledger** — positions >$10 k.
- [ ] **MEV protection Flashbots** — private mempool.
- [ ] **Postgres migration** — quand SQLite > 10 GB.
- [ ] **Disaster recovery plan** — RTO <1 h, RPO <15 min, testé.

### Risk management avancé
- [ ] **VaR / CVaR live** — 95%/99% loss envelope.
- [ ] **Portfolio stress tests Monte Carlo** — scenarios extrêmes.
- [ ] **Correlation matrix live** — monitor divergence vs assumptions.
- [ ] **Concentration limits** — max X % per market/city/TTR.
- [ ] **Liquidity-aware sizing** — ≤ Y % of market depth.
- [ ] **Oracle risk hedging** — positions inverses pour couvrir.

### Entity / legal
- [ ] **Entity structure review** — SAS vs SCI vs fund offshore.
- [ ] **Insurance** — cyber + D&O si external investors.
- [ ] **KYC/AML** si custodian integration.

---

## 🎯 Ordre recommandé prochaine session

### Session A : Compliance + risk layer (3-4 h, non bloqué)
1. Circuit breaker daily loss dans `risk_manager.py`.
2. Tax lot tracking FIFO (`trade_log.pnl` → lot attribution).
3. Audit log table + wire dans `persist_signal` / `order_manager`.
4. Daily DB snapshots cron S3/B2.

### Session B : ML gains (2-3 h, non bloqué)
1. Meta-learning regime selector (XGBoost sur month × lat × climate).
2. Isotonic calibration si ECE > 0.05.
3. Per-station EMOS fit.
4. MLflow tracking wrap sur tous les train scripts.

### Session C : Execution débloqué (si user OK)
1. `uv add py-clob-client`.
2. Wire dans `order_manager.py`, dry-run Polygon Mumbai.
3. WS orderbook daemon launchd.
4. Orderbook imbalance alpha.
5. Live $100 test trade.

### Session D : Observability (1-2 h)
1. Sharpe/Sortino/Calmar LIVE rolling 30 j.
2. Attribution par alpha × city × hour.
3. Grafana + Prometheus docker-compose.

### Session E : ERA5 + DRN (bloqué user Copernicus)
1. `backfill_era5.py --years 5`.
2. `train_drn.py --epochs 200`.
3. Validate val CRPS target <0.6 °C.
4. Swap dans `model_prob.py` baseline.

---

## 🛑 Ne jamais faire sans autorisation explicite

- Submit real orders avec money réel
- Modify wallet
- Push force sur git
- Skip paper shadow avant real money
- Over-promise ROI sans caveats
- Bypass calibration alert si ECE > threshold pour une alpha
- Disable kill switches sans confirmation user
- Deploy en prod sans A/B validation 7 j

---

## Success criteria hedge fund grade

- [ ] $10 k+ capital real tourne 30 j sans intervention manuelle
- [ ] Sharpe réalisé > 2.0 sur fenêtre roulante 60 j
- [ ] Max DD < 8 %
- [ ] ECE global < 0.05 sur toutes les alphas actives
- [ ] Latency P95 < 200 ms
- [ ] Uptime > 99.5 % (excluant windows oracle)
- [ ] Rapport quotidien automatique (Grafana + Telegram digest)
- [ ] Audit log complet toutes actions sensibles
- [ ] Disaster recovery testé (restore DB < 1 h)

Voir [[audit-hedge-fund-grade|audit détaillé]] pour le gap analysis complet.

## Related

- [[_MOC|Hub principal]]
- [[STATE-HANDOFF|State complet]]
- [[audit-hedge-fund-grade|Audit hedge fund grade]]
- [[sessions/2026-04-18-overnight-model-upgrades|Session 2026-04-18 overnight (18 commits)]]
- [[roadmap|Roadmap phases classique]]
- [[deep-learning-roadmap|Deep Learning roadmap]]
- [[execution-playbook|Execution playbook 16 dimensions]]
