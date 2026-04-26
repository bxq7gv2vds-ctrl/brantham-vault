---
name: Bracket pricer observation-based
description: Heuristique simple pricer pour brackets weather Polymarket basée uniquement sur METAR observation + diurnal climato piecewise. Validé AUC>0.7 sur 30j historique sans ML.
type: pattern
project: brantham/polymarket
created: 2026-04-26
status: validated
tags: [polymarket, pattern, pricer, obs-based]
---

# Bracket pricer — observation-based

## Concept

Pour pricer un bracket weather "T_max in {city} on {date} ∈ [lo, hi]"
en cours de journée, **les observations METAR + une climato diurnale
piecewise suffisent** pour atteindre AUC > 0.7. Pas besoin de NWP
sophistiqué (Pangu, EMOS, BMA, XGBoost) pour le baseline.

## Algorithme

1. **T_max_so_far** = max(temp_c) observé depuis minuit local
2. **Diurnal state** par heure locale :
   - ≥17h : post_peak (delta=0, sigma=0.4)
   - 14-17h : near_peak (delta=0.3, sigma=0.7)
   - 10-14h : pre_peak (delta=(15-h)*0.9, sigma=1.4)
   - 6-10h : morning (delta=8.0, sigma=2.5)
   - <6h : predawn (delta=10, sigma=3.0)
3. **mu = T_max_so_far + delta_c**, **sigma = climato sigma**
4. **Floor** : T_max_final ≥ T_max_so_far. Brackets entièrement sous → P=0
5. **P(bracket) = Φ((hi-mu)/σ) - Φ(max(lo, T_max_so_far)-mu)/σ)**

## Performance empirique (30 jours, 46 stations)

| Pricing cutoff | AUC ROC | Brier score | Régime |
|---|---:|---:|---|
| T-2h (22h local) | **0.9944** | 0.031 | post_peak |
| T-8h (16h local) | **0.9610** | 0.044 | near_peak |
| T-14h (10h local) | **0.7035** | 0.073 | pre_peak |

Backtest : 1373 (station × day) × 13 brackets ±6°C autour de T_max
réalisé = 17,849 obs. 7.7% positive (un seul bracket gagne par jour).

**Tous les régimes passent le gate AUC ≥ 0.65 fixé dans la stratégie.**

## Quand utiliser

- Pricing live brackets en TTR < 14h (pre_peak ou plus tard)
- Edge prouvé empiriquement par reverse engineering top winners
  (cf [[brantham/polymarket/reverse-engineer-true-winners]])
- Baseline avant tout effort ML — gate de discipline anti-feature-creep

## Quand NE PAS utiliser

- TTR > 14h (pre-dawn / overnight) : sigma trop large, edge faible
- Brackets multi-jours (markets weekly) : le pricer est calé sur 1 calendar day
- Markets non-temperature (precipitation, snow) : algorithme à adapter

## Limites connues

- Climato piecewise hardcodée — pas de saisonnalité, pas de différenciation par ville
- Sigma constants — devrait scaler avec saison et latitude
- Pas de prise en compte des prévisions courte échéance (radar, satellite)
- Floor strict T_max_final ≥ T_max_so_far — ignore correctness errors METAR

## Code

- Module : `src/pmhedge/alpha/bracket_pricer_obs.py`
- Backtest : `scripts/backtest_bracket_pricer_obs.py`
- Functions principales : `price_bracket()`, `get_obs_state()`, `_diurnal_state()`

## Évolutions futures (gated, ne pas implémenter avant W2 paper passé)

1. Climato per-city per-month (extraire de obs historique 6+ mois)
2. Sigma adaptive selon obs density / variance récente
3. Wire dans live_executor avec edge filter `|p_obs - market_yes| > 5%`
4. Comparison vs marché pour identifier mispricings
5. ML calibration **uniquement si** baseline plateau et plafond AUC

## Related

- [[brantham/polymarket/strategy-2026-04-26]] — strategy parent (W1.2 completed)
- [[brantham/polymarket/reverse-engineer-true-winners]] — preuve empirique
- [[_system/MOC-patterns]]
- [[brantham/_MOC]]
