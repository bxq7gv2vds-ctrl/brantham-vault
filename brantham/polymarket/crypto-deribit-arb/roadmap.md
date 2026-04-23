---
title: Roadmap
created: 2026-04-23
parent: [[_MOC]]
tags: [roadmap, planning]
status: phase-1-active
---

# Roadmap — Build Polymarket × Deribit Crypto Arb

## Phase 1 : Data + Validation empirique (jour 1-2)

**Objectif** : valider que l'edge existe vraiment sur des données live.

**Tâches** :
- [ ] Setup module crypto_arb dans polymarket-hedge
- [ ] Build Deribit REST client (option chain BTC/ETH)
- [ ] Build Polymarket crypto market scanner
- [ ] Build SVI smile fitter
- [ ] Build risk-neutral density extractor
- [ ] Build fair_prob calculator + edge engine (avec fees Polymarket exact)
- [ ] Snapshot ingestion script (60s loop pour 24h)
- [ ] Analyse : combien de brackets simultanés ont edge >2pp ?

**Go/No-Go criterion** :
- ≥10 brackets simultanés avec edge >2pp en moyenne sur 24h → GO Phase 2
- 5-10 brackets → review, maybe niche strategy
- <5 brackets → NO-GO, abandon ou pivot

**Output** : `vault/brantham/polymarket/crypto-deribit-arb/phase1-validation-report.md`

## Phase 2 : Pricing engine production (jour 3-4)

**Objectif** : pricing engine performant et robust.

**Tâches** :
- [ ] Numba JIT pour SVI fit (target <5ms)
- [ ] Vectorized density computation (numpy)
- [ ] Cache layer (smile + density per asset+expiry, TTL 60s)
- [ ] Tests unitaires complets (smile fit, density, fair_prob)
- [ ] Integration test : full pipeline 1 cycle <2s

**Go/No-Go** : pricing cycle complet <2s, tests passent

## Phase 3 : Portfolio + hedge (jour 5-6)

**Objectif** : portfolio management + hedge optimization fonctionnels.

**Tâches** :
- [ ] Greeks aggregator (sum across positions per asset)
- [ ] Cvxpy hedge optimizer
- [ ] Hedge instrument catalog (Hyperliquid perp + Deribit options shortlist)
- [ ] Sizing logic (Kelly fractional + Ledoit-Wolf shrinkage)
- [ ] Position state machine (pending/open/closing/closed)
- [ ] Continuous rebalancer (60s soft / 5min hard)
- [ ] Risk engine (DD bands, kill-switch, position limits)

**Go/No-Go** : hedge cost <30% edge gross, optimizer converge en <200ms

## Phase 4 : Paper trading 7 jours (jour 7-13)

**Objectif** : valider full pipeline en paper avant tout capital réel.

**Tâches** :
- [ ] Paper execution layer (simulated fills réalistes avec slippage)
- [ ] Logging détaillé (chaque décision, chaque hedge, chaque P&L)
- [ ] Dashboard temps réel (Streamlit ou Textual TUI)
- [ ] Reporting quotidien auto (P&L, Sharpe rolling, DD, top trades)
- [ ] Run 7 jours complets, monitor

**Go/No-Go** :
- Sharpe paper > 1.5 → GO Phase 5
- Sharpe 1-1.5 → review params, retest 7j
- Sharpe <1 → debug ou abandon

## Phase 5 : Live $200 → $1000 (semaine 2-4)

**Objectif** : valider live, scaler progressivement.

**Sub-phase 5a (semaine 2)** : Live $200, monitoring intensif
- Open Deribit account ($150 deposit)
- Open Hyperliquid account ($50 collateral)
- 14 jours live, daily review
- Mesure live ratio = realized_sharpe / paper_sharpe

**Go/No-Go 5b** :
- Live ratio >0.6 → GO scale $1000
- Live ratio 0.3-0.6 → reduce expectations, continue $200
- Live ratio <0.3 → debug, possible abandon

**Sub-phase 5b (semaine 3-4)** : Live $1000 si validé
- Scale capital progressivement ($200 → $500 → $1000 sur 7 jours)
- Review hebdomadaire
- Adjust thresholds basé sur live data

## Phase 6 : Scaling (mois 2-12)

Si validation réussie :

- **Mois 2-3** : Optimization, scale à $5-10k AUM
- **Mois 4-6** : Add ETH brackets, monthly markets, scale à $25-50k
- **Mois 7-9** : Add second venue (Kalshi crypto), scale à $50-100k
- **Mois 10-12** : Optimization capacity, scale au plafond ~$200k AUM

## Phase 7 : Diversification stratégies (an 2+)

Si Phase 6 success :
- Strat #2 : Sports brackets Polymarket
- Strat #3 : Politique events
- Strat #4 : Météo (déjà existant, consolider)
- Portfolio of strategies : Sharpe agrégé > somme des Sharpes individuelles

## Tracking & reporting

**Daily** : auto-report dans `vault/brantham/polymarket/crypto-deribit-arb/sessions/YYYY-MM-DD.md`
**Weekly** : review humaine, ajustement thresholds
**Monthly** : MOC update, capacity check, scaling decision

## Related

- [[_MOC]]
- [[architecture]]
- [[math-pricing-hedge]]
- [[risks-mitigation]]
