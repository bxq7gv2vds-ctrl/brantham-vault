# Playbook de Prospection Automatisée M&A Distressed

Un système complet de prospection d'opportunités M&A distressed avec scoring automatisé, relances multi-canal et reporting temps réel.

## 📊 Features

### Intelligence (J-3 à J-1)
- **Scanning BODACC** : Surveillance des liquidations judiciaires
- **Scoring qualitatif** : Score automatisé (0-100) basé sur 5 critères
- **Critères d'admission** : CA 500K€-10M€, secteurs tech/SaaS/cybersécurité

### Activation (J0 à J+3)
- **Matching acheteurs** : Segmentation automatique des prospects
- **Contraintes légales** : Vérification L.642-3 Code de commerce
- **Séquences de relances** : Multi-canal (LinkedIn, email, téléphone)

### Exécution (J+3 à J+14)
- **Monitoring automatique** : Relances planifiées selon timing optimisé
- **Traitement des réponses** : Scoring automatique des réponses
- **Génération d'offres** : Offres légales conformes

### Dashboard
- **Reporting temps réel** : KPIs, évolution, prévisions
- **Alertes automatisées** : Notifications email pour relances en retard
- **CSV/JSON export** : Pour analyse externe

## 🚀 Installation

```bash
cd /Users/paul/vault/brantham/market-analysis/distressed-prospection/
pip install requests pandas numpy
```

## 📝 Utilisation

### Pipeline Complet

```python
from prospection_automatisee import ProspectionAutomatiseeMandA

# Initialiser le pipeline
pipeline = ProspectionAutomatiseeMandA()

# Exécuter le processus complet
rapport = pipeline.run_pipeline('complet')

# Exporter les données
export = pipeline.export_automatique()
print(f"CSV: {export['csv_export']}")
print(f"JSON: {export['json_export']}")
```

### Modules Individuels

```python
# Scanner les liquidations
from data_sources import DataSources
data_sources = DataSources()
liquidations = data_sources.scan_bodacc_liquidations()

# Calculer les scores
from scoring_distressed import ScoringDistressed
scoring = ScoringDistressed()
score = scoring.score_global(deal)

# Matcher avec acheteurs
from matching_acheteurs import MatchingAcheteurs
matching = MatchingAcheteurs()
score_segments = matching.calculer_matching('fonds_investissement', prospects)
```

### Dashboard

```python
from dashboard_prospection import RelanceTracker

tracker = RelanceTracker()

# Ajouter des prospects
tracker.ajouter_prospect(deal_data)

# Enregistrer des relances
tracker.enregistrer_relance(prospect_id, 'email', 'Contenu')

# Générer rapports
report_text = tracker.generer_report('text')
report_json = tracker.generer_report('json')
```

## 🎯 KPIs Cibles

- **Temps moyen J0 → dépôt offre** : 48h maximum
- **Taux de réponse** : 15-20%
- **Taux de conversion** : 8-12%
- **Prospects qualifiés/semaine** : 5-10

## 🔧 Configuration

### Critères de qualification
- **CA minimum** : 500 000€
- **CA maximum** : 10 000 000€
- **Secteurs prioritaires** : 62.01 (IT), 63.11 (consulting), 69.10 (ingénierie)
- **Score minimum** : 60/100

### Timing des relances
- **Vue pas de réponse** : J+1, J+3, J+7, J+14
- **Vue réponse positive** : J+2, J+5
- **Vue réponse négative** : J+7

## 📊 Exemple de rapport

```
============================================================
DASHBOARD - Suivi Prospection M&A Distressed
============================================================

📊 KPIs Clés:
  Total prospects: 8
  Contacts effectués: 6
  Prospects intéressés: 2
  Taux de réponse: 18.5%
  Temps moyen conversion: 4.2j
  Score moyen: 72.5/100

🎯 Segments cibles:
  fonds_investissement: 4 prospects
  strategique: 3 prospects
  family_office: 2 prospects

📈 Évolution 7 jours:
  Nouveaux prospects: 3
  Convertis: 1

⏰ Relances prévies (7j): 4
```

## 🔒 Sécurité

- **Critères légaux** : Respect de la L.642-3 Code de commerce
- **Données fictives** : Les données de démonstration ne représentent pas de vraies entreprises
- **Configuration sécurisée** : Stockage des credentials via variables d'environnement

## 📈 Évolution

### V1.0 (Actuel)
- Pipeline complet de prospection
- Scoring automatisé
- Dashboard de reporting
- Alertes automatisées

### V2.0 (Planifié)
- Intégration CRM Salesforce
- API web pour monitoring mobile
- Intelligence artificielle pour prédiction de conversion
- Automatisation du closing

---

**Documentation** : [Complet](README.md) | [API](api-reference.md) | [Configuration](config.md)

**Support** : support@mandistressed.fr