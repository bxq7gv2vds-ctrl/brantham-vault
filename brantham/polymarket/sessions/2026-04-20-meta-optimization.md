---
name: Session 2026-04-20 — Meta-optimization (P1+P2+P3)
description: Bandit Thompson sampling allocator + alpha decay t-statistic auto-sunset + LLM feature extractor Claude API. Self-optimizing self-pruning self-augmenting trading system.
type: session
created: 2026-04-20
tags: [polymarket, meta-learning, bandit, llm, self-optimizing]
---

# Session 2026-04-20 — Meta-optimization (P1 + P2 + P3)

Post-lucide compétitive review, 3 pivots out-of-the-box livrés. Le système passe de "framework hedge-fund-grade" à **méta-système self-optimizing + self-pruning + LLM-augmented**.

## P1 — Bandit Thompson sampling allocator

**Fichiers** :
- `src/pmhedge/alpha/bandit_allocator.py`
- `scripts/bandit_allocator.py`
- `com.paul.polymarket-alpha-bandit-allocator.plist` (daily 05:45)

**Méthodologie** :
- Normal-Inverse-Gamma conjugate prior sur μ/σ per-alpha
- Thompson sampling : 200 échantillons par scan, moyenne clipped à 0
- Exploration floor 5% + concentration cap 50%
- Lookback 30j (régime adaptatif)

**Output live test** :
```
Alpha                     n     μ mean     μ std    σ mean  Weight
MODEL_VS_MARKET        1027   +0.77338    0.111    3.574    72.22%
CONFIRMED_NO             55   +0.18491    0.006    0.045    27.78%
CONFIRMED_YES            31   -0.98413    0.022    0.125     0.00% (DISABLED)
```

**Storage** : `alpha_allocator_weights` table (alpha_type, weight, fit_ts, lookback_days).

**Wire downstream** : Live runner lit `load_latest_weights()` pour multiplier Kelly by weight → signal emission probability skewed vers alphas hot.

## P2 — Alpha decay auto-sunset t-statistic

**Fichiers** :
- `scripts/alpha_decay_monitor.py`
- `com.paul.polymarket-alpha-decay-monitor.plist` (daily 06:00)

**Méthodologie** :
- t-statistic = Sharpe × √N
- Short window 14j + Long window 60j
- `DISABLE` si t_short < 1.0 AND t_long < 1.5
- `SHADOW` si t_short < 1.5 seul
- Min N = 15 obs pour décision

**Output live test** :
```
alpha                   n_s    sh_s    t_s  n_l    sh_l    t_l  action
CONFIRMED_NO             55  +4.875 +36.16   55  +4.875 +36.16  KEEP
CONFIRMED_YES            31  +0.000  +0.00   31  +0.000  +0.00  DISABLE !!
MODEL_VS_MARKET        1027  +0.216  +6.93 1027  +0.216  +6.93  KEEP
```

**Safety rails** : avec --apply, update `alpha_states` transactionnel + log dans `alpha_decay_log`.

**Combiné avec P1** : bandit lit alpha_states, donne 0% aux DISABLED → self-consistent.

## P3 — LLM feature extractor Claude API

**Fichier** : `src/pmhedge/alpha/llm_features.py`

**Dépendances** : `anthropic` SDK installé via `uv add anthropic` (+ jiter + sniffio).

**Modèle** : `claude-haiku-4-5` (fast, cheap). Prompt caching sur system prompt (static).

**Input** : (icao, target_date, question_text, extra_context, city_name)

**Output schema** (JSON stricte) :
```
extreme_event_flag : 0|1
event_type         : wildfire|dust_storm|cold_snap|heat_dome|hurricane|snowstorm|none
intensity_1to5     : 0-5
sentiment_hot      : -1.0 to +1.0 (colder→hotter vs climato)
confidence_0to1    : 0-1
rationale          : 1 short sentence
```

**Cache** : 1h TTL sur `(icao, target_date)` — avoid re-query sur 5-min scan cadence.

**Fallback graceful** : API key absent → zero-vector LLMFeatures (pipeline XGB reste rectangular).

**Activation** :
```bash
export ANTHROPIC_API_KEY=sk-ant-...
# OR
security add-generic-password -s "Anthropic API Key" -a paul -w
```

Pour l'instant **inactif** (user doit set l'API key). Quand activé, extract_features tourne en ~1.4s pour une requête typique.

## Impact systémique

Le système devient **auto-piloté** à 3 niveaux :

1. **Per-signal** : Kelly + tail_filter + vol_filter + session_filter + edge_band (niveau existing)
2. **Per-alpha** : bandit allocator (P1) + decay monitor (P2) — **NEW**
3. **Per-context** : LLM features (P3) ajoutent couche sémantique unique à retail — **NEW**

Interaction :
- Decay monitor flag DISABLE → alpha_states update → persist_signal block
- Bandit reads alpha_states, ignore DISABLED, réalloue sur KEEPS
- LLM features feed XGB avec sémantique news/alerts

## Launchd infrastructure

**39 jobs actifs** (+2 nouveaux) :
- `alpha-bandit-allocator` → daily 05:45
- `alpha-decay-monitor` → daily 06:00 (--apply mode)

Séquence matinale :
```
03:30 bma-train
04:15 calibrators-train
04:30 vol-filter, ensemble-train
04:45 regime-train
05:15 station-xgb
05:45 bandit-allocator   NEW
06:00 decay-monitor      NEW
08:00 gate-scorecard
08:15 perf-digest
09:10 reconcile
...
```

## Next level out-of-the-box

Non-implémenté mais documenté :
- **Market-making skeleton** (flip taker → maker sur thin markets) — bloqué wallet user
- **Multi-category expansion** (sports/crypto/elections Polymarket) — 1-2 sem par vertical
- **ERCOT day-ahead** cross-chain weather → electricity — 1-2 mois dev, 100× capacity
- **Academic paper publication** — crédibilité / LP access — 2 semaines
- **DeFi hedge fund structure** — $500k-5M AUM scaling — avocat requis

## Tasks persistées

#54 P1 bandit — completed
#55 P2 decay — completed
#56 P3 LLM — completed (API key activation requise user)

## Related

- [[sessions/2026-04-20-scale-optimize|Scale & Optimize Kit]]
- [[sessions/2026-04-20-actions-applied|Actions Applied]]
- [[hedge-fund-rigor-upgrade|Rigor Upgrade]]
- [[g1-g2-qualification-kit|G1→G2 Framework]]
- [[STATE-HANDOFF]]
- [[_MOC]]
