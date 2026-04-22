---
type: quant-deep-dive
city: Seattle
slug: seattle
date: 2026-04-22
n_markets: 1011
n_trades: 407959
volume_usdc: 2106883
yes_win_rate: 0.0886
hurst: 0.7971
xgb_auc: 0.8372
best_strategy: buy_no_favorites
best_ev_pct: 1185.71
ofi: 0.5601
tags: [polymarket, weather, quant, seattle]
---

# Seattle — Quant Deep Dive Note

Ville : **Seattle** (seattle) — 1,011 marchés, 407,959 trades, $2.11M volume.

## Findings clés

- **Hurst H=0.797** (trending) — mémoire longue, persistance des drifts négatifs (NO edge)
- **AUC XGBoost=0.837** — signal prédictif ex-ante exploitable
- **OFI=0.560** — pression acheteuse structurelle (modérée)
- **YES win rate réel=8.9%** vs prix moyen ouverture=0.148 → sur-estimation systématique
- **Best edge : buy no favorites** — EV/bet=+1185.7%

## Stratégie recommandée

1. **Buy NO brackets** : EV=+8.0%, WR=0.904, seuil entrée YES<0.85
2. **Buy NO uncertain** : EV=+36.1%, seuil [0.45-0.55] avec OFI<0.6
3. **Éviter** : YES longshots (<10%) — Sharpe=-0.063

## Related

- [[_MOC]]
- [[odds-trajectories-v2-findings]]
- [[per-city-deep-dive/seattle|Deep Dive Baseline Seattle]]
- [[tier-s-v2-hedge-fund-gates]]
- [[capacity-reality-check]]
