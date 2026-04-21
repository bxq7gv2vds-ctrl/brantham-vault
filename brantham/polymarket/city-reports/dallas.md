---
name: Dallas — deep dive
description: Analyse empirique complète Polymarket weather. Performance, calibration, σ bias, TTR, top trades, verdict.
type: city-report
project: brantham/polymarket
date: 2026-04-21
verdict: SCALE
tags: [polymarket, city, dallas, scale]
---

# Dallas — deep dive

**Verdict: SCALE** — Star performer: $694, avg $5.30, kelly boost recommandé

## Identité

- ICAO : `KDAL`
- Coords : 32.8471, -96.8518
- Country / TZ : US / America/Chicago
- UTC offset : -5.0h
- Elevation : 149.0 m

## Configuration

- **Status** : ENABLED
- **Kelly fraction** : 0.5
- **N outcomes** : 131
- **Notes** : kelly from N=131 WR=86.3% (emp 0.619 → blended 0.500)
- **Updated** : 2026-04-21

## Calibrator (isotonic)

- N train : 100
- ECE before : 0.1916 → after : 0.0366
- Brier before : 0.0790 → after : 0.0271
- Fitted : 2026-04-21 02:20

## Performance empirique

- **Signaux émis** : 131
- **Outcomes réconciliés** : 131
- **P&L total** : +$694.10
- **Avg / trade** : +$5.30
- **WR** : 86.3%
- **Exposure cumulée** : +$2,274.78
- **Sharpe (ann.)** : 22.77
- **Daily P&L** : ['+$104.41', '+$38.88', '+$264.77', '+$286.05']

## Breakdown alpha × side × price bucket

| Alpha | Side | Bucket | N | P&L | Avg | WR |
|-------|------|--------|---|-----|-----|-----|
| MODEL_VS_MARKET | NO | mid | 84 | +$464.55 | +$5.53 | 86.9% |
| MODEL_VS_MARKET | NO | ITM | 29 | +$165.65 | +$5.71 | 100.0% |
| MODEL_VS_MARKET | YES | OTM | 3 | +$97.62 | +$32.54 | 100.0% |
| MODEL_VS_MARKET | YES | ITM | 8 | +$29.69 | +$3.71 | 100.0% |
| MODEL_VS_MARKET | YES | deep_OTM | 7 | -$63.41 | -$9.06 | 0.0% |

## Edge distribution (MODEL_VS_MARKET)

| Edge range | N | P&L | Avg | WR |
|------------|---|-----|-----|-----|
| low (4-8%) | 17 | +$91.71 | +$5.39 | 100.0% |
| mid (8-15%) | 40 | -$72.60 | -$1.82 | 55.0% |
| high (15-30%) | 56 | +$527.43 | +$9.42 | 100.0% |
| extreme (>30%) | 18 | +$147.56 | +$8.20 | 100.0% |

## TTR (time-to-resolution) analysis

| TTR bucket | N | P&L | Avg | WR |
|-----------|---|-----|-----|-----|
| 6-12h | 20 | +$162.73 | +$8.14 | 100.0% |
| 12-24h | 36 | +$248.64 | +$6.91 | 80.6% |
| 24-48h | 68 | +$157.36 | +$2.31 | 83.8% |
| >48h | 7 | +$125.36 | +$17.91 | 100.0% |

## σ bias — model vs empirical

- σ_c predicted avg : **1.48°C**
- Predicted YES rate : 81.6%
- Actual YES rate : 16.8%
- **Calibration bias ratio** : 0.21 (over-predicts YES)

## Top 5 wins

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-18 11:56:41 | MODEL_VS_MARKET | YES | 0.185 | 0.304 | 11.9% | $14.3 | +$62.87 |
| 2026-04-18 08:42:48 | MODEL_VS_MARKET | YES | 0.250 | 0.304 | 5.4% | $6.1 | +$18.39 |
| 2026-04-18 08:49:46 | MODEL_VS_MARKET | YES | 0.255 | 0.304 | 4.9% | $5.6 | +$16.36 |
| 2026-04-19 16:59:17 | MODEL_VS_MARKET | NO | 0.645 | 0.859 | 21.4% | $22.4 | +$12.31 |
| 2026-04-19 17:04:21 | MODEL_VS_MARKET | NO | 0.645 | 0.859 | 21.4% | $22.4 | +$12.31 |

## Top 5 losses

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-17 21:43:27 | MODEL_VS_MARKET | NO | 0.570 | 0.692 | 12.2% | $21.3 | -$21.32 |
| 2026-04-17 21:48:30 | MODEL_VS_MARKET | NO | 0.570 | 0.692 | 12.2% | $21.3 | -$21.32 |
| 2026-04-17 21:53:33 | MODEL_VS_MARKET | NO | 0.570 | 0.692 | 12.2% | $21.3 | -$21.32 |
| 2026-04-17 22:08:42 | MODEL_VS_MARKET | NO | 0.570 | 0.692 | 12.2% | $19.6 | -$19.61 |
| 2026-04-17 21:38:24 | MODEL_VS_MARKET | NO | 0.570 | 0.692 | 12.2% | $18.9 | -$18.90 |

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/city-optimization]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]