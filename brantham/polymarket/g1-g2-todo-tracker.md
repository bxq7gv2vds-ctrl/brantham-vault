---
name: G1→G2 Todo Tracker
description: Tracker d'exécution des 16 livrables du Qualification Kit. Source de vérité pour l'état d'avancement. Survive context clear.
type: todo
created: 2026-04-20
updated: 2026-04-20
priority: critical
tags: [polymarket, todo, tracker, execution, qualification-kit]
---

# G1→G2 Todo Tracker

Tracker d'exécution détaillée des 16 livrables du [[g1-g2-qualification-kit]]. Chaque livrable a : ID, status, path attendu, commande de vérification, dépendances.

## Convention status

- `pending` — non commencé
- `in_progress` — en cours (1 max à la fois si sprint courant)
- `done` — livré + vérifié via commande check
- `blocked` — attente externe (user, API, data)
- `skipped` — déscopé avec raison

## Sprint 1 — Research Governance (4h)

| ID | Livrable | Path | Status | Check |
|---|---|---|---|---|
| B1 | Economic thesis draft | `vault/brantham/polymarket/economic-thesis.md` | `done` (DRAFT) → blocked (user review) | `grep -q "THESIS VALIDATED" vault/brantham/polymarket/economic-thesis.md` |
| B4 | Research log + wrapper | `research/hypotheses.jsonl` + `scripts/log_hypothesis.py` | `pending` | `test -f /Users/paul/polymarket-hedge/scripts/log_hypothesis.py && uv run scripts/log_hypothesis.py --list \| head -1` |
| B2 | Failure modes catalog | `vault/brantham/polymarket/failure-modes.md` | `done` (DRAFT) | `wc -l vault/brantham/polymarket/failure-modes.md` |
| B3 | Strategy lifecycle | `vault/brantham/polymarket/strategy-lifecycle.md` | `done` (DRAFT) | `wc -l vault/brantham/polymarket/strategy-lifecycle.md` |

## Sprint 2 — Validation Core & Robustness (10h)

| ID | Livrable | Path | Status | Dépend | Check |
|---|---|---|---|---|---|
| A1 | Deflated Sharpe Ratio | `scripts/deflated_sharpe.py` | `pending` | B4 | `KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/deflated_sharpe.py --dry-run` |
| A4 | Purged K-fold evaluator | `scripts/purged_kfold_eval.py` | `pending` | — | `uv run scripts/purged_kfold_eval.py --help` |
| C4 | SHAP feature stability | `scripts/shap_stability.py` | `pending` | — | `uv run scripts/shap_stability.py --station KLAX --dry-run` |
| C5 | Alpha decay by TTR | `scripts/alpha_decay.py` | `pending` | — | `uv run scripts/alpha_decay.py --dry-run` |
| C6 | Leakage audit | `scripts/leakage_audit.py` | `pending` | — | `uv run scripts/leakage_audit.py` |
| C10 | NWP disagreement feature | `src/pmhedge/alpha/feature_engineering.py` extend | `pending` | — | `grep -q "nwp_disagreement_pct" src/pmhedge/alpha/feature_engineering.py` |

## Sprint 3 — Execution & Risk & Monitoring (7h)

| ID | Livrable | Path | Status | Dépend | Check |
|---|---|---|---|---|---|
| C7 | Transaction cost model | `src/pmhedge/alpha/tc_model.py` + `scripts/transaction_cost_model.py` | `pending` | — | `uv run scripts/transaction_cost_model.py --sample 10` |
| A2 | Capacity curve | `scripts/capacity_curve.py` | `pending` | C7 | `uv run scripts/capacity_curve.py --dry-run` |
| C8 | Correlation drift monitor | `scripts/correlation_drift.py` | `pending` | — | `uv run scripts/correlation_drift.py --dry-run` |
| C9 | Regime transition hazard | `scripts/regime_transition_risk.py` | `pending` | — | `uv run scripts/regime_transition_risk.py --dry-run` |
| A3 | Factor exposure | `scripts/factor_exposure.py` | `pending` | C8, C9 | `uv run scripts/factor_exposure.py --dry-run` |
| E1 | Gate scorecard | `scripts/gate_scorecard.py` | `pending` | tous | `uv run scripts/gate_scorecard.py --gate G1` |
| E2 | Launchd + Telegram digest | `launchd/com.paul.polymarket-alpha-gate-scorecard.plist` | `pending` | E1 | `launchctl list \| grep gate-scorecard` |

## Quick progress check (reprise session)

```bash
cd /Users/paul/polymarket-hedge

# Status package A
for f in scripts/deflated_sharpe.py scripts/purged_kfold_eval.py scripts/capacity_curve.py scripts/factor_exposure.py; do
  test -f "$f" && echo "OK  $f" || echo "TODO $f"
done

# Status package C model robustness
for f in scripts/shap_stability.py scripts/alpha_decay.py scripts/leakage_audit.py; do
  test -f "$f" && echo "OK  $f" || echo "TODO $f"
done

# Status package D execution
for f in src/pmhedge/alpha/tc_model.py scripts/transaction_cost_model.py scripts/correlation_drift.py scripts/regime_transition_risk.py; do
  test -f "$f" && echo "OK  $f" || echo "TODO $f"
done

# Status package E monitoring
test -f scripts/gate_scorecard.py && echo "OK  gate_scorecard" || echo "TODO gate_scorecard"
launchctl list | grep -q polymarket-alpha-gate-scorecard && echo "OK  launchd" || echo "TODO launchd"

# NWP disagreement feature
grep -q "nwp_disagreement_pct" src/pmhedge/alpha/feature_engineering.py && echo "OK  disagreement feature" || echo "TODO feature"
```

## Gate Exit G1 — critères à PASS

Format output `gate_scorecard.py --gate G1` attendu :

```
G1 Research Validation — Status: PASS/FAIL

[A] Statistical Validation
  DSR adjusted >= 1.5        : [value] [PASS/FAIL]
  PBO <= 20%                  : [value] [PASS/FAIL]

[B] Research Governance
  Economic thesis validated   : [yes/no]
  Failure modes catalog       : [n items]
  Strategy lifecycle defined  : [yes/no]
  N_hypotheses logged         : [n]

[C] Model Robustness
  SHAP top-3 stability >= 70% : [value] [PASS/FAIL]
  Alpha decay half-life >= 5d : [value] [PASS/FAIL]
  No leakage                  : [yes/no] [PASS/FAIL]

[D] Execution Readiness
  TC model calibrated         : [yes/no]
  Capacity at 5% edge loss    : [$value]
  Factor max exposure <= 30%  : [value] [PASS/FAIL]
  Correlation drift KS p>0.05 : [value] [PASS/FAIL]

G2 Ready: YES/NO
Next action: [proceed to paper shadow / fix criterion X]
```

## Estimations effort

| Sprint | Heures solo | Durée calendaire estimée |
|---|---|---|
| Sprint 1 | 4h | 1 session de 4h |
| Sprint 2 | 10h | 1-2 sessions |
| Sprint 3 | 7h | 1 session |
| **Total** | **~21h** | **2-3 sessions** |

## Reprise après context clear

1. Lire [[STATE-HANDOFF]]
2. Lire [[g1-g2-qualification-kit]] (framework)
3. Lire ce doc (tracker)
4. Run "Quick progress check" ci-dessus
5. Reprendre sur le 1er `TODO` trouvé

## Related

- [[g1-g2-qualification-kit|Framework master]]
- [[gate-scorecard-spec|Spec critères scorecard]]
- [[economic-thesis|Economic thesis — DRAFT]]
- [[failure-modes|Failure modes]]
- [[strategy-lifecycle|Strategy lifecycle]]
- [[STATE-HANDOFF|State Handoff — entrée session]]
- [[_MOC|Polymarket Hub MOC]]
- [[../../_system/MOC-master|Master MOC]]
