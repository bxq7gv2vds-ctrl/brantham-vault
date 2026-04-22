# Shanghai — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **280** markets analysés
- **362,233** trades on-chain
- **$2.28M** volume total USDC
- Période : 2026-03-13 → 2026-04-08

## Outcomes

- YES wins : **25** (9.0%)
- NO wins : **254**
- Ambiguous : 1

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0500 | 0.1700 | 0.2720 | 0.1079 | 0.1288 |
| `price_mid_avg` | 0.0012 | 0.0048 | 0.0200 | 0.1470 | 0.3692 | 0.1126 | 0.1806 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.0021 | 0.0937 | 0.2902 |
| `drift_pp` | -0.2390 | -0.1490 | -0.0290 | -0.0090 | -0.0080 | -0.0142 | 0.2936 |
| `volatility_pp` | 0.0061 | 0.0130 | 0.0330 | 0.0975 | 0.2372 | 0.0758 | 0.0951 |
| `max_drawdown` | -0.6800 | -0.3990 | -0.2190 | -0.0990 | -0.0390 | -0.2875 | 0.2471 |
| `hurst` | 0.0680 | 0.1124 | 0.1971 | 0.3070 | 0.3838 | 0.2129 | 0.1217 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.0000 | 0.3299 | 2.501 | 1.040 | 3.580 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 174 | 4.6% | -0.0190 |
| [0.1, 0.2) | 48 | 12.5% | -0.1490 |
| [0.2, 0.3) | 32 | 15.6% | -0.2190 |
| [0.3, 0.4) | 15 | 33.3% | -0.3190 |
| [0.4, 0.5) | 7 | 14.3% | -0.3990 |
| [0.5, 0.6) | 1 | 0.0% | -0.4990 |
| [0.6, 0.7) | 1 | 0.0% | -0.6990 |
| [0.7, 0.8) | 0 | — | — |
| [0.8, 0.9) | 0 | — | — |
| [0.9, 1.0) | 1 | 0.0% | -0.9790 |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 228 | 10.6% | 0.0700 | -0.0440 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **8** trades, WR=4.6%
- **Favorite losses** (open>0.90 + NO win) : **1** trades, WR=100.0%

- Long-shot payoff moyen : +0.947 pp

## Patterns temporels

- **Heures peak (UTC)** : [5, 4, 6] (79,671 trades)
- **Heures calmes (UTC)** : [18, 21, 20] (23,493 trades)
- **Jours peak** : ['Wed', 'Fri']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0630 | 0.0277 | 88.204 |
| [0.25-0.50] | 0.0513 | 0.0186 | 133.932 |
| [0.50-0.75] | 0.0286 | 0.0154 | 322.728 |
| [0.75-1.00] | 0.0125 | 0.0135 | 753.620 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 66 | -0.1740 | 0.1120 | 0.3484 | -0.4990 | 0.0% |
| 1 | 186 | -0.0210 | 0.0190 | 0.1428 | -0.1390 | 0.0% |
| 2 | 26 | 0.8290 | 0.3081 | 0.3494 | -0.4550 | 100.0% |

## Volume profile

- Trade size : médian $1, p90 $6, p99 $71
- Total volume USDC : $2.28M
- Trades total : 362,233

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/shanghai.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
