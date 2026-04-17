---
name: Architecture Polymarket Hedge Fund Grade
description: Architecture système complète en 4 couches (data/model/alpha/execution) pour trading Polymarket hedge-fund style
type: architecture
created: 2026-04-17
tags: [polymarket, architecture, hedge-fund]
---

# Architecture Polymarket Hedge Fund Grade

## Principe directeur

**4 couches orthogonales, chacune utilisant les meilleurs outils disponibles (gratuits) sur sa spécialité.**

Cohérence du système > sophistication de chaque couche. On vise **simplicité opérationnelle + rigueur ML + execution latency faible**.

## Vue d'ensemble

```
┌──────────────────────────────────────────────────────────────┐
│ LAYER 1 : DATA HUB                                           │
│   NWP multi-source (HRRR, ECMWF-IFS, ICON-EU, GFS, GEFS)    │
│   Obs (METAR, Mesonet, PWS, radar, satellite)                │
│   Reanalysis ERA5 (training)                                 │
│   Polymarket CLOB L2 orderbook                               │
└──────────────────┬───────────────────────────────────────────┘
                   │
┌──────────────────▼───────────────────────────────────────────┐
│ LAYER 2 : MODEL HUB                                          │
│   EMOS par (station × mois)                                  │
│   BMA (Bayesian Model Averaging) entre NWP sources           │
│   XGBoost post-proc (features riches)                        │
│   DRN neural ensemble (SOTA 2023)                            │
│   Kalman filter online (intra-day bias)                      │
│   → Output: distribution calibrée P(T_max)                   │
└──────────────────┬───────────────────────────────────────────┘
                   │
┌──────────────────▼───────────────────────────────────────────┐
│ LAYER 3 : ALPHA LAYERS (orthogonaux)                         │
│   1. Model vs market (edge principal 3-7%)                   │
│   2. Sum-to-1 arbitrage (math, near-zero risk)               │
│   3. CONFIRMED oracle (T_max connu avant settlement)         │
│   4. Orderbook microstructure (imbalance, staleness)         │
│   5. Cross-market pairs (corrélations villes)                │
│   6. Nowcast 0-6h (radar + HRRR + obs)                       │
└──────────────────┬───────────────────────────────────────────┘
                   │
┌──────────────────▼───────────────────────────────────────────┐
│ LAYER 4 : EXECUTION + RISK                                   │
│   Polymarket CLOB WebSocket (real-time L2 book)              │
│   Order manager (limit-first, rebate capture)                │
│   Kelly correlation-adjusted sizing                          │
│   Kill switch (per-day, per-signal, drawdown)                │
│   Slippage auto-calibration live                             │
└──────────────────────────────────────────────────────────────┘
```

## Layer 1 : Data Hub

### Sources best-in-class par région

**USA** :
- **HRRR** (NOAA) — 3km, 1h updates, 18h forecast → meilleur nowcast US
- **RAP** (NOAA) — 13km, 6h forecast → backup
- **GFS** (NOAA) — 13km, 384h → long-range
- **GEFS** (NOAA) — 31 membres, ensemble pour incertitude
- **METAR ASOS** — aviationweather.gov, 1h updates
- **Mesonet** (synopticdata.com) — stations denses
- **NEXRAD Level-II** via AWS S3 — radar raw
- **MRMS** via AWS — composite radar + QPE
- **GOES-16/17/18** via AWS — satellite IR

**Europe** :
- **ECMWF-IFS** 9km — meilleur global NWP (Open Data)
- **ICON-EU** 6.5km (DWD) — Europe-spécialisé
- **AROME** 1.3km (Météo-France) — France haute-res
- **UKV** 1.5km (MetOffice) — UK
- **METAR** + **OGIMET** (historique)
- **EUMETNET OPERA** — radar composite
- **Meteosat MSG** — satellite

**Asie** :
- **ECMWF** + **ICON-EU**
- **JMA MSM** 5km — Japon
- **KMA LDAPS** 1.5km — Corée
- **CMA GRAPES** — Chine
- **Himawari** — satellite Asie-Pacifique

**Global** :
- **ERA5** (Copernicus) — reanalysis 40+ ans, training ML
- **MERRA-2** (NASA) — backup reanalysis
- **ISD** (NOAA) — integrated surface database historique

### Coût : $0

Toutes les sources sont gratuites (Copernicus/NASA/NOAA/DWD/Météo-France en open data). Le coût réel est dans le stockage (~100 Go) et l'ingestion CPU (minimal).

### Schema DB unifié

Tables (voir `alpha/data_hub.py`) :
- `stations` — registry ICAO + lat/lon + timezone + climato
- `nwp_forecasts` — per-source ensemble forecasts
- `nwp_ensemble_blend` — pre-computed stats par station × date
- `obs_temperature` — observations METAR/Mesonet
- `orderbook_snapshots` — Polymarket CLOB L2 (best bid/ask + depth)
- `calibrated_probs` — output modèle
- `signal_log` — tous les signaux émis
- `trade_log` — trades exécutés avec slippage + fees
- `model_performance` — tracking RMSE/CRPS par modèle
- `data_freshness` — monitoring des sources

## Layer 2 : Model Hub

### Stack ML par complexité croissante

1. **EMOS** (Gneiting 2005) — Ensemble Model Output Statistics
   - Calibre (a + b·ensemble_mean, c + d·ensemble_std) par station × mois
   - Robuste, rapide, interprétable
   - Baseline indispensable

2. **BMA** — Bayesian Model Averaging
   - Weights entre NWP sources (GFS, ECMWF, ICON, HRRR) mis à jour online via rolling CRPS
   - Exploite complémentarité des sources

3. **XGBoost post-processing**
   - Features : ensemble mean, spread, obs lags (1h, 3h, 24h), radar echo, hour-of-day, day-of-year, station climatology
   - Target : T_max actual (from ERA5 / METAR)
   - Un modèle par région pour éviter curse of dimensionality

4. **DRN** (Distributional Regression Network, Rasp & Lerch 2018)
   - Neural net qui output (μ, σ) de distribution
   - Beat EMOS de 5-15% en CRPS
   - SOTA 2020+ pour ensemble post-processing

5. **Analog regression** pour events rares
   - k-NN sur patterns synoptiques (heat wave, cold snap)
   - Utile quand NWP fail (régimes extrêmes)

6. **Kalman online**
   - Update intra-day du bias station (t_current vs prédit)
   - Bouge la distribution au fil de la journée

### Output final

Pour chaque (station, target_date, horizon) :
- `P(T_max ≥ threshold)` calibré
- `P(T_max ∈ [a, b])` pour bins
- Mean + variance + quantiles
- Confidence score (basé sur cohérence modèles + freshness data)

## Layer 3 : Alpha Layers

### Les 6 alphas orthogonaux

| # | Alpha | Edge source | Risk | EV typique |
|---|---|---|---|---|
| 1 | Model vs market | Calibration > consensus | Model drift | 3-7% par trade |
| 2 | Sum-to-1 arb | Math (Σ bins = 1) | Fill legging | 0.5-2% par arb |
| 3 | CONFIRMED oracle | T_max déjà observé | Near-zero | ~100% WR rare |
| 4 | Orderbook imbal. | Microstructure | Latency | 0.3-1% par trade |
| 5 | Cross-market pairs | Corrélation villes | Regime change | 1-3% par pair |
| 6 | Nowcast 0-6h | Radar+obs+HRRR | Timing | 2-5% par trade |

Les alphas sont **orthogonaux** : ils exploitent des inefficiences différentes, donc peuvent être additionnés dans un portfolio (après correlation-adjustment).

### Signal emission

Chaque alpha émet un signal dict :
```python
{
    "alpha_type": "MODEL_VS_MARKET",
    "market_id": "...",
    "side": "YES" | "NO",
    "entry_price": 0.45,
    "est_prob": 0.58,
    "edge": 0.13,
    "confidence": 0.85,   # 0-1 score
    "max_size_usdc": 150,
    "reason": "...",
    "metadata": {...}
}
```

Le risk manager décide size finale via Kelly correlation-adjusted.

## Layer 4 : Execution + Risk

### Execution

**Polymarket CLOB direct** (pas Gamma API) :
- WebSocket L2 orderbook stream → latence ~50-150ms
- REST API pour order placement
- Maker orders priority (rebates 0.02% → gagne spread)
- Cancel-replace adaptive si prix drift

**Order manager logic** :
1. Post limit au best bid (buy) ou best ask + 1 tick (maker)
2. Si pas filled après 30s → cancel + replace à mid
3. Si mid bouge >2c de signal entry → skip
4. Log fill price + slippage vs signal
5. Update slippage model online (exponential moving avg)

**VPS** :
- Primary : AWS us-east-1 (proche Polymarket Matic RPC via Infura)
- Backup : Hetzner EU
- Health check mutual, failover automatique

### Risk management

**Sizing** :
- Kelly fractional (pas full — 25-40% de full Kelly)
- **Correlation-adjusted** : si 5 signaux sur villes corrélées, scale down par √5
- Per-alpha cap (ex : sum-arb max 2% bankroll, model-vs-market max 5%)
- Per-trade cap (ex : 2% bankroll par signal)

**Caps** :
- Per-city daily : 20% bankroll
- Per-day total : 10% loss → kill switch
- Per-signal type : cap selon WR historical

**Kill switch triggers** :
- Daily loss > 10% bankroll
- Realized WR drift > 5 points vs expected
- Data freshness DOWN sur >1 source critique
- Model output diverge > 3σ de baseline
- API rejection rate > 5%

**Drawdown-based scaling** :
- DD 0-10% : full sizing
- DD 10-15% : 0.7× sizing
- DD 15-20% : 0.5× sizing
- DD > 20% : pause + manual review

## Monitoring

**Grafana + Prometheus** (à installer) :
- Live P&L par alpha
- Realized vs expected WR
- Data freshness status
- Order fill rate
- API latency
- Orderbook depth

**Alerts Telegram** (existant) :
- New signal émis
- Trade exécuté + fill price
- Daily P&L summary (09:00 Paris)
- Kill switch trigger
- Data source DOWN

**Reports** :
- Daily auto-report vers `vault/brantham/polymarket/reports/YYYY-MM-DD.md`
- Weekly performance review
- Monthly model retrain + evaluation

## Related

- [[_MOC|Polymarket Hub]]
- [[data-sources|Data sources détaillées par région]]
- [[model-design|Design modèle ML détaillé]]
- [[execution-design|Infrastructure execution]]
- [[risk-management|Risk management]]
- [[roadmap|Roadmap phased]]
