---
name: Austin — deep dive
description: Analyse empirique complète Polymarket weather. Performance, calibration, σ bias, TTR, top trades, verdict.
type: city-report
project: brantham/polymarket
date: 2026-04-21
verdict: SCALE
tags: [polymarket, city, austin, scale]
---

# Austin — deep dive

**Verdict: SCALE** — Star performer: $16795, avg $144.79, kelly boost recommandé

## Identité

- ICAO : `KAUS`
- Coords : 30.1945, -97.6699
- Country / TZ : US / America/Chicago
- UTC offset : -5.0h
- Elevation : 165.0 m

## Configuration

- **Status** : ENABLED
- **Kelly fraction** : 0.5
- **N outcomes** : 116
- **Notes** : kelly from N=112 WR=79.5% (emp 0.717 → blended 0.500)
- **Updated** : 2026-04-21

## Calibrator (isotonic)

- N train : 100
- ECE before : 0.1807 → after : 0.0860
- Brier before : 0.1817 → after : 0.1090
- Fitted : 2026-04-21 02:20

## Performance empirique

- **Signaux émis** : 116
- **Outcomes réconciliés** : 116
- **P&L total** : +$16,795.40
- **Avg / trade** : +$144.79
- **WR** : 80.2%
- **Exposure cumulée** : +$1,934.24
- **Sharpe (ann.)** : 11.22
- **Daily P&L** : ['+$226.47', '+$12,518.95', '-$358.16', '+$4,408.14']

## Breakdown alpha × side × price bucket

| Alpha | Side | Bucket | N | P&L | Avg | WR |
|-------|------|--------|---|-----|-----|-----|
| MODEL_VS_MARKET | YES | deep_OTM | 60 | +$12,082.16 | +$201.37 | 61.7% |
| MODEL_VS_MARKET | NO | deep_OTM | 12 | +$4,408.14 | +$367.34 | 100.0% |
| MODEL_VS_MARKET | NO | mid | 19 | +$157.98 | +$8.31 | 100.0% |
| MODEL_VS_MARKET | NO | ITM | 21 | +$141.81 | +$6.75 | 100.0% |
| CONFIRMED_NO | NO | ITM | 3 | +$4.81 | +$1.60 | 100.0% |

## Edge distribution (MODEL_VS_MARKET)

| Edge range | N | P&L | Avg | WR |
|------------|---|-----|-----|-----|
| mid (8-15%) | 12 | +$4,408.14 | +$367.34 | 100.0% |
| high (15-30%) | 63 | +$7,643.62 | +$121.33 | 85.7% |
| extreme (>30%) | 37 | +$4,738.34 | +$128.06 | 62.2% |

## TTR (time-to-resolution) analysis

| TTR bucket | N | P&L | Avg | WR |
|-----------|---|-----|-----|-----|
| 0-6h | 8 | -$48.44 | -$6.06 | 50.0% |
| 6-12h | 17 | +$97.01 | +$5.71 | 100.0% |
| 12-24h | 40 | -$186.99 | -$4.67 | 55.0% |
| 24-48h | 51 | +$16,933.83 | +$332.04 | 98.0% |

## σ bias — model vs empirical

- σ_c predicted avg : **1.98°C**
- Predicted YES rate : 55.6%
- Actual YES rate : 33.0%
- **Calibration bias ratio** : 0.59 (over-predicts YES)

## Top 5 wins

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-19 17:54:59 | MODEL_VS_MARKET | NO | 0.012 | 0.123 | 11.1% | $11.0 | +$908.96 |
| 2026-04-19 17:44:55 | MODEL_VS_MARKET | NO | 0.017 | 0.123 | 10.6% | $11.0 | +$637.79 |
| 2026-04-17 21:43:27 | MODEL_VS_MARKET | YES | 0.050 | 0.314 | 26.4% | $21.3 | +$405.08 |
| 2026-04-17 21:48:30 | MODEL_VS_MARKET | YES | 0.050 | 0.314 | 26.4% | $21.3 | +$405.08 |
| 2026-04-17 21:53:33 | MODEL_VS_MARKET | YES | 0.050 | 0.314 | 26.4% | $21.3 | +$405.08 |

## Top 5 losses

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-17 14:40:06 | MODEL_VS_MARKET | YES | 0.003 | 0.183 | 18.0% | $45.2 | -$45.16 |
| 2026-04-18 13:52:46 | MODEL_VS_MARKET | YES | 0.045 | 0.410 | 36.5% | $21.3 | -$21.32 |
| 2026-04-18 12:42:13 | MODEL_VS_MARKET | YES | 0.045 | 0.326 | 28.1% | $20.4 | -$20.41 |
| 2026-04-18 12:52:18 | MODEL_VS_MARKET | YES | 0.045 | 0.326 | 28.1% | $20.4 | -$20.41 |
| 2026-04-18 13:02:22 | MODEL_VS_MARKET | YES | 0.045 | 0.386 | 34.1% | $20.4 | -$20.41 |

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/city-optimization]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]