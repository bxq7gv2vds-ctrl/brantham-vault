---
name: Session 2026-04-20 — Actions appliquées (5 hedge-fund fixes)
description: 5 actions concrètes appliquées suite aux findings de TC-aware attribution + stationarity + correlation Kelly. Impact live immediate sur signaux + city_config + alpha_states.
type: session
created: 2026-04-20
tags: [polymarket, actions, live, hedge-fund, fixes]
---

# Session 2026-04-20 — Actions appliquées

Suite aux findings hedge-fund-rigor-upgrade, 5 actions concrètes appliquées en live (non bloquées par user).

## 1. Edge band 8-15 % bloqué au niveau signal_generator

`SignalGenConfig.edge_band_blocked = (0.08, 0.15)` — appliqué dans le code.

**Justification empirique** (`tc_aware_attribution.py`) :
- tier_4_8 : CI95 [+0.04, +0.30] — **KEEP** (positive)
- tier_8_15 : CI95 [-0.31, -0.18] — **BLOCKED** (stat negative)
- tier_15_25 : CI95 [-0.03, +0.10] — kept (overlap zero, watch)
- tier_25+ : CI95 [+2.01, +3.61] — **KEEP** (winner)

Le filter rejette les signaux dont |edge| ∈ [0.08, 0.15), zone empiriquement loss-making post-TC. Le min_edge=0.05 reste en place pour tier_4_8.

## 2. audit_per_city.py — critère DISABLE post-TC ajouté

Nouveau critère :
```python
if n >= 30 and net_roi_ci95_upper < 0:
    return (DISABLED, "post-TC sunset")
```

Override `net_roi_ci95_lower > 0 → force ENABLED` (protège Austin malgré WR CI-lo 69 % marginal).

**Cities reclassifiées** (après re-run avec --apply) :
- **Miami SHADOW → DISABLED** (net-ROI CI95 upper -0.042, N=68)
- **NYC → DISABLED** (net-ROI CI95 upper -0.056, N=30)
- Tokyo, Chicago restent DISABLED
- Austin ENABLED (net-ROI CI95 lo +4.93 > 0)

Final breakdown : **20 ENABLED / 2 SHADOW (dallas, mexico city) / 4 DISABLED (NYC, miami, chicago, tokyo)**.

## 3. CONFIRMED_YES alpha — DISABLED via alpha_states

Bug diagnostiqué : 31 signaux CONFIRMED_YES ROI -100 % sont des trades **legacy pré-fix** du 2026-04-18. Metadata confirme `diag: prev_day=2026-04-17` pour `target_date=2026-04-18` (fix `prev_day only if past` appliqué après).

Le code actuel gère ce cas correctement. Safety-net : alpha désactivée dans `alpha_states` jusqu'à validation sur 30 jours de nouveaux outcomes sans régression.

```sql
UPDATE alpha_states SET status='DISABLED'
WHERE alpha_type='CONFIRMED_YES'
```

Les prochains signaux CONFIRMED_YES seront loggés comme `signal.blocked (kill_switch)` dans audit_log.

## 4. Monte Carlo P&L — default block_size = 10

Ljung-Box lag-10 a détecté autocorrelation significative (p=0.019). IID bootstrap **biaisé** pour annualize. Default passé à block_size=10 pour préserver la structure de dépendance.

```python
# monte_carlo_pnl.py
ap.add_argument("--block-size", type=int, default=10, ...)
```

## 5. Portfolio Kelly — wire opt-in dans risk_manager

Nouvelle fonction `compute_portfolio_kelly_weights(cities, f_naive, reg)` :
- Construit matrice C de corrélations pair_correlations
- Résout `f* = (C + λI)^{-1} · f_naive`
- Clip dans [0, 1]
- Fallback sur scalar portfolio_factor si matrice singulière

Wiré dans `evaluate_batch` via `RiskConfig.use_portfolio_kelly` (default **OFF** pour backward-compat).

**Test empirique** sur 4 signaux US+Asia ($50 chacun) :
- Legacy scalar shrink : factor 0.632, total allocated **$126**
- Portfolio Kelly : avg_shrink 0.400, total allocated **$80** (37 % plus conservateur)

À flip à `use_portfolio_kelly=True` quand :
1. G2 paper shadow 30+ jours validates no edge erosion
2. G3 real money wired

## Effets live immédiats

### Signaux bloqués en production
- Edges dans [8 %, 15 %) → rejected
- Alpha CONFIRMED_YES → blocked
- 4 villes DISABLED (NYC/Miami/Chicago/Tokyo) → kelly=0 via city_config
- Sessions 06-09 UTC → blocked via session_filter (appliqué session B2)

### Sécurité
- 37 launchd jobs toujours actifs
- alpha_states respecté dans persist_signal
- audit_log loggue raison de block (kill_switch / session_filter / edge_band / tail_filter)

## Caveats méthodologiques

- **Edge-band block basé sur 2 jours** d'émission + N=300 trades tier_8_15. Le CI95 est large. Possible false-negative (alpha qui marchera en régime climato différent). Revalider après T≥30 jours distincts.
- **Portfolio Kelly v1** utilise correlation matrix d'observations **passées** (pair_correlations table). Si régime change, matrix est stale. À retrain weekly.
- **Miami DISABLED basé sur N=68** au ROI -33 % post-TC. Période courte, possible faux sunset si régime météo change drastiquement. Re-évaluer mensuellement.
- **CONFIRMED_YES** réactivable — le code actuel a le fix `target >= today_utc → None`. Simplement une safety-net redondante.

## Prochaine étape

Attendre accumulation data (7-14 jours) avant re-run attribution complète. Observer :
- Nombre de signaux bloqués par nouveau edge_band (suivre audit_log)
- Drift de performance après exclusion sunset cities
- Impact session_filter h06-h09 blocked sur volume global

## Related

- [[hedge-fund-rigor-upgrade|Hedge Fund Rigor Upgrade]]
- [[g1-g2-qualification-kit|G1→G2 Framework]]
- [[feature-rejection-log|Feature rejection log]]
- [[sessions/2026-04-20-execution-performance-kit|Execution & Perf Kit]]
- [[sessions/2026-04-20-g1-g2-kit-build|G1-G2 Kit]]
- [[STATE-HANDOFF]]
