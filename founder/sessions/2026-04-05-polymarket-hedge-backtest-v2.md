---
tags: [session, polymarket, backtest, trading]
project: polymarket-hedge
date: 2026-04-05
---

# Session: Polymarket Hedge — Backtest V2

## Travaux effectués

### 1. Fix download_all_markets.py
- **Bug corrigé**: utilisait `gamma-api.polymarket.com/prices-history` → 404 sur tous les marchés
- **Fix**: changé vers `clob.polymarket.com/prices-history` avec token_id = clobTokenIds[0]
- **Résultat**: 55/55 marchés avec bars, 4301 bars téléchargés

### 2. Pagination historique
- **Ancien**: `public-search` limité à 5 events/query
- **Nouveau**: `events?tag_slug=weather` → 2568 events, 22131 marchés uniques
- **Couverture**: Jan 2024 → Avril 2026

### 3. Fix modèle de coûts (CRITIQUE)
**Deux bugs corrigés:**

a) **Fee**: était `0.02 * size_usdc * entry_price` → DOUBLE multiplication par prix
   - Corrigé: `fee_entry = 0.05 * size_usdc` (5% du USDC investi)
   - Source: Polymarket feeSchedule.rate=0.05, takerOnly=True

b) **Spread**: était `size_usdc / entry_price * 0.03` → créait 87 contrats × 0.03 = $2.61 de spread sur $10
   - Corrigé: `half_spread = entry_price * 0.05` (5% du prix)
   - Pour entry=0.115: spread total = $0.115 sur $10 investi ✓

c) **PnL formula**: était `size * (exit - entry)` → traitait size comme "contrats"
   - Corrigé: `n_ctrs = size_usdc / entry_price; gross_pnl = n_ctrs * (exit - entry)`
   - Pour $10 investi à 0.115: 87 contrats, PnL réel = 87 × delta ✓

### 4. Backtest results (backtest_data.db, US/UK cities)
| Param | Valeur |
|-------|--------|
| min_edge | 0.10 |
| buy_max | 0.15 |
| trade_size | $10 |
| Trades | 34 |
| Win rate net | 50% |
| Net PnL | +$88.22 |
| Profit factor | 1.86 |
| Avg win | +$11.19 |
| Avg loss | -$6.00 |

Exit breakdown: TP=16 (+$11.86 avg), SL=12 (-$7.31 avg), EXP=6 (-$2.30 avg)

**7/9 TP trades resolved NO → pure intraday play, pas de hold-to-resolution.**

### 5. Nouvelles villes (EMOS)
- Ajouté CITY_COORDS: Istanbul, Moscow, Mexico City, Busan
- EMOS calibré: Istanbul (732 records, 12 mois), Moscow (732 records)
- Busan, Mexico City: pas de données EMOS → fallback sigma=2.5

### 6. Live engine updates
- `gopfan_buy_max`: 0.12 → 0.15
- `min_edge`: 0.15 → 0.10
- `swing_min_edge`: 0.25 → 0.15

### 7. Download all_markets.db
- Lancé en background: 11167 marchés post-Mars 2026
- ~78k bars chargés (~2100/11167 au moment de la session)
- ETA: ~2h

## Diagnostics
- Asian markets (March 11): NWP miss → Seoul prédit 31.6% mais actual=7.9°C
- Sample size trop petit pour Asian cities → attendre download complet
- all_markets.db results non-concluants car données partielles

## Prochaines étapes
1. Re-run backtest complet une fois all_markets.db complété (~4h)
2. Tester paper trading mode
3. Analyser résultats Asian cities avec 45j de données

## Related
- [[_system/MOC-decisions]]
- [[patterns/polymarket-nwp-emos-calibration]]
- [[patterns/polymarket-intraday-architecture]]
