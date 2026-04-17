---
name: Session 2026-04-17 Phase 1 — CLOB Orderbook + Risk Manager + ERA5
description: CLOB WebSocket orderbook client, Risk manager correlation-adjusted, ERA5 downloader — Phase 1 completion
type: session
date: 2026-04-17
tags: [polymarket, session, orderbook, risk, era5]
---

# Session 2026-04-17 — CLOB Orderbook + Risk Manager + ERA5

4e session. Finalise Phase 1 Data Foundation.

## Ce qui a été livré

### CLOB Orderbook (task 18 ✅)

**`src/pmhedge/alpha/orderbook.py`** (230 lignes)
- `OrderBook` dataclass : état L2 (bids/asks dict price→size), best_bid/ask, depth USDC
- `OrderbookClient` : WebSocket client async avec auto-reconnect
  - Subscribe sur `book` channel pour liste de token_ids
  - Handle messages `book` (full refresh) + `price_change` (L2 delta)
  - Persist snapshots périodique (30s default)
  - Freshness tracking
- `fetch_orderbook_rest` : REST fallback one-shot pour ad-hoc queries

**Test REST validé** : token test → bid 0.620, ask 0.650, mid 0.635, depth $149 bid / $78 ask dans 5c

### Risk Manager correlation-adjusted (tasks 13, 24 ✅)

**`src/pmhedge/alpha/risk_manager.py`** (210 lignes)

Logic :
1. **Kill switch** : daily PnL ≤ -10% bankroll → block all
2. **Per-signal cap** : max 5% bankroll per trade
3. **Per-city cap** : max 1 position par ville
4. **Total exposure cap** : max 60% bankroll
5. **Correlation adjustment** : scale down by √(1 + (N-1)·ρ_avg) avec ρ basé sur régions
6. **Min position** : $5 USDC

Régions (12 groupes) : US_EAST, US_WEST, CA, EU_WEST, EU_CENTRAL, EU_EAST, CN, JP_KR, TW_SEA, IN_ME, LATAM, OCEANIA.

Corrélations : même ville=1.0, même région=0.5, même hémisphère=0.3, sinon=0.1.

**Test live** :
- 29 candidates → 15 approved (14 coupés par per-city cap)
- Total exposure $212 (21% vs 60% max)
- Portfolio factor 0.35 (bon — diversifie sur 15 villes)
- Size $15/trade (descended de $50 via correlation factor)

### ERA5 downloader (task 17 ✅)

**`scripts/backfill_era5.py`** (130 lignes)
- Requires cdsapi + xarray + netCDF4 (à installer) + Copernicus account + ~/.cdsapirc
- Downloads 2m_temperature hourly pour 40+ stations × N années
- Tiny spatial box (0.2° × 0.2°) autour de chaque station → minuscule storage
- Extract T_max UTC day → `obs_temperature` table avec source='ERA5'
- Script fail-fast avec instructions si prereq manquant

**À lancer** :
```bash
uv add cdsapi xarray netCDF4
# Setup ~/.cdsapirc
uv run scripts/backfill_era5.py --years 5     # ~1-3h download
```

## Pipeline complet fonctionnel

```
                   Polymarket /public-search
                           ↓
           368 bracket markets (43 cities)
                           ↓
    ensure_nwp_fresh → 1218-2701 NWP rows/scan
                           ↓
   model_prob.forecast (EMOS + BMA, 71 members)
                           ↓
   signal_generator.generate_signal (edge filter)
                           ↓
         29 candidate signals
                           ↓
   risk_manager.evaluate_batch
   (kill switch + per-city + correlation + caps)
                           ↓
      15 approved signals ($15 each)
                           ↓
        persist_signal + signal_log
                           ↓
    [Telegram alerts pour edges ≥ 8%]
```

## Observations de cette session

### Edges observés (live scan 2026-04-17)

Top 10 approved :
1. YES @0.102 edge +0.895 (TRÈS suspect, model=1.0)
2. NO @0.570 edge +0.430
3. NO @0.595 edge +0.405
4. NO @0.635 edge +0.316
5. NO @0.815 edge +0.176
6. NO @0.845 edge +0.146
7. NO @0.845 edge +0.125
8. NO @0.855 edge +0.122
9. NO @0.825 edge +0.111
10. NO @0.785 edge +0.109

### Calibration à faire

- Edges > 30% = très suspects → flag et filtrer
- Edges 5-15% = réalistes, keep
- Cap max_edge=0.40 peut-être sain

### Bugs résiduels

1. Edges absurdes (>30%) pour certains markets — cause non identifiée (peut-être target_date decalage ?)
2. BMA weights non calibrés (passthrough defaults)
3. EMOS non calibrés (passthrough jusqu'à ERA5 download)
4. CLOB WebSocket non lancé en continu (orderbook_snapshots vide)

## Code total session 2026-04-17 (4 sessions)

| Session | Focus | Lignes Python |
|---|---|---|
| #1 diagnostic | EdgeFilter, backtest, metrics, report | ~1,600 |
| #2 data foundation | data_hub, nwp_sources, emos, bma, model_prob, signal_gen | ~1,560 |
| #3 live runner | metar_archive, freshness, polymarket_client, run_alpha_live | ~750 |
| #4 orderbook + risk + era5 | orderbook, risk_manager, backfill_era5 | ~570 |
| **Total Python** | | **~4,480** |
| **Markdown vault** | 8 docs + 4 session logs | ~3,200 |
| **Total** | | **~7,680** |

## Tasks final status (21/25 ✅)

**Done (21)** :
1-10, 12-16, 18-21, 23, 24, 13, 17

**Pending (4)** :
- 11 Debug CONFIRMED oracle
- 22 XGBoost post-proc (needs ERA5)
- 25 Paper shadow mode 30j

## Database state final

| Table | Rows | Status |
|---|---|---|
| stations | 46 | ✅ |
| nwp_forecasts | 3,919 | ✅ |
| nwp_ensemble_blend | 131 | ✅ |
| obs_temperature | 1,089 | ⚠️ need ERA5 backfill |
| orderbook_snapshots | 0 | ⏳ besoin WS live |
| signal_log | 34 | ✅ (15 from risk-mgr test) |
| market_resolutions | 1,886 | ✅ (from scalper_signals) |

## Next steps (Phase 2)

**Semaine prochaine** :
1. User setup : cdsapi + ~/.cdsapirc Copernicus
2. Lancer `backfill_era5.py --years 5` (1-3h)
3. Build EMOS training script sur ERA5 data
4. Build XGBoost post-proc (task 22)
5. Debug high-edge signals (filtres volume + freshness)
6. CLOB WebSocket en continu avec supervisor launchd

**Semaine +2** :
7. Paper shadow mode 30j (task 25)
8. Backtest avec ERA5 ground truth
9. Calibrate EMOS params live vs market

**Semaine +3** :
10. Deploy VPS AWS us-east-1
11. Live small capital ($500-1000)
12. Daily reconciliation backtest vs live

## Related

- [[_MOC|Polymarket Hub]]
- [[architecture|Architecture]]
- [[findings|Findings]]
- [[decisions|Decisions]]
- [[roadmap|Roadmap]]
- [[2026-04-17-diagnostic-and-alpha-engine|Session 1 — Diagnostic]]
- [[2026-04-17-phase1-data-foundation|Session 2 — Data Foundation]]
- [[2026-04-17-phase1-live-runner|Session 3 — Live Runner]]
