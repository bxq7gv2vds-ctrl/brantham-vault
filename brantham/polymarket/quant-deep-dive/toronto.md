---
type: quant-deep-dive
city: Toronto
slug: toronto
date: 2026-04-22
n_markets: 1024
n_trades: 357387
volume_usdc: 2004502
yes_win_rate: 0.1053
hurst: 0.7131
xgb_auc: 0.7684
best_strategy: buy_no_favorites
best_ev_pct: 2409.49
ofi: 0.7349
tags: [polymarket, weather, quant, toronto]
---

# Toronto — Quant Deep Dive Note

Ville : **Toronto** (toronto) — 1,024 marchés, 357,387 trades, $2.00M volume.

## Findings clés

- **Hurst H=0.713** (trending) — mémoire longue, persistance des drifts négatifs (NO edge)
- **AUC XGBoost=0.768** — signal prédictif ex-ante exploitable
- **OFI=0.735** — pression acheteuse structurelle (forte)
- **YES win rate réel=10.5%** vs prix moyen ouverture=0.136 → sur-estimation systématique
- **Best edge : buy no favorites** — EV/bet=+2409.5%

## Stratégie recommandée

1. **Buy NO brackets** : EV=+7.0%, WR=0.904, seuil entrée YES<0.85
2. **Buy NO uncertain** : EV=+23.9%, seuil [0.45-0.55] avec OFI<0.6
3. **Éviter** : YES longshots (<10%) — Sharpe=-0.022

## Related

- [[_MOC]]
- [[odds-trajectories-v2-findings]]
- [[per-city-deep-dive/toronto|Deep Dive Baseline Toronto]]
- [[tier-s-v2-hedge-fund-gates]]
- [[capacity-reality-check]]
