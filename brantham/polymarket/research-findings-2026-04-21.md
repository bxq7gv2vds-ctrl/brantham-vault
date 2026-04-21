---
name: Polymarket Research Pipeline Findings 2026-04-21
description: Synthèse des 12 scripts research (pôle stats 01-07 + pôle analysis 01-05). Trouvailles actionnables sur skill NWP, calibration σ, momentum, corrélations.
type: analysis
project: brantham/polymarket
created: 2026-04-21
tags: [polymarket, research, findings, calibration, nwp, bma]
priority: high
---

# Polymarket Research Pipeline — Findings 2026-04-21

Session research complète : 7 scripts stats + 5 scripts analysis.
Entrée point : `/Users/paul/polymarket-hedge/research/`

## Métriques globales

- **46 villes** analysées avec historique METAR
- **368-405 jours** d'observations par ville
- **2 547 signaux** scorés via bracket sweep
- **1 035 paires** cross-city corrélées

## Top findings actionnables

### 1. σ sous-estimé massivement dans certaines villes

Fichier : `research/outputs/06_sigma_empirical.md`

| City | σ prédit | σ empirique | shrinkage | Action |
|------|---------:|------------:|----------:|--------|
| Seoul | 1.15 | 2.52 | **2.00** | SEVERE_EXPAND |
| Shanghai | 1.01 | 1.07 | 1.43 | EXPAND |
| Sao Paulo | 1.17 | 1.40 | 1.37 | EXPAND |
| Toronto | 1.47 | 1.82 | 1.38 | EXPAND |
| Wuhan | 1.06 | 1.03 | 1.34 | EXPAND |
| NYC | 1.20 | 1.49 | 1.27 | EXPAND |
| Tokyo | 1.08 | 0.95 | 1.18 | EXPAND |

**Implication** : sans σ shrinkage, les bets deep_OTM sur ces villes sous-estiment le risque queue. Seoul particulièrement dangereux.

**Action** : wire un multiplier σ par ville dans `signal_generator.py` (avant le calcul de `prob_bracket`).

### 2. NWP skill score domine par ville — ECMWF clear winner

Fichier : `research/outputs/03_forecast_skill.md`

- **ECMWF gagne 29/46 villes** (MAE médian < 0.5°C)
- **ICON_ENS gagne en Asie humide** (Jakarta, KL, Shenzhen, Singapore, Shanghai)
- **AIFS** (ML model) gagne à Mexico City + Taipei
- **GRAPHCAST** gagne à Beijing
- **CMA** gagne à Wuhan (modèle chinois, local advantage)

**Implication** : le BMA weights par défaut doit être tilted vers ECMWF globalement, avec overrides ICON_ENS pour Asie humide + CMA pour Chine.

**Action** : mettre à jour `ensemble_weights` table avec priors per-city dérivés de `research/data/forecast_skill.json`.

### 3. Correlation clusters — concentration risk identifiée

Fichier : `research/outputs/analysis_02_cross_city_correlation.md`

Paires ρ > 0.90 (zero diversification) :
- Austin ↔ Houston : 0.91
- Hong Kong ↔ Shenzhen : 0.91
- Boston ↔ NYC : 0.90

Clusters synoptiques identifiés :
- **US South** : Austin/Dallas/Houston/Atlanta (ρ moyen 0.80+)
- **US Northeast** : Boston/NYC/Toronto (ρ 0.75+)
- **Europe NW** : London/Paris/Amsterdam (ρ 0.80+)
- **China South** : HK/Shenzhen/Taipei (ρ 0.65+)

**Implication** : des trades simultanés YES sur Austin + Houston = double-exposition au même regime. Pas de diversification réelle.

**Action** : ajouter un cluster cap dans `risk_manager.py` — max exposure par cluster synoptique.

### 4. Calibration 90% coverage empirique — 18/44 OVERCONFIDENT

Fichier : `research/outputs/05_outcome_distributions.md`

Villes avec cov90 < 0.70 (σ trop petit) :
- Seoul cov90 = 0.15 (!)
- Shanghai cov90 = 0.33
- Wuhan cov90 = 0.58
- Toronto cov90 = 0.62

Villes WELL_CALIBRATED (cov90 ≈ 0.85-0.95) : Paris, Madrid, Phoenix, London, SF, Milan, Moscow, Amsterdam, Houston, Istanbul.

**Implication** : trader sur Seoul avec le modèle actuel = miser sur une gaussienne trop serrée. Les tails (>95%+) sont massivement sous-prisées.

**Action** : désactiver (ou shrink aggressivement) Seoul/Shanghai/Wuhan tant que les σ ne sont pas recalibrés.

### 5. Momentum candidates — continuation alpha

Fichier : `research/outputs/analysis_05_momentum_patterns.md`

Shanghai identifiée en pôle stats 02 avec ACF(7) = 0.92 — persistance massive sur 7j.

**Implication** : une anomalie chaude à Shanghai aujourd'hui → anomalie chaude demain 92%. Tradable comme facteur de continuation dans les brackets upper_tail YES.

**Action** : créer un feature `persistence_factor` dans `feature_engineering.py` utilisant l'ACF historique par ville.

### 6. Bracket microstructure par ville

Fichier : `research/outputs/04_microstructure.md`

- Spread implicite (1 - yes - no) : très faible (<2c sur la plupart des villes)
- YES price médian < 0.05 sur la majorité des villes (deep OTM dominant)
- NO price médian > 0.95 (symétrique — deep OTM NO)
- Bracket width typical : ~0.5-1°C (narrow_bin très majoritaire)

## Recommandations par ville — Top 10

Fichier complet : `research/outputs/analysis_04_model_recommendations.md` (46 villes avec actions chiffrées).

Extraits critiques :
- **Seoul** : σ × 2.00, Kelly cut aggressif
- **Shanghai** : σ × 1.43, Kelly cut (cov90 33%)
- **Beijing** : Kelly cut de 0.41 → 0.20 (cov90 60%)
- **NYC** : σ × 1.27, BMA = [ECMWF, UKMO, JMA]
- **Toronto** : σ × 1.38, BMA = [ECMWF, NBM, AIFS]

## Next steps

1. Wire σ shrinkage dans `signal_generator.py` ligne ~336 (avant `prob_bracket`)
2. Wire per-city BMA priors dans `ensemble_weights` table
3. Ajouter cluster cap dans `risk_manager.py`
4. Désactiver Seoul + Shanghai temporairement en city_config (SEVERE_EXPAND)
5. Créer persistence_factor feature

## Fichiers générés

```
research/data/
  ├── forecast_skill.json
  ├── microstructure.json
  ├── outcome_distributions.json
  ├── sigma_empirical.json
  ├── bracket_sweep.json
  ├── cross_city_correlation.json
  ├── hedge_detection.json
  ├── model_recommendations.json
  └── momentum_patterns.json

research/outputs/
  ├── 03_forecast_skill.md
  ├── 04_microstructure.md
  ├── 05_outcome_distributions.md
  ├── 06_sigma_empirical.md
  ├── 07_bracket_sweep.md
  ├── analysis_02_cross_city_correlation.md
  ├── analysis_03_hedge_detection.md
  ├── analysis_04_model_recommendations.md
  └── analysis_05_momentum_patterns.md
```

## Related

- [[_MOC]]
- [[CONTINUATION-PROMPT]]
- [[TODO-pending]]
- [[ARCHITECTURE]]
- [[city-optimization]]
- [[_system/MOC-decisions]]
