---
name: Atlanta — deep dive
description: Analyse empirique complète Polymarket weather. Performance, calibration, σ bias, TTR, top trades, verdict.
type: city-report
project: brantham/polymarket
date: 2026-04-21
verdict: SCALE
tags: [polymarket, city, atlanta, scale]
---

# Atlanta — deep dive

**Verdict: SCALE** — Star performer: $1061, avg $8.10, kelly boost recommandé

## Identité

- ICAO : `KATL`
- Coords : 33.6367, -84.4281
- Country / TZ : US / America/New_York
- UTC offset : -4.0h
- Elevation : 313.0 m

## Configuration

- **Status** : ENABLED
- **Kelly fraction** : 0.5
- **N outcomes** : 131
- **Notes** : kelly from N=120 WR=100.0% (emp 1.000 → blended 0.500)
- **Updated** : 2026-04-21

## Calibrator (isotonic)

- N train : 89
- ECE before : 0.0312 → after : 0.0100
- Brier before : 0.0041 → after : 0.0001
- Fitted : 2026-04-21 02:20

## Performance empirique

- **Signaux émis** : 144
- **Outcomes réconciliés** : 131
- **P&L total** : +$1,061.21
- **Avg / trade** : +$8.10
- **WR** : 100.0%
- **Exposure cumulée** : +$2,526.93
- **Sharpe (ann.)** : 40.86
- **Daily P&L** : ['+$208.72', '+$346.23', '+$148.68', '+$357.59']

## Breakdown alpha × side × price bucket

| Alpha | Side | Bucket | N | P&L | Avg | WR |
|-------|------|--------|---|-----|-----|-----|
| MODEL_VS_MARKET | NO | mid | 62 | +$666.15 | +$11.10 | 100.0% |
| MODEL_VS_MARKET | NO | ITM | 50 | +$351.26 | +$7.17 | 100.0% |
| CONFIRMED_NO | NO | ITM | 16 | +$24.48 | +$2.23 | 100.0% |
| MODEL_VS_MARKET | NO | deep_ITM | 11 | +$19.33 | +$1.76 | 100.0% |
| MODEL_VS_MARKET | YES | OTM | 5 | +$0.00 | +$0.00 | 0.0% |

## Edge distribution (MODEL_VS_MARKET)

| Edge range | N | P&L | Avg | WR |
|------------|---|-----|-----|-----|
| mid (8-15%) | 12 | +$21.84 | +$1.82 | 100.0% |
| high (15-30%) | 78 | +$710.99 | +$9.12 | 100.0% |
| extreme (>30%) | 30 | +$303.91 | +$10.13 | 100.0% |

## TTR (time-to-resolution) analysis

| TTR bucket | N | P&L | Avg | WR |
|-----------|---|-----|-----|-----|
| 0-6h | 11 | +$24.48 | +$2.23 | 100.0% |
| 6-12h | 4 | +$49.73 | +$12.43 | 100.0% |
| 12-24h | 48 | +$561.94 | +$11.71 | 100.0% |
| 24-48h | 67 | +$416.46 | +$6.22 | 100.0% |
| >48h | 1 | +$8.61 | +$8.61 | 100.0% |

## σ bias — model vs empirical

- σ_c predicted avg : **1.12°C**
- Predicted YES rate : 94.7%
- Actual YES rate : 0.0%
- **Calibration bias ratio** : 0.00 (over-predicts YES)

## Top 5 wins

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-19 16:59:17 | MODEL_VS_MARKET | NO | 0.565 | 0.841 | 27.6% | $22.4 | +$17.22 |
| 2026-04-19 17:24:44 | MODEL_VS_MARKET | NO | 0.570 | 0.841 | 27.1% | $22.4 | +$16.87 |
| 2026-04-17 21:43:27 | MODEL_VS_MARKET | NO | 0.580 | 0.889 | 30.9% | $21.3 | +$15.44 |
| 2026-04-17 21:48:30 | MODEL_VS_MARKET | NO | 0.585 | 0.889 | 30.4% | $21.3 | +$15.12 |
| 2026-04-17 21:53:33 | MODEL_VS_MARKET | NO | 0.585 | 0.889 | 30.4% | $21.3 | +$15.12 |

## Top 5 losses

| Time | Alpha | Side | Entry | Model | Edge | Size | P&L |
|------|-------|------|-------|-------|------|------|-----|
| 2026-04-17 20:37:21 | MODEL_VS_MARKET | NO | 0.905 | 1.000 | 9.5% | $14.8 | +$1.55 |
| 2026-04-18 06:12:36 | CONFIRMED_NO | NO | 0.845 | 1.000 | 15.5% | $9.1 | +$1.68 |
| 2026-04-18 06:18:17 | CONFIRMED_NO | NO | 0.845 | 1.000 | 15.5% | $9.1 | +$1.68 |
| 2026-04-18 06:24:14 | CONFIRMED_NO | NO | 0.845 | 1.000 | 15.5% | $9.1 | +$1.68 |
| 2026-04-17 20:02:00 | MODEL_VS_MARKET | NO | 0.910 | 1.000 | 9.0% | $17.1 | +$1.69 |

## Related

- [[brantham/polymarket/_MOC]]
- [[brantham/polymarket/city-optimization]]
- [[brantham/polymarket/MODEL-STATE-COMPLETE]]