---
type: pattern
project: weather-alpha
date: 2026-03-18
category: data
tags: [calibration, isotonic, NWP, backtest]
---

# Hierarchical Isotonic Calibration

## Problem
Une seule isotonic regression globale pour tout le modele = trop grossier. Les stations ont des biais differents, les contract types ont des distributions differentes.

## Solution
3 niveaux de calibration isotonique avec fallback:
1. Per-(station, ctype): si >= 50 samples
2. Per-ctype: fallback si pas assez par station
3. Global: dernier recours

```python
# Level 1: Per (station, ctype)
for station in stations:
    for ctype in ctypes:
        sub = train[(train["station_id"] == station) & (train["contract_type"] == ctype)]
        if len(sub) >= MIN_ISO_SAMPLES:
            iso = IsotonicRegression(y_min=0.01, y_max=0.99, out_of_bounds="clip")
            iso.fit(sub["prob"].values, sub["actual"].values)
            iso_models[(station, ctype)] = iso
```

Completer avec climatology prior blending AVANT isotonic:
```python
blended = alpha * model_prob + (1-alpha) * climo_prob
# alpha adaptatif: plus le spread inter-modeles est grand, plus on utilise climo
```

## When to Use
- Backtest avec plusieurs stations/contract types
- Quand ECE > 0.10 avec isotonic globale
- Quand certaines stations ont BSS negatif

## Gotchas
- Minimum 50 samples par sous-groupe sinon overfit
- Les station+ctype filtres sur train peuvent ne pas generaliser sur test
- Climo en Celsius dans le parquet, forecasts en Fahrenheit — convertir!
- Climatology parquet n'a que 183/366 DOYs — chercher DOY adjacent en fallback

## Related
- [[_system/MOC-patterns]]
- [[brantham/_MOC]]
- [[reports/2026-03-18-daily]]
- [[website/research/2026-03-18-keyword-research-distressed-ma]]
- [[website/research/2026-03-18-indexation-ranking-audit]]
- [[website/audits/2026-03-18-brantham-seo-indexation-audit]]
- [[website/strategies/2026-03-18-fast-ranking-strategy]]
- [[website/sessions/2026-03-18]]
- [[brantham/decisions/2026-03-18-backtest-v5-calibrated]]
- [[brantham/sessions/2026-03-18]]
- [[founder/decisions/2026-03-18-weather-alpha-dashboard-design-system]]
- [[founder/decisions/2026-03-18-mirofish-distilled-architecture]]
- [[founder/sessions/2026-03-18-weather-alpha-dashboard-redesign]]
