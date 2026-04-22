---
name: Polymarket — TODO pending (2026-04-22)
description: Punch list MAJ après session hedge-fund-grade upgrades. P&L réel $979, plafond AUM $10-20k identifié.
type: todo
project: brantham/polymarket
created: 2026-04-18
updated: 2026-04-22
tags: [polymarket, todo, roadmap]
priority: critical
---

# Polymarket — TODO pending

## COMPLETED 2026-04-22

- [x] **city_slug NULL bugfix** — confirmed_oracle + pair_arb wire Signal properly
- [x] **σ shrinkage per-city** — table + module + 46 villes + daily launchd 09:35
- [x] **Tier S v2 hedge-fund gates** — kill above_N/narrow/short_TTR/low_edge
- [x] **Tier S whitelist DB-backed** — auto-adaptatif + daily audit 09:40
- [x] **Market-side dedup** — révélé 20× P&L inflation, true P&L $979
- [x] **Slippage realistic** — price-aware fallback 1500 bps deep OTM
- [x] **Volume metadata** — signal_log.metadata.volume_usdc + backfill
- [x] **Capacity analysis** — plafond AUM $10-20k identifié
- [x] **Odds trajectories backtest** — 50% convergence = efficient markets
- [x] **Research pipeline** 7 stats + 6 analysis scripts

## P0 — User action required

- [ ] **Compte Copernicus CDS** : register free + accepter licences ERA5
  - URL : https://cds.climate.copernicus.eu/user/register
  - Licences : reanalysis-era5-pressure-levels + reanalysis-era5-single-levels
- [ ] **Créer `~/.cdsapirc`** avec clé API après register → débloque Pangu
- [ ] **Validate economic-thesis.md** : sentinel `THESIS VALIDATED BY PAUL ON YYYY-MM-DD`

## P1 — Investigation after scanner accumulates clean data

- [ ] **Debug London/Toronto/Sao Paulo 0 signaux** — villes ENABLED mais émission faible
- [ ] **Re-validate Austin edge** post-dedup (n actuel = 2 unique, besoin n ≥ 15)
- [ ] **Promote LA/NYC/Denver à graylist** via `audit_tier_s_whitelist.py` si n ≥ 15 WR ≥ 50%

## P2 — Scale beyond Polymarket weather

- [ ] **Wire Kalshi weather** — stub `kalshi_client.py` dormant, volume 10× Polymarket
- [ ] **Wire ECMWF OpenData** (13e NWP gratuite — HRES + ENS 51 membres)
- [ ] **Wire Pangu BMA** (après CDS setup user)
- [ ] **Persistence factor feature** — Shanghai ACF 0.92 momentum

## P3 — Risk management

- [ ] **Cluster cap dans risk_manager** — depuis correlation findings (austin↔houston ρ=0.91)
- [ ] **Force-fit calibrators** villes ENABLED — bloqué par n_outcomes < 30
- [ ] **Regime-aware filters** — detect saisonnalité edges (Austin printemps seul?)

## P4 — Infrastructure

- [ ] **Tests unitaires** : bucket_router v2, ttr_filter, sigma_shrinkage, live_executor dedup
- [ ] **Fusion pmhedge.db → alpha_data_hub.db** (2 DBs coexistantes)
- [ ] **Archive DBs legacy** dans backups/
- [ ] **Audit 150 scripts** — 30-40% probablement legacy

## P5 — Pro-level

- [ ] **Mesonet Synoptic** (free tier 5k req/day) wire dans `mesonet_client.py`
- [ ] **LLM features Claude API** — `llm_features.py`, ANTHROPIC_API_KEY en env
- [ ] **Market-making rebate** — `market_maker.py` quand py-clob-client wired
- [ ] **Live trading wire** — `POLY_PRIVATE_KEY` + py-clob-client dans `order_manager.py`

## P6 — Out of scope

- [ ] ECMWF HRES payant $50k/an — inutile vu OpenData gratuit
- [ ] Mesonet paid $500/mo
- [ ] Colocation NY5/LD5
- [ ] Pangu per-city fine-tune (quand N_obs ≥ 150 par ville)

## Tracking

| Task | Status |
|------|--------|
| Paper accumulate post-dedup | in_progress (started 2026-04-22) |
| User CDS setup | pending user |
| Austin re-validation | blocked — need 15+ unique trades |
| Multi-venue (Kalshi) | P2 — highest ROI for scaling |

## Related

- [[CONTINUATION-PROMPT]]
- [[dedup-bug-p-and-l-inflation]]
- [[capacity-reality-check]]
- [[tier-s-v2-hedge-fund-gates]]
- [[odds-trajectories-findings]]
- [[research-findings-2026-04-21]]
- [[ARCHITECTURE]]
- [[_MOC]]
