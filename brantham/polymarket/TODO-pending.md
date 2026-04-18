---
name: TODO Pending — Prochaines étapes Polymarket Hedge Fund
description: Liste exhaustive des tâches restantes, priorisées par ROI × feasibility
type: todo
created: 2026-04-18
updated: 2026-04-18
tags: [polymarket, todo, backlog]
---

# TODO Pending — Priorité

**Lire [[STATE-HANDOFF]] d'abord** pour comprendre l'état complet.

> **2026-04-18 overnight (voir [[sessions/2026-04-18-overnight-model-upgrades]])**
> — Complétés : fix OPEN_METEO freshness, BMA training réel (cron daily),
> XGBoost post-proc bootstrap (10 régions), wire `use_xgb_post` flag,
> write-through cache, backfill Open-Meteo Archive (100 k obs)
> + historical NWP (18 k forecasts), reconcile_from_obs autonome
> (199 settled, WR 84.4 %), fix CONFIRMED_YES `prev_day` bug.

## 🔥 Blocage utilisateur (à faire AVANT les tâches dev)

### Phase ML (bloque tout le volet deep learning)

- [ ] **Créer compte Copernicus CDS**
  - URL : https://cds.climate.copernicus.eu/
  - Accepter license ERA5 hourly single levels
  - Créer `~/.cdsapirc` avec API key
- [ ] `uv add cdsapi xarray netCDF4`
- [ ] `uv run scripts/backfill_era5.py --years 5` (~1-3h download)

### Phase Live (bloque real money)

- [ ] **Funder wallet Polymarket** ($500-1000 initial)
- [ ] `.env` : `POLY_PRIVATE_KEY=0x...` + optional `POLY_API_KEY=...`
- [ ] `uv add py-clob-client`
- [ ] Valider paper shadow 7-30j avant deploy

### Phase LLM

- [ ] `.env` : `ANTHROPIC_API_KEY=sk-ant-...` pour LLM reasoning
- [ ] Test `uv run python -c "from pmhedge.deep_learning.llm_reasoning import reason; ..."`

## 📋 Tâches dev (21 pending)

### HIGH ROI (1-2 semaines)

- [ ] **#22 XGBoost training sur ERA5** (bloqué user : ERA5)
  - Commande : `uv run scripts/train_xgboost_post.py`
  - Output : `models/xgb_postproc_{region}.json`
- [ ] **#27 DRN training sur ERA5** (bloqué user : ERA5)
  - Commande : `uv run scripts/train_drn.py --epochs 200 --device mps`
  - Output : `models/drn.pt` + `models/drn_features.npz`
  - Target : val CRPS < 1.5°C
- [ ] **Swap EMOS → DRN dans model_prob.py** (feature flag)
  - Add `use_drn: bool = False` param
  - A/B test DRN vs EMOS sur paper shadow 7j
- [ ] **#31 Meta-learning regime-aware selector**
  - XGBoost pick best sub-model par synoptic pattern
  - Features : month, lat, climate_type, recent_variance
  - Target : CRPS of each sub-model → lowest-CRPS wins
- [ ] **#32 MLflow tracking**
  - `uv add mlflow`
  - Wrap DRN/Transformer/XGBoost training with `mlflow.log_*`
  - UI : `uv run mlflow ui --port 5000`
- [ ] **#33 Feature store (custom SQLite)**
  - Table `feature_store` avec (signal_id, feature_name, value)
  - Reusable across models
- [ ] **py-clob-client live integration** (bloqué user)
  - Wire `_ClobClientStub` in `order_manager.py`
  - Dry-run testnet first
- [ ] **WS orderbook daemon launchd** (continuous 24/7)
  - Create `scripts/run_orderbook_daemon.py`
  - Plist launchd KeepAlive
  - Subscribe top 100 active markets

### MEDIUM ROI (semaines 2-4)

- [ ] **#28 Transformer training sur ERA5**
  - Commande : `uv run python -c "from pmhedge.deep_learning.transformer import train_transformer; ..."`
  - ~5-10h sur MPS ou 1-2h sur GPU cloud
- [ ] **#29 PPO training sur simulated orderbook**
  - Env : synthetic orderbook from price_bars history
  - `uv add stable-baselines3 gymnasium`
  - ~10K-100K timesteps
- [ ] **#26 Foundation models : Pangu-Weather ONNX** 
  - Download Pangu HF : `huggingface-cli download LFIBSULBYV/pangu-weather`
  - Local inference via `onnxruntime`
  - Add as NWP source
- [ ] **#26 Foundation models : GraphCast**
  - Via Google Earth Engine ou self-host ONNX
  - Requires ~8GB RAM
- [ ] **Grafana + Prometheus stack**
  - Docker compose : grafana + prometheus
  - Dashboards préconfigurés (P&L, latency, drift)
- [ ] **Daily auto-reports**
  - Cron vers `vault/brantham/polymarket/reports/YYYY-MM-DD.md`
  - Include : P&L, signals, drift, top cities

### LOW ROI / STRETCH

- [ ] **#34 Diffusion model GenCast-style**
  - Score-based diffusion PyTorch
  - 100M+ params, needs GPU serious
  - 3+ mois de dev
- [ ] **#35 GPU infra Hetzner/AWS**
  - Hetzner GEX44 ~€200/mo (RTX 4000 Ada)
  - RunPod A100 spot ~$0.30/h
  - Nécessaire pour Transformer gros + Diffusion
- [ ] **Aurora 1.3B params** (Microsoft)
  - Via HF hub
  - 8GB+ VRAM
- [ ] **Multi-venue routing**
  - Kalshi, Manifold, Polymarket EU
  - Requires each exchange's API
- [ ] **Own Polygon validator node**
  - Direct mempool submission
  - MEV protection
- [ ] **Hardware wallet Ledger**
  - Pour positions >$10k
  - USB-C connection

### NICE-TO-HAVE / Monitoring

- [ ] Weekly review script (vendredi soir)
- [ ] Monthly model retrain cron
- [ ] Drift alert Telegram si WR drift >5pts
- [ ] Tax lot tracking FIFO
- [ ] Position reconciliation DB↔wallet (après live)
- [ ] Daily snapshot backup DB vers S3/B2

## 🎯 Ordre recommandé prochaine session

### Session A : ERA5 + DRN (2-3h)
Si user a setup Copernicus :
1. `uv run scripts/backfill_era5.py --years 2` (test petit d'abord)
2. `uv run scripts/train_drn.py --epochs 100`
3. Évaluer val CRPS
4. Scale à 5 ans si OK
5. Wire DRN dans model_prob.py (feature flag)

### Session B : Live validation (1-2h)
Si paper shadow accumulé :
1. Check `signal_outcomes` resolved count
2. `uv run scripts/reconcile_and_report.py`
3. Review drift
4. Adjust filter thresholds si besoin

### Session C : Foundation models (3-4h)
Si DRN trained et stable :
1. Download Pangu ONNX (1GB)
2. `onnxruntime` inference local
3. Intégrer comme source NWP
4. Benchmark vs AIFS + DRN

### Session D : Live execution (SI user ready, 2-3h)
Si paper shadow validé + user autorise :
1. `uv add py-clob-client`
2. Wire dans `order_manager.py`
3. Dry-run testnet Polygon Mumbai
4. Live $100 test trade
5. Si OK, start $500 auto

## 🛑 Ne jamais faire sans autorisation explicite

- Submit real orders avec money réel
- Modify wallet
- Push force sur git
- Skip paper shadow avant real money
- Over-promise ROI sans caveats

## Related

- [[STATE-HANDOFF|State complet]]
- [[_MOC|Hub principal]]
- [[roadmap|Roadmap phases classique]]
- [[deep-learning-roadmap|Deep Learning roadmap]]
- [[execution-playbook|Execution playbook 16 dimensions]]
