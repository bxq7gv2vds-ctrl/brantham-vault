# New York — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **1,486** markets analysés
- **931,578** trades on-chain
- **$7.43M** volume total USDC
- Période : 2025-10-01 → 2026-04-08

## Outcomes

- YES wins : **172** (12.0%)
- NO wins : **1,261**
- Ambiguous : 53

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0700 | 0.2100 | 0.4300 | 0.1486 | 0.1783 |
| `price_mid_avg` | 0.0012 | 0.0040 | 0.0208 | 0.1899 | 0.4812 | 0.1407 | 0.2261 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.9990 | 0.1295 | 0.3335 |
| `drift_pp` | -0.3191 | -0.1298 | -0.0390 | -0.0090 | 0.4990 | -0.0190 | 0.3132 |
| `volatility_pp` | 0.0048 | 0.0114 | 0.0368 | 0.1225 | 0.2372 | 0.0806 | 0.0940 |
| `max_drawdown` | -0.6927 | -0.4990 | -0.2266 | -0.0783 | -0.0290 | -0.3063 | 0.2654 |
| `hurst` | 0.0462 | 0.0926 | 0.1642 | 0.2541 | 0.3349 | 0.1778 | 0.1112 |
| `half_life_minutes` | 0.0000 | 0.3163 | 1.376 | 4.108 | 12.314 | 5.389 | 25.711 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 807 | 3.6% | -0.0190 |
| [0.1, 0.2) | 249 | 11.2% | -0.1110 |
| [0.2, 0.3) | 141 | 22.0% | -0.2090 |
| [0.3, 0.4) | 76 | 23.7% | -0.3295 |
| [0.4, 0.5) | 73 | 34.2% | -0.4090 |
| [0.5, 0.6) | 52 | 50.0% | -0.0500 |
| [0.6, 0.7) | 20 | 35.0% | -0.6240 |
| [0.7, 0.8) | 2 | 100.0% | 0.2590 |
| [0.8, 0.9) | 2 | 100.0% | 0.1590 |
| [0.9, 1.0) | 11 | 36.4% | -0.9390 |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 140 | 10.6% | 0.0550 | -0.0390 |
| cold | 563 | 12.4% | 0.1000 | -0.0590 |
| mild | 349 | 15.3% | 0.1200 | -0.0790 |
| warm | 53 | 13.5% | 0.0800 | -0.0440 |
| hot | 1 | 0.0% | 0.0100 | -0.0090 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **29** trades, WR=3.6%
- **Favorite losses** (open>0.90 + NO win) : **6** trades, WR=60.0%

- Long-shot payoff moyen : +0.921 pp

## Patterns temporels

- **Heures peak (UTC)** : [19, 18, 17] (181,861 trades)
- **Heures calmes (UTC)** : [2, 1, 3] (78,132 trades)
- **Jours peak** : ['Mon', 'Wed']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0671 | 0.0277 | 52.262 |
| [0.25-0.50] | 0.0458 | 0.0191 | 75.407 |
| [0.50-0.75] | 0.0333 | 0.0175 | 166.264 |
| [0.75-1.00] | 0.0139 | 0.0122 | 338.369 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 388 | -0.2490 | 0.1220 | 0.2383 | -0.5990 | 1.7% |
| 1 | 917 | -0.0290 | 0.0154 | 0.1195 | -0.0990 | 0.8% |
| 2 | 179 | 0.7090 | 0.2661 | 0.2921 | -0.4900 | 99.4% |

## Volume profile

- Trade size : médian $1, p90 $9, p99 $100
- Total volume USDC : $7.43M
- Trades total : 931,578

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/new-york.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
