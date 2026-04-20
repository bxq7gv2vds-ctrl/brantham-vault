---
name: Continuation Prompt — prochain session Claude
description: Prompt exact à donner au prochain Claude pour reprendre la session 15j paper + tout le système en cours. Zero perte de contexte.
type: handoff
priority: critical
created: 2026-04-20
tags: [polymarket, handoff, prompt, continuation]
---

# Prompt à donner au prochain Claude

Copy-paste ce qui suit dans la nouvelle session.

---

```
Projet Polymarket Weather Hedge Fund — /Users/paul/polymarket-hedge/.
Je reprends une session 15-jour paper trading qui a été lancée 2026-04-20.

DOCS À LIRE EN PRIORITÉ (dans cet ordre, OBLIGATOIRE avant toute action) :
1. vault/brantham/polymarket/MODEL-STATE-COMPLETE.md — zéro-omission models snapshot
2. vault/brantham/polymarket/STATE-HANDOFF.md — état global
3. vault/brantham/polymarket/weather-domination-strategy.md — philosophie 100% weather
4. vault/brantham/polymarket/CONTINUATION-PROMPT.md — ce doc
5. research/hypotheses.jsonl — 19 hypothèses loggées (DSR compte)

CONTEXTE EN UNE PHRASE
Le meilleur hedge fund weather Polymarket, stack hedge-fund-grade validé
empiriquement, paper session 15j active, compound $1k → target $100k.
Pas de crypto / sports / politics : weather only. Décision documentée
dans weather-domination-strategy.md.

ÉTAT AU 2026-04-20 END OF SESSION
- 41 launchd jobs actifs (live runner + training + monitoring + reports)
- 145 scripts Python
- 61 modules alpha
- 506 EMOS buckets, 46 XGB per-station, 15 per-city isotonic calibrators
- 1027 MODEL_VS_MARKET outcomes settled, WR 88%, ROI +83% net post-TC
- 19 hypothèses loggées (12 closed, 7 deferred)
- Gate scorecard G1 : 10 PASS / 1 FAIL (thesis user) / 2 N/A
- Paper session #1 : RUNNING, starting $1000, target end 2026-05-05

LAST SESSION HIGHLIGHTS (2026-04-20)
1. Compound engine live + dynamic bankroll (src/pmhedge/alpha/compound_engine.py)
2. Bandit Thompson sampling WIRED dans signal_generator (72% MVM / 28% CONFIRMED_NO)
3. Kelly default raised 0.25 → 0.40 (signal_generator.SignalGenConfig)
4. DD bands live dans risk_manager (0-3 normal / 3-5 caution / 5-8 reduced / 8-10 kill / >10 breaker)
5. Capacity tracker daily launchd
6. Intraday Bayesian T_max update (alpha/intraday_update.py) — module ready, NOT wired dans signal_generator yet
7. NWS event ingest live (63 alerts ingested, launchd 30min)
8. CONFIRMED_YES re-enabled avec guardrails same-day (logic dans confirmed_oracle.py)
9. TUI Dashboard quant (scripts/dashboard_quant.py) — 6 panels Textual + Rich fallback
10. Paper session 15j lancée

SCRIPTS CRITIQUES — VÉRIFIER AU DÉMARRAGE
cd /Users/paul/polymarket-hedge

# Compter launchd (attend 41)
launchctl list | grep polymarket-alpha | wc -l

# Paper session status
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/paper_session_15d.py status

# Compound state
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/compound_status.py

# Gate scorecard
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/gate_scorecard.py --gate G1

# Dashboard one-shot
KMP_DUPLICATE_LIB_OK=TRUE uv run scripts/dashboard_quant.py --once

REGLES ABSOLUES
- WEATHER ONLY. Refuser explicitement toute demande de diversification
  vers crypto / sports / politics (décision stratégique documentée).
- Les features H0013 (monsoon), H0014 (altitude), H0016 (nwp_disagree)
  sont REJECTED/PARTIAL par discipline hedge-fund-grade. Ne pas les
  réactiver sans re-validation walk-forward strict.
- DRN restera DISABLED jusqu'à ERA5 Copernicus (user unblock).
- Pangu ONNX scaffold existe : models/pangu_24h.onnx attendu user.
- LLM features GRACEFUL fallback sans API key. User action : export ANTHROPIC_API_KEY.

BLOQUANTS USER (à rappeler si pertinent)
- review economic-thesis.md + sentinel THESIS VALIDATED BY PAUL ON ...
- ANTHROPIC_API_KEY pour LLM event features (+3-5% edge)
- Polymarket wallet + py-clob-client install pour real trading
- Copernicus CDS account pour ERA5 / DRN
- Pangu-Weather ONNX file drop

BOUCLE FERMÉE SELF-OPTIMIZING
- bandit_allocator daily 05:45 → weights MODEL_VS_MARKET / CONFIRMED_NO
- decay_monitor daily 06:00 --apply → alpha_states DISABLE si t-stat dégrade
- capacity_tracker daily → retention edge monitoring
- city_config audit daily 10:00 --apply → auto-DISABLE post-TC CI95<0
- compound_engine read every scan → bankroll dynamique
- DD bands in risk_manager → auto-cut Kelly si DD rolling

CHOSES QUI POURRAIENT VENIR ENSUITE
1. Wire intraday_update.refine_intraday() dans signal_generator post-12z UTC
   (module prêt, integration 30min)
2. Wire event_ingest.event_feature_for_market() dans enrich_features
   (fonction prête, integration 20min)
3. Activer use_portfolio_kelly=True après 7j validation
4. Re-run bandit_allocator après qq jours de nouveaux outcomes
5. Si T=30 distinct days atteint : re-run var_es_kupiec, correlation_drift,
   DSR daily (vs DSR per-trade)
6. Wire concurrent_positions.record_position() dans persist_signal
7. Activer vol_targeting en mode opt-in
8. Market-making weather thin markets (Seoul/Moscow/Lucknow) — mais
   seulement après $50k bankroll (pas pour $1k-100k)

ARCHITECTURE FLOW (référence rapide)
DATA (12 NWP + obs + synoptic + events) → MODEL (climato + EMOS + BMA + XGB
+ regime HMM) → POST-PROC (isotonic + tail + vol + session + edge_band
filters) → SIGNAL (MODEL_VS_MARKET + CONFIRMED_NO/YES) → RISK (Kelly +
portfolio Kelly + DD bands + circuit breaker) → PERSIST (alpha_states
+ session_filter check + audit log) → [EXEC live post-wallet]
→ SETTLEMENT (reconcile obs) → FEEDBACK (bandit + decay + compound + DD)

LANGUE
Français conversation, anglais code. Pas d'emojis. Pas de violet.
Accents obligatoires (é è à â ô î ï ç).
```

---

## Notes pour le toi-futur Claude

Ne pas oublier :

1. **`KMP_DUPLICATE_LIB_OK=TRUE` toujours** avant `uv run` pour XGBoost + torch (OpenMP collision sur macOS ARM)

2. **Schema `alpha_states`** : primary key `alpha_type`, status ENABLED/DISABLED seulement (pas SHADOW — c'est au niveau `city_config` pour les villes).

3. **Compound engine table** : `compound_state` a 1 seule row (id=1) qui track starting_bankroll + current (via joins à signal_outcomes).

4. **Paper session** : `paper_sessions` table, status RUNNING/COMPLETED/CANCELLED.

5. **Dashboard TUI** : deux modes — textual interactive (default) ou `--once` Rich render (safe background tmux). Keybindings q/r/1-6.

6. **Research log** : **19 hypotheses** = compteur DSR. Ne pas re-logger d'anciennes. Utiliser `scripts/log_hypothesis.py add` pour nouvelles.

7. **City config rules (2026-04-20 upgrade)** :
   - `DISABLED` si `net_roi_ci95_upper < 0` AND N≥30 (post-TC)
   - `ENABLED` override si `net_roi_ci95_lower > 0` AND N≥30 (stat-profitable)
   - Austin reste ENABLED grâce à l'override (CI95_lo +4.93)

8. **Session filter blocked hours** : UTC {6, 7, 8, 9}. Override via env `PMHEDGE_BLOCKED_HOURS="6,7,8,9"`.

9. **Bandit cache** : 15 min TTL dans `signal_generator._bandit_weight`. Si tu changes alpha_allocator_weights, attendre 15 min ou redémarrer live runner.

10. **Portfolio Kelly** : opt-in (default False). Flip `RiskConfig.use_portfolio_kelly=True` après validation G2 paper shadow.

11. **Intraday update** : NOT yet wired dans signal_generator.create_model_vs_market_signal. Le module existe mais il faut ajouter `refine_intraday()` call post-12z UTC pour override mu/sigma forecast. C'est la priorité 1 des optimisations pending.

## Fichiers à ne JAMAIS supprimer

- `alpha_data_hub.db` — données de trading + outcomes + attributions + compound
- `emos_alpha.db` — 506 EMOS buckets
- `city_models.db` — climatologies DOY
- `research/hypotheses.jsonl` — append-only log (DSR N_trials)
- Tous les `models/*.json`, `models/*.pkl`, `models/*.pt`
- Tous les launchd `.plist` dans `~/Library/LaunchAgents/com.paul.polymarket-alpha-*`

## Related

- [[MODEL-STATE-COMPLETE|Model state zero-omission]]
- [[STATE-HANDOFF|State handoff]]
- [[weather-domination-strategy]]
- [[g1-g2-qualification-kit]]
- [[_MOC]]
