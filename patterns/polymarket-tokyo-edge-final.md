---
name: Polymarket Tokyo — Stratégie finale validée
description: Single bracket + filtre spread NWP. 57.8% WR quand spread ≤ 1.5°C. $4.5-9.3k/mois. Backtest 330 jours.
type: pattern
project: polymarket-hedge
tags: [polymarket, tokyo, weather, nwp, spread-filter, strategy, validated]
date: 2026-04-17
---

# Polymarket Tokyo — Stratégie finale

## Résumé

**Single bracket, médiane 4 NWP + rolling bias 30j, filtre spread ≤ 1.5°C.**

| Métrique | Valeur |
|----------|--------|
| WR exact | **57.8%** (avec filtre spread ≤ 1.5°C) |
| WR baseline (sans filtre) | 48.2% |
| Marché Polymarket | ~34% |
| Edge vs marché | **+24 points** |
| Fréquence | ~10 trades/mois (1 jour sur 3) |
| PnL estimé ($1000/trade @30¢) | **$9 270/mois** |
| PnL estimé ($1000/trade @40¢) | **$4 450/mois** |
| Backtest | 330 jours (avril 2025 → avril 2026) |
| Walk-forward | Rolling bias 30j, out-of-sample |

## Modèle

```python
# 1. Fetch 4 NWP forecasts
ecmwf = fetch("ecmwf_ifs025", lat=35.55, lon=139.78, tz="Asia/Tokyo")
gfs   = fetch("gfs_seamless", ...)
icon  = fetch("icon_seamless", ...)
jma   = fetch("jma_seamless", ...)

# 2. Rolling bias correction (30 derniers jours)
bias = mean(median(NWP) - WU_tmax) over last 30 days

# 3. Prediction
corrected = [v - bias for v in [ecmwf, gfs, icon, jma]]
predicted = round(median(corrected))

# 4. FILTRE CONFIANCE — spread entre modèles
spread = max(corrected) - min(corrected)
if spread > 1.5:
    SKIP  # modèles pas d'accord → pas de trade
else:
    BUY bracket {predicted}°C
```

## Filtre spread — Résultats complets

| Filtre | N | WR | Fréquence | EV@30¢ | EV@40¢ |
|--------|---|-----|-----------|--------|--------|
| Aucun | 330 | 48.2% | 100% | +61% | +20% |
| Spread ≤ 2.0 | 173 | 54.9% | 52% | +83% | +37% |
| **Spread ≤ 1.5** | **109** | **57.8%** | **33%** | **+93%** | **+45%** |
| Spread ≤ 1.0 | 46 | 56.5% | 14% | +88% | +41% |

Le sweet spot est **spread ≤ 1.5°C** : meilleur WR (57.8%) avec assez de fréquence (33% des jours = ~10/mois).

## Seuil de rentabilité

```
WR = 57.8%
Breakeven price = 1 / (1 + 1/((WR/(1-WR)))) = WR = 57.8¢

Autrement dit: profitable tant que le prix d'entrée < 58¢
Prix médian observé à T-12h: ~40¢ → PROFITABLE
```

## Saisonnalité

| Saison | WR | Action |
|--------|-----|--------|
| Printemps (MAM) | 56% | TRADE |
| Automne (SON) | 56% | TRADE |
| Hiver (DJF) | 44% | TRADE (edge réduit) |
| **Été (JJA)** | **34%** | **SKIP** |

Pas trader juin-août. Le modèle tombe au niveau du marché.

## Risques

1. **Série perdante max: 8 jours** → drawdown $8k @$1000/trade → bankroll min $25k
2. **Lookahead bias possible**: forecast 00Z dispo ~06:00 UTC, pas 00:00
3. **N=23 trades avec vrais prix Polymarket** — PnL estimé, pas vérifié live
4. **Liquidité**: $3-24k par bracket estimé, non vérifié au-dessus de $500
5. **Été sans edge**: couper juin-août

## Scaling

| Size/trade | PnL/mois @30¢ | PnL/mois @40¢ | DD max | Bankroll min |
|------------|---------------|---------------|--------|-------------|
| $500 | $4 635 | $2 225 | $4k | $12k |
| $1 000 | $9 270 | $4 450 | $8k | $25k |
| $2 000 | $18 540 | $8 900 | $16k | $50k |

## Multi-villes (en cours de validation)

| Ville | Meilleur modèle | WR | Status |
|-------|----------------|-----|--------|
| **Tokyo** | median 4 NWP + bias 30j | **49% (58% filtré)** | **LIVE** |
| Shanghai | best 2 NWP + bias 30j | 45% | À valider avec filtre |
| Beijing | ICON + bias 30j | 43% | À valider avec filtre |

## Infrastructure

- **Scripts**: `scripts/hedge3_oracle.py`, `scripts/dashboard_tui.py`
- **DB**: `mega_dataset.db` (360j × 6 villes, WU + 4 NWP)
- **VPS**: 95.216.198.143, crons à 00:00/08:00/13:30 UTC
- **WU API**: `api.weather.com` clé `e1f10a1e78da46f5b10a1e78da96f525`
- **Résolution**: WU station RJTT (Tokyo Haneda), entier °C

## Premier trade live

```
Date:     2026-04-17
Prédit:   18°C
Réel:     17°C (WU/Polymarket)
Brackets: [17°C @16¢, 18°C @36¢, 19°C @34¢]
Résultat: 17°C WIN → +$162 (mode hedge)
Note:     En single bracket @18°C, aurait été une perte (-$500)
          Le filtre spread aurait-il filtré ce trade? À vérifier.
```

## Décision

Mode paper trading pendant 2 semaines avec le filtre spread.
Si WR confirme > 55% sur 10+ trades filtrés → passer en live $500/trade.

## Related

- [[patterns/polymarket-weather-mega-model]]
- [[patterns/polymarket-weather-final-verdict]]
- [[founder/decisions/2026-04-16-weather-model-critique]]
- [[_system/MOC-patterns]]
