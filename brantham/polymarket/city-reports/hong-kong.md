---
name: Hong Kong — deep dive
description: Analyse empirique complète Polymarket weather. Performance, calibration, σ bias, TTR, top trades, verdict.
type: city-report
project: brantham/polymarket
date: 2026-04-21
verdict: WATCH
tags: [polymarket, city, hong-kong, watch]
---

# Hong Kong — deep dive

**Verdict: WATCH** — Marginal: $35, waiting for more data

## Identité

- ICAO : `VHHH`
- Coords : 22.308, 113.9185
- Country / TZ : HK / Asia/Hong_Kong
- UTC offset : 8.0h
- Elevation : 3.0 m

## Configuration

- **Status** : ENABLED
- **Kelly fraction** : 0.5
- **N outcomes** : 35
- **Notes** : kelly from N=35 WR=100.0% (emp 1.000 → blended 0.500)
- **Updated** : 2026-04-21

## Calibrator (isotonic)

- N train : 22
- ECE before : 0.0143 → after : 0.0100
- Brier before : 0.0003 → after : 0.0001
- Fitted : 2026-04-20 09:36

## Performance empirique

- **Signaux émis** : 35
- **Outcomes réconciliés** : 35
- **P&L total** : +$34.52
- **Avg / trade** : +$0.99
- **WR** : 100.0%
- **Exposure cumulée** : +$594.15
- **Sharpe (ann.)** : 19.11
- **Daily P&L** : ['+$1.80', '+$20.92', '+$11.80']

## Breakdown alpha × side × price bucket

| Alpha | Side | Bucket | N | P&L | Avg | WR |
|-------|------|--------|---|-----|-----|-----|
| MODEL_VS_MARKET | NO | deep_ITM | 35 | +$34.52 | +$0.99 | 100.0% |

## Edge distribution (MODEL_VS_MARKET)

| Edge range | N | P&L | Avg | WR |
|------------|---|-----|-----|-----|
| low (4-8%) | 35 | +$34.52 | +$0.99 | 100.0% |

## TTR (time-to-resolution) analysis

| TTR bucket | N | P&L | Avg | WR |
|-----------|---|-----|-----|-----|
| 12-24h | 2 | +$1.80 | +$0.90 | 100.0% |
| 24-48h | 33 | +$32.72 | +$0.99 | 100.0% |

## σ bias — model vs empirical

- σ_c predicted avg : **1.06°C**
- Predicted YES rate : 99.1%
- Actual YES rate : 0.0%
- **Calibration bias ratio** : 0.00 (over-predicts YES)

## Top 5 wins

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-18 00:14:53 | MODEL_VS_MARKET | NO | 0.914 | 0.975 | 6.0% | $15.1 | +$1.41 |
| 2026-04-18 00:19:56 | MODEL_VS_MARKET | NO | 0.916 | 0.975 | 5.8% | $15.1 | +$1.37 |
| 2026-04-18 00:45:11 | MODEL_VS_MARKET | NO | 0.919 | 0.975 | 5.5% | $14.3 | +$1.25 |
| 2026-04-18 01:12:12 | MODEL_VS_MARKET | NO | 0.915 | 0.975 | 5.9% | $13.3 | +$1.22 |
| 2026-04-18 01:18:01 | MODEL_VS_MARKET | NO | 0.915 | 0.975 | 5.9% | $12.9 | +$1.19 |

## Top 5 losses

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-17 20:37:22 | MODEL_VS_MARKET | NO | 0.951 | 0.993 | 4.2% | $14.8 | +$0.76 |
| 2026-04-17 20:02:00 | MODEL_VS_MARKET | NO | 0.955 | 1.000 | 4.5% | $17.1 | +$0.80 |
| 2026-04-17 19:46:51 | MODEL_VS_MARKET | NO | 0.955 | 1.000 | 4.5% | $17.1 | +$0.81 |
| 2026-04-17 20:07:03 | MODEL_VS_MARKET | NO | 0.955 | 1.000 | 4.5% | $17.1 | +$0.81 |
| 2026-04-17 20:12:06 | MODEL_VS_MARKET | NO | 0.955 | 1.000 | 4.5% | $17.1 | +$0.81 |

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/city-optimization]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]