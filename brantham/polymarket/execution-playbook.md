---
name: Execution Playbook — Tout Optimiser
description: Playbook exhaustif des 16 dimensions d'optimisation d'exécution pour un hedge fund grade Polymarket
type: playbook
created: 2026-04-17
tags: [polymarket, execution, optimization, latency, risk, infra]
---

# Execution Playbook — Tout Optimiser

Reference exhaustive des 16 dimensions d'optimisation. Check-list à revisiter par phase de déploiement (paper → small live → scale).

## A. Latency Stack (signal → fill)

**Target** : < 500ms P99 end-to-end

```
Signal Gen (10ms) → Risk Check (2ms) → Order Build (5ms) →
Sign TX (20ms) → Submit WS (50ms) → Match (100ms) → Confirm (50ms)
```

### Checklist
- [x] Latency profiler instrumenté (`src/pmhedge/execution/latency.py`)
- [x] P50/P95/P99 per step sauvé en DB (`latency_samples`)
- [ ] Pre-compute forecasts offline (cron 6h → lookup <1ms au scan)
- [ ] Template orders pré-buildés (nonce management)
- [ ] Signature locale ecdsa-native (pas RPC remote)
- [ ] WebSocket persistent (auto-reconnect, ping 20s)
- [ ] DNS pre-resolution (cache endpoint IPs)
- [ ] HTTP/2 multiplex (REST fallback)

### Mesure
```bash
# Real-time latency report
uv run python -c "from pmhedge.execution.latency import report_markdown; print(report_markdown())"
```

## B. Order Strategy

**Default : post-only limit** → garantit maker (0% fees)

| Type | Use case | Cost | Status |
|---|---|---|---|
| post-only limit | Default entry | 0% fees | ✅ scaffold |
| limit at mid | Thin book | Spread | ✅ fallback |
| IOC | Time-sensitive | Partial ok | ✅ enum |
| FOK | Arbitrage all-or-nothing | Miss common | ✅ enum |
| market | Emergency exit | ~5c slippage | ✅ enum |
| cancel-replace >2c drift | Price chased | Re-queue | ✅ logic |
| iceberg split | Large size | Reduce impact | ⏳ todo |

### Module
`src/pmhedge/execution/order_manager.py` — `OrderManager` + `OrderIntent` + `TimeInForce`

### Checklist
- [x] Post-only flag support
- [x] Cancel-replace sur mid drift > 2c
- [x] Max replaces cap (3)
- [x] Patience timeout (30s default)
- [ ] Iceberg splitting (> $200 orders)
- [ ] py-clob-client integration (live wiring)
- [ ] Order ID reconciliation (DB ↔ exchange)

## C. Network Infrastructure

- [ ] Multi-RPC Polygon : Infura + Alchemy + own node
- [x] WebSocket CLOB orderbook client (`alpha/orderbook.py`)
- [ ] Persistent WebSocket launchd daemon
- [x] REST fallback (`fetch_orderbook_rest`)
- [ ] AWS us-east-1 VPS (future, proche Polymarket nodes)
- [ ] Hetzner EU backup (95.216.198.143 existant)

### Check RPC health
```bash
uv run python -c "
import aiohttp, asyncio, time
async def ping(url):
    t0 = time.time()
    async with aiohttp.ClientSession() as s:
        async with s.post(url, json={'jsonrpc':'2.0','method':'eth_blockNumber','params':[],'id':1}) as r:
            await r.json()
    return (time.time() - t0) * 1000
for url in ['https://polygon-rpc.com', 'https://rpc.ankr.com/polygon']:
    print(f'{url}: {asyncio.run(ping(url)):.0f}ms')
"
```

## D. Fill Optimization

- [x] L2 orderbook tracking continu
- [x] Best bid/ask en temps réel (via WebSocket)
- [x] Slippage learner per market (`execution/slippage.py`)
- [ ] Sizing ≤ 30% visible depth (dynamic cap)
- [ ] Routage maker preference (post-only default)
- [ ] Smart order routing (multi-venue future)

### Slippage stats
```bash
uv run python -c "from pmhedge.execution.slippage import global_stats; print(global_stats())"
```

## E. Real-time Risk

| Trigger | Action | Status |
|---|---|---|
| Per-trade cap $50 | Reject | ✅ |
| Per-city 20% bankroll | Skip city | ✅ |
| Per-day loss 10% | **Kill jour** | ✅ |
| Realized WR < expected -5pts | **Kill model** | ⏳ partial |
| Data freshness DOWN | **Pause global** | ✅ |
| RPC latency >500ms | **Failover RPC** | ⏳ |
| Position drift DB↔wallet | Alert + pause | ⏳ |

### Module
`src/pmhedge/alpha/risk_manager.py` — `RiskConfig` + `evaluate_batch`

## F. Monitoring + Alerting

### Dashboard
`src/pmhedge/execution/dashboard.py` — FastAPI + SSE, port 8080
```bash
uv run python -m pmhedge.execution.dashboard
# → http://localhost:8080/
```

### Prometheus metrics
`src/pmhedge/execution/metrics.py` — port 9090
```bash
uv run python -m pmhedge.execution.metrics
# → http://localhost:9090/metrics
```

### Alerts Telegram (cascading)
- [x] CRITICAL : kill switch / data DOWN → instant Telegram
- [x] HIGH : signal édge >8% → Telegram avec détails
- [x] MED : daily P&L summary → Telegram 09:15 UTC
- [x] LOW : routine confirmations → logs only

## G. Model Inference Optim

- [x] MPS Metal backend (Mac M5 GPU)
- [ ] Pré-compute forecasts cron 6h (store in calibrated_probs)
- [ ] Cache P(T_max) TTL 1h (SQLite hot table)
- [ ] Batch DRN inference (N markets en 1 call)
- [ ] ONNX quantization foundation models (4-8x speedup)
- [x] DRN scaffold (`deep_learning/drn.py`)
- [x] Transformer scaffold (`deep_learning/transformer.py`)

## H. Data Pipeline Optim

- [x] Incremental NWP ingestion (delta via `ingested_ts`)
- [x] DB indexes sur (icao, target_date, run_ts)
- [ ] Parquet archive pour >30j data
- [ ] Redis in-memory cache (stations metadata + hot NWP)
- [ ] Compressed WAL rotation

## I. Cost Optimization

| Item | Limit | Current | Optim |
|---|---|---|---|
| Open-Meteo | 10k req/j gratuit | ~300/j | ✅ OK |
| Claude API | $ per call | 0 | Only edge>15% or size>$100 |
| Polymarket fees | 0% | 0 | ✅ N/A |
| Gas Polygon | ~$0.001/tx | — | ✅ negligible |
| Hetzner VPS | €20/mo | payé | ✅ |
| GPU cloud | optional | €0 | Mac MPS suffit pour maintenant |

## J. Reconciliation + Audit

- [x] Every trade persisted avec signal_id, fill_price, slippage, fees, ts
- [x] Paper shadow mode (`alpha/paper_shadow.py`)
- [x] Daily reconcile script (`scripts/reconcile_and_report.py`)
- [ ] Wallet balance vs DB matching (bloqué : pas de wallet yet)
- [ ] Tax lot tracking FIFO
- [ ] Position inconsistency detector

## K. Redundancy

- [ ] Primary VPS (AWS us-east-1 quand live)
- [x] Backup Hetzner (95.216.198.143 existant)
- [ ] DB replication WAL
- [ ] Daily snapshot backup (S3 ou B2)
- [x] Multi-fetch NWP sources (GEFS + ICON + ECMWF + HRRR + AIFS)

## L. Security

- [ ] Private key AES-256 encrypted
- [ ] Hardware wallet (Ledger) pour >$10k
- [ ] 2FA Polymarket account
- [x] Environnements séparés (paper / testnet / prod via env flags)
- [x] Audit logs via signal_log immutable

## M. Latency Measurement

### Current (measured via profiler)
Après `run_alpha_live.py --once` :
- `fetch_markets` : P99 ~2000ms (API bound)
- `ensure_nwp_fresh` : P99 ~5000ms (si fetching)
- `confirmed_scan` : P99 ~50ms
- `model_vs_market_batch` : P99 ~500ms pour 366 markets
- `risk_evaluate` : P99 ~10ms

### Target
- End-to-end : <500ms per scan (currently ~3-8s car API + NWP)
- Signal→fill (live) : <500ms P99

## N. Feedback Loop

- [x] Backtest continuous (`alpha_backtest.py`, `city_focused_backtest.py`)
- [ ] Paper shadow champion/challenger 7j
- [ ] A/B tests live (20% traffic)
- [ ] Monthly model retrain + event-triggered

## O. Tax / Compliance

- [x] Daily/weekly/monthly reports auto (`reconcile_and_report.py`)
- [ ] Tax lot tracking FIFO
- [ ] France flat tax 30% calc
- [ ] Possibly SAS corporate si scale

## P. Advanced (stretch)

- [ ] Own Polygon validator node (direct mempool)
- [ ] MEV protection (Flashbots-style si disponible)
- [ ] Multi-venue routing (Kalshi, Manifold, PolyMarket EU)
- [ ] LLM reasoning auto-escalation (Claude Opus on high-stakes)

## Prochaines actions priorisées par ROI

### ROI HIGH (à faire maintenant)
1. [x] Latency profiler + metrics (DONE)
2. [x] Order manager scaffold (DONE)
3. [x] Slippage learner (DONE)
4. [x] HTML dashboard (DONE)
5. [x] Prometheus exporter (DONE)
6. [ ] WS orderbook daemon launchd (5 min)
7. [ ] Multi-RPC fallback setup (15 min)

### ROI MED (après paper shadow validation)
8. [ ] ERA5 + DRN training (jours, bloqué user)
9. [ ] py-clob-client live integration (bloqué : user auth + capital)
10. [ ] Batch inference + caching
11. [ ] Pre-compute forecasts cron

### ROI LOW (stretch, quand profitable)
12. [ ] GPU cloud pour Transformer/Diffusion
13. [ ] AWS colocation
14. [ ] Hardware wallet
15. [ ] Multi-venue routing

## Related

- [[_MOC|Polymarket Hub]]
- [[architecture|Architecture]]
- [[deep-learning-roadmap|Deep Learning Roadmap]]
- [[quick-start|Quick-start]]
