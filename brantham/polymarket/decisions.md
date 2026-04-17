---
name: Décisions architecturales Polymarket Hedge Fund
description: Log des décisions prises avec raisonnement et alternatives écartées
type: decisions
created: 2026-04-17
tags: [polymarket, decisions, architecture]
---

# Décisions Architecturales — Polymarket Hedge Fund

Log chronologique des décisions prises avec le raisonnement et les alternatives écartées.

## 2026-04-17 — Session kickoff

### D1 — Défensif (EdgeFilter) avant offensif (new alphas)
- **Décision** : Builder EdgeFilter en premier (pocket registry + Kelly) avant de chasser nouveaux alphas
- **Pourquoi** : bot actuel génère des signaux à -$2,500 (PROB_YES low-price). Bloquer les pertes avant d'ajouter des gains. Math : -1 perte vaut +1 gain.
- **Alternatives écartées** :
  - Chercher direct le "golden alpha" (ML/ensemble) : trop risqué sans nettoyer les pertes
  - Full refactor scanner existant : 2137 lignes, trop long pour ROI
- **Résultat** : +$1,669 delta (+269%) sur backtest $1k bankroll

### D2 — Module `alpha/` séparé du code existant
- **Décision** : Nouveau module `src/pmhedge/alpha/` plugin, pas refactor `scanner.py`
- **Pourquoi** : 
  - Permet parité research-prod (même code)
  - Non-intrusif sur le bot live existant
  - Plus facile à tester en isolation
  - Évolutif (nouveaux alphas ajoutables sans toucher l'existant)
- **Alternatives écartées** :
  - Refactor inline dans scanner.py (risque de casser live)
  - Fork complet (duplication)

### D3 — Open-Meteo comme primary NWP aggregator
- **Décision** : Utiliser Open-Meteo comme source principale (GFS + ICON + GEM + ECMWF blended)
- **Pourquoi** :
  - 139 ensemble members aggregated, API gratuite jusqu'à 10k req/jour
  - Pas besoin de parser GRIB2 (overhead CPU + complexité)
  - Abstraction ensemble déjà faite
- **Alternatives écartées** :
  - Direct NOAA NOMADS GRIB parsing : complexe, lent
  - ECMWF CDS API : quotas restrictifs pour temps réel
- **Complément** : HRRR (US) + ICON-EU + AROME via Open-Meteo modèles spécifiques

### D4 — SQLite pour data hub
- **Décision** : Utiliser SQLite pour data_hub.db
- **Pourquoi** :
  - Déjà pattern dans le projet (bracket_scalper_trades.db, pmhedge.db)
  - Performance suffisante pour 50k+ obs/jour × 40 stations
  - Pas de déploiement serveur DB
  - Backup simple (copy file)
- **Alternatives écartées** :
  - PostgreSQL : overkill, besoins petit volume
  - TimescaleDB : overkill, pas de grosses queries temporelles
  - Parquet files : moins flexible pour queries ponctuelles

### D5 — Python asyncio, pas Rust/Go pour execution
- **Décision** : Rester sur Python avec asyncio + aiohttp pour execution
- **Pourquoi** :
  - Volume actuel : <10 trades/min → latency 500ms OK
  - Pas de bataille contre HFT (Polymarket moins compétitif que equity markets)
  - Stack unifié Python = moins de bugs boundary
- **Alternatives écartées** :
  - Rust/Go order engine : overkill + dual-language complexity
  - À reconsidérer si volume dépasse 100 trades/min

### D6 — Kelly fractional 25-50% (pas full Kelly)
- **Décision** : Kelly fraction entre 0.25 et 0.50 selon confidence du pocket
- **Pourquoi** :
  - Full Kelly = maximise log return mais variance insupportable
  - 1/4 Kelly = 1/4 return mais 1/16 variance (meilleur risk-adjusted)
  - Edge stats sont noisy → prudence
- **Alternatives écartées** :
  - Full Kelly : ruin risk réel
  - Fixed sizing : ignore edge magnitude

### D7 — Kelly correlation-adjusted obligatoire
- **Décision** : Portfolio manager doit réduire sizing si signaux corrélés
- **Pourquoi** :
  - 10 signaux sur villes corrélées = 1 signal réel
  - Non-correction = over-leverage caché
  - Covariance depuis data historique (rolling 30j)
- **Alternatives écartées** :
  - Kelly naïf par signal : sous-estime variance portfolio

### D8 — Paper shadow 30 jours minimum avant real money
- **Décision** : 30 jours paper live shadow avant deploy capital
- **Pourquoi** :
  - Backtest = optimiste (slippage, rejects non modélisés parfaitement)
  - Live market can shift regime
  - Détecte bugs d'intégration
- **Alternatives écartées** :
  - 7 jours : pas assez pour détecter regime shifts
  - Saut direct live small : risque ruine sur bug execution

### D9 — Walk-forward purged K-fold pour backtest
- **Décision** : Walk-forward rolling + purged (Lopez de Prado) obligatoire
- **Pourquoi** :
  - In-sample backtest = fausses sécurités (overfitting)
  - Walk-forward = test réaliste
  - Purged K-fold évite label leakage temporel
- **Alternatives écartées** :
  - In-sample backtest : biais optimiste

### D10 — EMOS + BMA + XGBoost stack ML (pas neural d'abord)
- **Décision** : Commencer par EMOS + BMA + XGBoost, DRN/transformer plus tard
- **Pourquoi** :
  - EMOS = baseline bien connu, robuste
  - XGBoost = 80% de la perf avec 20% de complexité
  - DRN/transformer = +5-10% perf mais +10x complexité
  - Suivre principe "MVP beats perfection"
- **Alternatives écartées** :
  - Direct DRN : risque de debug long
  - Foundation models (Pangu/GraphCast) : overkill pour station T_max

### D11 — Polymarket CLOB WebSocket (pas Gamma API pour execution)
- **Décision** : Utiliser CLOB WebSocket pour orderbook et execution
- **Pourquoi** :
  - Gamma API = metadata, trop lent pour execution
  - CLOB = source of truth + L2 depth
  - WebSocket = real-time vs polling
- **Alternatives écartées** :
  - Gamma polling : trop lent, slippage réel mal estimé

### D12 — Vault Obsidian pour knowledge + décisions
- **Décision** : Documenter TOUT dans `vault/brantham/polymarket/`
- **Pourquoi** :
  - Mémoire persistante entre sessions
  - Graph de connaissances cross-linked
  - Findings archivés pour référence future
  - Accountability (décisions tracées)
- **Alternatives écartées** :
  - README.md dans repo : dispersé, pas cross-linked

### D13 — Vault section dédiée polymarket (nouveau folder)
- **Décision** : Créer `vault/brantham/polymarket/` séparé, pas diluer dans brantham général
- **Pourquoi** :
  - Projet large, mérite son MOC dédié
  - Pas confondre avec M&A / internal-tool
  - Permet évolution indépendante
- **Alternatives écartées** :
  - Mixer dans brantham/patterns : pollue le pattern library

### D14 — Pas de market making en Phase 1
- **Décision** : Market making reporté Phase 2+
- **Pourquoi** :
  - Besoin inventory management robuste (complexe)
  - Rebates 0.02% sur Polymarket → petit gain vs alpha de model
  - Focus d'abord : alpha durable
- **Alternatives écartées** :
  - MM d'emblée : complexity overhead trop tôt

### D15 — Sum-to-1 arb en Phase 3 (pas 1)
- **Décision** : Sum-arb après CLOB orderbook live, pas avant
- **Pourquoi** :
  - Besoin orderbook snapshot synchronisé (pas price_bars asynchrone)
  - price_bars historique insuffisant pour valider
  - Fill legging risk nécessite order manager mûr
- **Alternatives écartées** :
  - Sum-arb d'emblée avec price_bars : résultats non fiables (20k "opportunities" à 22% = fake)

## Related

- [[_MOC|Polymarket Hub]]
- [[architecture|Architecture détaillée]]
- [[roadmap|Roadmap avec rationales]]
- [[questions|Framework questions]]
