# Toronto — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **1,024** markets analysés
- **357,387** trades on-chain
- **$2.00M** volume total USDC
- Période : 2025-12-06 → 2026-04-08

## Outcomes

- YES wins : **101** (10.5%)
- NO wins : **858**
- Ambiguous : 65

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0600 | 0.1860 | 0.3716 | 0.1357 | 0.1707 |
| `price_mid_avg` | 0.0010 | 0.0038 | 0.0300 | 0.1827 | 0.4642 | 0.1442 | 0.2378 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0020 | 0.9990 | 0.1232 | 0.3253 |
| `drift_pp` | -0.3017 | -0.1290 | -0.0295 | -0.0090 | 0.4990 | -0.0125 | 0.3150 |
| `volatility_pp` | 0.0043 | 0.0104 | 0.0393 | 0.1106 | 0.2562 | 0.0821 | 0.0991 |
| `max_drawdown` | -0.6875 | -0.4183 | -0.1961 | -0.0526 | -0.0190 | -0.2746 | 0.2582 |
| `hurst` | 0.0159 | 0.0857 | 0.1608 | 0.2583 | 0.3454 | 0.1702 | 0.1330 |
| `half_life_minutes` | 0.0000 | 0.1448 | 0.9905 | 4.418 | 16.598 | 7.443 | 23.566 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 570 | 3.3% | -0.0190 |
| [0.1, 0.2) | 179 | 14.0% | -0.1190 |
| [0.2, 0.3) | 87 | 24.1% | -0.2090 |
| [0.3, 0.4) | 52 | 19.2% | -0.3290 |
| [0.4, 0.5) | 22 | 31.8% | -0.3990 |
| [0.5, 0.6) | 29 | 37.9% | -0.4990 |
| [0.6, 0.7) | 4 | 25.0% | -0.6290 |
| [0.7, 0.8) | 2 | 50.0% | -0.2457 |
| [0.8, 0.9) | 5 | 40.0% | -0.7990 |
| [0.9, 1.0) | 9 | 44.4% | -0.8990 |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 776 | 9.6% | 0.0800 | -0.0440 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **19** trades, WR=3.3%
- **Favorite losses** (open>0.90 + NO win) : **4** trades, WR=50.0%

- Long-shot payoff moyen : +0.947 pp

## Patterns temporels

- **Heures peak (UTC)** : [18, 4, 20] (56,890 trades)
- **Heures calmes (UTC)** : [2, 6, 1] (33,090 trades)
- **Jours peak** : ['Thu', 'Sat']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0684 | 0.0223 | 32.849 |
| [0.25-0.50] | 0.0592 | 0.0163 | 54.592 |
| [0.50-0.75] | 0.0345 | 0.0166 | 98.336 |
| [0.75-1.00] | 0.0151 | 0.0131 | 177.413 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 250 | -0.1990 | 0.1153 | 0.2350 | -0.5340 | 2.4% |
| 1 | 646 | -0.0290 | 0.0157 | 0.1299 | -0.0890 | 1.1% |
| 2 | 110 | 0.8040 | 0.3052 | 0.2908 | -0.4150 | 97.8% |

## Volume profile

- Trade size : médian $0, p90 $5, p99 $70
- Total volume USDC : $2.00M
- Trades total : 357,387

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/toronto.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
