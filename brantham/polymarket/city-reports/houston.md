---
name: Houston — deep dive
description: Analyse empirique complète Polymarket weather. Performance, calibration, σ bias, TTR, top trades, verdict.
type: city-report
project: brantham/polymarket
date: 2026-04-21
verdict: KEEP
tags: [polymarket, city, houston, keep]
---

# Houston — deep dive

**Verdict: KEEP** — Steady: $293 on 95 trades

## Identité

- ICAO : `KIAH`
- Coords : 29.9844, -95.3414
- Country / TZ : US / America/Chicago
- UTC offset : -5.0h
- Elevation : 30.0 m

## Configuration

- **Status** : ENABLED
- **Kelly fraction** : 0.5
- **N outcomes** : 95
- **Notes** : kelly from N=95 WR=89.5% (emp 0.612 → blended 0.500)
- **Updated** : 2026-04-21

## Calibrator (isotonic)

_No calibrator fit for this city → falls back to global calibrator._

## Performance empirique

- **Signaux émis** : 121
- **Outcomes réconciliés** : 95
- **P&L total** : +$292.50
- **Avg / trade** : +$3.08
- **WR** : 89.5%
- **Exposure cumulée** : +$1,448.37
- **Sharpe (ann.)** : 12.47
- **Daily P&L** : ['+$237.13', '-$0.38', '+$55.75']

## Breakdown alpha × side × price bucket

| Alpha | Side | Bucket | N | P&L | Avg | WR |
|-------|------|--------|---|-----|-----|-----|
| MODEL_VS_MARKET | NO | ITM | 61 | +$252.27 | +$4.14 | 100.0% |
| MODEL_VS_MARKET | NO | mid | 16 | +$125.66 | +$7.85 | 100.0% |
| CONFIRMED_NO | NO | ITM | 8 | +$0.00 | +$0.00 | 0.0% |
| CONFIRMED_YES | YES | mid | 18 | +$0.00 | +$0.00 | 0.0% |
| MODEL_VS_MARKET | YES | OTM | 2 | -$11.08 | -$5.54 | 0.0% |
| MODEL_VS_MARKET | NO | deep_ITM | 15 | -$59.57 | -$3.97 | 53.3% |

## Edge distribution (MODEL_VS_MARKET)

| Edge range | N | P&L | Avg | WR |
|------------|---|-----|-----|-----|
| low (4-8%) | 18 | -$71.90 | -$3.99 | 55.6% |
| mid (8-15%) | 13 | +$62.06 | +$4.77 | 100.0% |
| high (15-30%) | 54 | +$220.05 | +$4.07 | 96.3% |
| extreme (>30%) | 10 | +$82.30 | +$8.23 | 100.0% |

## TTR (time-to-resolution) analysis

| TTR bucket | N | P&L | Avg | WR |
|-----------|---|-----|-----|-----|
| 12-24h | 21 | +$103.45 | +$4.93 | 100.0% |
| 24-48h | 66 | +$249.41 | +$3.78 | 95.5% |
| >48h | 8 | -$60.36 | -$7.55 | 12.5% |

## σ bias — model vs empirical

- σ_c predicted avg : **2.10°C**
- Predicted YES rate : 92.0%
- Actual YES rate : 7.4%
- **Calibration bias ratio** : 0.08 (over-predicts YES)

## Top 5 wins

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-17 19:35:23 | MODEL_VS_MARKET | NO | 0.770 | 0.894 | 12.4% | $63.9 | +$19.09 |
| 2026-04-17 14:40:06 | MODEL_VS_MARKET | NO | 0.785 | 0.894 | 10.9% | $50.0 | +$13.69 |
| 2026-04-19 17:04:21 | MODEL_VS_MARKET | NO | 0.590 | 0.906 | 31.6% | $13.4 | +$9.33 |
| 2026-04-19 17:24:44 | MODEL_VS_MARKET | NO | 0.590 | 0.906 | 31.6% | $13.4 | +$9.33 |
| 2026-04-18 16:23:04 | MODEL_VS_MARKET | NO | 0.575 | 0.881 | 30.6% | $11.8 | +$8.70 |

## Top 5 losses

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-17 14:40:06 | MODEL_VS_MARKET | YES | 0.020 | 0.078 | 5.8% | $14.8 | -$14.78 |
| 2026-04-18 08:49:46 | MODEL_VS_MARKET | NO | 0.929 | 0.983 | 5.4% | $10.3 | -$10.29 |
| 2026-04-18 09:10:43 | MODEL_VS_MARKET | NO | 0.928 | 0.983 | 5.5% | $10.3 | -$10.29 |
| 2026-04-18 08:55:48 | MODEL_VS_MARKET | NO | 0.929 | 0.983 | 5.4% | $10.0 | -$10.00 |
| 2026-04-18 09:01:54 | MODEL_VS_MARKET | NO | 0.928 | 0.983 | 5.5% | $10.0 | -$10.00 |

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/city-optimization]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]