---
name: Polymarket — TODO pending (2026-04-21)
description: Punch list actualisée après research pipeline + cleanup. Actions ordonnées par priorité (P0 = immédiat, P4 = structural).
type: todo
project: brantham/polymarket
created: 2026-04-18
updated: 2026-04-21
tags: [polymarket, todo, roadmap]
priority: critical
---

# Polymarket — TODO pending

## P0 — Immédiat (en cours / bloquant)

- [ ] **Pangu ONNX re-download** — premier fichier corrompu, retry curl --retry 10 en background (~10-15 min)
- [ ] **Vérifier Pangu ONNX load** post-download : `uv run scripts/setup_pangu.py --verify`
- [ ] **Debug London/Toronto/Sao Paulo 0 signaux** : tracer pourquoi ces villes (ENABLED maintenant, markets actifs) ne génèrent pas de signaux dans signal_log. Tester scan manuel avec logging verbose.

## P1 — User action required (bloquant modèle amélioré)

- [ ] **Compte Copernicus CDS** : register free + accepter licences ERA5
  - URL : https://cds.climate.copernicus.eu/user/register
  - Licences : reanalysis-era5-pressure-levels + reanalysis-era5-single-levels
- [ ] **Créer `~/.cdsapirc`** avec clé API après register
- [ ] **Validate economic-thesis** : review [[economic-thesis]] et ajouter sentinel `THESIS VALIDATED BY PAUL ON YYYY-MM-DD` pour débloquer G1 exit

## P2 — Quick wins (< 1h)

- [ ] **Force-fit calibrators** pour Seoul, Tel Aviv, Seattle, Sao Paulo, London, Toronto, Shanghai, Buenos Aires, Shenzhen (villes ENABLED sans calibrator)
  - Script : `scripts/train_city_calibrators.py --city=<slug>`
- [ ] **Run Pangu cycle** après Copernicus setup : `uv run scripts/run_pangu_cycle.py --steps 3`
- [ ] **Re-run city_deep_dive** pour les 10 villes nouvellement activées (après 7j de data accumulation)

## P3 — Research pipeline à compléter (pôle stats)

- [x] **01_city_discovery.py** — 38 villes, $288M volume (DONE)
- [x] **02_city_trajectories.py** — ACF, runs, regimes, mean reversion (DONE, 46 villes)
- [ ] **03_city_forecast_skill.py** — skill scores 12 NWP sources per-city (CRPS, MAE, bias)
- [ ] **04_city_market_microstructure.py** — spreads moyens, bracket density, bid-ask, depth
- [ ] **05_city_outcome_distributions.py** — actual vs predicted distributions per-city
- [ ] **06_sigma_empirical.py** — σ empirique vs σ prédit par NWP (detect bias Tokyo-like)
- [ ] **07_bracket_sweep.py** — quels brackets tradés (lower/mid/upper tail preferences market)

## P3b — Research pipeline (pôle analysis)

- [x] **01_priority_actions.py** — 14 actions P0/P1/P2 (DONE)
- [ ] **02_cross_city_correlation.py** — regime clustering (villes qui bougent ensemble)
- [ ] **03_hedge_detection.py** — (city_A, city_B) avec correlation négative → hedge pairs
- [ ] **04_model_recommendations.py** — per-city hyperparam tuning auto (σ shrinkage, Kelly override)
- [ ] **05_momentum_patterns.py** — identifier villes avec persistance tradable (ex: Shanghai ACF 0.92)

## P4 — Infrastructure (structural)

- [ ] **Wire ECMWF OpenData** dans `nwp_sources.py` — ajouter comme 13e source NWP (HRES + ENS gratuit)
- [ ] **Wire Pangu dans BMA** : après run_pangu_cycle valide, ajouter 'PANGU' aux ensemble_weights
- [ ] **Tests unitaires** : `bucket_router.py`, `ttr_filter.py`, `live_executor.py`, `city_optimizer.py`
- [ ] **Fusion `pmhedge.db` → `alpha_data_hub.db`** — migrer les 2 systèmes coexistants
- [ ] **Archive DBs legacy** : `bracket_scalper_trades.db`, `coldmath_trades.db`, `mega_dataset.db`, `oracle_data.db` dans `backups/legacy-dbs/`
- [ ] **Audit 150 scripts** : probablement 30-40% legacy à archiver

## P5 — Pro-level features (budget ou stratégique)

- [ ] **Mesonet Synoptic free tier** (5k req/day) — token free, wire dans `mesonet_client.py`
- [ ] **LLM features Claude API** — wire dans `llm_features.py`, `ANTHROPIC_API_KEY` déjà en env
- [ ] **Market-making rebate** — branch `market_maker.py` quand py-clob-client wired
- [ ] **Live trading wire** — `POLY_PRIVATE_KEY` + py-clob-client dans `order_manager.py`
- [ ] **Kalshi cross-venue** — `kalshi_client.py` dormant, activate pour capacity scaling

## P6 — Out of scope sauf budget (optionnel)

- [ ] ECMWF HRES payant $50k/an — **pas nécessaire** vu OpenData gratuit
- [ ] Mesonet paid $500/mo — historique 10 ans pour training
- [ ] Équipe quants (4-8 pers) — capacity scaling
- [ ] Colocation NY5/LD5 — latency edge
- [ ] Pangu per-city fine-tune (quand N_obs >= 150 par ville)

## Tracking

| Task ID | Subject | Status |
|---------|---------|--------|
| 11 | Re-download Pangu ONNX | in_progress |
| 12 | Debug London 0 signaux | pending |
| 13 | Pôle stats 02-05 | in_progress (01, 02 done; 03-07 pending) |
| 14 | Pôle analysis 02-04 | pending |

## Related

- [[ARCHITECTURE]]
- [[MODEL-STATE-COMPLETE]]
- [[STATE-HANDOFF]]
- [[city-optimization]]
- [[_MOC]]
