# Paris — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **521** markets analysés
- **375,840** trades on-chain
- **$1.88M** volume total USDC
- Période : 2026-02-11 → 2026-04-08

## Outcomes

- YES wins : **53** (10.2%)
- NO wins : **466**
- Ambiguous : 2

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0600 | 0.2000 | 0.3436 | 0.1332 | 0.1596 |
| `price_mid_avg` | 0.0020 | 0.0046 | 0.0236 | 0.1500 | 0.4130 | 0.1189 | 0.1893 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.9990 | 0.1028 | 0.3019 |
| `drift_pp` | -0.3190 | -0.1590 | -0.0290 | -0.0090 | 0.0890 | -0.0304 | 0.2956 |
| `volatility_pp` | 0.0045 | 0.0120 | 0.0314 | 0.0959 | 0.2200 | 0.0723 | 0.0931 |
| `max_drawdown` | -0.6490 | -0.3990 | -0.1890 | -0.0690 | -0.0280 | -0.2647 | 0.2401 |
| `hurst` | 0.0624 | 0.1087 | 0.1843 | 0.2724 | 0.3426 | 0.1941 | 0.1068 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.3924 | 2.749 | 7.498 | 3.757 | 15.303 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 293 | 2.7% | -0.0190 |
| [0.1, 0.2) | 91 | 12.1% | -0.1390 |
| [0.2, 0.3) | 62 | 24.2% | -0.2090 |
| [0.3, 0.4) | 33 | 24.2% | -0.3281 |
| [0.4, 0.5) | 24 | 25.0% | -0.4090 |
| [0.5, 0.6) | 4 | 0.0% | -0.4985 |
| [0.6, 0.7) | 7 | 42.9% | -0.6690 |
| [0.7, 0.8) | 1 | 100.0% | 0.2790 |
| [0.8, 0.9) | 0 | — | — |
| [0.9, 1.0) | 4 | 25.0% | -0.9390 |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 415 | 11.9% | 0.1000 | -0.0490 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **8** trades, WR=2.7%
- **Favorite losses** (open>0.90 + NO win) : **2** trades, WR=66.7%

- Long-shot payoff moyen : +0.924 pp

## Patterns temporels

- **Heures peak (UTC)** : [14, 13, 12] (93,034 trades)
- **Heures calmes (UTC)** : [4, 3, 2] (22,475 trades)
- **Jours peak** : ['Mon', 'Wed']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0586 | 0.0262 | 51.642 |
| [0.25-0.50] | 0.0365 | 0.0160 | 78.994 |
| [0.50-0.75] | 0.0264 | 0.0121 | 160.144 |
| [0.75-1.00] | 0.0145 | 0.0123 | 436.102 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 341 | -0.0250 | 0.0152 | 0.1377 | -0.0940 | 0.6% |
| 1 | 50 | 0.7740 | 0.2849 | 0.3130 | -0.4450 | 100.0% |
| 2 | 127 | -0.2290 | 0.1113 | 0.2590 | -0.4990 | 0.8% |

## Volume profile

- Trade size : médian $0, p90 $5, p99 $71
- Total volume USDC : $1.88M
- Trades total : 375,840

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/paris.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
