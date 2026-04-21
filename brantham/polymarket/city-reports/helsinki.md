---
name: Helsinki — deep dive
description: Analyse empirique complète Polymarket weather. Performance, calibration, σ bias, TTR, top trades, verdict.
type: city-report
project: brantham/polymarket
date: 2026-04-21
verdict: INSUFFICIENT_DATA
tags: [polymarket, city, helsinki, insufficient_data]
---

# Helsinki — deep dive

**Verdict: INSUFFICIENT_DATA** — N=19 trop petit pour verdict

## Identité

- ICAO : `EFHK`
- Coords : 60.3172, 24.9633
- Country / TZ : FI / Europe/Helsinki
- UTC offset : 3.0h
- Elevation : 55.0 m

## Configuration

- **Status** : ENABLED
- **Kelly fraction** : 0.5
- **N outcomes** : 19
- **Notes** : kelly from N=19 WR=100.0% (emp 1.000 → blended 0.500)
- **Updated** : 2026-04-21

## Calibrator (isotonic)

_No calibrator fit for this city → falls back to global calibrator._

## Performance empirique

- **Signaux émis** : 27
- **Outcomes réconciliés** : 19
- **P&L total** : +$18.80
- **Avg / trade** : +$0.99
- **WR** : 100.0%
- **Exposure cumulée** : +$450.03
- **Sharpe (ann.)** : 10.65
- **Daily P&L** : ['+$0.57', '+$1.18', '+$17.04']

## Breakdown alpha × side × price bucket

| Alpha | Side | Bucket | N | P&L | Avg | WR |
|-------|------|--------|---|-----|-----|-----|
| MODEL_VS_MARKET | NO | deep_ITM | 19 | +$18.80 | +$0.99 | 100.0% |
| CONFIRMED_YES | YES | deep_OTM | 7 | +$0.00 | +$0.00 | 0.0% |

## Edge distribution (MODEL_VS_MARKET)

| Edge range | N | P&L | Avg | WR |
|------------|---|-----|-----|-----|
| low (4-8%) | 19 | +$18.80 | +$0.99 | 100.0% |

## TTR (time-to-resolution) analysis

| TTR bucket | N | P&L | Avg | WR |
|-----------|---|-----|-----|-----|
| 6-12h | 3 | +$1.75 | +$0.58 | 100.0% |
| 24-48h | 15 | +$15.79 | +$1.05 | 100.0% |
| >48h | 1 | +$1.25 | +$1.25 | 100.0% |

## σ bias — model vs empirical

- σ_c predicted avg : **1.29°C**
- Predicted YES rate : 99.9%
- Actual YES rate : 0.0%
- **Calibration bias ratio** : 0.00 (over-predicts YES)

## Top 5 wins

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-18 12:42:13 | MODEL_VS_MARKET | NO | 0.940 | 1.000 | 6.0% | $20.4 | +$1.30 |
| 2026-04-18 11:56:42 | MODEL_VS_MARKET | NO | 0.940 | 1.000 | 6.0% | $19.6 | +$1.25 |
| 2026-04-18 12:47:16 | MODEL_VS_MARKET | NO | 0.940 | 1.000 | 6.0% | $18.9 | +$1.21 |
| 2026-04-18 12:52:18 | MODEL_VS_MARKET | NO | 0.945 | 1.000 | 5.5% | $20.4 | +$1.19 |
| 2026-04-18 13:02:22 | MODEL_VS_MARKET | NO | 0.945 | 0.999 | 5.4% | $20.4 | +$1.19 |

## Top 5 losses

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-18 01:06:19 | MODEL_VS_MARKET | NO | 0.955 | 0.999 | 4.4% | $12.1 | +$0.57 |
| 2026-04-18 02:19:50 | MODEL_VS_MARKET | NO | 0.954 | 0.999 | 4.5% | $12.1 | +$0.58 |
| 2026-04-18 02:25:36 | MODEL_VS_MARKET | NO | 0.954 | 0.999 | 4.5% | $12.4 | +$0.60 |
| 2026-04-18 13:32:37 | MODEL_VS_MARKET | NO | 0.955 | 0.998 | 4.3% | $18.9 | +$0.89 |
| 2026-04-18 13:37:39 | MODEL_VS_MARKET | NO | 0.955 | 0.998 | 4.3% | $19.6 | +$0.92 |

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/city-optimization]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]