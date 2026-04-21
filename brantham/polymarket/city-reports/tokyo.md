---
name: Tokyo — deep dive
description: Analyse empirique complète Polymarket weather. Performance, calibration, σ bias, TTR, top trades, verdict.
type: city-report
project: brantham/polymarket
date: 2026-04-21
verdict: DISABLED
tags: [polymarket, city, tokyo, disabled]
---

# Tokyo — deep dive

**Verdict: DISABLED** — Killed: kelly from N=94 WR=1.1% (emp 0.000 → blended 0.060)

## Identité

- ICAO : `RJTT`
- Coords : 35.5494, 139.7798
- Country / TZ : JP / Asia/Tokyo
- UTC offset : 9.0h
- Elevation : 11.0 m

## Configuration

- **Status** : DISABLED
- **Kelly fraction** : 0.06048387096774194
- **N outcomes** : 94
- **Notes** : kelly from N=94 WR=1.1% (emp 0.000 → blended 0.060)
- **Updated** : 2026-04-21

## Calibrator (isotonic)

- N train : 85
- ECE before : 0.1840 → after : 0.0100
- Brier before : 0.0347 → after : 0.0001
- Fitted : 2026-04-21 02:20

## Performance empirique

- **Signaux émis** : 94
- **Outcomes réconciliés** : 94
- **P&L total** : -$1,071.81
- **Avg / trade** : -$11.40
- **WR** : 1.1%
- **Exposure cumulée** : +$1,098.41
- **Sharpe (ann.)** : -9.27
- **Daily P&L** : ['-$23.39', '-$955.62', '-$34.15', '-$58.65']

## Breakdown alpha × side × price bucket

| Alpha | Side | Bucket | N | P&L | Avg | WR |
|-------|------|--------|---|-----|-----|-----|
| MODEL_VS_MARKET | YES | deep_OTM | 93 | -$1,073.41 | -$11.54 | 0.0% |

## Edge distribution (MODEL_VS_MARKET)

| Edge range | N | P&L | Avg | WR |
|------------|---|-----|-----|-----|
| low (4-8%) | 10 | -$65.00 | -$6.50 | 10.0% |
| mid (8-15%) | 68 | -$725.25 | -$10.67 | 0.0% |
| high (15-30%) | 16 | -$281.56 | -$17.60 | 0.0% |

## TTR (time-to-resolution) analysis

| TTR bucket | N | P&L | Avg | WR |
|-----------|---|-----|-----|-----|
| 12-24h | 14 | -$116.19 | -$8.30 | 7.1% |
| 24-48h | 80 | -$955.62 | -$11.95 | 0.0% |

## σ bias — model vs empirical

- σ_c predicted avg : **1.28°C**
- Predicted YES rate : 18.8%
- Actual YES rate : 0.0%
- **Calibration bias ratio** : 0.00 (over-predicts YES)

## Top 5 wins

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-19 16:29:09 | MODEL_VS_MARKET | NO | 0.940 | 0.990 | 5.0% | $25.0 | +$1.60 |
| 2026-04-17 20:07:03 | MODEL_VS_MARKET | YES | 0.062 | 0.132 | 6.9% | $6.3 | -$6.35 |
| 2026-04-19 16:29:03 | MODEL_VS_MARKET | YES | 0.060 | 0.130 | 7.0% | $7.3 | -$7.26 |
| 2026-04-19 15:53:44 | MODEL_VS_MARKET | YES | 0.055 | 0.130 | 7.5% | $7.5 | -$7.45 |
| 2026-04-19 16:13:55 | MODEL_VS_MARKET | YES | 0.055 | 0.130 | 7.5% | $7.5 | -$7.45 |

## Top 5 losses

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-17 19:36:46 | MODEL_VS_MARKET | YES | 0.050 | 0.242 | 19.2% | $20.4 | -$20.41 |
| 2026-04-17 19:34:51 | MODEL_VS_MARKET | YES | 0.050 | 0.242 | 19.2% | $18.3 | -$18.26 |
| 2026-04-17 19:35:23 | MODEL_VS_MARKET | YES | 0.050 | 0.242 | 19.2% | $18.3 | -$18.26 |
| 2026-04-17 19:41:48 | MODEL_VS_MARKET | YES | 0.045 | 0.242 | 19.7% | $18.3 | -$18.26 |
| 2026-04-17 20:27:15 | MODEL_VS_MARKET | YES | 0.045 | 0.242 | 19.7% | $18.3 | -$18.26 |

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/city-optimization]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]