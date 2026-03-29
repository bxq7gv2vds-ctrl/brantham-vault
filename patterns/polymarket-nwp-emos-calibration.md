---
name: NWP EMOS Calibration pour Prediction Markets
description: Calibrer des prévisions NWP ensemble avec EMOS+BMA pour obtenir des probabilités fondamentales précises sur les marchés météo Polymarket
type: pattern
tags: [trading, nwp, emos, calibration, polymarket]
---

# Pattern : NWP EMOS Calibration pour Prediction Markets

## Problème
Les marchés météo Polymarket ont des prix qui ne reflètent pas la vrai probabilité météo. La probabilité fondamentale "naïve" (compter les membres NWP au-dessus d'un seuil) est biaisée car les modèles NWP ont des biais systématiques par ville et saison.

## Solution : EMOS + BMA

### EMOS (Ensemble Model Output Statistics)
Non-Homogeneous Gaussian Regression :
```
T_obs ~ N(μ_c, σ_c)
μ_c = a + b × μ_ens           (correction du biais)
σ_c = √(c + d × var_ens)     (correction de la dispersion)
```
Fit par MLE par (ville, mois) sur 731 jours historiques.

### BMA (Bayesian Model Averaging)
Poids adaptatifs basés sur CRPS historique par modèle :
```
w_i = (1/CRPS_i) / Σ(1/CRPS_j)
μ_BMA = w_GFS × μ_GFS + w_ICON × μ_ICON + w_GEM × μ_GEM
```

### Données sources
- Observations : `archive-api.open-meteo.com` (2 ans)
- Prévisions historiques : `historical-forecast-api.open-meteo.com` (3 modèles déterministes)
- Prévisions live : `ensemble-api.open-meteo.com` (89 membres)

### Cohérence clé
**var_ens doit être la variance inter-modèle** (entre les 3 moyennes GFS/ICON/GEM), pas la variance des 89 membres. C'est ce qu'on utilise à l'entraînement (données historiques).

## Résultats
- CRPS NYC = **1.01°F** — précision pro
- 444 params (37 villes × 12 mois), 148 BMA weights
- Calibration complète en ~6 secondes
- Stocké : `/Users/paul/polymarket-hedge/emos_cache.db`

## Code
```python
# Calibration one-time
cal = EMOSCalibrator()
await cal.fit_all()  # 6s pour 37 villes

# Usage
nwp = NWPForecast(calibrator=cal)
p = await nwp.get_fundamental_prob(
    "Will the highest temperature in NYC on March 31 be above 74°F?"
)
```

## Gotchas
1. Parseur de questions : filtrer les nombres de date (ex: "March **31**") avec `date_nums` exclusion
2. `var_ens` = inter-model variance, pas all-members variance
3. Endpoint météo Polymarket : `public-search?q=temperature` (PAS `/markets?search=weather`)
4. DB path : utiliser `Path(__file__).resolve()` pour éviter les chemins relatifs

## Related
- [[founder/sessions/2026-03-29-polymarket-hedge-engine]]
- [[_system/MOC-patterns]]
