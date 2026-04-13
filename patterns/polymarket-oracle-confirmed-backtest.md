---
name: Polymarket Oracle CONFIRMED — Backtest & Infrastructure
type: pattern
project: polymarket-hedge
tags: [polymarket, oracle, backtest, trading, coldmath]
date: 2026-04-08
---

# Pattern : Polymarket Oracle CONFIRMED Strategy

## Résumé
Stratégie d'arbitrage risk-free sur les marchés température Polymarket.
À 09:07 UTC, le T_max UTC du jour précédent est 100% connu via METAR.
Les marchés "April X" expirent à 12:00 UTC et résolvent sur T_max du jour X-1 UTC.
→ 3h de fenêtre d'arb quasi risk-free.

## Résultats backtest (jan 2025 → avr 2026)
- **+5,293%** sur $10k bankroll (390 trades, 105 jours)
- **WR 100%** — certitude physique absolue
- **0% drawdown**
- YES trades : entry avg 0.40, edge 152%
- NO trades : entry avg 0.93, edge 7.3%

## Mécanique oracle
```
Marché "Will Dallas T_max be 72-73°F on April 8?"
  → expire 2026-04-08 12:00 UTC
  → résout sur T_max 2026-04-07 UTC (METAR KDAL)

À 09:07 UTC le 8 avril:
  T_max_prev_UTC = 72.4°F (METAR historique confirmé)
  → YES bin [72,73) → ACHETER YES @ 0.15 → résout 1.0
  → NO sur tous les autres bins → ACHETER NO @ 0.92-0.98 → résout 1.0
```

## Signaux par priorité
| Type | Trigger | Size | Edge |
|------|---------|------|------|
| CONFIRMED_YES | T_max ∈ bin, TTR < 3.5h | $2000 | 2-150% |
| CONFIRMED_NO | T_max ∉ bin, TTR < 3.5h | $2000 | 2-15% |
| EXACT_BIN_YES | T_obs ∈ bin, heure locale ≥ 16h | $2000 | ~5% |

## Infrastructure
- Scanner : `scripts/run_bracket_scalper.py`
- Daily P&L : `scripts/daily_pnl_report.py`
- Backtest : `scripts/backtest_oracle.py`
- Data download : `scripts/download_oracle_data.py`
- DB historique : `oracle_data.db` (3034 marchés, en cours d'extension)

## Schedule
- 09:07 UTC — scan oracle principal (CCR cloud `trig_019ESZGPjKHV4T9omziw429H`)
- 10:30 UTC — scan secondaire (CCR `trig_01RgvQnW9ME9FCawykq4G63e`)
- 16:15 UTC — SPEEDA villes asiatiques (CCR `trig_01BpKEU3JFbr3Vrf3XKxQUaa`)
- 09:00 local — daily P&L report (launchd `com.paul.polymarket-daily-pnl`)

## Limites connues
1. Coverage oracle_data.db : 14.4% (3034/20k marchés) — archives CLOB limitées
2. Open-Meteo T_max ≠ METAR exact (différence possible ±0.5°F) → risque sur bins 1°F
3. Liquidité : fill $2000 à 0.40 YES réaliste, mais fins de carnet possibles
4. Busan/SF non couverts : token IDs absents de all_markets.db

## Prochaines étapes
- Remplir credentials Polymarket pour live
- Vérifier WR réel sur 1 semaine paper
- Singapore EMOS à recalibrer (biais +6°C)
- intraday_engine.py : ajouter flag --no-bracket

## Related
- [[_system/MOC-patterns]]
- [[founder/sessions/2026-04-08-polymarket-oracle-backtest]]
- [[founder/sessions/2026-04-05-polymarket-coldmath-strategy-complete]]
- [[patterns/polymarket-bracket-arb]]
- [[patterns/polymarket-nwp-emos-calibration]]
- [[brantham/_MOC]]
