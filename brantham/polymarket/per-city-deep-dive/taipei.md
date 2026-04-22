# Taipei — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **253** markets analysés
- **104,476** trades on-chain
- **$643k** volume total USDC
- Période : 2026-03-16 → 2026-04-08

## Outcomes

- YES wins : **23** (9.2%)
- NO wins : **228**
- Ambiguous : 2

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0500 | 0.1800 | 0.3200 | 0.1266 | 0.1764 |
| `price_mid_avg` | 0.0010 | 0.0032 | 0.0110 | 0.1300 | 0.3247 | 0.1157 | 0.2203 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.0100 | 0.0956 | 0.2915 |
| `drift_pp` | -0.2970 | -0.1480 | -0.0290 | -0.0090 | -0.0046 | -0.0310 | 0.3239 |
| `volatility_pp` | 0.0044 | 0.0131 | 0.0540 | 0.1132 | 0.2213 | 0.0852 | 0.0989 |
| `max_drawdown` | -0.7890 | -0.4980 | -0.2890 | -0.0850 | -0.0250 | -0.3348 | 0.2834 |
| `hurst` | 0.0451 | 0.0939 | 0.1641 | 0.2465 | 0.3345 | 0.1760 | 0.1155 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.0000 | 0.4260 | 1.789 | 1.370 | 8.492 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 155 | 6.5% | -0.0190 |
| [0.1, 0.2) | 39 | 7.7% | -0.1390 |
| [0.2, 0.3) | 28 | 14.3% | -0.2190 |
| [0.3, 0.4) | 13 | 30.8% | -0.3190 |
| [0.4, 0.5) | 2 | 0.0% | -0.4500 |
| [0.5, 0.6) | 5 | 20.0% | -0.4990 |
| [0.6, 0.7) | 1 | 0.0% | -0.6490 |
| [0.7, 0.8) | 1 | 0.0% | -0.7790 |
| [0.8, 0.9) | 6 | 16.7% | -0.7985 |
| [0.9, 1.0) | 1 | 0.0% | -0.9690 |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 196 | 8.7% | 0.0750 | -0.0590 |
| cold | 11 | 0.0% | 0.0200 | -0.0190 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **10** trades, WR=6.5%
- **Favorite losses** (open>0.90 + NO win) : **1** trades, WR=100.0%

- Long-shot payoff moyen : +0.963 pp

## Patterns temporels

- **Heures peak (UTC)** : [4, 6, 8] (22,902 trades)
- **Heures calmes (UTC)** : [21, 20, 19] (5,558 trades)
- **Jours peak** : ['Fri', 'Sat']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0749 | 0.0331 | 18.930 |
| [0.25-0.50] | 0.0606 | 0.0190 | 40.388 |
| [0.50-0.75] | 0.0392 | 0.0172 | 104.628 |
| [0.75-1.00] | 0.0104 | 0.0120 | 254.135 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 144 | -0.0190 | 0.0170 | 0.1282 | -0.1000 | 0.0% |
| 1 | 23 | 0.8990 | 0.3601 | 0.3496 | -0.5000 | 100.0% |
| 2 | 86 | -0.1430 | 0.1108 | 0.2072 | -0.5340 | 1.2% |

## Volume profile

- Trade size : médian $0, p90 $5, p99 $96
- Total volume USDC : $643k
- Trades total : 104,476

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/taipei.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
