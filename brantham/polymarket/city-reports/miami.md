---
name: Miami — deep dive
description: Analyse empirique complète Polymarket weather. Performance, calibration, σ bias, TTR, top trades, verdict.
type: city-report
project: brantham/polymarket
date: 2026-04-21
verdict: DISABLE
tags: [polymarket, city, miami, disable]
---

# Miami — deep dive

**Verdict: DISABLE** — P&L $-162, WR 77% — kill recommended

## Identité

- ICAO : `KMIA`
- Coords : 25.7932, -80.2906
- Country / TZ : US / America/New_York
- UTC offset : -4.0h
- Elevation : 2.0 m

## Configuration

- **Status** : SHADOW
- **Kelly fraction** : 0.5
- **N outcomes** : 82
- **Notes** : kelly from N=54 WR=98.1% (emp 0.918 → blended 0.500)
- **Updated** : 2026-04-21

## Calibrator (isotonic)

- N train : 40
- ECE before : 0.0534 → after : 0.0308
- Brier before : 0.0255 → after : 0.0276
- Fitted : 2026-04-21 02:20

## Performance empirique

- **Signaux émis** : 90
- **Outcomes réconciliés** : 82
- **P&L total** : -$162.07
- **Avg / trade** : -$1.98
- **WR** : 76.8%
- **Exposure cumulée** : +$816.37
- **Sharpe (ann.)** : -6.58
- **Daily P&L** : ['-$168.86', '-$64.10', '+$29.59', '+$41.31']

## Breakdown alpha × side × price bucket

| Alpha | Side | Bucket | N | P&L | Avg | WR |
|-------|------|--------|---|-----|-----|-----|
| MODEL_VS_MARKET | NO | mid | 13 | +$51.75 | +$3.98 | 100.0% |
| MODEL_VS_MARKET | NO | ITM | 41 | +$14.80 | +$0.36 | 97.6% |
| CONFIRMED_NO | NO | ITM | 17 | +$10.30 | +$1.03 | 100.0% |
| CONFIRMED_YES | YES | mid | 18 | -$238.92 | -$13.27 | 0.0% |

## Edge distribution (MODEL_VS_MARKET)

| Edge range | N | P&L | Avg | WR |
|------------|---|-----|-----|-----|
| mid (8-15%) | 26 | +$27.73 | +$1.07 | 100.0% |
| high (15-30%) | 25 | +$19.99 | +$0.80 | 96.0% |
| extreme (>30%) | 3 | +$18.82 | +$6.27 | 100.0% |

## TTR (time-to-resolution) analysis

| TTR bucket | N | P&L | Avg | WR |
|-----------|---|-----|-----|-----|
| 0-6h | 8 | +$8.00 | +$1.00 | 100.0% |
| 6-12h | 20 | -$236.62 | -$11.83 | 10.0% |
| 12-24h | 26 | +$82.68 | +$3.18 | 100.0% |
| 24-48h | 28 | -$16.13 | -$0.58 | 96.4% |

## σ bias — model vs empirical

- σ_c predicted avg : **1.52°C**
- Predicted YES rate : 92.7%
- Actual YES rate : 1.9%
- **Calibration bias ratio** : 0.02 (over-predicts YES)

## Top 5 wins

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-18 13:02:21 | MODEL_VS_MARKET | NO | 0.565 | 0.884 | 31.9% | $8.2 | +$6.34 |
| 2026-04-18 13:07:24 | MODEL_VS_MARKET | NO | 0.565 | 0.884 | 31.9% | $8.2 | +$6.34 |
| 2026-04-18 11:56:41 | MODEL_VS_MARKET | NO | 0.565 | 0.886 | 32.1% | $8.0 | +$6.14 |
| 2026-04-19 15:46:09 | MODEL_VS_MARKET | NO | 0.570 | 0.775 | 20.5% | $5.6 | +$4.22 |
| 2026-04-19 15:48:42 | MODEL_VS_MARKET | NO | 0.570 | 0.775 | 20.5% | $5.6 | +$4.22 |

## Top 5 losses

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-17 14:40:06 | MODEL_VS_MARKET | NO | 0.715 | 0.895 | 18.0% | $50.0 | -$50.00 |
| 2026-04-18 00:09:49 | CONFIRMED_YES | YES | 0.535 | 1.000 | 46.5% | $15.1 | -$15.08 |
| 2026-04-18 00:14:52 | CONFIRMED_YES | YES | 0.525 | 1.000 | 47.5% | $15.1 | -$15.08 |
| 2026-04-18 00:19:55 | CONFIRMED_YES | YES | 0.520 | 1.000 | 48.0% | $15.1 | -$15.08 |
| 2026-04-18 02:13:54 | CONFIRMED_YES | YES | 0.535 | 1.000 | 46.5% | $15.1 | -$15.08 |

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/city-optimization]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]