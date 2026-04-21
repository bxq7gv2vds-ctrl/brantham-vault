---
name: Continuation Prompt — prochaine session Claude
description: Prompt exact à donner au prochain Claude pour reprendre la session 15j paper + research pipeline + tout le contexte 2026-04-21. Zero perte de contexte.
type: handoff
priority: critical
created: 2026-04-20
updated: 2026-04-21
tags: [polymarket, handoff, prompt, continuation]
---

# Prompt à copier-coller dans la prochaine session

```
Projet : Polymarket Weather Hedge Fund — /Users/paul/polymarket-hedge/

Paper session #1 ACTIVE depuis 2026-04-20. Bankroll $1000 target $100k via compound.

Lis dans cet ordre avant de répondre :
1. /Users/paul/vault/brantham/polymarket/ARCHITECTURE.md (structure complète)
2. /Users/paul/vault/brantham/polymarket/CONTINUATION-PROMPT.md (ce doc)
3. /Users/paul/vault/brantham/polymarket/TODO-pending.md (punch list P0-P6)
4. /Users/paul/vault/brantham/polymarket/MODEL-STATE-COMPLETE.md (snapshot models)
5. /Users/paul/vault/brantham/polymarket/city-optimization.md (kill/boost par ville)

Mémoire auto : /Users/paul/.claude/projects/-Users-paul/memory/polymarket_paper_session_1.md

Règles absolues :
- WEATHER ONLY (pas crypto/sports/politics)
- Kelly 0.40 default
- FR conversation / EN code
- KMP_DUPLICATE_LIB_OK=TRUE avant uv run
- No emojis, no violet
- Accents FR obligatoires (é è ê à â ô î ï û ç)
```

## État au 2026-04-21 (après context-clear prévu)

### Paper session #1 — Stats live

- **1704 trades** (1518 closed, 186 open)
- **P&L réalisé : +$19,599.51**
- **WR : 83.6%**
- Open exposure : $1,896.50
- Avg / trade : +$12.91

**Par tier** :
- Tier S (MODEL YES deep_OTM, Kelly ×1.5) : +$15,607 / 228 trades / WR 17.6% / avg +$68.75 → STAR, 80% du P&L
- Tier A (MODEL NO workhorse) : +$3,847 / 1075 trades / WR 94.5% / avg +$3.94
- Tier C (CONFIRMED_NO) : +$98 / 134 trades / WR 100%
- Tier B (MODEL NO >0.9) : +$48 / 267 trades / WR 96.9%

### 2545 signaux émis total (686 aujourd'hui 2026-04-21)

### City config : 36 ENABLED, 4 DISABLED (Tokyo, Chicago, Miami, NYC)

## Scanner vs launchd — ce qui tourne automatiquement

**Scanner live** (`run_alpha_live.py`) : loop 300s, PID persistant via launchd `com.paul.polymarket-alpha-live-runner`

**54 launchd jobs actifs** :
- `alpha-live-runner` (loop 300s)
- `nwp-ingest` / `metar-archive` / `soil-ingest` / `synoptic-fetch` / `event-alerts`
- Training : `bma-train`, `emos-train`, `ensemble-train`, `hmm-train`, `regime-v2-train`, `station-xgb`, `xgb-retrain`, `calibration`, `calibrators-train`, `city-calibrators`
- Tuning quotidien : `city-optimizer` (09:30), `ttr-denylist` (09:45), `city-kelly`, `bandit-allocator`
- Reconcile : `reconcile-obs` (09:20, close trades auto), `auto-settle`, `daily-pnl`, `daily-summary`
- Monitoring : `circuit-breaker`, `drift-monitor`, `gate-scorecard` (08:00), `perf-digest` (08:15)
- Dashboard : `alpha-dashboard` (port 8090)

## Changements majeurs 2026-04-20 → 2026-04-21

### 2026-04-20 après-midi — Exec pipeline fix

**Bug critique** : 1793 signaux émis, 0 trades (pipeline exec débranché)

**Fix** :
- `src/pmhedge/alpha/bucket_router.py` (S/A/B/C tier classification sur edge empirique)
- `src/pmhedge/alpha/live_executor.py` (paper fill + trade_log writer)
- Wire dans `signal_generator.persist_signal()` ligne 559
- Hook `close_resolved_trades()` dans `scripts/reconcile_from_obs.py`
- 1646 trades backfillés, +$19k P&L théorique matérialisé

### 2026-04-20 soir — Kill list per-ville

**4 villes DISABLED** : Tokyo (-$1013 / WR 0%), Chicago (-$448 / WR 28%), Miami (-$203), NYC (-$151)

**8 villes BOOST Kelly ×2** : Austin, Atlanta, Dallas, Beijing, SF, Houston, Denver, LA

**Scripts** :
- `scripts/city_optimizer.py` + launchd daily 09:30
- `scripts/city_deep_dive.py` (27 rapports dans `vault/brantham/polymarket/city-reports/`)

### 2026-04-20 soir — Per-(city, TTR) denylist

**11 règles** blocked : Tokyo 24-48h, Chicago 24-48h, Wellington 24-48h, Miami 6-12h, Austin 0-6h, NYC 0-6h, etc.

**Modules** : `src/pmhedge/alpha/ttr_filter.py` + launchd `ttr-denylist` (09:45 UTC)

### 2026-04-20 fin — Calibration bug fix

**Bug** : `use_calibration=False` par défaut dans `SignalConfig`. Tokyo calibrator (dit 1% partout) jamais appliqué avant 2026-04-20 09:36 UTC = 85 trades Tokyo perdus.

**Fix** : `use_calibration=True` + `use_volatility_filter=True` default dans `signal_generator.py` ligne 218-222.

### 2026-04-21 matin — Cleanup + Architecture doc

**Cleanup** :
- Delete `pangu_forecaster.py` (scaffold orphelin)
- Disable launchd `polymarket-dashboard` (ancien port 8765 en conflit)
- Move 5 scripts legacy → `scripts/legacy/`
- 54 launchd actifs (était 55)

**Doc** : `vault/brantham/polymarket/ARCHITECTURE.md` — vision ultra-claire du stack (flow diagram + 67 modules + 54 launchd + 150 scripts + 15 DBs)

### 2026-04-21 midi — Pangu + ECMWF OpenData install

**Deps installées** :
```
uv add onnxruntime cfgrib cdsapi xarray netCDF4 ecmwf-opendata
brew install eccodes
```
- `onnxruntime` : 1.24.4 avec `CoreMLExecutionProvider` (M5 Metal)
- `ecmwf-opendata` : 0.3.26 — **GRATUIT** pour HRES + ENS 51-membres

**Modules créés** :
- `src/pmhedge/alpha/pangu_runner.py` — ONNX inference M5/CPU fallback
- `src/pmhedge/alpha/era5_ingest.py` — CDS API fetch
- `src/pmhedge/alpha/ecmwf_client.py` — stub payant (inutile, OpenData gratuit)
- `src/pmhedge/alpha/mesonet_client.py` — stub (free tier prêt)
- `src/pmhedge/execution/market_maker.py` — stub maker rebate

**Scripts** :
- `scripts/setup_pangu.py` — download + verify
- `scripts/run_pangu_cycle.py` — fetch ERA5 + run Pangu + insert as 13e NWP source
- `scripts/train_pangu_city.py` — stub per-city fine-tune

**Pangu download** : EN COURS via curl --retry 10 en background. Premier DL 1.1GB corrompu (Protobuf parse fail), retry.
URL : `https://get.ecmwf.int/repository/test-data/ai-models/pangu-weather/pangu_weather_24.onnx`
Size attendue : 1,181,711,187 bytes (~1.18 GB)
File path : `models/pangu_weather_24.onnx`

### 2026-04-21 après-midi — Research Pipeline 2-pôles

**Structure** : `research/pole_stats/` + `research/pole_analysis/` + `research/data/` + `research/outputs/`

**Scripts créés** :
- `research/pole_stats/01_city_discovery.py` — 38 villes, $288M volume historique
- `research/pole_stats/02_city_trajectories.py` — 46 villes, ACF/runs/regimes/mean-reversion/diurnal

**Findings critiques** :

1. **London $65.3M volume UNTAPPED** → jamais configurée avant, maintenant ENABLED
2. **9 villes activées** : London, Shanghai, Toronto, Sao Paulo, Madrid, Munich, Amsterdam, Moscow, Istanbul, Busan
3. **Shanghai ACF lag-7 = 0.92** (persistance massive → edge continuation tradable)
4. **Hong Kong 11j max up-run** (heatwaves persistantes)
5. **Kuala Lumpur/Jakarta/Singapore half-life 1.5-2.2j** (climat tight, markets efficient, pas d'edge facile)

**Outputs** :
- `research/outputs/01_discovery.md` + `cities_universe.json`
- `research/outputs/02_trajectories.md` + `city_trajectories.json`
- `research/outputs/analysis_01_priority_actions_2026-04-21.md`

## BLOQUANTS user

1. **Pangu download** : en cours (135MB/1.18GB, ~15% au moment du context-clear). Check status avec `ls -lh models/pangu_weather_24.onnx`
2. **Compte Copernicus CDS** : user doit créer compte + accepter licences ERA5
   - URL : https://cds.climate.copernicus.eu/user/register
   - Licences : reanalysis-era5-pressure-levels + reanalysis-era5-single-levels
   - Après : `~/.cdsapirc` avec clé API
3. **Debug London/Toronto/Sao Paulo 0 signaux** : le scanner voit les markets mais 0 signaux dans signal_log. Investigation en pending.
4. **Review `economic-thesis.md`** : ajouter `THESIS VALIDATED BY PAUL ON YYYY-MM-DD` pour débloquer G1 exit

## Actions P0 au reprise de session

1. **Check Pangu download complet** : `ls -lh /Users/paul/polymarket-hedge/models/pangu_weather_24.onnx`
   - Si >= 1.1GB : `uv run scripts/setup_pangu.py --verify`
   - Si incomplet : relance `curl -L --retry 10 -C - -o ... $URL`
2. **Check Copernicus setup** : `ls ~/.cdsapirc`
   - Si existe : `uv run scripts/run_pangu_cycle.py --steps 3`
   - Si absent : rappel à user
3. **Debug London 0 signaux** : scan manuel verbose
4. **Continuer pôle stats 03-07** et **pôle analysis 02-04**

## Commandes essentielles

```bash
cd /Users/paul/polymarket-hedge

# Status & monitoring
uv run python scripts/trade_status.py          # snapshot CLI
uv run python scripts/alpha_tui.py             # TUI Rich refresh 5s
open http://127.0.0.1:8090                     # web dashboard

# Research pipeline
uv run python research/pole_stats/01_city_discovery.py
uv run python research/pole_stats/02_city_trajectories.py
uv run python research/pole_analysis/01_priority_actions.py

# City tuning
uv run python scripts/city_optimizer.py        # dry-run
uv run python scripts/city_optimizer.py --apply
uv run python scripts/city_deep_dive.py --city <slug>

# Pangu (après ~/.cdsapirc setup)
uv run python scripts/setup_pangu.py --verify
uv run python scripts/run_pangu_cycle.py --steps 3

# Scanner manuel
uv run python scripts/run_alpha_live.py --once

# Reconcile + close trades
uv run python scripts/reconcile_from_obs.py
```

## Scripts importants par rôle

### Pipeline live
- `scripts/run_alpha_live.py` — scanner principal, loop 300s
- `src/pmhedge/alpha/signal_generator.py::persist_signal` ligne 526 — orchestre filtres + execute
- `src/pmhedge/alpha/live_executor.py::execute_signal` — paper fill + trade_log
- `src/pmhedge/alpha/bucket_router.py::route` — classification S/A/B/C/KILL

### Filtres (ordre d'application dans persist_signal)
1. `is_alpha_enabled(alpha_type)` — kill switch global
2. `session_filter.should_block(ts)` — h06-09 UTC block
3. `ttr_filter.is_blocked(city, ttr_h)` — per-(city, bucket) denylist
4. `get_config(city_slug).status == DISABLED` — city kill
5. Risk manager Kelly/exposure
6. `execute_signal()` → paper fill → trade_log

### Settlement (cron)
- `scripts/reconcile_from_obs.py` → signal_outcomes + close_resolved_trades (09:20 UTC)

### Research (2-pôles)
- `research/pole_stats/` — stats brutes auto
- `research/pole_analysis/` — interpretation + actions

## Doublons à surveiller

- 11 DBs legacy restent (bracket_scalper_trades, pmhedge, coldmath_trades, etc.) — non archivées car refs existent. TODO : audit complet.
- 150 scripts dans `scripts/` — 30-40% probablement legacy (voir `ARCHITECTURE.md` pour liste canonique)

## Principes Paul

- Kelly 0.40 default (pas plus sans validation)
- Weather only (pas d'autres marchés)
- Paper 15j avant live money
- Pas de fix cosmétiques — root cause
- Tester avant de dire "done"
- Pas d'emojis, pas de violet, accents FR

## Memory notes

- Projet mémorisé : `memory/polymarket_paper_session_1.md`
- Global MEMORY : `MEMORY.md`
- Paper session finit 2026-05-05 (15 jours)

## Quick health check à la reprise

```bash
# Scanner toujours up?
launchctl list | grep alpha-live-runner

# Dashboard web up?
curl -s http://127.0.0.1:8090/api/state | python3 -c "import json,sys; d=json.load(sys.stdin); print(f'P&L: \${d[\"total\"][\"pnl\"]:+,.2f}, trades: {d[\"total\"][\"trades\"]}')"

# Circuit breaker state?
sqlite3 alpha_data_hub.db "SELECT status, reason FROM alpha_states WHERE alpha_type='__CIRCUIT_BREAKER__'"

# Trades aujourd'hui
sqlite3 alpha_data_hub.db "SELECT COUNT(*) FROM trade_log WHERE open_ts > unixepoch('$(date -u +%Y-%m-%d)')"
```

## Pièges connus

- `KMP_DUPLICATE_LIB_OK=TRUE` requis avant `uv run` sur macOS (OpenMP conflict)
- Python 3.14 sur le venv (attention compat deps)
- Certaines tables SQLite ont `obs_ts` pas `ts` (obs_temperature vs signal_log)
- Signal metadata stocké en TEXT JSON, utiliser `json_extract(metadata, '$.key')`
- `city_slug` lowercase dans nos tables, `city` capitalized dans Polymarket

## Related

- [[ARCHITECTURE]] — structure complète
- [[STATE-HANDOFF]] — état global actualisé
- [[MODEL-STATE-COMPLETE]] — snapshot models
- [[TODO-pending]] — punch list
- [[city-optimization]] — kill/boost per-city
- [[_MOC]] — hub central
