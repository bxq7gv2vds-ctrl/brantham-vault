---
name: Architecture Intraday Trading Prediction Markets (Hedge Fund Level)
description: Architecture complète pour trader les mouvements de cotes avant résolution sur Polymarket — Jump-Diffusion, NWP Lead-Lag, Bracket Vol Surface, Order Flow
type: pattern
tags: [trading, intraday, polymarket, jump-diffusion, microstructure, hedge-fund]
---

# Pattern : Intraday Trading Prediction Markets

## Principe fondamental

Ne pas attendre la résolution. Les marchés de prédiction ont des inefficiences INTRADAY exploitables :
1. **NWP Lead-Lag** : marché prend 10-60 min à absorber les mises à jour NWP
2. **Bracket arbitrage** : les brackets (NYC march 31) doivent sommer à 1 → souvent 109% → arbitrage
3. **Jump-Diffusion** : log-odds suit un OU process + sauts aux updates NWP → trading régimes
4. **Order Flow** : order imbalance prédit la direction court terme

## Architecture des modules

### Layer 1 : Data
```
data/tick_store.py      → WebSocket events → SQLite 10s OHLCV bars
data/nwp_scheduler.py   → Détection runs GFS (00Z/06Z/12Z/18Z UTC), event NWP_JUMP
```
Schema SQLite :
- `ticks(token_id, ts, price, bid, ask, bid_size, ask_size)`
- `ohlcv(token_id, bar_ts, open, high, low, close, volume)`
- `nwp_runs(run_ts, city, date, mu_gfs, mu_icon, mu_gem, p_answer, delta_p)`

### Layer 2 : Modèles mathématiques

#### Jump-Diffusion (models/jump_diffusion.py)
```
dL = κ(μ-L)dt + σ_diff dW + J dN(t)
```
- L = log-odds : `logit(P)`
- J = saut au run NWP : `logit(p_new) - logit(p_old)`
- Absorption ratio : `(L_t - L_pre_jump) / J_expected`
- Exit condition : `absorption_ratio >= 0.80`
- Extension de SBMM existant (même Kalman, injection du saut)

#### Bracket Vol Surface (models/bracket_surface.py)
```
min Σ(p_market[i] - q[i])²   s.t. Σq[i]=1, q[i]>=0
```
- Distribution implicite du marché via CVXPY (déjà dans les deps)
- Comparer à distribution NWP EMOS → `mispricing[i] = p_market[i] - nwp_q[i]`
- Trade : short overpriced brackets, long underpriced brackets
- Observation : NYC March 31 sommait à 109.5% → violation structurelle

#### Microstructure (models/microstructure.py)
```
OI(t) = (bid_qty - ask_qty) / (bid_qty + ask_qty)   ∈ [-1, +1]
ΔL_impact = λ × sign(trade) × size^0.5             (Kyle 1985)
```

### Layer 3 : Signal Engine (strategy/intraday_engine.py)
Signal composite :
```
signal_total = 0.40×S_jump + 0.30×S_bracket + 0.20×S_oi + 0.10×S_sbmm
```
Kelly intraday (pas fondamental) :
```
edge_intraday = J_expected × (1 - exp(-α×T))
f = (edge_intraday / sigma_T) × kelly_fraction
```

### Layer 4 : Execution (infra/clob_executor.py)
- Limit orders uniquement (jamais market)
- `py-clob-client` (SDK officiel Polymarket, signing ECDSA Polygon)
- Placement à `best_bid + 0.001`, patience 30s, cancel si pas fill
- Fee Polymarket : 2% → taille min position : `max(10 USDC, spread × notional)`

## Timeline implémentation

**Buildable NOW (sans données historiques) :**
- tick_store.py + nwp_scheduler.py
- jump_diffusion.py (modèle mathématique, pas besoin de training)
- bracket_surface.py (CVXPY optimization)

**Après 2-4 semaines de collecte :**
- Calibration λ market impact
- Fit vitesse absorption NWP réelle (vs prior 30 min)
- Autocorrélation intraday des returns → signal OI calibré
- Backtest sur tick data collecté

## P&L théorique (bankroll $10k)
- 4 runs NWP/jour × 15 marchés = 60 opportunités/jour
- Win rate estimé : 60-65%
- Edge moyen : ~8%
- Taille moyenne : $300
- P&L/jour espéré : ~$500-600 (hypothétique)

## Dépendances à ajouter
```toml
"py-clob-client>=0.18"  # SDK officiel Polymarket
```

## Related
- [[founder/sessions/2026-03-29-polymarket-hedge-engine]]
- [[patterns/polymarket-nwp-emos-calibration]]
- [[_system/MOC-patterns]]
