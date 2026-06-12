---
type: pattern
template: workflow
created: 2026-06-12
tags: [m-a, workflow, process, optimization]
---

# Workflow Deal Flow Optimisé

Processus structuré pour maximiser l'efficacité du pipeline M&A distressed.

## Phase 1 : Identification & Qualification (J+0 à J+7)

### 1.1 Intelligence précoce
**Sources :**
- Scanning BODACC quotidien (nouvelles procédures)
- Alertes Pappers (changement statut RCs)
- Réseau AJ (partenariats exclusifs)
- Veille sectorielle (actualités régionales)

**Outils automatisés :**
- Script Python BODACC scraper
- Alertes Google News sectorielles
- Slack notifications pour deals scoring >70

### 1.2 Qualification initiale (Quick Scan)
**Checklist 30 minutes :**
- ✅ Statut juridique (SIREN vérifié)
- ✅ Type procédure + délais
- ✅ CA estimé (last known)
- ✅ Secteur + localisation
- ✅ Effectif estimé

**Scoring préliminaire :**
- Calcul score M&A rapide (basé sur 5 critères)
- Classer : A (>70), B (50-70), C (<50)

**Output :**
- Fiche deal 1 page
- Prioritisation dans pipeline

### 1.3 Validation interne
**Review :**
- Appel 15 min avec senior M&A
- Validation scoring préliminaire
- Go/no-go pour due diligence

## Phase 2 : Due Diligence Accélérée (J+7 à J+21)

### 2.1 Documents clés (48h)
**Documents à collecter :**
- Jugement d'ouverture procédure
- Dernier bilan/compte de résultat
- Liste créanciers
- Contrats clients >50k€
- Contrats fournisseurs clés
- Contrat de bail commercial
- Brevets/marques

**Outils :**
- Template demande documents standardisée
- NDA automatique (DocuSign)
- Cloud storage sécurisé (SharePoint)

### 2.2 Analyse sectorielle (J+10)
**Focus :**
- Tendances marché
- Positionnement concurrentiel
- Réglementation applicable
- Potentiel de restructuration

**Sources :**
- Rapports sectoriels
- Données INSEE
- Benchmarking concurrents
- Expert sectorial interne

### 2.3 Scoring détaillé (J+14)
**Variables complémentaires :**
- Tendance CA 3 ans
- Marge récente
- Dettes structurelles
- Actifs sous-valorisés
- Risques spécifiques sector

**Output :**
- Score M&A final (0-100)
- Classe de risque (Premium/High/Standard/Low)
- Deal memo 5 pages max

## Phase 3 : Matching Acquéreurs (J+21 à J+35)

### 3.1 Ciblage repreneurs
**Critères de matching :**
- Secteur d'expérience
- Capacité financière
- Expertise opérationnelle
- Timeline d'acquisition

**Base de données :**
- 200+ repreneurs qualifiés
- Score de matching (75%+ match)
- Historique deals précédents

### 3.2 Approche personnalisée
**Script par type :**
- E-commerce : Script repreneurs digital
- Industrie : Script repreneurs opérationnels  
- Commerce : Script investisseurs
- Fonds : Deal pitch financier

**Canaux :**
- LinkedIn InMail (priorité)
- Réseau événementiel
- Partenariats sectoriels

### 3.3 NDA & accès données
**Processus :**
- NDA électronique (DocuSign)
- Accès deal room (SharePoint)
- Présentation conférence call

## Phase 4 : Due Diligence Avancée (J+35 à J+56)

### 4.1 Technical DD (optionnel)
- Visite site
- Vérification actifs
- Management interviews
- Due diligence opérationnelle

### 4.2 Financial DD
- Audit financier indépendant
- Valorisation DCF
- Comparables sectoriels
- Analyse synergies

### 4.3 Legal DD
- Analyse contrats
- Litiges en cours
- Conformité sector
- Structuration juridique

## Phase 5 : Closing (J+56 à J+84)

### 5.1 Négociation
- Term sheet préliminaire
- Due diligence finale
- Structuration deal

### 5.2 Closing
- Signature acte
- Paiement
- Transition
- Post-closing review

## Metrics de performance

### Temps moyen par phase
| Phase | Cible | Actuel |
|-------|--------|--------|
| Qualification | 7j | 6j |
| Due diligence | 14j | 12j |
| Matching | 14j | 11j |
| Closing | 28j | 25j |
| **Total** | **63j** | **54j** |

### Taux de conversion
- **Qualification** : 85% → Pipeline
- **Due diligence** : 65% → Matching
- **Matching** : 40% → Closing
- **Overall** : 22% → Deal clos

### Indicateurs clés
- **Deal flow** : 8 deals/mois
- **Temps deal** : 54 jours
- **Success rate** : 22%
- **Pipeline value** : 42M€

## Outils technologiques

### Automatisation
- Zapier pour notifications
- Python scripts pour scraping
- AI scoring automatisé
- Template管理系统

### Collaboration
- Slack pour communications
- SharePoint pour documents
- Figma pour présentations
- Notion pour suivi deals

## Related
- [[brantham/patterns/scoring-predictif-m-a]]
- [[brantham/patterns/due-diligence-checklist]]
- [[brantham/knowledge/skills/process-optimization]]
- [[brantham/deals/_MOC]]

---

**Utilité** : Workflow optimisé réduisant le temps de deal de 63 à 54 jours avec taux de conversion amélioré.

**Prochaine action** : Tâche 5 - Knowledge base 10 articles distressed