---
name: Polymarket — Stratégie convexe par ville (variance optimizer v2)
description: Analyse Sharpe+Monte Carlo sur 37 villes, 486K obs. Portefeuille optimal 22 villes. Mexico City 18.6%, Taipei 16.8%, Madrid 16.2%, Tokyo 14.2%.
type: pattern
project: polymarket-hedge
tags: [polymarket, convex, kelly, monte-carlo, sharpe, variance-optimizer, longshot]
date: 2026-04-11
scripts:
  - scripts/variance_optimizer.py
  - scripts/city_convex_strategy.py
outputs:
  - analysis/T_sharpe_ranking.png
  - analysis/T_portfolio_frontier.png
  - analysis/T1_variance_*.png
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

## Implémentation dans run_bracket_scalper.py (2026-04-11)

Signal `CONVEX_YES` implémenté dans `scripts/run_bracket_scalper.py` :

```python
# Dict ville → WR empirique (backtest 2026-03-05 to 2026-04-05)
CONVEX_CITIES_WR = {
    "tokyo":       0.096,   # n=3695 (+8.6%)  ***
    "paris":       0.086,   # n=4736 (+7.6%)  ***
    "milan":       0.080,   # n=2789 (+7.0%)  **
    "london":      0.067,   # n=5230 (+5.7%)  **
    "shanghai":    0.068,   # n=~1500 (+4.8%) *
    "tel aviv":    0.065,   # n=~800  (+4.5%) *
    "mexico city": 0.107,   # n=422   (+9.7%) * petit n → Kelly conservatif
}

# Villes exclues (edge nul ou négatif) :
CONVEX_EXCLUDED = frozenset({
    "new york", "new york city", "nyc", "dallas", "miami", "atlanta",
    "austin", "houston", "seattle", "los angeles", "san francisco",
    "denver", "boston", "phoenix", "chicago",
    "singapore", "lucknow"
})

# Condition d'entrée CONVEX_YES :
# 1. city in CONVEX_CITIES_WR
# 2. 0.002 <= yes_price < 0.02  (fourchette 0.2%-2%)
# 3. ttr_hours >= 8.0
# 4. city not in CONVEX_EXCLUDED
# (Pas besoin de NWP — edge purement statistique)

# Sizing :
# kelly_f = (WR_city - yes_price) / (1 - yes_price) × 0.25
# size = min(kelly_f × bankroll, max_convex_size)  # capped at $250
```

**Résultats live (2026-04-11, bankroll $10K) :**
- 42 CONVEX_YES générés en un seul scan
- Villes actives : Tokyo, Paris, Milan, Shanghai, London, Mexico City, Tel Aviv
- Tailles typiques : $157 (Tel Aviv) → $250 (Mexico City, cap atteint)
- LONGSHOT_YES correctement filtré : 0 ville US dans les 11 signaux

**Priorité dans la pile de signaux :**
`CONFIRMED > CERT_NO > SPEEDA > COLDMATH > CONVEX_YES > LONGSHOT_YES > PROB`

---

## Variance Optimizer — Résultats complets (2026-04-11)

**Script** : `scripts/variance_optimizer.py` — 486K obs, 37 villes, bins fins [0.2%–3.0%]

### Classement Sharpe/100 (top 22 villes rentables)

| Ville | Px optimal | WR | Sharpe/100 | Std/100 | P(+) |
|-------|-----------|-----|-----------|---------|------|
| ★★★★ Mexico City | 0.20% | 18.6% | 4.74 | $29K | 100% |
| ★★★★ Taipei | 1.80% | 16.8% | 4.01 | $3.1K | 100% |
| ★★★★ Madrid | 1.80% | 16.2% | 3.90 | $3.1K | 100% |
| ★★★★ Tokyo | 1.80% | 14.2% | 3.56 | $2.9K | 100% |
| ★★★ Hong Kong | 2.25% | 13.9% | 3.36 | $2.3K | 100% |
| ★★★ Milan | 1.80% | 12.8% | 3.29 | $2.8K | 100% |
| ★★★ Austin | 1.00% | 11.2% | 3.23 | $4.7K | 100% |
| ★★★ Beijing | 1.80% | 12.3% | 3.19 | $2.7K | 100% |
| ★★★ Paris | 0.60% | 10.2% | 3.17 | $7.5K | 100% |
| ★★★ Tel Aviv | 1.80% | 11.5% | 3.04 | $2.6K | 100% |
| ★★ Wuhan | 1.00% | 9.8% | 2.96 | $4.5K | 100% |
| ★★ Warsaw | 1.80% | 10.7% | 2.88 | $2.6K | 100% |
| ★★ Shanghai | 0.60% | 8.7% | 2.87 | $7.0K | 100% |
| ★★ London | 1.00% | 9.0% | 2.79 | $4.3K | 100% |
| ★ Buenos Aires | 2.25% | 10.6% | 2.72 | $2.0K | 100% |
| ★ Atlanta | 2.25% | 10.4% | 2.66 | $2.0K | 100% |
| ★ Chengdu | 2.25% | 10.1% | 2.60 | $2.0K | 100% |
| ★ Wellington | 1.40% | 8.7% | 2.60 | $3.0K | 100% |
| ★ São Paulo | 2.25% | 9.2% | 2.41 | $1.9K | 100% |
| ★ Toronto | 0.60% | 6.2% | 2.33 | $6.0K | 100% |
| ★ Seoul | 1.40% | 7.6% | 2.33 | $2.8K | 100% |
| ★ Munich | 2.25% | 8.6% | 2.27 | $1.9K | 99% |

**Portefeuille optimal** : 9 villes (Sharpe > 3.0) — Mexico City, Taipei, Madrid, Tokyo, Hong Kong, Milan, Austin, Beijing, Paris

**Villes SKIP** (EV ≤ 0) : Houston, Los Angeles

**Villes exclues** (Sharpe < 1.5) : Dallas (0.24), Singapore (0.83), Lucknow (0.65), Moscow (1.26)

### Erreurs de calibration initiale corrigées

| Ville | WR initial | WR corrigé | Bucket optimal | Cause |
|-------|-----------|-----------|---------------|-------|
| Tokyo | 9.6% | **14.2%** | 1.80% (vs global <2%) | mauvais bucket |
| Paris | 8.6% | **10.2%** | 0.60% | mauvais bucket |
| Milan | 8.0% | **12.8%** | 1.80% | mauvais bucket |
| Austin | exclu | **11.2%** (Sharpe=3.23) | 1.00% | exclusion erronée |
| Atlanta | exclu | 10.4% (Sharpe=2.66) | 2.25% | exclusion à vérifier |
| Taipei | absent | **16.8%** (Sharpe=4.01) | 1.80% | ville non incluse |
| Madrid | absent | **16.2%** (Sharpe=3.90) | 1.80% | ville non incluse |
| Hong Kong | absent | 13.9% (Sharpe=3.36) | 2.25% | ville non incluse |

### Règles opérationnelles (v2 — post variance_optimizer)

```python
# 22 villes ciblées — voir CONVEX_CITIES_WR dans run_bracket_scalper.py
# Format: WR @ Sharpe-optimal bucket | max_convex_size=$15 (liquidity cap)

# Condition d'entrée :
# 1. market_price ∈ [0.2%, 2.5%)
# 2. Ville dans CONVEX_CITIES_WR (22 villes)
# 3. TTR >= 8h
# 4. Ville NOT in CONVEX_EXCLUDED

# Sizing :
# kelly_f = (WR_city - price) / (1 - price) × 0.25
# size = min(kelly_f × bankroll, 15.0)  # cap ordre book réaliste

# Déploiement typique : 40-70 signaux × $15 = $600-$1,050/scan
# EV par bet : +200-570% sur ask réel ($6-$11 fill)
# Diversification : 22 villes × prix indépendants = corrélation minimale
```

---

## Related

- [[_system/MOC-patterns]]
- [[patterns/polymarket-price-process-deep-analysis]]
- [[patterns/polymarket-coldmath-no-ev-analysis]]
- [[patterns/polymarket-oracle-confirmed-backtest]]
- [[patterns/polymarket-bracket-arb]]
