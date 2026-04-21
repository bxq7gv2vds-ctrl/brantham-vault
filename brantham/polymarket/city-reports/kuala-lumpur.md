---
name: Kuala Lumpur — deep dive
description: Analyse empirique complète Polymarket weather. Performance, calibration, σ bias, TTR, top trades, verdict.
type: city-report
project: brantham/polymarket
date: 2026-04-21
verdict: WATCH
tags: [polymarket, city, kuala-lumpur, watch]
---

# Kuala Lumpur — deep dive

**Verdict: WATCH** — Marginal: $93, waiting for more data

## Identité

- ICAO : `WMKK`
- Coords : 2.7456, 101.7099
- Country / TZ : MY / Asia/Kuala_Lumpur
- UTC offset : 8.0h
- Elevation : 21.0 m

## Configuration

- **Status** : ENABLED
- **Kelly fraction** : 0.5
- **N outcomes** : 34
- **Notes** : kelly from N=34 WR=100.0% (emp 1.000 → blended 0.500)
- **Updated** : 2026-04-21

## Calibrator (isotonic)

- N train : 34
- ECE before : 0.0184 → after : 0.0100
- Brier before : 0.0006 → after : 0.0001
- Fitted : 2026-04-21 02:20

## Performance empirique

- **Signaux émis** : 35
- **Outcomes réconciliés** : 34
- **P&L total** : +$92.68
- **Avg / trade** : +$2.73
- **WR** : 100.0%
- **Exposure cumulée** : +$611.89
- **Sharpe (ann.)** : 12.29
- **Daily P&L** : ['+$88.66', '+$4.02']

## Breakdown alpha × side × price bucket

| Alpha | Side | Bucket | N | P&L | Avg | WR |
|-------|------|--------|---|-----|-----|-----|
| MODEL_VS_MARKET | NO | ITM | 26 | +$85.80 | +$3.30 | 100.0% |
| MODEL_VS_MARKET | NO | deep_ITM | 8 | +$6.88 | +$0.86 | 100.0% |

## Edge distribution (MODEL_VS_MARKET)

| Edge range | N | P&L | Avg | WR |
|------------|---|-----|-----|-----|
| low (4-8%) | 8 | +$6.88 | +$0.86 | 100.0% |
| mid (8-15%) | 23 | +$75.49 | +$3.28 | 100.0% |
| high (15-30%) | 3 | +$10.31 | +$3.44 | 100.0% |

## TTR (time-to-resolution) analysis

| TTR bucket | N | P&L | Avg | WR |
|-----------|---|-----|-----|-----|
| 12-24h | 33 | +$88.66 | +$2.69 | 100.0% |
| 24-48h | 1 | +$4.02 | +$4.02 | 100.0% |

## σ bias — model vs empirical

- σ_c predicted avg : **1.32°C**
- Predicted YES rate : 98.2%
- Actual YES rate : 0.0%
- **Calibration bias ratio** : 0.00 (over-predicts YES)

## Top 5 wins

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-18 16:23:05 | MODEL_VS_MARKET | NO | 0.830 | 0.942 | 11.2% | $19.6 | +$4.02 |
| 2026-04-17 19:36:46 | MODEL_VS_MARKET | NO | 0.840 | 0.970 | 13.0% | $20.4 | +$3.89 |
| 2026-04-17 19:46:51 | MODEL_VS_MARKET | NO | 0.825 | 0.970 | 14.5% | $17.1 | +$3.64 |
| 2026-04-17 19:56:57 | MODEL_VS_MARKET | NO | 0.830 | 0.970 | 14.0% | $17.7 | +$3.62 |
| 2026-04-17 20:58:04 | MODEL_VS_MARKET | NO | 0.845 | 0.998 | 15.3% | $19.6 | +$3.60 |

## Top 5 losses

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-17 23:24:24 | MODEL_VS_MARKET | NO | 0.955 | 0.998 | 4.3% | $16.0 | +$0.75 |
| 2026-04-17 23:09:16 | MODEL_VS_MARKET | NO | 0.955 | 0.998 | 4.3% | $17.1 | +$0.81 |
| 2026-04-17 23:14:19 | MODEL_VS_MARKET | NO | 0.955 | 0.998 | 4.3% | $17.1 | +$0.81 |
| 2026-04-17 23:19:22 | MODEL_VS_MARKET | NO | 0.955 | 0.998 | 4.3% | $17.1 | +$0.81 |
| 2026-04-17 22:54:08 | MODEL_VS_MARKET | NO | 0.955 | 0.998 | 4.3% | $18.3 | +$0.86 |

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/city-optimization]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]