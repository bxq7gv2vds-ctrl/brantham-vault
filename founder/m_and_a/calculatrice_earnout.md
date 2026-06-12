---
name: calculatrice_earnout
description: Outil de calcul earnout & holdback pour structurer les deals SaaS
metadata:
  type: tool
  format: spreadsheet_template
  version: 1.0
---

# Calculatrice Earnout & Holdback

## **INPUTS — À remplir**

```
Enterprise Value (EV)          €[  1.000.000  ]
├─ ARR target                  €[    250.000  ]  (ex: 4x ARR)
├─ EBITDA margin               [      20%     ]

Dettes nettes                  €[    (50.000) ]
NWC adjustment                 €[        0    ]
─────────────────────────────────────────────
Equity Value à payer           €[    950.000  ]
```

---

## **STRUCTURE PAIEMENT**

### Scénario 1 : 60 cash + 15 holdback + 25 earnout

```
Equity Value                   €950.000

Paiement @ closing
├─ Cash au vendeur             €570.000  (60%)
├─ Escrow (holdback)           €142.500  (15%)
└─ Earnout promis              €237.500  (25%)

Escrow (18 mois)
├─ Libération 12m              €71.250
└─ Libération 18m              €71.250
```

**Vendeur encaisse :** €570k jour 1, +€142.5k à 18m si DD OK.
**Earnout** : dépend retention/croissance (années 1–3).

---

### Scénario 2 : 70 cash + 20 holdback + 10 earnout (vendeur préfère)

```
Paiement @ closing
├─ Cash au vendeur             €665.000  (70%)
├─ Escrow (holdback)           €190.000  (20%)
└─ Earnout promis              €95.000   (10%)
```

**Avantage vendeur :** liquidités immédiates, earnout bas = moins de risque acheteur « tue le produit ».

---

### Scénario 3 : 50 cash + 25 earnout + 25 locked shares (si acheteur SaaS)

```
Paiement @ closing
├─ Cash au vendeur             €475.000  (50%)
├─ Actions acheteur            €237.500  (25%) — vesting 4 ans
└─ Earnout métrique            €237.500  (25%) — 18 mois

Vendeur devient shareholder acheteur → upside, mais risque liquidité.
```

---

## **EARNOUT — Exemples de structures**

### Structure 1 : Rétention client (le plus simple)

```
Metrique  : Client retention rate (CRR)
Target    : ≥ 85% au 12-18 mois
Payout    : €95.000 si target atteint
           €47.500 si 80-85%
           €0 si <80%
```

**Formule simple** : 
```
CRR_actual = (Clients_retained_18m / Clients_at_closing) × 100
Earnout = Base × (CRR - 80%) / 5%  [capped at €95k]
```

---

### Structure 2 : ARR growth + retention combo

```
Année 1 :
├─ Si ARR croît ≥15%  →  €50.000
├─ Si retention ≥85%  →  €30.000
└─ Total possible      →  €80.000

Année 2 :
├─ Si ARR croît ≥10%  →  €30.000
└─ Total Y2 possible   →  €30.000

Total earnout maximum  €110.000
```

---

### Structure 3 : EBITDA margin (pour produits matures)

```
Target    : EBITDA margin ≥ 25% (vs 20% today)
Payouts   : 
├─ €50k si 22-23%
├─ €75k si 23-24%
└─ €95k si ≥25%
```

---

## **HOLDBACK — Allocations typiques**

```
Total equity value           €950.000
├─ Représentations générales €90.000  (9-10%)
├─ Indemnités taxes          €47.500  (5%)
└─ Reps spécifiques (IP)     €4.750   (0.5%)
─────────────────────────────────────
Total holdback              €142.500  (15%)

Libération : 
├─ @ 12 mois                 €71.250  (si aucune claim)
└─ @ 18 mois                 €71.250  (si aucune claim)
```

**Durée réclamation :**
- Reps générales : 18 mois
- Taxes : 3-6 ans (per jurisdiction)
- IP/IP infringement : 3-5 ans

---

## **CALCUL RÉEL : Exemple SaaS €250k ARR**

```
Inputs:
├─ ARR                        €250.000
├─ Multiple visé              3.5x
├─ Dettes nettes              €0
├─ NWC adjustment             €0
─────────────────────────────
EV                           €875.000

Paiement au closing:
├─ Cash (65%)                €568.750  ← Vendeur reçoit immédiatement
├─ Holdback (18 mois)        €131.250  ← Si aucune réclamation
├─ Earnout Y1                €87.500   ← Si 85% retention
├─ Earnout Y2 (si croissance)€87.500   ← Si +10% ARR
─────────────────────────────
Total encaissement possible   €875.000

Cas pessimiste (client perd 20% ARR, earnout réduit):
├─ Cash reçu                 €568.750  (garanti)
├─ Holdback perdu            €131.250  (si claims)
├─ Earnout réduit            €43.750   (50% seulement)
─────────────────────────────
Total réel (cas bad)          €743.750  (-€131k vs expectations)
```

---

## **Questionnaire pour décider de la structure**

1. **As-tu besoin de liquidités maintenant ou peux-tu attendre ?**
   - Oui, tout de suite → max cash (70%+)
   - Non → accepter 50% cash + earnout

2. **As-tu confiance en l'acheteur de retenir tes clients ?**
   - Oui → earnout sur rétention (safe)
   - Non → holdback/earn-out court (12m) + exit clause

3. **Veux-tu rester impliqué ou sortir complètement ?**
   - Rester → actions acheteur + rôle consultatif
   - Partir → cash + peu de dépendances futures

4. **Crains-tu que l'acheteur réduise volontairement l'ARR pour baisser l'earnout ?**
   - Oui → structurer earnout min-floor ou reps avec clause anti-dilution
   - Non → simple earnout sur ARR

---

## **Note finale**

Typique M&A SaaS <€2M : **65% cash + 15% holdback + 20% earnout**
- Vendeur : liquidités jour 1 (€)
- Acheteur : protection (holdback) + optionnel croissance (earnout)
- Deal : structure équilibrée, peu de friction

