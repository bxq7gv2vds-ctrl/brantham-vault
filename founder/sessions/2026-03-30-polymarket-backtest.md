---
title: Polymarket Hedge Engine — Backtest System Complete
date: 2026-03-30
project: polymarket-hedge
tags: [backtest, optuna, bracket-arb, nwp, polymarket]
---

# Session: Polymarket Backtest System — March 30

## What was built

Full historical backtest pipeline for the Polymarket intraday hedge engine:

### Infrastructure
- `src/pmhedge/backtest/data_downloader.py` — downloads Polymarket weather markets + CLOB price bars + Open-Meteo NWP forecasts
- `src/pmhedge/backtest/event_stream.py` — chronological stream of PriceEvent + NWPJumpEvent
- `src/pmhedge/backtest/backtester.py` — deterministic simulation engine
- `src/pmhedge/backtest/metrics.py` — Sharpe, Sortino, Calmar, profit factor
- `src/pmhedge/backtest/report.py` — rich console reports
- `src/pmhedge/backtest/optimizer.py` — Optuna walk-forward optimization
- `scripts/run_backtest.py` — CLI entry point
- `scripts/run_optimizer.py` — optimization CLI

### Key Bugs Fixed

1. **CLOB API data availability**: `interval=1m` only returns data 1 month back. Markets older than 1 month have no CLOB data. Fix: use recent markets (offset ≥ 1700 in Gamma API pagination).

2. **Gamma API endpoint**: `/markets?tag_slug=weather` returns 0 results. Must use `/events?tag_slug=weather` and parse `markets[]` array inside each event.

3. **NWP p_fundamental always 0.5**: All GFS runs gave identical p_fundamental → zero NWP_JUMP events. Fix: use multi-day lead approach (T-5 to T) — each day's forecast for target_date differs as the date approaches.

4. **NWP run-to-run evolution**: Open-Meteo `_seamless` models give ONE blended value per day — identical across all 4 daily GFS runs. Fix: use daily snapshots (one per calendar day for 5 days before target) to capture day-to-day forecast evolution.

5. **BRACKET_ARB never fires**: Signal was only triggered during NWP_JUMP events. With no NWP events, no arb either. Fix: also scan BRACKET_ARB every 50 price events.

6. **p_fundamental recomputation**: Event stream p_old/p_new were proxy values — backtester now recomputes per-market p using actual threshold + direction via normal CDF (or EMOS).

7. **NWP avail_hours bug**: Originally used only hours ≥ run_hour for each GFS run, causing artificial downward temperature bias (18Z run using only hours 18-23 misses afternoon peak). Fix: always use all 24 hours.

### Backtest Results (March 2026, params optimized via Optuna 100 trials)

| Metric | Value |
|--------|-------|
| Sharpe ratio | 19.6 |
| Win rate | 48.5% |
| Max drawdown | 0.16% |
| Total trades | 410 |
| BRACKET_ARB win rate | 63.4% |
| NWP_JUMP win rate | 21.4% |
| Total P&L | +7,099 USDC |
| Avg daily P&L | +473 USDC |
| Positive days | 13/15 |

### Optimized Parameters (config/best_params.json)

```json
{
  "min_edge": 0.030,
  "kelly_fraction": 0.40,
  "nwp_jump_ttl_min": 69,
  "bracket_arb_ttl_min": 152,
  "max_pos_pct": 0.026,
  "max_total_exposure_pct": 0.35
}
```

## Key Insights

1. **BRACKET_ARB is the dominant signal** (63% win rate vs 21% for NWP_JUMP). Temperature bracket markets often have sum ≠ 1.0, creating persistent arb opportunities.

2. **NWP signal is directionally correct** after fixing the bugs. 21% win rate (vs 4.4% pre-fix) with avg win > avg loss ratio of ~4.5x → profitable overall.

3. **CLOB data only goes back ~30-45 days**. For "huge" historical backtests, we'd need to collect data over time or use Polymarket's data export at data.polymarket.com.

4. **Weather market structure**: 9 brackets per city+date (e.g., "≤5°C", "6°C", "7°C", ..., "≥12°C"). Sum should = 1.0 but rarely does intraday.

## Data Coverage

- **Markets**: 738 (March 3-20, 2026)
- **Cities**: London, New York, Seattle, Atlanta, Chicago, Dallas, Miami
- **Price bars**: 206,756 (10-minute resolution)
- **NWP snapshots**: 1,968 (82 city+dates × 5 days × 4 runs)
- **DB**: `backtest_data.db` at project root

## Next Steps

1. Deploy live TUI: `uv run scripts/run_hedge.py`
2. Configure `.env`: `TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID`
3. Let live engine collect real tick data for 2-4 weeks
4. Re-run backtest monthly with fresh downloaded data
5. Add `microstructure.py` for order flow calibration after live data
6. Investigate MEAN_REVERT signal (currently 0 trades — z_entry threshold may be too high)

## Related

- [[polymarket-hedge engine session]] — previous session (TUI completion)
- [[vault/patterns/polymarket-nwp-emos-calibration]]
- [[vault/patterns/polymarket-intraday-architecture]]
- [[vault/founder/decisions/2026-03-29-polymarket-intraday-vs-fundamental]]
