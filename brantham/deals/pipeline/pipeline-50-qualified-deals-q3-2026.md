---
type: pipeline-plan
quarter: Q3-2026
target: 50-deals
created: 2026-06-12
version: 1.0
---

# Pipeline 50 Deals Qualifiés - Q3 2026

## 🎯 Objectif Global
**50 deals qualifiés** avec score >70 par fin septembre 2026
- **Début Q3**: 5 deals qualifiés (actuel)
- **Fin Q3**: 55 deals qualifiés (+50)
- **Taux conversion**: 15% (7.5 deals effectifs)

---

## 📊 Pipeline par Mois

### Juillet 2026: Fondation (17 deals)
**Sourcing**:
- AJ scrapes daily: 1,500 annonces/semaine
- Cibles sectorielles: Tech/industrie/services
- Score préliminaire: >60 points

**Qualification**:
- Deals passés score >70: 17
- Deals sous diligence: 8
- Deals en négociation: 2

### Août 2026: Accélération (20 deals)
**Sourcing boost**:
- Partenaires intermédiaires: 5 contacts
- Campagne ciblée: 3 secteurs focus
- Hot leads: Deals urgent (<15j)

**Progression**:
- Nouveaux deals qualifiés: 20
- Total Q3: 37 deals
- Conversion active: 4 deals

### Septembre 2026: Finalisation (18 deals)
**Closing push**:
- Deals prioritaires: Top 15
- Négociations intensives: 10 deals
- Closings: 3 deals

**Objectif**:
- Deals qualifiés: 18
- Total Q3: 55 deals
- Effectués: 7.5 deals

---

## 🎯 Stratégie de Sourcing

### Sources Prioritaires
1. **AJ Up** (Trajectoire, AjIRE) - 40%
   - Tech/industrie prioritaires
   - Deals <30j deadline

2. **Partenaires Intermediaries** - 30%
   - Mandataires spécialisés
   - Deals warm introductions

3. **Scraping Direct** - 20%
   - Secteurs chauds: Cyber, AI, GreenTech
   - Keywords stratégiques

4. **Réseau** - 10%
   - Deals referencés
   - High quality

### Critères de Qualification
```python
QUALITY_CRITERIA = {
    'sector': ['tech', 'industrie', 'healthtech', 'greentech'],
    'employees': range(20, 200),
    'revenue': range(2000000, 50000000),
    'ebitda_positive': True,
    'score': >70,
    'deadline': >15j
}
```

---

## 📈 Pipeline Management

### Workflow Qualification
1. **Screening Initial** (2 min/deal)
   - Score préliminaire: 0-100
   - Filtre secteur: Oui/Non
   - Taux rejet: 70%

2. **Enrichissement Pappers** (10 min/deal)
   - Données financières
   - Procédures collectives
   - Propriété intellectuelle

3. **Scoring Final** (5 min/deal)
   - Score détaillé >70
   - Risques identifiés
   - Potentiel de deal

4. **Priorisation** (1 min/deal)
   - Classement par score
   - Urgence relative
   - Ressources allouées

### Taux de Conversion Cible
| Étape | Taux | Temps | Nombre |
|-------|------|-------|--------|
| Sourcing | 100% | 2 min | 1,500 |
| Qualification | 30% | 10 min | 450 |
| Scoring >70 | 12% | 5 min | 180 |
| Diligence | 25% | 5h | 45 |
| Négociation | 50% | 2 sem | 22 |
| Closing | 75% | 2 sem | 16.5 |

---

## 🚀 Actions Mois par Mois

### Juillet 2026 - Setup
**Semaines 1-2**:
- [ ] Configurer scoring automatisé
- [ ] Lancer scraping AJ quotidien
- [ ] Contact 3 mandataires
- [ ] Benchmark sectoriel

**Semaines 3-4**:
- [ ] Analyser 500+ deals
- [ ] Qualifier 17 deals
- [ ] Lancer diligence sur 8 deals
- [ ] Template teasers finalisé

### Août 2026 - Scaling
**Semaines 5-6**:
- [ ] Campagne sectorielle ciblée
- [ ] Partenariats actifs
- [ ] Qualifier 20 deals
- [ ] Négocier 4 deals

**Semaines 7-8**:
- [ ] Focus deals urgents
- [ ] Diligence approfondie
- [ ] Pipeline review weekly
- [ ] Adjuster critères

### Septembre 2026 - Closing
**Semaines 9-10**:
- [ ] Priorité top 15 deals
- [ ] Négociations intensives
- [ ] LOIs signées
- [ ] Préparation closing

**Semaines 11-12**:
- [ ] Finaliser 3 closings
- [ ] Review pipeline Q3
- [ ] Plan Q4 validation
- [ ] Lessons learned

---

## 💰 Budget & Ressources

### Coûts Estimés Q3
- **Scraping AJ**: 500€/mois
- **Papers API**: 300€/mois (1,000 req)
- **Mandataires**: 2,000€ (fees)
- **Diligence**: 15,000€ (external)
- **Legal**: 10,000€
- **Total**: ~28,000€

### Équipe Allouée
- **Paul**: 100% focus pipeline
- **Mandataire externe**: Part-time (10 deals)
- **Juriste**: 2-3 jours/semaine (phase closing)

---

## 📊 Monitoring & KPIs

### Indicateurs Clés Quotidiens
- **Nouveaux deals**: 50-75/jour
- **Taux qualification**: 12-15%
- **Score moyen**: >75
- **Deadline tracking**: <15j urgent

### Suivi Hebdomadaire
| Semaine | Sourcing | Qualifiés | Diligence | Négociation |
|---------|----------|-----------|-----------|-------------|
| 1 | 350 | 8 | 2 | 0 |
| 2 | 375 | 9 | 3 | 1 |
| 3 | 400 | 10 | 4 | 2 |
| 4 | 375 | 8 | 3 | 1 |
| 5 | 425 | 12 | 4 | 2 |
| 6 | 450 | 13 | 5 | 3 |
| 7 | 475 | 15 | 6 | 4 |
| 8 | 450 | 12 | 4 | 3 |
| 9 | 400 | 10 | 5 | 5 |
| 10 | 375 | 8 | 3 | 4 |
| 11 | 350 | 6 | 2 | 3 |
| 12 | 300 | 4 | 1 | 2 |

### Dashboard
- **Pipeline réel**: vs planifié
- **Taux conversion**: par source
- **Temps moyen**: par étape
- **ROI estimé**: 3x investment

---

## 🎯 Risques & Mitigation

### Risques Principaux
1. **Volume scraping faible**: Diversifier sources
2. **Qualité deals variable**: Scoring strict
3. **Diligence lente**: Prioriser deals urgents
4. **Marché volatile**: Focus secteurs résilients

### Plan B
- **Réduire objectif**: 40 deals si nécessaire
- **Accélérer**: Deals <10j deadline
- **Partenariats**: Focus sur deals référencés

---

## 📈 Success Metrics Q3

### Objectifs Atteints
- [ ] 50+ deals qualifiés score >70
- [ ] 7.5 deals effectivement clos
- [ ] Pipeline renouvelé: 20+ deals Q4
- [ ] Processus optimisé: <20 min/deal

### Impact Business
- **Revenue estimé**: 15M€ (7.5 deals x 2M€)
- **Frais M&A**: 1.125M€ (7.5%)
- **Net**: 13.875M€
- **Multiple**: 10x investment

## Related
- [[brantham/deals/scores/distressed-target-scorecard]]
- [[brantham/deals/scripts/auto-teaser-generator-script]]
- [[brantham/deals/workflows/acquisition-step-by-step-workflow]]
- [[brantham/deals/_MOC]]