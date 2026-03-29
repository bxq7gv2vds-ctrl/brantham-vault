---
title: Polymarket — Passer du fondamental à l'intraday
date: 2026-03-29
type: decision
status: decided
tags: [polymarket, trading, strategy]
---

# Décision : Intraday > Hold-to-Resolution

## Contexte
On a construit un modèle EMOS (NWP calibré) qui trouve des edges comme London 11°C +46%. Mais ça implique d'attendre la résolution du marché (quelques jours).

## Options considérées

**Option A : Hold to resolution**
- Pro : modèle EMOS très précis, edge fondamental réel
- Con : capital bloqué, risque binaire, pas scalable, lent

**Option B : Intraday — trade les mouvements**
- Pro : capital se recycle rapidement, pas de risque résolution, scalable
- Con : nécessite plus de modélisation, besoin de tick data

## Décision
**Option B : architecture intraday complète.**

Le modèle EMOS reste utile comme "fundamental anchor" (μ dans le Jump-Diffusion), mais la stratégie principale est d'exploiter les inefficiences INTRADAY :
1. NWP Lead-Lag (faisable maintenant)
2. Bracket sum arbitrage (faisable maintenant)
3. Order flow mean-reversion (après 2-4 semaines de data)

**Why:** "Il y a des mecs qui font des millions avec la météo" — les millions viennent de la fréquence des trades et du recyclage du capital, pas de l'attente passive.

## Actions
1. ✅ Architecture planifiée (modules identifiés)
2. ⏳ Démarrer collecte tick data immédiatement (WebSocket → SQLite)
3. ⏳ Implémenter NWP Lead-Lag signal (buildable maintenant)
4. ⏳ Implémenter Bracket Vol Surface (buildable maintenant)
5. ⏳ Après 2-4 semaines : calibrer modèle microstructure

## Related
- [[founder/sessions/2026-03-29-polymarket-hedge-engine]]
- [[patterns/polymarket-intraday-architecture]]
- [[_system/MOC-decisions]]
