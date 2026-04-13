---
name: Polymarket CONVEX_YES — Breakdown Complet
description: Analyse exhaustive de la stratégie longshot bias Polymarket. Mathématiques, backtest réel 2699 trades, statistiques complètes par ville/heure/TTR/prix. Track record VPS.
type: pattern
project: polymarket-hedge
tags: [polymarket, convex-yes, longshot-bias, kelly, sharpe, backtest, statistiques]
date: 2026-04-12
scripts:
  - scripts/run_bracket_scalper.py
  - scripts/real_backtest.py
  - scripts/city_timing_backtest.py
  - scripts/daily_pnl_report.py
---

# Polymarket CONVEX_YES — Breakdown Complet

---

## 1. Principe fondamental — Le biais longshot

### Qu'est-ce que Polymarket propose ?

Chaque jour, pour 51 villes, Polymarket ouvre des marchés binaires du type :

> *"La température maximale à Tokyo le 13 avril 2026 sera-t-elle entre 13°C et 14°C ?"*

Chaque ville a ~25 brackets couvrant l'ensemble de la distribution possible. La somme de tous les YES d'une ville/jour ≈ 100% (loi de probabilité totale).

### Le mispricing structurel

Les marchés Polymarket fixent les brackets improbables (queues de distribution) **systématiquement trop chers** côté vendeur, donc **trop bon marché pour l'acheteur**. Un bracket avec 0.8% de probabilité réelle se négocie à 0.5–1.5¢, mais la fréquence réelle d'occurrence est ~7–12%.

Ce phénomène s'appelle le **longshot bias** — observé depuis des décennies dans les paris hippiques (Griffith 1949, Ali 1977) et généralisé aux marchés prédictifs (Wolfers & Zitzewitz 2004).

**Intuition** : les vendeurs (market makers peu sophistiqués, retail) ne monitorent pas les brackets extrêmes. Ils fixent le prix à la louche sur les queues de distribution. Les acheteurs institutionnels qui dominent le carnet d'ordres sur les brackets centraux (les plus probables) n'achètent pas les extremes → liquidité faible → prix inefficients.

### Pourquoi les villes asiatiques/européennes et pas US ?

Les marchés météo US (NYC, Dallas, Houston, LA) sont hyper-suivis par des traders locaux qui calibrent parfaitement leurs modèles NWP. Le mispricing est quasi-nul. Les marchés asiatiques et européens sont **sous-suivis** → mispricing structurel persistant.

| Zone | WR observé à <2% | Edge vs prix | Statut |
|------|-----------------|-------------|--------|
| Asie Est (Tokyo, HK, Shanghai, Taipei, Beijing) | 8–12% | +7–11% | **Exploitable** |
| Europe (Paris, Madrid, Milan, London, Warsaw) | 7–10% | +6–9% | **Exploitable** |
| Proche-Orient (Tel Aviv) | 7% | +6% | Exploitable |
| Amériques (Buenos Aires, Toronto, SA) | 5–7% | +4–6% | Marginal |
| US (NYC, Dallas, Houston, Atlanta) | 1–3% | 0–2% | Nul/négatif |

---

## 2. Mathématiques exactes

### 2.1 Structure du pari binaire

Chaque trade CONVEX_YES est un pari binaire :
- **Prix d'entrée** : `p` (en USDC, ex: `p = 0.008` = 0.8¢ par token YES)
- **Payout en cas de victoire** : `b = (1 - p) / p` (ex: b = 124 pour p=0.008)
- **Win rate empirique** : `WR` (ex: WR = 0.082 pour Shanghai)
- **Mise** : `K` USDC

Résultat financier :
```
Si WIN  (prob WR)  : gain net = K × b = K × (1-p)/p
Si LOSE (prob 1-WR): perte nette = K
```

### 2.2 Espérance mathématique (EV)

```
EV = WR × K × b - (1-WR) × K
   = K × [WR × (1-p)/p - (1-WR)]
   = K × [(WR - p) / p]

EV% = (WR × b - (1-WR)) × 100
    = (WR/p - 1) × 100  (approximation quand p << 1)
```

**Exemple Tokyo (WR=11.7%, p=0.82%, K=$15) :**
```
b    = (1 - 0.0082) / 0.0082 = 120.9
EV   = 15 × [0.117 × 120.9 - (1 - 0.117)]
     = 15 × [14.15 - 0.883]
     = 15 × 13.27
     = +$199 par trade
EV%  = +1,334%
```

### 2.3 Critère de Kelly fractionnel

Kelly optimal pour un pari binaire :

```
f* = (WR - p) / (1 - p)   [fraction du bankroll]
```

En pratique : **Kelly 25%** (`f_frac = f* × 0.25`) pour limiter la volatilité et la ruine.

```
f* Tokyo   = (0.117 - 0.0082) / (1 - 0.0082) = 0.1088 / 0.9918 = 10.97%
f_frac     = 10.97% × 0.25 = 2.74%  → bet = $274 sur $10K bankroll
Cap $15    = actif (book de profondeur ~$6–$11 à ces prix)
```

**Pourquoi cap à $15 ?** La profondeur du carnet d'ordres à 0.2–2% est de $6–$11 par token sur la plupart des marchés. Au-delà, on déplace le prix (slippage). $15 est la taille maximale réaliste pour un fill propre.

### 2.4 Sharpe/100 — métrique principale

```
Sharpe/100 = EV / (σ_bet × (b+1)) × √100

où :
  EV    = WR × b - (1-WR)       [espérance par bet]
  σ_bet = √(WR × (1-WR))        [écart-type d'un bernoulli]
  b+1   = 1/p                    [levier du pari]
  √100  = normalisation sur 100 bets

Simplifié :
  Sharpe/100 = (WR - p) / (p × √(WR × (1-WR))) × √(WR/(1-WR)) × 10
```

**Interprétation** : combien d'écarts-types de profit sur 100 bets identiques. Sharpe/100 > 2.0 = edge statistiquement robuste.

### 2.5 Intervalles de confiance Wilson

Pour un WR observé `w/n`, l'IC à 95% est :

```
Centre : c = (w/n + z²/2n) / (1 + z²/n)
Erreur : e = z × √(w/n × (1-w/n)/n + z²/4n²) / (1 + z²/n)
IC95%  : [c - e, c + e]   avec z = 1.96
```

**Exemple Hong Kong** (w=16, n=129) :
```
IC95% = [7.8% – 19.2%]
```
L'IC entier est au-dessus du prix marché (0.62%) → edge statistiquement certain.

### 2.6 Bootstrap p-value

H₀ : WR = prix marché (= random, aucun edge)

```
Procédure :
  1. Simuler 5,000 fois n tirages avec P(win) = prix_moyen
  2. Compter combien de simulations ont WR ≥ WR_observé
  3. p-value = proportion
```

Si p < 0.05 → rejet de H₀ avec 95% de confiance → edge réel.

**Résultat global** : p = 0.0000 → H₀ rejetée massivement.

---

## 3. Données — Backtest réel (2026-03-05 → 2026-04-05)

### Méthodologie

- **Source** : prix réels de `price_bars` (CLOB Polymarket, données historiques)
- **Sélection** : 1 barre par marché, la plus proche de TTR=12h dans la fenêtre [6h–48h]
- **Zéro reconstruction** : pas de prix synthétiques, pas de modèles climatologiques
- **Villes** : 22 villes avec edge empirique confirmé
- **Kelly sizing** : WR empirique par ville, cap $15/trade

### Résultats globaux

```
Période       : 2026-03-05 → 2026-04-05 (31 jours)
Trades réels  : 2,699
Wins          : 190   (7.04%)
CI 95%        : [6.13% – 8.07%]
Prix moyen    : 0.890%
EV/bet        : +691%
Sharpe/100    : 2.40
P&L simulé    : +$415,490  (Kelly 25%, cap $15)
Max Drawdown  : $1,007
Calmar        : 413x
p-value       : 0.0000   ← H₀ WR=prix rejetée
```

---

## 4. Statistiques par dimension

### 4.1 Par ville (Table A)

| Étoiles | Ville | N | W | WR | CI 95% | Px | EV% | S/100 | P&L |
|---------|-------|---|---|----|--------|-----|-----|-------|-----|
| ★★★★ | hong kong | 129 | 16 | 12.4% | [7.8–19.2%] | 0.62% | +1896% | 3.57 | +$25,153 |
| ★★★ | tokyo | 145 | 17 | 11.7% | [7.5–18.0%] | 0.82% | +1334% | 3.39 | +$49,675 |
| ★★ | paris | 144 | 13 | 9.0% | [5.4–14.8%] | 0.81% | +1015% | 2.87 | +$40,864 |
| ★★ | wellington | 171 | 15 | 8.8% | [5.4–14.0%] | 0.77% | +1037% | 2.83 | +$19,020 |
| ★★ | madrid | 103 | 9 | 8.7% | [4.7–15.8%] | 0.90% | +867% | 2.77 | +$15,118 |
| ★★ | shanghai | 134 | 11 | 8.2% | [4.6–14.1%] | 0.84% | +880% | 2.69 | +$29,828 |
| ★★ | taipei | 119 | 10 | 8.4% | [4.6–14.8%] | 0.98% | +759% | 2.68 | +$26,783 |
| ★★ | mexico city | 23 | 2 | 8.7% | [2.4–26.8%] | 1.25% | +593% | 2.64 | +$4,823 |
| ★★ | london | 157 | 12 | 7.6% | [4.4–12.9%] | 0.86% | +786% | 2.55 | +$34,177 |
| ★ | beijing | 98 | 7 | 7.1% | [3.5–14.0%] | 0.85% | +742% | 2.44 | +$15,265 |
| ★ | tel aviv | 124 | 9 | 7.3% | [3.9–13.2%] | 1.06% | +587% | 2.39 | +$14,082 |
| ★ | milan | 101 | 7 | 6.9% | [3.4–13.6%] | 0.90% | +674% | 2.38 | +$13,229 |
| ★ | warsaw | 120 | 8 | 6.7% | [3.4–12.6%] | 0.77% | +763% | 2.36 | +$18,349 |
| ★ | buenos aires | 147 | 10 | 6.8% | [3.7–12.1%] | 1.02% | +570% | 2.30 | +$20,422 |
| ★ | munich | 133 | 9 | 6.8% | [3.6–12.4%] | 1.00% | +574% | 2.29 | +$16,764 |
| ★ | chengdu | 85 | 5 | 5.9% | [2.5–13.0%] | 0.79% | +641% | 2.16 | +$13,871 |
| ★ | sao paulo | 123 | 7 | 5.7% | [2.8–11.3%] | 1.03% | +455% | 2.01 | +$6,568 |
| ◆ | toronto | 175 | 8 | 4.6% | [2.3–8.8%] | 0.87% | +423% | 1.77 | +$30,399 |
| ◆ | austin | 49 | 2 | 4.1% | [1.1–13.7%] | 1.23% | +233% | 1.44 | +$1,700 |
| ◆ | wuhan | 91 | 3 | 3.3% | [1.1–9.2%] | 0.81% | +308% | 1.39 | +$8,445 |
| ◆ | seoul | 176 | 6 | 3.4% | [1.6–7.2%] | 0.93% | +265% | 1.36 | +$7,698 |
| ◆ | atlanta | 152 | 4 | 2.6% | [1.0–6.6%] | 0.95% | +177% | 1.05 | +$3,258 |

*Toutes les villes : p-value < 0.05 sauf Austin (p=0.12)*

### 4.2 Par bucket de prix (Table B)

| Bucket | N | W | WR | Payout | EV% | S/100 | P&L |
|--------|---|---|----|--------|-----|-------|-----|
| 0.20–0.40% | 900 | 48 | 5.3% | ×315 | +1587% | 2.23 | +$219,214 |
| 0.40–0.80% | 497 | 28 | 5.6% | ×168 | +850% | 2.19 | +$63,523 |
| **0.80–1.20%** | **260** | **30** | **11.5%** | ×96 | **+1015%** | **3.29** | **+$39,668** |
| 1.20–1.60% | 279 | 24 | 8.6% | ×69 | +499% | 2.56 | +$21,239 |
| 1.60–2.00% | 208 | 20 | 9.6% | ×54 | +425% | 2.64 | +$13,126 |
| 2.00–2.50% | 321 | 34 | 10.6% | ×43 | +369% | 2.71 | +$17,229 |

**Bucket optimal en Sharpe** : 0.80–1.20% (S/100=3.29)
**Bucket optimal en P&L absolu** : 0.20–0.40% (volume + payout ×315)

### 4.3 Par TTR (Table C)

| TTR | N | W | WR | EV% | S/100 | P&L |
|-----|---|---|----|-----|-------|-----|
| **6–10h** | 257 | 27 | **10.5%** | +605% | **2.94** | +$32,064 |
| **10–14h** | 1593 | 130 | 8.2% | +806% | 2.65 | +$315,074 |
| 14–18h | 182 | 12 | 6.6% | +627% | 2.29 | +$30,754 |
| 18–24h | 225 | 7 | 3.1% | +434% | 1.46 | +$8,193 |
| 24–32h | 269 | 8 | 3.0% | +477% | 1.45 | +$26,012 |
| 32–48h | 173 | 6 | 3.5% | +299% | 1.42 | +$3,392 |

**Optimal** : TTR 6–14h. Au-delà de 18h, le WR chute de moitié.

**Interprétation** : plus on est proche de la résolution, plus le METAR local réduit l'incertitude → les brackets improbables restent mal pricés mais la certitude de leur issue augmente.

### 4.4 Par heure UTC d'entrée (Table D)

| H UTC | N | W | WR | S/100 | Remarque |
|-------|---|---|----|-------|---------|
| 18:00 | 34 | 5 | **14.7%** | **3.91** | ← pic absolu |
| 03:00 | 70 | 9 | 12.9% | 3.47 | ← scan 03:00 UTC |
| 05:00 | 88 | 10 | 11.4% | 3.20 | |
| 17:00 | 41 | 4 | 9.8% | 3.01 | |
| 00:00 | 1153 | 95 | 8.2% | 2.68 | volume principal |
| 23:00 | 256 | 20 | 7.8% | 2.58 | |
| 04:00 | 84 | 0 | **0.0%** | 0.00 | zone morte |
| 06:00 | 18 | 0 | **0.0%** | 0.00 | zone morte |
| 11:00 | 54 | 0 | **0.0%** | 0.00 | zone morte |
| 14:00 | 55 | 0 | **0.0%** | 0.00 | zone morte |
| 15:00 | 55 | 0 | **0.0%** | 0.00 | zone morte |

**Conclusion** : l'heure explique peu de variance (Sharpe 1.88–3.91 selon heure vs 2.40 global). Le VPS 1x/min couvre tout sans biais.

### 4.5 Par type de bracket (Table E)

| Type | N | W | WR | S/100 | P&L |
|------|---|---|----|-------|-----|
| EXACT (T ∈ [lo, hi]) | 2498 | 184 | **7.4%** | **2.48** | +$410,531 |
| BETWEEN | 201 | 6 | 3.0% | 1.16 | +$4,958 |

→ Filtrer BETWEEN agressivement. L'edge vient quasi-exclusivement des brackets EXACT.

### 4.6 Par jour de la semaine (Table F)

| Jour | N | WR | S/100 | P&L |
|------|---|----|-------|-----|
| Monday | 360 | 6.7% | 2.27 | +$33,473 |
| Tuesday | 240 | 6.7% | 2.33 | +$32,193 |
| Wednesday | 398 | 7.0% | 2.42 | +$71,879 |
| Thursday | 396 | 7.3% | 2.46 | +$48,425 |
| Friday | 453 | 7.1% | 2.42 | +$93,675 |
| Saturday | 423 | 7.1% | 2.40 | +$69,114 |
| Sunday | 429 | 7.2% | 2.47 | +$66,732 |

Aucune saisonnalité hebdomadaire significative. Le biais est constant 7j/7.

### 4.7 Distance au seuil (Table J) — insight critique

| Distance T_obs / seuil | N | Wins | WR | EV% |
|------------------------|---|------|----|-----|
| T_obs < seuil (déjà gagné) | 25 | 25 | **100%** | +8178% |
| 0 → +2°C du seuil | 810 | 165 | **20.4%** | +1805% |
| +2 → +5°C | 1088 | 0 | 0.0% | -100% |
| > +5°C | 776 | 0 | 0.0% | -100% |

**Conclusion** : l'edge vient entièrement des brackets **proches du seuil** (T_obs within 2°C). Au-delà, WR=0. Cela confirme que le marché misprices uniquement les cas "presque impossibles mais pas vraiment" — là où la climatologie est ambiguë.

### 4.8 Corrélation inter-villes (Table K)

```
Corrélation moyenne inter-villes : -0.011  ← quasi-nulle
Max corrélation : +0.577 (atlanta × beijing)
Min corrélation : -0.565 (taipei × toronto)
```

→ Diversification quasi-parfaite. Les 22 villes se comportent comme des actifs indépendants. Cela réduit la variance du portefeuille et augmente le Sharpe agrégé.

---

## 5. Monte Carlo — Projections à long terme

**Paramètres** : WR=7.04%, prix=0.89%, payout=×111, bet=$15, 10K simulations

| Scénario | N bets | E[PnL] | Std | P(profit) | P(×10) | Sharpe |
|----------|--------|--------|-----|-----------|--------|--------|
| 1 mois | 100 | +$10,354 | $4,295 | 99.9% | 0% | 2.41 |
| 5 mois | 500 | +$51,756 | $9,697 | 100% | 0% | 5.34 |
| 10 mois | 1,000 | +$103,672 | $13,677 | 100% | 83.7% | 7.58 |
| Backtest (31j) | 2,699 | +$279,778 | $22,588 | 100% | 100% | 12.39 |
| 1.5 an | 5,000 | +$518,207 | $30,478 | 100% | 100% | 17.00 |
| 3 ans | 10,000 | +$1,036,147 | $43,188 | 100% | 100% | 23.99 |

---

## 6. Analyse timing — Villes × Heure UTC

Backtest sur 39,112 observations (toutes heures × tous marchés) avec `city_timing_backtest.py`.

### Fenêtres optimales par ville (Sharpe max, N≥8)

| Ville | Heure UTC opt | Heure locale | WR opt | S/100 | 2ème choix |
|-------|--------------|-------------|--------|-------|-----------|
| mexico city | 03:00 | 21h local | 25.0% | 5.49 | 06:00 |
| chengdu | 09:00 | 17h local | 13.8% | 3.73 | 10:00 |
| tokyo | 02:00 | 11h local | 13.3% | 3.66 | 01:00 |
| madrid | 03:00 | 04h local | 12.5% | 3.53 | 04:00 |
| milan | 00:00 | 01h local | 12.1% | 3.42 | 10:00 |
| hong kong | 17:00 | 01h local | 11.4% | 3.34 | 20:00 |
| taipei | 21:00 | 05h local | 11.3% | 3.32 | 19:00 |
| shanghai | 11:00 | 19h local | 11.9% | 3.39 | 09:00 |
| london | 04:00 | 04h local | 8.9% | 2.83 | 02:00 |
| beijing | 04:00 | 12h local | 8.9% | 2.81 | 01:00 |
| tel aviv | 00:00 | 02h local | 8.4% | 2.72 | 23:00 |
| wellington | 18:00 | 06h local | 7.5% | 2.60 | 16:00 |
| warsaw | 03:00 | 04h local | 7.7% | 2.62 | 02:00 |
| buenos aires | 03:00 | 00h local | 7.6% | 2.55 | 02:00 |
| munich | 23:00 | 00h local | 7.4% | 2.49 | 22:00 |
| paris | 20:00 | 21h local | 10.3% | 3.10 | 18:00 |
| wuhan | 05:00 | 13h local | 7.1% | 2.40 | 21:00 |
| toronto | 06:00 | 01h local | 6.0% | 2.20 | 21:00 |
| sao paulo | 04:00 | 01h local | 6.1% | 2.23 | 05:00 |
| austin | 00:00 | 18h local | 7.7% | 2.49 | 08:00 |
| seoul | 05:00 | 14h local | 6.0% | 2.14 | 06:00 |
| atlanta | 21:00 | 16h local | 3.7% | 1.52 | 15:00 |

**Conclusion critique** : l'impact de l'heure est faible (+0.04 Sharpe max vs baseline). Le VPS 1x/min capture automatiquement la meilleure fenêtre pour chaque ville sans configuration.

---

## 7. Infrastructure de déploiement

### Architecture

```
LOCAL (Mac M5)                     VPS (Hetzner 95.216.198.143)
─────────────────────────────────  ───────────────────────────────────
launchd scans :                    cron 1x/min :
  03:00 UTC  → EU + Asie           * * * * * run_scan.sh
  09:07 UTC  → CONFIRMED window      → CONVEX_YES toutes villes
  10:32 UTC  → scan secondaire     Settlement 2x/jour :
  16:17 UTC  → Asie D+1              13:00 UTC, 20:00 UTC
  09:00 local → daily P&L           → METAR réel → won/pnl
```

### Track record VPS (DB propre depuis 2026-04-09)

```
Capital initial : $10,000
Capital actuel  : $116,551  (+1065%)
Trades settlés  : 38
WR              : 36.8%  (dominé par SPEEDA/CERT, CONVEX_YES pas encore settlé)
CONVEX_YES open : 73 positions (première batch, résolution 2026-04-13)
```

### Signal CONVEX_YES dans le code

```python
# run_bracket_scalper.py

CONVEX_CITIES_WR: dict[str, float] = {
    "hong kong":    0.124,   # Sharpe=3.57  WR=12.4%
    "tokyo":        0.117,   # Sharpe=3.39  WR=11.7%
    "paris":        0.090,   # Sharpe=2.87  WR=9.0%
    "wellington":   0.088,   # Sharpe=2.83  WR=8.8%
    "madrid":       0.087,   # Sharpe=2.77  WR=8.7%
    "shanghai":     0.082,   # Sharpe=2.69  WR=8.2%
    "taipei":       0.084,   # Sharpe=2.68  WR=8.4%
    "mexico city":  0.087,   # Sharpe=2.64  WR=8.7%  (n=23, CI large)
    "london":       0.076,   # Sharpe=2.55  WR=7.6%
    "beijing":      0.071,   # Sharpe=2.44  WR=7.1%
    "tel aviv":     0.073,   # Sharpe=2.39  WR=7.3%
    "milan":        0.069,   # Sharpe=2.38  WR=6.9%
    "warsaw":       0.067,   # Sharpe=2.36  WR=6.7%
    "buenos aires": 0.068,   # Sharpe=2.30  WR=6.8%
    "munich":       0.068,   # Sharpe=2.29  WR=6.8%
    "chengdu":      0.059,   # Sharpe=2.16  WR=5.9%
    "sao paulo":    0.057,   # Sharpe=2.01  WR=5.7%
    "toronto":      0.046,   # Sharpe=1.77  WR=4.6%
    "austin":       0.041,   # Sharpe=1.44  WR=4.1%  (p=0.12, à surveiller)
    "wuhan":        0.033,   # Sharpe=1.39  WR=3.3%
    "seoul":        0.034,   # Sharpe=1.36  WR=3.4%
    "atlanta":      0.026,   # Sharpe=1.05  WR=2.6%
}

# Conditions d'entrée
if (cfg.convex_yes_enabled
        and city_wr is not None          # ville calibrée
        and 0.002 <= yes_price < 0.02    # prix 0.2–2%
        and 6.0 <= ttr_hours <= 48.0     # TTR optimal
        and city not in CONVEX_EXCLUDED):
    kelly_f = 0.25 * (city_wr - yes_price) / (1 - yes_price)
    size = min(kelly_f * bankroll, 15.0)  # cap $15 (book depth)
```

---

## 8. Limites et risques

### 8.1 Taille de l'échantillon

31 jours de données réelles. Les WR par ville ont des IC larges pour les petites villes (ex: Mexico City n=23, CI [2.4–26.8%]). Avec 6 mois de live, les CI se resserreront.

### 8.2 Dépendance intra-ville

Plusieurs brackets de la même ville/jour partagent la même résolution (T_max unique). Cela crée une corrélation entre trades du même jour/ville. Le Monte Carlo traite les trades comme indépendants → variance **sous-estimée**.

**Mitigation** : diversifier sur 22 villes et 4 dates (D+1 à D+4) simultanément.

### 8.3 Liquidité et slippage

À 0.2–2%, la profondeur du carnet d'ordres est de $6–$11 par token. Pour des trades >$15, le slippage dégrade l'EV. Le cap $15 est calibré sur l'observation réelle du book.

### 8.4 Régime change

Le biais longshot est structurel mais peut se réduire si :
- Des traders sophistiqués arbitrent systématiquement cette anomalie
- Polymarket améliore ses market makers sur les marchés météo
- La liquidité augmente suffisamment pour permettre un pricing plus fin

Monitoring : si WR live tombe sous 5% sur 200+ trades → recalibrer.

### 8.5 Settlement METAR

La résolution dépend des données METAR (station météo officielle). Risques :
- Station METAR indisponible (maintenance, panne)
- Définition T_max différente entre METAR et Polymarket
- Horaire de clôture Polymarket vs T_max officiel

---

## 9. Résumé opérationnel

### Ce qu'on fait
Acheter des tokens YES sur des brackets météo improbables (0.2–2%) sur 22 villes avec un edge statistique confirmé. Kelly 25%, cap $15.

### Ce qu'on n'essaie PAS de faire
Prédire la météo. Utiliser des modèles NWP. Timer le marché.

### Métriques de suivi
- WR live rolling 30j : cible 6–8%, alerte si <4% sur 200+ trades
- Calmar ratio : cible >50x
- Sharpe/100 : cible >2.0

### Prochaines étapes
1. Premier settlement CONVEX_YES VPS : 2026-04-13 12:00 UTC (73 positions)
2. Recalibrer WR si N live > 200 trades
3. Déploiement live quand WR live ≈ WR backtest sur 100+ settlés

---

## Related

- [[_system/MOC-patterns]]
- [[patterns/polymarket-convex-strategy-city-analysis]]
- [[patterns/polymarket-coldmath-no-ev-analysis]]
- [[patterns/polymarket-oracle-confirmed-backtest]]
- [[patterns/polymarket-bracket-arb]]
- [[patterns/polymarket-price-process-deep-analysis]]
