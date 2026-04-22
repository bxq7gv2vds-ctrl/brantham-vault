# Atlanta — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **1,020** markets analysés
- **434,179** trades on-chain
- **$2.47M** volume total USDC
- Période : 2025-12-05 → 2026-04-08

## Outcomes

- YES wins : **120** (11.9%)
- NO wins : **888**
- Ambiguous : 12

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0500 | 0.2000 | 0.3900 | 0.1432 | 0.1918 |
| `price_mid_avg` | 0.0010 | 0.0036 | 0.0191 | 0.1780 | 0.4572 | 0.1380 | 0.2342 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.9990 | 0.1234 | 0.3260 |
| `drift_pp` | -0.2890 | -0.1490 | -0.0290 | -0.0090 | 0.3840 | -0.0197 | 0.3019 |
| `volatility_pp` | 0.0034 | 0.0091 | 0.0296 | 0.0980 | 0.2354 | 0.0739 | 0.0954 |
| `max_drawdown` | -0.6707 | -0.4119 | -0.1790 | -0.0480 | -0.0190 | -0.2611 | 0.2569 |
| `hurst` | 0.0327 | 0.0893 | 0.1534 | 0.2340 | 0.3233 | 0.1651 | 0.1177 |
| `half_life_minutes` | 0.0000 | 0.1268 | 0.8435 | 3.513 | 12.078 | 5.112 | 16.603 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 573 | 3.0% | -0.0190 |
| [0.1, 0.2) | 165 | 13.9% | -0.1290 |
| [0.2, 0.3) | 124 | 19.4% | -0.2190 |
| [0.3, 0.4) | 47 | 21.3% | -0.3290 |
| [0.4, 0.5) | 35 | 42.9% | -0.4009 |
| [0.5, 0.6) | 29 | 31.0% | -0.4990 |
| [0.6, 0.7) | 8 | 37.5% | -0.6535 |
| [0.7, 0.8) | 5 | 60.0% | 0.2090 |
| [0.8, 0.9) | 5 | 100.0% | 0.1690 |
| [0.9, 1.0) | 17 | 64.7% | 0.0290 |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 6 | 0.0% | 0.0400 | -0.0390 |
| cold | 188 | 7.7% | 0.0700 | -0.0355 |
| mild | 428 | 9.5% | 0.0500 | -0.0290 |
| warm | 136 | 11.8% | 0.1500 | -0.1040 |
| hot | 14 | 0.0% | 0.0200 | -0.0190 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **17** trades, WR=3.0%
- **Favorite losses** (open>0.90 + NO win) : **6** trades, WR=35.3%

- Long-shot payoff moyen : +0.947 pp

## Patterns temporels

- **Heures peak (UTC)** : [20, 21, 19] (82,806 trades)
- **Heures calmes (UTC)** : [3, 1, 2] (29,128 trades)
- **Jours peak** : ['Mon', 'Sat']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0526 | 0.0223 | 45.248 |
| [0.25-0.50] | 0.0362 | 0.0143 | 60.997 |
| [0.50-0.75] | 0.0243 | 0.0125 | 106.284 |
| [0.75-1.00] | 0.0108 | 0.0095 | 226.193 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 102 | 0.7990 | 0.2910 | 0.2831 | -0.4500 | 100.0% |
| 1 | 683 | -0.0190 | 0.0133 | 0.1283 | -0.0790 | 2.3% |
| 2 | 230 | -0.2200 | 0.1184 | 0.2093 | -0.5640 | 2.7% |

## Volume profile

- Trade size : médian $0, p90 $5, p99 $70
- Total volume USDC : $2.47M
- Trades total : 434,179

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/atlanta.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
