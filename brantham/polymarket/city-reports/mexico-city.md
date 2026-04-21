---
name: Mexico City — deep dive
description: Analyse empirique complète Polymarket weather. Performance, calibration, σ bias, TTR, top trades, verdict.
type: city-report
project: brantham/polymarket
date: 2026-04-21
verdict: KEEP
tags: [polymarket, city, mexico-city, keep]
---

# Mexico City — deep dive

**Verdict: KEEP** — Steady: $215 on 48 trades

## Identité

- ICAO : `MMMX`
- Coords : 19.436, -99.072
- Country / TZ : MX / America/Mexico_City
- UTC offset : -6.0h
- Elevation : 2230.0 m

## Configuration

- **Status** : ENABLED
- **Kelly fraction** : 0.5
- **N outcomes** : 48
- **Notes** : kelly from N=48 WR=95.8% (emp 0.839 → blended 0.500)
- **Updated** : 2026-04-21

## Calibrator (isotonic)

- N train : 17
- ECE before : 0.1119 → after : 0.0100
- Brier before : 0.1105 → after : 0.0001
- Fitted : 2026-04-20 09:36

## Performance empirique

- **Signaux émis** : 51
- **Outcomes réconciliés** : 48
- **P&L total** : +$215.08
- **Avg / trade** : +$4.48
- **WR** : 95.8%
- **Exposure cumulée** : +$674.13
- **Sharpe (ann.)** : 10.70
- **Daily P&L** : ['+$39.78', '-$15.04', '+$190.34']

## Breakdown alpha × side × price bucket

| Alpha | Side | Bucket | N | P&L | Avg | WR |
|-------|------|--------|---|-----|-----|-----|
| MODEL_VS_MARKET | NO | mid | 17 | +$121.40 | +$7.14 | 100.0% |
| MODEL_VS_MARKET | NO | ITM | 31 | +$93.68 | +$3.02 | 93.5% |
| CONFIRMED_NO | NO | ITM | 3 | +$0.00 | +$0.00 | 0.0% |

## Edge distribution (MODEL_VS_MARKET)

| Edge range | N | P&L | Avg | WR |
|------------|---|-----|-----|-----|
| mid (8-15%) | 2 | -$15.04 | -$7.52 | 0.0% |
| high (15-30%) | 32 | +$123.20 | +$3.85 | 100.0% |
| extreme (>30%) | 14 | +$106.92 | +$7.64 | 100.0% |

## TTR (time-to-resolution) analysis

| TTR bucket | N | P&L | Avg | WR |
|-----------|---|-----|-----|-----|
| 12-24h | 33 | +$175.30 | +$5.31 | 93.9% |
| 24-48h | 15 | +$39.78 | +$2.65 | 100.0% |

## σ bias — model vs empirical

- σ_c predicted avg : **1.09°C**
- Predicted YES rate : 99.6%
- Actual YES rate : 4.2%
- **Calibration bias ratio** : 0.04 (over-predicts YES)

## Top 5 wins

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-19 17:49:31 | MODEL_VS_MARKET | NO | 0.690 | 1.000 | 31.0% | $40.8 | +$18.34 |
| 2026-04-19 17:50:03 | MODEL_VS_MARKET | NO | 0.690 | 1.000 | 31.0% | $35.4 | +$15.89 |
| 2026-04-19 17:51:28 | MODEL_VS_MARKET | NO | 0.690 | 1.000 | 31.0% | $35.4 | +$15.89 |
| 2026-04-19 17:45:57 | MODEL_VS_MARKET | NO | 0.690 | 1.000 | 31.0% | $28.9 | +$12.97 |
| 2026-04-19 18:04:33 | MODEL_VS_MARKET | NO | 0.700 | 0.990 | 29.0% | $28.9 | +$12.37 |

## Top 5 losses

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-18 16:23:05 | MODEL_VS_MARKET | NO | 0.845 | 0.969 | 12.4% | $7.7 | -$7.69 |
| 2026-04-18 16:48:51 | MODEL_VS_MARKET | NO | 0.850 | 0.969 | 11.9% | $7.3 | -$7.35 |
| 2026-04-17 23:39:32 | MODEL_VS_MARKET | NO | 0.815 | 0.999 | 18.4% | $7.6 | +$1.73 |
| 2026-04-17 20:47:48 | MODEL_VS_MARKET | NO | 0.830 | 0.991 | 16.1% | $8.5 | +$1.74 |
| 2026-04-17 23:44:35 | MODEL_VS_MARKET | NO | 0.815 | 0.999 | 18.4% | $7.7 | +$1.75 |

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/city-optimization]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]