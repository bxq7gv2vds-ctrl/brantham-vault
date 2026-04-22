---
type: quant-deep-dive
city: Buenos Aires
slug: buenos-aires
date: 2026-04-22
n_markets: 1013
n_trades: 353565
volume_usdc: 1898954
yes_win_rate: 0.1218
hurst: 0.7933
xgb_auc: 0.8429
best_strategy: buy_no_favorites
best_ev_pct: 1051.24
ofi: 0.6433
tags: [polymarket, weather, quant, buenos-aires]
---

# Buenos Aires — Quant Deep Dive Note

Ville : **Buenos Aires** (buenos-aires) — 1,013 marchés, 353,565 trades, $1.90M volume.

## Findings clés

- **Hurst H=0.793** (trending) — mémoire longue, persistance des drifts négatifs (NO edge)
- **AUC XGBoost=0.843** — signal prédictif ex-ante exploitable
- **OFI=0.643** — pression acheteuse structurelle (forte)
- **YES win rate réel=12.2%** vs prix moyen ouverture=0.143 → sur-estimation systématique
- **Best edge : buy no favorites** — EV/bet=+1051.2%

## Stratégie recommandée

1. **Buy NO brackets** : EV=+19.2%, WR=0.901, seuil entrée YES<0.85
2. **Buy NO uncertain** : EV=+29.8%, seuil [0.45-0.55] avec OFI<0.6
3. **Éviter** : YES longshots (<10%) — Sharpe=0.056

## Related

- [[_MOC]]
- [[odds-trajectories-v2-findings]]
- [[per-city-deep-dive/buenos-aires|Deep Dive Baseline Buenos Aires]]
- [[tier-s-v2-hedge-fund-gates]]
- [[capacity-reality-check]]
