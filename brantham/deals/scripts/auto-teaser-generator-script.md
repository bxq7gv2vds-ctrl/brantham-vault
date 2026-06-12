---
type: script
purpose: deal-teaser-generation
created: 2026-06-12
version: 1.0
---

# Script Auto-Génération Teasers Deals

## 🎯 Objectif
Générer automatiquement 50+ teasers qualifiés par semaine à partir du pipeline deals existant.

## 📊 Structure du Script

### 1. Input Pipeline
```python
# Source: /Users/paul/Downloads/brantham-pipeline/deals/
# Format: CSV/JSON avec colonnes clés
REQUIRED_FIELDS = [
    'company_name',
    'siren', 
    'sector',
    'employees',
    'revenue',
    'ebitda',
    'procedure_type',
    'deadline',
    'source',
    'score'
]
```

### 2. Template Teaser Standardisé

#### Format: Markdown - 500 mots max
```markdown
# [Nom Entreprise] - [Secteur]

## 📋 Situation Actuelle
- **Procédure**: [Type] - [Date deadline]
- **Effectif**: [Nombre] salariés
- **Chiffre d'affaires**: [Montant] €
- **EBITDA**: [Montant] € ([Multiple]x)

## 🎯 Opportunité d'Investissement
- **Thématique**: [Focus sectoriel]
- **Stratégie**: [Positionnement cible]
- **Potentiel**: [Argument clé]

## 🔍 Points Clés à Diligence
- **Risques**: [Top 3 risques]
- **Atouts**: [Top 3 atouts]
- **Financement**: [Structure proposée]

## 💡 Prochaines Étapes
- **Timeline**: [Échéancier]
- **Contact**: [Information]
```

### 3. Scoring Priorisation

#### Score de Pertinence Deal
```python
def calculate_deal_score(company_data):
    score = 0
    
    # Critères sectoriels (30%)
    if company_data['sector'] in ['tech', 'industrie', 'healthtech']:
        score += 30
    
    # Taille deal (25%)
    if 20 <= company_data['employees'] <= 100:
        score += 25
    elif company_data['employees'] > 100:
        score += 20
    
    # Urgence (20%)
    days_to_deadline = (deadline - today).days
    if days_to_deadline < 7:
        score += 20
    elif days_to_deadline < 30:
        score += 15
    
    # Rentabilité (15%)
    if company_data['ebitda'] > 0:
        score += 15
    
    # Score source (10%)
    if company_data['source'] in ['AjIRE', 'Trajectoire']:
        score += 10
    
    return score
```

### 4. Processus Auto

#### Étape 1: Filtrage Initial (5 min)
- Appliquer score > 60
- Exclure secteurs non stratégiques
- Vérifier deadline > 7 jours

#### Étape 2: Enrichissement Pappers (15 min)
```python
# Récupérer données complémentaires
pappers_data = get_company_papers(company_data['siren'])
enriched_data = {
    'address': pappers_data['adresse'],
    'legal_status': pappers_data['forme_juridique'],
    'creation_date': pappers_data['date_creation'],
    'financial_health': calculate_financial_score(pappers_data)
}
```

#### Étape 3: Génération Teaser (2 min par deal)
```python
template = load_template(sector_template)
content = template.render(
    company=company_data,
    enriched=enriched_data,
    scoring=deal_score
)
```

#### Étape 4: Validation & Export (1 min)
- Vérifier longueur < 500 mots
- Exporter vers `/brantham/deals/teasers/YYYY-MM-DD/`
- Mettre à jour pipeline status

### 5. Automatisation

#### Workflow GitOps
```bash
# Lancement quotidien
0 6 * * * /usr/bin/python3 /path/to/auto-teaser-generator.py

# Surveillance
tail -f /var/log/teaser-generator.log
```

#### Monitoring & Alertes
- Taux de génération: >50 teasers/jour
- Taux d'erreur: <5%
- Délai de traitement: <30 min/deal

## 📊 Exemple Teaser Généré

```markdown
# BP METAL - Industrie Mécanique

## 📋 Situation Actuelle
- **Procédure**: Redressement judiciaire - 30/04/2026
- **Effectif**: 34 salariés
- **Chiffre d'affaires**: 2.8M€
- **EBITDA**: 420K€ (6.2x)

## 🎯 Opportunité d'Investissement
- **Thématique**: Consolidation secteur industriel
- **Stratégie**: Acquisition asset-light avec équipe technique
- **Potentiel**: Synergie avec portefeuille existant

## 🔍 Points Clés à Diligence
- **Risques**: Dette fournisseurs 400K€, dépendance client 35%
- **Atouts**: Brevets propriétaires, équipe technique stable
- **Financement**: 70% cash + 30% earn-out sur EBITDA

## 💡 Prochaines Étapes
- **Timeline**: LOI D+5, closing D+15
- **Contact**: Paul Roulleou - p@brantham.com
```

## 🚀 Performance Attendue

### Metrics Cibles
- **Volume**: 50+ teasers/semaine
- **Qualité**: 85% score >70
- **Temps**: <30 min/deal
- **Coût**: <2€/teaser (LLM)

### Pipeline Impact
| Étape | Actuel | Post-script | Amélioration |
|-------|--------|-------------|--------------|
| Teasers générés | 2/394 | 50+/394 | +2400% |
| Temps génération | J+7 | J+1 | -85% |
| Taux conversion | 5% | 15% | +200% |

### Risques & Mitigation
- **Qualité variable**: Template standardisé + review AI
- **Données incomplètes**: Fallback sur sector averages
- **Format inconsistent**: Validation automatique
- **Volume élevé**: Batch processing par lots de 10

## Related
- [[brantham/deals/workflows/acquisition-step-by-step-workflow]]
- [[brantham/deals/scores/distressed-target-scorecard]]
- [[brantham/deals/_MOC]]