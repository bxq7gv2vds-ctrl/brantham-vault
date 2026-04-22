# Chongqing — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **209** markets analysés
- **68,986** trades on-chain
- **$313k** volume total USDC
- Période : 2026-03-20 → 2026-04-08

## Outcomes

- YES wins : **19** (9.1%)
- NO wins : **189**
- Ambiguous : 1

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0400 | 0.1700 | 0.2991 | 0.1077 | 0.1352 |
| `price_mid_avg` | 0.0020 | 0.0040 | 0.0200 | 0.1180 | 0.3607 | 0.1107 | 0.2030 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.0062 | 0.0920 | 0.2874 |
| `drift_pp` | -0.2690 | -0.1190 | -0.0290 | -0.0090 | -0.0018 | -0.0157 | 0.2876 |
| `volatility_pp` | 0.0044 | 0.0104 | 0.0372 | 0.0966 | 0.2173 | 0.0760 | 0.0975 |
| `max_drawdown` | -0.5942 | -0.3700 | -0.1790 | -0.0490 | -0.0190 | -0.2429 | 0.2234 |
| `hurst` | 0.0501 | 0.1029 | 0.1920 | 0.2697 | 0.3573 | 0.1932 | 0.1241 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.1496 | 1.026 | 3.629 | 6.726 | 63.182 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 135 | 2.2% | -0.0190 |
| [0.1, 0.2) | 33 | 21.2% | -0.1390 |
| [0.2, 0.3) | 20 | 20.0% | -0.2342 |
| [0.3, 0.4) | 11 | 45.5% | -0.3150 |
| [0.4, 0.5) | 2 | 0.0% | -0.4440 |
| [0.5, 0.6) | 5 | 0.0% | -0.4990 |
| [0.6, 0.7) | 1 | 0.0% | -0.6753 |
| [0.7, 0.8) | 1 | 0.0% | -0.7890 |
| [0.8, 0.9) | 0 | — | — |
| [0.9, 1.0) | 0 | — | — |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 170 | 10.7% | 0.0500 | -0.0390 |
| cold | 1 | 0.0% | 0.0100 | -0.0080 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **3** trades, WR=2.2%
- **Favorite losses** (open>0.90 + NO win) : **0** trades, WR=0.0%

- Long-shot payoff moyen : +0.970 pp

## Patterns temporels

- **Heures peak (UTC)** : [7, 8, 6] (20,776 trades)
- **Heures calmes (UTC)** : [19, 18, 20] (2,677 trades)
- **Jours peak** : ['Mon', 'Fri']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0547 | 0.0194 | 25.055 |
| [0.25-0.50] | 0.0560 | 0.0159 | 38.172 |
| [0.50-0.75] | 0.0330 | 0.0143 | 72.202 |
| [0.75-1.00] | 0.0107 | 0.0089 | 198.665 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 56 | -0.1690 | 0.1084 | 0.2678 | -0.4655 | 0.0% |
| 1 | 19 | 0.8190 | 0.3344 | 0.3399 | -0.3460 | 100.0% |
| 2 | 130 | -0.0190 | 0.0161 | 0.1463 | -0.0790 | 0.0% |

## Volume profile

- Trade size : médian $0, p90 $5, p99 $71
- Total volume USDC : $313k
- Trades total : 68,986

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/chongqing.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
