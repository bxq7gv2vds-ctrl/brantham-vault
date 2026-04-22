# Seattle — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **1,011** markets analysés
- **407,959** trades on-chain
- **$2.11M** volume total USDC
- Période : 2025-12-05 → 2026-04-08

## Outcomes

- YES wins : **82** (8.9%)
- NO wins : **843**
- Ambiguous : 86

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0700 | 0.2200 | 0.4100 | 0.1482 | 0.1791 |
| `price_mid_avg` | 0.0010 | 0.0034 | 0.0197 | 0.1500 | 0.4680 | 0.1329 | 0.2236 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0020 | 0.9990 | 0.1249 | 0.3270 |
| `drift_pp` | -0.2990 | -0.1490 | -0.0290 | -0.0090 | 0.4490 | -0.0233 | 0.2930 |
| `volatility_pp` | 0.0041 | 0.0097 | 0.0320 | 0.1095 | 0.2424 | 0.0772 | 0.0941 |
| `max_drawdown` | -0.7000 | -0.4590 | -0.1800 | -0.0573 | -0.0190 | -0.2826 | 0.2673 |
| `hurst` | 0.0256 | 0.0813 | 0.1489 | 0.2351 | 0.3215 | 0.1591 | 0.1192 |
| `half_life_minutes` | 0.0000 | 0.1904 | 1.059 | 4.397 | 12.416 | 5.348 | 14.155 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 532 | 1.3% | -0.0190 |
| [0.1, 0.2) | 158 | 7.0% | -0.1290 |
| [0.2, 0.3) | 97 | 18.6% | -0.2290 |
| [0.3, 0.4) | 43 | 30.2% | -0.3190 |
| [0.4, 0.5) | 37 | 43.2% | -0.3990 |
| [0.5, 0.6) | 43 | 20.9% | -0.5050 |
| [0.6, 0.7) | 3 | 33.3% | -0.6780 |
| [0.7, 0.8) | 6 | 50.0% | -0.2375 |
| [0.8, 0.9) | 1 | 100.0% | 0.1790 |
| [0.9, 1.0) | 5 | 60.0% | 0.0100 |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| cold | 490 | 8.9% | 0.1000 | -0.0390 |
| mild | 271 | 10.8% | 0.1000 | -0.0390 |
| warm | 4 | 25.0% | 0.1150 | -0.0495 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **7** trades, WR=1.3%
- **Favorite losses** (open>0.90 + NO win) : **2** trades, WR=40.0%

- Long-shot payoff moyen : +0.953 pp

## Patterns temporels

- **Heures peak (UTC)** : [22, 21, 20] (80,625 trades)
- **Heures calmes (UTC)** : [4, 3, 5] (33,326 trades)
- **Jours peak** : ['Mon', 'Thu']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0535 | 0.0247 | 39.244 |
| [0.25-0.50] | 0.0428 | 0.0158 | 55.665 |
| [0.50-0.75] | 0.0276 | 0.0155 | 103.984 |
| [0.75-1.00] | 0.0134 | 0.0109 | 216.416 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 652 | -0.0200 | 0.0141 | 0.1169 | -0.0840 | 0.8% |
| 1 | 115 | 0.6790 | 0.2657 | 0.2619 | -0.5100 | 96.2% |
| 2 | 231 | -0.2500 | 0.1174 | 0.2154 | -0.5850 | 0.5% |

## Volume profile

- Trade size : médian $1, p90 $5, p99 $64
- Total volume USDC : $2.11M
- Trades total : 407,959

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/seattle.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
