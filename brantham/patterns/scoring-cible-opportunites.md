---
name: scoring-cible-opportunites
description: Scoring quantitatif pour prioriser les opportunités M&A distressed adapté au workflow Brantham Partners
metadata:
  type: pattern
  project: brantham
  category: m&a-distressed
  version: 1.0
  created: 2026-06-12
  updated: 2026-06-12
  related:
    - scoring-ma-template
    - distressed-expert
    - ma-checklist-due-diligence
  tags:
    - scoring
    - evaluation
    - priorisation
    - distressed
    - kpi
---

# Scoring Cible Opportunités Distressed

## Framework Scoring Combiné (0-100)

### Méthodologie
- **Pondération dynamique** selon type de procédure (LJ vs RJ)
- **Scores normalisés** par secteur d'activité
- **Facteurs temporels** intégrés (urgence procédurale)
- **Backtesting** sur deals historiques

---

## Grille de Scoring Priorisation

### 1. Potentiel de Rebond - 25 pts
| Indicateur | Scoring | Méthode |
|------------|---------|---------|
| **Viabilité commerciale** (10 pts) | /10 | Étude marché + concurrence |
| **Atouts défensifs** (8 pts) | /8 | Barrières entrée, PI, contrats exclusifs |
| **Potentiel croissance** (7 pts) | /7 | Leviers identifiables ( marché, produit, géo) |

**Calcul :**
- EBITDA pré-crice > 5% CA → +3 pts
- Portefeuille client non concentré (>20 clients) → +2 pts  
- Positionnement sectoriel en croissance → +2 pts

### 2. Opportunité Temporelle - 20 pts
| Indicateur | Scoring | Méthode |
|------------|---------|---------|
| **Urgence procédurale** (10 pts) | /10 | LJ: -30j=10pts, -60j=7pts, -90j=4pts |
| **Phase procédure** (5 pts) | /5 | LJ:10, RJ:8, SV:3 |
| **Timing marché** (5 pts) | /5 | Demandes sectorielle actuelle |

**Facteurs temporels critiques :**
- Moins de 45 jours pour LJ → score maximal
- RJ avec plan de cession → +3 pts
- Tendance sectorielle favorable → +2 pts

### 3. Complexité Opérationnelle - 20 pts
| Indicateur | Scoring | Méthode |
|------------|---------|---------|
| **Risques sociaux** (8 pts) | /8 | Licenciements, contentieux, TR |
| **Dépendance employés** (6 pts) | /6 | Key man risk > 3 → -3 pts |
| **Complexité juridique** (6 pts) | /6 | Recours en cours, procédures multiples |

**Calcul risques :**
- Plus de 5 contentieux en cours → -4 pts
- Team clé pour 80% CA → -3 pts
- Recours cassation → -2 pts

### 4. Potentiel Arbitrage - 20 pts
| Indicateur | Scoring | Méthode |
|------------|---------|---------|
| **Spread valeur** (10 pts) | /10 | VE réelle vs VE théorique |
| **Dettes structurelles** (5 pts) | /5 | Ratio dettes/CA < 1 → +3 pts |
| **Actifs sous-valorisés** (5 pts) | /5 | Immobilier non comptabilisé |

**Calcul arbitrage :**
- VE liquidative < 50% VE going concern → +5 pts
- Actifs non stratégiques → +3 pts
- Dettes fiscales/sociales → -2 pts

### 5. Fit Stratégique - 15 pts
| Indicateur | Scoring | Méthode |
|------------|---------|---------|
| **Synergie opérationnelle** (8 pts) | /8 | Complémentarité portefeuille existant |
| **Accès marché** (4 pts) | /4 | Nouveaux clients/segments |
| **Technologie** (3 pts) | /3 IP réutilisable |

**Fit scoring :**
- Secteur couvert par Brantham AI → +5 pts
- Technologies transferables → +3 pts
- Géo expansion → +2 pts

---

## Score Total & Classification

| Catégorie | Score (0-25) | Poids | Score Pondéré |
|-----------|--------------|-------|---------------|
| Potentiel Rebond | | 25% | |
| Opportunité Temporelle | | 20% | |
| Complexité Opérationnelle | | 20% | |
| Potentiel Arbitrage | | 20% | |
| Fit Stratégique | | 15% | |
| **Score Total** | | **100%** | |

### Classification Automatique

| Score | Priorité | Action |
|-------|----------|--------|
| **85-100** | **CRITIQUE** | Pipeline IMMÉDIAT - Assigner senior |
| **70-84** | **URGENT** | Pipeline 48h - Review quotidien |
| **55-69** | **Haut Potentiel** | Pipeline standard - Bi-hebdo review |
| **40-54** | **Surveillance** | Watch list - Mensuel review |
| **<40** | **Archive** | No follow - Retour BODACC |

---

## Métriques Clés par Type de Procédure

### Liquidation Judiciaire (LJ)
- **Sweet spot score** : 70-85
- **Facteurs dominants** : Urgence, simplicité opérationnelle, arbitrage valeur
- **Délai optimal** : 21-45 jours
- **Risque maximum** : 12 mois

### Redressement Judiciaire (RJ)
- **Sweet spot score** : 75-90  
- **Facteurs dominants** : Viabilité business plan, fit stratégique
- **Délai optimal** : 45-90 jours
- **Risque maximum** : 24 mois

### Sauvegarde (SV)
- **Sweet spot score** : 60-80
- **Facteurs dominants** : Stabilité management, solutions alternatives
- **Délai optimal** : 30-60 jours
- **Risque maximum** : 6 mois

---

## Indicateurs de Performance Tracking

### Metrics Par Deal
- **Time to First Offer** (J)
- **Conversion Rate** (%)
- **Multiple Realisé** (x)
- **Profitabilité** (%)

### Portfolio Metrics
- **Score moyen pipeline** : cible > 65
- **Ratio Urgent/Go** : idéal 30/70
- **Taux conversion** : cible > 25%
- **Multiple median** : benchmark sectoriel

---

## Alertes & Notifications

### Déclenchement Automatique
- **Score < 40** → Archivage automatique
- **Score > 85** → Alerte senior management
- **Urgence < 30j** → Notification immédiate
- **Risque social élevé** → Review spécialisé

### Re-evaluation Mensuelle
- **Deals scoring 55-69** : Re-evaluation mensuelle
- **Changement secteur** : Recalcul pondération
- **Nouveaux patterns** : Mise à jour scoring

---

## Calculateur Automatique

### Template d'Utilisation
```markdown
### [Nom Entreprise] - Scoring Initial

**Informations clés :**
- SIREN : [X]
- CA : [X] M€
- Effectif : [X]
- Procédure : [LJ/RJ/SV]
- Urgence : [X] jours

**Scores bruts :**
- Potentiel Rebond : [X]/25
- Opportunité Temp : [X]/20  
- Complexité : [X]/20
- Arbitrage : [X]/20
- Fit Stratégique : [X]/15

**Score total : [X]/100**
**Classification : [URGENT/GO/WATCH]**
```

### Validation Croisée
- **Minimum 3 sources** de validation
- **Backtest** sur deals similaires
- **Peer review** par lead analyst
- **Second opinion** pour scores > 75

---

## Documentation & Learning

### Historique Scoring
| Date | Analyste | Score Final | Outcome | Lessons |
|------|----------|-------------|---------|---------|
| | | | | |

### Pattern Recognition
- **Indicateurs prédictifs** : Identifier les variables corrélées avec succès
- **False positives** : Documenter les faux positifs
- **Optimisation continue** : Ajuster pondérations trimestriellement

---

## Related
- [[scoring-ma-template]]
- [[distressed-expert]]
- [[ma-checklist-due-diligence]]
- [[brantham/_MOC]]
- [[_system/MOC-patterns]]