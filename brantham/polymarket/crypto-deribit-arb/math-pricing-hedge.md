---
title: Math — Pricing & Hedge
created: 2026-04-23
parent: [[_MOC]]
tags: [math, pricing, hedge, breeden-litzenberger, svi, kelly]
---

# Math complète — Pricing & Hedge

## 1. Extraction de la fair value : Breeden-Litzenberger

Un bracket Polymarket "S(T) ∈ [K1, K2]" = digital double. Payoff = $1 si S(T) ∈ [K1, K2], sinon $0.

**Théorème de Breeden-Litzenberger (1978)** :
$$f(K) = \frac{\partial^2 C(K, T)}{\partial K^2}$$
où f(K) est la densité risque-neutre du prix S(T), extractible de la chaîne d'options Deribit.

**Donc** :
$$P(S(T) \in [K_1, K_2]) = \int_{K_1}^{K_2} f(K) \, dK = \frac{\partial C}{\partial K}\bigg|_{K_1} - \frac{\partial C}{\partial K}\bigg|_{K_2}$$

Sous Black-Scholes (baseline naive) :
$$P = N(d_2(K_1)) - N(d_2(K_2)), \quad d_2 = \frac{\ln(S/K) + (r - \sigma^2/2)T}{\sigma\sqrt{T}}$$

## 2. Modèle de smile : SVI (Stochastic Volatility Inspired)

Black-Scholes flat ignore le smile observable. On fit le smile entier avec SVI (Gatheral 2004) :

$$\sigma^2_{SVI}(k) = a + b\{\rho(k-m) + \sqrt{(k-m)^2 + \sigma^2}\}$$

où :
- k = log-moneyness = ln(K/S)
- 5 paramètres : a (level), b (slope), ρ (rotation), m (translation), σ (smoothness)
- Fit par moindres carrés sur les vol implicites Deribit

**Pourquoi SVI** :
- Smoothing intégré (élimine noise des options peu liquides aux ailes)
- Fit rapide (~5ms via scipy.optimize.least_squares)
- No arbitrage si paramètres dans bornes valides
- Standard de l'industrie (Goldman, JPM, etc.)

## 3. Risk-neutral density via Breeden-Litzenberger sur SVI

Une fois SVI calibré :

1. Reconstruct call prices C(K, T) for fine grid of K via BS avec σ_SVI(K)
2. Compute f(K) = ∂²C/∂K² par finite differences (centered, h adaptive)
3. Smooth optionally avec Savitzky-Golay filter
4. Vérifier : ∫ f(K) dK = 1 (normalisation)

## 4. Pricing du bracket : fair_prob

```python
def bracket_fair_prob(K1: float, K2: float, density: Callable) -> float:
    return scipy.integrate.quad(density, K1, K2)[0]
```

Ou plus rapide via cumulative trapezoid :

```python
def bracket_fair_prob_grid(K1, K2, K_grid, f_grid):
    mask = (K_grid >= K1) & (K_grid <= K2)
    return np.trapz(f_grid[mask], K_grid[mask])
```

## 5. Greeks du bracket (digital double)

Delta :
$$\Delta = \frac{\partial P}{\partial S} = f(K_1) - f(K_2)$$

Gamma :
$$\Gamma = \frac{\partial^2 P}{\partial S^2} = f'(K_1) - f'(K_2)$$

Vega :
$$Vega = \frac{\partial P}{\partial \sigma}$$
Calculé numériquement via bump-and-revalue (perturber σ_SVI level de +1pp, recalculer fair_prob, divide).

Theta :
$$\Theta = \frac{\partial P}{\partial T}$$
Bump T par -1 jour, recalculer.

## 6. Fees Polymarket — formule exacte

Source : docs Polymarket 2026.

```python
FEE_RATES = {
    "crypto": 0.072,   # highest
    "sports": 0.030,
    "politics": 0.040,
    "geopolitics": 0.000,
}

def polymarket_fee_usdc(shares: float, price: float, category: str = "crypto") -> float:
    """Exact Polymarket taker fee in USDC."""
    rate = FEE_RATES[category]
    return shares * rate * price * (1 - price)

def polymarket_fee_pct_of_notional(price: float, category: str = "crypto") -> float:
    """Fee as percentage of notional ($1 per share)."""
    rate = FEE_RATES[category]
    return rate * price * (1 - price)
```

**Maker = 0% fee + 20% rebate** sur les taker fees collectés (pour crypto).

Symétrie : trade à p=0.20 = trade à p=0.80 (même fee).
Fee max à p=0.50 = 1.80%.
Fee à ailes (p=0.05 ou 0.95) = 0.34%.

## 7. Edge net

```python
def edge_net(poly_price: float, fair_prob: float, side: str = "buy_yes") -> float:
    """Edge net après fees Polymarket (taker, hold to settlement)."""
    if side == "buy_yes":
        edge_brut = fair_prob - poly_price       # we pay poly_price, expect fair_prob
    else:  # buy_no = sell_yes
        edge_brut = (1 - fair_prob) - (1 - poly_price)  # = poly_price - fair_prob
    
    fee = polymarket_fee_pct_of_notional(poly_price, "crypto")
    return edge_brut - fee
```

**Threshold pratique** : signal si |edge_net| > 2pp (200 bps).

## 8. Kelly multi-asset avec Ledoit-Wolf shrinkage

Pour position individuelle binaire :
$$f^* = \frac{\epsilon}{\sigma^2} = \frac{\text{edge}}{p(1-p)}$$

Mais Kelly full = trop agressif. Fractional Kelly :
$$f_{used} = \alpha \times f^*, \quad \alpha = 0.25$$

Pour portefeuille :
$$\vec{f} = \alpha \times \Sigma^{-1} \vec{\epsilon}$$

avec Σ matrice covariance des positions, ε vecteur d'edges.

**Shrinkage Ledoit-Wolf** pour Σ :
$$\hat{\Sigma} = (1-\lambda) \Sigma_{empirical} + \lambda \Sigma_{prior}$$

avec λ optimal = formule fermée Ledoit-Wolf (2004), Σ_prior = diagonal + corrélation moyenne constante.

**Sizing avec budget de risque** ($1000 capital, max DD 30%) :

```python
total_var_budget = (0.30 * capital) ** 2 / annual_horizon   # daily VaR target
per_position_var = total_var_budget / N
size_i = sqrt(per_position_var / sigma_i ** 2)
```

## 9. Hedge optimizer (cvxpy)

```python
import cvxpy as cp

def optimize_hedge(portfolio_greeks, hedge_instruments):
    """
    portfolio_greeks: dict with 'delta', 'gamma', 'vega' (per asset)
    hedge_instruments: list of dicts {'asset', 'delta', 'gamma', 'vega', 'cost'}
    """
    n = len(hedge_instruments)
    w = cp.Variable(n)  # weights per instrument
    
    # Hedge contribution
    delta_hedge = sum(w[i] * h['delta'] for i, h in enumerate(hedge_instruments))
    gamma_hedge = sum(w[i] * h['gamma'] for i, h in enumerate(hedge_instruments))
    vega_hedge = sum(w[i] * h['vega'] for i, h in enumerate(hedge_instruments))
    
    # Cost
    cost = sum(cp.abs(w[i]) * h['cost'] for i, h in enumerate(hedge_instruments))
    
    constraints = [
        portfolio_greeks['delta'] + delta_hedge == 0,                      # delta neutral
        cp.abs(portfolio_greeks['vega'] + vega_hedge) <= VEGA_CAP,         # vega bounded
        cp.abs(portfolio_greeks['gamma'] + gamma_hedge) <= GAMMA_CAP,      # gamma bounded
    ]
    
    problem = cp.Problem(cp.Minimize(cost), constraints)
    problem.solve(solver=cp.ECOS)
    
    return w.value
```

## 10. Variance reduction par diversification

Sharpe portfolio avec N positions indépendantes (ρ ≈ 0) :
$$\text{Sharpe}_{portfolio} \approx \sqrt{N} \times \text{Sharpe}_{individual}$$

Avec corrélation ρ moyenne :
$$\text{Sharpe}_{portfolio} = \frac{\bar{\epsilon}}{\bar{\sigma} \sqrt{(1-\rho)/N + \rho}}$$

Pour N → ∞ : Sharpe → ε̄ / (σ̄ × √ρ). Donc même avec corrélation ρ=0.3, Sharpe atteint ε̄/(σ̄×0.55) = 1.8x Sharpe individual.

**Targets pratiques** :
- Sharpe individual : 0.2-0.4 (binaire à grosse variance)
- N positions : 30-100
- Corrélation moyenne : 0.2-0.4
- → **Sharpe portfolio : 1.5-3.0**

## 11. Math du capacity

Limite d'AUM avant price impact significatif :

$$\text{Capacity}_{bracket} \approx 0.10 \times V_{daily,bracket}$$

$$\text{Capacity}_{total} \approx 0.10 \times \sum_i V_{daily,i}$$

Pour Polymarket crypto :
- Volume total : $10-30M/jour
- Capacity safe : **$1-3M AUM théorique**
- En pratique avec slippage progressif : **$250-500k AUM**

Au-delà : Sharpe se dégrade, edge meurt.

## Related

- [[_MOC]]
- [[architecture]]
- [[risks-mitigation]]
