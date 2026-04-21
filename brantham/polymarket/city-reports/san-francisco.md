---
name: San Francisco — deep dive
description: Analyse empirique complète Polymarket weather. Performance, calibration, σ bias, TTR, top trades, verdict.
type: city-report
project: brantham/polymarket
date: 2026-04-21
verdict: KEEP
tags: [polymarket, city, san-francisco, keep]
---

# San Francisco — deep dive

**Verdict: KEEP** — Steady: $322 on 85 trades

## Identité

- ICAO : `KSFO`
- Coords : 37.6188, -122.375
- Country / TZ : US / America/Los_Angeles
- UTC offset : -7.0h
- Elevation : 4.0 m

## Configuration

- **Status** : ENABLED
- **Kelly fraction** : 0.5
- **N outcomes** : 85
- **Notes** : kelly from N=85 WR=100.0% (emp 1.000 → blended 0.500)
- **Updated** : 2026-04-21

## Calibrator (isotonic)

- N train : 63
- ECE before : 0.1360 → after : 0.0100
- Brier before : 0.0194 → after : 0.0001
- Fitted : 2026-04-21 02:20

## Performance empirique

- **Signaux émis** : 87
- **Outcomes réconciliés** : 85
- **P&L total** : +$321.93
- **Avg / trade** : +$3.79
- **WR** : 100.0%
- **Exposure cumulée** : +$604.43
- **Sharpe (ann.)** : 25.32
- **Daily P&L** : ['+$181.69', '+$89.51', '+$50.73']

## Breakdown alpha × side × price bucket

| Alpha | Side | Bucket | N | P&L | Avg | WR |
|-------|------|--------|---|-----|-----|-----|
| MODEL_VS_MARKET | NO | mid | 80 | +$304.26 | +$3.80 | 100.0% |
| MODEL_VS_MARKET | NO | ITM | 5 | +$17.67 | +$3.53 | 100.0% |
| CONFIRMED_YES | YES | ITM | 2 | +$0.00 | +$0.00 | 0.0% |

## Edge distribution (MODEL_VS_MARKET)

| Edge range | N | P&L | Avg | WR |
|------------|---|-----|-----|-----|
| mid (8-15%) | 4 | +$14.35 | +$3.59 | 100.0% |
| high (15-30%) | 69 | +$229.37 | +$3.32 | 100.0% |
| extreme (>30%) | 12 | +$78.21 | +$6.52 | 100.0% |

## TTR (time-to-resolution) analysis

| TTR bucket | N | P&L | Avg | WR |
|-----------|---|-----|-----|-----|
| 12-24h | 35 | +$132.26 | +$3.78 | 100.0% |
| 24-48h | 50 | +$189.67 | +$3.79 | 100.0% |

## σ bias — model vs empirical

- σ_c predicted avg : **1.33°C**
- Predicted YES rate : 86.5%
- Actual YES rate : 0.0%
- **Calibration bias ratio** : 0.00 (over-predicts YES)

## Top 5 wins

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-17 19:35:23 | MODEL_VS_MARKET | NO | 0.630 | 0.875 | 24.5% | $43.8 | +$25.74 |
| 2026-04-17 14:40:07 | MODEL_VS_MARKET | NO | 0.855 | 0.977 | 12.2% | $50.0 | +$8.48 |
| 2026-04-18 13:52:46 | MODEL_VS_MARKET | NO | 0.505 | 0.838 | 33.3% | $7.2 | +$7.02 |
| 2026-04-18 13:22:32 | MODEL_VS_MARKET | NO | 0.505 | 0.838 | 33.3% | $6.9 | +$6.72 |
| 2026-04-18 13:27:34 | MODEL_VS_MARKET | NO | 0.505 | 0.838 | 33.3% | $6.9 | +$6.72 |

## Top 5 losses

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-19 16:11:54 | MODEL_VS_MARKET | NO | 0.845 | 0.990 | 14.5% | $9.2 | +$1.68 |
| 2026-04-19 16:13:58 | MODEL_VS_MARKET | NO | 0.845 | 0.990 | 14.5% | $9.2 | +$1.68 |
| 2026-04-19 16:13:55 | MODEL_VS_MARKET | NO | 0.695 | 0.857 | 16.2% | $5.0 | +$2.21 |
| 2026-04-19 16:18:57 | MODEL_VS_MARKET | NO | 0.695 | 0.857 | 16.2% | $5.0 | +$2.21 |
| 2026-04-19 16:24:00 | MODEL_VS_MARKET | NO | 0.695 | 0.857 | 16.2% | $5.0 | +$2.21 |

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/city-optimization]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]