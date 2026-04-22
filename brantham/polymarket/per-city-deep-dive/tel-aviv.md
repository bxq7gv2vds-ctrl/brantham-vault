# Tel Aviv — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **307** markets analysés
- **113,903** trades on-chain
- **$2.21M** volume total USDC
- Période : 2026-03-10 → 2026-04-08

## Outcomes

- YES wins : **29** (9.4%)
- NO wins : **278**
- Ambiguous : 0

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0500 | 0.1750 | 0.3200 | 0.1156 | 0.1386 |
| `price_mid_avg` | 0.0020 | 0.0055 | 0.0222 | 0.1320 | 0.3868 | 0.1151 | 0.1919 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.0100 | 0.0954 | 0.2923 |
| `drift_pp` | -0.3090 | -0.1290 | -0.0290 | -0.0100 | -0.0088 | -0.0202 | 0.2916 |
| `volatility_pp` | 0.0042 | 0.0094 | 0.0263 | 0.0870 | 0.2337 | 0.0703 | 0.0937 |
| `max_drawdown` | -0.5606 | -0.3845 | -0.1651 | -0.0590 | -0.0249 | -0.2487 | 0.2260 |
| `hurst` | 0.0405 | 0.0903 | 0.1528 | 0.2454 | 0.3163 | 0.1693 | 0.1080 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.2175 | 0.9300 | 4.104 | 2.171 | 8.721 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 188 | 3.2% | -0.0190 |
| [0.1, 0.2) | 50 | 12.0% | -0.1290 |
| [0.2, 0.3) | 27 | 25.9% | -0.2240 |
| [0.3, 0.4) | 27 | 29.6% | -0.3190 |
| [0.4, 0.5) | 10 | 20.0% | -0.4090 |
| [0.5, 0.6) | 3 | 0.0% | -0.4990 |
| [0.6, 0.7) | 1 | 0.0% | -0.6990 |
| [0.7, 0.8) | 0 | — | — |
| [0.8, 0.9) | 0 | — | — |
| [0.9, 1.0) | 1 | 0.0% | -0.9890 |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 249 | 11.2% | 0.0600 | -0.0390 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **6** trades, WR=3.2%
- **Favorite losses** (open>0.90 + NO win) : **1** trades, WR=100.0%

- Long-shot payoff moyen : +0.944 pp

## Patterns temporels

- **Heures peak (UTC)** : [10, 11, 9] (25,412 trades)
- **Heures calmes (UTC)** : [23, 20, 2] (8,366 trades)
- **Jours peak** : ['Mon', 'Wed']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0638 | 0.0252 | 24.720 |
| [0.25-0.50] | 0.0474 | 0.0205 | 46.432 |
| [0.50-0.75] | 0.0271 | 0.0121 | 98.672 |
| [0.75-1.00] | 0.0134 | 0.0127 | 206.318 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 74 | -0.2640 | 0.1073 | 0.2548 | -0.4890 | 0.0% |
| 1 | 203 | -0.0190 | 0.0140 | 0.1068 | -0.0890 | 0.0% |
| 2 | 29 | 0.7890 | 0.3154 | 0.2824 | -0.4400 | 100.0% |

## Volume profile

- Trade size : médian $0, p90 $5, p99 $100
- Total volume USDC : $2.21M
- Trades total : 113,903

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/tel-aviv.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
