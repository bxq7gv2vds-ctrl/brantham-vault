---
title: Build vs Buy — Decision Framework
created: 2026-06-12
category: acquisition
status: active
---

# Build vs Buy — Framework de décision rapide

**Usage** : Décider en 30 min si l'acquisition se justifie vs construire en interne.

---

## 1. Critères de comparaison

| Dimension | BUILD | BUY | Poids décision |
|-----------|-------|-----|-----------------|
| **Temps au marché** | 18-36 mois | 3-6 mois | ⭐⭐⭐⭐⭐ |
| **Coût d'acquisition** | $0 M&A | $5-50M+ | ⭐⭐⭐ |
| **Coût de développement** | $2-10M R&D | $0 | ⭐⭐ |
| **Risque technique** | Moyen-haut | Bas (héritée) | ⭐⭐⭐ |
| **Risque commercial** | Haut (adoption) | Bas (clients acquis) | ⭐⭐⭐ |
| **Talent acquis** | Recruter 10-20p | Gain 30-50p immédiat | ⭐⭐ |
| **Coût d'intégration** | Moyen (équipe interne) | Haut (fusion) | ⭐⭐ |
| **IP & propriété** | 100% | Potentiel problème (antérieurs) | ⭐ |

---

## 2. Arbre de décision rapide

```
Besoin urgent (< 12 mois)?
├─ OUI → Time-to-market = priorité → BUY ✓
└─ NON → Continuer...
   
   Cible existe et validée?
   ├─ NON → Product fit risqué → BUILD ✓
   └─ OUI → Continuer...
      
      Coût achat < 3 × coût build + risque?
      ├─ OUI → BUY ✓
      └─ NON → BUILD ✓
```

---

## 3. Checklist rapide : Quand BUY est légitime

**Acquérir si ≥3 des 5 conditions** :

- ✅ **Time value** : Besoin produit dans 12 mois (avant construction finie)
- ✅ **Équipe acquise** : Talent rare/difficile à recruter (ex: ML engineers, growth expert)
- ✅ **Clients existants** : Base consolidée (ARR, NRR>100%, faible churn)
- ✅ **Synergies claires** : >20% cost savings OU >2x revenue multiplier 
- ✅ **Fermeture compétitive** : Concurrent achète → perte market share

---

## 4. Checklist rapide : Quand BUILD est mieux

**Construire si ≥3 des 5 conditions** :

- ✅ **Budget R&D disponible** : Startup peut attendre 18-24 mois
- ✅ **Pas de talent rare** : Peut recruter ingénieurs senior
- ✅ **Cibles peu matures** : Aucun produit au marché prêt à acheter
- ✅ **Différenciation forte** : Feature unique que cible n'a pas
- ✅ **Risk de diligence haute** : Trop de red flags cible (churn, debt, culture)

---

## 5. Cas particulier : Build + Buy hybride

**Stratégie mixte** :

1. **Build MVP vite** (4-6 mois)
2. **Acquérir competitor ou complément** (9-12 mois)
3. **Fusionner roadmaps** dans la même équipe

**Exemple** : Slack (built messaging) + acquired Glitch (DevTools) + absorbed into product.

---

## 6. Coût réel acquisition (caché)

Ne pas comparer uniquement "achat" vs "salaires R&D". Inclure :

```
BUY cost = Purchase price + Integration + Talent attrition + Lost rev from churn + Opportunity cost capital
         ≈ $10M achat + $2M intégration + $1M churn + $3M management time
         = $16M réel (vs $10M price)

BUILD cost = 18 mois × 8 eng × $250k/an + mgt time + opportunity cost
          ≈ $3M salaires + $1M infrastructure + $2M opportunity
          = $6M réel (vs $3M directs)
```

**Vraie question** : $16M achat vs $6M build = payoff en < 2 ans de revenue multiplier? Si non, passer.

---

## 7. Exemples d'industries

| Industrie | Tendance | Raison |
|-----------|----------|--------|
| **SaaS B2B** | 60% BUY | Time-to-market critique, talent rare |
| **Fintech** | 70% BUILD | Régulation, IP propriétaire, compliance |
| **Martech** | 80% BUY | Fragmentation, besoin intégrations |
| **Infrastructure** | 50/50 | Dépend talent disponible |

---

## 8. Template de décision final

**Remplir en 20 min** :

```markdown
## Décision : [CIBLE NAME]

### Urgence temps
- Besoin produit dans X mois? _____
- Compétition presse? OUI/NON

### Équipe & talent
- Talent clé acquis? OUI/NON
- Peut le recruire? OUI/NON (coût: $___k)

### Finances
- Budget achat disponible? $___M
- Budget R&D sur 18m? $___M
- Coût réel achat (avec intégration)? $___M
- Coût réel build? $___M

### Décision
→ **BUY** si (urgence temps) OU (talent + clients)
→ **BUILD** si (budget ample) ET (pas urgence) ET (équipe motiv.)
→ **HYBRID** si (MVP + acq complément)
```

---

## Points clés

1. **Timing compte plus que coût** — si urgence < 12 mois, BUY souvent gagne
2. **Talent est le vrai levier** — acquérir 30 engineers = 2-3 ans recruitement
3. **Synergies doivent être claires** — sinon payer "coût + intégration" pour zero upside
4. **Red flags = trop de risque** — si cible est pourrie, pas d'acquis vaut pas de coût
