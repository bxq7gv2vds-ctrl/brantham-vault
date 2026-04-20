---
name: G1→G2 Qualification Kit — Framework
description: Framework hedge-fund-grade pour qualifier la stratégie Polymarket weather de Gate 1 (research validation) à Gate 2 (paper shadow ready). 16 livrables groupés en 5 packages.
type: framework
created: 2026-04-20
updated: 2026-04-20
priority: critical
tags: [polymarket, framework, stage-gates, qualification, hedge-fund, validation]
---

# G1→G2 Qualification Kit — Framework

Document maître du plan qualifiant la stratégie Polymarket weather pour passer de **research validation (G1)** à **paper shadow ready (G2)**. Conçu pour survivre un context clear : ce doc seul permet à un nouveau Claude de reprendre sans perte.

## TL;DR

- **5 stage gates** pour déployer une strat (G0 hypothesis → G5 production). On est **G1 partiel**.
- **16 livrables** groupés en **5 packages cohérents** (A-E).
- **~21h solo autonome**, une seule review user requise (`economic-thesis.md`).
- **Gate exit** déterministe via `gate_scorecard.py` lancé quotidien.

## Stage Gate Framework

Convention d'un hedge fund institutionnel qui industrialise une alpha. Chaque gate a des critères quantifiés explicites.

| Gate | Objectif | Critères quantifiés | État actuel |
|---|---|---|---|
| **G0 — Hypothesis** | Thèse économique documentée | Source d'edge nommée · mécanisme de persistance · expiration théorique | **gap** — jamais écrit → [[economic-thesis]] |
| **G1 — Research Validation** | Signal statistiquement défendable | DSR ≥ 1.5 · PBO ≤ 20% · feature stability ≥ 70% · economic intuition cohérente · no leakage · alpha decay half-life ≥ 5d | **partiel** → Kit résout |
| **G2 — Paper Shadow** | Réalisé = backtest à 1σ | 30-90j strat verrouillée · alpha decay mesuré · capacity estimée · TC model validé | bloqué jusqu'à G1 exit |
| **G3 — Pilot** | Execution quality confirmée live | Small $ réel · IS < expected · fill ≥ 80% · playbook testé | bloqué user (wallet + py-clob-client) |
| **G4 — Scale** | Rentabilité stable | Paliers $500→$50k · Sharpe 60j > 1.5 · DD < 10% | — |
| **G5 — Production** | Strategy dans book | Capital alloc par risk budget · corr matrix avec autres strats | — |

## Panel — insights senior quant (condensé)

6 voix seniors ont challengé l'approche initiale. Insights retenus pour le kit :

- **Stats (Kim)** — DSR + PBO obligatoires avant de revendiquer un edge. N_trials comptés via [[research/hypotheses-jsonl|research log]], sinon DSR bidon.
- **Microstructure (Chen)** — Capacity curve par TTR bucket (edge à TTR=1 ≠ TTR=14). Impact model non-linéaire.
- **ML (Singh)** — SHAP feature stability walk-forward. Leakage audit exhaustif (soil, synoptic timing).
- **Risk (Kowalski)** — Factor exposure décomposé (synoptic regime × TTR × city cluster × edge tier). Regime transition hazard → Kelly adjust.
- **Physique (Schmidt)** — Ensemble NWP disagreement percentile comme feature épistémique. Vraie diversité NWP ≈ 6 sources indépendantes max.
- **Execution (Williams)** — TC model complet (gas Polygon + spread + impact + adverse selection). PnL net = PnL brut − ça.

Log complet : [[risk-committee-insights]] (à créer post-Sprint 1 si utile).

## 5 Packages — 16 livrables consolidés

### Package A — Statistical Validation Core (4)
Les fondations. Dépendent de C3 (research log).

| ID | Livrable | Path | Dépendance |
|---|---|---|---|
| A1 | Deflated Sharpe Ratio | `scripts/deflated_sharpe.py` | C3 |
| A2 | Capacity curve | `scripts/capacity_curve.py` | C7 |
| A3 | Factor exposure | `scripts/factor_exposure.py` | C8, C9 |
| A4 | Purged K-fold evaluator | `scripts/purged_kfold_eval.py` | — |

### Package B — Research Governance (4 docs)
Les docs que les quants écrivent AVANT le code.

| ID | Livrable | Path | Status |
|---|---|---|---|
| B1 | Economic thesis | `vault/.../economic-thesis.md` | DRAFT → user review |
| B2 | Failure modes catalog | `vault/.../failure-modes.md` | DRAFT |
| B3 | Strategy lifecycle | `vault/.../strategy-lifecycle.md` | DRAFT |
| B4 | Research log (hypotheses) | `research/hypotheses.jsonl` + `scripts/log_hypothesis.py` wrapper | — |

### Package C — Model Robustness (4)

| ID | Livrable | Path | Objectif |
|---|---|---|---|
| C4 | SHAP feature stability | `scripts/shap_stability.py` | Alert si top-N features changent > 30% walk-forward |
| C5 | Alpha decay by TTR | `scripts/alpha_decay.py` | Half-life du edge par bucket TTR |
| C6 | Leakage audit | `scripts/leakage_audit.py` | Scan features vs target_date timing |
| C10 | NWP disagreement feature | extend `src/pmhedge/alpha/feature_engineering.py` | Ensemble spread percentile vs climato |

### Package D — Execution & Operations (4)

| ID | Livrable | Path | Objectif |
|---|---|---|---|
| C7 | Transaction cost model | `scripts/transaction_cost_model.py` + `src/pmhedge/alpha/tc_model.py` | Gas + spread + impact + adverse selection |
| C8 | Correlation drift monitor | `scripts/correlation_drift.py` | KS test rolling 30j sur matrix corr |
| C9 | Regime transition hazard | `scripts/regime_transition_risk.py` | P(transition\|current) → Kelly multiplier |
| D1 | Execution quality simulator | `scripts/execution_quality_simulator.py` | Skeleton TWAP/POV/IS (active post-wire) |

### Package E — Monitoring Loop (2)

| ID | Livrable | Path | Objectif |
|---|---|---|---|
| E1 | Gate scorecard | `scripts/gate_scorecard.py` | Agrège A+B+C+D → dashboard déterministe G1→G5 |
| E2 | Launchd + Telegram digest | `launchd/com.paul.polymarket-alpha-gate-scorecard.plist` (08:00 daily) | Digest automatisé |

## Dépendances inter-packages

```
B4 (research log)  ─┐
                    ├─→ A1 (DSR) ──┐
B1 economic thesis ─┘              │
                                   ├─→ E1 (scorecard)
C7 (TC model) ─→ A2 (capacity) ────┤
C8 (corr drift) ──┐                │
                  ├─→ A3 (factor) ─┤
C9 (regime haz) ──┘                │
                                   │
A4 (purged kfold) ─────────────────┤
C4 (SHAP stab) ────────────────────┤
C5 (alpha decay) ──────────────────┤
C6 (leakage) ──────────────────────┤
C10 (NWP disagree) ────────────────┘
```

## Integration avec l'existant (zero duplication)

| Composant proposé | Existe déjà | Stratégie intégration |
|---|---|---|
| TC model | `src/pmhedge/alpha/slippage_ema.py` | **Étendre**, pas remplacer. slippage_ema devient composant du TC model complet |
| Regime HMM | `src/pmhedge/alpha/regime_hmm.py` | **Étendre** avec hazard rate, pas re-fit |
| Correlation | `pair_correlations` table (statique) | **Build rolling** au-dessus, garder statique pour pair_arb |
| Research log | `model_runs` table | **Au-dessus** (hypothesis-level, plus haut niveau) |
| Feature eng | `feature_engineering.py` | **Append** NWP disagreement feature |
| Factor model | Aucun | Nouveau |
| DSR / PBO | Aucun | Nouveau |
| SHAP stability | Aucun | Nouveau |

## Plan d'exécution — 3 sprints

### Sprint 1 — Research Governance (bloquant pour DSR) — 4h
1. B1 `economic-thesis.md` draft (me) → user review (15 min)
2. B4 `research/hypotheses.jsonl` + wrapper
3. B2 `failure-modes.md`
4. B3 `strategy-lifecycle.md`

### Sprint 2 — Validation Core & Robustness — 10h
5. A1 `deflated_sharpe.py`
6. A4 `purged_kfold_eval.py`
7. C4 `shap_stability.py`
8. C5 `alpha_decay.py`
9. C6 `leakage_audit.py`
10. C10 NWP disagreement feature + retrain

### Sprint 3 — Execution & Risk & Monitoring — 7h
11. C7 `transaction_cost_model.py` complet
12. A2 `capacity_curve.py`
13. C8 `correlation_drift.py`
14. C9 `regime_transition_risk.py`
15. A3 `factor_exposure.py`
16. E1 `gate_scorecard.py` + E2 launchd + telegram digest

## Gate Exit — critères quantitatifs

Output attendu de `gate_scorecard.py` quand G1 est passé :

```
G1 Status: PASS (6/6 criteria)
  - DSR adjusted = 1.87  PASS (>= 1.5)
  - PBO = 12%  PASS (<= 20%)
  - SHAP top-3 stability = 89%  PASS (>= 70%)
  - Alpha decay half-life = 9.2 days  PASS (>= 5d)
  - Capacity at 5% edge loss = $4,200  PASS (>= $2,000)
  - No leakage detected  PASS

G2 Ready: YES — proceed to paper shadow 30 days (strategy LOCKED)
```

Si `FAIL`, le scorecard dit exactement quel critère manque et quelle action corrective.

## Hors scope explicitement

| Hors scope G1→G2 | Pourquoi |
|---|---|
| Live execution wiring | Bloqué user (wallet + py-clob-client) — G2→G3 |
| ERA5 / DRN SOTA | Bloqué user (Copernicus) — optimisation post-G2 |
| Pangu ONNX live | Bloqué user (fichier) |
| VPS production | Pas nécessaire avant G3 |
| Champion/Challenger live | Nécessite G2 terminé |
| Kalshi cross-venue | G5+ |

Ces bloqués **ne gênent pas G1→G2**. Dès user débloque, on saute G2→G3 avec infra déjà prête.

## Why this framework

Sans le kit, l'erreur classique : on part en paper shadow avec une strat qui a **l'air** validée mais dont l'edge statistique n'est pas deflated, dont la capacity est inconnue, dont le TC model est incomplet. À la scale-up, surprise : l'edge évapore. Le kit formalise ce que Jane Street / Cubist / Two Sigma font en 1ère semaine de qualification.

## Related

- [[_MOC|Polymarket Hub MOC]]
- [[STATE-HANDOFF|State Handoff — état complet]]
- [[g1-g2-todo-tracker|Todo tracker — execution détaillée]]
- [[gate-scorecard-spec|Gate scorecard — spec critères]]
- [[economic-thesis|Economic thesis — DRAFT pour review user]]
- [[failure-modes|Failure modes — catalog]]
- [[strategy-lifecycle|Strategy lifecycle — sunset criteria]]
- [[audit-hedge-fund-grade|Audit hedge fund grade]]
- [[sessions/2026-04-20-feature-engineering-burst|Session 2026-04-20]]
- [[../_MOC|Brantham MOC]]
- [[../../_system/MOC-patterns|Patterns MOC]]
