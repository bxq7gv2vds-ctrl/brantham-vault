---
name: Odds Trajectories v2 — Backtest 6 mois on-chain
description: Analyse exhaustive des trajectoires de prix Polymarket reconstruites depuis 1117 markets weather sur 38 villes (6 mois on-chain via Goldsky subgraph). Identifie tiers d'efficience des bookies par ville et opportunités d'edge actionnables.
type: analysis
project: brantham/polymarket
created: 2026-04-22
updated: 2026-04-22
tags: [polymarket, odds, trajectories, backtest, market-efficiency, on-chain, hedge-fund-grade]
priority: high
---

# Odds Trajectories v2 — Backtest on-chain 2026-04-22

## TL;DR

- **1117 markets weather** analysés sur **38 villes**
- Source : trades on-chain Polymarket (Goldsky subgraph), 6 mois history
- Pipeline : `research/pole_stats/09_odds_trajectories_v2.py` + `10_trajectories_3d_viz.py` + `pole_analysis/07_odds_trajectories_findings.py`
- Visualisations 3D interactives : `research/outputs/10_trajectories_3d/`

## Méthode

1. **Fetch on-chain** (`scripts/fetch_trades_subgraph.py`) — tous les OrderFilledEvents Polymarket pour les ~18k tokens weather sur 6 mois
2. **Reconstruction price** : `price_per_token = makerAmountFilled / takerAmountFilled` (USDC→token side) ou inverse
3. **Métriques par market** : drift, volatility, monotonicity, Hurst, half-life mean-reversion, autocorrelation, max drawdown, n up/down runs
4. **Outcome inference** : moyenne 5 derniers trades (si ≥0.93 → YES, ≤0.07 → NO, sinon ambigu)
5. **Métriques d'efficience indépendantes du biais drift↔outcome** : 
   - `early_error` = |moyenne prix premiers 25% − outcome|
   - `mid_error` = |moyenne prix milieu − outcome|
   - `open_error` = |prix premier trade − outcome|

## Tiers d'efficience par ville (top 15 par volume)

| Ville | N | tier | early_err | edge_score | hurst | vol | volume |
|-------|--:|------|----------:|-----------:|------:|----:|-------:|
| London | 33 | SEMI_EFFICIENT | 0.058 | 0.04 | 0.21 | 0.032 | $352k |
| Shanghai | 33 | SEMI_EFFICIENT | 0.074 | 0.06 | 0.18 | 0.033 | $314k |
| Seoul | 33 | SEMI_EFFICIENT | 0.082 | 0.06 | 0.19 | 0.030 | $254k |
| Paris | 33 | SEMI_EFFICIENT | 0.058 | 0.05 | 0.19 | 0.037 | $190k |
| New York | 33 | SEMI_EFFICIENT | 0.059 | 0.04 | 0.19 | 0.028 | $124k |
| Hong Kong | 33 | EFFICIENT | 0.044 | 0.03 | 0.16 | 0.026 | $122k |
| Wellington | 33 | EFFICIENT | 0.035 | 0.03 | 0.16 | 0.019 | $120k |
| Tokyo | 33 | EFFICIENT | 0.043 | 0.03 | 0.18 | 0.021 | $117k |
| Miami | 33 | EFFICIENT | 0.021 | 0.02 | 0.18 | 0.021 | $93k |
| Toronto | 33 | SEMI_EFFICIENT | 0.081 | 0.06 | 0.19 | 0.038 | $78k |
| Madrid | 33 | EFFICIENT | 0.015 | 0.01 | 0.22 | 0.009 | $75k |
| Atlanta | 33 | EFFICIENT | 0.047 | 0.03 | 0.14 | 0.026 | $75k |
| Seattle | 33 | EFFICIENT | 0.028 | 0.02 | 0.22 | 0.020 | $73k |
| Singapore | 33 | EFFICIENT | 0.026 | 0.02 | 0.19 | 0.013 | $72k |
| Chicago | 33 | EFFICIENT | 0.024 | 0.01 | 0.15 | 0.013 | $71k |

## Findings clés

### 1. Bookies très inefficients (edge structurel exploitable)

- _Aucune ville classée VERY_INEFFICIENT (early_error ≥ 0.30)._

### 2. Bookies efficients (skip ou Tier minimal)

- **Sao Paulo** (N=33) : early_error=0.047 → bookies déjà right early. Edge faible.
- **Warsaw** (N=33) : early_error=0.049 → bookies déjà right early. Edge faible.
- **Munich** (N=33) : early_error=0.049 → bookies déjà right early. Edge faible.
- **Milan** (N=33) : early_error=0.047 → bookies déjà right early. Edge faible.
- **Tel Aviv** (N=33) : early_error=0.050 → bookies déjà right early. Edge faible.

### 3. Markets très volatiles (timing entry critique)

- **Wuhan** vol=0.045 → prix bouge significativement pendant la vie du market. Re-scanner agressivement pour pick meilleur prix d'entrée.
- **Istanbul** vol=0.045 → prix bouge significativement pendant la vie du market. Re-scanner agressivement pour pick meilleur prix d'entrée.
- **San Francisco** vol=0.043 → prix bouge significativement pendant la vie du market. Re-scanner agressivement pour pick meilleur prix d'entrée.
- **Milan** vol=0.042 → prix bouge significativement pendant la vie du market. Re-scanner agressivement pour pick meilleur prix d'entrée.
- **Los Angeles** vol=0.041 → prix bouge significativement pendant la vie du market. Re-scanner agressivement pour pick meilleur prix d'entrée.

### 4. Markets mean-reverting (favoriser fade strategies)

- **Austin** Hurst=0.12 (<0.5 = mean-reverting). Stratégie CONVEX_YES (fade extreme moves) a un edge théorique.
- **Dallas** Hurst=0.13 (<0.5 = mean-reverting). Stratégie CONVEX_YES (fade extreme moves) a un edge théorique.
- **Busan** Hurst=0.14 (<0.5 = mean-reverting). Stratégie CONVEX_YES (fade extreme moves) a un edge théorique.
- **Atlanta** Hurst=0.14 (<0.5 = mean-reverting). Stratégie CONVEX_YES (fade extreme moves) a un edge théorique.
- **Lucknow** Hurst=0.14 (<0.5 = mean-reverting). Stratégie CONVEX_YES (fade extreme moves) a un edge théorique.

## Recommandations actionnables

### Cities à BOOST (ENABLED, Kelly 0.50)

- _Aucune city en boost — data insuffisante ou markets globalement efficients._

### Cities à DOWNGRADE (SHADOW ou Kelly 0.20)

- **Sao Paulo** — early_error=0.047 (bookies right early); N=33
  - Action : `city_config[Sao Paulo] : status → SHADOW or Kelly fraction → 0.20`
- **Warsaw** — early_error=0.049 (bookies right early); N=33
  - Action : `city_config[Warsaw] : status → SHADOW or Kelly fraction → 0.20`
- **Munich** — early_error=0.049 (bookies right early); N=33
  - Action : `city_config[Munich] : status → SHADOW or Kelly fraction → 0.20`
- **Milan** — early_error=0.047 (bookies right early); N=33
  - Action : `city_config[Milan] : status → SHADOW or Kelly fraction → 0.20`
- **Tel Aviv** — early_error=0.050 (bookies right early); N=33
  - Action : `city_config[Tel Aviv] : status → SHADOW or Kelly fraction → 0.20`
- **Moscow** — early_error=0.049 (bookies right early); N=22
  - Action : `city_config[Moscow] : status → SHADOW or Kelly fraction → 0.20`
- **Atlanta** — early_error=0.047 (bookies right early); N=33
  - Action : `city_config[Atlanta] : status → SHADOW or Kelly fraction → 0.20`
- **Tokyo** — early_error=0.043 (bookies right early); N=33
  - Action : `city_config[Tokyo] : status → SHADOW or Kelly fraction → 0.20`

## Fichiers & visualisations

- `research/data/trajectories_v2.parquet` — métriques par market
- `research/data/trajectories_findings.json` — findings JSON canonique
- `research/outputs/10_trajectories_3d/surface_city_ttr_price.html` — surface 3D ville×TTR×prix (Plotly interactive)
- `research/outputs/10_trajectories_3d/trajectories_facet_city.html` — trajectoires individuelles colorées par outcome
- `research/outputs/10_trajectories_3d/density_volumes_3d.html` — heatmap 3D densité TTR/prix top 8 villes
- `research/outputs/10_trajectories_3d/pca_clustering.html` — PCA 3D sur métriques + KMeans clusters
- `research/outputs/10_trajectories_3d/ridge_per_city.png` — ridgeline plot trajectoires moyennes top 20
- `research/outputs/10_trajectories_3d/stats_by_city.csv` — stats agrégées par ville

## Prochaines étapes

1. **Wire les recommandations dans `city_config.py`** : appliquer boost/downgrade list
2. **Re-train `bucket_router.py`** avec TTR sweet spots détectés
3. **Backtest A/B** : strategy actuelle vs strategy + recommendations
4. **Re-run mensuel** : la détection d'edge décroît dans le temps; lancer ce pipeline tous les mois sur les 6 mois rolling pour détecter les régimes shifts
5. **Monitoring** : ajouter `early_error` au signal_log et flag les markets où on entre malgré early_error < 0.05 (low edge)

## Related

- [[_MOC|Polymarket Hub MOC]]
- [[odds-trajectories-findings|v1 — basé sur signal_log seul]]
- [[ARCHITECTURE|Architecture map du stack]]
- [[research-findings-2026-04-21|Research findings session 2026-04-21]]
- [[STATE-HANDOFF|State Handoff]]
- [[city-optimization|City optimization log]]
- [[tier-s-v2-hedge-fund-gates|Tier S v2 gates]]
- [[../../patterns/polymarket-coldmath-no-ev-analysis|Pattern COLDMATH NO EV]]
- [[../../patterns/polymarket-convex-yes-complete-breakdown|Pattern CONVEX_YES]]
- [[../../_system/MOC-patterns|MOC patterns]]