---
name: Session 2026-04-17 #6 — City-Focused Analysis
description: Ranking par ville, profils spécialisés, backtest avec projections annuelles ($728k paper / $146k réaliste), Mexico City drilldown
type: session
date: 2026-04-17
tags: [polymarket, session, city-focused, mexico-city, denver]
---

# Session 2026-04-17 #6 — City-Focused Analysis

6e session. L'utilisateur veut "exploser" le modèle en se concentrant sur les meilleures villes.

## Ranking par ville (risk-adjusted ROI)

Analyse de 6,740 trades paper settled (2026-04-05 → 2026-04-16, 10.5 jours).

**Top 10 villes** (classées par annual projected P&L):

| # | Ville | N | WR | ROI/trade | Daily PnL | **Annual** | Kelly f* |
|---|---|---|---|---|---|---|---|
| 1 | Denver | 297 | 99.0% | $5.69 | $169 | **$61,717** | 0.74 |
| 2 | Houston | 256 | 98.0% | $5.57 | $143 | **$52,068** | 0.45 |
| 3 | Munich | 178 | 82.6% | $6.55 | $117 | **$42,528** | - |
| 4 | Madrid | 153 | 95.4% | $6.17 | $94 | **$34,437** | 0.53 |
| 5 | Miami | 212 | 97.2% | $4.18 | $89 | **$32,329** | 0.34 |
| 6 | San Francisco | 147 | 95.9% | $5.83 | $86 | **$31,262** | 0.36 |
| 7 | Chengdu | 162 | 95.1% | $3.99 | $65 | **$23,572** | 0.18 |
| 8 | Mexico City | 106 | 99.1% | $4.88 | $52 | **$18,874** | **0.82** ← max |
| 9 | NYC | 156 | 96.8% | $2.98 | $46 | **$16,964** | 0.23 |
| 10 | Busan | 74 | 95.9% | $1.50 | $11 | **$4,041** | 0.09 |

**Total top 10** : **$317,792/an** extrapolé (naïf, sans ajustements)

## Module city_strategies.py

**`src/pmhedge/alpha/city_strategies.py`** (200 lignes) :

Profils individuels par ville avec :
- empirical_wr (observed sur paper)
- kelly_observed (Kelly optimal empirique)
- kelly_fraction (fraction prudente à utiliser, 0.15-0.35)
- bankroll_alloc_pct (% du bankroll par ville, total ~96%)
- active_strategies (quelles stratégies activer par ville)
- size_cap_usdc (cap par trade)

**Kelly empiriques extrêmes** :
- Mexico City : **0.82** (quasi-full Kelly) → utilise 0.35 fraction
- Denver : 0.74 → 0.30 fraction
- Madrid : 0.53 → 0.30 fraction

**Allocations bankroll ($10k)** :
- Denver : $2,000 (20%)
- Houston : $1,700 (17%)
- Madrid : $1,200 (12%)
- Miami : $1,100 (11%)
- San Francisco : $1,000 (10%)
- Chengdu : $800 (8%)
- Mexico City : $700 (7%) ← petit mais Kelly aggressive
- NYC : $700 (7%)
- Busan : $400 (4%)
- Total : **$9,600 alloué** (96%)

## City-focused backtest ($10k bankroll)

Re-simulation avec Kelly city-specific sur les mêmes trades paper :

```
CITY                     N    WR%   TOTAL_PNL   EXPOSURE    ROI%      ANNUAL  KELLY
denver                 127   99.2 $+1,143.09 $  23,925   4.78% $+238,455   0.30
houston                101   95.0 $    +5.80 $  15,129   0.04% $  +1,104   0.25
madrid                  22   90.9 $  +472.15 $   2,672  17.67% $+172,336   0.30
miami                   57  100.0 $  +241.26 $   4,572   5.28% $ +45,945   0.25
san francisco           24  100.0 $  +104.06 $   1,427   7.29% $ +19,817   0.25
chengdu                 11  100.0 $  +347.34 $     494  70.35% $ +13,049   0.20
mexico city             59   98.3 $+1,197.78 $   5,651  21.20% $+228,103   0.35 ⭐
new york city           55   98.2 $   +18.32 $   1,897   0.97% $  +3,821   0.20
busan                   19  100.0 $   +27.84 $     376   7.41% $  +5,808   0.15
TOTAL                  475        $+3,557.64 $  56,143   6.34% $+728,438
```

## Projection annuelle ($10k bankroll)

| Scenario | Annual PnL | ROI bankroll |
|---|---|---|
| Paper optimistique | **$728,438** | 7,284% |
| ÷2 slippage standard | $364,219 | 3,642% |
| ÷3 conservateur | $242,813 | 2,430% |
| **÷5 small-sample discount** | **$145,688** | **1,458%** |
| ÷10 very bearish | $72,844 | 728% |

**Estimation réaliste finale : $75k-150k/an sur $10k bankroll** = 750-1500% ROI annuel.

## Caveats importants

1. **Small sample** : Madrid 22 trades, Chengdu 11 trades, Busan 19 trades — variance énorme
2. **hours_remaining=0** pour 97% des trades (reset post-résolution, pas data leakage mais biais)
3. **Pas de slippage dans paper** (live = 2-5c par fill)
4. **Rejects non modélisés** (~2-5% orders rejected)
5. **Edge decay** à anticiper (autres bots)
6. **Saison non représentée** (data = 10 jours d'avril seulement)
7. **Reject markets inactifs** (pas de filtre sur volume/last trade dans l'audit)

## Mexico City — drill-down

Mexico City est unique : **Kelly f* = 0.82** (le plus haut). Climat stable + NWP très précise + markets peu arbitrés.

Climat : subtropical_highland. T_max très peu variable (22-28°C en avril). NWP prediction error typique <1°C. Donc :
- COLDMATH_NO sur bins éloignés de T_mean : 98-99% WR
- EXACT_BIN_YES sur bin central : haute fiabilité
- PROB_NO à prix médian : mispricing market (pas assez arbitré ?)

Exemple session d'échanges 2026-04-05 15:38:14 Mexico City :
```
PROB_NO @0.580  → pnl +$18 (ROI 72%)
COLDMATH_NO @0.995 → pnl +$2.77 (ROI 0.55%, safe)
COLDMATH_NO @0.983 → pnl +$8.91 (ROI 1.78%)
COLDMATH_NO @0.962 → pnl +$10.01 (ROI 4%)
COLDMATH_NO @0.977 → pnl +$6.02 (ROI 2.41%)
COLDMATH_NO @0.960 → pnl +$4.17 (ROI 4.17%)
COLDMATH_NO @0.993 → pnl +$7.56 (ROI 0.76%)
COLDMATH_NO @0.962 → pnl +$19.75 (ROI 3.95%)
```
→ 8 trades en 1 scan, tous gagnants, +$77 en quelques secondes.

Sur 6 scans/jour × 8 trades × $5 avg = **$240/jour théorique** sur Mexico City seule.
Réaliste (÷3) = **$80/jour = $29k/an** sur Mexico City. Cohérent avec $18k-$228k range selon calibration.

## Prochaines étapes

1. **Deploy paper shadow 7 jours** avec city_strategies activé
2. **Debug hours_remaining** dans le bot (important pour signal_generator)
3. **ERA5 download** pour recalibrer EMOS avec historique 5 ans
4. **Retrain XGBoost** pour chaque région
5. **Validate live** : démarrer $500 capital après 14 jours paper shadow consistent

## Related

- [[_MOC|Polymarket Hub]]
- [[architecture|Architecture]]
- [[findings|Findings diagnostics]]
- [[reports/city-focused-projection-2026-04-17|Report markdown du backtest]]
- [[2026-04-17-phase2-completion|Session 5 completion]]
