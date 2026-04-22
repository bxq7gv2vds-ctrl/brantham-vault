# Busan — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **66** markets analysés
- **12,822** trades on-chain
- **$58k** volume total USDC
- Période : 2026-04-03 → 2026-04-08

## Outcomes

- YES wins : **6** (9.2%)
- NO wins : **59**
- Ambiguous : 1

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0600 | 0.1775 | 0.3500 | 0.1220 | 0.1359 |
| `price_mid_avg` | 0.0030 | 0.0069 | 0.0348 | 0.0737 | 0.5384 | 0.1411 | 0.2598 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.0065 | 0.0920 | 0.2890 |
| `drift_pp` | -0.2440 | -0.1590 | -0.0330 | -0.0090 | -0.0085 | -0.0300 | 0.2606 |
| `volatility_pp` | 0.0076 | 0.0127 | 0.0297 | 0.0905 | 0.2183 | 0.0710 | 0.0926 |
| `max_drawdown` | -0.5140 | -0.3768 | -0.1540 | -0.0512 | -0.0290 | -0.2355 | 0.2325 |
| `hurst` | 0.0343 | 0.0894 | 0.1366 | 0.2365 | 0.3251 | 0.1565 | 0.1311 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.5030 | 0.2201 | 0.8516 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 38 | 2.6% | -0.0190 |
| [0.1, 0.2) | 16 | 6.2% | -0.1590 |
| [0.2, 0.3) | 4 | 25.0% | -0.2440 |
| [0.3, 0.4) | 1 | 0.0% | -0.3490 |
| [0.4, 0.5) | 4 | 50.0% | 0.0650 |
| [0.5, 0.6) | 2 | 50.0% | 0.0000 |
| [0.6, 0.7) | 0 | — | — |
| [0.7, 0.8) | 0 | — | — |
| [0.8, 0.9) | 0 | — | — |
| [0.9, 1.0) | 0 | — | — |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 54 | 11.3% | 0.1100 | -0.0590 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **1** trades, WR=2.6%
- **Favorite losses** (open>0.90 + NO win) : **0** trades, WR=0.0%

- Long-shot payoff moyen : +0.929 pp

## Patterns temporels

- **Heures peak (UTC)** : [6, 5, 7] (5,289 trades)
- **Heures calmes (UTC)** : [21, 18, 23] (249 trades)
- **Jours peak** : ['Sun', 'Sat']
- **Mois pic activité** : mois 4

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0452 | 0.0200 | 11.934 |
| [0.25-0.50] | 0.0360 | 0.0169 | 12.722 |
| [0.50-0.75] | 0.0308 | 0.0099 | 31.738 |
| [0.75-1.00] | 0.0174 | 0.0148 | 145.523 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 5 | 0.7790 | 0.3295 | 0.3426 | -0.4400 | 100.0% |
| 1 | 44 | -0.0190 | 0.0178 | 0.1211 | -0.0715 | 2.3% |
| 2 | 17 | -0.1790 | 0.1078 | 0.2284 | -0.4980 | 0.0% |

## Volume profile

- Trade size : médian $0, p90 $5, p99 $56
- Total volume USDC : $58k
- Trades total : 12,822

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/busan.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
