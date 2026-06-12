---
type: pattern
project: brantham
created: 2026-06-12
component: m&a-scoring
category: evaluation-framework
updated: 2026-06-12
---

# Template de Scoring M&A Distressed

Ce template permet d'évaluer rapidement des cibles de cession en utilisant le système de scoring 9D de Brantham Partners.

## Quick Score Calculator

| Composante | Poids | Score (0-100) | Pondéré | Notes |
|------------|-------|---------------|---------|-------|
| **1. Taille** | 30% | | | CA + Effectif + Total Bilan |
| **2. Secteur** | 25% | | | Code NAF attractivité |
| **3. Procédure** | 20% | | | Type + Stade procédure |
| **4. Fraîcheur** | 5% | | | <30j = 100, >180j = 0 |
| **5. Localisation** | 5% | | | Bassin économique |
| **6. Effectif** | 5% | | | 10-100 salariés optimal |
| **7. AFDCC** | 5% | | | Score défaut disponible |
| **8. Mandataire** | 3% | | | Track record cessions |
| **9. Actifs** | 2% | | | Qualité actifs identifiés |
| **TOTAL** | **100%** | | **/100** | |

## Seuils de Décision Immédiate

- **75+** → ✅ **URGENT** - Lancer pipeline complet maintenant
- **60-74** → 🚀 **LAUNCH** - Lancer pipeline standard
- **50-59** → 👀 **WATCH** - Surveillance, attente
- **<50** → 📦 **ARCHIVE** - Clôturer la piste

## Checklist Évaluation Rapide

### 📊 Données Clés à Vérifier
- [ ] SIREN valide et date immatriculation
- [ ] Code NAF et secteur d'activité
- [ ] Chiffre d'affaires (dernier exercice)
- [ ] Effectif salarié
- [ ] Type et date procédure judiciaire
- [ ] Mandataire judiciaire en charge
- [ ] Actifs identifiables (immobilier, machines)

### ⚠️ Signaux d'Alerte Rouge
- [ ] Procédure ouverte > 6 mois
- [ ] CA décroissant > 3 années consécutives
- [ ] Effectif < 5 salariés
- [ ] Secteur en déclin structurel
- [ ] Pas d'actifs tangibles identifiables

### 🎯 Criteres Prioritaires (Poids élevés)
1. **Taille** : PME 1-50M€ CA (optimal)
2. **Secteur** : Industrie/Agro > Services/Commerce
3. **Procédure** : Liquidation Judiciaire > Redressement

## Estimation Valeur d'Entreprise (VE)

| Méthode | Formule | Usage |
|---------|---------|-------|
| **Multiples sectoriels** | CA × multiple | Valeur opérationnelle |
| **Actifs nets** | Total Bilan - Dettes | Valeur liquidative |
| **DCF simplifié** | FCF année 1 / (r+g) | Potentiel restructuration |

### Multiples Sectoriels Courants
- Industrie : 2-4x CA
- Services : 1-3x CA  
- Commerce : 1.5-2.5x CA
- Tech : 3-6x CA (si IP)

## Probabilité de Cession (Cox Model)

| Horizon | Probabilité | Action |
|---------|-------------|--------|
| 3 mois | | Surveillance rapprochée |
| 6 mois | | Préparer approche acquéreurs |
| 12 mois | | Plan à long terme |

## Score Exemple : MLD Multi-Loisirs Distribution

| Composante | Score | Pondéré | Notes |
|------------|-------|---------|-------|
| Taille | 70 | 21 | CA 15M€, 45 salariés |
| Secteur | 65 | 16.25 | Distribution (NAF 46.90) |
| Procédure | 80 | 16 | LJ récente < 30j |
| Fraîcheur | 90 | 4.5 | Jugement 15j |
| Localisation | 75 | 3.75 | Région Grand Est |
| Effectif | 60 | 3 | 45 salariés (ok) |
| AFDCC | 70 | 3.5 | Score défaut modéré |
| Mandataire | 85 | 2.55 | Track record bon |
| Actifs | 50 | 1 | Peu d'actifs tangibles |
| **TOTAL** | | **71.05** | **→ LAUNCH** |

## Actions Déclenchées par Score

### Score ≥ 75 (URGENT)
- [ ] Analyst : Complète analyse dans 4h
- [ ] Writer : Teaser dans 24h
- [ ] Hunter : Liste acheteurs dans 48h

### Score 60-74 (LAUNCH)
- [ ] Analyst : Analyse standard 48h
- [ ] Writer : Teaser dans 3 jours
- [ ] Hunter : Matching acheteurs 5 jours

### Score < 60 (WATCH/ARCHIVE)
- [ ] Mise en surveillance weekly
- [ ] Réévaluation mensuelle
- [ ] Archivage si score < 50 > 3 mois

## Related
- [[brantham/_MOC]]
- [[vault/_system/MOC-patterns]]
- [[brantham/data-pipeline/scoring|Scoring System Reference]]