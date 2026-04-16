---
name: Polymarket Weather — Verdict final après mega-analyse
description: Résultat de 2 jours d'analyse intensive. Tokyo seul edge viable. Médiane 4 NWP = 51.7% exact. $3-6k/mois réaliste.
type: pattern
project: polymarket-hedge
tags: [polymarket, weather, verdict, tokyo, nwp, backtest]
date: 2026-04-16
---

# Polymarket Weather — Verdict final

## Session 2026-04-14 → 2026-04-16 (marathon)

### Angles testés et résultats

| Angle | Résultat | Exploitable |
|-------|----------|-------------|
| CONVEX_YES (longshot bias) | WR=0.71% vs prix 1.0% → -EV | NON |
| Sum-of-brackets arb | Illiquide, spread mange l'edge | NON |
| Oracle timing Asie (METAR) | T_max pas final à 06:00 UTC, marché ajuste déjà | NON |
| WU API oracle (confirmé) | 100% match Poly mais bracket gagnant déjà à 71¢ à 06:00 | MARGINAL |
| ECMWF + bias correction | 27% OOS (vs 39% in-sample = overfitting) | NON |
| XGBoost multi-NWP | 33% = pire que GFS seul | NON |
| NO strategy (vendre perdants) | +EV mais centimes par trade | NON |
| Odds mispricing (toutes cotes) | Marché efficient, pas de longshot bias | NON |
| **Médiane 4 NWP — Tokyo** | **51.7% exact, 89.4% ±1 sur 180j OOS** | **OUI** |
| Médiane 4 NWP — Wuhan | 40% exact, 83% ±1 sur 90j | PEUT-ÊTRE |
| Médiane 4 NWP — 4 autres villes | 17-33% = sous le marché | NON |

### Tokyo — Le seul signal vérifié

**Dataset** : 360 jours (avril 2025 → avril 2026), 4 modèles NWP (ECMWF, GFS, ICON, JMA)

**Méthode** : `int(round(median(ECMWF, GFS, ICON, JMA)))` — aucun ML, aucun biais, aucun paramètre

**Résultats walk-forward (10 mois testés)** :
- Accuracy exacte : **48.4% moyenne** (min 32% été, max 64% mars)
- ±1°C : **89.1% moyenne**
- Stable sur 10 mois consécutifs

**PnL backtesté (23 trades avec vrais prix marché)** :
- Single bracket $100 : WR 69.6%, EV +$105/trade, Sharpe 10.07, PF 4.46
- Hedge 3 brackets $150 : WR 100% (22/22), EV +$187/trade, Calmar 53.5x

**Saisonnalité** :
- Printemps/Automne : ~56% exact → meilleur edge
- Hiver : ~44% → correct
- Été : ~34% → pas d'edge, ne pas trader

### Caveats

1. **Lookahead bias possible** : Open-Meteo historical-forecast donne probablement le run 00Z (dispo 06:00 UTC). Trading à 00:00 UTC utiliserait le run 12Z veille (légèrement moins bon).
2. **N=23 trades avec prix réels** : petit échantillon pour le PnL. L'accuracy (N=360) est plus fiable.
3. **Liquidité inconnue** : price_bars n'ont pas de volume. Exécution réelle à vérifier en paper trading.
4. **Tokyo est une exception** : les 4 autres villes chinoises ne marchent pas. Le NWP est mieux calibré pour Haneda (station côtière, bien instrumentée).

### PnL projeté réaliste

| Scénario | Taille | /trade | /mois | /an |
|----------|--------|--------|-------|-----|
| Single bracket Tokyo | $100 | +$105 | ~$3 150 | ~$37 800 |
| Hedge 3 brackets Tokyo | $150 | +$187 | ~$5 600 | ~$67 200 |
| Hedge Tokyo hors été (10 mois) | $150 | +$187 | ~$5 600 | ~$56 000 |

### Scripts

- `mega_dataset.db` — 360+ jours × 6 villes, WU T_max + 4 NWP
- `scripts/build_mega_dataset.py` — construction dataset
- `scripts/train_model.py` — XGBoost (ne bat pas médiane simple)
- `scripts/hedge3_oracle.py` — déployé VPS
- `scripts/wu_api_oracle.py` — WU API temps réel

### Bugs critiques trouvés pendant la session

1. Settlement avec mauvais jour METAR (tmax_day - 24h)
2. METAR hours=48 trop court → faux wins
3. Mauvaises stations ICAO (Shanghai ZSSS→ZSPD, Taipei RCTP→RCSS)
4. Tout le backtest original sur Open-Meteo au lieu de WU = résultats faux
5. Biais correction overfitté (39% in-sample → 27% OOS)

## Related

- [[patterns/polymarket-weather-mega-model]]
- [[founder/decisions/2026-04-16-weather-model-critique]]
- [[patterns/polymarket-convex-yes-complete-breakdown]]
- [[_system/MOC-patterns]]
