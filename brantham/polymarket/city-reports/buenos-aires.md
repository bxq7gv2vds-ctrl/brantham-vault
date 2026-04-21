---
name: Buenos Aires — deep dive
description: Analyse empirique complète Polymarket weather. Performance, calibration, σ bias, TTR, top trades, verdict.
type: city-report
project: brantham/polymarket
date: 2026-04-21
verdict: WATCH
tags: [polymarket, city, buenos-aires, watch]
---

# Buenos Aires — deep dive

**Verdict: WATCH** — Marginal: $96, waiting for more data

## Identité

- ICAO : `SAEZ`
- Coords : -34.8222, -58.5358
- Country / TZ : AR / America/Argentina/Buenos_Aires
- UTC offset : -3.0h
- Elevation : 20.0 m

## Configuration

- **Status** : ENABLED
- **Kelly fraction** : 0.5
- **N outcomes** : 30
- **Notes** : kelly from N=30 WR=100.0% (emp 1.000 → blended 0.500)
- **Updated** : 2026-04-21

## Calibrator (isotonic)

_No calibrator fit for this city → falls back to global calibrator._

## Performance empirique

- **Signaux émis** : 30
- **Outcomes réconciliés** : 30
- **P&L total** : +$95.84
- **Avg / trade** : +$3.19
- **WR** : 100.0%
- **Exposure cumulée** : +$607.99
- **Daily P&L** : ['+$95.84']

## Breakdown alpha × side × price bucket

| Alpha | Side | Bucket | N | P&L | Avg | WR |
|-------|------|--------|---|-----|-----|-----|
| MODEL_VS_MARKET | NO | mid | 6 | +$52.71 | +$8.78 | 100.0% |
| MODEL_VS_MARKET | NO | deep_ITM | 24 | +$43.14 | +$1.80 | 100.0% |

## Edge distribution (MODEL_VS_MARKET)

| Edge range | N | P&L | Avg | WR |
|------------|---|-----|-----|-----|
| low (4-8%) | 24 | +$43.14 | +$1.80 | 100.0% |
| high (15-30%) | 6 | +$52.71 | +$8.78 | 100.0% |

## TTR (time-to-resolution) analysis

| TTR bucket | N | P&L | Avg | WR |
|-----------|---|-----|-----|-----|
| 12-24h | 24 | +$43.14 | +$1.80 | 100.0% |
| 24-48h | 6 | +$52.71 | +$8.78 | 100.0% |

## σ bias — model vs empirical

- σ_c predicted avg : **1.39°C**
- Predicted YES rate : 97.1%
- Actual YES rate : 0.0%
- **Calibration bias ratio** : 0.00 (over-predicts YES)

## Top 5 wins

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-19 16:39:07 | MODEL_VS_MARKET | NO | 0.690 | 0.886 | 19.6% | $21.3 | +$9.58 |
| 2026-04-19 15:58:47 | MODEL_VS_MARKET | NO | 0.690 | 0.886 | 19.6% | $19.6 | +$8.81 |
| 2026-04-19 16:34:05 | MODEL_VS_MARKET | NO | 0.690 | 0.886 | 19.6% | $19.6 | +$8.81 |
| 2026-04-19 16:11:54 | MODEL_VS_MARKET | NO | 0.695 | 0.990 | 29.5% | $19.6 | +$8.61 |
| 2026-04-19 16:13:58 | MODEL_VS_MARKET | NO | 0.695 | 0.990 | 29.5% | $19.6 | +$8.61 |

## Top 5 losses

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-19 16:18:57 | MODEL_VS_MARKET | NO | 0.924 | 0.983 | 5.9% | $18.9 | +$1.54 |
| 2026-04-19 16:24:00 | MODEL_VS_MARKET | NO | 0.924 | 0.983 | 5.9% | $18.9 | +$1.54 |
| 2026-04-19 16:49:12 | MODEL_VS_MARKET | NO | 0.919 | 0.983 | 6.4% | $18.3 | +$1.60 |
| 2026-04-19 16:54:15 | MODEL_VS_MARKET | NO | 0.919 | 0.983 | 6.4% | $18.3 | +$1.60 |
| 2026-04-19 16:08:52 | MODEL_VS_MARKET | NO | 0.924 | 0.983 | 5.9% | $19.6 | +$1.60 |

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/city-optimization]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]