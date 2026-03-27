---
type: decision
project: weather-alpha
date: 2026-03-18
status: active
tags: [backtest, calibration, model, NWP]
alternatives_considered: [keep-era5-with-downweight, keep-jma-with-penalty]
linked_assumptions: []
review_at: 2026-04-17
---

# Backtest v5 — Rebuild model for ultra-precise calibration

## Context
Audit complet du modele v3 a revele 7 problemes critiques: ERA5 look-ahead bias (corr 0.993 avec METAR = reanalyse, pas forecast), JMA inutilisable (MAE 4x GFS), calibration terrible sur trades liquides (ECE=0.18), SELL 96c sous-estime de 16pts, LOW_TEMP BSS negatif, stations KNYC/KORD/KMIA avec BSS negatif.

## Alternatives
1. **Garder ERA5 avec downweight** — Non: reanalyse = look-ahead, la corr 0.993 prouve que c'est des observations, pas des forecasts
2. **Garder JMA avec penalite** — Non: MAE 4x pire que GFS, pollue l'ensemble meme avec poids faible
3. **Rewrite complet (choisi)** — Clean NWP ensemble (GFS+ICON+GEM) + calibration granulaire

## Decision
Rewrite complet `backtest_v5_calibrated.py`:
- Ensemble: GFS + ICON + GEM uniquement
- Bias correction per-(station, model, ctype, season)
- Per-station pooled_std
- Climatology prior blending (80/20 model/climo, adaptatif)
- Per-(station, ctype) isotonic calibration avec fallbacks
- LightGBM avec features climo + season + station skill
- Station+ctype filtering (BSS < 0 = desactive)

## Resultats v5 vs v3
| Metrique | v3 (ERA5) | v5 (clean) |
|----------|-----------|------------|
| P&L | $56,461 | $52,963 (-6%) |
| Sharpe | 13.71 | 13.07 |
| ECE (ALL) | 0.18 | 0.049 |
| BSS (ALL) | N/A | +0.073 |

## Problemes restants
- SELL calibration gap 30pts (model underestime)
- LIQUID trades BSS negatif (-0.115)
- LOW_TEMP BSS negatif (-0.113)
- Stations KDEN/KMIA/KNYC/KORD BSS negatif sur test

## Consequences
- Le "vrai" P&L sans ERA5 est ~6% plus bas — c'est le signal reel
- Calibration globale bien meilleure (ECE 0.18 -> 0.049)
- SELL strategy reste rentable grace au payoff asymetrique (gain 93c vs perte 7c)

## Review
- 30d: [pending] Verifier performance en production live
- 60d: [pending]
- 90d: [pending]

## Related
- [[_system/MOC-decisions]]
- [[brantham/_MOC]]
- [[reports/2026-03-18-daily]]
- [[website/research/2026-03-18-keyword-research-distressed-ma]]
- [[website/research/2026-03-18-indexation-ranking-audit]]
- [[website/audits/2026-03-18-brantham-seo-indexation-audit]]
- [[website/strategies/2026-03-18-fast-ranking-strategy]]
- [[website/sessions/2026-03-18]]
- [[brantham/patterns/backtest-hierarchical-calibration]]
- [[brantham/sessions/2026-03-18]]
- [[founder/decisions/2026-03-18-weather-alpha-dashboard-design-system]]
- [[founder/decisions/2026-03-18-mirofish-distilled-architecture]]
- [[founder/sessions/2026-03-18-weather-alpha-dashboard-redesign]]
- [[founder/strategy/current-strategy]]
