---
type: pattern
title: M&A Valuation Metrics
domain: finance
project: brantham
created: 2026-06-13
last_updated: 2026-06-13
tags: ["ma", "valuation", "metrics", "finance"]
---

# M&A Valuation Metrics

> Métriques standards pour l'évaluation des cibles M&A chez Brantham. Approches multiples et indicateurs de risque ajustés pour les distressed deals.

## Méthodes d'Évaluation Multiples

### 1. Multiple d'EBITDA (Standard)

#### Multiples par Secteur
| Secteur | Multiple EBITDA | Notes |
|---------|----------------|-------|
| Tech Services | 6-10x | Croissance >15%, récurrent >70% |
| Distribution | 4-7x | Positionnement marché, réseau de vente |
| Industrie | 3-6x | Actifs physiques, cycles longs |
| Digital Services | 8-12x | Marges élevées, faible CAPEX |
| Pharma Services | 7-9x | Barrières réglementaires, contrats longs |

#### Ajustements Distressed
- **Distressed discount**: -30% à -60% du multiple sectoriel
- **Management uncertainty**: -10% si équipe non confirmée
- **Market position**: +15% si leader segment, -20% si suiveur
- **Cash position**: +5% par mois de trésorerie positive

### 2. Multiple de Chiffre d'Affaires

#### Application par Type de Business
- **Revenue multiples**: 0.5-3x du CA annuel
- **SaaS**: 5-10x (ARR annualisé)
- **E-commerce**: 1-2x (avec marge >15%)
- **Manufacturing**: 0.3-0.8x (asset-heavy)
- **Services récurrents**: 2-4x (stabilité contrats)

#### Distressed Application
- **Revenue stabilization**: Mécanisme si CA chute >20%
- **Customer concentration**: -25% si top 3 clients >50% CA
- **Contract quality**: -15% si contrats <12 mois
- **Seasonality adjustment**: Normaliser sur 12 mois

### 3. DCF (Discounted Cash Flow)

#### Paramètres Clés
- **Taux d'actualisation**: 12-18% (risque sectoriel + distressed premium)
- **Période de projection**: 5-10 ans
- **Croissance terminale**: 2-5% (sector average)
- **Valeur terminale**: Perpétuité ou EBITDA multiple exit

#### Stress Tests Distressed
- **Scénario base**: Taux de croissance actuel
- **Scénario pessimiste**: -30% croissance année 1
- **Scénario optimiste**: Stabilisation + croissance organique
- **Liquidation value**: Valeur des actifs nets de dettes

### 4. Valeur des Actifs (Asset Valuation)

#### Approche Distressed Prioritaire
- **Actifs opérationnels**: Valeur marchande ou utilité
- **Immobilier**: Valeur foncière moins coûts de sortie
- **Stocks**: Coût historique moins dépréciation
- **Clients**: Valeur actualisée des contrats récurrents
- **Goodwill**: Zéro ou négatif en distressed

#### Calcul du BFR de Reprise
```
BFR reprise = (Stocks cible + Créances clients cible) - (Dettes fournisseurs cible + Dettes fiscales/sociales cible)
+ Provision BFR opérationnel
- Cash disponible cible
```

## Indicateurs de Risque d'Évaluation

### Risk Adjustments multiples

| Facteur de Risque | Impact sur Multiple | Mécanisme d'Ajustement |
|-------------------|-------------------|----------------------|
| Concentration client >50% | -15% à -30% | Diversification nécessaire |
| Dette nette >3x EBITDA | -20% à -40% | Levier financier insoutenable |
| Perte de PDG/CFO | -10% à -25% | Incertitude opérationnelle |
| Concession concurrentielle | -25% à -50% | Risque de perte marché |
| Dépendance fournisseur unique | -10% à -20% | Risque d'approvisionnement |

### Financial Health Indicators

#### Liquidity Ratios
- **Current Ratio**: <1.5 = Tension
- **Quick Ratio**: <1.0 = Risque immédiat
- **Cash conversion cycle**: >90 jours = Problème BFR
- **Debt service coverage**: <1.2x = Difficulté paiement

#### Profitability Indicators
- **EBITDA margin**: <10% = Tension marginale
- **Net margin**: <5% = Rentabilité faible
- **ROIC**: <8% = Allocation inefficiente du capital
- **Gross margin**: <25% = Pouvoir pricing faible

## Métriques Spécifiques Distressed

### 1. 13-Week Cash Flow Position
- **Cash runway**: <8 semaines = Risque immédiat
- **Peak funding need**: Montant maximum à injecter
- **Break-even date**: Date de retour à équilibre
- **Cash burn rate**: Taux mensuel de consommation

### 2. Turnaround Potential Assessment
| Critère | Poids | Score |
|---------|-------|-------|
| Market position | 20% | Position actuelle vs concurrents |
| Product viability | 25% | Pertinence produit, innovation |
| Management team | 20% | Expérience sectorielle |
| Financial structure | 15% | Dette, rentabilité, BFR |
| Customer base | 20% | Diversification, récurrent |

### 3. Time to Profitability
- **Short-term**: <6 mois (quick wins)
- **Medium-term**: 6-18 mois (restructuration)
- **Long-term**: 18-36 mois (croissance organique)
- **Break-even timeline**: Point mort financier

## Validation Croisée des Évaluations

### Triangulation des Méthodes
1. **Market approach**: Multiples comparables transactions
2. **Income approach**: DCF avec taux ajustés
3. **Asset approach**: Valeur liquidation + goodwill

### Red Lines Évaluation
- **Maximum payback period**: 5 ans
- **Minimum ROI**: 2.5x sur 3 ans
- **Maximum debt ratio**: 4x EBITDA post-acquisition
- **Minimum EBITDA growth**: 10% CAGR

## Dashboard de Tracking

### KPIs Clés par Phase
| Phase | Métrique | Cible | Alerte |
|-------|----------|-------|--------|
| Screening | EV/EBITDA multiple | Sector avg ±20% | ±40% |
| Due Diligence | Cash burn rate | <500k€/mois | >800k€/mois |
| Offer | Payback period | <5 ans | >7 ans |
| Post-Acquisition | ROI track | 2.5x+ à 3 ans | <2x à 2 ans |

## Related

- [[brantham/_MOC]]
- [[ma-strategy]]
- [[brantham/knowledge/concepts/linkedin-distressed-ma-strategy]]
- [[brantham/patterns/distressed-due-diligence-checklist]]