---
name: Taipei — deep dive
description: Analyse empirique complète Polymarket weather. Performance, calibration, σ bias, TTR, top trades, verdict.
type: city-report
project: brantham/polymarket
date: 2026-04-21
verdict: INSUFFICIENT_DATA
tags: [polymarket, city, taipei, insufficient_data]
---

# Taipei — deep dive

**Verdict: INSUFFICIENT_DATA** — N=9 trop petit pour verdict

## Identité

- ICAO : `RCTP`
- Coords : 25.0777, 121.2328
- Country / TZ : TW / Asia/Taipei
- UTC offset : 8.0h
- Elevation : 33.0 m

## Configuration

- **Status** : ENABLED
- **Kelly fraction** : 0.1
- **N outcomes** : 9
- **Notes** : insufficient data (N=9 < 10)
- **Updated** : 2026-04-21

## Calibrator (isotonic)

_No calibrator fit for this city → falls back to global calibrator._

## Performance empirique

- **Signaux émis** : 10
- **Outcomes réconciliés** : 9
- **P&L total** : +$14.19
- **Avg / trade** : +$1.58
- **WR** : 100.0%
- **Exposure cumulée** : +$174.35
- **Sharpe (ann.)** : 15.04
- **Daily P&L** : ['+$1.80', '+$12.39']

## Breakdown alpha × side × price bucket

| Alpha | Side | Bucket | N | P&L | Avg | WR |
|-------|------|--------|---|-----|-----|-----|
| MODEL_VS_MARKET | NO | deep_ITM | 9 | +$14.19 | +$1.58 | 100.0% |

## Edge distribution (MODEL_VS_MARKET)

| Edge range | N | P&L | Avg | WR |
|------------|---|-----|-----|-----|
| low (4-8%) | 6 | +$8.04 | +$1.34 | 100.0% |
| mid (8-15%) | 3 | +$6.14 | +$2.05 | 100.0% |

## TTR (time-to-resolution) analysis

| TTR bucket | N | P&L | Avg | WR |
|-----------|---|-----|-----|-----|
| 12-24h | 2 | +$1.80 | +$0.90 | 100.0% |
| 24-48h | 7 | +$12.39 | +$1.77 | 100.0% |

## σ bias — model vs empirical

- σ_c predicted avg : **0.76°C**
- Predicted YES rate : 100.0%
- Actual YES rate : 0.0%
- **Calibration bias ratio** : 0.00 (over-predicts YES)

## Top 5 wins

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-18 13:02:22 | MODEL_VS_MARKET | NO | 0.905 | 1.000 | 9.4% | $20.4 | +$2.13 |
| 2026-04-18 13:07:24 | MODEL_VS_MARKET | NO | 0.905 | 1.000 | 9.4% | $20.4 | +$2.13 |
| 2026-04-18 12:42:14 | MODEL_VS_MARKET | NO | 0.915 | 1.000 | 8.5% | $20.4 | +$1.88 |
| 2026-04-18 12:47:16 | MODEL_VS_MARKET | NO | 0.920 | 1.000 | 8.0% | $18.9 | +$1.63 |
| 2026-04-18 13:12:27 | MODEL_VS_MARKET | NO | 0.926 | 1.000 | 7.3% | $19.6 | +$1.56 |

## Top 5 losses

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-17 23:54:41 | MODEL_VS_MARKET | NO | 0.942 | 1.000 | 5.8% | $14.5 | +$0.89 |
| 2026-04-17 21:33:22 | MODEL_VS_MARKET | NO | 0.947 | 1.000 | 5.3% | $16.2 | +$0.90 |
| 2026-04-18 13:32:37 | MODEL_VS_MARKET | NO | 0.926 | 1.000 | 7.3% | $18.9 | +$1.50 |
| 2026-04-18 13:12:27 | MODEL_VS_MARKET | NO | 0.926 | 1.000 | 7.3% | $19.6 | +$1.56 |
| 2026-04-18 13:17:29 | MODEL_VS_MARKET | NO | 0.926 | 1.000 | 7.3% | $19.6 | +$1.56 |

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/city-optimization]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]