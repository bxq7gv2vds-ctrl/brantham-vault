---
name: Economic Thesis — Polymarket Weather Alpha
description: Thèse économique formelle expliquant POURQUOI un edge existe sur les marchés weather Polymarket, POURQUOI il persiste, et QUAND il devrait expirer. DRAFT pour validation user.
type: thesis
status: DRAFT_NEEDS_USER_REVIEW
created: 2026-04-20
updated: 2026-04-20
priority: critical
tags: [polymarket, thesis, economic-intuition, hypothesis, governance]
---

# Economic Thesis — Polymarket Weather Alpha

**Status** : DRAFT. Pour valider G1, ce document doit être relu par Paul et recevoir le sentinel `THESIS VALIDATED` quelque part dans le doc. Sans validation, `gate_scorecard.py` bloque G1.

## 1. Thesis statement (1 phrase)

> Les brackets weather Polymarket sont systématiquement mispriced parce que (a) la majorité des participants sont retail sans accès aux ensembles NWP agrégés, (b) les oracles ouvrent pendant 1-14 jours avec repricing lent, et (c) les extrêmes de distribution (tail brackets) sont overpriced par aversion au regret, ce qui crée un edge capturable en side NO sur tails improbables.

## 2. Source d'edge — 5 mécanismes hypothesized

### M1 — Asymétrie d'information NWP (structural)
**Hypothèse** : La majorité des participants utilise 1 source météo publique (weather.com, AccuWeather) qui dérive d'un seul modèle (souvent GFS). On consomme 12 sources + ensemble BMA pondéré par station × régime.
**Signature attendue** : edge concentré sur les markets avec haute `ensemble_disagreement` (régime chaotique où mono-source sous-performe).
**Test** : edge by `nwp_disagreement_pct_bucket`. Si edge croit avec disagreement = confirmé.
**Expiration** : quand Polymarket ajoute un NWP agrégé natif, ou si un concurrent institutionnel arrive.

### M2 — Recency bias (behavioral)
**Hypothèse** : Les traders sur-pondèrent les derniers jours observés. Après une canicule 3 jours, ils achètent YES "chaud" à prix trop haut. On exploite via anomaly normalization (feature `anomaly_z` vs climato 30 ans).
**Signature attendue** : edge après événements météo extrêmes récents, surtout sur markets TTR 3-7 jours.
**Test** : edge by `days_since_extreme_anomaly_z_gt_2`.
**Expiration** : longue (biais cognitif stable) — probablement jamais.

### M3 — Tail aversion (behavioral)
**Hypothèse** : Les traders overprice les tails improbables par aversion au regret ("et si ça arrive je perds"). Un bracket "Above 40°C Paris" se trade à $0.12 quand climato implique $0.03. NO side edge systématique.
**Signature attendue** : edge concentré side NO sur brackets climato < 10% probability.
**Test** : WR side NO tail vs WR side NO body. Si tail WR > body WR = confirmé.
**Expiration** : long — biais cognitif structural.

### M4 — Oracle repricing lag (microstructure)
**Hypothèse** : Quand une obs confirme une bracket (e.g. MIDI atteint déjà 32°C → YES "Above 30°C" quasi-gagnant), le marché met 10-30 minutes à reprice à ~0.99. Window de capture YES à $0.85-0.95.
**Signature attendue** : signaux CONFIRMED_YES avec edge > 4% sur markets liquides.
**Test** : `signal_log` alpha_type=CONFIRMED_YES WR > 95% sur N >= 50.
**Expiration** : rapide si algo compétiteur arrive (3-12 mois).

### M5 — Weekend / low-liquidity arbitrage (microstructure)
**Hypothèse** : Le volume Polymarket chute 40-60% le weekend. Spreads élargis, market makers moins actifs. Entry prices plus favorables.
**Signature attendue** : edge weekend > edge weekday.
**Test** : edge by `is_weekend`.
**Expiration** : medium (3-6 mois, dépend d'institutional adoption).

## 3. Pourquoi ça persiste (defensibility)

Le edge weather sur Polymarket n'est **pas** du HFT latency arbitrage où tout disparaît en 6 mois. Raisons :

- **Capacity limitée** : la capacity totale visée est $50k-$200k max. Pas assez pour attirer un gros hedge fund (seuil minimum ~$5M AUM). On est sous le radar.
- **Barrière d'entrée modérée mais non triviale** : 12 sources NWP, 46 stations METAR, feature engineering domaine-spécifique. Pas trivial à répliquer.
- **Juridiction** : Polymarket bloqué US. Les gros HFT US n'y sont pas. Compétiteurs sérieux = rare (quelques crypto-native trading firms).
- **Weather markets niche** : Polymarket a 90% politique/sports. Weather = 2-5% du volume. Personne ne dédie une équipe à ça.

**Durée prévue d'edge** : 12-36 mois, avec dégradation progressive. Plan de sunset via [[strategy-lifecycle]].

## 4. Expiration triggers (quand tuer la strat)

Signaux que l'edge est mort :

- DSR rolling 90j passe sous 0.5
- WR global passe sous 65% sur N >= 100
- Capacity measurée chute > 50%
- Market maker identifié sur Polymarket weather (on voit orders tight spread volume élevé systématique)
- Polymarket intègre un oracle NWP natif / pricing tool
- Changement régulation qui banque Polymarket FR/EU

## 5. Non-edges (ce qu'on ne revendique pas)

Important : dire ce qu'on **n'est pas**, pour éviter data mining bias :

- **Pas** un edge sur forecast absolu (on n'est pas meilleur que ECMWF en pure CRPS)
- **Pas** un edge sur extreme weather forecasting (hurricanes, typhoons — sources satellite manquantes)
- **Pas** un edge sur markets ultra-liquides (BTC brackets Polymarket, NBA) — ceux-là sont sharped by pros
- **Pas** un edge sur longue horizon (> 14 jours — NWP skill s'effondre)

## 6. Capital-adjusted thesis

L'edge attendu par tier de bankroll :

| Bankroll | Edge net attendu | Notes |
|---|---|---|
| $500 | ~15-20% / mois | capacity non limitante, TC friction élevée en % |
| $2,000 | ~8-12% / mois | sweet spot paper-validated |
| $10,000 | ~3-6% / mois | capacity commence à jouer |
| $50,000 | ~1-3% / mois | capacity proche limite, impact non-trivial |
| $200,000 | ~0% | strat dead au-delà |

## 7. Assumptions critiques (à invalider en priorité)

Si l'une de ces assumptions tombe, toute la thèse s'effondre :

- **A1** : La majorité des participants weather Polymarket est retail sans ensemble NWP. **À vérifier** par analyse orderbook patterns (si on voit market makers tight = faux).
- **A2** : Les oracles Polymarket résolvent correctement et timely. **Historique 2026-01 à 2026-04** : pas de malfunction majeur observé. Risque résiduel mais géré.
- **A3** : Polymarket reste accessible juridiquement FR. **Risque** : AMF peut réclassifier. Hors de notre contrôle.
- **A4** : Le volume weather markets reste >= $500/market/day en moyenne. **À monitorer** — si chute, capacity disparaît.

## 8. Meta — cette thèse elle-même

La thèse peut être fausse même si le backtest est bon. Les 5 mécanismes sont des **hypothèses causales** que nos tests doivent chacun confirmer **individuellement**. Si seulement M3 (tail aversion) est confirmé, on doit restreindre la strat aux tails bets et abandonner les autres alphas.

Le research log [[research/hypotheses-jsonl|hypotheses.jsonl]] track les tests et résultats (PASS/FAIL per mécanisme).

---

## USER VALIDATION SECTION

**Paul**, relire et si la thèse capture ta conviction, ajouter cette ligne n'importe où dans le doc :

```
THESIS VALIDATED BY PAUL ON YYYY-MM-DD — [brief note on adjustments if any]
```

Sans ce sentinel, `gate_scorecard.py --gate G1` return FAIL.

**Questions ouvertes pour toi** :
1. Es-tu d'accord avec les 5 mécanismes ou tu en ajoutes / retires ?
2. L'expiration 12-36 mois est-elle réaliste pour ton horizon ?
3. Le tier bankroll $500 → $200k, tu vois des ajustements ?
4. Les 4 assumptions critiques — lesquelles doivent être testées en priorité ?

## Related

- [[g1-g2-qualification-kit|Framework master]]
- [[g1-g2-todo-tracker|Todo tracker]]
- [[strategy-lifecycle|Strategy lifecycle — sunset criteria]]
- [[failure-modes|Failure modes]]
- [[STATE-HANDOFF]]
- [[_MOC|Polymarket Hub]]
- [[../../_system/MOC-decisions|MOC Decisions]]
