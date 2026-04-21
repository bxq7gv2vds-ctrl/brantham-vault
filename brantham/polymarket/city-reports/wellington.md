---
name: Wellington — deep dive
description: Analyse empirique complète Polymarket weather. Performance, calibration, σ bias, TTR, top trades, verdict.
type: city-report
project: brantham/polymarket
date: 2026-04-21
verdict: DISABLED
tags: [polymarket, city, wellington, disabled]
---

# Wellington — deep dive

**Verdict: DISABLED** — Killed: kelly from N=28 WR=0.0% (emp 0.000 → blended 0.129)

## Identité

- ICAO : `NZWN`
- Coords : -41.3272, 174.8053
- Country / TZ : NZ / Pacific/Auckland
- UTC offset : 12.0h
- Elevation : 13.0 m

## Configuration

- **Status** : DISABLED
- **Kelly fraction** : 0.12931034482758622
- **N outcomes** : 28
- **Notes** : kelly from N=28 WR=0.0% (emp 0.000 → blended 0.129)
- **Updated** : 2026-04-21

## Calibrator (isotonic)

_No calibrator fit for this city → falls back to global calibrator._

## Performance empirique

- **Signaux émis** : 28
- **Outcomes réconciliés** : 28
- **P&L total** : -$519.24
- **Avg / trade** : -$18.54
- **WR** : 0.0%
- **Exposure cumulée** : +$519.24
- **Daily P&L** : ['-$519.24']

## Breakdown alpha × side × price bucket

| Alpha | Side | Bucket | N | P&L | Avg | WR |
|-------|------|--------|---|-----|-----|-----|
| MODEL_VS_MARKET | YES | deep_OTM | 28 | -$519.24 | -$18.54 | 0.0% |

## Edge distribution (MODEL_VS_MARKET)

| Edge range | N | P&L | Avg | WR |
|------------|---|-----|-----|-----|
| mid (8-15%) | 16 | -$249.61 | -$15.60 | 0.0% |
| high (15-30%) | 4 | -$73.08 | -$18.27 | 0.0% |
| extreme (>30%) | 8 | -$196.55 | -$24.57 | 0.0% |

## TTR (time-to-resolution) analysis

| TTR bucket | N | P&L | Avg | WR |
|-----------|---|-----|-----|-----|
| 24-48h | 28 | -$519.24 | -$18.54 | 0.0% |

## σ bias — model vs empirical

- σ_c predicted avg : **1.90°C**
- Predicted YES rate : 25.2%
- Actual YES rate : 0.0%
- **Calibration bias ratio** : 0.00 (over-predicts YES)

## Top 5 wins

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-19 16:24:00 | MODEL_VS_MARKET | YES | 0.045 | 0.193 | 14.8% | $14.7 | -$14.67 |
| 2026-04-19 16:13:55 | MODEL_VS_MARKET | YES | 0.044 | 0.193 | 14.9% | $14.7 | -$14.71 |
| 2026-04-19 15:53:45 | MODEL_VS_MARKET | YES | 0.044 | 0.193 | 14.9% | $14.8 | -$14.75 |
| 2026-04-19 16:18:57 | MODEL_VS_MARKET | YES | 0.044 | 0.193 | 14.9% | $14.8 | -$14.75 |
| 2026-04-19 16:29:03 | MODEL_VS_MARKET | YES | 0.045 | 0.193 | 14.8% | $15.2 | -$15.22 |

## Top 5 losses

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-19 16:21:20 | MODEL_VS_MARKET | YES | 0.044 | 0.400 | 35.6% | $28.9 | -$28.87 |
| 2026-04-19 16:23:44 | MODEL_VS_MARKET | YES | 0.045 | 0.400 | 35.5% | $26.7 | -$26.73 |
| 2026-04-19 16:24:47 | MODEL_VS_MARKET | YES | 0.045 | 0.400 | 35.5% | $26.7 | -$26.73 |
| 2026-04-19 16:29:09 | MODEL_VS_MARKET | YES | 0.045 | 0.400 | 35.5% | $25.0 | -$25.00 |
| 2026-04-19 16:54:31 | MODEL_VS_MARKET | YES | 0.035 | 0.400 | 36.5% | $25.0 | -$25.00 |

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/city-optimization]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]