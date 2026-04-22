---
title: Sao Paulo — Quant Deep Dive
city: Sao Paulo
slug: sao-paulo
generated: 2026-04-22
n_markets: 521
n_trades: 229049
volume_usdc: 1067581
yes_win_rate: 0.1017
xgb_auc: 0.779
kyle_lambda_median: 0.000289
hhi_makers: 0.01734
best_strategy: buy_no_uncertain
sharpe_no_uncertain: 0.711
ev_no_uncertain_pct: 52.0
half_life_days: 1.115
calibrated: false
tags: [polymarket, weather, sao-paulo, quant, microstructure, mis-calibrated]
---

# Sao Paulo — Quant Deep Dive

## Résumé Exécutif

Sao Paulo est le marché le **moins liquide** ($1.07M volume) et le **moins prédictible** (AUC=0.779). Pourtant, il offre le **meilleur Sharpe sur buy_no_uncertain parmi les 5 villes** (0.711, EV +52 %). Mis-calibré surtout dans le bin [0.3–0.4] (chi²_contrib=10.0 — record). Half-life = 1.115 jours (correction lente). Le maker `0x7bff96` est cross-city (Miami/Paris/Sao Paulo) — potentiel oracle institutionnel.

## Chiffres Clés

| Métrique | Valeur |
|---|---|
| YES win rate | 10.17 % |
| XGBoost AUC | **0.779** ± 0.086 (plus bas des 5) |
| Half-life mean-reversion | **1.115 jours** (le plus lent) |
| Kyle lambda médiane | **0.000289** (le plus bas des 5) |
| HHI makers | 0.01734 |
| IAT médiane | 44 secondes |
| Spread proxy | **154 bps** (élevé) |
| EV buy_no_uncertain | **+52.0 %** (N=22) |
| Sharpe buy_no_uncertain | **0.711** (meilleur des 5) |
| Bin [0.3–0.4] biais | −24.5 pp (chi² record) |
| Skewness drifts | +1.588 (le plus élevé) |

## Findings Principaux

1. **AUC le plus bas** (0.779) — climatologie tropicale peu variable = moins prédictible
2. **Bin [0.3–0.4] WR=10.5 % vs attendu 35 %** — edge pur massif, chi²=10.0
3. **Sharpe NO uncertain 0.711** — best Sharpe des 5 villes malgré N=22 faible
4. **Half-life 1.115j** — signal de correction lent, fenêtre d'entrée plus large
5. **Maker `0x7bff96`** cross-city : $91K SP, $186K Miami, $112K Paris → tracker comme oracle
6. **Silhouette 0.388** (le plus bas) — régimes moins nets, classification ex-ante plus difficile

## Edge Opérationnel

- **NO uncertain** : prix YES ∈ [0.30, 0.60] → priorité bin [0.3–0.4] (EV massif)
- **Sizing** : $15–$30 max (volume $2K/marché moyen)
- **NO brackets** : threshold ∈ {26, 27, 28}°C, prix ≤ 0.12 → EV +10.3 %
- **Signal maker** : si `0x7bff96` achète YES massivement → événement météo extrême
- **Timing** : 19h–22h UTC (16h–19h heure locale Brasília)

## Visualisations

- `viz_sao-paulo/surface_ev.html`
- `viz_sao-paulo/scatter_regimes.html`
- `viz_sao-paulo/density_volume.html`

## Related

- [[_MOC]]
- [[../odds-trajectories-v2-findings]]
- [[../per-city-deep-dive/sao-paulo|baseline Sao Paulo]]
- [[../tier-s-v2-hedge-fund-gates]]
- [[quant-deep-dive/paris|Paris QDD]]
- [[quant-deep-dive/tel-aviv|Tel Aviv QDD]]
