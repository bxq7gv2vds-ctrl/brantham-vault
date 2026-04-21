---
name: Wuhan — deep dive
description: Analyse empirique complète Polymarket weather. Performance, calibration, σ bias, TTR, top trades, verdict.
type: city-report
project: brantham/polymarket
date: 2026-04-21
verdict: INSUFFICIENT_DATA
tags: [polymarket, city, wuhan, insufficient_data]
---

# Wuhan — deep dive

**Verdict: INSUFFICIENT_DATA** — N=10 trop petit pour verdict

## Identité

- ICAO : `ZHHH`
- Coords : 30.7838, 114.2081
- Country / TZ : CN / Asia/Shanghai
- UTC offset : 8.0h
- Elevation : 34.0 m

## Configuration

- **Status** : ENABLED
- **Kelly fraction** : 0.4375
- **N outcomes** : 10
- **Notes** : kelly from N=10 WR=100.0% (emp 1.000 → blended 0.438)
- **Updated** : 2026-04-21

## Calibrator (isotonic)

_No calibrator fit for this city → falls back to global calibrator._

## Performance empirique

- **Signaux émis** : 10
- **Outcomes réconciliés** : 10
- **P&L total** : +$28.83
- **Avg / trade** : +$2.88
- **WR** : 100.0%
- **Exposure cumulée** : +$197.88
- **Daily P&L** : ['+$28.83']

## Breakdown alpha × side × price bucket

| Alpha | Side | Bucket | N | P&L | Avg | WR |
|-------|------|--------|---|-----|-----|-----|
| MODEL_VS_MARKET | NO | ITM | 6 | +$24.02 | +$4.00 | 100.0% |
| MODEL_VS_MARKET | NO | deep_ITM | 4 | +$4.81 | +$1.20 | 100.0% |

## Edge distribution (MODEL_VS_MARKET)

| Edge range | N | P&L | Avg | WR |
|------------|---|-----|-----|-----|
| low (4-8%) | 4 | +$4.81 | +$1.20 | 100.0% |
| mid (8-15%) | 3 | +$7.81 | +$2.60 | 100.0% |
| high (15-30%) | 3 | +$16.21 | +$5.40 | 100.0% |

## TTR (time-to-resolution) analysis

| TTR bucket | N | P&L | Avg | WR |
|-----------|---|-----|-----|-----|
| 12-24h | 9 | +$21.11 | +$2.35 | 100.0% |
| 24-48h | 1 | +$7.72 | +$7.72 | 100.0% |

## σ bias — model vs empirical

- σ_c predicted avg : **2.22°C**
- Predicted YES rate : 98.7%
- Actual YES rate : 0.0%
- **Calibration bias ratio** : 0.00 (over-predicts YES)

## Top 5 wins

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-19 17:09:32 | MODEL_VS_MARKET | NO | 0.710 | 0.902 | 19.2% | $18.9 | +$7.72 |
| 2026-04-19 17:34:49 | MODEL_VS_MARKET | NO | 0.814 | 0.996 | 18.2% | $19.6 | +$4.48 |
| 2026-04-19 17:39:52 | MODEL_VS_MARKET | NO | 0.825 | 0.996 | 17.1% | $18.9 | +$4.01 |
| 2026-04-19 17:49:57 | MODEL_VS_MARKET | NO | 0.885 | 0.996 | 11.0% | $22.4 | +$2.89 |
| 2026-04-19 17:55:00 | MODEL_VS_MARKET | NO | 0.885 | 0.996 | 11.0% | $19.6 | +$2.54 |

## Top 5 losses

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-19 16:54:15 | MODEL_VS_MARKET | NO | 0.955 | 0.996 | 4.1% | $18.3 | +$0.86 |
| 2026-04-19 15:53:44 | MODEL_VS_MARKET | NO | 0.947 | 0.996 | 4.9% | $18.9 | +$1.06 |
| 2026-04-19 16:44:10 | MODEL_VS_MARKET | NO | 0.941 | 0.996 | 5.5% | $21.3 | +$1.34 |
| 2026-04-19 16:29:03 | MODEL_VS_MARKET | NO | 0.926 | 0.996 | 6.9% | $19.6 | +$1.56 |
| 2026-04-19 17:44:55 | MODEL_VS_MARKET | NO | 0.895 | 0.996 | 10.0% | $20.4 | +$2.38 |

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/city-optimization]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]