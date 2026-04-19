---
name: Monte Carlo Bootstrap P&L
description: Resampled annual P&L distribution from empirical daily P&L series
generated: 2026-04-19T16:57:10.124760+00:00
type: report
---

# Monte Carlo Bootstrap P&L

Source: 2 distinct days of paper P&L, block size 5d, horizon 250d, N_boot = 3000.

## Annual P&L distribution

| quantile | value |
|----------|-------|
| p05  | $+109687 |
| p25  | $+112040 |
| p50  | $+114393 |
| p75  | $+115961 |
| p95  | $+119098 |
| mean | $+114353 |

**Prob(positive year)** : 100.0 %

## Tail risk (annual)

- **VaR 95** = $-109687
- **VaR 99** = $-107335
- **Max DD p50** = $0
- **Max DD p95** = $0
- **Max DD p99** = $0

## Sharpe distribution (annualised)

- p05 = 21.36
- p50 = 22.25
- p95 = 23.19
- mean = 22.25

## Caveats

- Based on paper-shadow P&L (no slippage), likely overstates live.
- Only 2 distinct days in history — bootstrap adds uncertainty but can't capture regimes we haven't seen.
- Assumes stationarity of the daily return distribution.

## Related
- [[_MOC|Polymarket Hub]]
- [[audit-hedge-fund-grade|Audit]]
- [[sessions/2026-04-19-hedge-fund-grade-upgrades|Session 2026-04-19]]
