---
name: ma-saa-valuation-framework
description: Framework d'évaluation rapide pour opportunités d'acquisition SaaS
metadata:
  type: pattern
  created: 2026-06-12
  tags: [ma, acquisition, saas, due-diligence]
---

## Framework d'Évaluation d'Acquisition SaaS

### Méthodologie
Évaluez chaque critère sur une échelle de 0 à 10, où :
- 0-3 = Faible/Problématique
- 4-6 = Moyen/À surveiller
- 7-10 = Fort/Excellent

### Critères d'Évaluation

#### 1. Market Fit (0-10)
- **Positionnement clair** : Produit résout un problème spécifique
- **Taille du marché** : TAM > €10M
- **Compétition** : Positionnement différentiable
- **Taux de rétention** > 80%
- **Feedback clients positif**

> *Indicateur clé :* NPS > 40 et Taux d'expansion > 120%

#### 2. Financial Health (0-10)
- **Burn rate** < 6 mois de trésorerie
- **Rune ratio** > 1 (Cash revenue / Run rate)
- **Délai de paiement clients** < 45 jours
- **Marge brute** > 70%
- **Recurring revenue** > 80% du CA

> *Indicateur clé :* Runway > 12 mois avec tendance positive

#### 3. Technical Debt (0-10)
- **Code coverage** > 80%
- **CI/CD pipeline** automatisé
- **Monitoring** observabilité complète
- **Architecture** scalable (SaaS-ready)
- **Tests** unitaires/intégration > 75%

> *Indicateur clé :* Temps de déploiement < 30 min en production

#### 4. Customer Concentration (0-10)
- **Top 10 clients** < 40% du CA
- **Diversification sectorielle** > 3 secteurs
- **Diversification géographique** > 2 régions
- **ACV moyen** > €5K
- **Renouvellements** > 85%

> *Indicateur clé :* Diversification > 50 clients actifs

#### 5. Growth Potential (0-10)
- **Taux de croissance mensuel** > 10% MoM
- **CAC payback period** < 12 mois
- **Taux d'acquisition organique** > 20%
- **Product-market fit** prouvé
- **Internationalisation** potential

> *Indicateur clé :* LTV > 3x CAC

### Score Global
- **45-50** : Acquisition prioritaire
- **35-44** : Étude approfondie nécessaire
- **25-34** : Suivi avec conditions
- **<25** : À écarter

### Matrice de Décision
```
| Score | Priorité | Action                                 |
|-------|----------|----------------------------------------|
| 45+   | Critique | Due diligence immédiate                 |
| 35-44 | Haute    | Due diligence ciblée                   |
| 25-34 | Moyenne  | Surveillance active + négociation flexible |
| <25   | Basse    | Pas de suite                          |
```

## Utilisation Pratique
1. Collecte des données financières et opérationnelles
2. Évaluation par critère (0-10)
3. Calcul du score global
4. Décision en fonction de la matrice
5. Validation par due diligence ciblée

### Related
- [[_system/MOC-patterns]]
- [[brantham/_MOC]]
- [[ma-due-diligence-checklist]]
## Related

- [[_system/MOC-patterns]]
- [[brantham/_MOC]]