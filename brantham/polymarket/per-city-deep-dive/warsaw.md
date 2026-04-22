# Warsaw — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **253** markets analysés
- **94,621** trades on-chain
- **$360k** volume total USDC
- Période : 2026-03-16 → 2026-04-08

## Outcomes

- YES wins : **23** (9.1%)
- NO wins : **230**
- Ambiguous : 0

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0100 | 0.0400 | 0.1500 | 0.2980 | 0.1058 | 0.1417 |
| `price_mid_avg` | 0.0018 | 0.0030 | 0.0120 | 0.0880 | 0.3664 | 0.1029 | 0.1982 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.0180 | 0.0925 | 0.2873 |
| `drift_pp` | -0.2490 | -0.1090 | -0.0290 | -0.0090 | 0.0000 | -0.0134 | 0.2654 |
| `volatility_pp` | 0.0030 | 0.0068 | 0.0225 | 0.0733 | 0.1831 | 0.0595 | 0.0840 |
| `max_drawdown` | -0.5170 | -0.3190 | -0.1440 | -0.0390 | -0.0100 | -0.2095 | 0.2185 |
| `hurst` | 0.0414 | 0.1046 | 0.1851 | 0.2711 | 0.3619 | 0.1913 | 0.1224 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.0000 | 0.7265 | 3.013 | 1.245 | 3.934 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 166 | 3.6% | -0.0190 |
| [0.1, 0.2) | 39 | 12.8% | -0.1460 |
| [0.2, 0.3) | 27 | 18.5% | -0.2390 |
| [0.3, 0.4) | 11 | 0.0% | -0.3290 |
| [0.4, 0.5) | 1 | 100.0% | 0.5390 |
| [0.5, 0.6) | 6 | 66.7% | 0.4990 |
| [0.6, 0.7) | 0 | — | — |
| [0.7, 0.8) | 0 | — | — |
| [0.8, 0.9) | 2 | 50.0% | -0.2755 |
| [0.9, 1.0) | 1 | 100.0% | 0.0890 |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 207 | 8.2% | 0.0500 | -0.0390 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **6** trades, WR=3.6%
- **Favorite losses** (open>0.90 + NO win) : **0** trades, WR=0.0%

- Long-shot payoff moyen : +0.942 pp

## Patterns temporels

- **Heures peak (UTC)** : [14, 10, 12] (20,446 trades)
- **Heures calmes (UTC)** : [2, 19, 3] (6,467 trades)
- **Jours peak** : ['Fri', 'Mon']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0539 | 0.0217 | 39.028 |
| [0.25-0.50] | 0.0317 | 0.0116 | 51.555 |
| [0.50-0.75] | 0.0162 | 0.0062 | 96.619 |
| [0.75-1.00] | 0.0054 | 0.0042 | 192.829 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 39 | -0.2290 | 0.1293 | 0.2729 | -0.5390 | 5.1% |
| 1 | 193 | -0.0290 | 0.0149 | 0.1484 | -0.0890 | 2.1% |
| 2 | 17 | 0.8890 | 0.2963 | 0.3608 | -0.4000 | 100.0% |

## Volume profile

- Trade size : médian $0, p90 $4, p99 $46
- Total volume USDC : $360k
- Trades total : 94,621

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/warsaw.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
