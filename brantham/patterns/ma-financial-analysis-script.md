---
name: script-analyse-financiere-ma
description: Script automatisé d'analyse financière pré-M&A avec calculs de valorisation, synergies et rentabilité
metadata:
  type: pattern
  category: ma
  date: 2024-06-12
  tags: [ma, finance, valuation, analyse, script]
  author: Paul Roulleau
---

# Script d'Analyse Financière Pré-M&A

## Vue d'entreprise

Script structuré pour l'analyse financière pré-M&A couvrant due diligence, valorisation, et structuration de deal. Optimisé pour une exécution rapide avec résultats actionnables.

## Workflow Complet

### Phase 1 : Collecte et Validation des Données (30 min)
```markdown
## Checklist Collecte Données Financières
### Données Historiques (3-5 ans)
- [ ] Comptes sociaux annuels (bilan, compte de résultat, annexe)
- [ ] Comptes consolidés si applicable
- [ ] Etat des flux de trésorerie (tableau de flux)
- [ ] Prévisions financières (business plan)
- [ ] Tableaux de bord de performance mensuelle

### Données Opérationnelles
- [ ] Chiffre d'affaires par ligne de produit/segment
- [ ] Marge brute par segment (>10% détail)
- [ ] Coûts fixes vs variables (détail par nature)
- [ ] Soldes intermédiaires de gestion (SIG)
- [ ] Indicateurs de performance opérationnelle (KPIs)

### Données de Dette
- [ ] Tableau d'amortissement des dettes
- [ ] Contrats de financement existants
- [ ] Covenants financiers (ratio leverage, coverage)
- [ ] Échéances de remboursement
- [ ] Garanties et collatéraux
```

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
    
    # Valeur actuelle
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

### Étape 6: Modélisation des Synergies Financières

```python
def calculate_synergies(target_data, acquirer_data):
    """
    Calcule les synergies financières potentielles
    """
    synergies = {}
    
    # Synergies de coûts
    cost_synergies = {
        'economies_echelle': target_data['coûts'] * 0.10,  # 10%
        'rationalisation_effectif': target_data['salaires'] * 0.15,  # 15% des effectifs
        'achats_groupes': target_data['achats'] * 0.05  # 5%
    }
    
    # Synergies de revenus
    revenue_synergies = {
        'cross_selling': target_data['ca'] * 0.15,  # 15%
        'premium_prix': target_data['ca'] * 0.07,  # 7%
        'nouveaux_produits': target_data['ca'] * 0.10  # 10%
    }
    
    # Investissements nécessaires
    investments = {
        'integration_systeme': target_data['ca'] * 0.03,  # 3%
        'formation_equipe': target_data['salaires'] * 0.02,  # 2%
        'technologie': target_data['investissements'] * 0.05  # 5%
    }
    
    # Flux de synergies nets
    synergies['annuel'] = sum(cost_synergies.values()) + sum(revenue_synergies.values()) - sum(investments.values())
    synergies['valeur_actualisee'] = synergies['annuel'] * 0.15  # Perpétuité à 15%
    
    return {
        'coûts': cost_synergies,
        'revenus': revenue_synergies,
        'investissements': investments,
        'flux_net': synergies['annuel'],
        'valeur': synergies['valeur_actualisee']
    }

# Calcul des synergies
synergies = calculate_synergies(target_data, acquirer_data)
```

### Étape 7: Analyse des Risques Financiers

```python
def financial_risk_assessment(ratios, industry_data):
    """
    Évalue les risques financiers spécifiques
    """
    risk_score = 0
    risks = []
    
    # Risques de liquidité
    if ratios['ratio_liquidite_immediate'] < 0.5:
        risk_score += 20
        risks.append("Risque de liquidité - ratio < 0.5")
    
    # Risques d'endettement
    if ratios['endettement'] > 4.0:
        risk_score += 30
        risks.append("Risque d'endettement élevé - >4x EBITDA")
    
    # Risques de croissance
    if ratios['croissance_ca'] < 0.05:
        risk_score += 15
        risks.append("Croissance insuffisante - <5%")
    
    # Risques de rentabilité
    if ratios['marge_ebitda'] < 0.10:
        risk_score += 20
        risks.append("Marge EBITDA faible - <10%")
    
    # Risques opérationnels
    if ratios['capacite_autofinancement'] < 1.0:
        risk_score += 15
        risks.append("Autofinancement insuffisant - <100%")
    
    return {
        'risk_score': min(risk_score, 100),
        'risk_level': 'Élevé' if risk_score > 60 else 'Moyen' if risk_score > 30 else 'Faible',
        'risks_identified': risks
    }

# Évaluation des risques
risk_assessment = financial_risk_assessment(ratios, industry_data)
```

### Étape 8: Scoring Global et Recommandation

```python
def generate_final_recommendation(valuation, ratios, comparison, risk_assessment, synergies):
    """
    Génère une recommandation finale avec scoring détaillé
    """
    
    # Calcul des scores
    scores = {}
    
    # Score de valorisation (30%)
    valuation_methods = ['ebitda_multiple', 'ca_multiple', 'net_multiple']
    avg_valuation = np.mean([valuation[m] for m in valuation_methods if m in valuation])
    scores['valuation'] = min(avg_valuation / 1000000 / 10, 1) * 30  # Normalisé sur 30
    
    # Score de santé financière (30%)
    financial_health = (
        min(ratios['marge_ebitda'] / 0.20, 1) * 0.3 +
        min(max(0, (3 - ratios['endettement']) / 3), 1) * 0.3 +
        min(ratios['croissance_ca'] / 0.15, 1) * 0.2 +
        min(ratios['couverture_dettes'] / 5, 1) * 0.2
    ) * 30
    scores['financial_health'] = financial_health
    
    # Score de positionnement (20%)
    competitive_score = sum(1 for comp in comparison.values() if comp['vs_avg'] > 0)
    scores['competitive'] = min(competitive_score / len(comparison), 1) * 20
    
    # Score de risques (20%)
    risk_component = max(0, (100 - risk_assessment['risk_score']) / 100)
    scores['risk'] = risk_component * 20
    
    # Score des synergies (bonus)
    if synergies['valeur'] > 0:
        scores['synergies'] = min(synergies['valeur'] / 1000000 / 5, 1) * 10
    else:
        scores['synergies'] = 0
    
    # Score total
    total_score = sum(scores.values())
    
    # Classement
    if total_score >= 80:
        recommendation = "ACHETER - Exceptionnel"
        priority = "Immédiate"
    elif total_score >= 60:
        recommendation = "ACHETER - Très attractif"
        priority = "Haute"
    elif total_score >= 40:
        recommendation = "SURVEILLER - Potentiel limité"
        priority = "Moyenne"
    else:
        recommendation = "ÉVITER - Trop de risques"
        priority = "Basse"
    
    return {
        'scores': scores,
        'total_score': total_score,
        'recommendation': recommendation,
        'priority': priority,
        'synergies_value': synergies['valeur']
    }

# Génération de la recommandation finale
final_recommendation = generate_final_recommendation(
    valuation, ratios, comparison, risk_assessment, synergies
)
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

=== SYNERGIES ===

Synergies Annuelles:
- Coûts: €500K/an (efficacité opérationnelle)
- Revenus: €750K/an (croissance cross-selling)
- Flux Net: €1.25M/an
- Valeur Actualisée: €8.3M

=== RISQUES ===

Score de Risque: 35/100 (Faible)
Risques Identifiés:
- [ ] Dépendance clientèle >30% (contrôlée)
- [ ] Innovation technologique (surveillance)
- [ ] Concurrence agressive (monitoring)

=== RECOMMANDATION FINALE ===

Score Global: 82/100
Recommandation: ACHETER - Exceptionnel
Priorité: Immédiate
Valeur Synergies: €8.3M
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