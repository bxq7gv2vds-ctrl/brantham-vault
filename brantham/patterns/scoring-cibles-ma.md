---
name: scoring-cibles-ma
description: Framework d'évaluation et scoring pour prioriser les cibles M&A
metadata:
  type: pattern
  project: brantham
  category: m-a
  created: 2026-06-12
---

# Framework de Scoring Cibles M&A

## Méthodologie d'Évaluation

### Score Global (0-100)
Le score combine 6 critères principaux avec pondération différenciée.

| Critère | Pondération | Score Max | Notes |
|---------|-------------|-----------|-------|
| Stratégique | 30% | 30 | Alignement avec stratégie |
| Financière | 25% | 25 | Rentabilité et croissance |
| Opérationnelle | 20% | 20 | Synergies et intégration |
| Risques | 15% | 15 | Risques identifiés |
| RH & Culture | 10% | 10 | Intégrabilité culturelle |
| Timing | 5% | 5 | Urgence et disponibilité |

---

## Grille de Scoring Détaillée

### 🔵 Stratégique (30 pts)
| Item | Points | Score | Justification |
|------|--------|-------|---------------|
| Alignement stratégique | 10 | [ ] | Correspondance avec stratégie acquéreur |
| Synergies claires | 10 | [ ] | Réduction coûts, accroissement CA |
| Avantage concurrentiel | 5 | [ ] | Positionnement unique, barrières entrée |
| Potentiel croissance | 5 | [ ] | Marchés émergents, diversification |

### 💰 Financière (25 pts)
| Item | Points | Score | Justification |
|------|--------|-------|---------------|
| EBITDA > 2M€ | 10 | [ ] | Rentabilité suffisante |
| Croissance CA >10% | 8 | [ ] | Dynamisme commercial |
| Dette raisonnable | 5 | [ ] | Dette/EBITDA < 3x |
| Cash flow positif | 2 | [ ] | Autofinancement possible |

### 🏭 Opérationnelle (20 pts)
| Item | Points | Score | Justification |
|------|--------|-------|---------------|
| Scalabilité | 5 | [ ] | Processus reproductibles |
| Infrastructure | 5 | [ ] | Systèmes modernes, compatibles |
| Supply chain robuste | 5 | [ ] | Fournisseurs diversifiés |
| Réseau de distribution | 5 | [ ] | Canaux efficaces et étendus |

### 🚨 Risques (15 pts)
| Item | Points | Score | Justification |
|------|--------|-------|---------------|
| Risques réglementaires | 5 | [ ] | Conformité, législation |
| Risques clients | 4 | [ ] | Concentration <30% CA |
| Risques financiers | 3 | [ ] | Litiges, passifs cachés |
| Risques technologiques | 3 | [ ] | Obsolescence, sécurité |

### 👥 RH & Culture (10 pts)
| Item | Points | Score | Justification |
|------|--------|-------|---------------|
| Key people retenus | 4 | [ ] | Talents clés identifiables |
| Culture compatible | 3 | [ ] | Valeurs alignées |
| Turnover maîtrisé | 3 | [ ] | Taux <15% |
| Plan succession | 0 | [ ] | Structures en place |

### ⏱️ Timing (5 pts)
| Item | Points | Score | Justification |
|------|--------|-------|---------------|
| Disponibilité immédiate | 3 | [ ] | Vendeur réactif |
| Processus concurrentiel | 2 | [ ] | Timing court (3-6 mois) |

---

## Classification des Cibles

### A++ (80-100 pts) - Priorité Absolue
- **Action** : Déploiement immédiat des ressources
- **Exemple** : Alignement parfait, synergies majeures, risques faibles
- **Timing** : 30 jours maximum pour LOI

### A+ (70-79 pts) - Priorité Haute
- **Action** : Préparation due diligence intensive
- **Exemple** : Bon alignement stratégique, synergie significative
- **Timing** : 45-60 jours

### A (60-69 pts) - Opportunité Intéressante
- **Action** : Suivi actif, analyse complémentaire
- **Exemple** : Potentiel intéressant mais risques ou synergies limités
- **Timing** : 60-90 jours

### B (50-59 pts) - À suivre
- **Action** : Surveillance passive des évolutions
- **Exemple** : Potentiel limité ou risques importants
- **Timing** : Réévaluer dans 6 mois

### C (<50 pts) - À déclasser
- **Action** : Archiver ou écarter
- **Raison** : Manque d'alignement ou risques prohibiteurs

---

## Calculatrice de Scoring

### Étape 1 : Saisie des données
- **Nom cible** : [ ]
- **CA** : [ ] M€
- **EBITDA** : [ ] M€
- **Croissance CA** : [ ] %
- **Dette/EBITDA** : [ ] x
- **Effectif** : [ ] personnes

### Étape 2 : Attribution des scores
| Catégorie | Score |
|-----------|-------|
| Stratégique | [ ]/30 |
| Financière | [ ]/25 |
| Opérationnelle | [ ]/20 |
| Risques | [ ]/15 |
| RH & Culture | [ ]/10 |
| Timing | [ ]/5 |
| **TOTAL** | **[ ]/100** |

### Étape 3 : Classification
- **Classe** : [A++/A+/A/B/C]
- **Recommandation** : [Actions spécifiques]

---

## Checklist Critères Exclusifs

### ❌ Exclusion immédiate (<20 pts total)
- [ ] Dette > 5x EBITDA
- [ ] Croissance négative sur 2 ans
- [ ] Dépendance client > 50% CA
- [ ] Risques légaux > 100k€
- [ ] Pas de synergies identifiables

### ✅ Validation rapide (>40 pts minimum)
- [ ] Alignement stratégique confirmé
- [ ] Potentiel de création de valeur >15%
- [ ] Risques maîtrisables
- [ ] Plan d'intégration réaliste

---

## Related
[[_system/MOC-patterns]]
[[brantham/_MOC]]
[[ma-strategy]]
[[valuation-multiples-sectorielles]]
[[teaser-ma-template]]
[[_system/MOC-ma]]