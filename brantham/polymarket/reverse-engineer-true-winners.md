---
name: Reverse engineering — True weather winners
description: Audit complet top traders weather Polymarket. Bug data layer révélé (trades_onchain manque NO tokens). Vrais patterns winners identifiés via activity API + CLOB settlements.
type: pattern
created: 2026-04-25
updated: 2026-04-26
tags: [polymarket, reverse-engineering, edge-research, hedge-fund-grade]
---

# Reverse engineering — True weather winners

## Contexte

Session 2026-04-25 / 26 : reverse-engineer les top traders weather pour
identifier les patterns gagnants. 3 itérations successives de l'analyse
ont révélé des bugs majeurs et finalement la vérité.

## Bugs majeurs découverts

### Bug 1 — Settlement inference (last-trade-price)
- `top_pnl_traders.py` v1 inférait le winner via `last-trade-price > 0.98`
- **Faux** sur beaucoup de markets (convergence partielle, multi-bracket)
- Fix : fetch authoritative `clob.polymarket.com/markets/{cid}` → `tokens[].winner`
- Script : `scripts/fetch_clob_settlements.py` → `reports/clob_settlements.csv`
- **17 604 markets settled, 17 402 closed (1937 YES won, 15465 NO won)**

### Bug 2 — Data layer trades_onchain ne capture que YES tokens
- `trades_onchain.db` : 9.5M trades mais **seulement sur token_id_yes**
- Les BUY NO directs (sur token_id_no) sont **invisibles**
- Pour `0x4eb5` : YES vol $40k visible, **NO vol $110k invisible**
- **70% du volume des winners est sur le NO token → on rate massif**
- Fix court terme : utiliser `data-api.polymarket.com/activity` pagination
- Fix long terme : étendre scraper pour ingérer NO token trades

### Bug 3 — Time window incomplet
- `trades_onchain` couvre 2025-09-30 → 2026-04-11 seulement
- Markets weather depuis 2025-01 → 9 mois manquants
- **+13 jours non scrapés** depuis dernière collecte (2026-04-11 → 2026-04-26)
- 3 485 markets sans aucun trade onchain (CLOB orderbook fills non captés)

### Bug 4 — Categories weather manquantes
- DB ne contient QUE `highest-temperature` (21 089 markets)
- Manquent : **lowest-temperature, precipitation, snow, rain**
- Scraper `polymarket_client.py` query `q="temperature {city}"` seulement
- Estimation : on rate ~50% de l'univers tradable

## Vérité finale (top 6 weather winners)

Source : `reports/true_pnl_top45.md` (activity API + CLOB)

| wallet | TRUE P&L | YES vol | NO vol | trades | window |
|---|---:|---:|---:|---:|---|
| `0x05e7...9641` | **+$68 936** | $299k | $210k | 219 | 2026-02-19 → 04-05 |
| `0x42fd...96c0` | **+$28 386** | $149k | $356k | 86 | 2026-02-12 → 04-08 |
| `0x331b...193f` | **+$27 017** | $79k | $68k | 2 671 | 2026-02-28 → 04-08 |
| `0xcd9d...06b0` | **+$15 230** | $31k | $5k | 2 901 | — |
| `0x584e...090f` | **+$11 724** | $19k | $44k | 2 286 | — |
| `0x97eb...9fbe` | **+$11 322** | $48k | $183k | 2 701 | — |

**32 wallets sur 45 ont sign opposé entre v2 et truth.**
Top P&L réel = $69k/an, pas $300k+. **Capacity micro-marché confirmée.**

## Patterns identifiés (deep-dive 3 winners)

Source : `reports/deepdive_true_winners.md`

### `0x05e7` — Whale opportuniste (37 trades, $510k vol)
- 100% TTR < 6h, concentré 0-2h
- Cities : **Atlanta dominante** +$54k, Sao Paulo, Miami
- Cellules killer :
  - **NO < 0.05 → +1623% ROI** ($958 vol → +$15.5k)
  - **YES 0.2-0.5 → +171% ROI** ($24k vol → +$41k)

### `0x42fd` — Mid-cap NA-focused (41 trades, $506k vol)
- TTR étalé 0-12h
- Cities : **Seattle, Toronto, Chicago, Dallas**
- Cellules killer :
  - **YES 0.2-0.5 → +119% ROI**
  - **NO 0.5-0.8 → +9.3% ROI** (bulk volume)
  - **TTR 12-24h → +163% ROI** (small vol)

### `0x331b` — HFT scalper US (2 114 trades, $147k vol)
- 95% TTR 0-2h, size médian ~$70/trade
- Cities : **NYC + Seattle**
- Cellules killer :
  - **NO < 0.05 → +1194% ROI**
  - YES < 0.05 → +195% ROI
  - YES 0.05-0.2 → +164% ROI

## Pattern unifié — où vit l'edge

| Cellule | Verdict | Notre exploitation |
|---|---|---|
| **TTR < 2h** | Edge dominant | Partiel (Tier A NO seulement) |
| Token YES + NO | Tradés activement | On voit que YES (gap data) |
| **Prix < 0.20** | Edge majeur (100-1600% ROI) | Tier S vise < 0.05 (mauvaise zone) |
| **Prix 0.2-0.5** | Edge fort (45-170%) | Pas trade |
| Prix > 0.95 ITM | Faible (1-2%) | C'est notre Tier A actuel |
| 100% highest_temp | Confirmé | OK |

## Hypothèse stratégique

**Les winners ne font PAS du NWP forecasting sophistiqué.** Pattern
observé = **METAR observation front-running** :
1. Track temp observée real-time (ASOS 5 min cadence, gratuit)
2. À T-2h du settlement, obs + diurnal → proba bracket
3. Achète bracket gagnant à 0.20-0.50 (mid-range mispricing) ou
   lottery NO à <0.05 (brackets clairement faux)
4. Collecte spread au settlement

**Notre Pangu/EMOS infra est inutile vs ces mecs.** Compétition
n'est pas modèle vs modèle, c'est **latence observation + bracket
selection rapide**.

## Implications pour notre stratégie

### À changer immédiatement
1. **Élargir Tier S YES** : zone 0.05-0.20 (pas <0.05) — 5× capacity, edge prouvé
2. **Ajouter Tier S NO** : NO < 0.05 sur brackets clairement faux given obs
3. **Trader mid-range 0.2-0.5** : ignoré aujourd'hui, edge fort
4. **Réduire Tier A ITM 0.95+** : faible ROI, on perd vs MM

### Build prioritaire
- `bracket_pricer_obs.py` : given Tmax-so-far + heure locale + diurnal climato
  → P(bracket = winner) pour chaque bracket
- Wire dans live_executor : si edge prix marché vs P_obs > 5% → trade
- Capacity ciblée : ~$70k/an extractable (top winner référence)

### À parker
- Pangu live cycle (CDS bloqué, mais aussi : pas l'edge réel)
- EMOS Tmin extension (à reprendre si phase 1 obs-based saturée)
- Precipitation forecasting full-month (R&D coûteux, edge incertain)

## Files livrés cette session

Scripts (dans `/Users/paul/polymarket-hedge/scripts/`) :
- `top_weather_traders.py` — leaderboard volume (step 1)
- `trader_equity_curves.py` — equity curves top-20 vol (step 2)
- `trader_patterns.py` — patterns top-5 calmar (step 3)
- `top_pnl_traders.py` — leaderboard P&L v1 (BROKEN — last-trade-price bug)
- `audit_top_traders_api.py` — audit /value /traded API
- `diagnose_0x4eb5_ttr.py` — TTR distribution wallet 0x4eb5
- `diagnose_0x4eb5_pnl.py` — vrai P&L wallet via activity + CLOB
- `fetch_clob_settlements.py` — fetch authoritative settlements (17 604 cids)
- `top_pnl_traders_v2.py` — leaderboard P&L v2 (still BROKEN — YES-only bias)
- `audit_top45_true_pnl.py` — TRUE P&L via activity API + CLOB (la vérité)
- `deepdive_true_winners.py` — patterns détaillés top 3 winners

Reports (dans `/Users/paul/polymarket-hedge/reports/`) :
- `weather_leaderboard.md` + `.csv`
- `trader_metrics.md` + `.csv`
- `top5_patterns.md`
- `pnl_leaderboard.md` (v1, BIAISÉ)
- `api_audit_top30.md`
- `diag_0x4eb5_ttr.md`
- `diag_0x4eb5_pnl.md`
- `diag_0x4eb5_trades.csv`
- `diag_0x4eb5_resolved.csv`
- `clob_settlements.csv` (17 604 markets settled)
- `pnl_leaderboard_v2.md` + `.csv` (v2, BIAISÉ — YES-only)
- `true_pnl_top45.md` + `.csv` (**LA VÉRITÉ**)
- `deepdive_true_winners.md`
- `deepdive_0x05e7.csv`
- `deepdive_0x42fd.csv`
- `deepdive_0x331b.csv`

## Related

- [[CONTINUATION-PROMPT]]
- [[ARCHITECTURE]]
- [[capacity-reality-check]]
- [[odds-trajectories-findings]]
- [[dedup-bug-p-and-l-inflation]]
- [[_MOC]]
- [[brantham/_MOC]]
