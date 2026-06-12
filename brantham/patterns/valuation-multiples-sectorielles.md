---
name: valuation-multiples-sectorielles
description: Modèle comparatif de multiples financiers par secteur pour évaluation M&A
metadata:
  type: pattern
  project: brantham
  category: m-a
  created: 2026-06-12
---

# Multiples de Valorisation Sectorielles - M&A

## Méthodologie d'Évaluation

### Multiples Clés par Secteur
| Secteur | Multiple CA | Multiple EBITDA | Multiple RN | Ratio P/E | Dette/EBITDA |
|---------|-------------|-----------------|-------------|----------|-------------|
| Tech/SaaS | 3-5x | 15-25x | 25-40x | 20-40x | 2-4x |
| E-commerce | 1-3x | 8-15x | 15-25x | 15-30x | 1-3x |
| Industrie | 0.8-1.5x | 6-12x | 10-20x | 10-20x | 2-5x |
| Services | 1-2x | 5-10x | 12-18x | 12-25x | 1-3x |
| Santé | 2-4x | 10-20x | 15-30x | 18-35x | 1-4x |
| Énergie | 1-2x | 5-8x | 8-15x | 8-15x | 3-6x |
| Finance | 2-3x | 8-15x | 12-20x | 10-20x | 2-4x |

### Facteurs d'Ajustement Sectoriels

#### 🚀 Facteurs positifs (+10 à +30%)
- [ ] Croissance >20% sur 3 ans
- [ ] Position de leader (>20% part de marché)
- [ ] Technologies propriétaires/patentées
- [ ] Portefeuille clients récurrent (>70%)
- [ ] Marges sectorielles leaders
- [ ] Internationalisation (>30% CA)

#### 📉 Facteurs négatifs (-10 à -40%)
- [ ] Stagnation ou décroissance
- [ ] Forte dépendance client/fournisseur
- [ ] Actifs obsolètes
- [ ] Risques réglementaires élevés
- [ ] Forte endettement
- [ ] Concurrence agressive

---

## Application Pratique

### Étape 1 : Données d'Entrée
- **CA dernier exercice** : [Montant] €
- **EBITDA** : [Montant] €
- **Résultat net** : [Montant] €
- **Croissance 3 ans** : [X]%

### Étape 2 : Sélection des Multiples
- **Secteur** : [Selection]
- **Multiple CA sectoriel** : [X]x
- **Multiple EBITDA sectoriel** : [X]x
- **Ajustements** : [Calculés]

### Étape 3 : Calcul de Fourchettes
| Méthode | Valeur basse | Valeur haute | Valeur médiane |
|---------|--------------|-------------|----------------|
| CA-based | [ ] € | [ ] € | [ ] € |
| EBITDA-based | [ ] € | [ ] € | [ ] € |
| RN-based | [ ] € | [ ] € | [ ] € |

### Étape 4 : Synthèse Évaluation
- **Valeur entreprise** : [ ] € (fourchette [ ] - [ ] €)
- **Valeur equity** : [ ] € (fourchette [ ] - [ ] €)
- **Indicateur de prime/rabais** : [X]%

---

## Benchmarks par Sous-Secteur

### Technologies
- **SaaS** : 4-6x CA, 20-30x EBITDA
- **Hardware** : 0.5-1.5x CA, 8-12x EBITDA
- **Software** : 3-5x CA, 15-25x EBITDA
- **IT Services** : 1-2x CA, 5-10x EBITDA

### Consommation
- **Alimentaire** : 0.8-1.2x CA, 6-10x EBITDA
- **Mode** : 1-1.5x CA, 8-12x EBITDA
- **Électroménager** : 0.6-1x CA, 5-8x EBITDA

### Services
- **Consulting** : 1.5-2.5x CA, 10-18x EBITDA
- **Marketing** : 1-2x CA, 6-12x EBITDA
- **Services aux entreprises** : 1-2x CA, 5-10x EBITDA

---

## Outils d'Analyse

### Calculatrice Rapide
```python
# Valeur entreprise = EBITDA × multiple EBITDA
# Valeur equity = Valeur entreprise - dettes + cash
```

### Facteurs Qualitatifs
- **Gouvernance** : +10% si excellente
- **Croissance** : +15% si >15% CAGR
- **Risques** : -20% si risques élevés
- **Synergies** : +25% si synergies identifiées

---

## Related
[[_system/MOC-patterns]]
[[brantham/_MOC]]
[[ma-strategy]]
[[due-diligence-checklist]]
[[teaser-ma-template]]
[[_system/MOC-ma]]