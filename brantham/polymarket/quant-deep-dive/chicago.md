---
type: quant-deep-dive
city: Chicago
slug: chicago
date: 2026-04-22
n_markets: 698
n_trades: 398810
volume_usdc: 2124398
yes_win_rate: 0.1059
hurst: 0.8703
xgb_auc: 0.7509
best_strategy: buy_yes_longshot
best_ev_pct: 81.77
ofi: 0.6855
tags: [polymarket, weather, quant, chicago]
---

# Chicago — Quant Deep Dive Note

Ville : **Chicago** (chicago) — 698 marchés, 398,810 trades, $2.12M volume.

## Findings clés

- **Hurst H=0.870** (trending) — mémoire longue, persistance des drifts négatifs (NO edge)
- **AUC XGBoost=0.751** — signal prédictif ex-ante exploitable
- **OFI=0.685** — pression acheteuse structurelle (forte)
- **YES win rate réel=10.6%** vs prix moyen ouverture=0.139 → sur-estimation systématique
- **Best edge : buy yes longshot** — EV/bet=+81.8%

## Stratégie recommandée

1. **Buy NO brackets** : EV=+5.2%, WR=0.901, seuil entrée YES<0.85
2. **Buy NO uncertain** : EV=+25.7%, seuil [0.45-0.55] avec OFI<0.6
3. **Éviter** : YES longshots (<10%) — Sharpe=0.075

## Related

- [[_MOC]]
- [[odds-trajectories-v2-findings]]
- [[per-city-deep-dive/chicago|Deep Dive Baseline Chicago]]
- [[tier-s-v2-hedge-fund-gates]]
- [[capacity-reality-check]]
