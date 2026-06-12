---
name: ma-valuation-model
description: Modèle d'évaluation d'entreprise multi-méthodes avec pondération sectorielle
metadata:
  type: pattern
  created: 2026-06-12
  tags: [ma, évaluation, valuation, multiple-methods]
---

## Modèle d'Évaluation d'Entreprise - Méthodes Multiples

### Méthodologie
Modèle combine 5 méthodes avec pondération sectorielle pour valorisation juste.

---

### Méthode 1 : Discounted Cash Flow (DCF)

**Formule :**
```
Valeur = Σ [CFt / (1+r)^t] + Valeur Terminale / (1+r)^n
```

**Paramètres :**
- **CFt** : Cash Flow libre année t
- **r** : Taux d'actualisation (WACC)
- **n** : Période de projection

**Calculs :**
- WACC = (E/V × Re) + (D/V × Rd × (1-T))
- Re = Rf + β × (Rm - Rf)
- Valeur Terminale = CFn × (1+g) / (r-g)

**Pondération :** 30% pour SaaS, 25% pour services

---

### Méthode 2 : Multiple de Revenus (Revenue Multiple)

**Multiples par Secteur :**
- **SaaS** : 6-8x revenus récurrents
- **Services** : 1-2x revenus annuels
- **E-commerce** : 0.8-1.2x revenus
- **Hardware** : 0.5-1x revenus

**Formule :**
```
Valeur = Revenus × Multiple × Facteurs Correctifs
```

**Facteurs Correctifs :**
- +20% si croissance > 30% YoY
- -15% si churn > 15%
- +10% si marque forte
- -10% si concentration client

**Pondération :** 25% pour tous secteurs

---

### Méthode 3 : Multiple de Bénéfices (EBITDA Multiple)

**Multiples par Taille :**
- **PME** (<€10M CA) : 8-12x EBITDA
- **ETI** (€10-100M CA) : 6-10x EBITDA
- **Grand groupe** (>€100M CA) : 4-8x EBITDA

**Formule :**
```
Valeur = EBITDA × Multiple + Trésorerie - Dettes
```

**Ajustements :**
- Normaliser EBITDA pour non-récurrents
- Ajuster pour secteur spécifique
- Comptabiliser options/warrants

**Pondération :** 20% pour tous secteurs

---

### Méthode 4 : Valeur des Actifs Net (Asset-Based)

**Formule :**
```
Valeur = Actifs Corporatifs - Passifs Corporatifs
```

**Composantes :**
- **Actifs** : Immobilisations, stocks, créances, cash
- **Passifs** : Dettes financières, provisions, engagements

**Ajouts spécifiques :**
- + Valeur des actifs incorporels (breves, clientèle)
- - Dépréciation technologique
- + Valeur terrain si propriété

**Pondération :** 15% pour actifs lourds, 10% pour services

---

### Méthode 5 : Comparable Company Analysis (CCA)

**Sélection des pairs :**
- Même secteur et sous-secteur
- Taille similaire (CA/EBITDA)
- Croissance comparable
- Risque similaire

**Calcul des multiples :**
- EV/Revenue, EV/EBITDA, P/E
- Médiane des pairs ajustés

**Facteurs d'ajustement :**
- Positionnement compétitif
- Gouvernance
- Risques géographiques
- Potentiel de croissance

**Pondération :** 10% pour analyse de pairs

---

### Pondération Sectorielle Optimisée

| Secteur | DCF | Revenue | EBITDA | Assets | CCA | Total |
|---------|-----|---------|--------|-------|-----|-------|
| **SaaS** | 30% | 25% | 20% | 10% | 15% | 100% |
| **Services** | 25% | 25% | 25% | 15% | 10% | 100% |
| **E-commerce** | 20% | 30% | 25% | 15% | 10% | 100% |
| **Manufacturing** | 15% | 20% | 30% | 25% | 10% | 100% |
| **Healthcare** | 35% | 20% | 25% | 10% | 10% | 100% |

---

### Calcul de la Valeur Finale

#### Étapes :
1. Calculer chaque méthode individuellement
2. Appliquer la pondération sectorielle
3. Ajuster pour risque spécifique
4. Appliquer bande de confiance (±10%)

#### Formule finale :
```
Valeur Pondérée = (DCF×pondération) + (Revenue×pondération) + (EBITDA×pondération) + (Assets×pondération) + (CCA×pondération)
```

#### Ajustements de Risque :
- **Risque faible** : -5% à valeur
- **Risque moyen** : ±0%
- **Risque élevé** : +5% à valeur

---

### Indicateurs Clés de Surveillance

#### Taux d'Actualisation par Risque
- **Low risk** : 8-10%
- **Medium risk** : 10-12%
- **High risk** : 12-15%

#### Multiples par Croissance
- **<10%** : Bas multiple
- **10-25%** : Multiple moyen
- **>25%** : Multiple élevé

#### Facteurs Qualitatifs
- **Équipe** : ±5% à la valorisation
- **Technologie** : ±7% à la valorisation
- **Marché** : ±10% à la valorisation

### Related
- [[_system/MOC-patterns]]
- [[brantham/_MOC]]
- [[ma-saa-valuation-framework]]