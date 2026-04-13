---
type: session
project: polymarket-hedge
date: 2026-04-11
tags: [polymarket, trading, coldmath, diagnosis, fix, oracle]
---

# Session 2026-04-11 — Diagnostic COLDMATH_NO + Fixes Infrastructure

## Ce qui s'est passé

### 1. Settlement 3420 trades bloqués

La DB `bracket_scalper_trades.db` avait 3,420 trades "open" avec `resolve_ts` déjà passé.
Cause : METAR API limite à 48h — les trades d'avril 5 (resolve_ts 6-10 avril) ne pouvaient pas être settlés.
**Fix** : script `scripts/settle_overdue.py` via Open-Meteo archive API.
PnL batch : -$23,539 (gros trades AA/AAA à $1000-2000 par position).

### 2. COLDMATH_NO = stratégie fondamentalement négative EV

**Le vrai P&L après settlement complet :**
```
Capital       : -$2,057 (départ $10,000 → -$12,057 PnL)
Trades résolus: 6,551 | WR: 91.3%

Tier B   (SPEEDA+CERT)   : 1000 trades | WR 68.8% | +$22,097  ← WINNER
Tier AA  (COLDMATH NO 97%): 3039 trades | WR 97.0% | -$18,005  ← KILLER
Tier AAA (COLDMATH NO 99%): 572 trades  | WR 97.4% | -$8,201   ← KILLER
Tier A                    : 808 trades  | WR 95.4% | -$3,834
Tier BBB                  : 1116 trades | WR 90.0% | -$3,754
```

**La math du problème :**
- Acheter NO à 0.99 → win +$0.01/share, lose $0.99/share
- Breakeven WR = 0.99 / (0.99 + 0.01) = 99.0%
- WR réel AA : 97% → perte nette à chaque trade
- Seul CONFIRMED (oracle 100% certitude) dépasse ce seuil

**Conclusion : COLDMATH_NO est structurellement -EV sauf si WR > 99%.**
La stratégie NWP ne donne pas 99% → toujours perdante à cette game.

### 3. Fix appliqué

`scripts/run_bracket_scalper.py` :
- Ajout flag `disable_coldmath_no: bool = True` dans ScalpConfig
- Check au début du Layer 2 (NWP path) ET du fallback market-only path
- CLI : `--coldmath-no` pour réactiver si besoin (monitoring seulement)

### 4. Infrastructure scanning rétablie

3 launchd jobs créés (persistent, survivent aux redémarrages) :
```
com.paul.polymarket-oracle-scan-0907  → 11:07 CEST (09:07 UTC) — CONFIRMED window
com.paul.polymarket-oracle-scan-1032  → 12:32 CEST (10:32 UTC) — scan secondaire
com.paul.polymarket-oracle-scan-1617  → 18:17 CEST (16:17 UTC) — Asian markets
```

### 5. CONFIRMED oracle signals : toujours pas déclenchés

Debug : METAR `t_max_prev_utc_day` est bien populé (Dallas April 10 UTC = 82.0°F).
Hypothèse : les scans d'aujourd'hui (11:34-11:40 UTC) se sont faits trop tard pour voir
les marchés US (peut-être déjà fermés ou TTR trop court).
**Test final demain 11:07 CEST** → premier scan dans la bonne fenêtre.
Signaux attendus : CONFIRMED_YES pour Dallas [82-83°F] + CONFIRMED_NO sur tous les autres bins.

## Signaux actuellement actifs (sans COLDMATH_NO)
- CERT_NO : contrainte physique (T_obs > bracket_hi) → near risk-free
- EXACT_BIN_YES : T_obs confirmé dans le bin après 16h local → buy YES cheap
- SPEEDA_EARLY : T_obs dans le bin, marché pas repriced → buy YES <5%
- CONFIRMED_YES/NO : oracle 09:07 UTC → CORE STRATEGY (jamais déclenché jusqu'ici)
- COLDMATH_YES : P_NWP > 85% + YES < 18% → rare mais positive EV

## Prochaines étapes

1. **Vérifier demain** : scanner.log à 11:07 CEST — CONFIRMED doit déclencher
2. **Deploiement live** : remplir `.env` PM_API_KEY / PM_SECRET / PM_PASSPHRASE
3. **Capital paper** : -$2,057. L'oracle CONFIRMED ($500/signal × 5-10/jour) peut rembourser en quelques jours si tout marche.
4. **settle_overdue.py** : à lancer périodiquement si METAR settlement échoue (marchés > 2 jours)

## Related

- [[_system/MOC-patterns]]
- [[founder/sessions/2026-04-08-polymarket-oracle-backtest]]
- [[founder/sessions/2026-04-05-polymarket-coldmath-strategy-complete]]
- [[patterns/polymarket-oracle-confirmed-backtest]]
- [[patterns/polymarket-bracket-arb]]
