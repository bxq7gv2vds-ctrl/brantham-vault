---
type: pattern
template: scoring-algorithm
created: 2026-06-12
tags: [m-a, scoring, ai, distressed]
---

# Scoring M&A Prédictif - Algorithmme

Système de scoring automatisé pour prioriser les deals M&A distressed.

## Variables d'entrée

### Critères financiers (poids: 40%)
- `ca_score` = min(100, (CA_annuel / 500000) * 100)  # Normalisé sur 500k€
- `ebitda_margin` = EBITDA / CA * 100  # Marge en %
- `dettes_ratio` = Dettes totales / CA  # Ratio endettement
- `cash_score` = min(100, Tresorerie / 12 * 100)  # 12 mois de CA

### Critères procéduraux (poids: 30%)
- `procedure_score` = 
  - liquidation: 30 points
  - redressement: 60 points  
  - sauvegarde: 80 points
- `duree_procedure` = jours depuis ouverture
- `deadline_urgence` = jours avant deadline (max 90)

### Critères sectoriels (poids: 20%)
- `secteur_score` = 
  - commerce: 70
  - industrie: 65
  - numérique: 75
  - services: 60
  - autres: 50

### Critères stratégiques (poids: 10%)
- `localisation_score` = 
  - IDF: 80
  - Grandes villes: 70
  - Autres: 50
- `effectif_score` = min(100, effectif / 50 * 100)

## Formule de scoring

```python
def calculate_deal_score(deal_data):
    # Critères financiers
    financial_score = (
        deal_data['ca_score'] * 0.4 +
        deal_data['ebitda_margin'] * 0.15 +
        max(0, 100 - deal_data['dettes_ratio'] * 2) * 0.15 +
        deal_data['cash_score'] * 0.1
    )
    
    # Critères procéduraux  
    procedural_score = (
        deal_data['procedure_score'] * 0.6 +
        max(0, 100 - deal_data['duree_procedure'] / 90 * 100) * 0.2 +
        max(0, 100 - deal_data['deadline_urgence'] / 90 * 100) * 0.2
    )
    
    # Score final pondéré
    final_score = (
        financial_score * 0.4 +
        procedural_score * 0.3 +
        deal_data['secteur_score'] * 0.2 +
        (deal_data['localisation_score'] + deal_data['effectif_score']) / 2 * 0.1
    )
    
    return round(final_score, 1)
```

## Classes de risque

- **90-100** : Deal premium (priorité immédiate)
- **70-89** : Deal high-potential (à suivre)
- **50-69** : Deal standard (pipeline normal)
- **<50** : Deal low-priority (surveiller)

## Indicateurs clés

- **Taux de conversion** : (Deals clos / Deals analysés)
- **Temps moyen deal** : jours du lead au close
- **Valeur moyenne deal** : CA moyen des deals clos
- **Sector success rate** : taux par secteur

## Implémentation

```python
# Exemple d'utilisation
deal_example = {
    'ca_annuel': 1200000,
    'ebitda': 180000,
    'dettes_totales': 800000,
    'tresorerie': 100000,
    'procedure': 'redressement',
    'duree_procedure': 45,
    'deadline_urgence': 30,
    'secteur': 'commerce',
    'localisation': 'IDF',
    'effectif': 25
}

score = calculate_deal_score(deal_example)
print(f"Score deal: {score}/100")
```

## Related
- [[brantham/knowledge/skills/data-science-m-a]]
- [[brantham/patterns/teaser-patterns]]
- [[brantham/deals/_MOC]]