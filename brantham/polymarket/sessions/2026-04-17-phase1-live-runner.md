---
name: Session 2026-04-17 Phase 1 — Live Runner + Polymarket Client
description: Live alpha runner end-to-end opérationnel — fetch markets, ensure NWP fresh, generate signals, persist, alert
type: session
date: 2026-04-17
tags: [polymarket, session, live, runner]
---

# Session 2026-04-17 — Phase 1 Live Runner

3e session de la journée. Pipeline live end-to-end validé.

## Ce qui a été livré

### Modules nouveaux

**`src/pmhedge/alpha/metar_archive.py`** (90 lignes)
- `fetch_metar_history` : récupère 36h METAR via aviationweather.gov
- `archive_all_stations` : bulk archive pour toutes les stations
- `prune_older_than` : rolling window 30 jours
- `t_max_per_utc_day` : extract T_max pour un jour UTC donné

**`src/pmhedge/alpha/freshness.py`** (140 lignes)
- `check_metar` / `check_nwp` / `check_orderbook` / `check_stations`
- `HealthReport` avec kill switch flag
- `send_telegram` alert helper

**`src/pmhedge/alpha/polymarket_client.py`** (220 lignes)
- `fetch_active_bracket_markets` : Gamma public-search per-city (43 cities)
- `BracketMarket` dataclass avec parse question/slug → (icao, target_date, bracket_lo_c, bracket_hi_c)
- Parsing "X°C or below" et "X-Y°C" et "above X"

### Scripts opérationnels

- `scripts/archive_metar.py` — cron 2h, archive 30-day rolling ✅
- `scripts/health_check.py` — cron 15min, check + alert Telegram ✅
- `scripts/run_alpha_live.py` — main orchestrator ✅

### Test end-to-end LIVE 2026-04-17

```
[1/4] Fetching active Polymarket bracket markets...
  Found 368 active bracket markets across 43 cities

[2/4] Ensuring NWP freshness for 86 (station, date) pairs...
  Ingested 2,701 new NWP rows

[3/4] Generating signals (min_edge=0.030)...
  Emitted 19 signals

  Top signals:
    NO @0.570 model=1.000 edge=+0.430 size=$50   <-- suspicious high edge
    NO @0.595 model=1.000 edge=+0.405 size=$50
    NO @0.635 model=0.951 edge=+0.316 size=$50
    YES @0.003 model=0.183 edge=+0.180 size=$45
    NO @0.815 model=0.991 edge=+0.176 size=$50
    NO @0.145 model=0.292 edge=+0.147 size=$43
    NO @0.755 model=0.889 edge=+0.134 size=$50
    NO @0.715 model=0.845 edge=+0.130 size=$50
    NO @0.855 model=0.977 edge=+0.122 size=$50
    NO @0.960 model=1.000 edge=+0.040 size=$50
```

### Observations sur les edges

**Edges réalistes (3-18%)** : +4.0%, +4.0%, +6.9%, +12.2%, +13.4%, +13.0%, +14.7%, +17.6%, +18.0%
- μ=24-27°C, σ=1-2°C typical
- Market YES 0.74-0.96 → NO 0.04-0.26
- Model donne NO ≥ 99% → edge 3-15% cohérent

**Edges suspects (30-43%)** : 3 signaux à +30% à +43%
- Market YES 0.43-0.57 (donc NO 0.57-0.43)
- Model dit P(NO)=1.00
- **Soit bug parsing**, **soit marché vraiment mispricé**

Hypothèses à vérifier :
1. Target_date parsing incorrect pour ces markets (model predict day differ from market day)
2. Volume faible (markets "mortes" restées ouvertes)
3. Real mispricing (unlikely à 43%)

→ **Action** : pre-filter markets à volume ≥ $500 + exclude markets sans trade récent

### Calibration actuelle vs attendue

Sur 368 markets, 19 signaux (5% hit rate) — ratio plausible.
Vrais top traders probablement font 5-10% hit rate avec edges 3-7%.
Les edges >20% = red flag à debug.

## Tables DB utilisées / remplies

| Table | Rows | Status |
|---|---|---|
| stations | 46 | ✅ seeded |
| nwp_forecasts | 2,845 | ✅ populated (Paris + 85 others) |
| nwp_ensemble_blend | 89 | ✅ computed |
| obs_temperature | 1,089 | ✅ METAR 36h archived |
| orderbook_snapshots | 0 | ⏳ (CLOB WS à venir) |
| calibrated_probs | 0 | (computed on-the-fly) |
| signal_log | 19 | ✅ live signals persisted |
| trade_log | 0 | ⏳ (execution non branchée) |
| data_freshness | 1 | ✅ METAR tracked |

## Pipeline architecture validée

```
Gamma API /public-search (per-city)
     ↓ 368 bracket markets
BracketMarket parse (city, target_date, lo_c, hi_c, prices)
     ↓
ensure_nwp_fresh (trigger fetch if stale)
     ↓ 2,701 NWP rows
model_prob.forecast (EMOS + BMA blend)
     ↓ μ, σ per (icao, date)
signal_generator.generate_signal
     ↓ 19 signals
EdgeFilter + Kelly sizing
     ↓ sized signals
persist_signal → signal_log
     ↓
Telegram alert (high-edge only)
```

## Bugs & améliorations identifiés

1. **Edges > 20% non validés** : ajouter filtre volume + freshness prix
2. **Pas d'orderbook L2 réel** : mid-price approx uniquement
3. **Cache BMA weights** : charge emos_cache.db qui n'existe pas encore
4. **Slippage model** : pas encore calibré sur fills réels

## Total code session 2026-04-17 (3 sessions)

| Session | Focus | Lignes |
|---|---|---|
| #1 diagnostic + alpha engine | EdgeFilter, backtest, metrics, report | ~1,600 |
| #2 data foundation + model hub | data_hub, nwp_sources, emos, bma, model_prob, signal_gen | ~1,560 |
| #3 live runner | metar_archive, freshness, polymarket_client, run_alpha_live, archive_metar, health_check | ~750 |
| **Total** | | **~3,900** |

Plus ~2,500 lignes markdown dans le vault.

## Tasks status (15/25 complétées)

**Done** :
1. Diagnostic CONVEX_YES
2. Diagnostic EXACT_BIN_YES
3. Audit CERT_NO
4. Edges survivants segment
5. Stratégie edge #1
6. OOS validation + live integration
7. Alpha module architecture
8. Backtest engine
9. Metrics lib
10. Sum-to-1 arb scanner
12. market_resolutions backfill
14. HTML+MD reports
15. Data hub multi-NWP
16. METAR 30-day archive
19. Data freshness monitor
20. EMOS calibration module
21. BMA fusion
23. Unified signal generator

**Pending** :
11. Debug CONFIRMED oracle
13. Risk + kill switch layer
17. ERA5 historical downloader
18. Polymarket CLOB WebSocket
22. XGBoost post-proc
24. Risk manager correlation-adjusted
25. Paper shadow mode

## Next session priority

1. Debug high-edge signals (volume filter + freshness check)
2. ERA5 downloader (cdsapi, one-shot)
3. CLOB WebSocket orderbook (real bid/ask + depth)
4. Risk manager correlation-adjusted
5. Paper shadow mode 30j

## Related

- [[_MOC|Polymarket Hub]]
- [[architecture|Architecture]]
- [[findings|Findings]]
- [[decisions|Decisions]]
- [[roadmap|Roadmap]]
- [[2026-04-17-diagnostic-and-alpha-engine|Session 1]]
- [[2026-04-17-phase1-data-foundation|Session 2]]
