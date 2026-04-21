---
name: Chicago — deep dive
description: Analyse empirique complète Polymarket weather. Performance, calibration, σ bias, TTR, top trades, verdict.
type: city-report
project: brantham/polymarket
date: 2026-04-21
verdict: DISABLED
tags: [polymarket, city, chicago, disabled]
---

# Chicago — deep dive

**Verdict: DISABLED** — Killed: kelly from N=69 WR=21.7% (emp 0.000 → blended 0.076)

## Identité

- ICAO : `KORD`
- Coords : 41.9786, -87.9048
- Country / TZ : US / America/Chicago
- UTC offset : -5.0h
- Elevation : 205.0 m

## Configuration

- **Status** : DISABLED
- **Kelly fraction** : 0.07575757575757576
- **N outcomes** : 69
- **Notes** : kelly from N=69 WR=21.7% (emp 0.000 → blended 0.076)
- **Updated** : 2026-04-21

## Calibrator (isotonic)

- N train : 54
- ECE before : 0.5613 → after : 0.0937
- Brier before : 0.4655 → after : 0.0605
- Fitted : 2026-04-21 02:20

## Performance empirique

- **Signaux émis** : 83
- **Outcomes réconciliés** : 69
- **P&L total** : -$641.82
- **Avg / trade** : -$9.30
- **WR** : 21.7%
- **Exposure cumulée** : +$1,293.81
- **Sharpe (ann.)** : -10.07
- **Daily P&L** : ['+$170.40', '-$445.55', '-$172.66', '-$194.00']

## Breakdown alpha × side × price bucket

| Alpha | Side | Bucket | N | P&L | Avg | WR |
|-------|------|--------|---|-----|-----|-----|
| CONFIRMED_YES | YES | deep_OTM | 14 | +$0.00 | +$0.00 | 0.0% |
| MODEL_VS_MARKET | NO | OTM | 3 | -$55.18 | -$18.39 | 0.0% |
| MODEL_VS_MARKET | YES | deep_OTM | 16 | -$64.76 | -$4.05 | 6.2% |
| MODEL_VS_MARKET | NO | mid | 15 | -$199.21 | -$13.28 | 6.7% |
| MODEL_VS_MARKET | NO | ITM | 35 | -$322.67 | -$9.22 | 37.1% |

## Edge distribution (MODEL_VS_MARKET)

| Edge range | N | P&L | Avg | WR |
|------------|---|-----|-----|-----|
| low (4-8%) | 8 | -$53.37 | -$6.67 | 25.0% |
| mid (8-15%) | 15 | -$141.75 | -$9.45 | 6.7% |
| high (15-30%) | 42 | -$531.68 | -$12.66 | 23.8% |
| extreme (>30%) | 4 | +$84.98 | +$21.25 | 50.0% |

## TTR (time-to-resolution) analysis

| TTR bucket | N | P&L | Avg | WR |
|-----------|---|-----|-----|-----|
| 6-12h | 5 | +$20.29 | +$4.06 | 100.0% |
| 12-24h | 25 | -$98.57 | -$3.94 | 28.0% |
| 24-48h | 37 | -$550.40 | -$14.88 | 5.4% |
| >48h | 2 | -$13.13 | -$6.57 | 50.0% |

## σ bias — model vs empirical

- σ_c predicted avg : **1.36°C**
- Predicted YES rate : 69.3%
- Actual YES rate : 58.0%
- **Calibration bias ratio** : 0.84 (calibré)

## Top 5 wins

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-17 14:44:59 | MODEL_VS_MARKET | YES | 0.102 | 0.998 | 89.5% | $14.8 | +$129.24 |
| 2026-04-17 14:40:06 | MODEL_VS_MARKET | NO | 0.715 | 0.845 | 13.0% | $50.0 | +$19.93 |
| 2026-04-18 03:21:44 | MODEL_VS_MARKET | NO | 0.695 | 0.999 | 30.4% | $13.1 | +$5.74 |
| 2026-04-17 23:59:43 | MODEL_VS_MARKET | NO | 0.785 | 0.995 | 21.0% | $18.3 | +$5.00 |
| 2026-04-17 23:49:37 | MODEL_VS_MARKET | NO | 0.785 | 0.995 | 21.0% | $17.7 | +$4.84 |

## Top 5 losses

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-19 17:45:57 | MODEL_VS_MARKET | YES | 0.055 | 0.147 | 9.2% | $25.3 | -$25.31 |
| 2026-04-19 16:54:31 | MODEL_VS_MARKET | YES | 0.060 | 0.364 | 30.4% | $25.0 | -$25.00 |
| 2026-04-19 16:54:51 | MODEL_VS_MARKET | YES | 0.060 | 0.364 | 30.4% | $25.0 | -$25.00 |
| 2026-04-17 19:36:45 | MODEL_VS_MARKET | NO | 0.705 | 0.876 | 17.1% | $20.4 | -$20.41 |
| 2026-04-18 13:02:21 | MODEL_VS_MARKET | NO | 0.625 | 0.827 | 20.2% | $20.4 | -$20.41 |

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/city-optimization]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]