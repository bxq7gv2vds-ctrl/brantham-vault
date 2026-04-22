---
name: Continuation Prompt — prochaine session Claude
description: Prompt exact pour reprendre session Polymarket. MAJ 2026-04-22 après massive hedge-fund-grade upgrade session. P&L réel $979 (post-dedup), plafond AUM $10-20k identifié.
type: handoff
priority: critical
created: 2026-04-20
updated: 2026-04-22
tags: [polymarket, handoff, prompt, continuation]
---

# Prompt à coller dans la prochaine session

```
Projet : Polymarket Weather Hedge Fund — /Users/paul/polymarket-hedge/

Paper session #1 ACTIVE depuis 2026-04-20. Bankroll $1000 target $100k.
MAJ 2026-04-22: massive hedge-fund-grade upgrade session.

Lis dans cet ordre avant de répondre :
1. /Users/paul/.claude/projects/-Users-paul/memory/polymarket_session_2026-04-22.md
   (récap complet des 7 fixes + research pipeline + capacity reality)
2. /Users/paul/vault/brantham/polymarket/dedup-bug-p-and-l-inflation.md
   (le bug qui a révélé 20× inflation du P&L paper)
3. /Users/paul/vault/brantham/polymarket/capacity-reality-check.md
   (plafond AUM $10-20k identifié — micro-strat, pas vrai hedge fund)
4. /Users/paul/vault/brantham/polymarket/ARCHITECTURE.md
5. /Users/paul/vault/brantham/polymarket/TODO-pending.md

Règles absolues :
- WEATHER ONLY (pas crypto/sports/politics)
- Kelly 0.40 default
- FR conversation / EN code
- KMP_DUPLICATE_LIB_OK=TRUE avant uv run
- No emojis, no violet
- Accents FR obligatoires (é è ê à â ô î ï û ç)
```

## État exact au 2026-04-22 fin de session

### Paper session — stats VRAIES (post-dedup 20× inflation)

- **138 trades uniques** (136 closed, 2 open)
- **P&L réel : +$979.47**
- **WR : 79.4%**
- Avg / trade : +$7.20

**Par tier** :
- Tier A (NO workhorse): 80 closed, WR 90%, +$353 — **âme du système**
- Tier S (YES deep_OTM): 21 closed, WR 14%, +$628, avg +$29.90 — volatile
- Tier C (CONFIRMED_NO): 6 closed, WR 100%, +$8
- Tier B (NO ITM 0.90+): 29 closed, WR 93%, -$9

**City whitelist post-dedup** : TOUS UNPROVEN (aucun n ≥ 15 unique). Tier S tourne
en exploration mode Kelly ×0.75 jusqu'à accumulation d'evidence.

### 57 launchd jobs actifs

Nouveaux aujourd'hui :
- `com.paul.polymarket-sigma-shrinkage` → 09:35 UTC daily (refresh σ calibration)
- `com.paul.polymarket-tier-s-audit` → 09:40 UTC daily (whitelist auto-update)

### Bugs fixés (tous wired, scanner restart pris effet)

1. **city_slug NULL** — confirmed_oracle.py + pair_arb.py set maintenant city_slug/icao
2. **σ shrinkage per-city** — table `sigma_shrinkage_city`, 46 villes. Seoul ×2.00, LA ×0.63
3. **Tier S v2 gates** — kill above_N/narrow/short_TTR/low_edge. DB-backed whitelist
4. **Market-side dedup** — guard `WHERE market_id=? AND side=? AND status IN (OPEN,FILLED)`
5. **Slippage realistic** — 1500 bps deep OTM vs flat 30 bps avant
6. **Volume metadata** — stocké dans signal_log.metadata pour capacity analysis

### Recherche pipeline complet

`research/pole_stats/` : 01-08 (8 scripts)
`research/pole_analysis/` : 01-06 (6 scripts)

Top findings :
- **ECMWF domine 29/46 villes** (MAE < 0.5°C)
- **Seoul σ × 2.00 SEVERE_EXPAND** (cov90=15%)
- **Austin↔Houston ρ=0.91** (zero diversification intra-cluster)
- **50% convergence global** = markets Polymarket random walk efficient
- **Austin convergence 40% + vol 0.007** = mispricing stable structurel
- **Volume median Tier S $749** → plafond AUM $10-20k

## Vérités hedge-fund-grade

1. Ce n'est PAS un vrai hedge fund scalable
2. Plafond AUM capacity ~$10-20k avant market impact
3. ROI réaliste : $30-60k/an à full capacity (micro-strat)
4. Pour scaler : **multi-venue** (Kalshi stub existe déjà dans `kalshi_client.py`)
5. Ou expand au-delà weather (sports/politics si edge transférable)

## Bloquants user

1. **Compte Copernicus CDS** : https://cds.climate.copernicus.eu/user/register
   - Accepter licences ERA5 (pressure-levels + single-levels)
   - Créer `~/.cdsapirc` avec clé API
   - Débloque Pangu live cycle
2. **Validate economic-thesis.md** : ajouter sentinel `THESIS VALIDATED BY PAUL ON YYYY-MM-DD`
3. **Debug London/Toronto/Sao Paulo 0 signaux** : toujours pending (villes ENABLED mais
   peu de signaux émis — à investiguer scan verbose)

## Actions P0 à la reprise

1. **Check scanner health** : `launchctl list com.paul.polymarket-alpha-live-runner`
2. **Check fresh signals post-fixes** :
   ```sql
   SELECT COUNT(*), SUM(pnl_usdc) FROM trade_log
   WHERE open_ts > strftime('%s', '2026-04-22 12:00')
     AND is_dup = 0 AND status='CLOSED';
   ```
3. **Re-run tier_s_audit** quand n ≥ 15 unique par ville (probable 10-14 jours)
4. **Check Pangu download** : `ls -lh /Users/paul/polymarket-hedge/models/pangu_weather_24.onnx`
   Size attendue : ~1.18 GB. Download complet, ONNX validé via `uv run scripts/setup_pangu.py --verify`

## Actions P1-P3 disponibles

- P1 : Wire Kalshi weather (stub dormant, scale 10× Polymarket vol)
- P2 : Wire ECMWF OpenData (13e NWP source gratuite)
- P3 : Wire Pangu BMA (bloqué CDS)
- P3 : Persistence factor feature (Shanghai ACF 0.92 momentum)
- P4 : Cluster cap dans risk_manager (correlation findings)
- P4 : Force-fit calibrators villes ENABLED (bloqué n_outcomes)

## Commandes essentielles

```bash
cd /Users/paul/polymarket-hedge

# Status CLI (avec dedup filter auto)
KMP_DUPLICATE_LIB_OK=TRUE uv run python scripts/trade_status.py

# Audit whitelist Tier S
KMP_DUPLICATE_LIB_OK=TRUE uv run python scripts/audit_tier_s_whitelist.py

# Research pipeline refresh
KMP_DUPLICATE_LIB_OK=TRUE uv run python research/pole_stats/06_sigma_empirical.py
KMP_DUPLICATE_LIB_OK=TRUE uv run python research/pole_analysis/06_capacity_analysis.py

# Load σ shrinkage manually
KMP_DUPLICATE_LIB_OK=TRUE uv run python scripts/load_sigma_shrinkage.py

# Restart scanner (after code changes)
launchctl kickstart -k gui/501/com.paul.polymarket-alpha-live-runner
```

## Related

- [[dedup-bug-p-and-l-inflation]] — le fix qui a révélé la vérité
- [[capacity-reality-check]] — plafond AUM micro-marché
- [[tier-s-v2-hedge-fund-gates]] — Tier S v2 logic
- [[odds-trajectories-findings]] — market efficiency analysis
- [[research-findings-2026-04-21]] — pôle stats findings
- [[ARCHITECTURE]]
- [[TODO-pending]]
- [[_MOC]]
