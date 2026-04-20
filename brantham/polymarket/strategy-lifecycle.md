---
name: Strategy Lifecycle — Sunset & retrain criteria
description: Règles formelles pour décider quand retrain, quand descaler, quand tuer la stratégie Polymarket weather. Prévient l'attachement émotionnel à une strat morte.
type: playbook
created: 2026-04-20
updated: 2026-04-20
priority: high
tags: [polymarket, lifecycle, sunset, retrain, governance, risk]
---

# Strategy Lifecycle — Sunset & retrain criteria

Règles formelles pour éviter le piège classique d'attachement émotionnel à une stratégie morte. Chaque trigger est **déterministe** (pas de judgement call).

**Sentinel** : `LIFECYCLE READY` présent dans ce doc = passe check G1 criterion.

## 1. Stages de vie

```
    G1→G2→G3→G4→G5  [ACTIVE]  →  [DEGRADING]  →  [SUNSET]  →  [ARCHIVE]
                        |             |              |
                     monitor    reduce scale    kill switch
                     daily       auto-trigger    + retrain ou abandon
```

## 2. Retrain triggers — obligatoires

### Retrain NORMAL (schedule)
- **BMA weights** : daily 03:30 via `bma-train` (déjà en place)
- **XGBoost post** : weekly Fri 05:15 via `xgb-retrain` (déjà en place)
- **Regime HMM** : weekly Fri 05:30
- **Per-city calibrators** : daily 04:20
- **Vol thresholds** : daily 04:30

### Retrain FORCÉ (drift detected)
Trigger : `drift_monitor` alerte sur :

| Condition | Retrain forcé de |
|---|---|
| ECE rolling 7j > 0.15 | Calibrators (global + per-city) |
| WR rolling 30j < 70% (vs baseline 88%) | Ensemble weights + tail filter |
| Feature importance top-3 change > 30% | XGBoost per-station |
| Pair correlation KS p < 0.01 | `pair_correlations` table |
| Capacity curve shifts > 30% | TC model recalibration |

Script force retrain : `scripts/force_retrain.py --component {bma|xgb|calib|regime|all}` (à livrer dans Sprint 3 si utilisé).

## 3. De-scale triggers — automatiques

Pas forcément fatal, mais appelle un rétrécissement exposition.

| Condition | Action auto |
|---|---|
| Sharpe rolling 60j < 1.5 | Kelly global × 0.5 (de 0.5 → 0.25) |
| Max DD 30j > 5% | Bankroll risk cap à 50% du cap normal |
| Ville N=50+ outcomes WR < 60% | `city_config.status = SHADOW` auto |
| Factor max exposure > 40% | Enforce size cap per factor bucket |
| Data freshness uptime < 95% rolling 7j | Disable source incriminée |

Déjà implémenté en partie via `audit_per_city.py --apply` qui descale autonome.

## 4. SUNSET triggers — critiques

Quand déclencher sunset (kill switch complet) :

| Condition | Action |
|---|---|
| **DSR rolling 90j < 0.5** | Pause all trading, user review required |
| **WR rolling 30j < 60% sur N >= 200** | Idem |
| **PBO rolling 90j > 40%** | Idem (overfitting detected ex-post) |
| **Perte > 15% bankroll en 7 jours** | Circuit breaker + sunset evaluation |
| **Oracle malfunction majeur** (> 3 markets mal résolus en 7j) | Pause jusqu'à resolution |
| **Polymarket banned FR** | Sunset permanent, migration éventuelle Kalshi |
| **Compétiteur institutionnel détecté** (tight spreads systématiques, volume 10x inhabituel) | Rétrécir scope aux niches non-arbitrées ou sunset |

Le sunset ne signifie **pas** abandon permanent : c'est pause + investigation + décision (retrain profond ou abandon définitif).

## 5. Décision post-sunset — arbre

```
SUNSET triggered
        |
   Investigation cause (7j max)
        |
   ┌────┴─────────────────────────┐
   |                              |
Cause technique                 Cause structurelle
(bug, data issue, leakage)    (edge died, compétition)
   |                              |
Fix + backtest                 Retrain profond ? 
revalidate G1 PASS ?            OU pivot scope ?
   |                              |  
   ├── PASS → redémarrer G2    ├── Nouveau scope → restart G0
   └── FAIL → voir droite      └── Pas de pivot viable → ARCHIVE
```

## 6. Archive — procédure

Si sunset permanent :

1. Dump final : `scripts/archive_strategy.py --reason "..."` →
   - Freeze all models files → `models/archive/YYYY-MM-DD/`
   - Export final `signal_outcomes` → `archive/outcomes.parquet`
   - Export `audit_log` → `archive/audit.jsonl`
   - DB snapshot → S3 (si configuré)
2. Disable tous les launchd jobs liés.
3. Documenter dans `vault/brantham/polymarket/archive-YYYY-MM-DD-reason.md` :
   - Durée de vie de la strat
   - P&L total
   - Cause de mort
   - Leçons (pour futures strats)
4. Mettre à jour `_MOC.md` statut → ARCHIVED.

## 7. Renaissance — if edge returns

Si après archive, signal statistique suggère le edge revient :

- Repartir de G0 (pas de shortcut)
- Re-justifier economic thesis (que se passe-t-il de différent ?)
- Full qualification kit re-run

Pas de "juste réactiver". Protège du wishful thinking.

## 8. Horizon de vie attendu

Selon [[economic-thesis]] :

- **Expected lifetime** : 12-36 mois
- **Probable sunset causes (rank)** :
  1. Compétition institutionnelle (probability 40%)
  2. Polymarket weather volume collapse (25%)
  3. Regulatory change (15%)
  4. Oracle systemic issue (10%)
  5. Model irreparably drifted (10%)

## 9. Check gouvernance

Chaque fin de mois : relire ce doc + review [[gate-scorecard-spec|scorecard]] output mensuel. Si aucun trigger, continuer. Sinon, appliquer l'action prescrite.

Pas de skip. Pas de "cette fois c'est différent".

## 10. Accountability

Paul seul décide sunset permanent (décision capital). Sunset temporaire + de-scale peuvent être auto-triggered. Chaque décision sunset est loguée dans `audit_log` avec actor=paul + raison.

---

**LIFECYCLE READY** — ce doc couvre retrain + de-scale + sunset + archive + renaissance. Passe critère G1.

## Related

- [[g1-g2-qualification-kit|Framework master]]
- [[g1-g2-todo-tracker|Todo tracker]]
- [[gate-scorecard-spec|Gate scorecard spec]]
- [[economic-thesis|Economic thesis — lifetime expected]]
- [[failure-modes|Failure modes — liens vers sunset]]
- [[STATE-HANDOFF]]
- [[_MOC|Polymarket Hub]]
- [[../../_system/MOC-decisions|Decisions MOC]]
