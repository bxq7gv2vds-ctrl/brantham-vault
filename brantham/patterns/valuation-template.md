---
type: pattern
title: Valuation Template Pattern
domain: finance
project: brantham
created: 2026-06-13
last_updated: 2026-06-13
tags: ["ma", "valuation", "template", "due-diligence"]
---

# Valuation Template Pattern

> Pattern standard pour l'évaluation des cibles M&A chez Brantham. Méthodologie complète avec multiples approches et mécanismes d'ajustement pour les distressed deals.

## Contexte d'Application

Ce pattern s'applique lorsque :
- On identifie une opportunité d'acquisition potentielle
- On doit établir une offre juste et compétitive
- On analyse une entreprise en difficulté (distressed)
- On valide la viabilité financière du deal

## Processus d'Évaluation Standard

### Phase 1: Screening Rapide (J-1 à J+3)

#### Initial Assessment
1. **Quick multiple screening**:
   - EV/EBITDA vs secteur
   - EV/Revenue vs historique
   - Comparables transactions récentes

2. **Red flags identification**:
   - BFR > 90 jours CA
   - Dette nette > 3x EBITDA
   - Marge brute < 20%
   - Concentration client > 50%

3. **Go/no-go decision**:
   - Multiple < 50% du secteur = abandon
   - Trop de red flags = DD approfondie requise
   - Potentiel intéressant = validation comité

### Phase 2: Due Diligence Évaluative (J+4 à J+14)

#### Financial Deep Dive
1. **Analyse historique** (3-5 ans):
   - Croissance organique et organique
   - Marge trend (brute, opérationnelle, nette)
   - Investissements CAPEX vs maintenance
   - Variation BFR et causes

2. **Cash flow modeling**:
   - 13-week cash flow forecast
   - DCF à 5 ans avec stress tests
   - Sensibilité aux hypothèses clés
   - Break-even analysis

3. **Asset valuation**:
   - Valeur comptable vs marché
   - Actifs obsolètes à déprécier
   - Propriété intellectuelle
   - Immobilier et équipements

#### Market & Competitive Analysis
1. **Positionnement marché**:
   - Part de marché et trend
   - Barrières à l'entrée
   - Pouvoir de négociation clients/fournisseurs

2. **Competitive landscape**:
   - Benchmarking vs concurrents
   - Avantages concurrentiels durables
   - Risque de substitution

#### Operational Assessment
1. **Team evaluation**:
   - Expérience sectorielle
   - Stabilité de l'équipe clé
   - Capacité de changement

2. **Processes & systems**:
   - Efficacité opérationnelle
   - Digital maturity
   - Scalabilité du modèle

### Phase 3: Structuration de l'Offre (J+15 à J+21)

#### Multiple Approach Construction
1. **Base multiple determination**:
   - Sector average EV/EBITDA
   - Company-specific premiums/discounts
   - Market timing adjustments

2. **Distressed adjustments**:
   - Risk premium: +2-4% taux d'actualisation
   - Liquidity discount: -30% à -60% multiple
   - Uncertainty discount: -10% à -25%

3. **Comparable transactions**:
   - Deals similaires sur 24 derniers mois
   - Geographic and sector adjustments
   - Size premium/large deal discount

#### Offer Price Calculation
```
Prix de base = EBITDA × Multiple sectoriel
Ajustements = Risk premium + Liquidity discount + Uncertainty discount
Earn-out = Montant basé sur objectifs 12-36 mois
Prix total = Prix de base + Ajustements + Earn-out maximum
```

#### Valuation Range Definition
- **Floor price**: Valeur liquidation nette
- **Target price**: Évaluation basée sur multiples et DCF
- **Ceiling price**: Maximum acceptable avec earn-out
- **Walk-away price**: En dessous de laquelle on abandonne

### Phase 4: Validation Finale (J+22 à J+30)

#### Cross-Validation Méthodes
1. **Market approach**:
   - Multiples EV/EBITDA comparables
   - EV/Revenue vs transactions similaires
   - Premiums pour taille/specialisation

2. **Income approach**:
   - DCF avec taux ajustés au risque
   - Terminal value multiples
   - Sensibilité aux key assumptions

3. **Asset approach**:
   - Valeur marchande des actifs
   - BFR de reprise
   - Goodwill (souvent négatif en distressed)

#### Risk-Adjusted Valuation
| Risque | Probabilité | Impact | Ajustement Prix |
|--------|-------------|--------|----------------|
| Perte client clé | 30% | Élevé | -15% |
| Changement réglementaire | 20% | Moyen | -10% |
| Dépendance fournisseur | 40% | Moyen | -12% |
| Incertitude management | 35% | Élevé | -18% |

#### Final Approval Process
1. ** Comité investissement review**:
   - Présentation des 3 méthodes d'évaluation
   - Analyse des risques et ajustements
   - Vote go/no-go sur l'offre

2. **Board approval**:
   - Synthèse deal rationale
   - Risques identifiés
   - Ressources requises

## Template d'Évaluation Rapide

### Quick Valuation Checklist
- [ ] EV/EBITDA multiple calculé
- [ ] Ajustements sectoriaux appliqués
- [ ] Red flags identifiés
- [ ] BFR de reprise estimé
- [ ] DCF baseline établi
- [ ] Comparables transactions analysés
- [ ] Risk premium intégré
- [ ] Offer price validated par comité

### Distressed Deal Specifics
- [ ] 13-week cash flow forecast vérifié
- [ ] Valeur liquidation calculée
- [ ] Management stability évaluée
- [ ] Market position vs concurrents
- [ ] Customer concentration analyzed
- [ ] Debt structure stress tested
- [ ] Turnaround timeline defined

## Outils & Calculs

### Formules Clés
```
EV = Enterprise Value = Equity Value + Net Debt
Multiple = EV / EBITDA
BFR = (Stocks + Créances clients) - (Dettes fourniseurs + Dettes fiscales/sociales)
DCF = Σ [Cash Flow / (1 + r)^t] + Terminal Value / (1 + r)^n
```

### Benchmarking Tables
| Taux d'actualisation | Risque | Distressed Premium |
|---------------------|--------|-------------------|
| 10-12% | Low | +0-2% |
| 12-15% | Medium | +2-4% |
| 15-18% | High | +4-6% |
| 18-20% | Very High | +6-8% |

## Risques Communs & Mitigation

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| Surévaluation | Médium | Élevé | Validation croisée méthodes |
| Synergies non réalisées | Faible | Élevé | Clause earn-out stricte |
| Perte équipe clé | Médium | Médium | Garanties d'emploi |
| Changement marché | Faible | Élevé | Revue trimestrielle post-closing |

## Exemple Réel Brantham

### Tech Services Acquisition (2025)
- **Situation**: EBITDA €500k, secteur multiple 8x
- **Base evaluation**: €4M (8x €500k)
- **Distressed adjustments**: -30% = €2.8M
- **BFR de reprise**: €800k
- **Final offer**: €3.6M (base + earn-out potential)
- **Résultat**: Acquis à €3.2M avec earn-out €400k

## Related

- [[ma-valuation-metrics]]
- [[ma-strategy]]
- [[brantham/patterns/distressed-due-diligence-checklist]]
- [[brantham/templates/term-sheet-acquisition]]