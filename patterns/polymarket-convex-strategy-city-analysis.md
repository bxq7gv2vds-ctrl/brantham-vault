---
name: Polymarket — Stratégie convexe par ville (Tokyo/Paris vs NYC)
description: Analyse Kelly + Monte Carlo de la stratégie buy YES cheap (<2%) par ville — Tokyo edge +8.5% vs NYC +0.9%
type: pattern
project: polymarket-hedge
tags: [polymarket, convex, kelly, monte-carlo, tokyo, paris, fat-tails, longshot]
date: 2026-04-11
scripts:
  - scripts/city_convex_strategy.py
outputs:
  - analysis/J_city_calibration.png
  - analysis/K_kelly_analysis.png
  - analysis/L_monte_carlo.png
  - analysis/M_optimal_portfolio.png
---

# Polymarket — Stratégie convexe par ville

## Fracture ville par ville : WR à <2% price

| Ville | WR à <2% | Edge | Notes |
|-------|----------|------|-------|
| Mexico City | 10.7% | +9.7% | n=422 (petit) |
| **Tokyo** | **9.6%** | **+8.6%** | n=3695 ✓ |
| **Paris** | **8.6%** | **+7.6%** | n=4736 ✓ |
| Milan | 8.0% | +7.0% | n=2789 |
| London | 6.7% | +5.7% | n=5230 |
| New York | 1.9% | +0.9% | n=5583 |
| Dallas | 0.5% | −0.5% | **négatif** |
| Houston/LA | 0.0% | −1.0% | **négatif** |

**Pourquoi cette fracture ?** Les marchés US (NYC, Dallas, Miami, LA) sont très liquides et les traders US calibrent mieux la météo locale → peu de mispricing. Les marchés asiatiques et européens sont sous-suivis → mispricing structurel des bins improbables.

---

## Kelly formula — bet binaire exact

```
f* = (WR - p) / (1 - p)

Payout b = (1 - p) / p

Tokyo à p=1%, WR=9.55% :
  f* = (0.0955 - 0.01) / 0.99 = 8.64%  (full Kelly)
  f_frac = f* × 0.25 = 2.16%  → bet = $216 sur $10K

  Si WIN  (9.55%) : gain = $216 × 99 = $21,384
  Si LOSE (90.45%): perte = $216
  EV par bet = 0.0955 × $21,384 - 0.9045 × $216 = $2,042 - $195 = +$1,847
```

**Table Kelly par bucket (Tokyo, bankroll $10K) :**

| Prix | WR | f* | Bet $ | Win $ | EV/bet |
|------|----|----|-------|-------|--------|
| 0.2% | 7.7% | 7.5% | $188 | $74,973 | $5,635 |
| 0.8% | 8.7% | 8.0% | $200 | $26,466 | $2,117 |
| 1.2% | 12.5% | 11.4% | $284 | $22,432 | $2,548 |
| 1.8% | 13.8% | 12.3% | $307 | $17,228 | $2,115 |
| 2.5% | 9.4% | 7.0% | $176 | $6,866 | $484 |

---

## Monte Carlo — 50K portfolios de 100 bets

**Paramètres :** Tokyo WR=9.55%, prix=1%, bet=$216, bankroll=$10K

| Métrique | Tokyo | New York |
|----------|-------|----------|
| E[P&L] 100 bets | **+$184,365** | +$1,855 |
| Médiane | $172,727 | $2,172 |
| P(profit) | **99.9%** | 55.5% |
| P(×2 bankroll) | **99.9%** | 1.1% |
| P(×5 bankroll) | **99.7%** | 0.0% |
| P(×10 bankroll) | **92.4%** | 0.0% |
| P(ruine >50%) | **0.0%** | 0.0% |
| P10 / P90 | $108K / $259K | −$2K / +$7K |

### Pourquoi Tokyo ×100 vs NYC ?

La math est simple : **WR Tokyo = 5× WR NYC**. Sur 100 bets à 99:1 payout :
- Tokyo : 9.5 wins attendus → 9.5 × $21K = $200K de gains
- NYC : 1.9 wins attendus → 1.9 × $21K = $40K de gains mais seulement 1.9 sur 100 → trop aléatoire

---

## ⚠️ Caveat critique — dépendance intra-journalière

Le Monte Carlo suppose **100 bets indépendants**. En réalité :
- Tokyo a UN T_max par jour
- Si tu achètes 10 bins Tokyo le même jour, ils sont **corrélés** (même résolution)
- Le "N effectif indépendant" = N jours différents, pas N tokens

**Impact :** P(profit) réel sur 100 bets est inférieure à 99.9%. L'espérance reste correcte, mais la variance est sous-estimée.

**Mitigation :**
1. Acheter des tokens sur plusieurs villes différentes le même jour (Tokyo + Paris + Milan → 3 résolutions indépendantes)
2. Acheter sur des dates différentes (T+1, T+2, T+3 dans le futur)

---

## Stratégie optimale — N bets simultanés

| N bets | E[P&L] | P(profit) | P(×5) | P(×10) | Sharpe |
|--------|--------|-----------|-------|--------|--------|
| 10 | $18K | 63% | 24.6% | 0.1% | 0.92 |
| 20 | $37K | 87% | 29.3% | 3.7% | 1.30 |
| 50 | $85K | 99% | 87.1% | 34.4% | 2.08 |
| 75 | $85K | 100% | 93.5% | 42.5% | 2.51 |
| 100 | $85K | 100% | 92.2% | 36.0% | 2.91 |

Optimal : **50+ bets simultanés** (sur plusieurs villes/dates) pour maximiser P(×5) et Sharpe.

---

## Règles opérationnelles

```python
# Villes ciblées (edge >5%) :
CONVEX_CITIES = ["tokyo", "paris", "milan", "london"]

# Villes exclues (edge quasi-nul ou négatif) :
EXCLUDED_CITIES = ["new york", "dallas", "miami", "los angeles",
                   "houston", "atlanta", "denver"]

# Condition d'entrée :
# 1. market_price < 2%
# 2. NWP P(YES) > market_price + 10 points (edge minimum)
# 3. Ville dans CONVEX_CITIES
# 4. TTR dans 40-8h (fenêtre collapse entropique)

# Sizing :
# bet_size = Kelly_f* × 0.25 × bankroll
# = (WR - price) / (1 - price) × 0.25 × bankroll
# Pour Tokyo à 1% avec WR=9.55% → $216

# Objectif : diversifier sur 5+ villes/dates indépendantes par cycle
```

---

## Related

- [[_system/MOC-patterns]]
- [[patterns/polymarket-price-process-deep-analysis]]
- [[patterns/polymarket-coldmath-no-ev-analysis]]
- [[patterns/polymarket-oracle-confirmed-backtest]]
- [[patterns/polymarket-bracket-arb]]
