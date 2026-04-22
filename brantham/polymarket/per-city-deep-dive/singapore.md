# Singapore — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **280** markets analysés
- **153,985** trades on-chain
- **$823k** volume total USDC
- Période : 2026-03-13 → 2026-04-08

## Outcomes

- YES wins : **25** (9.0%)
- NO wins : **254**
- Ambiguous : 1

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0100 | 0.0300 | 0.1700 | 0.3200 | 0.1041 | 0.1268 |
| `price_mid_avg` | 0.0016 | 0.0026 | 0.0132 | 0.1000 | 0.3920 | 0.1078 | 0.1877 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.0051 | 0.0938 | 0.2901 |
| `drift_pp` | -0.2890 | -0.1190 | -0.0190 | -0.0090 | -0.0079 | -0.0103 | 0.2727 |
| `volatility_pp` | 0.0028 | 0.0062 | 0.0217 | 0.0774 | 0.1867 | 0.0616 | 0.0891 |
| `max_drawdown` | -0.5810 | -0.3592 | -0.1490 | -0.0390 | -0.0149 | -0.2254 | 0.2299 |
| `hurst` | 0.0595 | 0.1009 | 0.1624 | 0.2550 | 0.3366 | 0.1836 | 0.1076 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.0000 | 0.5110 | 3.114 | 1.459 | 4.938 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 180 | 1.7% | -0.0090 |
| [0.1, 0.2) | 34 | 17.6% | -0.1368 |
| [0.2, 0.3) | 32 | 18.8% | -0.2238 |
| [0.3, 0.4) | 26 | 26.9% | -0.3190 |
| [0.4, 0.5) | 5 | 60.0% | 0.5364 |
| [0.5, 0.6) | 1 | 0.0% | -0.4990 |
| [0.6, 0.7) | 1 | 0.0% | -0.6990 |
| [0.7, 0.8) | 0 | — | — |
| [0.8, 0.9) | 0 | — | — |
| [0.9, 1.0) | 0 | — | — |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 126 | 0.8% | 0.0200 | -0.0190 |
| cold | 102 | 23.8% | 0.2000 | -0.1035 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **3** trades, WR=1.7%
- **Favorite losses** (open>0.90 + NO win) : **0** trades, WR=0.0%

- Long-shot payoff moyen : +0.972 pp

## Patterns temporels

- **Heures peak (UTC)** : [6, 7, 5] (34,270 trades)
- **Heures calmes (UTC)** : [20, 23, 21] (10,870 trades)
- **Jours peak** : ['Mon', 'Wed']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0409 | 0.0213 | 68.867 |
| [0.25-0.50] | 0.0269 | 0.0114 | 55.843 |
| [0.50-0.75] | 0.0194 | 0.0094 | 116.986 |
| [0.75-1.00] | 0.0088 | 0.0078 | 310.258 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 201 | -0.0190 | 0.0124 | 0.1278 | -0.0760 | 0.0% |
| 1 | 26 | 0.7190 | 0.2990 | 0.3350 | -0.4728 | 100.0% |
| 2 | 53 | -0.2690 | 0.1091 | 0.2674 | -0.4990 | 0.0% |

## Volume profile

- Trade size : médian $0, p90 $5, p99 $60
- Total volume USDC : $823k
- Trades total : 153,985

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/singapore.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
