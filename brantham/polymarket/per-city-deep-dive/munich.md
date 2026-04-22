# Munich — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **352** markets analysés
- **190,580** trades on-chain
- **$807k** volume total USDC
- Période : 2026-03-05 → 2026-04-08

## Outcomes

- YES wins : **34** (9.7%)
- NO wins : **317**
- Ambiguous : 1

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0500 | 0.1700 | 0.2980 | 0.1098 | 0.1191 |
| `price_mid_avg` | 0.0020 | 0.0046 | 0.0250 | 0.1822 | 0.3694 | 0.1138 | 0.1681 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.0100 | 0.0977 | 0.2951 |
| `drift_pp` | -0.2409 | -0.1200 | -0.0390 | -0.0100 | -0.0060 | -0.0121 | 0.2874 |
| `volatility_pp` | 0.0042 | 0.0101 | 0.0291 | 0.0830 | 0.2290 | 0.0689 | 0.0895 |
| `max_drawdown` | -0.5490 | -0.3652 | -0.1668 | -0.0597 | -0.0251 | -0.2411 | 0.2218 |
| `hurst` | 0.0690 | 0.1214 | 0.1909 | 0.2775 | 0.3520 | 0.2014 | 0.1117 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.2580 | 1.584 | 5.705 | 3.240 | 18.932 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 206 | 1.5% | -0.0190 |
| [0.1, 0.2) | 73 | 17.8% | -0.1190 |
| [0.2, 0.3) | 38 | 34.2% | -0.1990 |
| [0.3, 0.4) | 20 | 15.0% | -0.3345 |
| [0.4, 0.5) | 10 | 10.0% | -0.4090 |
| [0.5, 0.6) | 3 | 33.3% | -0.4990 |
| [0.6, 0.7) | 1 | 0.0% | -0.6980 |
| [0.7, 0.8) | 0 | — | — |
| [0.8, 0.9) | 0 | — | — |
| [0.9, 1.0) | 0 | — | — |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 284 | 11.7% | 0.0850 | -0.0490 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **3** trades, WR=1.5%
- **Favorite losses** (open>0.90 + NO win) : **0** trades, WR=0.0%

- Long-shot payoff moyen : +0.942 pp

## Patterns temporels

- **Heures peak (UTC)** : [13, 14, 12] (42,503 trades)
- **Heures calmes (UTC)** : [3, 20, 21] (11,120 trades)
- **Jours peak** : ['Wed', 'Sat']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0714 | 0.0239 | 35.688 |
| [0.25-0.50] | 0.0546 | 0.0177 | 64.094 |
| [0.50-0.75] | 0.0307 | 0.0142 | 138.323 |
| [0.75-1.00] | 0.0138 | 0.0112 | 304.398 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 98 | -0.1890 | 0.0885 | 0.2642 | -0.4290 | 0.0% |
| 1 | 220 | -0.0290 | 0.0141 | 0.1445 | -0.0790 | 0.0% |
| 2 | 34 | 0.7990 | 0.2969 | 0.3508 | -0.4200 | 100.0% |

## Volume profile

- Trade size : médian $0, p90 $5, p99 $49
- Total volume USDC : $807k
- Trades total : 190,580

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/munich.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
