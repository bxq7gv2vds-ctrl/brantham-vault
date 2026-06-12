---
title: "Template Scoring M&A Cibles Distressed"
date: 2026-06-12
version: "2.0"
category: templates
type: scoring-template
tags: [ma, scoring, qualification, distressed]
---

# Template de Scoring M&A pour Cibles Distressed

## Instructions d'usage

Copier ce template pour chaque nouvelle opportunité d'acquisition. Compléter les sections avec les données disponibles. Le score final automatique est généré par le système sur 100 points.

---

## Informations Cible

| Champ | Valeur | Source | Date verification |
|-------|--------|--------|------------------|
| SIREN | | | |
| Raison sociale | | | |
| Code NAF | | | |
| Secteur | | | |
| Siège | | | |
| Tribunal | | | |
| Date jugement | | | |

---

## Scoring Détaillé (sur 100 pts)

### 1. Taille - 30%
| Sous-critère | Score | Poids | Pondéré | Notes |
|--------------|-------|-------|---------|-------|
| Chiffre d'affaires (CA) | /100 | 15% | | |
| Effectif salariés | /100 | 10% | | |
| Total bilan | /100 | 5% | | |
| **Sous-total Taille** | | **30%** | | |

Sweet spot : CA 1-50M€, effectif 10-200 salariés

### 2. Secteur - 25%
| Sous-critère | Score | Notes |
|--------------|-------|-------|
| Attractivité sectorielle (NAF) | /100 | Industrie/Agro/Tech > Services génériques |
| Croissance marché | /100 | Tendances sectorielles |
| Réglementation | /100 | Barrières à l'entrée |
| **Sous-total Secteur** | | **25%** |

### 3. Procédure - 20%
| Critère | Score | Justification |
|---------|-------|---------------|
| Type procédure | /100 | LJ:100, RJ:80, SV:60 |
| Stade avancement | /100 | Ouverture:100, Observation:80, Plan:60 |
| Urgence | /100 | <30j:100, <90j:80, >180j:40 |
| **Sous-total Procédure** | | **20%** |

### 4. Actifs Stratégiques - 15%
| Type d'actif | Présence | Valeur | Score |
|--------------|---------|--------|-------|
| Immobilier | | | /100 |
| Machines/équipements | | | /100 |
| Stocks | | | /100 |
| PI (brevets, marques) | | | /100 |
| Clientèle/fonds de commerce | | | /100 |
| **Sous-total Actifs** | | | **15%** |

### 5. Marché Acheteurs - 10%
| Critère | Score | Notes |
|---------|-------|-------|
| Profondeur marché | /100 | Nombre d'acheteurs identifiés |
| Convergence stratégique | /100 | Synergie avec profile idéal |
| Compétition | /100 | Nombre d'autres repreneurs potentiels |
| **Sous-total Acheteurs** | | **10%** |

### 6. Facteurs Qualitatifs - 10%
| Critère | Score | Notes |
|---------|-------|-------|
| Équipe technique | /100 | Compétences clés présentes |
| Réputation marque | /100 | Notoriété et positionnement |
| Relations fournisseurs | /100 | Chaîne d'approvisionnement stable |
| Potentiel croissance | /100 | Leviers de développement |
| **Sous-total Qualitatif** | | **10%** |

---

## Score Total & Décision

| Composante | Score | Poids | Pondéré |
|------------|-------|-------|---------|
| Taille | | 30% | |
| Secteur | | 25% | |
| Procédure | | 20% | |
| Actifs | | 15% | |
| Acheteurs | | 10% | |
| **Score TOTAL** | | **100%** | |

### Seuils de décision :

- **75+** : **URGENT** → Lancement pipeline complet prioritaire
- **60-74** : **GO** → Lancement pipeline standard  
- **50-59** : **WATCH** → Surveillance, réévaluation mensuelle
- **<50** : **ARCHIVE** → Archivage, aucun suivi

---

## Estimation Valeur d'Entreprise

| Méthode | VE Min (€) | VE Médiane (€) | VE Max (€) | Méthode |
|---------|------------|---------------|------------|---------|
| Liquidative | | | | Actifs nets - dettes |
| Comparables | | | | Multiples sectoriels |
| Going concern | | | | DCF simplifié |
| **Recommandation** | | | | |

---

## Predictions Cession (Modèle Cox)

| Période | Probabilité cession | C-index |
|---------|-------------------|---------|
| 3 mois | % | |
| 6 mois | % | 0.84 |
| 9 mois | % | |
| 12 mois | % | |

---

## Actions Recommandées

### Court terme (J-7)
- [ ] Valider intérêt avec acheteurs cibles
- [ ] Demander accès data room
- [ ] Évaluer fit stratégique
- [ ] Préparer due diligence rapide

### Moyen terme (J-30)
- [ ] Préparer offre de reprise
- [ ] Négocier termes avec mandataire
- [ ] Valider financement
- [ ] Plan d'intégration

### Risques identifiés
- [ ] 
- [ ] 
- [ ] 

---

## Backtracking - Historique Similaire

| SIREN similaire | Score final | Outcome | Delai cession |
|-----------------|-------------|---------|---------------|
| | | | |
| | | | |
| | | | |

---

## Notes & Décision

[Documenter les éléments non quantifiables, hypothèses, et décision finale]

---

## Related
- [[brantham/patterns/scoring-patterns]]
- [[brantham/data-pipeline/scoring]]
- [[brantham/deals/template]]
- [[_system/MOC-patterns]]
- [[brantham/_MOC]]