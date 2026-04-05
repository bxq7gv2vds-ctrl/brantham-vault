---
title: Reverse engineering @speeda/@coldmath — Polymarket Bracket Scalper
date: 2026-04-05
type: session
project: polymarket-hedge
tags: [polymarket, bracket-scalper, reverse-engineering, coldmath, speeda]
---

# Session — Reverse Engineering @speeda/@coldmath

## Résultats du reverse engineering complet

### @coldmath — Fussy-Expedition
- **Wallet**: `0x594edb9112f526fa6a80b8f858a6379c8a2c1c11`
- **Profil**: 5391 trades, volume $7.1M, PnL **$102.5K**, depuis nov 2025
- **Plus gros win**: $12.4K

**Stratégie réelle**:
1. Pour chaque city-date pair (D+1 à D+4, TTR 20-100h)
2. Récupère NWP forecast T_max → mu ± sigma
3. Pour TOUS les bins où P(YES) < 5% (bins impossibles loin du forecast):
   - Achète NO token (outcomeIndex=1) au prix 0.96-0.99
   - Ex: Austin Apr 9, forecast 74°F → bins 62-63°F, 64-65°F, 66-67°F, 68-69°F tous impossibles
4. Pour les ceiling bins "X°F or higher" où X est bien EN-DESSOUS du forecast:
   - Achète YES token au prix 0.86-0.98
   - Ex: Dallas "70°F or higher Apr 9" YES à 0.9654 (forecast ~80°F)

**Données brutes observées**:
```
Austin Apr 9: 74°F+ YES @ 0.8898 ($105)
Austin Apr 9: 68-69°F NO @ 0.9892 ($595)
Austin Apr 9: 66-67°F NO @ 0.9817 ($351)
Austin Apr 9: 64-65°F NO @ 0.99 ($129)
Austin Apr 6: 64-65°F NO @ 0.99 ($2562) ← GROSSE position
Dallas Apr 9: 70°F+ YES @ 0.9654 ($184)
Dallas Apr 9: 66-67°F NO @ 0.9893 ($627)
Houston Apr 8: 70-71°F NO @ 0.9611 ($87)
```

**Mécanique P&L**:
- Par trade: $500 × (NO_entry → 1.0) = $500 × 0.002-0.04 = $1-20
- Volume: $7.1M, 5400 trades → avg $1300/trade
- P&L annualisé ≈ $240K/an depuis nov 2025

---

### @speeda — Dimpled-Scrap
- **Wallet**: `0x46745788e678a6f8ceebcd8bc7e37462b74703ca`
- **Profil**: 337 trades, volume $847K, PnL **$18.8K**, depuis 22 mars 2026
- **Plus gros win**: $2792

**Stratégie réelle — DEUX PHASES**:

#### Phase 1 (12:00-14:00 UTC pour villes asiatiques, TTR 2-4h)
- T_max est déjà confirmé par METAR (température de pointe passée à ~07h UTC HK)
- Mais le marché tarde à réévaluer (YES price encore à 0.13 sur un bin confirmé)
- @speeda achète YES à 0.13 sur HK 25°C alors que T_max = 25°C déjà observé
- Profit: 0.13 → 0.80 en quelques heures = **5-6x**

#### Phase 2 (16:00-17:00 UTC, TTR <1h)
- T_max totalement confirmé (fin de journée locale)
- Achète NO sur les bins que T_max a dépassés au prix 0.987-0.999
- Grosse position: HK 24°C NO à 0.9976 pour $3689 → vend à 0.999 = $8.78 profit
- Aussi achète YES sur le bin confirmé à 0.965-0.98

**Donnée clé observée**:
```
12:19 UTC | BUY | HK 25°C YES @ 0.13   ($12) ← Phase 1, T_max déjà 25°C
12:19 UTC | BUY | HK 24°C NO  @ 0.20   ($24) ← Phase 1, marché en retard
15:22 UTC | SELL| HK 25°C YES @ 0.72   ($45) ← sortie Phase 1
16:17 UTC | BUY | HK 24°C NO  @ 0.9865 ($327)← Phase 2
16:17 UTC | BUY | HK 24°C NO  @ 0.9976 ($3689)← Phase 2 GROSSE
17:01 UTC | SELL| HK 24°C NO  @ 0.999  ($3693)← exit Phase 2
```

---

## Bugs corrigés dans run_bracket_scalper.py

### Bug #1 — Market discovery (CRITIQUE)
- **Avant**: `public-search?q=temperature` → 50 events max → 27 marchés (3 villes)
- **Après**: Requête par ville (39 villes) → 1301 events → **1475 marchés**
- Fix: boucle async `fetch_city(city)` pour chaque ville de `CITY_STATIONS`

### Bug #2 — Heure de pic ignorée (SPEEDA Phase 1 bloquée)
- **Avant**: `max_possible = T_obs + hrs_left * rate` même à 22h local
- **Après**: si `local_hour >= 16`, alors `max_possible = T_obs` (T_max est final)
- Impact: SPEEDA_EARLY peut maintenant détecter les bins certifiés avec YES cheap

### Bug #3 — speeda_min_price trop élevé
- **Avant**: `speeda_min_price = 0.70` → manque le market-lag alpha (0.13-0.50)
- **Après**: signal SPEEDA_EARLY pour yes_price < 0.50, SPEEDA_YES pour 0.50-0.99

### Bug #4 — Edge négatif inclus
- **Avant**: COLDMATH_NO généré même quand notre modèle surestimait P(YES)
- **Après**: filtre `if edge <= 0: continue` → 554 signaux propres vs 632

---

## Résultats paper trading (premier scan complet)

```
1475 marchés découverts (36 villes × 4 jours × 11 bins)
 140 NWP fetches réussis (140/140)
 749 signaux totaux:
   COLDMATH_NO : 554 (avg NO_price=0.978, avg edge=0.019)
   COLDMATH_YES:   4 (avg YES_price=0.966, avg edge=0.031)
   PROB_NO     : 122 (avg=0.691)
   PROB_YES    :  69 (avg=0.140)
```

Signaux COLDMATH_YES trouvés (correspond aux trades @coldmath réels):
- Dallas Apr 9 "70°F or higher" YES @ 0.976 — @coldmath a acheté @ 0.9654 ✓
- Denver Apr 8 "56°F or higher" YES @ 0.966
- Chicago Apr 8 "50°F or higher" YES @ 0.962
- Chicago Apr 9 "52°F or higher" YES @ 0.960

---

## Points manquants vs @coldmath réel

1. **Taille de position**: @coldmath met $500-2500/trade. Notre paper trade = $25.
2. **Position sizing dynamique**: plus de capital sur les signaux NO price > 0.995
3. **Exit logic**: @coldmath SELL avant résolution à 0.999 pour recycler capital
4. **Cities non couvertes**: Busan, Ankara, Kuala Lumpur, Melbourne (pas dans notre CITY_STATIONS)
5. **Profondeur orderbook**: @coldmath sait si les ordres vont passer. Nous assumons fill.

## Related

- [[_system/MOC-patterns]]
- [[brantham/_MOC]]
- [[patterns/polymarket-bracket-arb]]
- [[patterns/polymarket-nwp-emos-calibration]]
- [[founder/decisions/2026-03-29-polymarket-intraday-vs-fundamental]]
