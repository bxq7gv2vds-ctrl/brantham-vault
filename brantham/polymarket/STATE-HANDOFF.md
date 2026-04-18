---
name: State Handoff — Polymarket Hedge Fund
description: Document de transmission complet pour prochaine session — tout ce qu'il faut savoir pour reprendre sans perte de contexte
type: handoff
created: 2026-04-18
tags: [polymarket, handoff, state, continuity]
priority: critical
---

# 📋 State Handoff — Polymarket Hedge Fund

**À LIRE EN PRIORITÉ dans toute nouvelle session** — ce doc + [[_MOC]] = state complet.

## TL;DR système actuel

**Status** : Pipeline hedge fund grade opérationnel en paper shadow autonome.
- 7 sessions de dev le 2026-04-17 (~8h marathon)
- ~6,000 lignes Python + ~5,000 lignes markdown vault
- 5 commits git sur main
- 5 launchd jobs autonomous
- Pas encore de capital réel déployé

**Next milestone** : Paper shadow 7-30 jours validation avant real money.

## Architecture état actuel

```
Layer 1 DATA HUB        → ✅ 3,919 NWP forecasts, 1,465 METAR obs, 46 stations
Layer 2 MODEL HUB       → ✅ EMOS + BMA (passthrough), DRN/Transformer scaffolds
Layer 3 ALPHA LAYERS    → ✅ CONFIRMED + MODEL_VS_MARKET + sum_arb + city_strategies
Layer 4 RISK            → ✅ Kelly correlation + kill switch + per-city caps
Layer 5 EXECUTION       → ✅ latency profiler + order_manager + slippage + dashboard
Layer 6 VALIDATION      → ✅ paper_shadow + reconcile + drift monitor
Layer 7 MONITORING      → ✅ Prometheus + HTML dashboard + Telegram
```

## Modules livrés

### `src/pmhedge/alpha/` (18 modules)
- `data_hub.py` — schema DB unifié + writers/readers
- `nwp_sources.py` — multi-source (GEFS+ICON+ECMWF+HRRR+ICON-EU+AIFS)
- `metar_archive.py` — 30-day rolling archive
- `orderbook.py` — Polymarket CLOB WebSocket + REST
- `polymarket_client.py` — Gamma API parser
- `freshness.py` — health monitor + kill switch
- `emos.py` — Gneiting 2005 calibration
- `bma.py` — Bayesian Model Averaging
- `model_prob.py` — pipeline EMOS+BMA → P(T_max)
- `signal_generator.py` — MODEL_VS_MARKET alpha
- `confirmed_oracle.py` — CONFIRMED_YES/NO alpha
- `sum_arb.py` — sum-to-1 scanner
- `risk_manager.py` — correlation Kelly + caps
- `paper_shadow.py` — validation mode
- `city_strategies.py` — 10 profils (Mexico City Kelly 0.82)
- `edge_filter.py` — pocket registry (via src/pmhedge/strategy/)
- `metrics.py` — Sharpe/Sortino/Calmar/VaR
- `backtest.py` — unified engine + walk-forward
- `report.py` — markdown reports
- `xgboost_post.py` — XGBoost skeleton

### `src/pmhedge/deep_learning/` (4 modules)
- `drn.py` — Distributional Regression Network (PyTorch MPS)
- `transformer.py` — Temporal transformer (27K params)
- `ppo_execution.py` — PPO RL agent scaffold
- `llm_reasoning.py` — Claude API rare-event detection

### `src/pmhedge/execution/` (5 modules)
- `latency.py` — profiler P50/P95/P99 persisté DB
- `slippage.py` — EMA per-market learner
- `order_manager.py` — post-only + cancel-replace
- `metrics.py` — Prometheus exporter :9090
- `dashboard.py` — FastAPI + SSE HTML :8080

### Scripts opérationnels (~15)
Dans `/Users/paul/polymarket-hedge/scripts/` :
- `seed_stations.py` — 46 stations seeded
- `ingest_nwp_daily.py` — cron 4x/jour ingestion
- `archive_metar.py` — cron 2h rolling archive
- `populate_market_resolutions.py` — 1,886 resolutions backfilled
- `health_check.py` — 15min cron + Telegram
- `run_alpha_live.py` — **main orchestrator continuous (KeepAlive)**
- `backfill_era5.py` — ERA5 download (bloqué user)
- `alpha_backtest.py` — unified backtest CLI
- `reconcile_and_report.py` — daily 09:15 cron
- `train_xgboost_post.py` — XGBoost training (bloqué ERA5)
- `train_drn.py` — DRN training (bloqué ERA5)
- `city_focused_backtest.py` — Top 10 villes projection
- `debug_unknown_pocket.py`, `backtest_edge_filter*.py`

### Launchd jobs autonomes (5 actifs)

```
~/Library/LaunchAgents/com.paul.polymarket-alpha-*.plist
```

| Job | Fréquence | Action |
|---|---|---|
| alpha-live-runner | KeepAlive (loop 300s) | Scan + signals |
| alpha-nwp-ingest | 4x/jour 01:30/07:30/13:30/19:30 | NWP ingestion |
| alpha-metar-archive | Every 2h | METAR rolling |
| alpha-health-check | Every 15min | Telegram alerts |
| alpha-reconcile | Daily 09:15 | Paper shadow report |

Copies versionnées : `deploy/launchd-alpha/*.plist`

## Git commits (5)

```
596ad78 feat(alpha): hedge fund grade architecture (18 modules)
7535278 fix(alpha): quality gates + city_strategies integration
8b34917 ops(launchd): alpha subsystem cron jobs (5 plists)
e3dfcbc feat(deep-learning): DRN + Transformer + PPO + LLM + AIFS
XXXXXXX feat(execution): latency + orders + slippage + metrics + dashboard
```

## Databases

| DB | Path | Rows clés |
|---|---|---|
| `bracket_scalper_trades.db` | /Users/paul/polymarket-hedge/ | 6,740 paper trades settled |
| `alpha_data_hub.db` | /Users/paul/polymarket-hedge/ | 46 stations, 3,919 NWP, signal_log |
| `pmhedge.db` | /Users/paul/polymarket-hedge/ | 1,886 market_resolutions |
| `all_markets.db` | /Users/paul/polymarket-hedge/ | 22k markets, 702k price_bars |
| `emos_cache.db` | /Users/paul/polymarket-hedge/ | 468 EMOS params (legacy) |

## Résultats backtest paper (2026-04-17)

**City-focused backtest, bankroll $10k, 10.5 jours** :
- Total N=475 trades, P&L +$3,557 (ROI 6.34%)
- **Annuel extrapolé : $728,438** (paper naïf)
- **Réaliste ÷5 : $145,688/an** (1,458% ROI)
- **Très bearish ÷10 : $72,844/an** (728% ROI)

**Top 5 villes** :
1. Denver : $238k/an (WR 99.2%, 127 trades)
2. Mexico City : $228k/an (WR 98.3%, Kelly 0.82)
3. Madrid : $172k/an (WR 90.9%)
4. Miami : $46k/an (WR 100%)
5. San Francisco : $20k/an (WR 100%)

**Live scan récent** : 366 markets → 18 candidats → 10 approved → $169 exposure sur $1k bankroll.

## Bloquants utilisateur (priorité ordre)

### 🔴 CRITIQUE (bloque Phase ML)
1. **Compte Copernicus CDS** — https://cds.climate.copernicus.eu/
   - Créer compte
   - Accepter license ERA5 hourly single levels
   - Créer `~/.cdsapirc` :
     ```
     url: https://cds.climate.copernicus.eu/api
     key: <UID>:<TOKEN>
     ```

### 🟡 POUR LIVE EXECUTION (bloque real money)
2. **Polymarket wallet funded** — $500-1000 initial
3. **Private key** dans `.env` :
   ```
   POLY_PRIVATE_KEY=0x...
   POLY_API_KEY=... (optional for rebates)
   ```
4. **py-clob-client install** : `uv add py-clob-client`

### 🟢 NICE-TO-HAVE
5. **ANTHROPIC_API_KEY** env — pour LLM reasoning live
6. **Hetzner GPU** €200/mo pour Transformer training scale
7. **AWS us-east-1 VPS** pour latency colocation (quand >$10k capital)

## Tasks pending (next session)

### Phase ML (dépend ERA5)
- [ ] `backfill_era5.py --years 5` (~1-3h download)
- [ ] `train_drn.py` → models/drn.pt
- [ ] `train_xgboost_post.py` → models/xgb_postproc_*.json
- [ ] A/B test DRN vs EMOS sur paper shadow 7j
- [ ] Swap EMOS → DRN dans `model_prob.py` (feature flag)
- [ ] Transformer training (Mac MPS ~5-10h ou GPU cloud)
- [ ] Meta-learning regime-aware model selector
- [ ] MLflow experiment tracking
- [ ] Feature store (Feast ou custom SQLite)
- [ ] Diffusion model GenCast-style (stretch)

### Phase Execution
- [ ] **Pre-compute forecasts cron** (6h interval) — scan latency <200ms
- [ ] **Batch inference module** (multi-market 1 call)
- [ ] **Model inference caching TTL 1h** (SQLite hot table)
- [ ] **Multi-RPC supervisor** Polygon (Infura + Alchemy + own)
- [ ] **WS orderbook daemon launchd** (continuous 24/7)
- [ ] **py-clob-client live integration** (après user auth)
- [ ] Hardware wallet Ledger integration
- [ ] AWS us-east-1 deployment
- [ ] Grafana + Prometheus stack (Docker compose)

### Phase Monitoring
- [ ] Daily auto-report vers vault/brantham/polymarket/reports/YYYY-MM-DD.md
- [ ] Weekly review script (vendredi soir)
- [ ] Drift alert si WR drift >5pts
- [ ] P&L candlestick historical tracking

### Phase Universe expansion
- [ ] Sport markets (NBA, soccer)
- [ ] Crypto markets (BTC price brackets)
- [ ] Politics markets
- [ ] Multi-venue routing (Kalshi, Manifold)

### Phase Edge discovery
- [ ] Pangu-Weather ONNX inference local
- [ ] GraphCast via Google
- [ ] Foundation model Aurora (Microsoft, stretch)
- [ ] Radar MRMS nowcast <6h
- [ ] Cross-market pairs stat-arb NYC↔Boston
- [ ] Orderbook imbalance microstructure alpha

## Commandes essentielles

### Status quotidien
```bash
# Santé du système
uv run scripts/health_check.py

# Vérifier launchd
launchctl list | grep polymarket-alpha

# Dashboard live
uv run python -m pmhedge.execution.dashboard  # http://localhost:8080

# Metrics Prometheus
uv run python -m pmhedge.execution.metrics  # http://localhost:9090/metrics

# Reconcile + daily report
uv run scripts/reconcile_and_report.py --alert
```

### Query DB
```bash
# Signaux émis aujourd'hui
sqlite3 /Users/paul/polymarket-hedge/alpha_data_hub.db "
SELECT alpha_type, side, entry_price, est_prob, edge, size_usdc
FROM signal_log WHERE emit_ts >= strftime('%s','now','start of day')
ORDER BY emit_ts DESC LIMIT 20;"

# NWP freshness
sqlite3 /Users/paul/polymarket-hedge/alpha_data_hub.db "
SELECT source, status, datetime(last_success,'unixepoch') FROM data_freshness;"

# Top cities all-time P&L
sqlite3 /Users/paul/polymarket-hedge/bracket_scalper_trades.db "
SELECT city, COUNT(*) n, ROUND(SUM(pnl),2) pnl
FROM scalper_signals WHERE resolved=1 GROUP BY city ORDER BY pnl DESC LIMIT 10;"

# Latency stats live
uv run python -c "from pmhedge.execution.latency import report_markdown; print(report_markdown())"
```

### Backtest
```bash
uv run scripts/alpha_backtest.py --bankroll 10000
uv run scripts/city_focused_backtest.py --bankroll 10000
```

### Scan manuel
```bash
uv run scripts/run_alpha_live.py --once --no-telegram --min-edge 0.04 --bankroll 1000
```

## Structure vault (cross-linked wikilinks)

```
vault/brantham/polymarket/
├── _MOC.md                    (INDEX principal)
├── STATE-HANDOFF.md           (ce doc — PRIORITÉ)
├── architecture.md            (4 couches classique)
├── deep-learning-roadmap.md   (7 couches SOTA)
├── execution-playbook.md      (16 dimensions opti)
├── quick-start.md             (commandes pratiques)
├── data-sources.md            (inventaire par région)
├── findings.md                (diagnostics edges)
├── decisions.md               (15 décisions archi)
├── questions.md               (93 questions framework)
├── roadmap.md                 (phases 0-5 classique)
├── sessions/
│   ├── 2026-04-17-diagnostic-and-alpha-engine.md    (#1)
│   ├── 2026-04-17-phase1-data-foundation.md         (#2)
│   ├── 2026-04-17-phase1-live-runner.md             (#3)
│   ├── 2026-04-17-phase1-risk-orderbook.md          (#4)
│   ├── 2026-04-17-phase2-completion.md              (#5)
│   ├── 2026-04-17-city-focused-analysis.md          (#6)
│   └── 2026-04-17-deep-learning-foundation.md       (#7)
├── reports/
│   ├── city-focused-projection-2026-04-17.md
│   ├── alpha-backtest-2026-04-17.md
│   ├── alpha-backtest-2026-04-17.trades.csv
│   └── paper-2026-04-17.md
├── backtest-results/ (future)
└── data-sources/ (future)
```

## Commandes prochaine session (priorité)

Quand tu reprends, check cet ordre :

```bash
# 1. Status launchd
launchctl list | grep polymarket-alpha

# 2. Logs récents
tail -50 /Users/paul/polymarket-hedge/logs/alpha-live.log
tail -20 /Users/paul/polymarket-hedge/logs/alpha-health.log

# 3. Count signals last 24h
sqlite3 /Users/paul/polymarket-hedge/alpha_data_hub.db \
  "SELECT COUNT(*) FROM signal_log WHERE emit_ts >= strftime('%s','now') - 86400;"

# 4. Latency observée
uv run python -c "from pmhedge.execution.latency import report_markdown; print(report_markdown())"

# 5. Paper shadow resolved count
sqlite3 /Users/paul/polymarket-hedge/alpha_data_hub.db \
  "SELECT COUNT(*) FROM signal_outcomes;" 2>/dev/null || echo "0 resolved yet"
```

## Contexte business

- **Projet parent** : Brantham Partners (M&A distressed PME France)
- **Polymarket = side project trading** — objectif capital personnel
- **Paul Roulleau** : tech/product, 1 personne sur ce projet
- **Location** : `/Users/paul/polymarket-hedge/`
- **Email** : paul.roulleau@branthampartners.fr
- **Jurisdiction** : France (Polymarket bloqué US, OK EU avec compliance)
- **Tolérance risque** : small start $500-1k → scale si valide

## Métriques success

### Paper shadow phase (maintenant → +30j)
- [ ] Drift < 5 pts (realized WR vs expected)
- [ ] Signaux émis régulièrement (>5/jour)
- [ ] Health check 100% OK
- [ ] Sum-arb detecté (si actif après CLOB WS daemon)

### Live small phase (mois 2-3)
- [ ] $500 real capital deployed
- [ ] 7j first trades OK (no systemic bugs)
- [ ] Slippage < 200bps mediane
- [ ] Daily P&L positive >50% des jours

### Scale phase (mois 4+)
- [ ] $10k bankroll
- [ ] $75-150k/an run-rate (réaliste)
- [ ] ML stack (DRN) beats EMOS baseline

## Si quelque chose casse

### Live runner crash
```bash
launchctl unload ~/Library/LaunchAgents/com.paul.polymarket-alpha-live-runner.plist
launchctl load ~/Library/LaunchAgents/com.paul.polymarket-alpha-live-runner.plist
tail -100 /Users/paul/polymarket-hedge/logs/alpha-live.log
```

### NWP source DOWN
- Open-Meteo down → scan continues avec cached data
- METAR down → t_max_prev_utc_day unavailable → CONFIRMED skip
- AIFS down → fallback sur autres sources dans ensemble

### Signal aberrant
- max_edge cap = 0.40 déjà actif
- min_ensemble_members = 20 actif
- Edit `src/pmhedge/alpha/signal_generator.py` `SignalGenConfig` pour ajuster

### DB lock/corruption
- `alpha_data_hub.db` : WAL mode, automatic recovery
- Backup quotidien recommandé : `cp alpha_data_hub.db backups/$(date +%F).db`

## Contacts + liens externes

- Polymarket docs : https://docs.polymarket.com/
- Open-Meteo API : https://open-meteo.com/en/docs
- Copernicus CDS : https://cds.climate.copernicus.eu/
- NOAA NOMADS : https://nomads.ncep.noaa.gov/
- Telegram bot : check `.env` `TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID`

## Instructions pour prochaine session Claude

**Au démarrage** :
1. Lire ce doc STATE-HANDOFF.md en premier
2. Lire [[_MOC|Polymarket Hub MOC]]
3. Check launchd status + logs récents
4. Demander user : as-tu fait ERA5 setup ? as-tu des questions ?

**Priorités immédiates** :
1. Vérifier que le système tourne (launchd + logs)
2. Compter les signaux 24h (si <10, debug)
3. Check paper shadow resolved count (devrait augmenter)
4. Si rien cassé → continuer roadmap ML (Phase 2)

**Ne PAS** :
- Refaire le diagnostic (déjà fait dans findings.md)
- Recréer les modules alpha/ (déjà livrés)
- Demander à l'utilisateur des infos déjà dans ce doc

## Related

- [[_MOC|Polymarket Hub (index)]]
- [[architecture|Architecture classique]]
- [[deep-learning-roadmap|Deep Learning Roadmap]]
- [[execution-playbook|Execution Playbook]]
- [[quick-start|Quick-start opérationnel]]
- [[findings|Findings diagnostic]]
- [[decisions|Décisions archi]]
- [[roadmap|Roadmap phases]]
