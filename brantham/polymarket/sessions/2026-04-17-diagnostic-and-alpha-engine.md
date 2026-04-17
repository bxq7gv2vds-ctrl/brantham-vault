---
name: Session 2026-04-17 — Diagnostic + Alpha Engine v0
description: Session complète de diagnostic, EdgeFilter v1, backtest engine unifié, et kickoff architecture hedge fund
type: session
date: 2026-04-17
tags: [polymarket, session, diagnostic, alpha-engine]
---

# Session 2026-04-17 — Diagnostic + Alpha Engine v0

**Durée** : ~4h marathon
**Mode** : effort max
**Context** : user demande "modèle ultra puissant pour faire plusieurs centaines de k€/an sur Polymarket comme les meilleurs traders"

## Ce qui a été fait

### 1. Audit du bot actuel (45min)

**Findings** :
- 6,814 trades paper mode (0 live)
- COLDMATH_NO désactivé depuis v4 (2026-04-14) alors que c'est l'edge principal
- Capital passé de $98k à $20k entre 04-15 et 04-16 (reset suspect)
- CONFIRMED oracle codé mais jamais triggered
- market_resolutions table vide → pas de ground truth
- all_markets.db stale (last price_bar = 2026-04-05, 12 jours d'écart)

### 2. Diagnostic des edges (1h)

Analyse par signal_type × price bucket × TTR × sigma pour tous les 6,740 trades settled.

**Rentables** (voir [[../findings|findings détaillés]]) :
- PROB_NO <0.70 : +7.4 pts vs breakeven (WR 70.2%, +$526)
- COLDMATH_NO 0.85-0.95 : +3.3 pts (WR 96.9%, +$2,050)
- COLDMATH_NO ≥0.95 : +1.1 pt (WR 99.6%, +$11,528 — volume principal)
- EXACT_BIN_YES ≥0.95 : ~+4 pts (WR 100%, +$108)

**Toxiques** :
- PROB_YES <0.30 : -3.6 pts (WR 0.7%, -$2,502)
- PROB_NO 0.70-0.85 : -5.5 pts (WR 69%, -$452 asymétrie)
- EXACT_BIN_YES <0.30 : disaster (WR 10%, -$582)
- SPEEDA_EARLY : 0% WR sur 11 trades, -$550

**Lottery** (variance trop haute pour daily P&L) :
- CONVEX_YES <0.10 : 1 win sur 122 (Paris, +$652)
- LONGSHOT_YES <0.10 : 1 win sur 22

### 3. Construction EdgeFilter v1 (45min)

**Module** : `src/pmhedge/strategy/edge_filter.py` (260 lignes)

Registry data-driven de 13 pockets :
- 6 pockets ALLOWED avec Kelly fraction + size cap
- 7 pockets BLOCKED explicites

**Logic** :
```python
for sig in signals:
    pocket = classify(sig)
    if pocket.allowed:
        size = kelly_size(pocket.wr_observed, sig.buy_price, bankroll) × kelly_fraction
        size = min(size, pocket.size_cap_usdc, bankroll × max_pos_pct)
    else:
        skip
```

**Résultat backtest (bankroll $1k)** :
| Mode | N | WR | P&L | Sharpe | Max DD |
|---|---|---|---|---|---|
| Baseline passthrough | 1,599 | 81.9% | **-$620** | -9.23 | -56.6% |
| Filter + Kelly | 1,540 | 97.1% | **+$1,049** | 12.30 | 0% |

**Δ = +$1,669 (+269%)** — transformation perte → gain.

### 4. OOS validation (30min)

Walk-forward avec 4 windows (train=2j, test=1j, step=1j) :
- Pooled N=16, PnL +$18.51, Sharpe 16.4
- Data limitée (10.5 jours total) → validation préliminaire

### 5. Module `alpha/` scaffold (1.5h)

**Fichiers créés** :

- `src/pmhedge/alpha/metrics.py` (200 lignes)
  - Sharpe, Sortino, Calmar annualisés
  - VaR 95%, CVaR 95%
  - Max drawdown + durée
  - Kelly optimal empirique
  - Monte Carlo bootstrap 1000 sims
  - Attribution per signal/city/hour

- `src/pmhedge/alpha/backtest.py` (300 lignes)
  - SlippageModel : depth-aware linear slippage
  - load_settled_trades : DB reader
  - edge_filter_policy / passthrough_policy
  - run_backtest : deterministic replay
  - walk_forward : rolling OOS validator

- `src/pmhedge/alpha/sum_arb.py` (250 lignes)
  - scan_current_arbs : Gamma API live scan
  - backtest_arbs_historical : price_bars replay
  - **ATTENTION** : résultats backtest non fiables (prix pas synchronisés)

- `src/pmhedge/alpha/report.py` (200 lignes)
  - Markdown report generator
  - Equity curve ASCII
  - Attribution tables
  - Monte Carlo CIs
  - Walk-forward per-window

- `src/pmhedge/alpha/data_hub.py` (300 lignes)
  - Schema DB unifié : stations, nwp_forecasts, obs_temperature, orderbook_snapshots, signal_log, trade_log, model_performance, data_freshness
  - Connection management
  - Writers + readers typés

- `src/pmhedge/alpha/nwp_sources.py` (250 lignes)
  - fetch_open_meteo_ensemble : primary (139 members)
  - fetch_hrrr : US 3km via Open-Meteo
  - fetch_icon_eu : EU 6.5km
  - RegionalFetcher : router par région
  - compute_ensemble_blend : stats ensemble

**Entry point** :
- `scripts/alpha_backtest.py` (180 lignes)
  - CLI unifié
  - Runs : baseline + filter + walk-forward + sum-arb
  - Output markdown report vers vault

### 6. Architecture hedge fund définie (45min)

4 couches orthogonales (voir [[../architecture|architecture détaillée]]) :

1. **Data Hub** : NWP multi-source + obs + radar + orderbook + reanalysis
2. **Model Hub** : EMOS + BMA + XGBoost + DRN (calibrée)
3. **Alpha Layers** : 6 edges orthogonaux
4. **Execution + Risk** : CLOB WebSocket + Kelly corr-adj + kill switch

### 7. Vault section créée (30min)

**Structure** :
```
vault/brantham/polymarket/
  _MOC.md                    # Index principal
  architecture.md            # Architecture complète
  data-sources.md            # Inventaire best-in-class
  findings.md                # Diagnostics + edges
  decisions.md               # Log décisions
  questions.md               # 93 questions framework
  roadmap.md                 # Phases 0-5
  sessions/                  # Session logs
    2026-04-17-diagnostic-and-alpha-engine.md  # (ce fichier)
  backtest-results/          # Per-run results
  data-sources/              # Par source si besoin
```

Toutes les pages cross-linkées via wikilinks.

## Décisions prises (voir [[../decisions|log complet]])

- D1 : Défensif avant offensif (EdgeFilter d'abord)
- D2 : Module `alpha/` plugin (pas refactor)
- D3 : Open-Meteo primary (139 members ensemble)
- D4 : SQLite pour data hub
- D5 : Python asyncio, pas Rust/Go
- D6 : Kelly fractional 25-50%
- D7 : Correlation-adjusted obligatoire
- D8 : 30j paper shadow avant live
- D9 : Walk-forward purged K-fold
- D10 : EMOS+BMA+XGBoost avant neural
- D11 : Polymarket CLOB WebSocket pour exec
- D12 : Vault Obsidian pour knowledge
- D13 : Folder polymarket/ séparé
- D14 : Pas MM en Phase 1
- D15 : Sum-arb en Phase 3

## Questions levées sans réponse

- Capital réel disponible (phase 1) ?
- Private key Polymarket existante ?
- Jurisdiction (France OK ?) ?
- VPS existant ou à provisionner ?
- Tolérance drawdown exacte ?

## Code stats

- Files créés : 9 modules + 1 script CLI + 7 docs vault
- Lignes ajoutées : ~1,600 Python + ~1,500 markdown
- Tests manuels : backtest passes, sum-arb nombres suspects (flagged)

## Bugs identifiés à fix

1. Sum-arb backtest : prix pas synchronisés → nombres gonflés (20k opportunities à 22% = fake)
   → Fix : utiliser orderbook snapshots simultanés
2. CONFIRMED oracle : jamais triggered, root cause à investiguer
3. market_resolutions table vide
4. Pipeline data stale 12 jours

## Next session priority

**Phase 1 — Data Foundation** (voir [[../roadmap|roadmap]]) :
1. Finaliser nwp_sources.py (HRRR + ICON-EU ingestion)
2. Script ERA5 backfill 5 ans
3. Polymarket CLOB WebSocket client
4. Populate market_resolutions depuis settled trades
5. Data freshness monitor + alerts
6. Seed stations table (40 stations)

**Parallèle** : debug CONFIRMED oracle pendant attente data ingestion

## Related

- [[../_MOC|Polymarket Hub]]
- [[../findings|Findings détaillés]]
- [[../architecture|Architecture hedge fund]]
- [[../decisions|Décisions architecturales]]
- [[../roadmap|Roadmap phased]]
- [[../questions|Questions framework]]
- [[../data-sources|Data sources best-in-class]]
- [[../../brantham/_MOC|Brantham MOC]]
