---
name: New York City — deep dive
description: Analyse empirique complète Polymarket weather. Performance, calibration, σ bias, TTR, top trades, verdict.
type: city-report
project: brantham/polymarket
date: 2026-04-21
verdict: DISABLED
tags: [polymarket, city, new-york-city, disabled]
---

# New York City — deep dive

**Verdict: DISABLED** — Killed: kelly from N=34 WR=91.2% (emp 0.681 → blended 0.479)

## Identité

- ICAO : `KLGA`
- Coords : 40.7772, -73.8726
- Country / TZ : US / America/New_York
- UTC offset : -4.0h
- Elevation : 7.0 m

## Configuration

- **Status** : DISABLED
- **Kelly fraction** : 0.4790698060573857
- **N outcomes** : 47
- **Notes** : kelly from N=34 WR=91.2% (emp 0.681 → blended 0.479)
- **Updated** : 2026-04-21

## Calibrator (isotonic)

- N train : 17
- ECE before : 0.0508 → after : 0.0173
- Brier before : 0.0037 → after : 0.0007
- Fitted : 2026-04-20 09:36

## Performance empirique

- **Signaux émis** : 47
- **Outcomes réconciliés** : 47
- **P&L total** : -$159.51
- **Avg / trade** : -$3.39
- **WR** : 66.0%
- **Exposure cumulée** : +$567.43
- **Sharpe (ann.)** : -5.67
- **Daily P&L** : ['+$36.14', '-$204.96', '+$17.93', '-$8.62']

## Breakdown alpha × side × price bucket

| Alpha | Side | Bucket | N | P&L | Avg | WR |
|-------|------|--------|---|-----|-----|-----|
| MODEL_VS_MARKET | NO | mid | 12 | +$81.01 | +$6.75 | 100.0% |
| MODEL_VS_MARKET | NO | ITM | 6 | +$24.16 | +$4.03 | 100.0% |
| MODEL_VS_MARKET | NO | deep_ITM | 13 | +$6.11 | +$0.47 | 100.0% |
| MODEL_VS_MARKET | YES | deep_OTM | 3 | -$65.83 | -$21.94 | 0.0% |
| CONFIRMED_YES | YES | OTM | 13 | -$204.96 | -$15.77 | 0.0% |

## Edge distribution (MODEL_VS_MARKET)

| Edge range | N | P&L | Avg | WR |
|------------|---|-----|-----|-----|
| low (4-8%) | 10 | +$4.60 | +$0.46 | 100.0% |
| mid (8-15%) | 7 | -$48.09 | -$6.87 | 57.1% |
| high (15-30%) | 12 | +$40.85 | +$3.40 | 100.0% |
| extreme (>30%) | 5 | +$48.09 | +$9.62 | 100.0% |

## TTR (time-to-resolution) analysis

| TTR bucket | N | P&L | Avg | WR |
|-----------|---|-----|-----|-----|
| 0-6h | 11 | -$177.71 | -$16.16 | 0.0% |
| 6-12h | 2 | -$27.25 | -$13.62 | 0.0% |
| 12-24h | 34 | +$45.45 | +$1.34 | 91.2% |

## σ bias — model vs empirical

- σ_c predicted avg : **1.34°C**
- Predicted YES rate : 90.4%
- Actual YES rate : 0.0%
- **Calibration bias ratio** : 0.00 (over-predicts YES)

## Top 5 wins

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-17 14:40:06 | MODEL_VS_MARKET | NO | 0.635 | 0.951 | 31.6% | $50.0 | +$28.74 |
| 2026-04-17 19:35:22 | MODEL_VS_MARKET | NO | 0.655 | 0.951 | 29.6% | $36.5 | +$19.23 |
| 2026-04-17 14:40:06 | MODEL_VS_MARKET | NO | 0.755 | 0.889 | 13.4% | $50.0 | +$16.23 |
| 2026-04-17 14:44:59 | MODEL_VS_MARKET | NO | 0.635 | 0.951 | 31.6% | $14.8 | +$8.48 |
| 2026-04-17 21:53:33 | MODEL_VS_MARKET | NO | 0.585 | 0.953 | 36.8% | $5.3 | +$3.76 |

## Top 5 losses

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-17 14:40:06 | MODEL_VS_MARKET | YES | 0.055 | 0.146 | 9.1% | $24.1 | -$24.11 |
| 2026-04-17 14:40:06 | MODEL_VS_MARKET | YES | 0.008 | 0.100 | 9.2% | $23.3 | -$23.30 |
| 2026-04-19 17:45:57 | MODEL_VS_MARKET | YES | 0.045 | 0.167 | 12.2% | $18.4 | -$18.42 |
| 2026-04-18 08:42:48 | CONFIRMED_YES | YES | 0.195 | 1.000 | 80.5% | $17.1 | -$17.15 |
| 2026-04-18 08:49:46 | CONFIRMED_YES | YES | 0.195 | 1.000 | 80.5% | $17.1 | -$17.15 |

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/city-optimization]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]