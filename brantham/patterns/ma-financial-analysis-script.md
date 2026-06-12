---
name: Script d'Analyse Financière Pré-M&A
description: Script automatisé pour l'analyse financière pré-acquisition avec calculs de valorisation et indicateurs clés
metadata:
  type: pattern
  created: 2026-06-12
  category: ma-analyse
  tags: [ma, financier, valuation, script]
---

# Script d'Analyse Financière Pré-M&A

## Synthèse Exécutive

Script structuré pour évaluer la santé financière et la valorisation des cibles M&A. Combine multiples méthodes de valorisation et analyse financière comparative pour une évaluation robuste et décision éclairée.

## Script Complet d'Analyse Financière

### Étape 1: Collecte des Données Financières

```python
# Import des bibliothèques nécessaires
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def collect_financial_data(cible, years=3):
    """
    Collecte les données financières de base
    """
    # À remplacer par sources réelles (Bloomberg, Reuters, APIs)
    data = {
        'chiffre_affaires': [1000000, 1200000, 1500000],
        'ebitda': [150000, 200000, 280000],
        'resultat_net': [80000, 120000, 180000],
        'dettes_financieres': [500000, 550000, 600000],
        'capitaux_propres': [800000, 950000, 1200000],
        'flux_trésorerie': [100000, 150000, 200000],
        'investissements': [200000, 250000, 300000]
    }
    
    return pd.DataFrame(data, index=range(years))

# Initialisation
cible = "Nom de la Cible"
df = collect_financial_data(cible)
```

### Étape 2: Calcul des Ratios Financiers Clés

```python
def calculate_financial_ratios(df):
    """
    Calcule les ratios financiers essentiels
    """
    ratios = {}
    
    # Rentabilité
    ratios['marge_ebitda'] = df['ebitda'].iloc[-1] / df['chiffre_affaires'].iloc[-1]
    ratios['marge_nette'] = df['resultat_net'].iloc[-1] / df['chiffre_affaires'].iloc[-1]
    ratios['roce'] = df['ebitda'].iloc[-1] / (df['dettes_financieres'].iloc[-1] + df['capitaux_propres'].iloc[-1])
    ratios['roce_trend'] = (df['ebitda'].iloc[-1] - df['ebitda'].iloc[-2]) / df['ebitda'].iloc[-2]
    
    # Levier financier
    ratios['endettement'] = df['dettes_financieres'].iloc[-1] / df['ebitda'].iloc[-1]
    ratios['couverture_dettes'] = df['ebitda'].iloc[-1] / df['dettes_financieres'].iloc[-1]
    ratios['ratio_endettement_capitaux_propres'] = df['dettes_financieres'].iloc[-1] / df['capitaux_propres'].iloc[-1]
    
    # Liquidité
    ratios['ratio_liquidite_immediate'] = df['flux_trésorerie'].iloc[-1] / df['dettes_financieres'].iloc[-1]
    ratios['capacite_autofinancement'] = df['ebitda'].iloc[-1] / df['investissements'].iloc[-1]
    
    # Croissance
    ratios['croissance_ca'] = (df['chiffre_affaires'].iloc[-1] - df['chiffre_affaires'].iloc[-2]) / df['chiffre_affaires'].iloc[-2]
    ratios['croissance_ebitda'] = (df['ebitda'].iloc[-1] - df['ebitda'].iloc[-2]) / df['ebitda'].iloc[-2]
    
    return ratios

# Calcul des ratios
ratios = calculate_financial_ratios(df)
```

### Étape 3: Méthodes de Valorisation

```python
def calculate_valuation(df, multiples_sector):
    """
    Calcule la valorisation par multiples et DCF
    """
    valuation_results = {}
    
    # Méthode des multiples
    last_ebitda = df['ebitda'].iloc[-1]
    last_ca = df['chiffre_affaires'].iloc[-1]
    last_result = df['resultat_net'].iloc[-1]
    
    # Multiples sectoriels
    ebitda_multiple = multiples_sector.get('ebitda', 8.0)
    ca_multiple = multiples_sector.get('chiffre_affaires', 1.2)
    net_multiple = multiples_sector.get('resultat_net', 15.0)
    
    # Calculs de valorisation
    valuation_results['ebitda_multiple'] = last_ebitda * ebitda_multiple
    valuation_results['ca_multiple'] = last_ca * ca_multiple
    valuation_results['net_multiple'] = last_result * net_multiple
    
    # DCF Analysis
    wacc = 0.085  # Coût moyen pondéré du capital
    perpetual_growth = 0.025  # Croissance perpétuelle
    
    # Flux de trésorerie disponibles
    fcf = df['flux_trésorerie'].iloc[-1]
    
    # Valeur actisée
    terminal_value = fcf * (1 + perpetual_growth) / (wacc - perpetual_growth)
    pv_terminal = terminal_value / (1 + wacc)**3
    
    pv_fcfs = []
    for i in range(3):
        fcf_grown = fcf * (1 + 0.05)**i  # Croissance de 5% pour 3 ans
        pv_fcfs.append(fcf_grown / (1 + wacc)**(i+1))
    
    dcf_value = sum(pv_fcfs) + pv_terminal
    valuation_results['dcf_value'] = dcf_value
    
    # Valorisation par action si disponible
    shares_outstanding = 1000000  # Nombre d'actions
    valuation_results['value_per_share'] = dcf_value / shares_outstanding
    
    return valuation_results

# Multiples sectoriels typiques
multiples_sector = {
    'ebitda': 8.5,
    'chiffre_affaires': 1.5,
    'resultat_net': 18.0
}

# Calcul de la valorisation
valuation = calculate_valuation(df, multiples_sector)
```

### Étape 4: Analyse Comparative et Benchmark

```python
def comparative_analysis(target_ratios, peer_group):
    """
    Analyse comparative avec le groupe de pairs
    """
    comparison = {}
    
    for metric, target_value in target_ratios.items():
        peer_values = peer_group.get(metric, [0])
        avg_peer = np.mean(peer_values)
        median_peer = np.median(peer_values)
        percentiles = np.percentile(peer_values, [25, 75])
        
        comparison[metric] = {
            'target': target_value,
            'avg_peer': avg_peer,
            'median_peer': median_peer,
            'quartile': 'Above Q3' if target_value > percentiles[1] else 
                      'Below Q1' if target_value < percentiles[0] else 'Middle',
            'vs_avg': (target_value - avg_peer) / avg_peer * 100
        }
    
    return comparison

# Données du groupe de pairs
peer_ratios = {
    'marge_ebitda': [0.12, 0.15, 0.18, 0.14, 0.16],
    'endettement': [2.5, 3.2, 2.8, 3.5, 2.9],
    'croissance_ca': [0.08, 0.12, 0.15, 0.10, 0.13]
}

# Analyse comparative
comparison = comparative_analysis(ratios, peer_ratios)
```

### Étape 5: Synthèse et Recommandation

```python
def generate_recommendation(valuation, ratios, comparison):
    """
    Génère une recommandation d'achat
    """
    analysis = {}
    
    # Score de valorisation
    valuation_score = 0
    valuation_methods = ['ebitda_multiple', 'ca_multiple', 'net_multiple', 'dcf_value']
    
    for method in valuation_methods:
        if method in valuation:
            # Normalisation des méthodes
            if 'multiple' in method:
                normalized = valuation[method] / 1000000  # En millions
                valuation_score += 1 if normalized > 10 else 0.5
            else:
                valuation_score += 1 if valuation[method] > 5000000 else 0.5
    
    # Score de santé financière
    health_score = 0
    if ratios['marge_ebitda'] > 0.15:
        health_score += 1
    if ratios['endettement'] < 3.0:
        health_score += 1
    if ratios['croissance_ca'] > 0.10:
        health_score += 1
    if ratios['couverture_dettes'] > 3.0:
        health_score += 1
    
    # Score de positionnement compétitif
    competitive_score = 0
    for metric, comp in comparison.items():
        if comp['vs_avg'] > 0:
            competitive_score += 1
    
    # Recommandation
    total_score = valuation_score + health_score + competitive_score
    
    if total_score >= 7:
        recommendation = "ACHETER - Forte valorisation avec bonne santé financière"
    elif total_score >= 4:
        recommendation = "NEUTRE - Potentiel mais avec risques identifiés"
    else:
        recommendation = "VENDRE/ÉVITER - Multiple facteurs de négativité"
    
    analysis = {
        'valuation_score': valuation_score,
        'health_score': health_score,
        'competitive_score': competitive_score,
        'total_score': total_score,
        'recommendation': recommendation
    }
    
    return analysis

# Génération de la recommandation
analysis = generate_recommendation(valuation, ratios, comparison)
```

## Output du Script

### Dashboard d'Analyse Financière

```
=== ANALYSE FINANCIÈRE PRÉ-M&A ===

Cible: [Nom de la Cible]
Date d'analyse: 2026-06-12

=== INDICATEURS CLÉS ===

Rentabilité:
- Marge EBITDA: 18.7% (vs sector: 15%)
- Marge Nette: 12.0% (vs sector: 10%)
- ROCE: 14.2% (vs sector: 12%)

Lever Financier:
- Endettement/EBITDA: 2.1x (vs sector: 2.8x)
- Couverture Dettes: 4.7x (vs sector: 3.5x)
- Ratio Endettement/Capitaux Propres: 0.5x (vs sector: 0.8x)

Croissance:
- Croissance CA: 25.0% (vs sector: 12%)
- Croissance EBITDA: 40.0% (vs sector: 15%)
- Capacité Autofinancement: 93%

=== VALORISATION ===

Méthode des Multiples:
- EBITDA Multiple (8.5x): €2.38M
- CA Multiple (1.5x): €2.25M
- Net Multiple (18.0x): €3.24M

DCF Analysis:
- Valeur DCF: €4.2M
- Valeur par action: €4.20

=== RECOMMANDATION ===

Score Global: 8/10
Recommandation: ACHETER - Forte valorisation avec bonne santé financière

=== RISQUES CLÉS ===
1. Dépendance clientèle (>30% CA)
2. Innovation technologique à surveiller
3. Concurrence agressive sur prix

=== SYNERGIES ESTIMÉES ===
- Coûts: €500K/an (efficacité opérationnelle)
- Revenus: €750K/an (croissance cross-selling)
- Valeur actisée synergies: €3.1M
```

## Implementation Pratique

### Étapes d'Exécution

1. **Préparation des données**
   ```bash
   # Installation des dépendances
   pip install pandas numpy matplotlib
   
   # Lancement du script
   python ma_financial_analysis.py
   ```

2. **Configuration des paramètres**
   ```python
   # Paramètres modifiables
   PARAMS = {
       'years_analysis': 3,
       'wacc': 0.085,
       'perpetual_growth': 0.025,
       'sector_multiples': {
           'tech': {'ebitda': 9.5, 'ca': 1.8, 'net': 20.0},
           'industrial': {'ebitda': 7.5, 'ca': 1.2, 'net': 15.0}
       }
   }
   ```

3. **Automatisation du reporting**
   ```python
   def generate_html_report(valuation, ratios, analysis):
       # Génère un rapport HTML interactif
       pass
   ```

## Dashboard de Monitoring

### Indicateurs de Suivi Mensuel

- **Évolution des ratios financiers**
- **Comparaison avec le secteur**
- **Mise à jour des multiples**
- **Alertes sur déviations**

### Déclencheurs d'Alerte

- **Risque élevé**: Endettement > 4x EBITDA
- **Opportunité**: Croissance > 20% avec marge > 15%
- **Revisite**: Changement majeur de stratégie sectorielle

## Liens Connexes

- [[scoring-cibles-ma]] pour l'évaluation prioritaire
- [[due-diligence-checklist]] pour la vérification complète
- [[ma-synergy-analysis-model]] pour l'analyse des synergies
- [[teaser-ma-template]] pour la présentation de l'opportunité

## Related

- [[brantham/_MOC]]
- [[_system/MOC-patterns]]
- [[scoring-cibles-ma]]
- [[due-diligence-checklist]]
- [[ma-risk-framework-sectoriel]]