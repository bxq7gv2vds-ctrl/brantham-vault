---
name: Los Angeles — deep dive
description: Analyse empirique complète Polymarket weather. Performance, calibration, σ bias, TTR, top trades, verdict.
type: city-report
project: brantham/polymarket
date: 2026-04-21
verdict: KEEP
tags: [polymarket, city, los-angeles, keep]
---

# Los Angeles — deep dive

**Verdict: KEEP** — Steady: $471 on 121 trades

## Identité

- ICAO : `KLAX`
- Coords : 33.9425, -118.4081
- Country / TZ : US / America/Los_Angeles
- UTC offset : -7.0h
- Elevation : 39.0 m

## Configuration

- **Status** : ENABLED
- **Kelly fraction** : 0.5
- **N outcomes** : 121
- **Notes** : kelly from N=121 WR=96.7% (emp 0.840 → blended 0.500)
- **Updated** : 2026-04-21

## Calibrator (isotonic)

- N train : 84
- ECE before : 0.0565 → after : 0.0057
- Brier before : 0.0191 → after : 0.0129
- Fitted : 2026-04-21 02:20

## Performance empirique

- **Signaux émis** : 121
- **Outcomes réconciliés** : 121
- **P&L total** : +$471.13
- **Avg / trade** : +$3.89
- **WR** : 96.7%
- **Exposure cumulée** : +$2,398.51
- **Sharpe (ann.)** : 14.34
- **Daily P&L** : ['-$54.36', '+$121.46', '+$142.18', '+$261.85']

## Breakdown alpha × side × price bucket

| Alpha | Side | Bucket | N | P&L | Avg | WR |
|-------|------|--------|---|-----|-----|-----|
| MODEL_VS_MARKET | NO | ITM | 101 | +$465.12 | +$4.61 | 100.0% |
| MODEL_VS_MARKET | NO | mid | 10 | +$99.15 | +$9.92 | 100.0% |
| MODEL_VS_MARKET | YES | deep_OTM | 2 | -$11.38 | -$5.69 | 0.0% |
| MODEL_VS_MARKET | NO | deep_ITM | 7 | -$38.78 | -$5.54 | 85.7% |

## Edge distribution (MODEL_VS_MARKET)

| Edge range | N | P&L | Avg | WR |
|------------|---|-----|-----|-----|
| low (4-8%) | 57 | +$54.02 | +$0.95 | 94.7% |
| mid (8-15%) | 17 | +$22.31 | +$1.31 | 94.1% |
| high (15-30%) | 47 | +$394.81 | +$8.40 | 100.0% |

## TTR (time-to-resolution) analysis

| TTR bucket | N | P&L | Avg | WR |
|-----------|---|-----|-----|-----|
| 12-24h | 29 | +$119.83 | +$4.13 | 89.7% |
| 24-48h | 88 | +$338.04 | +$3.84 | 98.9% |
| >48h | 4 | +$13.25 | +$3.31 | 100.0% |

## σ bias — model vs empirical

- σ_c predicted avg : **1.07°C**
- Predicted YES rate : 92.0%
- Actual YES rate : 1.7%
- **Calibration bias ratio** : 0.02 (over-predicts YES)

## Top 5 wins

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-19 16:21:20 | MODEL_VS_MARKET | NO | 0.715 | 0.990 | 27.5% | $28.9 | +$11.51 |
| 2026-04-18 12:42:13 | MODEL_VS_MARKET | NO | 0.640 | 0.932 | 29.2% | $20.4 | +$11.48 |
| 2026-04-18 12:52:18 | MODEL_VS_MARKET | NO | 0.645 | 0.932 | 28.7% | $20.4 | +$11.23 |
| 2026-04-18 12:47:15 | MODEL_VS_MARKET | NO | 0.635 | 0.932 | 29.7% | $18.9 | +$10.86 |
| 2026-04-19 16:23:43 | MODEL_VS_MARKET | NO | 0.715 | 0.990 | 27.5% | $26.7 | +$10.65 |

## Top 5 losses

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-17 14:40:07 | MODEL_VS_MARKET | NO | 0.940 | 0.996 | 5.6% | $50.0 | -$50.00 |
| 2026-04-17 14:40:07 | MODEL_VS_MARKET | NO | 0.145 | 0.292 | 14.7% | $43.0 | -$42.98 |
| 2026-04-17 20:42:34 | MODEL_VS_MARKET | YES | 0.022 | 0.082 | 6.0% | $5.8 | -$5.79 |
| 2026-04-17 20:47:47 | MODEL_VS_MARKET | YES | 0.022 | 0.082 | 6.0% | $5.6 | -$5.59 |
| 2026-04-18 00:04:46 | MODEL_VS_MARKET | NO | 0.895 | 0.953 | 5.8% | $12.9 | +$1.51 |

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/city-optimization]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]