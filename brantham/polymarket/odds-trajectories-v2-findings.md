---
name: Odds Trajectories v2 — Backtest 6 mois on-chain
description: Analyse exhaustive des trajectoires de prix Polymarket reconstruites depuis 17601 markets weather sur 38 villes (6 mois on-chain via Goldsky subgraph). Identifie tiers d'efficience des bookies par ville et opportunités d'edge actionnables.
type: analysis
project: brantham/polymarket
created: 2026-04-22
updated: 2026-04-22
tags: [polymarket, odds, trajectories, backtest, market-efficiency, on-chain, hedge-fund-grade]
priority: high
---

# Odds Trajectories v2 — Backtest on-chain 2026-04-22

## TL;DR

- **17601 markets weather** analysés sur **38 villes**
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
| London | 1475 | SEMI_EFFICIENT | 0.052 | 0.09 | 0.17 | 0.033 | $8.66M |
| New York | 1486 | SEMI_EFFICIENT | 0.050 | 0.08 | 0.16 | 0.037 | $7.43M |
| Seoul | 1013 | SEMI_EFFICIENT | 0.074 | 0.11 | 0.16 | 0.046 | $5.92M |
| Dallas | 1027 | EFFICIENT | 0.042 | 0.06 | 0.15 | 0.031 | $2.76M |
| Atlanta | 1020 | EFFICIENT | 0.044 | 0.07 | 0.15 | 0.030 | $2.47M |
| Wellington | 684 | SEMI_EFFICIENT | 0.053 | 0.07 | 0.17 | 0.034 | $2.46M |
| Shanghai | 280 | SEMI_EFFICIENT | 0.055 | 0.07 | 0.20 | 0.033 | $2.28M |
| Miami | 698 | EFFICIENT | 0.045 | 0.06 | 0.16 | 0.030 | $2.22M |
| Tel Aviv | 307 | EFFICIENT | 0.047 | 0.06 | 0.15 | 0.026 | $2.21M |
| Chicago | 698 | SEMI_EFFICIENT | 0.063 | 0.09 | 0.18 | 0.039 | $2.12M |
| Seattle | 1012 | EFFICIENT | 0.040 | 0.05 | 0.15 | 0.032 | $2.11M |
| Toronto | 1024 | SEMI_EFFICIENT | 0.056 | 0.08 | 0.16 | 0.039 | $2.00M |
| Buenos Aires | 1013 | SEMI_EFFICIENT | 0.052 | 0.08 | 0.15 | 0.035 | $1.90M |
| Paris | 521 | EFFICIENT | 0.048 | 0.07 | 0.18 | 0.031 | $1.88M |
| Tokyo | 307 | EFFICIENT | 0.045 | 0.05 | 0.20 | 0.025 | $1.43M |

## Findings clés

### 1. Bookies très inefficients (edge structurel exploitable)

- _Aucune ville classée VERY_INEFFICIENT (early_error ≥ 0.30)._

### 2. Bookies efficients (skip ou Tier minimal)

- **Paris** (N=521) : early_error=0.048 → bookies déjà right early. Edge faible.
- **Atlanta** (N=1020) : early_error=0.044 → bookies déjà right early. Edge faible.
- **Miami** (N=698) : early_error=0.045 → bookies déjà right early. Edge faible.
- **Dallas** (N=1027) : early_error=0.042 → bookies déjà right early. Edge faible.
- **Tel Aviv** (N=307) : early_error=0.047 → bookies déjà right early. Edge faible.

### 3. Markets très volatiles (timing entry critique)

- **Taipei** vol=0.054 → prix bouge significativement pendant la vie du market. Re-scanner agressivement pour pick meilleur prix d'entrée.
- **Seoul** vol=0.046 → prix bouge significativement pendant la vie du market. Re-scanner agressivement pour pick meilleur prix d'entrée.
- **Wuhan** vol=0.044 → prix bouge significativement pendant la vie du market. Re-scanner agressivement pour pick meilleur prix d'entrée.
- **Los Angeles** vol=0.041 → prix bouge significativement pendant la vie du market. Re-scanner agressivement pour pick meilleur prix d'entrée.
- **Toronto** vol=0.039 → prix bouge significativement pendant la vie du market. Re-scanner agressivement pour pick meilleur prix d'entrée.

### 4. Markets mean-reverting (favoriser fade strategies)

- **Busan** Hurst=0.14 (<0.5 = mean-reverting). Stratégie CONVEX_YES (fade extreme moves) a un edge théorique.
- **Seattle** Hurst=0.15 (<0.5 = mean-reverting). Stratégie CONVEX_YES (fade extreme moves) a un edge théorique.
- **Dallas** Hurst=0.15 (<0.5 = mean-reverting). Stratégie CONVEX_YES (fade extreme moves) a un edge théorique.
- **Mexico City** Hurst=0.15 (<0.5 = mean-reverting). Stratégie CONVEX_YES (fade extreme moves) a un edge théorique.
- **Tel Aviv** Hurst=0.15 (<0.5 = mean-reverting). Stratégie CONVEX_YES (fade extreme moves) a un edge théorique.

## Recommandations actionnables

### Cities à BOOST (ENABLED, Kelly 0.50)

- _Aucune city en boost — data insuffisante ou markets globalement efficients._

### Cities à DOWNGRADE (SHADOW ou Kelly 0.20)

- **Paris** — early_error=0.048 (bookies right early); N=521
  - Action : `city_config[Paris] : status → SHADOW or Kelly fraction → 0.20`
- **Atlanta** — early_error=0.044 (bookies right early); N=1020
  - Action : `city_config[Atlanta] : status → SHADOW or Kelly fraction → 0.20`
- **Miami** — early_error=0.045 (bookies right early); N=698
  - Action : `city_config[Miami] : status → SHADOW or Kelly fraction → 0.20`
- **Dallas** — early_error=0.042 (bookies right early); N=1027
  - Action : `city_config[Dallas] : status → SHADOW or Kelly fraction → 0.20`
- **Tel Aviv** — early_error=0.047 (bookies right early); N=307
  - Action : `city_config[Tel Aviv] : status → SHADOW or Kelly fraction → 0.20`
- **Shenzhen** — early_error=0.049 (bookies right early); N=209
  - Action : `city_config[Shenzhen] : status → SHADOW or Kelly fraction → 0.20`
- **Tokyo** — early_error=0.045 (bookies right early); N=307
  - Action : `city_config[Tokyo] : status → SHADOW or Kelly fraction → 0.20`
- **Seattle** — early_error=0.040 (bookies right early); N=1012
  - Action : `city_config[Seattle] : status → SHADOW or Kelly fraction → 0.20`

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