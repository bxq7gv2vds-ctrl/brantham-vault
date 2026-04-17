---
name: Quick-Start Guide Polymarket Hedge Fund
description: Guide opérationnel — comment utiliser le système alpha au quotidien
type: guide
created: 2026-04-17
tags: [polymarket, quick-start, operational]
---

# Quick-Start Guide — Polymarket Hedge Fund

Guide opérationnel. Le système tourne en autonome via launchd. Ce doc = comment interagir.

## Services autonomes (déjà actifs via launchd)

| Service | Plist | Fréquence | Action |
|---|---|---|---|
| Alpha live runner | `com.paul.polymarket-alpha-live-runner` | Continu (loop 5min) | Scan markets, génère signaux, persist |
| NWP ingestion | `com.paul.polymarket-alpha-nwp-ingest` | 4x/jour (01:30, 07:30, 13:30, 19:30) | Ingère GEFS+ICON+ECMWF+HRRR |
| METAR archive | `com.paul.polymarket-alpha-metar-archive` | Toutes les 2h | Rolling 30-day METAR |
| Health check | `com.paul.polymarket-alpha-health-check` | Toutes les 15min | Alerte si source DOWN |
| Reconcile + report | `com.paul.polymarket-alpha-reconcile` | 09:15 quotidien | Daily paper shadow report |

**Vérifier que tout tourne** :
```bash
launchctl list | grep polymarket-alpha
```

**Logs** :
- `/Users/paul/polymarket-hedge/logs/alpha-live.log` (signaux live)
- `/Users/paul/polymarket-hedge/logs/alpha-nwp.log` (ingestion NWP)
- `/Users/paul/polymarket-hedge/logs/alpha-metar.log` (METAR archiver)
- `/Users/paul/polymarket-hedge/logs/alpha-health.log` (health checks)
- `/Users/paul/polymarket-hedge/logs/alpha-reconcile.log` (daily reports)

## Commandes manuelles

### Vérifier santé system
```bash
cd /Users/paul/polymarket-hedge
uv run scripts/health_check.py              # console seulement
uv run scripts/health_check.py --alert      # + Telegram si problème
```

### Backtest
```bash
uv run scripts/alpha_backtest.py --bankroll 10000
uv run scripts/city_focused_backtest.py --bankroll 10000
```

### Scan manuel une fois
```bash
uv run scripts/run_alpha_live.py --once --no-telegram --min-edge 0.04 --bankroll 1000
```

### Archive METAR immédiat
```bash
uv run scripts/archive_metar.py
```

### Ingérer NWP immédiat
```bash
uv run scripts/ingest_nwp_daily.py --days 5
uv run scripts/ingest_nwp_daily.py --city paris --days 2   # single city
```

### Reconciler + report
```bash
uv run scripts/reconcile_and_report.py --alert
```

## Setup ERA5 (bloquant pour training ML)

```bash
# 1. Créer compte Copernicus
#    https://cds.climate.copernicus.eu/
#    Accepter license ERA5 hourly single levels

# 2. Créer ~/.cdsapirc :
cat > ~/.cdsapirc <<EOF
url: https://cds.climate.copernicus.eu/api
key: <UID>:<TOKEN>
EOF

# 3. Installer deps
uv add cdsapi xarray netCDF4

# 4. Download 5 ans ERA5 (~1-3h selon queue Copernicus)
uv run scripts/backfill_era5.py --years 5

# 5. Train XGBoost post-proc
uv run scripts/train_xgboost_post.py
```

## Queries DB utiles

### Signaux émis dernières 24h
```bash
sqlite3 /Users/paul/polymarket-hedge/alpha_data_hub.db "
SELECT alpha_type, side, entry_price, est_prob, edge, size_usdc, datetime(emit_ts,'unixepoch')
FROM signal_log ORDER BY emit_ts DESC LIMIT 20;
"
```

### Top cities en PnL
```bash
sqlite3 /Users/paul/polymarket-hedge/bracket_scalper_trades.db "
SELECT city, COUNT(*) n, ROUND(SUM(pnl),2) pnl, ROUND(100.0*SUM(won)/COUNT(*),1) wr
FROM scalper_signals WHERE resolved=1
GROUP BY city ORDER BY pnl DESC LIMIT 10;
"
```

### Paper shadow resolved count
```bash
sqlite3 /Users/paul/polymarket-hedge/alpha_data_hub.db "
SELECT COUNT(*) total, SUM(outcome_yes) yes_wins,
       ROUND(SUM(realized_pnl),2) total_pnl
FROM signal_outcomes;
"
```

## Dépannage

### Live runner ne démarre pas
```bash
launchctl unload ~/Library/LaunchAgents/com.paul.polymarket-alpha-live-runner.plist
launchctl load ~/Library/LaunchAgents/com.paul.polymarket-alpha-live-runner.plist
tail -50 /Users/paul/polymarket-hedge/logs/alpha-live.log
```

### Aucun signal émis
1. Vérifier health : `uv run scripts/health_check.py`
2. Vérifier markets fetched : scan manuel avec `--once`
3. Vérifier NWP freshness : `uv run scripts/ingest_nwp_daily.py --days 2`
4. Peut-être `min_edge` trop haut : essayer `--min-edge 0.03`

### Signaux aberrants (edge > 40%)
Filter config auto-reject depuis v1 :
- `min_ensemble_members=20` (rejette NWP partials)
- `min_market_volume=$200` (rejette markets dead)
- `max_edge=0.40` (rejette aberrants)

Ajuster dans `src/pmhedge/alpha/signal_generator.py` → `SignalGenConfig`.

## Roadmap utilisateur

### Cette semaine
- [ ] Laisser tourner paper shadow 7 jours
- [ ] Review logs + signal_log quotidiennement
- [ ] Setup ERA5 + train XGBoost

### Semaine +2
- [ ] 30 jours paper shadow complet
- [ ] Daily reports dans `vault/brantham/polymarket/reports/`
- [ ] Analyze drift (WR realized vs expected)

### Semaine +3
- [ ] Décision go/no-go basée sur 30j track record
- [ ] Si go : fund wallet Polymarket $500-1000
- [ ] Install py-clob-client + wire live execution
- [ ] Start small, scale graduellement

## Related

- [[_MOC|Polymarket Hub]]
- [[architecture|Architecture]]
- [[findings|Findings]]
- [[roadmap|Roadmap]]
- [[reports/city-focused-projection-2026-04-17|Dernière projection]]
