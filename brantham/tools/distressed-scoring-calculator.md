---
name: Distressed Company Scoring System
description: Système de scoring 0-100 pour évaluer les opportunités M&A distressed
category: scoring-system
template: true
date: 2024-12-19
version: 1.0
tags: [m-a, distressed, scoring, evaluation, priorisation]
---

# Scoring System M&A Distressed (0-100)

## 🎯 Objectif

Évaluer rapidement les opportunités d'acquisition de sociétés en difficulté pour prioriser l'allocation des ressources.

## 📊 Structure du Scoring

| Catégorie | Pondération | Score Max | Note |
|-----------|-------------|-----------|------|
| **Viabilité Financière** | 35% | 35 points | |
| **Potentiel Opérationnel** | 25% | 25 points | |
| **Risques Juridiques** | 20% | 20 points | |
| **Market Position** | 15% | 15 points | |
| **Capacité de Transformation** | 5% | 5 points | |
| **TOTAL** | **100%** | **100 points** | |

---

## 🔍 Métriques de Scoring Détaillées

### 1️⃣ Viabilité Financière (35 points)

#### Indicateurs Critiques (Poids total: 35)

| Indicateur | Poids | Score | Calcul | Description |
|------------|-------|-------|--------|-------------|
| **Rentabilité Nette** | 10 pts | /10 | Net CA × 100 | Taux de rentabilité nette |
| **Marge Brute** | 8 pts | /8 | Marge brute CA × 100 | Santé opérationnelle |
| **BFR Jours CA** | 7 pts | /7 | Max(0, 60 - BFR) | BFR optimal < 60j |
| **Endettement** | 6 pts | /6 | Max(0, 100 - Endettement) | Dette < 70% idéal |
| **Trésorerie** | 4 pts | /4 | Min(Trésorerie / 100k, 4) | Trésorie positive nécessaire |

#### Formules de Calcul

```excel
# Rentabilité Nette
Score_Rentabilité = MAX(0, MIN(10, (Bénéfice_net / Chiffre_affaires) × 100))

# BFR Jours
Score_BFR = MAX(0, MIN(7, 60 - BFR_jours))
# Si BFR > 60j → score = 0

# Endettement
Score_Endettement = MAX(0, MIN(6, 100 - (Dettes_total / Capitaux_propres × 100)))
```

### 2️⃣ Potentiel Opérationnel (25 points)

#### Indicateurs de Performance (Poids total: 25)

| Indicateur | Poids | Score | Échelle | Description |
|------------|-------|-------|---------|-------------|
| **Taux d'Utilisation Capacité** | 8 pts | /8 | % | Production optimale > 70% |
| **Quality Index** | 6 pts | /6 | 1-10 | Qualité produit/service |
| **Supply Chain Health** | 5 pts | /5 | 1-5 | Robustesse chaîne logistique |
| **Brand Recognition** | 4 pts | /4 | 1-4 | Notoriété marque |
| **Tech Stack Modernity** | 2 pts | /2 | 1-2 | Systèmes modernes |

### 3️⃣ Risques Juridiques (20 points)

#### Gestion des Risques (Poids total: 20)

| Indicateur | Poids | Score | Calcul | Description |
|------------|-------|-------|--------|-------------|
| **Contentieux Actifs** | 8 pts | /8 | MAX(0, 8 - Nombre) | < 3 contentieux |
| **Conformité Réglementaire** | 6 pts | /6 | Vérification checklist | Complétude conforme |
| **Propriété Intellectuelle** | 4 pts | /4 | Actifs / 10 | Brevets/marques actifs |
| **Contrats Clés** | 2 pts | /2 | Renouvellement possible | Durée contrats |

### 4️⃣ Market Position (15 points)

#### Position Concurrentielle (Poids total: 15)

| Indicateur | Poids | Score | Calcul | Description |
|------------|-------|-------|--------|-------------|
| **Market Share** | 6 pts | /6 | % | Part secteur > 5% |
| **Growth Trajectory** | 5 pts | /5 | Tendance 3 ans | Stabilité ou croissance |
| **Customer Concentration** | 4 pts | /4 | MAX(0, 4 - Top3%) | Diversification clients |

### 5️⃣ Capacité de Transformation (5 points)

#### Potentiel de Value Creation (Poids total: 5)

| Indicateur | Poids | Score | Calcul | Description |
|------------|-------|-------|--------|-------------|
| **Management Quality** | 3 pts | /3 | Évaluation 1-3 | Équipe dirigeante |
| **Digital Maturity** | 2 pts | /2 | Stade digitalisation | Transformation numérique |

---

## 📈 Calcul du Score Final

### Formule Combinée

```excel
Score_Final = 
  (Score_Viabilité_Financière × 0.35) +
  (Score_Potentiel_Opérationnel × 0.25) +
  (Score_Risques_Juridiques × 0.20) +
  (Score_Market_Position × 0.15) +
  (Score_Transformation × 0.05)
```

### Classification des Scores

| Score | Classification | Priorité | Action |
|-------|----------------|----------|--------|
| 85-100 | A++ | Exceptionnelle | Acquisition immédiate |
| 75-84 | A+ | Excellente | Forte priorité |
| 65-74 | A | Bonne | Priorité moyenne |
| 55-64 | B | Acceptable | Conditionnelle |
| 45-54 | C | Marginal | Requiert garanties |
| <45 | D | Risquée | À éviter |

---

## 🚨 Seuils Critiques

### Conditions Non Négociables
- **Score < 30** : Abandonner l'opportunité
- **Trésorerie négative** : Score maximum de 50
- **Procédures collectives** : Maximum 60 jours d'examen
- **Endettement > 100%** : Score maximum de 70

### Zones de Risque Élevé
- **Score 30-45** : Risque très élevé - éviter sans garanties
- **Score 45-55** : Risque élevé - conditions strictes requises
- **Score 55-65** : Risque modéré - diligence approfondie requise

---

## 📋 Exemple d'Application

### Cas Camaieu (Simplifié)

| Catégorie | Score Pondéré | Poids | Contribution |
|-----------|---------------|-------|--------------|
| Viabilité Financière | 22 | 35% | 7.7 |
| Potentiel Opérationnel | 15 | 25% | 3.75 |
| Risques Juridiques | 12 | 20% | 2.4 |
| Market Position | 8 | 15% | 1.2 |
| Capacité Transformation | 3 | 5% | 0.15 |
| **TOTAL** | **60** | **100%** | **15.2** |

**Classification : B** - Priorité conditionnelle

---

## 🔧 Calculateur Interactif

### Template de Calcul Excel

```excel
# Configuration
INDICATEURS = {
    "Rentabilité_Nette": {"poids": 10, "max": 10},
    "Marge_Brute": {"poids": 8, "max": 8},
    # ... autres indicateurs
}

# Calcul des scores
def calculate_score(data):
    total = 0
    details = {}
    
    for indicator, config in INDICATEURS.items():
        value = data[indicator]
        score = min(value, config["max"])
        details[indicator] = score
        total += score * (config["poids"] / 100)
    
    return total, details
```

---

## 🎯 Utilisation Pratique

### Processus d'Évaluation
1. **Collecte des données** (24h)
2. **Calcul des scores par catégorie** (48h)
3. **Validation des seuils critiques** (immediat)
4. **Décision de priorisation** (avec investisseur)

### Dashboards Recommandés
- **Daily Tracker** : Scores en temps réel
- **Weekly Review** : Tendances d'évolution
- **Monthly Analysis** : Performance vs. Prévisions

---

## Related

- [[_system/MOC-scoring]]
- [[brantham/templates/distressed-analysis-template]]
- [[brantham/templates/distressed-due-diligence-checklist]]
- [[brantham/patterns/valuation-template]]