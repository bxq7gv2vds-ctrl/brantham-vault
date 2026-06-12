---
name: risques-ma-sectoriels
description: Framework de risques M&A par secteur d'activité avec cartographie détaillée
type: pattern
---

# Framework de Risques M&A Sectoriels

## Introduction

Ce framework permet d'évaluer les risques spécifiques par secteur pour les opérations M&A, avec une approche prédictive et des mesures d'atténuation adaptées.

## Méthodologie d'Évaluation des Risques

### Score de Risque Global
```
Risque Global = (Risque Secteur × Pondération) + (Risque Transactionnel × Pondération) + (Risque Post-M&A × Pondération)
```

### Échelle de Gravité
- **Très Faible (1)** : Impact minime, mesures standards
- **Faible (2)** : Impact contrôlable, surveillance légère
- **Moyen (3)** : Impact significatif, action requise
- **Élevé (4)** : Impact critique, plan d'action immédiat
- **Très Élevé (5)** : Impact critique, risque existentiel

## Cartographie des Risques par Secteur

### 1. Secteur Technologie & Digital

**Risques Spécifiques :**
- **Obsolescence technologique** (Score 4)
  - Signes : Technologie non-maintenue, R&D sous-investie
  - Atténuation : Due diligence tech, roadmap de migration
  - KPI : % de code legacy < 30%

- **Fuite de talents** (Score 4)
  - Signes : Turnover > 20%, key employees leaving
  - Atténuation : Retention clauses, earn-out
  - KPI : Taux de rétention équipe technique

- **Cybersécurité** (Score 5)
  - Signes : Vulnérabilités connues, pas de SOC
  - Atténuation : Audit sécurité, compliance SOC2
  - KPI : Score de maturité cybersécurité > 80%

- **Données utilisateurs** (Score 3)
  - Signes : Non-compliance GDPR, données non structurées
  - Atténuation : Audit RGPD, plan de migration
  - KPI : % de conformité réglementaire

**Checkliste Sectorielle Tech :**
```
□ Audit de code source (vulnérabilités)
□ Évaluation de la stack technique (maintenance, scalability)
□ Analyse des contrats SaaS/clients
□ Due diligence sécurité (penetration testing)
□ Évaluation des brevets/IP
□ Cartographie des compétences clés
```

### 2. Secteur Santé & Pharma

**Risques Spécifiques :**
- **Approbation réglementaire** (Score 5)
  - Signes : Dossiers FDA/EMA incomplets
  - Atténuation : Consultant réglementaire, processus validation
  - KPI : % de produits approuvés

- **Responsabilité médicale** (Score 5)
  - Signes : Historique litiges, procédures non-documented
  - Atténuation : Due diligence assurance, compliance FDA 21 CFR
  - KPI : Score audit qualité > 90%

- **Perte de licence** (Score 4)
  - Signes : Non-conformité GMP, inspections échouées
  - Atténuation : Plan de correction, investissement qualité
  - KPI : Audit qualité trimestriel passed

- **Intellectual Property** (Score 4)
  - Signes : Brevets expirés, liberté d'exploitation douteuse
  - Atténuation : IP audit, freedom-to-operate analysis
  - KPI : Brevets valides > 70%

**Checkliste Sectorielle Santé :**
```
□ Audit réglementaire (FDA, EMA, HAS)
□ Analyse des essais cliniques (data integrity)
□ Évaluation des installations (GMP compliance)
□ Due diligence assurance (claims history)
□ Audit qualité systèmes
□ Cartographie des certifications
```

### 3. Secteur Manufacturing & Industrie

**Risques Spécifiques :**
- **Pollution environnementale** (Score 5)
  - Signes : Historique non-conformité, sites REACH concernés
  - Atténuation : Audit environnemental, provision réglementaire
  - KPI : % de sites ISO 14001 certifiés

- **Sécurité travailleurs** (Score 4)
  - Signes : Taux d'accident élevé, procedures non-standard
  - Atténuation : Audit sécurité, investissement prévention
  - KPI : TRS > 95%

- **Chaîne d'approvisionnement** (Score 3)
  - Signes : Single-source suppliers, stockout récent
  - Atténuation : Diversification fournisseurs, plan B
  - KPI : % fournisseurs certifiés ISO 9001

- **Obligations REACH** (Score 4)
  - Signes : Substances chimiques non-documented
  - Atténuation : Chemical safety assessment, compliance
  - KPI : % substances conformes REACH

**Checkliste Sectorielle Industrie :**
```
□ Audit environnemental (ISO 14001, REACH)
□ Analyse sécurité (accidents, procédures)
□ Évaluation supply chain (fournisseurs critiques)
□ Audit qualité systèmes (ISO 9001)
□ Cartographie des équipements (maintenance)
□ Analyse réglementaire (permis d'exploiter)
```

### 4. Secteur Services & Consulting

**Risques Spécifiques :**
- **Client concentration** (Score 3)
  - Signes : >30% revenue de 3 clients tops
  - Atténuation : Diversification portefeuille, contrats long-term
  - KPI : % clients portefeuille > 20

- **Propriété intellectuelle** (Score 2)
  - Signes : Méthodes non-patentées, know-how non-documenté
  - Atténuation : IP strategy, documentation procédures
  - KPI : % méthodes propriétaires

- **Réputation** (Score 3)
  - Signes : Reviews négatifs, churn élevé
  - Atténuation : Due diligence réputation, crise management
  - KPI : Net Promoter Score > 50

- **Talents clés** (Score 3)
  - Signes : Key persons dependency
  - Atténuation : Cross-training, retention strategy
  - KPI : % compétences multi-compétents

**Checkliste Sectorielle Services :**
```
□ Analyse portefeuille clients (concentration)
□ Audit réputation (reviews, references)
□ Due diligence RH (turnover, satisfaction)
□ Evaluation méthodes propriétaires
□ Cartographie compétences clés
□ Analyse contrats clients (MRR, churn)
```

## Matrice de Risques Sectoriels

| Secteur | Réglementaire | Opérationnel | Financier | Humain | Technologique | Score Max |
|---------|---------------|--------------|-----------|--------|---------------|-----------|
| Tech | 2 | 3 | 2 | 4 | 5 | 16 |
| Santé | 5 | 4 | 3 | 4 | 3 | 19 |
| Industrie | 4 | 5 | 3 | 3 | 2 | 17 |
| Services | 2 | 3 | 3 | 4 | 2 | 14 |
| Retail | 3 | 4 | 4 | 3 | 2 | 16 |

## Processus d'Évaluation des Risques

### Phase 1 : Identification Préliminaire (J-14)
```
1. Screening sectoriel (30 min)
2. Identification risques red flags
3. Plan de due diligence ciblée
4. Équipe d'experts sectoriels assignée
```

### Phase 2 : Due Diligence Approfondie (J-7 à J-0)
```
1. Audit spécifique sectoriel (3-5 jours)
2. Consultation experts externes
3. Analyse comparatif peers
4. Quantification impacts financiers
```

### Phase 3 : Cartographie des Risques (J-1)
```
1. Scoring détaillé par risque
2. Priorisation actions atténuation
3. Plan de monitoring post-M&A
4. Reporting à la direction
```

## Tableau de Bord de Risques Sectoriels

### Indicateurs Clés de Surveillance (KPIs)
```markdown
| Risque | Fréquence | Seuil Alerte | Action |
|--------|-----------|--------------|---------|
| Tech Stack | Hebdo | >40% legacy | Migration roadmap |
| Regulatory | Mensuel | Audit failed | Corrective action |
| Talent Turnover | Quotidien | >15% monthly | Retention program |
| Compliance Trimestriel | Score < 80% | External audit |
```

### Reporting des Risques
```python
class RiskDashboard:
    def __init__(self, sector):
        self.sector = sector
        self.risks = self.load_sector_risks()
        
    def calculate_risk_score(self):
        total_score = sum(risk['score'] for risk in self.risks)
        max_score = len(self.risks) * 5
        return (total_score / max_score) * 100
    
    def generate_report(self):
        return {
            'sector': self.sector,
            'overall_risk_level': self.get_risk_level(),
            'critical_risks': self.get_critical_risks(),
            'mitigation_plan': self.get_mitigation_plan()
        }
```

## Plan d'Atténuation des Risques

### Actions Immédiates (0-30 jours)
```
1. Comité de crise risques sectoriels
2. Documentation procédures critiques
3. Communication parties prenantes
4. Mise en place monitoring
```

### Actions Moyen Terme (1-6 mois)
```
1. Intégration systèmes
2. Formation équipes cible
3. Harmonisation pratiques
4. Reporting consolidé
```

### Actions Long Terme (6-12 mois)
```
1. Optimisation synergies
2. Standardisation globale
3. Transformation digitale
4. Exit strategy review
```

## Tools & Templates

### Risk Assessment Template
```yaml
risk_assessment:
  sector: "technology"
  target_company:
    name: "TechCorp"
    industry: "SaaS"
  identified_risks:
    - category: "technological"
      name: "Legacy codebase"
      score: 4
      impact: "high"
      likelihood: "medium"
      mitigation: "Migration plan in 6 months"
      ownership: "CTO"
  timeline:
    discovery_phase: "J-14"
    due_diligence: "J-7"
    assessment_complete: "J-0"
```

### Sector Risk Matrix
```python
def generate_sector_risk_matrix(sector):
    risk_matrices = {
        'technology': {
            'key_risks': ['obsolescence', 'talent_retention', 'cybersecurity'],
            'red_flags': ['legacy_code > 40%', 'turnover > 25%', 'no SOC2'],
            'success_factors': ['tech_stack_modern', 'dev_team_stable', 'security_certified']
        },
        'healthcare': {
            'key_risks': ['regulatory', 'liability', 'ip_protection'],
            'red_flags': ['pending_fda', 'litigation_history', 'expired_patents'],
            'success_factors': ['fda_approved', 'compliance_certified', 'ip_portfolio']
        }
    }
    return risk_matrices.get(sector, {})
```

## Best Practices Sectorielles

### Tech Sector
- **Embaucher un CTO pour la due diligence tech**
- **Vérifier les contrats SaaS existants**
- **Auditer la stack technique (scalability, security)**
- **Évaluer la roadmap produit vs marché**

### Santé Sector
- **Engager des réglementaires spécialisés**
- **Auditer les essais cliniques (data integrity)**
- **Vérifier les assurances responsabilité médicale**
- **Évaluer les installations (GMP compliance)**

### Industrie Sector
- **Auditer environnemental (ISO 14001)**
- **Vérifier les permis d'exploiter**
- **Évaluer la chaîne d'approvisionnement**
- **Analyser la sécurité au travail**

## Conclusion

Ce framework permet d'identifier les risques spécifiques par secteur avec une approche structurée et prédictive. L'analyse combinée des risques sectoriels et transactionnels fournit une vision complète pour une évaluation M&A robuste.

## Related
- [[scoring-cibles-ma]]
- [[due-diligence-checklist]]
- [[ma-synergy-analysis-model]]
- [[_system/MOC-patterns]]