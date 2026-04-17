---
name: Deep Learning Roadmap — SOTA Weather Forecasting + Prediction Markets
description: Plan complet pour atteindre le meilleur modèle deep learning météo sur Polymarket — foundation models, neural post-processing, RL execution, LLM reasoning
type: roadmap
created: 2026-04-17
tags: [polymarket, deep-learning, foundation-models, transformer, rl]
---

# Deep Learning Roadmap — Le Meilleur Modèle Météo + Prediction Markets

**Objectif** : Construire LE meilleur modèle deep learning météo accessible pour un individu, appliqué aux prediction markets Polymarket. Target = battre les traders pro + les APIs commerciales sur weather brackets.

## État du SOTA météo (2024-2026)

### Foundation models qui battent ECMWF-IFS

| Modèle | Source | Year | Résolution | Horizon | Beat ECMWF? |
|---|---|---|---|---|---|
| **GraphCast** | DeepMind | 2023 | 0.25° | 10j | ✅ +10-20% |
| **Pangu-Weather** | Huawei | 2023 | 0.25° | 7j | ✅ +15% T2m |
| **FourCastNet** | NVIDIA | 2022 | 0.25° | 5j | ~ parité |
| **AIFS** | ECMWF | 2024 | 0.25° | 10j | ✅ (production ECMWF) |
| **Aurora** | Microsoft | 2024 | 0.25° | 10j | ✅ (1.3B params) |
| **GenCast** | DeepMind | 2024 | 1° | 15j ens | ✅ battu MEPS |
| **NeuralGCM** | Google | 2024 | 1.4° | 30j | ✅ (hybrid physics+ML) |

### Post-processing neural

| Modèle | Year | Input | Gain vs EMOS |
|---|---|---|---|
| **DRN** (Rasp & Lerch) | 2018 | Ensemble stats → MLP | +10-15% CRPS |
| **BernsteinQN** | 2021 | Features → quantile fns | +12% CRPS |
| **D-ATTN** | 2023 | Attention over members | +15% CRPS |
| **CASM** | 2024 | Conditional diffusion | +20% CRPS |

## Architecture cible — 7 couches

```
┌─────────────────────────────────────────────────────────────────┐
│ LAYER 1: FOUNDATION MODELS (gridded forecast)                    │
│   • ECMWF AIFS (via Open-Meteo or direct ONNX)                  │
│   • Pangu-Weather (HuggingFace)                                 │
│   • GraphCast (Google Earth Engine / TF)                        │
│   • Aurora (Microsoft, 1.3B params)                             │
│   + Classical: ECMWF-IFS, GEFS, ICON, HRRR, AROME               │
└────────────────────┬────────────────────────────────────────────┘
                     │ grid → nearest neighbor → station
┌────────────────────▼────────────────────────────────────────────┐
│ LAYER 2: STATION DOWNSCALING                                    │
│   • Bilinear interp + elevation correction                      │
│   • Station bias per (station × month × hour)                   │
│   • Urban heat island correction                                │
└────────────────────┬────────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────────┐
│ LAYER 3: ENSEMBLE BLEND + POST-PROCESSING                       │
│   • EMOS (baseline, Gneiting 2005)                              │
│   • BMA (Bayesian Model Averaging, online weights)              │
│   • DRN (Distributional Regression Network, PyTorch)            │
│   • Transformer (attention on members + obs lags)               │
│   • CASM-style diffusion (conditional on obs)                   │
└────────────────────┬────────────────────────────────────────────┘
                     │ P(T_max) calibré
┌────────────────────▼────────────────────────────────────────────┐
│ LAYER 4: FEATURE STORE + META-LEARNING                          │
│   • Centralized features (obs, NWP, radar, climato)             │
│   • Regime detector (synoptic pattern clustering)               │
│   • Meta-model picks best sub-model per regime                  │
└────────────────────┬────────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────────┐
│ LAYER 5: LLM REASONING (rare events)                            │
│   • Ingest weather news, Twitter, NOAA alerts                   │
│   • Claude API: detect unusual synoptic patterns                │
│   • Boost confidence on heat dome, cold snap, derecho           │
│   • Override model when physical red flags                      │
└────────────────────┬────────────────────────────────────────────┘
                     │ final P(bracket_YES)
┌────────────────────▼────────────────────────────────────────────┐
│ LAYER 6: SIGNAL GENERATOR (existing)                            │
│   • edge = model_prob - market_price                            │
│   • City-specific Kelly profiles                                │
│   • Min edge / max edge / volume filters                        │
└────────────────────┬────────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────────┐
│ LAYER 7: RL EXECUTION (PPO)                                     │
│   • Agent learns sizing + timing + cancel-replace               │
│   • Env: synthetic orderbook + fill simulator                   │
│   • Reward: PnL - variance penalty - holding cost               │
│   • Beats fixed Kelly in volatile regimes                       │
└─────────────────────────────────────────────────────────────────┘
```

## Roadmap phased (3 mois)

### Mois 1 — Foundation + Post-processing (4 semaines)

**S1 — Data + Foundation models**
- [ ] ERA5 backfill 5 ans (Copernicus CDS)
- [ ] AIFS integration via Open-Meteo (`ecmwf_aifs025_single` model)
- [ ] Pangu-Weather HuggingFace inference
- [ ] GraphCast via Google (or self-host ONNX)
- [ ] Extend `data_hub.nwp_sources` avec 4 new sources DL

**S2 — Post-processing neural (PyTorch)**
- [ ] DRN module (~200 lines) — train on ERA5
- [ ] Train on MPS (Mac Metal) ou Hetzner GPU spot
- [ ] Eval : CRPS, reliability diagram, sharpness
- [ ] Compare EMOS baseline → DRN (should beat by 10-15% CRPS)

**S3 — Transformer temporal**
- [ ] Transformer encoder (multi-head attention on sequence)
- [ ] Input : hourly NWP + METAR obs lags + radar + satellite
- [ ] Output : Gaussian (μ, σ) ou quantile
- [ ] Train on ERA5 5 ans + METAR + radar

**S4 — Ensemble blending v2**
- [ ] Meta-model : XGBoost learns best combiner (DRN + Transformer + Classical)
- [ ] Reliability calibration
- [ ] Deployment : replace EMOS+BMA in `model_prob.py`

### Mois 2 — RL + LLM + infra (4 semaines)

**S5 — PPO execution agent**
- [ ] Synthetic orderbook simulator
- [ ] PPO via stable-baselines3
- [ ] Train on paper history + shadow live
- [ ] Replace fixed Kelly in `signal_generator`

**S6 — LLM reasoning layer**
- [ ] Claude API integration (Anthropic SDK)
- [ ] Ingest : weather.gov alerts, r/weather, Twitter OSINT
- [ ] Prompt : "flag unusual patterns in this synoptic setup"
- [ ] Override model confidence on detected anomalies

**S7 — Infra + MLOps**
- [ ] Hetzner GPU spot (A100 ~€200/mo ou free tier) 
- [ ] Docker training pipeline
- [ ] MLflow tracking
- [ ] Model registry + A/B testing

**S8 — Diffusion model (stretch)**
- [ ] GenCast-style score-based diffusion
- [ ] Generates ensemble samples conditional on recent obs
- [ ] Richer than BMA mixture

### Mois 3 — Validation + Scale (4 semaines)

**S9-10 — Paper shadow validation**
- [ ] 30+ jours live paper avec full stack DL
- [ ] Drift monitoring par model version
- [ ] Champion/challenger A/B tests

**S11-12 — Live deployment graduel**
- [ ] $500 live small après 30j paper OK
- [ ] Scale à $5k après 14j live OK
- [ ] Scale à $50k après 60j live OK
- [ ] Mois 6+ : $100k+ si perfs tenables

## Stack technique final

### ML / Deep Learning
- **PyTorch 2.5+** avec MPS (Mac Metal backend pour inference)
- **Stable-Baselines3** pour PPO RL
- **HuggingFace Transformers** pour foundation models
- **ONNX Runtime** pour AIFS/Pangu inference
- **Lightning AI** ou pure PyTorch pour training loop
- **MLflow** experiment tracking
- **Weights & Biases** training viz

### Compute
- **Mac M5** pour inference (Metal GPU, 128GB unified memory)
- **Hetzner GPU spot** pour training gros modèles (~€200/mo ou free)
- **Google Colab Pro** backup (~€10/mo)
- **Modal** ou **RunPod** pour burst compute si besoin

### Data Engineering
- **Feast** feature store (ou custom SQLite)
- **DuckDB** pour queries analytiques rapides
- **Parquet** pour training datasets (compressed)
- **dbt** pour transformations si complexe

### Monitoring
- **Grafana** + **Prometheus** (real-time)
- **Telegram** alerts
- **Slack** webhook backup

## Coût estimé

| Item | Mensuel | Notes |
|---|---|---|
| Hetzner GPU spot | €0-200 | selon utilisation |
| Copernicus CDS | €0 | gratuit |
| Open-Meteo API | €0 | 10k req/j gratuit |
| Claude API | €10-30 | LLM reasoning |
| Hetzner VPS (existant) | €20 | déjà payé |
| MLflow/monitoring | €0 | self-hosted |
| **Total** | **€30-250/mo** | selon phase |

## Target rendements après stack full

### Sans DL (état actuel)
- Paper backtest : $728k/an sur $10k (trop optimiste, overfit 10j)
- Réaliste : $75-150k/an (÷5 pour slippage + sample discount)

### Avec DL stack complet (estimation)
- Foundation models : +10-15% edge T2m
- Neural post-proc : +10-15% CRPS additionnel
- RL execution : -20% slippage, +5% fill rate
- LLM reasoning : +2-3% sur rare events (petit mais tail)
- **Multiplicateur edge total : ~1.3-1.5x**
- **Target réaliste : $100-250k/an sur $10k bankroll**
- **Scale à $50k bankroll : $500k-1M/an** (avec fraction Kelly correcte)

### Comparaison avec hedge funds pro
- Hedge fund weather spécialisé (ex: Alastair Holmes) : $10-50M/an (mais >$100M AUM)
- Retail trader sophistiqué : $50-500k/an
- **Nous : viser le haut du retail sophistiqué**, potentiellement basse bande pro si scale

## Blocage / risques

1. **GPU compute** — Mac M5 MPS suffit pour inference mais training transformer gros = gpu externe
2. **ERA5 download long** — 5 ans × 40 stations × 1h = ~50Go, 2-6h queue Copernicus
3. **Overfitting** — ML gourmand en data, risque élevé sur 1-2 saisons d'entraînement
4. **Latency** — foundation models inference ~1s, peut-être trop lent pour intra-day nowcast
5. **Edge decay** — autres bots adoptent SOTA → premier arrivant gagne
6. **Oracle disputes** — risque rare mais tail (UMA resolution wrong)

## Prochaines étapes immédiates

**Session 8 (ce soir / demain)** :
1. Vault doc ML architecture (ce doc) ✅
2. Scaffolds PyTorch : DRN, Transformer, PPO
3. AIFS via Open-Meteo integration
4. LLM reasoning module (Claude API)
5. MLflow setup

**Session 9** :
6. Foundation models download + test local inference
7. Training pipeline skeleton
8. Feature store

**Session 10+** :
9. ERA5 download + premier training DRN
10. Iterate until DRN beats EMOS

## Related

- [[_MOC|Polymarket Hub]]
- [[architecture|Architecture]]
- [[data-sources|Data sources]]
- [[quick-start|Quick-start]]
- [[roadmap|Roadmap classique (mois 1)]]
