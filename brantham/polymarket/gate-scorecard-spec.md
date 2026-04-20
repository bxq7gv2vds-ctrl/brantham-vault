---
name: Gate Scorecard — Spec critères
description: Spécification formelle des critères quantitatifs pour chaque stage gate G1→G5 du déploiement Polymarket weather. Référence pour gate_scorecard.py.
type: spec
created: 2026-04-20
updated: 2026-04-20
priority: high
tags: [polymarket, spec, stage-gates, scorecard, validation]
---

# Gate Scorecard — Spec critères

Spec formelle des seuils et sources data pour chaque gate. Implémenté par `scripts/gate_scorecard.py` (livrable E1 du [[g1-g2-qualification-kit]]).

## G1 — Research Validation

Un signal PASS G1 est **statistiquement défendable** contre le data mining bias.

| Critère | Seuil | Source data | Formule / méthode |
|---|---|---|---|
| **DSR (Deflated Sharpe)** | `>= 1.5` | `signal_outcomes` + `research/hypotheses.jsonl` | Bailey & Lopez de Prado 2014. `SR_deflated = (SR_obs - E[max SR]) / sqrt(Var)` |
| **PBO (Probability of Backtest Overfitting)** | `<= 20%` | split combinatoire `signal_outcomes` | Lopez de Prado. Combinatorial symmetric CV, measure rank degradation OOS |
| **Economic thesis validated** | user flag `THESIS VALIDATED` | `vault/.../economic-thesis.md` | Grep sentinel string |
| **N_hypotheses logged** | `>= 5` | `research/hypotheses.jsonl` | Count rows (pour DSR correction) |
| **Failure modes catalog** | `>= 8 items` | `vault/.../failure-modes.md` | Count `## Mode` sections |
| **Strategy lifecycle defined** | present | `vault/.../strategy-lifecycle.md` | Grep sentinel `LIFECYCLE READY` |
| **SHAP top-3 feature stability** | `>= 70%` | `xgb_station_*.json` + walk-forward SHAP | Kendall tau entre top-3 ranks sur fenêtres rolling 60j |
| **Alpha decay half-life** | `>= 5 days` | `signal_outcomes` + TTR | Exponential fit `edge(ttr) = edge_0 * exp(-ttr/tau)` |
| **Leakage detected** | `no` | feature → target_date timing check | Scan : aucune feature n'utilise data post target_date |
| **TC model calibrated** | `yes` | `tc_model.py` + `slippage_ema` | Spread + gas + impact + adverse selection tous calibrés avec N >= 50 fills |
| **Capacity at 5% edge loss** | `>= $2,000` | `capacity_curve.py` output | Bankroll où realized edge = 0.95 × paper edge |
| **Factor max exposure** | `<= 30%` bankroll | `factor_exposure.py` daily snap | Max(exposure[factor]) / total bankroll |
| **Correlation drift KS** | `p > 0.05` rolling 30j | `correlation_drift.py` | KS test entre corr matrix semaine N vs semaine N-1 |

**Exit action G1 PASS** : proceed to G2 paper shadow 30 jours avec strat **verrouillée** (no retraining, no feature change).

## G2 — Paper Shadow

Strat verrouillée tourne 30-90 jours en paper. Comparaison live vs backtest.

| Critère | Seuil | Source |
|---|---|---|
| Durée shadow | `>= 30 jours` continu | `signal_outcomes` timestamp |
| Réalisé WR vs backtest | `\|live - backtest\| <= 1 sigma` | t-test paired |
| Réalisé Sharpe vs backtest | `\|live - backtest\| <= 1 sigma` | idem |
| Alpha decay observé | `within 20% of predicted` | `alpha_decay.py` compare predicted vs realized |
| Zero kill-switch déclenchement spurieux | `kill_switch_triggers <= 2 in 30d` | `alpha_states` changes |
| Data freshness uptime | `>= 99%` | `data_freshness` table |

**Exit action G2 PASS** : proceed to G3 pilot avec bankroll `min($500, 10% × capacity)`.

## G3 — Pilot

Small real capital. Objectif : execution quality.

| Critère | Seuil |
|---|---|
| Bankroll initial | `$500-$2000` |
| Implementation shortfall | `<= 1.5 × expected slippage` |
| Fill rate | `>= 80%` orders within 60s |
| Zero operational incident unresolved | `0` |
| Playbook runbook executed | `>= 1 full cycle` |

**Exit action G3 PASS** : scale to $2k → $10k ($10k only after 30d at $2k avec Sharpe rolling 60j > 1.5).

## G4 — Scale

| Critère | Seuil |
|---|---|
| Sharpe 60j rolling | `> 1.5` à chaque palier |
| Max DD | `< 10%` bankroll |
| Capacity headroom | `> 2x current bankroll` |
| Factor max exposure | `< 25%` (plus strict à la scale) |

## G5 — Production

| Critère | Seuil |
|---|---|
| Durée en prod | `>= 180 jours` |
| Correlation avec autres strats du book | `< 0.3` |
| DSR updated mensuel | `> 1.3` rolling 12m |
| Strategy registered in book | `yes` |

## Failure modes de gate

**Si un critère FAIL** : scorecard bloque transition et pointe l'action correctrice :

- `DSR < 1.5` → "Trop de variantes testées. Soit log toutes dans hypotheses.jsonl, soit restreindre scope. DSR factor = sqrt(log(N_trials))."
- `PBO > 20%` → "Risque overfit élevé. Run `purged_kfold_eval.py --embargo 72h` et checker stability."
- `SHAP stability < 70%` → "Features instable dans le temps. Candidate retrait : `{feature_x}`."
- `Alpha decay < 5d` → "Edge trop court-lived pour capacity visée. Restreindre TTR bucket."
- `Leakage detected` → "Feature `{feature_name}` utilise data post target_date. Fix immediate."
- `Capacity < $2,000` → "Strat trop fine pour scale. Restreindre aux markets volume >= $5k/day."
- `Factor max exposure > 30%` → "Concentration facteur `{factor}`. Enforce size cap."

## Output format canonique

```
============================================================
POLYMARKET WEATHER ALPHA — GATE SCORECARD
Date: 2026-04-20 09:30:00 CEST
Evaluating: G1 Research Validation
============================================================

[A] Statistical Validation
  DSR (adjusted for N_trials=12) ............. 1.87  PASS
  PBO ........................................ 12%   PASS

[B] Research Governance
  Economic thesis validated .................. yes   PASS
  Failure modes cataloged (>=8) .............. 11    PASS
  Strategy lifecycle defined ................. yes   PASS
  N_hypotheses logged ........................ 12    PASS

[C] Model Robustness
  SHAP top-3 stability ....................... 89%   PASS
  Alpha decay half-life ...................... 9.2d  PASS
  Leakage detected ........................... no    PASS

[D] Execution Readiness
  TC model calibrated ........................ yes   PASS
  Capacity at 5% edge loss ................... $4.2k PASS
  Factor max exposure ........................ 22%   PASS
  Correlation drift KS p-value ............... 0.31  PASS

============================================================
G1 VERDICT: PASS (13/13 criteria)
============================================================
Next action: proceed to G2 (lock strategy, start 30-day paper shadow)
Estimated G2 completion: 2026-05-20
```

## Related

- [[g1-g2-qualification-kit|Framework master]]
- [[g1-g2-todo-tracker|Execution tracker]]
- [[economic-thesis|Economic thesis]]
- [[failure-modes|Failure modes catalog]]
- [[strategy-lifecycle|Strategy lifecycle]]
- [[STATE-HANDOFF]]
- [[_MOC|Polymarket Hub]]
