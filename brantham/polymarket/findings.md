---
name: Findings Polymarket — Diagnostics & Edges
description: Findings détaillés du diagnostic 2026-04-17 sur les 6,740 trades paper settled
type: findings
created: 2026-04-17
tags: [polymarket, diagnostic, edges]
---

# Findings — Diagnostic & Edges Détectés

Analyse rigoureuse des 6,740 trades paper settled dans `bracket_scalper_trades.db` (période 2026-04-05 → 2026-04-16, 10.5 jours).

## Vue d'ensemble — tous signal types (all time)

| Signal | N settled | WR | Total PnL | Avg win | Avg loss | Verdict |
|---|---|---|---|---|---|---|
| COLDMATH_NO | 5,845 | 99.4% | +$13,578 | $4.13 | -$280.59 | ✅ Rentable (volume principal) |
| CONVEX_YES | 122 | 0.8% | +$222.77 | $671.18 | -$3.71 | ⚠️ Lottery — 1/122 win |
| SPEEDA_YES | 2 | 100% | +$62.05 | $31.02 | - | ✅ Small volume |
| COLDMATH_YES | 25 | 100% | +$57.24 | $2.29 | - | ✅ Small |
| LONGSHOT_YES | 22 | 4.5% | +$36.36 | $1086.36 | -$50.00 | ⚠️ Lottery |
| PROB_NO | 433 | 68.4% | +$29.14 | $11.67 | -$25.00 | ~ Marginal |
| **CERT_NO** | 9 | 66.7% | -$29.47 | $45.09 | -$100.00 | ⚠️ Small, mixed |
| **EXACT_BIN_YES** | 29 | 65.5% | -$527.38 | $24.87 | -$100.00 | ❌ Asymmetry |
| **SPEEDA_EARLY** | 11 | 0% | -$550.00 | - | -$50.00 | ❌ Anti-edge |
| **PROB_YES** | 242 | 12.4% | -$2,801.47 | $83.28 | -$25.00 | ❌ Désastre |

## Edges rentables (edge réel vs breakeven)

Le **breakeven WR** d'un bet = `buy_price` (car payoff = 1/price - 1). Si WR observée > breakeven, edge positif.

| Pocket | N | WR | Breakeven | **Edge net** | PnL |
|---|---|---|---|---|---|
| **PROB_NO prix <0.70** | 178 | 70.2% | 62.8% | **+7.4 pts** | +$526 |
| **COLDMATH_NO 0.85-0.95** | 479 | 96.9% | 93.6% | **+3.3 pts** | +$2,050 |
| **EXACT_BIN_YES ≥0.95** | 16 | 100% | ~96% | +4 pts | +$108 |
| **COLDMATH_NO ≥0.95** | 5,366 | 99.6% | 98.5% | +1.1 pt | +$11,528 |

## Poches toxiques (anti-edge — à BLOQUER)

| Pocket | N | WR | Breakeven | Edge | PnL |
|---|---|---|---|---|---|
| PROB_YES prix <0.30 | 134 | 0.7% | 4.3% | -3.6 pts | -$2,502 |
| PROB_NO prix 0.70-0.85 | 239 | 69.0% | 74.5% | -5.5 pts | -$452 |
| EXACT_BIN_YES <0.30 | 10 | 10% | ~20% | -10 pts | -$582 |
| SPEEDA_EARLY (any) | 11 | 0% | ~20% | -20 pts | -$550 |

## Patterns critiques identifiés

### CONVEX_YES = lottery, pas daily P&L
- 122 trades à prix moyen $0.003 (lottery tickets)
- 1 seul win (Paris), porte +$652
- Incompatible avec objectif "daily gain accurate"
- **Verdict : DÉSACTIVER en mode scalping regulier**

### EXACT_BIN_YES = asymmetry dual
- 64% WR mais -$442 total
- Avg win $28 / avg loss $100 → ratio 1:3.5 → besoin 78% WR breakeven
- High-price (≥0.5) + Asie = 11/11 wins, +$452
- Low-price (<0.25) + US = 0/8, -$700
- **Verdict : filtrer à prix ≥0.85 uniquement**

### COLDMATH_NO = edge principal mais thin
- 5,845 trades → volume massif → stat significance
- WR 99.4% vs breakeven 98.1% → edge +1.3 pts
- Sur $300 avg size × 0.013 edge × 5845 trades = $22.8k théorique
- Observé +$13.5k → **47% capture** (reste = slippage réel)
- Concentré à TTR <1h : 5,689/5,845 trades
- **Sigma optimal 1-2°C** (WR 100%, +$7,357 sur 1,491 trades)
- **Verdict : réactiver avec filter comme garde-fou**

### PROB_NO = edge safest
- +7.4 pts edge → large marge de sécurité
- 178 trades validés → robuste
- Payoff symétrique (avg win $12 / avg loss $25) → ratio 1:2
- **Verdict : garder actif, augmenter sizing**

## Backtest filter v1 (2026-04-17)

Avec EdgeFilter + Kelly sizing sur bankroll $1k :

| Mode | N | WR | P&L | Sharpe | Max DD |
|---|---|---|---|---|---|
| Baseline (passthrough) | 1,599 | 81.9% | -$620 | -9.23 | -56.6% |
| **Filter + Kelly** | **1,540** | **97.1%** | **+$1,049** | **12.30** | **0%** |

**Δ = +$1,669 (+269%)**

Walk-forward OOS (4 windows) :
- Pooled N=16, PnL +$18.51, Sharpe 16.4
- Peu de data OOS (10.5 jours totaux) → validation limitée

## Bugs identifiés dans le bot actuel

1. **COLDMATH_NO désactivé depuis v4 (2026-04-14)** — edge principal perdu (memo dit -$33k mais data visible +$13.5k)
2. **CONFIRMED oracle n'a jamais triggered** — bug à investiguer (narrow window TTR<3.5h + METAR coverage ?)
3. **market_resolutions table VIDE** — pas de ground truth stored
4. **Pipeline data stale 12 jours** — all_markets.db last price_bar = 2026-04-05
5. **Size moyenne $300 incohérente** avec bankroll $1k — historique assumait $10k bankroll

## Edges découverts NON exploités

1. **Sum-to-1 arbitrage** (sur price_bars historique — 20k violations détectées mais nombres non fiables car pas orderbook snapshot)
2. **CONFIRMED oracle** (jamais triggered, edge ~100% WR potentiel)
3. **Orderbook microstructure** (pas accessible sans CLOB WebSocket)
4. **Nowcast <2h avec radar** (pas implémenté)
5. **ECMWF ensemble individuals** (51 members — pas accédés, seulement mean via Open-Meteo)

## Related

- [[_MOC|Polymarket Hub]]
- [[architecture|Architecture cible]]
- [[backtest-results/2026-04-17-baseline|Baseline backtest details]]
- [[sessions/2026-04-17-diagnostic-and-alpha-engine|Session log]]
