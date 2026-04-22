---
type: quant-deep-dive
city: Wellington
slug: wellington
date: 2026-04-22
n_markets: 684
n_trades: 312315
volume_usdc: 2460646
yes_win_rate: 0.1114
hurst: 1.0943
xgb_auc: 0.8725
best_strategy: buy_no_uncertain
best_ev_pct: 40.85
ofi: 0.7582
tags: [polymarket, weather, quant, wellington]
---

# Wellington — Quant Deep Dive Note

Ville : **Wellington** (wellington) — 684 marchés, 312,315 trades, $2.46M volume.

## Findings clés

- **Hurst H=1.094** (trending) — mémoire longue, persistance des drifts négatifs (NO edge)
- **AUC XGBoost=0.872** — signal prédictif ex-ante exploitable
- **OFI=0.758** — pression acheteuse structurelle (forte)
- **YES win rate réel=11.1%** vs prix moyen ouverture=0.131 → sur-estimation systématique
- **Best edge : buy no uncertain** — EV/bet=+40.9%

## Stratégie recommandée

1. **Buy NO brackets** : EV=+9.1%, WR=0.896, seuil entrée YES<0.85
2. **Buy NO uncertain** : EV=+40.9%, seuil [0.45-0.55] avec OFI<0.6
3. **Éviter** : YES longshots (<10%) — Sharpe=-0.174

## Related

- [[_MOC]]
- [[odds-trajectories-v2-findings]]
- [[per-city-deep-dive/wellington|Deep Dive Baseline Wellington]]
- [[tier-s-v2-hedge-fund-gates]]
- [[capacity-reality-check]]
