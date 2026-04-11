---
name: Session — Analyse mathématique profonde des prix Polymarket
type: session
project: polymarket-hedge
date: 2026-04-11
tags: [polymarket, quant, stochastic-process, fat-tails, calibration, markov, session]
---

# Session — Analyse mathématique profonde des prix Polymarket

**Date :** 2026-04-11 (session 8)
**Contexte :** Suite de la session 7 (diagnostic COLDMATH_NO). Objectif : aller bien plus loin dans l'analyse mathématique des flux de prix pour identifier des patterns exploitables.

---

## Ce qui a été fait

### 1. Script d'analyse de surface (session 7)
`scripts/price_pattern_analysis.py` — lancé et interprété :
- Trajectoires YES vs NO par TTR
- Heatmap EV par (price_bucket × TTR)
- ACF à 6 lags
- Timing des jumps

**Résultat surface :** cheap YES (1-8¢) EV positif +3-6%, confirme LONGSHOT_YES.

### 2. Script d'analyse profonde (session 8)
`scripts/price_deep_analysis.py` — nouveau script ~800 lignes couvrant 10 analyses :

1. **Distribution fitting** (Normal/Laplace/Student-t MLE + Hill estimator)
2. **ACF/PACF 48 lags** + Ljung-Box Q-test
3. **Variance Ratio Test** (Lo-MacKinlay 1988)
4. **Processus OU** (Ornstein-Uhlenbeck) global + par bucket
5. **Chaîne de Markov empirique** 12×12 + stationary + mixing + absorption
6. **Hazard rate** P(|Δp|>5% | price, TTR)
7. **Courbe de calibration** market_price vs P_empirique(YES)
8. **Volatilité conditionnelle** σ(Δp | price, TTR)
9. **Entropie de Shannon** H(prix | TTR)
10. **Momentum conditionnel** E[Δp_futur | direction_passée]

---

## Résultats clés par ordre d'importance

### #1 — Courbe de calibration (finding le plus actionable)

Le marché **sous-évalue systématiquement** les YES à prix < 6% :

```
Prix 0.5% → P(YES) réel = 3.4%   edge = +2.9%  n=87842  ***
Prix 1.5% → P(YES) réel = 4.9%   edge = +3.4%  n=40414  ***
Prix 2.5% → P(YES) réel = 5.6%   edge = +3.1%  n=23355  ***
Crossover exact : ~6.5%
Prix 10%  → P(YES) réel = 7.6%   edge = −2.4%  n=42702
Prix 25%  → P(YES) réel = 11.5%  edge = −13.5% n=70106
```

Biais d'ancrage : tokens à 20% semblent "pas chers" aux traders, créant une surévaluation structurelle. Tokens à 1% semblent "impossibles", créant une sous-évaluation structurelle. LONGSHOT_YES exploite exactement ce biais.

### #2 — Distribution Pareto (α=1.89, ν=0.3)

Variance infinie. Kelly Gaussien invalide. Les queues arrivent ~50-100x plus souvent que prévu sous hypothèse Gaussienne. Confirme le maintien de Kelly × 0.25 max.

### #3 — Martingale rejetée (VR test)

VR(2h)=0.874, VR(24h)=0.331, VR(48h)=0.257 — tous significatifs à Z>38. Le marché mean-reverte sur tous les horizons. Après un gros move sans information fondamentale → le prix revient.

### #4 — OU half-life = 47h

Un token à 25% sans signal NWP revient vers θ=5% en ~47h. Timing d'entrée optimal : sur des tokens qui ont dévié vers le haut récemment sans cause visible.

### #5 — Markov : mixing time = 345h

Le marché "se souvient" de son état pendant 14 jours. Quasi-non-ergodique. Les états <1% et >98% sont quasi-absorbants. Les probabilités d'absorption Markov sous-estiment P(→YES) à cause des sauts à longue queue.

### #6 — Information arrive à TTR=40-8h

Collapse entropique commence à TTR≈40h. Fenêtre optimale pour les scans NWP.

### #7 — Mean-reversion à 1h (bid-ask bounce)

E[Δp(t+1) | Δp(t)>+1%] = −0.006. Après un jump haussier : attendre 1h avant d'entrer.

---

## Fichiers créés

| Fichier | Description |
|---------|-------------|
| `scripts/price_deep_analysis.py` | Script complet 10 analyses |
| `analysis/A_distributions.png` | Distribution fitting + QQ plots |
| `analysis/B_acf_pacf.png` | ACF/PACF 48 lags + Ljung-Box |
| `analysis/C_variance_ratio.png` | VR test martingale |
| `analysis/E_markov.png` | Chaîne de Markov 12×12 |
| `analysis/F_hazard.png` | Hazard rate surface |
| `analysis/G_calibration.png` | Courbe de calibration |
| `analysis/H_cond_vol.png` | Volatilité conditionnelle |
| `analysis/I_entropy_momentum.png` | Entropie + momentum conditionnel |
| `vault/patterns/polymarket-price-process-deep-analysis.md` | Pattern vault |

---

## Décisions prises

1. **Signal LONGSHOT_YES confirmé empiriquement** par la courbe de calibration (6562 marchés, IC 95% strictement positif pour prix <4%)
2. **Pas de scalp intraday** — pas de pattern directionnel exploitable par heure UTC
3. **Kelly × 0.25 maintenu** — distribution Pareto α=1.89 justifie la prudence
4. **Fenêtre prioritaire TTR=40-8h** pour les scans NWP

---

## Related

- [[_system/MOC-patterns]]
- [[patterns/polymarket-price-process-deep-analysis]]
- [[patterns/polymarket-coldmath-no-ev-analysis]]
- [[patterns/polymarket-oracle-confirmed-backtest]]
- [[founder/sessions/2026-04-11-polymarket-coldmath-diagnosis]]
