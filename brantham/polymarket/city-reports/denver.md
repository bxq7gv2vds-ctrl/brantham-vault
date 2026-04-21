---
name: Denver — deep dive
description: Analyse empirique complète Polymarket weather. Performance, calibration, σ bias, TTR, top trades, verdict.
type: city-report
project: brantham/polymarket
date: 2026-04-21
verdict: KEEP
tags: [polymarket, city, denver, keep]
---

# Denver — deep dive

**Verdict: KEEP** — Steady: $213 on 100 trades

## Identité

- ICAO : `KDEN`
- Coords : 39.8617, -104.6731
- Country / TZ : US / America/Denver
- UTC offset : -6.0h
- Elevation : 1656.0 m

## Configuration

- **Status** : ENABLED
- **Kelly fraction** : 0.5
- **N outcomes** : 100
- **Notes** : kelly from N=70 WR=100.0% (emp 1.000 → blended 0.500)
- **Updated** : 2026-04-21

## Calibrator (isotonic)

- N train : 70
- ECE before : 0.0518 → after : 0.0100
- Brier before : 0.0073 → after : 0.0001
- Fitted : 2026-04-21 02:20

## Performance empirique

- **Signaux émis** : 100
- **Outcomes réconciliés** : 100
- **P&L total** : +$212.74
- **Avg / trade** : +$2.13
- **WR** : 100.0%
- **Exposure cumulée** : +$1,047.06
- **Sharpe (ann.)** : 14.73
- **Daily P&L** : ['+$28.16', '+$159.15', '+$25.44']

## Breakdown alpha × side × price bucket

| Alpha | Side | Bucket | N | P&L | Avg | WR |
|-------|------|--------|---|-----|-----|-----|
| MODEL_VS_MARKET | NO | ITM | 69 | +$152.27 | +$2.21 | 100.0% |
| CONFIRMED_NO | NO | ITM | 30 | +$59.98 | +$2.00 | 100.0% |

## Edge distribution (MODEL_VS_MARKET)

| Edge range | N | P&L | Avg | WR |
|------------|---|-----|-----|-----|
| low (4-8%) | 19 | +$49.15 | +$2.59 | 100.0% |
| mid (8-15%) | 38 | +$75.59 | +$1.99 | 100.0% |
| high (15-30%) | 13 | +$28.02 | +$2.16 | 100.0% |

## TTR (time-to-resolution) analysis

| TTR bucket | N | P&L | Avg | WR |
|-----------|---|-----|-----|-----|
| 0-6h | 10 | +$24.05 | +$2.40 | 100.0% |
| 6-12h | 20 | +$35.93 | +$1.80 | 100.0% |
| 12-24h | 13 | +$25.44 | +$1.96 | 100.0% |
| 24-48h | 57 | +$127.32 | +$2.23 | 100.0% |

## σ bias — model vs empirical

- σ_c predicted avg : **0.90°C**
- Predicted YES rate : 94.8%
- Actual YES rate : 0.0%
- **Calibration bias ratio** : 0.00 (over-predicts YES)

## Top 5 wins

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-17 19:35:23 | MODEL_VS_MARKET | NO | 0.820 | 0.897 | 7.7% | $73.0 | +$16.03 |
| 2026-04-17 14:44:59 | MODEL_VS_MARKET | NO | 0.790 | 0.897 | 10.7% | $14.8 | +$3.92 |
| 2026-04-18 09:10:43 | CONFIRMED_NO | NO | 0.805 | 1.000 | 19.5% | $13.4 | +$3.24 |
| 2026-04-18 09:47:35 | CONFIRMED_NO | NO | 0.810 | 1.000 | 19.0% | $12.7 | +$2.97 |
| 2026-04-18 06:24:14 | CONFIRMED_NO | NO | 0.815 | 1.000 | 18.5% | $10.9 | +$2.48 |

## Top 5 losses

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-17 20:07:03 | MODEL_VS_MARKET | NO | 0.954 | 1.000 | 4.6% | $10.3 | +$0.50 |
| 2026-04-18 03:21:44 | CONFIRMED_NO | NO | 0.890 | 1.000 | 11.0% | $5.8 | +$0.71 |
| 2026-04-18 02:08:10 | CONFIRMED_NO | NO | 0.860 | 1.000 | 14.0% | $7.0 | +$1.14 |
| 2026-04-18 02:19:50 | CONFIRMED_NO | NO | 0.850 | 1.000 | 15.0% | $7.3 | +$1.28 |
| 2026-04-18 02:25:36 | CONFIRMED_NO | NO | 0.850 | 1.000 | 15.0% | $7.5 | +$1.32 |

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/city-optimization]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]