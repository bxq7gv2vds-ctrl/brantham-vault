# Miami — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **697** markets analysés
- **423,994** trades on-chain
- **$2.22M** volume total USDC
- Période : 2025-12-04 → 2026-04-08

## Outcomes

- YES wins : **76** (11.0%)
- NO wins : **616**
- Ambiguous : 5

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0600 | 0.2000 | 0.3400 | 0.1340 | 0.1629 |
| `price_mid_avg` | 0.0020 | 0.0050 | 0.0248 | 0.1640 | 0.4056 | 0.1210 | 0.1876 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.9990 | 0.1131 | 0.3147 |
| `drift_pp` | -0.3090 | -0.1490 | -0.0290 | -0.0090 | 0.5170 | -0.0209 | 0.3057 |
| `volatility_pp` | 0.0044 | 0.0107 | 0.0301 | 0.0999 | 0.2414 | 0.0736 | 0.0919 |
| `max_drawdown` | -0.6990 | -0.4500 | -0.1730 | -0.0590 | -0.0280 | -0.2820 | 0.2653 |
| `hurst` | 0.0591 | 0.1087 | 0.1621 | 0.2331 | 0.3087 | 0.1748 | 0.0974 |
| `half_life_minutes` | 0.0000 | 0.1619 | 0.8079 | 2.792 | 8.223 | 3.402 | 9.267 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 382 | 1.3% | -0.0190 |
| [0.1, 0.2) | 131 | 17.6% | -0.1290 |
| [0.2, 0.3) | 82 | 29.3% | -0.2090 |
| [0.3, 0.4) | 48 | 20.8% | -0.3290 |
| [0.4, 0.5) | 27 | 29.6% | -0.4090 |
| [0.5, 0.6) | 6 | 0.0% | -0.5240 |
| [0.6, 0.7) | 6 | 33.3% | -0.6290 |
| [0.7, 0.8) | 3 | 33.3% | -0.7390 |
| [0.8, 0.9) | 4 | 75.0% | 0.1340 |
| [0.9, 1.0) | 3 | 0.0% | -0.9290 |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| mild | 91 | 10.0% | 0.0900 | -0.0390 |
| warm | 357 | 15.5% | 0.1400 | -0.0690 |
| hot | 93 | 3.2% | 0.0200 | -0.0190 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **5** trades, WR=1.3%
- **Favorite losses** (open>0.90 + NO win) : **3** trades, WR=100.0%

- Long-shot payoff moyen : +0.937 pp

## Patterns temporels

- **Heures peak (UTC)** : [17, 18, 16] (93,349 trades)
- **Heures calmes (UTC)** : [3, 2, 5] (30,800 trades)
- **Jours peak** : ['Tue', 'Thu']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0548 | 0.0240 | 60.728 |
| [0.25-0.50] | 0.0407 | 0.0178 | 74.584 |
| [0.50-0.75] | 0.0260 | 0.0136 | 153.141 |
| [0.75-1.00] | 0.0177 | 0.0154 | 321.806 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 71 | 0.7890 | 0.2862 | 0.2730 | -0.5500 | 100.0% |
| 1 | 457 | -0.0190 | 0.0150 | 0.1346 | -0.0908 | 1.1% |
| 2 | 166 | -0.2540 | 0.1119 | 0.2283 | -0.6080 | 1.2% |

## Volume profile

- Trade size : médian $1, p90 $5, p99 $54
- Total volume USDC : $2.22M
- Trades total : 423,994

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/miami.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
