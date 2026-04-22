# Seoul — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **1,013** markets analysés
- **696,480** trades on-chain
- **$5.92M** volume total USDC
- Période : 2025-12-06 → 2026-04-08

## Outcomes

- YES wins : **122** (12.1%)
- NO wins : **887**
- Ambiguous : 4

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0600 | 0.2000 | 0.3800 | 0.1350 | 0.1653 |
| `price_mid_avg` | 0.0016 | 0.0050 | 0.0300 | 0.1657 | 0.4947 | 0.1465 | 0.2463 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.9990 | 0.1218 | 0.3248 |
| `drift_pp` | -0.2990 | -0.1490 | -0.0290 | -0.0090 | 0.5270 | -0.0132 | 0.3125 |
| `volatility_pp` | 0.0058 | 0.0140 | 0.0464 | 0.1314 | 0.2587 | 0.0893 | 0.1019 |
| `max_drawdown` | -0.7142 | -0.4890 | -0.2490 | -0.0780 | -0.0272 | -0.3107 | 0.2643 |
| `hurst` | 0.0296 | 0.0916 | 0.1649 | 0.2665 | 0.3702 | 0.1813 | 0.1312 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.7083 | 2.497 | 8.391 | 3.636 | 10.259 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 577 | 4.0% | -0.0190 |
| [0.1, 0.2) | 174 | 14.4% | -0.1210 |
| [0.2, 0.3) | 116 | 25.9% | -0.2190 |
| [0.3, 0.4) | 52 | 25.0% | -0.3390 |
| [0.4, 0.5) | 45 | 31.1% | -0.4090 |
| [0.5, 0.6) | 27 | 33.3% | -0.4990 |
| [0.6, 0.7) | 8 | 12.5% | -0.6890 |
| [0.7, 0.8) | 1 | 100.0% | 0.2651 |
| [0.8, 0.9) | 2 | 0.0% | -0.8538 |
| [0.9, 1.0) | 7 | 85.7% | 0.0341 |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 767 | 13.5% | 0.0900 | -0.0490 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **23** trades, WR=4.0%
- **Favorite losses** (open>0.90 + NO win) : **1** trades, WR=20.0%

- Long-shot payoff moyen : +0.956 pp

## Patterns temporels

- **Heures peak (UTC)** : [4, 3, 5] (155,566 trades)
- **Heures calmes (UTC)** : [19, 21, 18] (50,173 trades)
- **Jours peak** : ['Thu', 'Mon']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0729 | 0.0269 | 63.822 |
| [0.25-0.50] | 0.0687 | 0.0199 | 88.444 |
| [0.50-0.75] | 0.0443 | 0.0197 | 165.469 |
| [0.75-1.00] | 0.0183 | 0.0165 | 393.198 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 292 | -0.1990 | 0.1262 | 0.2482 | -0.5990 | 1.4% |
| 1 | 115 | 0.7590 | 0.3080 | 0.3301 | -0.4700 | 100.0% |
| 2 | 596 | -0.0275 | 0.0184 | 0.1182 | -0.0990 | 0.5% |

## Volume profile

- Trade size : médian $1, p90 $7, p99 $100
- Total volume USDC : $5.92M
- Trades total : 696,480

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/seoul.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
