---
name: deal-risk-matrix
description: Matrice 4-quadrants taille de deal vs risque d'intégration pour décision rapide
metadata:
  type: reference
---

# Deal Risk × Size Matrix

Utilisez cette matrice pour classer rapidement les targets en 4 quadrants et décider de la stratégie.

```
           TAILLE DEAL (€)
           ↑
       $100M+|
             | [STRAT HQ] | [MAJOR RISK]
       $20-  |            |
       100M  | Complex    | Deal-breaker
             | Steering   | unless perfect
       ------+----------- + --------
       $5-   | [QUICK WIN]| [MEDIUM]
       20M   | Fast close | Manageable
             | Light due  | risk
       ------+-----------+---------
         <$5M| [MICRO]   | [MICRO+]
             | Acqui-hire | Tuck-in
             | Talent     |
             +----------+---------→
             LOW      MEDIUM   HIGH
         (RISQUE INTÉGRATION)
```

---

## Guide par Quadrant

### 🟢 QUICK WIN (<$5M, Low Risk)

**Caractéristiques:**
- Tech complementaire simple
- Équipe alignée (3-5 pers)
- Produit validé, churn <3%
- NRR > 110%

**Stratégie:**
- Timeline : 30-45 jours
- CEO seul négocie
- Due diligence légère (5 jours)
- 1 intégration manager suffit

**Exemple:** Acquérir une API de paiement, outil interne, petite feature complémentaire.

---

### 🟡 MEDIUM ($5-20M, Low-Medium Risk)

**Caractéristiques:**
- Produit validé, traction claire
- Équipe 5-15 pers, 1-2 fondateurs
- Churn <4%, NRR > 105%
- Tech intégrable, pas de legacy majeur

**Stratégie:**
- Timeline : 60-90 jours
- Deal team: CEO + CTO + CFO
- Due diligence : 2 semaines
- Integration manager + 1 tech lead

**Exemple:** Acquérir un concurrent complémentaire, une startup Serie A.

---

### 🟠 COMPLEX ($20-100M, Medium-High Risk)

**Caractéristiques:**
- Traction solide (>$5M ARR) mais points d'interrogation
- Équipe 15-30 pers
- Produit complexe à intégrer
- Risques: churn douteux, culture clash, tech debt

**Stratégie:**
- Timeline : 120-180 jours (patient)
- Deal team complet : CEO, CTO, CFO, General Counsel
- Due diligence approfondie : 4-6 semaines
- PMO (Program Management Office) + steering committee

**Exemple:** Acquérir un concurrent de taille, startup Serie B.

---

### 🔴 MAJOR RISK (>$100M OR High Risk)

**Caractéristiques:**
- Transformation majeure requise
- Équipe 30+ pers, culture très différente
- Tech rewrite potential
- Churn élevée, NRR <100%, concentration clients
- ou : Réglementaire incertain

**Décision:**
- **Walk away sauf** : PMF prouvé, équipe leadership reste, synergies claires >20%
- Timeline : 180+ jours (si continue)
- Full M&A team + external advisors
- Governance : Board + external counsel

**Exemple:** Acquérir une boîte classique, grande transformation, très compliquée.

---

## Scoring Rapide (2 min)

### TAILLE = Deal Price
- <$5M → MICRO
- $5-20M → SMALL
- $20-100M → MID
- >$100M → LARGE

### RISQUE = Somme des points
**Tech:**
- Vert (simple) : 0 pts
- Jaune (moyen) : 5 pts
- Rouge (complexe) : 10 pts

**Équipe:**
- Leader reste : 0 pts
- Leader va partir : 10 pts

**Financière:**
- Croissance >30%, Churn <3% : 0 pts
- Churn 3-5%, croissance 10-30% : 5 pts
- Churn >5%, décroissance : 10 pts

**Clients:**
- Diversifiée, >5 clients significatifs : 0 pts
- 2-3 clients clés : 5 pts
- 1-2 clients = >40% : 10 pts

**Score total :**
- 0-5 : Low Risk
- 5-15 : Medium Risk
- 15-25 : High Risk
- >25 : Major Risk

---

## Action par Quadrant

| Quadrant | Action | Timeline |
|----------|--------|----------|
| Quick Win | Auto-approve | 30-45 jours |
| Medium | Steering + approval | 60-90 jours |
| Complex | Board + advisors | 120-180 jours |
| Major Risk | Walk away ou Major discount | N/A ou 180+ jours |

---

## Prochaines étapes

1. Mapper 3-5 targets potentiels sur cette matrice
2. Discuter quadrant par quadrant avec leadership
3. Approuver targets dans Quick Win/Medium d'abord
4. Revisiter Complex/Major Risk selon trésorerie/stratégie
## Related
