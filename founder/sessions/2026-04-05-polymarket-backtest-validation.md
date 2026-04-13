---
Session: 2026-04-05 — Polymarket Weather Backtest Validation
Project: polymarket-hedge
---

## Ce qui a été accompli

### Backtest PMXT (natif, sans NautilusTrader)
- Script `scripts/backtest_pmxt.py` — lit Parquet L2 de r2.pmxt.dev
- Problem découvert: PMXT garde ~42 jours max de données (window: 2026-02-22 à 2026-04-03)
- Marchés dans notre DB dataient de 2025 (trop anciens pour PMXT)

### Structure des marchés météo Polymarket
- Pas des marchés simples "above X" — ce sont des **BRACKET markets** (plages de 1°F/1°C)
- "Will Dallas be 73°F on March 4?" = P(73 ≤ T < 74) — pas P(T ≥ 73)
- final_price dans DB = 0.0 pour TOUS (bug: valeur par défaut non mise à jour)
- Outcomes réels calculés depuis Open-Meteo archive API

### Backtest retroactif sur price_bars
- Script `scripts/backtest_retroactive.py`
- NWP retroactif depuis historical-forecast-api.open-meteo.com (GFS + ICON)
- EMOS calibration depuis emos_cache.db (444 params, 37 villes)
- Outcomes réels: Open-Meteo archive API
- **Résultats validés**: profit factor 3.14, +$6.92 sur 16 trades (3 semaines)

### Paramètres optimaux identifiés
- min_edge = 0.10 (NWP - prix)
- buy_max = 0.15 (entrée seulement en dessous)
- tp_fraction = 0.70
- sl_fraction = 0.40
- Toutes les victoires TP = marchés bracket

### Insight clé
La stratégie EST intraday, pas hold-to-resolution:
- 7/9 TP sur marchés qui ont résolu NO
- On profite du repricing prix→NWP avant resolution
- Quand un modèle NWP se met à jour (GFS toutes les 6h), le marché se réequilibre
- Notre edge = réagir AVANT le marché

## Prochaines étapes
1. Paper trading avec spread réel
2. Backtest toutes les villes depuis max historique
3. Intégrer marchés bracket dans l'engine live
4. Spread grid Polymarket dans le modèle

## Related
[[brantham/_MOC]]
[[_system/MOC-decisions]]
[[patterns/polymarket-nwp-emos-calibration]]
