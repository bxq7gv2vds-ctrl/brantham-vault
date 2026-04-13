---
name: Polymarket COLDMATH_NO — Negative EV Analysis
type: pattern
project: polymarket-hedge
tags: [polymarket, coldmath, ev-analysis, trading, warning]
date: 2026-04-11
---

# Pattern : COLDMATH_NO est structurellement -EV

## Le problème

Acheter des tokens NO sur des bins "improbables" (P_NWP < 5%) semble attractif en surface :
- Win rate apparent : 97% (3 pertes sur 100)
- Apparence : "presque toujours gagnant"

## La math qui détruit la thèse

```
Acheter NO à prix P_NO = 1 - P_YES_market
  → Win: +P_YES_market par share
  → Lose: -P_NO par share = -(1 - P_YES_market)

Breakeven WR = P_NO / (P_NO + P_YES_market) = P_NO / 1 = P_NO

Exemple COLDMATH_NO AA :
  P_YES_market = 0.01 (1%) → P_NO = 0.99
  Breakeven WR = 99.0%
  WR réel du modèle NWP : ~97%
  → Net EV par trade = -2% de la mise
```

## Résultats empiriques (6551 trades papier)

```
Tier AA  (P_YES < 0.001, NO ≥ 0.97): 3039 trades | WR 97.0% | -$18,005
Tier AAA (P_YES = 0.0,  NO ≥ 0.98):  572 trades  | WR 97.4% | -$8,201
Tier A   (P_YES < 0.005, NO ≥ 0.96): 808 trades  | WR 95.4% | -$3,834
Tier BBB (P_YES < 0.02):             1116 trades  | WR 90.0% | -$3,754
Total COLDMATH_NO                                              -$33,794
```

## Pourquoi le WR NWP ne suffit jamais

Le WR de 97% semble excellent mais ne dépasse jamais le seuil de breakeven :
- AA tier (NO @ 0.991) : besoin 99.1% WR, a 97% → -$59/trade sur $1000
- AAA tier (NO @ 0.993) : besoin 99.3% WR, a 97.4% → -$40/trade sur $2000

Le seul cas où on dépasse 99% WR : **certitude physique absolue** (oracle CONFIRMED).

## Ce qui fonctionne à la place

```
Tier B (SPEEDA_EARLY + CERT_NO + cheap YES): 1000 trades | WR 68.8% | +$22,097

Pourquoi B gagne malgré 68.8% WR ?
  → Achète YES à 0.5-5% → win payout x20-200
  → Les wins compensent largement les pertes
  → EV = 0.688 × 95% + 0.312 × (-100%) ≈ +34% par trade
```

## Règle à retenir

> Pour tout trade "acheter un token cher" (NO à 0.95+) :
> Le WR requis = le prix du token. Si modèle NWP < ce WR, c'est -EV.
> Seule exception : certitude physique (CONFIRMED oracle, CERT_NO).

## Application dans le code

```python
# run_bracket_scalper.py — ScalpConfig
disable_coldmath_no: bool = True   # défaut: désactivé

# Pour l'activer (monitoring uniquement) :
# uv run scripts/run_bracket_scalper.py --coldmath-no
```

## Related

- [[_system/MOC-patterns]]
- [[founder/sessions/2026-04-11-polymarket-coldmath-diagnosis]]
- [[patterns/polymarket-oracle-confirmed-backtest]]
- [[patterns/polymarket-bracket-arb]]
