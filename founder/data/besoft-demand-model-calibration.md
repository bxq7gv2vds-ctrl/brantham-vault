---
name: BeSoft Demand Model Calibration v2
description: Reverse-engineered demand model from 2 BeSoft universes (Paul 6f + Leo 5f), 6 periods, 11 firms, 21K+ data points. Updated 2026-03-22.
type: reference
---

# BeSoft Demand Model — Full Reverse-Engineering (v2)

Updated: 2026-03-22
Sources: `/Users/paul/Desktop/Besoft Paul/` (Sim #3535, U05, 6 firms) + `/Users/paul/Desktop/Besoft Leo/` (5 firms)

## Architecture BeSoft

BeSoft utilise un modele **MNL (Multinomial Logit)** :
1. Marche total local = f(seasonal, macro) — ~20,000 u normalise pour 6 firmes
2. Attractivite firme = f(prix, pub, vendeurs, travel)
3. Part de marche = attractivite relative
4. Demand_i = marche_total × share_i

Notre approximation lineaire fonctionne bien quand les prix sont proches (P1-P2).

## Parametres calibres (v2)

### Base Demand
- **3,300 u/firme** desaisonnalise (was 3,200 in v1)
- Cross-validation:
  - Paul P1: 21,434/6 = 3,572/firme at seasonal 107 → **3,339 desais.**
  - Leo P1: 17,658/5 = 3,532/firme at seasonal 107 → **3,301 desais.**
  - Ratio Leo/Paul: 0.989 (< 1% delta = independant du nb de firmes)

### Price Elasticity
- **85 u/EUR** d'ecart vs moyenne concurrents — INCHANGE
- Methodes convergentes:
  - Regression directe P1 (6 firmes): pente = -87.4, R² = 0.848
  - Pairwise F3 vs F4 (extreme spread): 350/4.11 = **85.2 u/EUR**
  - Pairwise moyenne: 151 (biaisee par paires proches), mediane: 103
- **competitor_prices doit EXCLURE notre propre prix** (valide: F3 exact match 0.0% avec EXCLUT)

### Advertising Effect
- Formula: `200 * (1 - 3600 / advertising)` (was 300 in v1)
- Reduced from 300 to **200** based on P2 residual analysis:
  - Paul F1 P1→P2: ads 5K→7.5K, residual net = ~20-30 units (not 72 as predicted by 300)
- Values:
  - At 3,600 (min): 0
  - At 5,000: **+56 u**
  - At 7,500: **+104 u**
  - At 10,000: **+128 u**
  - At 15,000: **+152 u**
  - Max: ~200 u (asymptote)

### Seller Effect
- **+150 u/vendeur** au-dela de 2 (was 250 in v1)
- Reduced from 250 to 150 based on Leo F4 P1→P2:
  - Added 1 seller (+1K ads, -0.50 price, better seasonal)
  - Total demand (ATOM+BOLT) DROPPED from 3,563 to 3,530
  - Model with 250: predicted 3,917 (+387 overshoot)
  - Model with 150: predicted 3,767 (+237 overshoot, still high)
  - Seller effect is hard to isolate but clearly < 250

### Market Memory
- **15%** weight on (previous_sales - base_demand) — INCHANGE
- Difficult to isolate precisely

### Seasonal Indices
- Q1: 107, Q2: 108, Q3: 101, Q4: 84 — constantes BeSoft, 100% fiables

### Demand Clamp
- [1,500 — 4,500] unites — INCHANGE

## Validation croisee (2 univers)

### Pre-BOLT (P1-P2) — 13 data points

| Universe | Period | Firm | Price | Actual | Predicted | Error |
|----------|--------|------|-------|--------|-----------|-------|
| Paul | P1 | F1 | 169.80 | 3,514 | 3,506 | -0.2% |
| Paul | P1 | F2 | 168.90 | 3,687 | 3,598 | -2.4% |
| Paul | P1 | F3 | 165.89 | 3,826 | 3,905 | +2.1% |
| Paul | P1 | F4 | 170.00 | 3,476 | 3,486 | +0.3% |
| Paul | P1 | F5 | 170.00 | 3,476 | 3,486 | +0.3% |
| Paul | P1 | F6 | 169.50 | 3,455 | 3,537 | +2.4% |
| Paul | P2 | F1 | 164.00 | 4,064 | 4,053 | -0.3% |
| Leo | P1 | F1 | 172.50 | 3,530 | 3,588 | +1.6% |
| Leo | P1 | F2 | 172.50 | 3,497 | 3,588 | +2.6% |
| Leo | P1 | F3 | 172.50 | 3,534 | 3,588 | +1.5% |
| Leo | P1 | F4 | 172.50 | 3,563 | 3,544 | -0.5% |
| Leo | P1 | F5 | 172.50 | 3,534 | 3,588 | +1.5% |

**Erreur moyenne pre-BOLT: 1.5%**

### Post-BOLT — model overpredicts (expected)

| Period | Actual (local) | Predicted | Error | Cause |
|--------|---------------|-----------|-------|-------|
| P3 Paul F1 | 3,614 | 4,075 | +12.8% | BOLT debut (5% du local) |
| P4 Paul F1 | 2,395 | 3,537 | +47.7% | BOLT 10% + Export cannibalise local |
| P5 Paul F1 | 2,855 | 4,083 | +43.0% | BOLT 13% + Export |
| P6 Paul F1 | 2,151 | 3,976 | +84.8% | BOLT 45% du marche local |

Le modele predit la demande ATOM LOCAL. Apres P2, BOLT et l'Export redistribuent la demande.

## Mecanismes BeSoft decouverts

### 3 marches separes
1. **Local ATOM** — marche principal, predit par notre modele
2. **Local BOLT** — cannibalise ATOM local progressivement
3. **Export (ATOM + BOLT)** — marche additionnel, mais reduit le local de ~15-20%

### BOLT cannibalization timeline

| Period | ATOM local % | BOLT local % | Export % | BOLT market effort |
|--------|-------------|-------------|---------|-------------------|
| P1 | 100% | 0% | 0% | 0.00 |
| P2 | 96% | 4% | 0% | 0.00 |
| P3 | 95% | 5% | 0% | 0.15 |
| P4 | 76% | 9% | 15% | 0.20 |
| P5 | 67% | 10% | 23% | 0.30 |
| P6 | 44% | 36% | 20% | 0.40 |

Consistant entre les 2 univers (Paul 6f et Leo 5f).

### Marche total par firme (normalise, TOUT inclus)

| Period | Paul/firme | Leo/firme |
|--------|-----------|----------|
| P1 | 3,339 | 3,301 |
| P2 | 3,441 | 3,285 |
| P3 | 3,136 | 3,064 |
| P4 | 3,204 | 3,189 |
| P5 | 3,564 | 3,535 |
| P6 | 4,103 | 3,652 |

Le marche TOTAL (local+export, ATOM+BOLT) par firme est relativement stable ~3,200-3,500 normalise. Il augmente en P5-P6 grace a l'export.

### Storage costs (formule exacte)
```
storage = 1000 + 1% * min(inv, 180K) + 2% * min(max(inv-180K,0), 360K) + 4% * max(inv-540K, 0)
```
Verifie exact sur F1 Paul P3 (5,305 EUR) et P4 (7,878 EUR).

### Commission
- Quota: 750 u/vendeur, rate: 4.32 EUR/u au-dela — verifie exact P1-P2
- P3+: ecart avec calcul simple → probablement commissions export separees ou rates differents pour BOLT

### Seller salary progression
- P1: 10,800/vendeur, P2: 11,300 (+500), P3: 11,800 (+500)
- P4-P6 avec 3 vendeurs: 34,600/3 = 11,533/vendeur (3e vendeur a un rate different?)

### Export pricing
- F1 Paul: export ATOM = local + 3 EUR systematiquement
- Marche export = marche SEPARE qui ajoute du volume mais reduit le local

## Strategie competition

### T1-T2: le modele est fiable (1.5% erreur)
- Undercut 3-5 EUR vs concurrents
- Production max (3,000)
- Pub 5,100 EUR (optimum recalcule)
- 2-3 vendeurs
- MLT obligatoire T1

### T3+: recalibrer en live
- Entrer les resultats reels dans l'app
- Observer la cannibalization BOLT
- Ajuster le modele avec les prix concurrents observes
- Anticiper BOLT des l'annonce

## Files updated
- `backend/engine/optimizer.py` — `estimate_demand()` recalibrated v2
- `backend/engine/optimizer.py` — ad optimization uses 200 (was 300)
- `backend/tests/test_analysis.py` — baseline demand range updated
- 272 tests green
