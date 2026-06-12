---
name: framework-risques-ma-sectoriel
description: Framework de risques M&A spécifiques par secteur d'activité
metadata:
  type: pattern
  category: ma
  date: 2026-06-12
  author: Brantham Partners
  created_for: M&A Risk Assessment
  industry_verticals: ['tech', 'healthcare', 'retail', 'manufacturing', 'energy']
  risk_categories: ['market', 'operational', 'financial', 'regulatory', 'integration']
---

# Framework de Risques M&A Sectoriels

## Vue d'Exécutive

Ce framework identifie et quantifie les risques sectoriels spécifiques pour les transactions M&A, permettant une évaluation ciblée et des stratégies de mitigation proactives. Systématisation de l'analyse des risques par code NAF et caractéristiques sectorielles.

## Classification Sectorielle des Risques

### Secteur 1 : Technologie & Digital (NAF 61, 62, 63)

**Risques Spécifiques :**
- Obsolescence technologique (>60% dans le secteur)
- Dépendance fournisseurs clés (concentration >40%)
- Cybersecurity & protection données (RGPR)
- Brain drain post-acquisition
- Régulation IA & données

**Indicateurs Clés :**
- Ratio R&D/CA (>15% = risque élevé)
- Cycle de renouvellement technologique
- Portefeuille de brevets et propriété intellectuelle
- Score de cybersécurité

### Secteur 2 : Santé & Pharma (NAF 21, 26)

**Risques Spécifiques :**
- Approbations réglementaires (ANSM, EMA)
- Contentieux médicaux
- Dépendance génériques
- R&D pipeline validation
- Régulation anti-corruption

**Indicateurs Clés :**
- Nombre d'approbations en attente
- Ratio R&D/exploitation
- Portfolio de molécules en cours
- Litiges en cours

### Secteur 3 : Énergie & Environnement (NAF 35, 37, 38)

**Risques Spécifiques :**
- Régulation climatique (CSRD, Taxonomie)
- Obligations ESG & reporting
- Transition énergétique
- Responsabilité environnementale
- Prix des matières premières

**Indicateurs Clés :**
- Score ESG (>75% requis)
- Intensité carbone (tCO2/€ CA)
- Programme décarbonation
- Coûts de conformité

### Secteur 4 : Retail & Distribution (NAF 47, 46)

**Risques Spécifiques :**
- Transformation digitale
- Loyauté client & rétention
- Concurrence en ligne
- Supply chain resilience
- Valeur foncière immobilière

**Indicateurs Clés :**
- % CA en ligne (>25% = tendance positive)
- Score NPS (>50 = santé)
- Rotation des stocks (<60 jours)
- Rentabilité m²

### Secteur 5 : Industrie & Manufacturing (NAF 10-33)

**Risques Spécifiques :**
- Supply chain globale
- Coûts énergétiques
- Automatisation & IA
- Normes qualité & certification
- Impact carbonique

**Indicateurs Clés :**
- Intensité énergétique (€/produit)
- Taux d'automatisation (>40% = opportunité)
- Délai de production
- Taux de rebuts

## Méthodologie d'Évaluation des Risques

### Étape 1 : Cartographie des Risques Sectoriels
```markdown
1. Identification du code NAF principal
2. Analyse des sous-secteurs concernés
3. Documentation des régulations spécifiques
4. Identification des risques transversaux
```

### Étape 2 : Quantification des Expositions
```markdown
- Probabilité : 1-5 (très faible à très élevée)
- Impact financier : € (estimation directe)
- Impact stratégique : 1-5 (court/moyen/long terme)
- Impact réglementaire : non conforme/en ligne/out of compliance
```

### Étape 3 : Scoring Agrégé
**Formule :**
```
Score = Σ(Probabilité × Impact Financier × Pondération Sectorielle)
```

**Classification :**
- 0-30 : Risque faible (vert)
- 31-60 : Risque modéré (orange)  
- 61-100 : Risque élevé (rouge)

## Stratégies de Mitigation Sectorielles

### Tech Sector Mitigation
- **Due diligence tech** : Audit des systèmes, code review, security assessment
- **Retention plan** : Clauses de non-concurrence, stock options, bonus liés
- **Transition planning** : Roadmap d'intégration technique, décommissioning plan
- **Regulatory compliance** : DPO nommé, conformité RGPR, certification ISO 27001

### Pharma Sector Mitigation
- **Regulatory tracking** : Pipeline d'approbations, délais réglementaires
- **IP protection** : Audit des brevets, freedom to operate analysis
- **Compliance culture** : Code of conduct, hotlines, training mandatory
- **Supply chain diversification** : Deux fournisseurs critiques minimum

### Energy Sector Mitigation
- **ESG integration** : Reporting intégré, objectifs climatiques vérifiés
- **Regulatory monitoring** : Suivi CSRD, Taxonomie verte, régulations locales
- **Physical risks** : Climate vulnerability assessment, adaptation plan
- **Transition planning** : Roadmap décarbonation, investissements verts

## Checklist de Due Diligence Sectorielle

### Documents à Requérir par Secteur

**Tech Sector :**
- [ ] Audit de sécurité (pen test, vuln scan)
- [ ] Cartographie des systèmes d'information
- [ ] Contrats de licence logiciels
- [ ] Politiques de données personnelles
- [ ] Documentation technique complète

**Pharma Sector :**
- [ ] Dossiers ANSM/EMA
- [ ] Brevets et propriété intellectuelle
- [ ] Essais cliniques et données
- [ ] Contrats de distribution
- [ ] Conformité anti-corruption

**Energy Sector :**
- [ ] Autorisations environnementales
- [ ] Bilan carbone et reporting ESG
- [ ] Contrats d'approvisionnement énergétique
- [ ] Plan de démantèlement
- [ ] Conformité réglementaire

## Outils & Templates

### Risk Assessment Template
```markdown
## Risque [Nom du Risque]
**Secteur :** [Code NAF]
**Probabilité :** [1-5]
**Impact Financier :** [€]
**Impact Stratégique :** [1-5]
**Indicateur Clé :** [Métrique de monitoring]
**Plan de Mitigation :**
- Action 1 : [Responsable, Délai]
- Action 2 : [Responsable, Délai]
**Monitoring :** [Fréquence, Alertes]
```

### Risk Dashboard Structure
- **Heatmap sectorielle** : Visualisation des risques par secteur
- **Trending indicators** : Évolution des risques dans le temps
- **Mitigation tracking** : Progress des actions correctives
- **Early warning system** : Signaux d'alerte précoce

## Déclencheurs d'Action

### Rouge (Risque élevé >60)
- **Action immédiate** : Due diligence ciblée, négociation de clauses protectrices
- **Reporting :** Board alerte mensuelle, Comité des risques spécialisé
- **Escalade :** CEO, CFO, Legal Counsel

### Orange (Risque modéré 31-60)
- **Action planifiée** : Intégration dans planning DD
- **Reporting :** Comité des risques trimestriel
- **Responsable :** Head of M&A, Legal

### Vert (Risque faible <30)
- **Monitoring :** Suivi annuel
- **Reporting :** Due diligence standard
- **Responsable :** M&A Analyst

## Indicateurs de Performance

### KPIs de Risques M&A
- **Taux de risques résolus** (>90% cible)
- **Coût de mitigation** vs budget alloué
- **Temps de résolution moyen** (<45 jours)
- **Nouveaux risques identifiés** (track trending)
- **Efficacité des stratégies** (vs benchmark sectoriel)

## Next Steps

1. **Validation sectorielle** : Recueillir input experts sectoriels
2. **Calibration des poids** : Ajuster pondérations par secteur
3. **Intégration process** : Inclure dans processus M&A standard
4. **Training teams** : Former M&A et DD aux spécificités
5. **Tools deployment** : Déployer dashboard de monitoring

---

## Related

- [[brantham/_MOC]]
- [[_system/MOC-patterns]]
- [[due-diligence-checklist]]
- [[scoring-cibles-ma]]
- [[teaser-ma-template]]