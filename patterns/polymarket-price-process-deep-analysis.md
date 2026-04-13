---
name: Polymarket — Analyse mathématique profonde du processus de prix
description: 10 analyses stats/proba sur 6562 marchés / 411K rendements houraires — distribution, Markov, OU, calibration, VR test
type: pattern
project: polymarket-hedge
tags: [polymarket, quant, stochastic-process, calibration, markov, OU, fat-tails, mean-reversion]
date: 2026-04-11
scripts:
  - scripts/price_deep_analysis.py
  - scripts/price_pattern_analysis.py
outputs:
  - analysis/A_distributions.png
  - analysis/B_acf_pacf.png
  - analysis/C_variance_ratio.png
  - analysis/E_markov.png
  - analysis/F_hazard.png
  - analysis/G_calibration.png
  - analysis/H_cond_vol.png
  - analysis/I_entropy_momentum.png
---

# Polymarket — Analyse mathématique profonde du processus de prix

## Dataset

- **6 562 marchés bracket** avec outcome oracle confirmé
- **411 001 paires consécutives 1h** (rendements Δp)
- 27 villes, 31 jours (2026-03-05 → 2026-04-05)
- Script : `scripts/price_deep_analysis.py`

---

## A — Distribution des rendements Δp : queues de Pareto

**Meilleur fit par AIC (MLE) :**

| Modèle | AIC | Paramètre clé |
|--------|-----|---------------|
| Normal | -1 684 987 | σ=0.031 |
| Laplace | -2 234 161 | b=0.012 |
| **Student-t** | **-4 612 536** | **ν=0.3** ← gagnant |

**ν=0.3 < 1** → pire que Cauchy (ν=1). La distribution a une **variance infinie** (besoin ν>2 pour variance finie).

**Hill estimator : α=1.89**
→ P(|Δp| > x) ~ x^{−1.89} (loi de puissance Pareto)
→ α<2 confirme variance infinie
→ Kurtosis excès = 153.69 (Normal=0, t-Student typique ~10-30)

**Implication critique :** Kelly Gaussien invalide. VaR Gaussien dangereusement sous-estimé. Les mouvements "rares" arrivent 50-100× plus souvent que prévu sous hypothèse normale.

---

## B — ACF/PACF : structure temporelle significative

- ρ(lag=1h) = **−0.090** (hors bandes IC 95%)
- Tous les lags 1-48h : Ljung-Box Q(5) p≈0, Q(24) p≈0
- **Conclusion : prix NON i.i.d.** — structure temporelle certaine

Mean-reversion immédiate : si Δp(t) > 0 → E[Δp(t+1)] < 0 et vice versa.

---

## C — Variance Ratio Test (Lo-MacKinlay 1988) : martingale rejetée

**VR(q) = Var[q-step return] / (q × Var[1-step return])**
Sous H₀ (martingale) : VR(q)=1. VR<1 = mean-reversion.

| Horizon q | VR(q) | Z-stat | p-value |
|-----------|-------|--------|---------|
| 2h | 0.874 | −82.8 | ≈0 |
| 4h | 0.724 | −95.8 | ≈0 |
| 8h | 0.557 | −94.1 | ≈0 |
| 16h | 0.396 | −80.6 | ≈0 |
| 24h | 0.331 | −66.6 | ≈0 |
| 48h | 0.257 | −38.7 | ≈0 |

**Martingale rejetée à tous les horizons.** Z-stats de 38-96 — certitude absolue.

VR décroît avec q : la mean-reversion s'amplifie sur les horizons plus longs. Pattern caractéristique d'un processus OU.

---

## D — Processus Ornstein-Uhlenbeck

**Équation :** dP = κ(θ − P)dt + σ dW

**Paramètres estimés (OLS, 440 585 paires) :**

```
κ = 0.0147/h    →  half-life = 47h
θ = 0.051       →  équilibre naturel ≈ 5%  (les YES sont "attirés" vers 5%)
σ = 0.032/h     →  3.2% de diffusion par heure
R² = 0.003      →  faible mais significatif à 440K obs
```

**Interprétation :**
- Tout token YES tend vers θ=5% en l'absence d'information
- Déviation de 20% (e.g. prix à 25%) → retour vers 5% en ~47h
- La mean-reversion n'est pas une opportunité en soi : c'est la signature de l'absence de signal

**OU par bucket de prix (κ):**
- Buckets 0-15% : κ légèrement positif → mean-reverting
- Buckets 60-100% : κ très négatif → **explosif** (convergence vers YES en cours)
- La non-linéarité du κ confirme que le processus réel est OU uniquement en première approximation

---

## E — Chaîne de Markov empirique 12×12

**États :** <1%, 1-3%, 3-6%, 6-10%, 10-15%, 15-25%, 25-40%, 40-60%, 60-80%, 80-92%, 92-98%, >98%

### Persistance (P[rester dans le même bucket]) :

| État | P[stay] | n obs |
|------|---------|-------|
| <1% | **0.967** | 77 445 |
| 1-3% | 0.854 | 59 326 |
| 3-6% | 0.759 | 42 744 |
| 10-15% | 0.716 | 43 690 |
| 15-25% | 0.829 | 81 186 |
| >98% | **0.981** | 880 |

**Mixing time = 345.8h** (λ₂=0.9971)
→ Le marché a une mémoire de ~14 jours. Quasi-non-ergodique à court terme.

### Probabilités d'absorption (→0% vs →100%) :

| État de départ | P(→YES) | P(→NO) |
|----------------|---------|--------|
| 1-3% | 1.0% | 99.0% |
| 6-10% | 3.2% | 96.8% |
| 15-25% | 6.1% | 93.9% |
| 25-40% | **8.6%** | 91.4% |
| 60-80% | **42.9%** | 57.1% |
| 80-92% | **78.9%** | 21.1% |

**Note critique** : P_Markov(→YES | 1-3%) = 1% mais la calibration empirique donne 4-5%. La différence s'explique par les sauts à longue queue (événements extrêmes qui court-circuitent la diffusion Markov).

---

## G — Courbe de calibration (résultat le plus important)

**Est-ce que le prix marché = P(YES) réelle ?** Non.

### Zone sous-évaluée (YES trop pas cher) :

| Prix marché | P(YES) réel | Edge | n | CI 95% |
|------------|-------------|------|---|--------|
| 0.5% | **3.4%** | +2.9% | 87 842 | [3.3%, 3.5%] *** |
| 1.5% | **4.9%** | +3.4% | 40 414 | [4.7%, 5.1%] *** |
| 2.5% | **5.6%** | +3.1% | 23 355 | [5.3%, 5.9%] *** |
| 4.0% | **5.6%** | +1.6% | 33 226 | [5.4%, 5.9%] *** |
| ~6.5% | 6.5% | **0%** | 35 973 | ← crossover |

### Zone surévaluée (YES trop cher) :

| Prix marché | P(YES) réel | Edge | n |
|------------|-------------|------|---|
| 10% | 7.6% | **−2.4%** | 42 702 |
| 16% | 9.6% | **−6.4%** | 75 631 |
| 25% | 11.5% | **−13.5%** | 70 106 |

**Crossover à 6-7%** : en-dessous = structurellement sous-évalué, au-dessus = structurellement surévalué.

### Pourquoi ce biais ?

Biais d'ancrage + base rate neglect (Kahneman) :
- Un token à 20% semble "pas cher" → les traders y voient de la valeur → surenchère
- Un token à 1% semble "quasi-impossible" → les traders ignorent → sous-enchère
- La vérité : les marchés météo ont un base rate de 7-8% de YES sur les bins improbables, pas 20%

---

## H — Volatilité conditionnelle σ(Δp | état)

**Volatilité varie de 20× selon l'état :**

| Bucket prix | TTR long | TTR court (0-6h) |
|-------------|----------|-----------------|
| 0-6% | σ ≈ 1.5-2.5% | σ ≈ 2-4% |
| 10-25% | σ ≈ 2.5-3.5% | σ ≈ 5-9% |
| 40-60% | σ ≈ 4-9% | σ ≈ 12-13% |
| 60-85% | σ ≈ **26%** | σ ≈ **26%** |
| 85-100% | σ ≈ 10-18% | σ ≈ 18% |

→ Kelly sizing doit adapter la taille selon σ conditionnel, pas σ global.

---

## I — Entropie de Shannon H(prix|TTR)

Le collapse entropique commence à **TTR ≈ 40h** :

```
TTR=100h : H=1.75 nats
TTR=80h  : H=1.87 nats  (pic — incertitude maximale)
TTR=40h  : H=1.73 nats  (début du collapse)
TTR=10h  : H=1.65 nats
TTR=0h   : H=1.60 nats  (collapse terminal)
```

**Implication** : l'information NWP est la plus actionable dans la fenêtre **TTR=40-8h**. C'est là que le marché commence à intégrer l'information météo et que notre modèle NWP a un avantage.

---

## J — Momentum conditionnel

```
E[Δp(t+1) | Δp(t) > +1%] = −0.0063  → mean-reversion immédiate après hausse
E[Δp(t+1) | Δp(t) < −1%] = +0.0026  → légère récupération après baisse
lag=2-12h : convergence vers 0
```

Signal de mean-reversion à **1h uniquement** (probablement bid-ask bounce + market makers). Pas exploitable seul (fees > signal). Mais utile pour **timing des entrées** : après un gros move haussier, attendre 1h.

---

## Synthèse et règles opérationnelles

### Règle 1 — Taille de position (distribution Pareto)
```python
# Variance infinie (α=1.89 < 2) → Kelly Gaussien invalide
# Utiliser Kelly × 0.25 max (déjà configuré dans ScalpConfig)
# Ne jamais scaler la taille sans backtester sur les queues
```

### Règle 2 — Calibration (la règle la plus importante)
```python
# Acheter YES si market_price < 6% ET edge NWP confirmé  →  structurellement +EV
# NE PAS acheter YES si market_price > 10%               →  structurellement -EV
# Exception : CONFIRMED oracle (certitude 100%) ignore la calibration
```

### Règle 3 — Timing d'entrée
```python
# Fenêtre optimale : TTR=40-8h (collapse entropique commence)
# Après un jump haussier sur un token : attendre 1h (mean-reversion lag=1)
# Half-life OU = 47h → un token monté sans information revient en ~2 jours
```

### Règle 4 — Processus non-martingale
```python
# VR(q) << 1 pour tout q → les prix mean-révertent
# Un token qui a monté sans signal NWP → probabilité de retour vers θ=5%
# Ne pas "chaser" les moves récents
```

### Règle 5 — Ne jamais utiliser la persistance Markov seule
```python
# P_Markov(→YES | 1-3%) = 1% ≠ P_empirique(YES | 1-3%) = 4-5%
# La différence = sauts à longue queue non capturés par la diffusion
# Toujours croiser avec le signal NWP pour les entrées
```

---

## Related

- [[_system/MOC-patterns]]
- [[patterns/polymarket-coldmath-no-ev-analysis]]
- [[patterns/polymarket-oracle-confirmed-backtest]]
- [[patterns/polymarket-bracket-arb]]
- [[patterns/polymarket-nwp-emos-calibration]]
