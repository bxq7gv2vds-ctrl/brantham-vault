# Austin — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **165** markets analysés
- **73,024** trades on-chain
- **$232k** volume total USDC
- Période : 2026-03-24 → 2026-04-08

## Outcomes

- YES wins : **15** (9.1%)
- NO wins : **150**
- Ambiguous : 0

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0400 | 0.1600 | 0.2600 | 0.0971 | 0.1092 |
| `price_mid_avg` | 0.0020 | 0.0050 | 0.0230 | 0.1051 | 0.3293 | 0.1052 | 0.1826 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.0100 | 0.0921 | 0.2876 |
| `drift_pp` | -0.2550 | -0.1280 | -0.0380 | -0.0090 | -0.0056 | -0.0050 | 0.2869 |
| `volatility_pp` | 0.0061 | 0.0130 | 0.0314 | 0.0810 | 0.2069 | 0.0701 | 0.0889 |
| `max_drawdown` | -0.6372 | -0.3690 | -0.1690 | -0.0690 | -0.0320 | -0.2502 | 0.2301 |
| `hurst` | 0.0496 | 0.1006 | 0.1759 | 0.2527 | 0.3514 | 0.1919 | 0.1163 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.0000 | 0.7833 | 4.410 | 9.285 | 93.964 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 108 | 2.8% | -0.0190 |
| [0.1, 0.2) | 26 | 34.6% | -0.1285 |
| [0.2, 0.3) | 21 | 9.5% | -0.2290 |
| [0.3, 0.4) | 6 | 0.0% | -0.3446 |
| [0.4, 0.5) | 3 | 0.0% | -0.4090 |
| [0.5, 0.6) | 1 | 100.0% | 0.4890 |
| [0.6, 0.7) | 0 | — | — |
| [0.7, 0.8) | 0 | — | — |
| [0.8, 0.9) | 0 | — | — |
| [0.9, 1.0) | 0 | — | — |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| mild | 23 | 4.3% | 0.0300 | -0.0190 |
| warm | 62 | 11.3% | 0.0750 | -0.0390 |
| hot | 50 | 14.0% | 0.0500 | -0.0335 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **3** trades, WR=2.8%
- **Favorite losses** (open>0.90 + NO win) : **0** trades, WR=0.0%

- Long-shot payoff moyen : +0.952 pp

## Patterns temporels

- **Heures peak (UTC)** : [22, 19, 21] (14,394 trades)
- **Heures calmes (UTC)** : [8, 3, 13] (5,177 trades)
- **Jours peak** : ['Wed', 'Sun']
- **Mois pic activité** : mois 4

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0533 | 0.0261 | 42.191 |
| [0.25-0.50] | 0.0418 | 0.0159 | 55.847 |
| [0.50-0.75] | 0.0273 | 0.0133 | 90.927 |
| [0.75-1.00] | 0.0118 | 0.0140 | 256.279 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 15 | 0.8390 | 0.2938 | 0.3487 | -0.5200 | 100.0% |
| 1 | 113 | -0.0290 | 0.0176 | 0.1307 | -0.0950 | 0.0% |
| 2 | 37 | -0.2090 | 0.1114 | 0.2905 | -0.4690 | 0.0% |

## Volume profile

- Trade size : médian $0, p90 $4, p99 $38
- Total volume USDC : $232k
- Trades total : 73,024

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/austin.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
