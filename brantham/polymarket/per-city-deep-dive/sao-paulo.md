# Sao Paulo — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **521** markets analysés
- **229,049** trades on-chain
- **$1.07M** volume total USDC
- Période : 2026-02-11 → 2026-04-08

## Outcomes

- YES wins : **53** (10.2%)
- NO wins : **468**
- Ambiguous : 0

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0700 | 0.1900 | 0.3400 | 0.1295 | 0.1533 |
| `price_mid_avg` | 0.0020 | 0.0064 | 0.0367 | 0.1850 | 0.3620 | 0.1232 | 0.1813 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.9950 | 0.1032 | 0.3018 |
| `drift_pp` | -0.3100 | -0.1490 | -0.0390 | -0.0090 | 0.0201 | -0.0264 | 0.3050 |
| `volatility_pp` | 0.0044 | 0.0118 | 0.0359 | 0.0996 | 0.2617 | 0.0768 | 0.0974 |
| `max_drawdown` | -0.5990 | -0.4099 | -0.2074 | -0.0680 | -0.0270 | -0.2660 | 0.2291 |
| `hurst` | 0.0611 | 0.1126 | 0.1788 | 0.2511 | 0.3347 | 0.1887 | 0.1066 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.5189 | 2.719 | 11.706 | 4.281 | 11.239 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 295 | 2.4% | -0.0190 |
| [0.1, 0.2) | 99 | 19.2% | -0.1190 |
| [0.2, 0.3) | 58 | 27.6% | -0.2090 |
| [0.3, 0.4) | 38 | 10.5% | -0.3364 |
| [0.4, 0.5) | 17 | 17.6% | -0.4090 |
| [0.5, 0.6) | 5 | 20.0% | -0.4980 |
| [0.6, 0.7) | 4 | 50.0% | -0.1800 |
| [0.7, 0.8) | 0 | — | — |
| [0.8, 0.9) | 2 | 0.0% | -0.8340 |
| [0.9, 1.0) | 3 | 33.3% | -0.8990 |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 324 | 13.0% | 0.1100 | -0.0690 |
| cold | 91 | 8.8% | 0.0500 | -0.0490 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **7** trades, WR=2.4%
- **Favorite losses** (open>0.90 + NO win) : **1** trades, WR=50.0%

- Long-shot payoff moyen : +0.955 pp

## Patterns temporels

- **Heures peak (UTC)** : [18, 16, 17] (55,871 trades)
- **Heures calmes (UTC)** : [2, 23, 5] (14,213 trades)
- **Jours peak** : ['Tue', 'Mon']
- **Mois pic activité** : mois 3

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0656 | 0.0247 | 39.525 |
| [0.25-0.50] | 0.0578 | 0.0160 | 54.727 |
| [0.50-0.75] | 0.0387 | 0.0152 | 103.434 |
| [0.75-1.00] | 0.0251 | 0.0194 | 245.563 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 329 | -0.0290 | 0.0163 | 0.1390 | -0.0940 | 0.3% |
| 1 | 51 | 0.8090 | 0.3147 | 0.3253 | -0.4127 | 100.0% |
| 2 | 139 | -0.2190 | 0.1035 | 0.2432 | -0.4890 | 0.7% |

## Volume profile

- Trade size : médian $0, p90 $5, p99 $62
- Total volume USDC : $1.07M
- Trades total : 229,049

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/sao-paulo.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
