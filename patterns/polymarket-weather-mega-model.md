---
name: Polymarket Weather Prediction — Mega Model Architecture
description: Architecture complète du modèle de prédiction météo pour Polymarket. Résolutions WU, NWP multi-modèle, audit des biais, résultats OOS.
type: pattern
project: polymarket-hedge
tags: [polymarket, weather, prediction, xgboost, ecmwf, wu, model]
date: 2026-04-16
---

# Polymarket Weather — Mega Model

## Contexte

Session marathon 2026-04-14 → 2026-04-16. Objectif : trouver un edge exploitable sur les marchés météo Polymarket.

## Découvertes clés validées

### 1. Source de résolution
- **Polymarket résout via Weather Underground** (pas METAR, pas Open-Meteo)
- Chaque ville a une URL WU spécifique avec un ICAO précis
- Stations DIFFÉRENTES de METAR habituel : Shanghai=ZSPD (pas ZSSS), Taipei=RCSS, London=EGLC
- HK utilise HK Observatory (pas WU), Moscow utilise NOAA
- Résolution = T_max entier (°C) affiché par WU pour le jour LOCAL

### 2. WU API fonctionnelle
- Endpoint : `api.weather.com/v1/location/{ICAO}:9:{CC}/observations/historical.json`
- Clé : `e1f10a1e78da46f5b10a1e78da96f525` (embedded dans frontend WU)
- Matche Polymarket : 100% (Tokyo/Beijing/Shanghai), 90%+ (Seoul/Wuhan/Chengdu)
- Taipei exclu (ni RCSS ni RCTP ne matche — source WU inconnue)
- Profondeur historique : 2+ ans

### 3. Marché efficient
- WR marché (bracket le + cher = gagnant) : 34%
- ECMWF brut : 26% exact
- ECMWF + biais : 39% in-sample → **27% out-of-sample** (overfitting)
- Hedge 3 brackets YES : breakeven (coût 81¢ pour $1 payout à 80% WR)
- NO strategy : +EV mais centimes par trade
- Sum-of-brackets arb : pas exploitable (illiquidité)
- Longshot bias : **inversé** (petites cotes sous-performent leur prix)

### 4. Oracle timing
- Marchés ferment 12:00 UTC
- T_max Asie (UTC+8/+9) atteint ~06:00-08:00 UTC
- MAIS T_max change après 06:00 pour 40-100% des jours
- Le marché ajuste déjà les prix (bracket gagnant à 71% à 06:00 UTC)

## Architecture modèle v2 (en construction)

### Dataset
- **Target** : WU T_max integer (via WU API, 12 mois d'historique)
- **Features NWP** : ECMWF HRES, GFS, ICON, JMA (via Open-Meteo historical-forecast)
- **Features ensemble** : ECMWF ENS (51 membres), GFS GEFS spread
- **Features temporelles** : mois, DoY, DoW, erreurs NWP laggées (J-1, J-2, J-3)
- **Features dérivées** : accord inter-modèle (std, range), tendance T_max 3j
- **Villes** : tokyo, beijing, shanghai, seoul, chengdu, wuhan

### Modèle
- XGBoost regression → point forecast T_max
- Walk-forward CV (train 6 mois → test 1 mois, pas de lookahead)
- Conversion en probabilité bracket via résidus calibrés

### Seuil de validation
- **>38% bracket accuracy OOS** = edge exploitable vs marché 34%
- **>34%** = marginal, pas suffisant
- **<34%** = le marché nous bat, on arrête

## Bugs trouvés et corrigés (session)

1. **Settlement jour UTC-1** : `tmax_day = resolve_day - 24h` → fixé (supprimé le -24h)
2. **METAR hours=48 trop court** : données partielles → faux wins → fixé (settlement via Polymarket API)
3. **Mauvaises stations ICAO** : Shanghai ZSSS→ZSPD, Taipei RCTP→RCSS, London EGLL→EGLC
4. **Source résolution** : tout le backtest utilisait Open-Meteo → résultat faux. Corrigé avec WU API.

## Scripts clés
- `scripts/build_mega_dataset.py` — fetch WU + NWP 12 mois
- `scripts/train_model.py` — XGBoost walk-forward CV
- `scripts/wu_api_oracle.py` — fetch WU T_max temps réel
- `scripts/hedge3_oracle.py` — stratégie hedge 3 brackets (déployé VPS)
- `mega_dataset.db` — dataset d'entraînement
- `wu_tmax_dataset.db` — résolutions Polymarket vérifiées (827 city-dates)
- `metar_wu_validation.db` — validation METAR vs WU

## Prochaines étapes
1. Compléter le dataset 12 mois
2. Entraîner XGBoost, mesurer accuracy OOS
3. Si >38% : calibrer les probabilités bracket, backtester le PnL
4. Si <38% : explorer features supplémentaires ou conclure que le marché est efficient

## Related

- [[_system/MOC-patterns]]
- [[patterns/polymarket-convex-yes-complete-breakdown]]
- [[patterns/polymarket-coldmath-no-ev-analysis]]
- [[patterns/polymarket-oracle-confirmed-backtest]]
