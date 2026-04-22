# Mexico City — Deep Dive Quantitatif

_Généré : 2026-04-22 14:58 UTC_

## Volumétrie

- **99** markets analysés
- **30,882** trades on-chain
- **$80k** volume total USDC
- Période : 2026-03-30 → 2026-04-08

## Outcomes

- YES wins : **9** (9.1%)
- NO wins : **90**
- Ambiguous : 0

## Distribution des prix

| Métrique | p10 | p25 | p50 | p75 | p90 | mean | std |
|----------|----:|----:|----:|----:|----:|-----:|----:|
| `price_open` | 0.0100 | 0.0200 | 0.0600 | 0.1814 | 0.2700 | 0.1138 | 0.1194 |
| `price_mid_avg` | 0.0014 | 0.0023 | 0.0139 | 0.1105 | 0.3695 | 0.0975 | 0.1753 |
| `price_close` | 0.0010 | 0.0010 | 0.0010 | 0.0010 | 0.0102 | 0.0923 | 0.2882 |
| `drift_pp` | -0.2690 | -0.1690 | -0.0390 | -0.0090 | -0.0048 | -0.0216 | 0.2840 |
| `volatility_pp` | 0.0050 | 0.0131 | 0.0309 | 0.0986 | 0.2083 | 0.0719 | 0.0912 |
| `max_drawdown` | -0.6228 | -0.4445 | -0.1940 | -0.0835 | -0.0270 | -0.2828 | 0.2421 |
| `hurst` | 0.0582 | 0.0961 | 0.1498 | 0.2351 | 0.3169 | 0.1726 | 0.1063 |
| `half_life_minutes` | 0.0000 | 0.0000 | 0.0000 | 0.3153 | 2.358 | 0.8778 | 2.285 |

## Win rate YES par bin de prix d'entrée

_Si bookies parfaits : WR ≈ centre du bin (calibration parfaite). Décalages = mispricings exploitables._

| Bin prix open | N markets | WR YES réel | drift médian |
|---------------|----------:|------------:|-------------:|
| [0.0, 0.1) | 58 | 3.4% | -0.0190 |
| [0.1, 0.2) | 19 | 10.5% | -0.1660 |
| [0.2, 0.3) | 14 | 28.6% | -0.2270 |
| [0.3, 0.4) | 5 | 0.0% | -0.3190 |
| [0.4, 0.5) | 0 | — | — |
| [0.5, 0.6) | 3 | 33.3% | -0.4990 |
| [0.6, 0.7) | 0 | — | — |
| [0.7, 0.8) | 0 | — | — |
| [0.8, 0.9) | 0 | — | — |
| [0.9, 1.0) | 0 | — | — |

## Brackets par range de threshold

| Range | N markets | WR YES | open médian | drift médian |
|-------|----------:|-------:|------------:|-------------:|
| very_cold | 81 | 9.9% | 0.0700 | -0.0490 |

## Edges détectés

- **Long-shot wins** (open<0.10 + YES win) : **2** trades, WR=3.4%
- **Favorite losses** (open>0.90 + NO win) : **0** trades, WR=0.0%

- Long-shot payoff moyen : +0.939 pp

## Patterns temporels

- **Heures peak (UTC)** : [0, 14, 22] (7,189 trades)
- **Heures calmes (UTC)** : [5, 4, 3] (1,388 trades)
- **Jours peak** : ['Wed', 'Sun']
- **Mois pic activité** : mois 4

## Comportement par quartile TTR

| TTR | mean price | std price | avg n_trades |
|-----|----------:|----------:|-------------:|
| [0.00-0.25] | 0.0635 | 0.0278 | 39.608 |
| [0.25-0.50] | 0.0383 | 0.0163 | 53.949 |
| [0.50-0.75] | 0.0272 | 0.0163 | 72.091 |
| [0.75-1.00] | 0.0125 | 0.0137 | 147.606 |

## Régimes détectés (K-means clustering)

| Cluster | N markets | drift | vol | hurst | max DD | WR YES |
|---------|----------:|------:|----:|------:|-------:|-------:|
| 0 | 65 | -0.0290 | 0.0183 | 0.1210 | -0.1180 | 0.0% |
| 1 | 9 | 0.7890 | 0.3071 | 0.3313 | -0.5696 | 100.0% |
| 2 | 25 | -0.1790 | 0.1135 | 0.2322 | -0.5290 | 0.0% |

## Volume profile

- Trade size : médian $0, p90 $3, p99 $25
- Total volume USDC : $80k
- Trades total : 30,882

## Visualisation interactive

`research/outputs/11_per_city_deep_dive/mexico-city.html`

## Related

- [[_MOC|Per-city Deep Dive MOC]]
- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Findings global v2]]
- [[../city-optimization|City optimization log]]
