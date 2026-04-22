# Wellington — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **684** markets analysés
- **312,315** trades on-chain
- **$2.46M** volume total USDC
- Période : 2026-01-22 → 2026-04-08

## Outcomes

- YES wins : **76** (11.1%)
- NO wins : **606**
- Ambiguous : 2

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0600 | 0.2000 | 0.3362 | 0.1312 | 0.1626 |
| `price_mid_avg` | 0.0017 | 0.0050 | 0.0280 | 0.1540 | 0.4441 | 0.1309 | 0.2200 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.9990 | 0.1123 | 0.3137 |
| `drift_pp` | -0.2819 | -0.1392 | -0.0375 | -0.0090 | 0.4000 | -0.0189 | 0.2960 |
| `volatility_pp` | 0.0042 | 0.0120 | 0.0338 | 0.1035 | 0.2277 | 0.0771 | 0.0957 |
| `max_drawdown` | -0.6480 | -0.4115 | -0.1850 | -0.0580 | -0.0190 | -0.2642 | 0.2423 |
| `hurst` | 0.0446 | 0.1004 | 0.1689 | 0.2467 | 0.3362 | 0.1800 | 0.1139 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.2362 | 1.380 | 6.970 | 3.425 | 25.638 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 388 | 2.1% | -0.0190 |
| [0.1, 0.2) | 117 | 11.1% | -0.1290 |
| [0.2, 0.3) | 86 | 30.2% | -0.2090 |
| [0.3, 0.4) | 42 | 31.0% | -0.3090 |
| [0.4, 0.5) | 19 | 36.8% | -0.3990 |
| [0.5, 0.6) | 12 | 16.7% | -0.5490 |
| [0.6, 0.7) | 10 | 20.0% | -0.6640 |
| [0.7, 0.8) | 2 | 50.0% | -0.2500 |
| [0.8, 0.9) | 3 | 66.7% | 0.1790 |
| [0.9, 1.0) | 3 | 66.7% | 0.0790 |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 532 | 10.4% | 0.0800 | -0.0490 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **8** trades, WR=2.1%
- **Favorite losses** (open>0.90 + NO win) : **1** trades, WR=33.3%

- Long-shot payoff moyen : +0.939 pp

## Patterns temporels

- **Heures peak (UTC)** : [7, 0, 8] (70,443 trades)
- **Heures calmes (UTC)** : [19, 18, 10] (24,845 trades)
- **Jours peak** : ['Mon', 'Wed']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0663 | 0.0259 | 35.825 |
| [0.25-0.50] | 0.0489 | 0.0169 | 55.500 |
| [0.50-0.75] | 0.0359 | 0.0157 | 107.187 |
| [0.75-1.00] | 0.0199 | 0.0167 | 269.582 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 409 | -0.0190 | 0.0156 | 0.1299 | -0.0790 | 0.0% |
| 1 | 192 | -0.1990 | 0.1058 | 0.2324 | -0.4940 | 2.1% |
| 2 | 72 | 0.7390 | 0.3052 | 0.3053 | -0.4200 | 100.0% |

## Volume profile

- Trade size : médian $1, p90 $7, p99 $85
- Total volume USDC : $2.46M
- Trades total : 312,315

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/wellington.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
