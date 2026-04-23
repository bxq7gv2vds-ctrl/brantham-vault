---
title: Risks & Mitigations
created: 2026-04-23
parent: [[_MOC]]
tags: [risks, mitigations]
---

# Risks identifiés & mitigations

## 10 pièges mathématiques / opérationnels

| # | Risque | Impact | Mitigation |
|---|---|---|---|
| 1 | **Pin risk aux bornes** | Gamma diverge, hedge instable, fair value bouge violemment | Skip si \|S-K\| < 0.5 σ √T |
| 2 | **Smile dynamics** (sticky-strike vs sticky-delta) | Hedge correct à t=0 wrong à t=Δt | Recalibrer smile chaque 60s |
| 3 | **Vol of vol (vega jump)** | Sur news/FOMC, IV explose, P&L bouge | Hedge vega via long straddle Deribit + size limit J-2 events |
| 4 | **Settlement basis risk** Polymarket Chainlink vs Deribit index | Spread peut spike en stress | Hedge via Hyperliquid perp (basis ≈ 0 continu) |
| 5 | **Adverse selection** retail vs informed | Tes signaux "forts" = peut-être que quelqu'un sait quelque chose | Whale detection, news filter, size-down |
| 6 | **Latency edge decay** | Edge 5% à t=0 → 2% à t=5s (mais rebalance 60s assouplit) | Mesurer latency, decay size linéairement |
| 7 | **Funding rate ≠ drift sous Q** | Mauvais drift → biais systématique | μ = -funding × annualization (sign convention strict) |
| 8 | **Tail events** (crash 10% en 1min) | Hedge couvre 90% mais bracket pricing fucked | Hard kill-switch >2σ en 60s, close all |
| 9 | **Correlation BTC-ETH** (~0.75) | Diversification illusoire | Kelly multi-asset avec correlation shrinkage |
| 10 | **Vol scaling 5min depuis daily** | √T scaling assumes Brownian, faux intraday | Empirical intraday vol multiplier (à mesurer) |

## 7 façons dont la stratégie peut échouer (réalisme)

| # | Mode d'échec | Probabilité 12mo | Mitigation |
|---|---|---|---|
| 1 | L'edge n'existe pas en réalité (paper > live de 50%+) | 40% | Mesure live ratio strict, kill si <0.3 du paper |
| 2 | Autres bots arrivent et arbitrage l'edge | 30% | Suivre depth/spreads ; pivot sur niches sous-couvertes |
| 3 | Polymarket change règles (fees, KYC, API limits) | 15% | Diversifier vers Kalshi, Manifold |
| 4 | Bug d'exécution (order calibré faux, hedge fail) | 20% | Tests unitaires + integration + paper trading 7j |
| 5 | Black swan crypto (crash 30% en 1h) | 5% | Kill-switch >2σ + emergency close all |
| 6 | Liquidité Polymarket s'effondre | 10% | Monitor volume, reduce size si depth <50% historical |
| 7 | Maintenance fatigue / abandon | 50% | Automatisation max, dashboard simple, reporting auto |

## Risk controls implémentés

### Position-level
- Pin risk filter : skip si gamma > seuil
- Edge threshold : ouvrir seulement si \|edge_net\| > 2pp
- Depth check : skip si bracket depth < $200
- Settlement source check : refuse si pas Chainlink/oracle confirmé

### Portfolio-level
- Per-position cap : 5% capital ($50 sur $1000)
- Total exposure cap : 80% capital ($800 sur $1000)
- Vega cap : limite l'exposition vol
- Gamma cap : limite l'exposition convexité
- Asset concentration : max 60% sur un seul asset (BTC ou ETH)

### Drawdown
- Soft DD -10% : reduce size 50%
- Hard DD -20% : close 50% positions, halt new
- Kill DD -30% : close all, halt 24h

### Operational
- Network heartbeat : kill si data stale >2min
- Order timeout : cancel après 30s sans fill
- Stale data check : refuse decisions sur smile fit > 5min old
- Manual override : kill-switch CLI command

## Patterns d'incident à anticiper

### Polymarket API rate limit
Symptôme : 429 errors → snapshot incomplet
Mitigation : exponential backoff, cache 60s, fallback sur subset

### Deribit WS disconnect
Symptôme : smile devient stale
Mitigation : auto-reconnect avec exponential backoff, mark smile stale, halt nouveau trade

### Hyperliquid hedge failure
Symptôme : delta drift sans hedge possible
Mitigation : fallback sur Bybit perp ; sinon emergency close Polymarket positions

### Settlement disputed
Symptôme : Polymarket position en attente résolution
Mitigation : marquer pending, exclure du portfolio Greeks live, attendre résolution

## Related

- [[_MOC]]
- [[math-pricing-hedge]]
- [[architecture]]
- [[../failure-modes]] — failure modes strat météo (référence)
