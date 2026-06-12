---
type: pattern
template: scoring-algorithm
created: 2026-06-12
tags: [m-a, scoring, sectoriel, ai]
---

# Scoring Sectoriel M&A

Algorithme de scoring adapté par secteur pour deals distressed.

## Variables communes (tous secteurs)

### Critères financiers (poids: 40%)
```python
def financial_score(deal):
    ca_normalized = min(100, (deal['ca_annuel'] / 500000) * 100)
    ebitda_margin = (deal['ebitda'] / deal['ca_annuel']) * 100
    debt_ratio = deal['dettes_totales'] / deal['ca_annuel']
    cash_score = min(100, (deal['tresorerie'] / (deal['ca_annuel'] / 12)) * 100)
    
    return (
        ca_normalized * 0.4 +
        ebitda_margin * 0.15 +
        max(0, 100 - debt_ratio * 2) * 0.15 +
        cash_score * 0.3
    )
```

### Critères procéduraux (poids: 30%)
```python
def procedural_score(deal):
    procedure_points = {
        'liquidation': 30,
        'redressement': 60,
        'sauvegarde': 80
    }
    
    procedure_score = procedure_points.get(deal['procedure_type'], 50)
    urgency_score = max(0, 100 - (deal['days_to_deadline'] / 90) * 100)
    duration_score = max(0, 100 - (deal['days_since_opening'] / 180) * 100)
    
    return (
        procedure_score * 0.5 +
        urgency_score * 0.3 +
        duration_score * 0.2
    )
```

## Secteur 1 : Commerce/Retail

### Spécificités sectorielles
**Actifs clés :** emplacement, clientèle, marque, stock
**Risques :** concurrence, changement de consommation, digitalisation
**Opportunités :** synergie réseau, optimisation coûts, transformation digitale

### Variables supplémentaires (poids: 30%)
```python
def commerce_score(deal):
    # Localisation (15%)
    location_score = {
        'centre_ville': 90,
        'quartier_commercial': 80,
        'zone_périphérique': 60,
        'rural': 40
    }
    
    # Clientèle (10%)
    client_concentration = max(0, 100 - (deal['top_client_percent'] * 1.5))
    
    # Digitalisation (5%)
    digital_score = min(100, deal['online_sales_percent'] * 2)
    
    return (
        location_score.get(deal['location_type'], 50) * 0.5 +
        client_concentration * 0.33 +
        digital_score * 0.17
    )
```

### Score final commerce
```python
def commerce_total_score(deal):
    financial = financial_score(deal)
    procedural = procedural_score(deal) 
    sectorial = commerce_score(deal)
    
    return (
        financial * 0.4 +
        procedural * 0.3 +
        sectorial * 0.3
    )
```

## Secteur 2 : Industrie/Manufacturing

### Spécificités sectorielles
**Actifs clés :** équipements, savoir-faire, fournisseurs, locaux
**Risques :** obsolescence technologique, dépendance fournisseurs, réglementation
**Opportunités :** synergies techniques, modernisation, optimisation logistique

### Variables supplémentaires (poids: 30%)
```python
def industry_score(deal):
    # Actifs physiques (15%)
    asset_quality = {
        'neuf': 90,
        'recent': 70,
        'age_moyen': 50,
        'vieux': 30
    }
    
    # Chaîne d'approvisionnement (10%)
    supplier_diversity = min(100, deal['supplier_count'] * 5)
    
    # Technologie (5%)
    tech_score = deal['automation_level'] * 20  # 0-5 scale
    
    return (
        asset_quality.get(deal['asset_condition'], 50) * 0.5 +
        supplier_diversity * 0.33 +
        tech_score * 0.17
    )
```

### Score final industrie
```python
def industry_total_score(deal):
    financial = financial_score(deal)
    procedural = procedural_score(deal)
    sectorial = industry_score(deal)
    
    return (
        financial * 0.4 +
        procedural * 0.3 +
        sectorial * 0.3
    )
```

## Secteur 3 : Numérique/SaaS

### Spécificités sectorielles
**Actifs clés :** base clients, code, équipe technique, technologie stack
**Risques :** obsolescence tech, churn, dépendance clé techniques
**Opportunités :** croissance rapide, internationalisation, économies d'échelle

### Variables supplémentaires (poids: 30%)
```python
def digital_score(deal):
    # Base clients (10%)
    client_base_score = min(100, deal['client_count'] / 10)
    
    # Recurring revenue (10%)
    recurring_score = deal['recurring_revenue_percent'] * 0.8
    
    # Technologie (5%)
    tech_stack_score = deal['tech_stack_quality'] * 20  # 0-5 scale
    scalability = deal['scalability_potential'] * 20  # 0-5 scale
    
    return (
        client_base_score * 0.25 +
        recurring_score * 0.5 +
        (tech_stack_score + scalability) / 2 * 0.25
    )
```

### Score final numérique
```python
def digital_total_score(deal):
    financial = financial_score(deal)
    procedural = procedural_score(deal)
    sectorial = digital_score(deal)
    
    return (
        financial * 0.4 +
        procedural * 0.3 +
        sectorial * 0.3
    )
```

## Secteur 4 : Services

### Spécificités sectorielles
**Actifs clés :** équipe, clientèle, contrats long terme, réputation
**Risques :** dépendance personnes, concurrence prix, changements réglementaires
**Opportunités :** standardisation, digitalisation, acquisition concurrents

### Variables supplémentaires (poids: 30%)
```python
def services_score(deal):
    # Capital humain (10%)
    team_score = min(100, deal['employee_count'] * 2)
    key_person_risk = max(0, 100 - deal['key_person_dependency'] * 10)
    
    # Portefeuille contrats (10%)
    contract_quality = deal['contract_duration_years'] * 10
    contract_renewal_rate = deal['contract_renewal_rate'] * 100
    
    # Réputation (10%)
    brand_score = deal['brand_strength'] * 20  # 0-5 scale
    
    return (
        (team_score + key_person_risk) / 2 * 0.33 +
        contract_quality * 0.33 +
        (contract_renewal_rate + brand_score) / 2 * 0.34
    )
```

### Score final services
```python
def services_total_score(deal):
    financial = financial_score(deal)
    procedural = procedural_score(deal)
    sectorial = services_score(deal)
    
    return (
        financial * 0.4 +
        procedural * 0.3 +
        sectorial * 0.3
    )
```

## Implémentation système

### Dashboard de scoring
```python
class SectorialScoringSystem:
    def __init__(self):
        self.sectors = {
            'commerce': commerce_total_score,
            'industrie': industry_total_score,
            'numerique': digital_total_score,
            'services': services_total_score
        }
    
    def calculate_score(self, deal_data):
        sector = deal_data['secteur'].lower()
        scoring_func = self.sectors.get(sector, commerce_total_score)
        return scoring_func(deal_data)
    
    def classify_deal(self, score):
        if score >= 90:
            return "Premium", "Priorité immédiate"
        elif score >= 70:
            return "High-potential", "À suivre"
        elif score >= 50:
            return "Standard", "Pipeline normal"
        else:
            return "Low-priority", "Surveiller"
```

### Exemple d'utilisation
```python
# Deal e-commerce
deal_ecommerce = {
    'ca_annuel': 2000000,
    'ebitda': 300000,
    'dettes_totales': 800000,
    'tresorerie': 150000,
    'procedure_type': 'redressement',
    'days_to_deadline': 45,
    'days_since_opening': 60,
    'secteur': 'numerique',
    'location_type': 'centre_ville',
    'top_client_percent': 35,
    'online_sales_percent': 70,
    'client_count': 150,
    'recurring_revenue_percent': 80,
    'tech_stack_quality': 4,
    'scalability_potential': 4
}

scoring_system = SectorialScoringSystem()
score = scoring_system.calculate_score(deal_ecommerce)
classification = scoring_system.classify_deal(score)
print(f"Score: {score}/100, Classe: {classification}")
```

## Related
- [[brantham/patterns/scoring-predictif-m-a]]
- [[brantham/knowledge/skills/data-science-m-a]]
- [[brantham/deals/_MOC]]

---

**Utilité** : Scoring sectoriel adapté pour prioriser deals par type d'activité avec variables spécifiques à chaque secteur.

**Prochaine action** : Tâche 7 - Script prospection Fonds d'investissement