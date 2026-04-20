---
name: Failure Modes — Catalog
description: Catalog formel des modes de défaillance de la stratégie Polymarket weather. Pour chaque mode — mécanisme, signature, détection, mitigation, sévérité.
type: catalog
created: 2026-04-20
updated: 2026-04-20
priority: high
tags: [polymarket, risk, failure-modes, catalog, governance]
---

# Failure Modes — Catalog

Ce doc liste formellement **ce qui peut casser la strat**. Sans ce catalog, les circuit breakers et kill switches sont arbitraires. Un failure mode = cause + signature observable + détection + mitigation + sévérité.

## Légende sévérité

- **CRITICAL** : perte > 10% bankroll en < 24h, ou perte permanente (key compromise, oracle malfunction)
- **HIGH** : degradation edge silencieuse, détectée sur 7-30j
- **MEDIUM** : bruit operationnel, gérable par retry/failover
- **LOW** : inconvénient (alertes manquées, rapports retardés)

## Modes

### Mode 1 — NWP source contamination (silencieux)
**Cause** : Open-Meteo change son backend ou une source retourne des valeurs aberrantes sans flag erreur.
**Signature** : ensemble_mean diverge du baseline climato historique, ECE drift brutal.
**Détection** : `drift_monitor` job (10:00 daily), alerte Telegram si ECE rolling 7j > 0.15.
**Mitigation** : auto-disable source via `alpha_states`, retrain BMA sans.
**Sévérité** : HIGH.

### Mode 2 — METAR feed down
**Cause** : Aviation Weather Center API down, ou changement format.
**Signature** : `data_freshness.METAR.status != OK` > 2h.
**Détection** : `health_check` job (15min).
**Mitigation** : fallback Open-Meteo historical ARCHIVE (moins précis mais live).
**Sévérité** : MEDIUM.

### Mode 3 — Polymarket oracle malfunction
**Cause** : UMA/Polymarket dispute resolves contrary to real outcome, ou résolution tardive > 48h.
**Signature** : `signal_outcomes.resolved_ts - signal_outcomes.target_ts > 48h` récurrent.
**Détection** : nightly `reconcile_from_obs.py` compare claim vs obs réelle.
**Mitigation** : flag ville/market pour human review. Exclusion temporaire via `city_config.status=DISABLED`.
**Sévérité** : CRITICAL (perte permanente + érosion trust).

### Mode 4 — Catastrophic weather event (tail risk)
**Cause** : ouragan/typhon/vague chaleur > 4σ climato, ensemble NWP ne capture pas.
**Signature** : anomaly_z > 4 sur obs réalisée.
**Détection** : ex-post via reconcile. Ex-ante via ensemble_std > 3°C check.
**Mitigation** : `tail_filter.py` rejette déjà YES tails. Size cap per-city limite l'exposition.
**Sévérité** : HIGH.

### Mode 5 — MEV / sandwich attack
**Cause** : bot observe notre order en mempool Polygon, front-run.
**Signature** : slippage réalisé >> attendu systématiquement.
**Détection** : `slippage_ema` vs prédicté par TC model, drift > 2σ.
**Mitigation** : Flashbots private mempool, ou hardware wallet + batch orders.
**Sévérité** : HIGH (bloquant pour real money > $5k).

### Mode 6 — Private key compromise
**Cause** : leak `.env`, machine compromise, phishing.
**Signature** : unauthorized trades, balance transfer.
**Détection** : hourly balance diff vs expected.
**Mitigation** : hardware wallet Ledger, rotation, air-gap signing pour positions > $10k.
**Sévérité** : CRITICAL.

### Mode 7 — Model drift (alpha decay silencieux)
**Cause** : regime climatique change, compétiteurs arrivent, le edge s'effrite.
**Signature** : rolling Sharpe 30j diverge du backtest progressivement.
**Détection** : `drift_monitor` + `gate_scorecard` daily, alerte si Sharpe rolling < 1.0.
**Mitigation** : retrain auto, sinon trigger sunset via [[strategy-lifecycle]].
**Sévérité** : HIGH.

### Mode 8 — Regulatory change (Polymarket banned FR/EU)
**Cause** : AMF ou ESMA reclassifie Polymarket, plateforme bloquée.
**Signature** : impossible d'accéder API, wallet frozen.
**Détection** : monitoring news + API error rate.
**Mitigation** : migration vers Kalshi (si US-légal accessible), ou sunset.
**Sévérité** : CRITICAL mais rare (probabilité estimée < 5% en 12 mois).

### Mode 9 — Liquidity collapse (volume chute)
**Cause** : Polymarket weather markets deviennent illiquides si oracle issues ou concurrence.
**Signature** : `volume_24h` rolling median < $200/market.
**Détection** : `capacity_curve` update weekly.
**Mitigation** : descale bankroll, restreindre aux top-20 markets par volume.
**Sévérité** : HIGH.

### Mode 10 — Data leakage (silent overfit)
**Cause** : feature introduite accidentellement utilise data post target_date.
**Signature** : live WR << backtest WR after lock.
**Détection** : `leakage_audit.py` dans le kit + G2 paper shadow divergence alert.
**Mitigation** : retrait feature, retrain.
**Sévérité** : HIGH.

### Mode 11 — Circuit breaker stuck
**Cause** : bug dans `circuit_breaker` qui trip à tort et ne rearm pas.
**Signature** : `alpha_states` montre ENABLED=false > 24h sans raison légitime.
**Détection** : `validator.py` daily check.
**Mitigation** : script manual `rearm_breaker.py`.
**Sévérité** : MEDIUM.

### Mode 12 — Infrastructure fail (Mac reboot, launchd crash)
**Cause** : OS update force reboot, process manager down.
**Signature** : `launchctl list | grep polymarket` returns < 35 jobs.
**Détection** : `health_check` job, Telegram alert.
**Mitigation** : post-reboot init script auto-reload plists.
**Sévérité** : MEDIUM (cap restart latency < 15min).

## Monitoring aggregate

Les modes sont monitored par ces jobs existants :

| Job launchd | Couvre |
|---|---|
| `health_check` (15min) | 2, 11, 12 |
| `drift_monitor` (10:00 daily) | 1, 7 |
| `reconcile` + `reconcile_from_obs` (09:10/09:15) | 3, 4 |
| `circuit_breaker` (15min) | 11 |
| `slippage_ema` (updated per trade) | 5 |
| `gate_scorecard` (08:00 daily, à livrer E1) | 7, 10 |

## Modes non monitored (gaps)

Ces modes n'ont **pas** de détection automatisée :

- **Mode 6 (key compromise)** : aucun monitoring balance on-chain. **À corriger post G3 (quand wallet actif)**.
- **Mode 8 (regulatory)** : monitoring news manuel. **Acceptable — rare + action user requise de toute façon**.
- **Mode 9 (liquidity)** : capacity_curve weekly mais pas alerte automatique. **À fix dans Sprint 3**.

## Severité agrégée

| Sévérité | Count | Action |
|---|---|---|
| CRITICAL | 3 (oracle, key, regulatory) | chacun a un kill switch dédié |
| HIGH | 5 | drift monitor + gate scorecard |
| MEDIUM | 3 | auto-recovery |
| LOW | 0 | — |

## Validation count

Pour G1 PASS : **>= 8 modes cataloged**. Actuel : **12**. PASS.

## Related

- [[g1-g2-qualification-kit|Framework master]]
- [[g1-g2-todo-tracker|Todo tracker]]
- [[gate-scorecard-spec|Gate scorecard spec]]
- [[strategy-lifecycle|Strategy lifecycle — quand tuer la strat]]
- [[economic-thesis|Economic thesis — quand le edge meurt]]
- [[STATE-HANDOFF]]
- [[_MOC|Polymarket Hub]]
- [[../../_system/MOC-bugs|Bugs MOC]]
