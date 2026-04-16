---
name: Auto-critique modèle météo Polymarket
description: Analyse critique de chaque hypothèse du modèle XGBoost weather. Ce qui peut foirer, ce qu'il faut vérifier.
type: decision
date: 2026-04-16
status: in-progress
---

# Auto-critique — Modèle météo Polymarket

## Hypothèses à challenger AVANT de faire confiance au modèle

### H1: "XGBoost multi-NWP va battre un seul modèle NWP"

**Pourquoi ça pourrait être faux :**
- Open-Meteo historical-forecast API renvoie le forecast ARCHIVÉ — mais quel run? Le run de 00:00 UTC ou 12:00 UTC? Si c'est le run de 12:00, c'est un forecast qui n'était PAS disponible à 00:00 quand on doit trader.
- Les 4 modèles NWP (ECMWF, GFS, ICON, JMA) sont fortement corrélés — l'ensemble n'ajoute peut-être que ~2% de skill vs le meilleur seul.
- XGBoost avec 40 features et ~300 samples par ville = overfitting quasi garanti. La walk-forward CV devrait catcher ça mais avec 6 folds de 1 mois chacun, la variance est énorme.

**Comment vérifier :**
- Comparer XGBoost vs simple moyenne des 4 NWP (pas besoin de ML pour ça)
- Vérifier le run time des forecasts Open-Meteo
- Tester avec max_depth=2 et n_estimators=50 (modèle plus simple)

### H2: "Les erreurs laggées (J-1, J-2) apportent de l'info"

**Pourquoi ça pourrait être faux :**
- L'autocorrélation des biais NWP dépend du régime météo. En situation stable (anticyclone), le biais est constant. En situation perturbée (front), il change brutalement. Le lag est informatif dans un cas mais pas l'autre.
- Le marché Polymarket intègre probablement déjà les biais récents (les traders voient les mêmes erreurs hier).

**Comment vérifier :**
- Mesurer l'autocorrélation réelle des erreurs ECMWF→WU par ville
- Tester le modèle SANS les features laggées et comparer

### H3: "12 mois de données suffisent"

**Pourquoi ça pourrait être faux :**
- La météo a des cycles saisonniers forts. 12 mois = 1 cycle. Le modèle voit chaque mois UNE SEULE FOIS en train → il apprend la saisonnalité comme du bruit.
- Avec 6 villes × 365 jours = 2190 samples, et 40 features, le ratio samples/features = 55. C'est limite pour XGBoost.

**Comment vérifier :**
- Utiliser les 2+ ans de données WU disponibles
- Réduire les features à <15 (feature selection)

### H4: "Le bracket accuracy OOS est la bonne métrique"

**Pourquoi ça pourrait être faux :**
- On veut BATTRE LE MARCHÉ, pas battre un random baseline. Le marché à T-12h price le bracket gagnant à 34%. Si notre modèle a 38% accuracy mais met la probabilité sur le MÊME bracket que le marché, on n'a pas d'edge — on confirme juste le marché.
- La vraie métrique est : quand notre modèle DISAGREE avec le marché, qui a raison?

**Comment vérifier :**
- Comparer notre top bracket vs le top bracket du marché (prix le plus élevé)
- Mesurer le PnL de la stratégie "acheter quand notre prob > prix marché + 5%"
- Si notre modèle disagree avec le marché sur 20% des cas et a raison 60% du temps → edge

### H5: "L'API Open-Meteo historical-forecast est fiable"

**Pourquoi ça pourrait être faux :**
- Open-Meteo peut archiver des forecasts RÉVISÉS (pas le forecast original du run 00:00)
- Les données peuvent avoir des trous (stations en maintenance)
- Le modèle JMA pour l'Asie n'est peut-être pas dans l'archive historical-forecast

**Comment vérifier :**
- Fetch une date récente (hier) et comparer avec le forecast actuel
- Vérifier la complétude par modèle

### H6: "Le marché Polymarket est battu par les NWP seuls"

**Pourquoi c'est probablement FAUX :**
- Le marché intègre DÉJÀ les NWP (les market makers utilisent les mêmes sources)
- Le marché intègre aussi les observations METAR en temps réel
- Le marché intègre le consensus des traders humains (local knowledge)
- Pour battre le marché il faut soit un MEILLEUR modèle, soit une INFO PLUS RAPIDE

**Le seul avantage potentiel :**
- Calibration spécifique NWP→WU station (le marché ne corrige peut-être pas précisément pour la station WU)
- Timing: notre bot trade à 00:00 UTC quand le marché est moins liquide
- Systématisation: on trade TOUTES les villes TOUS les jours sans exception

## Décision

Continuer la construction du modèle mais avec des attentes réalistes :
- Si accuracy OOS > 38% et disagree-accuracy > 50% → déployer
- Sinon → le marché est efficient sur la météo, pivoter

## Related

- [[patterns/polymarket-weather-mega-model]]
- [[_system/MOC-decisions]]
