---
type: pattern
title: M&A Strategy Pattern
domain: strategy
project: brantham
created: 2026-06-13
last_updated: 2026-06-13
tags: ["ma", "strategy", "deal-flow", "distressed"]
---

# M&A Strategy Pattern

> Pattern standard pour structurer les opérations M&A chez Brantham Partners. Couvre l'identification, l'évaluation, la négociation et l'intégration.

## Contexte d'Application

Ce pattern s'applique lorsque :
- On identifie une opportunité d'acquisition cible
- On doit structurer une due diligence complète
- On prépare une offre de reprise
- On planifie l'intégration post-acquisition

## Pattern de Déroulement

### Phase 1: Identification & Qualification (J-30 à J-0)

#### Critères de Cible
- **Taille**: PME/ETI 5-50M€ de CA
- **Secteurs**: Industrial, Tech Services, Distribution
- **Situation**: Distressed ou transformation stratégique
- **Synergies**: Complémentarité évidente avec Brantham

#### Processus d'Identification
1. **Source des leads**:
   - LinkedIn prospecting automatisé
   - Réseau investisseurs & avocats
   - Cabinets M&A spécialisés

2. **Scoring initial**:
   - Potentiel de redressement: 1-5
   - Risque juridique: 1-5  
   - Synergies opérationnelles: 1-5
   - Fit avec portfolio actuel: 1-5

3. **Validation comité**:
   - Présentation 1-page
   - Vote go/no-go
   - Allocation resources

### Phase 2: Due Diligence Complète (J-1 à J+30)

#### DD Financial (Prioritaire)
- Analyse BFR et trésorerie
- Validation comptabilité
- Cash flow forecasting 13 semaines
- Analyse dettes & provisions

#### DD Legal
- Procédures collectives
- Contentieux en cours
- Contrats clients/fournisseurs
- Compliance réglementaire

#### DD Commercial
- Positionnement marché
- Portefeuille clients
- Contrats clés
- Risques sectoriels

#### DD Opérationnelle
- Supply chain
- Équipe dirigeante
- Systèmes IT
- Immobilié & équipements

### Phase 3: Structuration de l'Offre (J+31 à J+45)

#### Évaluation
- **Multiple approach**: EV/EBITDA, EV/Revenue, comparables transactions
- **DCF ajusté**: Pour les distressed deals
- **Asset valuation**: Valeur réelle des actifs

#### Term Sheet
- **Prix de cession**: Base + earn-out potentiel
- **Earn-out**: Objectifs mesurables, période 1-3 ans
- **Representations & warranties**: Portée et durée
- **Conditions suspensives**: DD complète, financement, approbations

#### Financement
- Apport propre: 30-40%
- Dette bancaire: 40-50%
- Fonds investisseurs: 10-20%

### Phase 4: Négociation & Closing (J+46 à J+90)

#### Négociation
- **Red lines**: Non-négociables (prix min, contrôle, emploi)
- **Concessions**: Éarn-out, prix décalé, garantis
- **Legal due diligence**: Avant signature définitive

#### Closing
- **Sp legal**: Création de la structure d'acquisition
- **Transfert actifs**: Actifs et contrats clés
- **Financement**: Déblocement des fonds
- **Communication**: Annonce aux parties prenantes

### Phase 5: Post-Acquisition Integration (J+91 à J+180)

#### 100-Day Plan
- **Quick wins**: Actions à fort impact immédiat
- **Integration système**: Convergence IT & reporting
- **Team alignment**: Structure organisationnelle
- **Stabilisation**: Cash flow opérationnel

#### Métriques de Succès
- **ROI deal**: >2.5x sur 3 ans
- **Synergies réalisées**: 100% prévues à J+12
- **Taux de rétention équipe**: >80%
- **Cash flow positif**: J+90

## Checklists Clés

### Pre-Deal Checklist
- [ ] Validation scoring cible
- [ ] DD initial complété
- [ ] Approbation comité investissement
- [ ] Budget DD alloué

### Post-Deal Checklist  
- [ ] NDA signé
- [ ] Exclusivité négociation
- [ ] Financement secured
- [ ] Integration plan validé

## Risques Communs & Mitigation

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| Surévaluation | Médium | Élevé | Divers méthodes d'évaluation |
| Synergies non réalisées | Faible | Élevé | Clause earn-out stricte |
| Perte équipe clé | Médium | Médium | Garanties d'emploi |
| Réglementation | Faible | Élevé | Compliance check précoce |

## Template Associés

- [[brantham/m&a/due-diligence-financiere-template]]
- [[brantham/templates/term-sheet-acquisition]]
- [[brantham/templates/distressed-due-diligence-checklist]]
- [[brantham/deals/active]]

## Exemple Réel Brantham

### Acquisition Tech Services Pro (2025)
- **Situation**: Entreprise en difficulté technique, mais portefeuille clients solide
- **Stratégie**: Acquisition pour les clients, non pour la tech existante
- **Intégration**: Fusion avec Brantham tech division
- **Résultat**: ROI 3.2x en 18 mois, 100% synergies réalisées

## Related

- [[brantham/_MOC]]
- [[brantham/deals]]
- [[patterns/due-diligence-checklist]]
- [[ma-valuation-metrics]]
- [[linkedin-distressed-ma-strategy]]