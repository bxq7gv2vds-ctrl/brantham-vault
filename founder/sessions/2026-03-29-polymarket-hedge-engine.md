---
title: Polymarket Hedge Engine — Construction complète
date: 2026-03-29
project: polymarket-hedge
type: session
tags: [polymarket, trading, nwp, emos, hedge-fund, intraday]
---

# Session 2026-03-29 — Polymarket Hedge Engine

## Ce qui a été construit

### Point de départ
TUI Textual pour dashboard de trading Polymarket. L'objectif a évolué rapidement vers un vrai moteur de trading météo professionnel.

### Architecture finale — `/Users/paul/polymarket-hedge/`

#### Stack
- Python 3.13, uv, Textual TUI
- SBMM + Kalman Filter (log-odds OU process)
- DCC-GARCH (corrélations dynamiques)
- CVaR optimization (CVXPY)
- EMOS + BMA calibration (NWP météo)
- APScheduler (jobs 5min/1h/hebdo)
- SQLite (signals, positions, P&L)
- Telegram Bot (alertes)

#### Modules clés

**`src/pmhedge/models/emos.py`** — Core du modèle météo
- EMOS (Ensemble Model Output Statistics) : régression Gaussienne Non-Homogène
- Formule : `T_obs ~ N(a + b×μ_ens, √(c + d×var_ens))`
- Entraîné sur 731 jours de (prévision NWP, observation réelle) par ville+mois
- BMA (Bayesian Model Averaging) : poids GFS/ICON/GEM basés sur CRPS historique
- 37 villes × 12 mois = **444 params EMOS, 148 BMA weights**
- DB SQLite : `/Users/paul/polymarket-hedge/emos_cache.db`
- CRPS NYC = **1.01°F** (précision météo professionnelle)
- Calibration complète en 6 secondes

**`src/pmhedge/data/nwp.py`** — NWP intégré EMOS
- `NWPForecast(calibrator=cal)` : mode calibré ou empirique
- 92 membres ensemble (GFS 30 + ICON 39 + GEM 20 + extras)
- Parseur de questions Polymarket : ville + date + seuil + unité
- Fix critique : filtrage des nombres de date (ex: "March **31**")
- `var_ens` = variance inter-modèle (cohérent avec données entraînement)

**`src/pmhedge/data/live.py`** — API Polymarket
- CLOB API : `https://clob.polymarket.com`
- Gamma API : `https://gamma-api.polymarket.com`
- Endpoint correct météo : `public-search?q=temperature` (PAS `/markets?search=weather`)
- `outcomePrices`, `clobTokenIds` : JSON strings, pas objets imbriqués
- WebSocket : `wss://ws-subscriptions-clob.polymarket.com/ws/market`

**`src/pmhedge/infra/`** — Infrastructure 24/7
- `alerts.py` : Telegram Bot (TELEGRAM_BOT_TOKEN + TELEGRAM_CHAT_ID)
- `db.py` : SQLite — tables signals, positions, pnl_history, nwp_signals_log
- `scheduler.py` : APScheduler — scan/5min, NWP refresh/1h, recalibration EMOS/dimanche 3h

**`scripts/calibrate_emos.py`** — One-time calibration
**`scripts/run_headless.py`** — Run 24/7 sans TUI
**`deploy/pmhedge.service`** + **`deploy/deploy.sh`** — Systemd Hetzner

#### Résultats live (scan 2026-03-29)
- 57 marchés météo Polymarket trouvés
- 50 NWP calculés (dont 12 avec EMOS calibré)
- **London 11°C LONG** : marché 25.5% vs EMOS 71.9% → **edge +46.4%**
- **London 13°C SHORT** : marché 25.5% vs EMOS 3.3% → **edge +22.2%**
- **Miami 80-81°F SHORT** : marché 33% vs EMOS 13.8% → **edge +19.2%**
- **NYC 72-73°F LONG** : marché 42.5% vs EMOS 57.0% → **edge +14.5%**

---

## Décision stratégique majeure en fin de session

### La stratégie "hold to resolution" est sous-optimale

Le modèle EMOS calcule correctement `edge = market - NWP_fundamental`. Mais c'est du capital bloqué jusqu'à la résolution.

**Ce qui fait vraiment de l'argent : trader les MOUVEMENTS avant résolution.**

### Architecture intraday planifiée (non encore implémentée)

#### 1. Jump-Diffusion Model
```
dL = κ(μ-L)dt + σ_diff dW + J dN(t)
```
- L = log-odds
- Sauts J aux mises à jour NWP (4×/jour : 00Z, 06Z, 12Z, 18Z UTC)
- Entre les sauts : mean-reversion → fade les mouvements
- Au saut : trade la direction → ferme à 80% absorption

#### 2. NWP Lead-Lag Signal
- GFS update → calcul immédiat proba EMOS
- Marché prend 10-60 min à absorber
- Entry immédiat, TP à 80% convergence, max hold 2h
- **Pas de risque résolution**

#### 3. Bracket Vol Surface
- N brackets NYC March 31 doivent sommer à 1
- Fitter distribution implicite du marché (CVXPY)
- Comparer à distribution NWP → arbitrage sur "strikes" (comme surface de vol options)
- Somme observée le 2026-03-29 : **109.5%** → violation no-arb structurelle

#### 4. Order Flow Microstructure
- Order Imbalance = (bid_qty - ask_qty) / (bid_qty + ask_qty)
- Temporary impact reversion : après gros trade → prix revient → trade le retour
- Nécessite tick data historique pour calibrer λ

#### 5. Tick Data Collection
- WebSocket → SQLite : bars 10 secondes
- NWP run timestamps (événements schedulés)
- Order book depth snapshots

---

## Modules à construire (prochaine session)

| Priorité | Module | Description |
|----------|--------|-------------|
| 1 | `data/tick_store.py` | WebSocket → SQLite 10s OHLCV bars |
| 2 | `data/nwp_scheduler.py` | Détection runs NWP, event NWP_JUMP |
| 3 | `models/jump_diffusion.py` | Extension SBMM avec sauts + absorption tracking |
| 4 | `models/bracket_surface.py` | Distribution implicite + arbitrage inter-brackets |
| 5 | `models/microstructure.py` | OI signal + temporary impact |
| 6 | `strategy/intraday_engine.py` | Moteur tick-by-tick, signal aggregation |
| 7 | `infra/clob_executor.py` | Limit orders CLOB, cancel, fill tracking |

Dépendance à ajouter : `py-clob-client` (SDK officiel Polymarket pour signing ECDSA)

---

## Commandes utiles

```bash
# Calibrer EMOS (37 villes, ~6s)
uv run scripts/calibrate_emos.py --force

# Statut calibration
uv run scripts/calibrate_emos.py --status

# Lancer le TUI
uv run scripts/run_hedge.py

# Lancer headless (production)
uv run scripts/run_headless.py

# Deploy Hetzner
bash deploy/deploy.sh
```

---

## Bugs résolus durant la session

1. **Endpoint météo incorrect** : `/markets?search=weather` retourne n'importe quoi → fix: `public-search?q=temperature`
2. **Parseur threshold** : "March 31" capturait "31" comme seuil température → fix: filtre nombres de date
3. **var_ens incohérent** : `np.var(89 membres)` vs `np.var(3 moyennes modèles)` → fix: inter-model variance
4. **Scanner alias manquant** : `Scanner` pas défini → fix: `Scanner = OpportunityScanner`
5. **DB path** : `emos_cache.db` dans `scripts/` → fix: `Path(__file__).resolve().parent×4`
6. **max_ttr_h=48h** filtrait tout → fix: `max_ttr_h=8760h`

## Related

- [[founder/_MOC]]
- [[_system/MOC-decisions]]
- [[_system/MOC-patterns]]
- [[founder/sessions/2026-03-18-weather-alpha-dashboard-redesign]]
