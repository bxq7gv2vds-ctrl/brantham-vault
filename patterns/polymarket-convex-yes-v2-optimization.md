---
name: CONVEX_YES v2a Optimization
type: pattern
date: 2026-04-13
project: polymarket-hedge
tags: [polymarket, trading, convex, optimization, statistics]
---

# CONVEX_YES v2a — Optimisation Statistique TTR

**Date**: 2026-04-13  
**Source**: `real_backtest.py` — 2699 trades réels 2026-03-05→2026-04-05  
**Impacte**: [[patterns/polymarket-convex-yes-complete-breakdown]]

## Contexte

Après le premier vrai jour de settlement CONVEX_YES (2026-04-13), analyse complète
des 3 leviers d'optimisation tirés du backtest certifié.

**Résultat settlement 13 avril** :
- 62 trades settlés, WR=6.5% (vs 7.04% backtest) ✓ dans l'intervalle de confiance
- Net -$2,342 à cause des positions pré-cap ($209–$233 vs $15 cap)
- 4 winners : Beijing +$1,348, Tel Aviv +$922, Moscow +$506, Lucknow +$14
- Positions $15-cap : +$1,911 profit → stratégie v2 valide

## Trois Leviers d'Optimisation

### Levier 1 — Villes (WRs certifiés par real_backtest.py)

| Tier | Villes | WR | Sharpe/100 | N | p |
|------|--------|-----|-----------|---|---|
| S | Hong Kong, Tokyo | 11.7–12.4% | 3.4–3.6 | 129–145 | 0.000 |
| A | Paris, Wellington, Madrid, Mexico City, Taipei, Shanghai, London | 7.6–9.0% | 2.5–2.9 | 23–171 | 0.000–0.032 |
| B | Tel Aviv, Beijing, Milan, Buenos Aires, Munich, Warsaw, Chengdu, São Paulo | 5.7–7.3% | 2.0–2.4 | 85–147 | 0.000–0.001 |

**Exclus** (p>0.05 ou WR<5% ou Sharpe<1.5) :
Toronto 4.6%, Wuhan 3.3%, Seoul 3.4%, Atlanta 2.6% (p=0.058), Austin 4.1% (p=0.122),
villes US (near-zero), Singapore (EMOS bias), Lucknow (0.5%), Moscow (variance extrême)

### Levier 2 — TTR (Time To Resolution)

| Fenêtre TTR | WR | Ratio vs v1 |
|-------------|-----|------------|
| 6–10h | 10.5% | +49% |
| 10–14h | 8.2% | +16% |
| **6–14h (v2a)** | **8.45%** | **+20%** |
| 14–18h | 6.6% | −6% |
| 18–24h | 3.1% | −56% |
| 24–48h | 3.0% | −57% |

**Insight** : passé 14h TTR, le marché a le temps de se recalibrer → edge disparaît.
À 6–10h, le prix est encore stale = alpha maximal.

### Levier 3 — Prix (buckets analysés)

| Bucket prix | WR | Sharpe/100 | EV/trade ($15 mise) |
|-------------|-----|-----------|---------------------|
| 0.2–0.4% | 5.3% | 2.23 | $251 |
| 0.4–0.8% | 5.6% | 2.19 (pire) | ~$190 |
| **0.8–1.2%** | **11.5%** | **3.29 (meilleur)** | **$159** |
| 1.2–2.5% | ~7% | ~2.5 | ~$90 |

## Comparaison Scénarios

| Paramètre | v1 baseline | v2a TTR-only | v2b TTR+prix | Décision |
|-----------|-------------|--------------|--------------|----------|
| Filtres | TTR 6–48h, prix 0.2–2.5% | **TTR 6–14h**, prix 0.2–2.5% | TTR 6–14h, prix 0.8–2.5% | |
| N/jour | 87 | 60 | 20 | |
| Win Rate | 7.04% | 8.45% | 8.91% | |
| Sharpe/100 | 2.40 | 2.70 | 3.29 | |
| EV/trade | $104 | **$127** | $88 | |
| P(jour rentable) | 99.8% | **99.5%** | 84.5% | |
| **CHOIX** | ❌ | **✅ v2a** | ❌ | v2a retenu |

**Pourquoi pas v2b ?** Le bucket 0.2–0.8% a un Sharpe plus bas MAIS un EV/trade
plus élevé ($251 vs $159) car le levier est énorme (buy à 0.3%, WR=5.3% = 17x upside).
Couper ce bucket réduit le volume de 3× et le P(jours rentables) à 84.5% sans gain réel.

## Code Implémenté (v2a)

```python
# run_bracket_scalper.py — CONVEX_YES filter
if (cfg.convex_yes_enabled
        and city_wr is not None
        and 0.002 <= yes_price <= 0.025   # plein range 0.2-2.5%
        and 6.0 <= ttr_hours <= 14.0      # v2a : TTR court uniquement
        and city not in CONVEX_EXCLUDED):
```

```python
# Kelly sizing (inchangé)
kelly_f = 0.25 * max(0.0, city_wr - yes_price) / max(0.01, 1.0 - yes_price)
convex_size = min(kelly_f * cfg.bankroll, cfg.max_convex_size)  # cap $15
```

## Métriques Live (à suivre)

- **WR live attendu** : 8.0–9.0% (v2a), calibrer quand N>200
- **Track record** : `logs/track_record.csv` (snapshot quotidien auto)
- **Prochaine vérification** : 2026-04-15 après 2 jours de settlement v2a

## Leçons Clés

1. **TTR < 14h** est le seul filtre qui améliore sans dégrader le volume
2. **Prix bas (0.2–0.8%)** = levier géant → ne pas couper même si Sharpe individuel <3
3. **Positions pre-cap** (pré 2026-04-12) causaient de grosses pertes — $15 Kelly cap résout ça
4. **WR live = backtest** à ±1% → modèle non-overfitté sur les 62 trades du 13/04

## v3 — Deep Analysis (2026-04-13, deep_city_analysis.py)

Analyse sur dataset complet 2025-01→2026-04 (17500 obs, 37 villes). Résultats v3 :

| Tier | Villes | WR range | S/100 range |
|------|--------|----------|-------------|
| S | HK, Tokyo, Beijing, Chengdu, Madrid, Mexico City, Milan, **Moscow**, Taipei, Paris | 9.8–17.7% | 3.0–4.5 |
| A | Warsaw, Tel Aviv, Munich, Buenos Aires, London, Wellington, **Wuhan**, Shanghai, São Paulo, **Seoul** | 5.7–9.3% | 2.0–2.9 |
| B | **Istanbul** (NEW), Toronto, Seattle | 4.1–4.8% | 1.6–1.9 |
| ✗ | Atlanta, Chicago, Dallas, Denver, Miami, etc. | 0–2.8% | <1.2 |

**Corrections majeures** :
- Moscow : exclus (S=1.26) → **Tier S** (WR=11.1%, S=3.25) — erreur dataset précédent
- Wuhan : exclus (WR=3.3%) → **Tier A** (WR=6.8%, S=2.35)
- Seoul : exclus (WR=3.4%) → **Tier A** (WR=5.7%, S=2.02)
- Istanbul : **NEW** Tier B (WR=4.8%, S=1.88, N=62)
- WR global : 7.04% → **8.52%** (+1.5 pp)

**Prix buckets** (Sharpe très stable 2.23–2.58 sur toute la plage) :
→ Garder 0.2–2.5% complet confirmé, EV/trade $+54–$+300 selon le bucket

## Related

- [[_system/MOC-patterns]]
- [[patterns/polymarket-bracket-arb]]
- [[patterns/polymarket-convex-yes-complete-breakdown]]
- [[patterns/polymarket-oracle-confirmed-backtest]]
- [[patterns/polymarket-coldmath-no-ev-analysis]]
- [[patterns/polymarket-price-process-deep-analysis]]
