---
name: Quant Deep Dive — Actions appliquées au modèle
description: Modifications concrètes apportées au stack Polymarket suite aux findings du quant deep dive 38 villes (2026-04-23). DB city_config updates + nouveau module regime quiet_bear.
type: action-log
project: brantham/polymarket
created: 2026-04-23
tags: [polymarket, action, city-config, regime, quiet-bear, hedge-fund-grade]
priority: critical
---

# Quant Deep Dive — Actions appliquées (2026-04-23)

Suite aux findings du master quant deep dive (38 villes × 6 mois on-chain), modifications appliquées au stack live.

## A. DB updates `alpha_data_hub.city_config`

### A.1 Cities DISABLED (no edge identifiable)

| Ville | Avant | Après | Rationale |
|-------|-------|-------|-----------|
| **Moscow** | ENABLED kelly=0.05 | **DISABLED** | AUC ex-ante 0.51 (random), calibrated p>0.05, χ²=1.6, pas d'edge ex-ante exploitable |
| **Busan** | ENABLED kelly=0.10 | **DISABLED** | AUC 0.54, calibrated p>0.05, χ²=1.4, N=66 trop petit |

### A.2 Cities SHADOW (high vol regime, exposition limitée)

| Ville | Avant | Après | Rationale |
|-------|-------|-------|-----------|
| **Denver** | ENABLED kelly=0.50 | **SHADOW** | GARCH persistence 0.98, vol shocks durent 5-7 markets |
| **Los Angeles** | ENABLED kelly=0.50 | **SHADOW** | GARCH persistence 0.96, EV bracket-NO +15% mais vol explosive |

### A.3 Kelly réduit (bookies calibrated, edge limité)

Kelly 0.50 → **0.15** sur :

- Madrid, Singapore, Warsaw (early_error <0.05, calibrated p>0.05)
- Lucknow (AUC 0.89 mais best EV +22% seulement)
- Mexico City (déjà DISABLED, kelly mis à 0.15 pour cohérence si ré-activé)
- Wuhan, Chengdu (calibrated, χ²<5)
- Tel Aviv (oligopole HHI=0.124, exposition limitée)

### A.4 Kelly boost (mal calibrées + edge potentiel élevé)

Kelly 0.25 → **0.40** sur :

- **London** (χ²=121.2, buy_no_favorites EV +3939% N=12)
- **Atlanta** (χ²=54.9, EV +2129% N=18)
- **Toronto** (χ²=70.5, EV +2410% N=13)

⚠️ N petits (12-18) — Kelly 0.40 est aggressive. Monitoring recommandé : si après 30j live le WR observé décroche de WR historique (66.7%) > 20pp, redescendre à 0.25.

### A.5 Cities laissées telles quelles

- **New York** : déjà SHADOW par city_optimizer (N=66 WR=95.5%) — cohérent avec finding χ²=102.5
- **Buenos Aires** : déjà DISABLED — finding suggérerait BOOST mais override conservatif
- **Mexico City** : déjà DISABLED ✓

## B. Nouveau module `quiet_bear_filter.py`

**Path** : `src/pmhedge/alpha/quiet_bear_filter.py`

### Règle

Sur Shanghai et Tel Aviv, si la volatilité réalisée d'un market <0.015pp :

- **BUY NO** → boost size ×1.5
- **BUY YES** → reject (size_mult = 0.0)

### Justification

Quant deep dive a identifié sur 6 mois on-chain :
- Shanghai : 185 markets en régime "Quiet Bear" (vol<0.015) → WR_YES = 0% absolu
- Tel Aviv : 203 markets idem → WR_YES = 0%

→ Quand le marché reste calme sur ces villes, NO est structurellement certain. Bookies laissent le market quiet car NO n'est pas contesté.

### Statut

**Module prêt** mais **NON wired** dans `signal_generator.py` pour l'instant (besoin de validation que le calcul de vol récente est fiable au moment du signal).

### Test unitaire

```python
from pmhedge.alpha.quiet_bear_filter import quiet_bear_adjustment

# Shanghai NO + vol low → boost ×1.5
quiet_bear_adjustment('shanghai', 'NO', 0.010)
# → QuietBearDecision(is_quiet_bear=True, size_mult=1.5)

# Shanghai YES + vol low → reject
quiet_bear_adjustment('shanghai', 'YES', 0.010)
# → QuietBearDecision(is_quiet_bear=True, size_mult=0.0)

# Tel Aviv NO + vol high → passthrough
quiet_bear_adjustment('tel aviv', 'NO', 0.030)
# → QuietBearDecision(is_quiet_bear=False, size_mult=1.0)

# London → passthrough (pas dans set)
quiet_bear_adjustment('london', 'NO', 0.005)
# → QuietBearDecision(is_quiet_bear=False, size_mult=1.0)
```

✓ Tous tests passent.

### Wire-in proposé

Dans `signal_generator.py` après le `regime_mult`, avant le calcul de `size_usdc` :

```python
# Quiet Bear filter — Shanghai/Tel Aviv WR_YES=0% en régime low-vol
from pmhedge.alpha.quiet_bear_filter import quiet_bear_adjustment
recent_vol_pp = _compute_recent_vol(market.token_id)  # à implémenter
qb = quiet_bear_adjustment(city_slug, side, recent_vol_pp)
if qb.size_mult == 0.0:
    return None  # reject signal
quiet_bear_mult = qb.size_mult
# Multiplier dans la formule de sizing :
raw = cfg.bankroll * city_cfg.kelly_fraction * regime_mult * bandit_w * quiet_bear_mult * max(0.0, kelly)
```

## C. Findings non actionnés (pourquoi)

### Pourquoi pas wirer `buy_no_favorites` comme nouvelle alpha ?

EV +3939% London / +2237% NYC mais N=12 chacun sur 6 mois = ~2 trades/mois. Trop peu pour stat reliable. Recommandation : faire **30j paper SHADOW** d'abord avec un module séparé `alpha/favorite_no.py` qui scope strictement à open_price >0.85, validate avec N>30 nouveaux trades, puis activer.

### Pourquoi pas Hong Kong calibration adjustment ?

Finding : HK seul Asian mal calibré + GARCH 0.855. Requiert un module de re-calibration spécifique sur bins 0.1-0.3. Refit complexe, à faire dans l'itération suivante via `train_city_calibrators.py --city hong-kong --boost-bins 0.1 0.3`.

### Pourquoi pas Istanbul/Madrid tail froids sous-pricés ?

Finding : Bookies sous-pricent les YES tails extrêmes (≤0.02) sur Istanbul/Madrid (oscillations arctiques NAO non intégrées). Activable via `tail_filter.py` reverse-mode. Non fait car notre `tail_filter` actuel reject ces tails (par défaut conservateur). Inverser pour ces 2 villes nécessite override targeté.

## D. Rollback (si besoin)

```sql
-- Revert DB updates
UPDATE city_config SET status='ENABLED', kelly_fraction=0.05, notes=NULL,
       updated_ts=strftime('%s','now')
WHERE city_slug IN ('moscow', 'busan');

UPDATE city_config SET status='ENABLED', kelly_fraction=0.50, notes=NULL,
       updated_ts=strftime('%s','now')
WHERE city_slug IN ('denver', 'los angeles');

UPDATE city_config SET kelly_fraction=0.50, notes=NULL,
       updated_ts=strftime('%s','now')
WHERE notes LIKE '%2026-04-23%' AND status = 'ENABLED';
```

## E. Monitoring à mettre en place

1. **Post-action 7j** : check P&L par ville pour les 5 villes boostées (London, Atlanta, Toronto, NYC, BA)
2. **Post-action 30j** : recompute `quant_deep_dive` cycle complet et comparer drift de χ², AUC
3. **Quiet Bear validation** : dès le wire-in, log `quiet_bear_decision` séparément et tracker WR observé sur Shanghai/TA pour valider le 0% historique tient
4. **Auto-rollback trigger** : si WR_observé < 50% sur les villes boostées sur 30 nouveaux signals, automatic kelly reduce via `city_optimizer.py`

## Related

- [[_MOC|Quant Deep Dive Master MOC]]
- [[../odds-trajectories-v2-findings|Odds Trajectories v2 (global)]]
- [[../STATE-HANDOFF|State Handoff]]
- [[../city-optimization|City optimization log]]
- [[../tier-s-v2-hedge-fund-gates|Tier S v2 gates]]
- [[../ARCHITECTURE|Architecture map]]
