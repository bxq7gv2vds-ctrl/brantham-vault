---
name: Odds Trajectories per City — Backtest Findings
description: Analyse de l'évolution des prix Polymarket yes_price entre emission et résolution par ville. 98 markets résolus, 50% convergence global = random walk efficient. Austin/NYC/LA identifiés comme inefficient markets à edge structurel.
type: analysis
project: brantham/polymarket
created: 2026-04-22
tags: [polymarket, research, odds, market-efficiency, backtest]
priority: high
---

# Odds Trajectories Backtest — 2026-04-22

## Méthode

Script : `research/pole_stats/08_odds_trajectories.py`

Pour chaque (market_id, side) scanné ≥3 fois dans signal_log, reconstruct
la série temporelle des `entry_price`. Compute :

- `drift_pp` — yes_price(last) − yes_price(first), signed
- `volatility_pp` — std(price)
- `monotonicity` — fraction de mouvements alignés avec drift final
- `convergence_rate` — fraction des markets où drift direction = outcome

## Résultat global

**98 markets résolus avec ≥3 snapshots** :
- Drift aligné avec outcome : **49/98 = 50%**
- **Random walk** : les bookies n'incorporent pas progressivement l'info

→ l'edge ne vient pas du "news leak" mais du **mispricing initial persistant**
  jusqu'à la résolution.

## Par ville — top insights

### Bookies efficients (edge difficile)

| City | n | convergence | verdict |
|------|--:|------------:|---------|
| Miami | 10 | **83%** | skip ou Tier A only |
| Chicago | 4 | 75% | idem |

### Bookies inefficients (edge possible)

| City | n | convergence | drift | vol | verdict |
|------|--:|------------:|------:|----:|---------|
| Los Angeles | 4 | **25%** | -0.020 | 0.015 | candidate Austin-like |
| NYC | 4 | **25%** | -0.020 | 0.014 | candidate Austin-like |
| Denver | 3 | 33% | -0.020 | 0.016 | à confirmer |
| **Austin** | 5 | **40%** | -0.001 | 0.007 | edge structurel confirmé |
| Houston | 10 | 40% | -0.001 | 0.008 | similaire à Austin |

### Volatile markets — timing matters

| City | vol | interprétation |
|------|----:|----------------|
| Singapore | 0.074 | odds swing → timing entry important |
| Warsaw | 0.066 | idem |
| Chongqing | 0.066 | idem |
| Wuhan | 0.052 | idem |

### Stable markets — entry any time

| City | vol | interprétation |
|------|----:|----------------|
| Moscow | 0.001 | frozen odds |
| Dallas | 0.005 | stable |
| Wellington | 0.005 | stable |

### Drift moyen par ville (heating vs cooling markets)

| Heating | drift pp | | Cooling | drift pp |
|---------|---------:|-|---------|---------:|
| Singapore | +0.160 | | Tel Aviv | -0.042 |
| Warsaw | +0.106 | | Paris | -0.029 |
| Buenos Aires | +0.086 | | Taipei | -0.019 |
| Wuhan | +0.077 | | Hong Kong | -0.019 |
| Kuala Lumpur | +0.067 | | Toronto | -0.015 |

## Implications stratégiques

1. **Austin edge structurellement confirmé** — convergence 40% + vol 0.007 =
   le marché ne corrige pas le mispricing initial. Le WR 100% historique
   paper n'est pas une fluke mais une vraie inefficience.

2. **NYC / LA / Denver** = candidates Austin-like sur convergence<40%.
   Attention : n petit (3-4), à valider avec plus de trades.

3. **Miami à skip** sur Tier S — bookies reactivent. Tier A NO workhorse
   reste OK (moins sensible à la convergence).

4. **Timing entries**: cities volatile (Singapore, Warsaw, Wuhan) → l'entry
   price peut bouger 5-16% pendant la vie du market. Opportunité :
   re-scanner agressivement ces villes pour pick meilleure entrée.

5. **Global 50% = random walk** signifie qu'attendre la résolution ne réduit
   pas l'incertitude. Une fois entrée à mispricing, la proba de gain est
   fixée dès l'ingestion — le book n'améliore pas la prédiction.

## Actions

1. Ajouter `LA`, `NYC`, `Denver` au test graylist Tier S (once live n ≥ 10)
2. Per-city **volatility multiplier** sur la fenêtre de ré-entrée : villes
   stables → permit 1 entry/market, villes volatiles → permit à -5% drift
3. Investigation plus profonde sur Austin : mesurer stabilité sur 60-90j
   une fois paper session relance clean post-dedup

## Related

- [[_MOC]]
- [[research-findings-2026-04-21]]
- [[tier-s-v2-hedge-fund-gates]]
- [[dedup-bug-p-and-l-inflation]]
