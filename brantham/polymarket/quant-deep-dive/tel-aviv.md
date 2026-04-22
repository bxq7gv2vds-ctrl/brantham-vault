---
title: Tel Aviv — Quant Deep Dive
city: Tel Aviv
slug: tel-aviv
generated: 2026-04-22
n_markets: 307
n_trades: 113903
volume_usdc: 2210645
volume_total_all_markets: 17306984
volume_per_market: 7200
trade_size_mean: 19.41
yes_win_rate: 0.0945
xgb_auc: 0.776
kyle_lambda_median: 0.001381
hhi_makers: 0.124049
best_strategy: buy_no_uncertain
sharpe_no_uncertain: 0.852
ev_no_uncertain_pct: 59.3
whale_vol_pct: 87.5
calibrated: true
serie_too_short: true
tags: [polymarket, weather, tel-aviv, quant, microstructure, calibrated, concentration-risk, oligopoly]
---

# Tel Aviv — Quant Deep Dive

## Résumé Exécutif

Tel Aviv est le marché avec la **concentration de market makers la plus élevée** (HHI=0.124 — 18× Shanghai, zone oligopolistique) et le **trade size moyen le plus élevé** ($19.41). Les 3 premiers makers contrôlent **55.6 % du volume** on-chain. Les whales (>$100) représentent **87.5 % du volume** — distribution Pareto la plus extrême du corpus. Bien calibré (p=0.339). XGBoost AUC=0.776. Seul marché où `is_bracket` a une importance **nulle** dans le modèle.

## Chiffres Clés

| Métrique | Valeur |
|---|---|
| Durée historique | **29 jours** |
| Volume total (tous marchés) | **$17.3M** |
| Volume moyen par marché | **$7 200** |
| Trade size moyen | **$19.41** (record des 5) |
| YES win rate | **9.45 %** |
| XGBoost AUC | 0.776 ± 0.081 |
| price_open importance | **51.3 %** (le plus élevé) |
| is_bracket importance | **0.0 %** (UNIQUE) |
| Kyle lambda médiane | **0.001381** (record élevé — 4.3× Shanghai) |
| HHI makers | **0.124049** (oligopole) |
| Top-3 makers contrôlent | **55.6 % du volume** |
| Whales > $100 vol | **87.5 %** (record) |
| IAT médiane | 74 secondes (moins liquide) |
| Spread proxy | **108 bps** |
| EV buy_no_uncertain | +59.3 %, Sharpe 0.852 (N=13) |
| Silhouette régimes | **0.435** (le plus net des 5) |

## Findings Principaux

1. **HHI=0.124** — zone oligopolistique, risque de manipulation systémique
2. **`is_bracket` importance ZÉRO** — structure bracket non informative à Tel Aviv
3. **price_open 51.3 %** — signal initial capture la quasi-totalité de l'information
4. **Régime Quiet WR=0 %** sur 203+218 marchés — buy_NO quasi-certain en régime calme
5. **Silhouette 0.435** (le plus net) — régimes très bien séparés, classification ex-ante fiable
6. **Distribution Pareto extrême** : 66 % trades < $1 (retail) mais 87.5 % volume > $100 (institutionnel)

## Risque de Manipulation — ALERTE

- Top maker `0xf91515` : $564 723, 25.5 % du volume (98 trades)
- Top maker `0x2785e7` : $436 397, 19.7 % du volume (43 trades)
- Si convergence des top-2 makers sur le même côté → signal possible de price coordination
- Kyle lambda le plus élevé (0.00138) → chaque $1K de trade déplace ~13.8 bps

## Edge Opérationnel

- **NO uncertain** : prix YES ∈ [0.45, 0.60] → EV +59.3 %, Sharpe 0.852 (N=13)
- **NO quiet** : vol_pp < 0.015 → acheter NO (WR=0 % sur 203+ marchés)
- **Sizing max** : $10–$15 par trade (Kyle lambda élevé = impact coût)
- **Timing** : 08h–09h UTC (10h–11h IST, peak liquidité)
- **Anti-manipulation** : ne jamais trader si un maker > 20 % du volume d'un marché individuel

## Visualisations

- `viz_tel-aviv/surface_ev.html`
- `viz_tel-aviv/scatter_regimes.html`
- `viz_tel-aviv/density_volume.html`

## Related

- [[_MOC]]
- [[../odds-trajectories-v2-findings]]
- [[../per-city-deep-dive/tel-aviv|baseline Tel Aviv]]
- [[../tier-s-v2-hedge-fund-gates]]
- [[quant-deep-dive/shanghai|Shanghai QDD]]
- [[quant-deep-dive/sao-paulo|Sao Paulo QDD]]
