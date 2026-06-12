---
title: "Analyse du Pipeline M&A - État au 12 juin 2026"
date: 2026-06-12
type: analysis
category: m-a-pipeline
status: completed
---

# Analyse du Pipeline M&A - État au 12 juin 2026

## Vue d'ensemble du pipeline

### Volume global
- **423 dossiers actifs** dans `/deals/` (vs 25 au 25/03 — croissance x17 en 3 mois)
- **90 089 procédures actives** en base (81 362 en_cours + 8 727 plan_en_cours)
- **45 deals** dans le workspace (brantham-pipeline/deals/)
- **10 deals actifs** actuellement dans le pipeline board

### Statuts récents
- **29 deals avec analyse complète** / 1 avec teaser / 20 avec acheteurs identifiés / 36 enrichis
- **0 deal complet** (analyse + teaser + acheteurs)
- **Seul deal actif** sur le board : MLD en statut "teaser_redige"

### Points critiques identifiés
1. **Goulez d'écoulement** : 0 deal complet malgré 29 analyses → problème de génération de teasers
2. **Risque de surcharge** : croissance explosive x17 en 3 mois, risque de dégradation qualité
3. **Manque d'automatisation** : processus manuel pour matching acheteurs, génération de teasers

## Focus deals actifs

### Deal prioritaire : MONABEE
- **Statut** : Actif, dossier complet (analyse + SAV technique)
- **Marché** : Photovoltaïque résidentiel B2C, distressed
- **Chiffre d'affaires** : 8,22 M€ (2024) — base solide
- **Points forts** : Marque régionale, technologie propriétaire, équipe technique formée
- **Deadline** : 19 juin 2026 (urgence)
- **Valeur ajoutée** : Différenciation par verticalisation technique (boîtiers de pilotage)

### Autres deals actifs significatifs
- **MLD** : Teaser rédigé, en attente de matching acheteurs
- **Multiple deals industriels** : Priorité matching (SILICONES, API TECH type)
- **58 sal** : Deal avec actif immo, données disponibles pour génération teaser

## Indicateurs de performance

### Productivité
- **Taux de conversion analyse → teaser** : 1/29 (3,4%) → Critiquement bas
- **Nombre moyen de deals par statut** : Inéquilibré vers l'amont
- **Temps de traitement moyen** : Non tracké → besoin de monitoring

### Qualité du sourcing
- **Segments dominants** : Énergie renouvelable, tech industrielle, distressed
- **Géographie** : Rhône-Alpes fort concentré, Bretagne émergente
- **Tailles cibles** : Micro à PME (CA < 15M€) typiques M&A distressed

## Actions prioritaires identifiées

### Court terme (J-7)
1. **Urgent MLD** : Générer matching acheteurs sur ADIAMAS (58 sal, actif immo)
2. **Monabee** : Accélérer processus - deadline 19 juin
3. **Automatisation teasers** : Lancer `generate_teaser.py` sur les 12 deals actifs

### Moyen terme (J-30)
1. **Scaling qualité** : Implémenter scoring automatique pour priorisation
2. **Processus outreach** : Automatiser enrichissement contacts + emailing
3. **Monitoring pipeline** : Tableau de bord en temps réel

### Long terme (J-90)
1. **Diversification segments** : Élargissement vers M&A non-distressed
2. **Intelligence marché** : Veille concurrentielle et sectorielle
3. **Écosystème acheteurs** : Base de données propriétaires enrichie

## Insights stratégiques

### Force principale
- **Expertise distressed** : Processus éprouvé dans procédures judiciaires
- **Data BODACC** : Avantage informationnel significatif vs compétiteurs
- **Réseau régional** : Maillage solide Auvergne-Rhône-Alpes

### Risques majeurs
- **Scalabilité** : Croissance x17 non soutenue sans automatisation
- **Diversification** : Dépendance excessive au segment distressed
- **Qualité deals** : Risque de dilution avec volume élevé

### Opportunités
- **Monetisation data** : Vente d'analyses sectorielles aux acheteurs
- **Plateforme tech** : Développement outils M&A pour petits cabinets
- **Internationalisation** : Extension modèle vers marchés similaires (Europe du Sud)

## Related
- [[brantham/_MOC]]
- [[brantham/pipeline/board]]
- [[brantham/patterns/distressed-ma-pattern]]
- [[brantham/agents/director/index]]
- [[brantham/cowork-prompts/03-deal-analysis]]