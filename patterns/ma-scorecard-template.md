---
name: ma-scorecard-template
description: Template de scorecard de due diligence M&A avec métriques standardisées
type: pattern
metadata:
  category: m&a
  priority: high
  tags: [m&a, due diligence, scorecard, evaluation]
---

# Template de Scorecard de Due Diligence M&A

## 🎯 Structure de la Scorecard de Due Diligence

### **Évaluation Globale (Score Final 0-100)**
```markdown
**Scorecard Principale**: 0-100 points
- **Score de Finance**: 0-30 points
- **Score de Juridique**: 0-25 points  
- **Score de Technologie**: 0-20 points
- **Score d'Équipe**: 0-15 points
- **Score de Marché**: 0-10 points

**Classification Globale**:
- 🟢 **Green Light**: 80-100 points (Recommandé fortement)
- 🟡 **Yellow Light**: 60-79 points (Recommandé avec conditions)
- 🔴 **Red Light**: <60 points (Non recommandé ou risques majeurs)
```

## 💰 Évaluation Financière (30 points maximum)

### **Health Financière (10 points)**
```markdown
**1. Rentabilité (3 points)**
- [ ] EBITDA Margin >20%: 3 points
- [ ] EBITDA Margin 15-20%: 2 points
- [ ] EBITDA Margin 10-15%: 1 point
- [ ] EBITDA Margin <10%: 0 points

**2. Growth Rate (4 points)** 
- [ ] Revenue growth >25% YoY: 4 points
- [ ] Revenue growth 15-25% YoY: 3 points
- [ ] Revenue growth 5-15% YoY: 2 points
- [ ] Revenue growth <5% YoY: 0 points

**3. Cash Flow (3 points)**
- [ ] Positive operating cash flow: 3 points
- [ ] Neutral cash flow: 1 point
- [ ] Negative cash flow: 0 points
```

### **Structure Financière (10 points)**
```markdown
**4. Dette/EBITDA Ratio (4 points)**
- [ ] <2x: 4 points
- [ ] 2-3x: 3 points
- [ ] 3-4x: 2 points
- [ ] >4x: 0 points

**5. Revenues Récurrents (3 points)**
- [ ] >80% revenue récurrent: 3 points
- [ ] 60-80% revenue récurrent: 2 points
- [ ] 40-60% revenue récurrent: 1 point
- [ ] <40% revenue récurrent: 0 points

**6. Capital de Rotation (3 points)**
- [ ] BFR positif et contrôlé: 3 points
- [ ] BFR neutre: 2 points
- [ ] BFR négatif: 1 point
- [ ] BFR incontrôlé: 0 points
```

### **Santé Balance (10 points)**
```markdown
**7. Liquidité (4 points)**
- [ ] Current ratio >2.0: 4 points
- [ ] Current ratio 1.5-2.0: 3 points
- [ ] Current ratio 1.0-1.5: 2 points
- [ ] Current ratio <1.0: 0 points

**8. Capitaux Propres (3 points)**
- [ ] Equity/Assets >50%: 3 points
- [ ] Equity/Assets 30-50%: 2 points
- [ ] Equity/Assets 20-30%: 1 point
- [ ] Equity/Assets <20%: 0 points

**9. Couverture Intérêts (3 points)**
- [ ] Interest coverage >5x: 3 points
- [ ] Interest coverage 3-5x: 2 points
- [ ] Interest coverage 1-3x: 1 point
- [ ] Interest coverage <1x: 0 points
```

## ⚖️ Évaluation Juridique (25 points maximum)

### **Litiges et Risques (10 points)**
```markdown
**10. Litiges Actifs (4 points)**
- [ ] 0 litiges significatifs: 4 points
- [ ] 1-2 litiges mineurs: 3 points
- [ ] 3-5 litiges modérés: 1 point
- [ ] >5 litiges majeurs: 0 points

**11. Conformité Réglementaire (3 points)**
- [ ] 0 violations: 3 points
- [ ] 1-2 violations mineures: 2 points
- [ ] 3-5 violations: 1 point
- [ ] >5 violations: 0 points

**12. Litiges Clients (3 points)**
- [ ] <5% revenus en litiges: 3 points
- [ ] 5-10% revenus en litiges: 2 points
- [ ] 10-15% revenus en litiges: 1 point
- [ ] >15% revenus en litiges: 0 points
```

### **Contrats et Obligations (10 points)**
```markdown
**13. Contrats Clients (3 points)**
- [ ] Tous contrats récents et renouvelés: 3 points
- [ ] >80% contrats récents: 2 points
- [ ] 60-80% contrats récents: 1 point
- [ ] <60% contrats récents: 0 points

**14. Contrats Fournisseurs (3 points)**
- [ ] Tous contrats favorables: 3 points
- [ ] Conditions standard: 2 points
- [ ] Quelques contraintes: 1 point
- [ ] Conditions défavorables: 0 points

**15. Contrats Employés (4 points)**
- [ ] Tous contrats standard sans risques: 4 points
- [ ] Quelques contrats types: 3 points
- [ ] Certains contrats complexes: 2 points
- [ ] Contrats à risque: 0 points
```

### **Propriété Intellectuelle (5 points)**
```markdown
**16. Actifs PI (3 points)**
- [ ] PI forte et protégée: 3 points
- [ ] PI moyenne: 2 points
- [ ] PI faible: 1 point
- [ ] PI inexistante: 0 points

**17. Licences et Permissions (2 points)**
- [ ] Toutes licences actives: 2 points
- [ ] Quelques licences: 1 point
- [ ] Aucunes licences: 0 points
```

## 🔧 Évaluation Technologie (20 points maximum)

### **Architecture Système (8 points)**
```markdown
**18. Stack Moderne (3 points)**
- [ ] Stack récente et scalable: 3 points
- [ ] Stack mixte acceptable: 2 points
- [ ] Stack dépassée: 1 point
- [ ] Stack critique: 0 points

**19. Architecture Cloud (3 points)**
- [ ] Fully cloud-native: 3 points
- [ ] Hybrid cloud: 2 points
- [ ] On-premise: 1 point
- [ ] Legacy system: 0 points

**20. Scalabilité (2 points)**
- [ ] Très scalable: 2 points
- [ ] Modérément scalable: 1 point
- [ ] Non scalable: 0 points
```

### **Qualité et Maintenance (7 points)**
```markdown
**21. Code Quality (3 points)**
- [ ] Code propre, bien documenté: 3 points
- [ ] Code acceptable: 2 points
- [ ] Code médiocre: 1 point
- [ ] Code mauvais: 0 points

**22. Tests Coverage (2 points)**
- [ ] >80% test coverage: 2 points
- [ ] 50-80% test coverage: 1 point
- [ ] <50% test coverage: 0 points

**23. Déploiement (2 points)**
- [ ] CI/CD mature: 2 points
- [ ] CI/CD basique: 1 point
- [ ] Pas de CI/CD: 0 points
```

### **Sécurité et Performance (5 points)**
```markdown
**24. Sécurité (3 points)**
- [ ] Sécurité robuste: 3 points
- [ ] Sécurité moyenne: 2 points
- [ ] Vulnérabilités connues: 1 point
- [ ] Vulnérabilités critiques: 0 points

**25. Performance (2 points)**
- [ ] Performance excellente: 2 points
- [ ] Performance acceptable: 1 point
- [ ] Performance médiocre: 0 points
```

## 👥 Équipe Évaluation (15 points maximum)

### **Team Leadership (6 points)**
```markdown
**26. Leadership (3 points)**
- [ ] Leadership fort et expérimenté: 3 points
- [ ] Leadership compétent: 2 points
- [ ] Leadership médiocre: 1 point
- [ ] Leadership inconnu: 0 points

**27. Équipe Fondatrice (3 points)**
- [ ] Équipe complémentaire expérimentée: 3 points
- [ ] Équipe acceptable: 2 points
- [ ] Équipe en développement: 1 point
- [ ] Équipe incomplète: 0 points
```

### **Talent et Culture (5 points)**
```markdown
**28. Retention (3 points)**
- [ ] <10% turnover: 3 points
- [ ] 10-20% turnover: 2 points
- [ ] 20-30% turnover: 1 point
- [ ] >30% turnover: 0 points

**29. Culture (2 points)**
- [ ] Culture excellente: 2 points
- [ ] Culture bonne: 1 point
- [ ] Culture problématique: 0 points
```

### **Structure Organisation (4 points)**
```markdown
**30. Organisation (4 points)**
- [ ] Structure claire et scalable: 4 points
- [ ] Structure acceptable: 3 points
- [ ] Structure confuse: 2 points
- [ ] Structure chaotique: 0 points
```

## 📊 Marché Évaluation (10 points maximum)

### **Positionnement Marché (4 points)**
```markdown
**31. Market Share (2 points)**
- [ ] Leader (>30%): 2 points
- [ ] Challenger (15-30%): 1 point
- [ ] Follower (<15%): 0 points

**32. Tendances (2 points)**
- [ ] Tendance forte: 2 points
- [ ] Tendance modérée: 1 point
- [ ] Tendance faible: 0 points
```

### **Compétitivité (4 points)**
```markdown
**33. Avantage Concurrentiel (2 points)**
- [ ] Avantage durable: 2 points
- [ ] Avantage temporaire: 1 point
- [ ] Pas d'avantage: 0 points

**34. Barrières Entrée (2 points)**
- [ ] Barrières élevées: 2 points
- [ ] Barrières modérées: 1 point
- [ ] Barrières faibles: 0 points
```

### **Vision Stratégique (2 points)**
```markdown
**35. Roadmap (2 points)**
- [ ] Vision claire et réalisable: 2 points
- [ ] Vision modérée: 1 point
- [ ] Vision inexistante: 0 points
```

## 🚨 Red Flags et Critères d'Exclusion

### **Red Flags Immédiates (0 points si trouvées)**
```markdown
**Critères d'exclusion absolue**:
- [ ] Litiges majeurs (>1M€)
- [ ] Dette/EBITDA >5x
- [ ] Churn client >20%
- [ ] Turnover >30%
- [ ] Technologie dépassée (>5 ans)
- [ ] Conformité non résolue
- [ ] Fondateurs quittant l'entreprise
- [ ] Client concentration >50%
```

### **Warnings Conditions (Réduire score)**
```markdown
**Conditions à négocier**:
- [ ] EBITDA <15% (-5 points)
- [ ] Revenus non-récurrents >50% (-5 points)
- [ ] Clients concentration >30% (-3 points)
- [ ] Technologie legacy (-3 points)
- [ ] Conformité partielle (-3 points)
```

## 📈 Métriques de Suivi

### **Scorecard Dashboard**
```markdown
**Tracking Metrics**:
- Score final: [ ]/100
- Status: 🟢/🟡/🔴
- Date d'évaluation: [Date]
- Évaluateur: [Nom]
- Échéance: [Date]

**Key Insights**:
- Force principale: [Section]
- Faiblesse principale: [Section]
- Risques identifiés: [List]
- Opportunités: [List]
```

### **Comparaison avec Benchmarks**
```markdown
**Benchmark Industry**:
- Score industry moyen: [Score]
- Positionnement: [Above/Average/Below]
- Gap à combler: [Gap]

**Competitive Position**:
- vs Competitor 1: [Better/Equal/Worse]
- vs Competitor 2: [Better/Equal/Worse]
- Market positioning: [Rank]
```

---

### Related
- [[ma-checklist-template]]
- [[ma-valuation-process]]
- [[ma-antitrust-scenarios]]
- [[ma-grid-comparatif]]
## Related

- [[_system/MOC-patterns]]
- [[brantham/_MOC]]