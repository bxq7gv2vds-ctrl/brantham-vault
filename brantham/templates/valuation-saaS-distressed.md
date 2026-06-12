---
type: template
category: valuation
created: 2026-06-12
updated: 2026-06-12
---

# Framework de Valorisation - Cibles Tech SaaS Distressed

*Methodologie spécifique pour valorisation des entreprises SaaS en difficulté financière*

## Instructions d'utilisation

Appliquer ce framework après la phase de due diligence technique et validation du modèle commercial. Pondérer les multiples sectoriels en fonction du niveau de détresse.

```yaml
# Configuration de la cible
deal_slug: "[slug-du-deal]"
entreprise: "[Nom entreprise]"
secteur: "SaaS/[SOUS-SECTEUR]"
phase_distress: "Early □ | Mid □ | Late □"
date_donnees: "YYYY-MM-DD"
evaluator: "[Nom de l'évaluateur]"
```

---

## Méthodes de Base (1ère génération)

### A. Multiple de Chiffre d'Affaires (Revenue Multiple)

| Segment SaaS | Multiple indicatif | Hypothèses |
|--------------|-------------------|------------|
| **Enterprise SaaS** | 3-6x | Contrats >2ans, revenus récurrents |
| **Mid-Market SaaS** | 2-4x | Mix de contrats récurrents/ponctuels |
| ** SMB SaaS** | 1-3x | Haute rotation, rétention faible |
| **Niche SaaS** | 4-8x | Dominance segment, barrières fortes |

**Ajustements détresse**:
- **Early distress** (détection précoce) : ×0.9-1.0
- **Mid distress** (croissance stoppée) : ×0.7-0.9  
- **Late distress** (churn élevé) : ×0.5-0.7

**Formule**:
```
Valeur = (CA N-1 + MRR × 12 × ratio_croissance) × multiple_ajuste
```

### B. Multiple de MRR (Monthly Recurring Revenue)

| Taux de Croissance | Multiple MRR | Facteurs Correctifs |
|-------------------|--------------|-------------------|
| **>50% croissance** | 8-12x | ×0.8 détresse |
| **20-50% croissance** | 6-9x | ×0.9 détresse |
| **0-20% croissance** | 4-7x | ×1.0 détresse |
| **Déclin négatif** | 2-4x | ×0.6 détresse |

**Formule**:
```
Valeur = MRR actuel × multiple × (1 + taux_croissance/2)
```

### C. Approche par la Valeur à Vie Client (LTV)

| Segment | LTV moyen | Acquisition (CAC) | Ratio LTV/CAC | Valeur |
|---------|-----------|-------------------|---------------|---------|
| **Enterprise** | 50-150K€ | 20-80K€ | 2.5-3x | LTV × base_clients |
| **Mid-Market** | 10-50K€ | 5-20K€ | 2-3x | LTV × base_clients |
| **SMB** | 2-10K€ | 1-5K€ | 1-2x | LTV × base_clients |

**Ajustement détresse**:
- **Churn >10%** : ÷1.5
- **CAC élevé** : ÷1.3
- **Retention <80%** : ÷1.2

---

## Méthodes Avancées (2ème génération)

### D. Modèle DCF (Discounted Cash Flow) Détress

**Hypothèses spécifiques**:
- Croissance ajustée : -20% à +5% (vs 15-30% normal)
- Taux d'actualisation : 25-35% (vs 15-25% normal)
- Période de prévision : 3-5 ans (vs 5-10 ans normal)

**Flux de trésorerie ajustés**:
```
FCF = (Chiffre d'affaires - Coût d'acquisition client - Coûts fixes) × (1 - taux_detresse)
```

**Facteurs de détresse**:
- Incertitude juridique : +5-10%
- Risque client : +5-15%
- Rotation management : +3-8%

### E. Comparaison avec Transactions Similaires

| Transaction Date | Cible | Multiple | Caractéristiques | Différenciel |
|-----------------|-------|----------|----------------|--------------|
| **[Transaction]** | [Nom] | [Multiple] | [Description] | [Ajustement] |
| **[Transaction]** | [Nom] | [Multiple] | [Description] | [Ajustement] |
| **[Transaction]** | [Nom] | [Multiple] | [Description] | [Ajustement] |

**Moyenne sectorielle ajustée**: _____________

### F. Multiple d'EBITA (Loss-Adjusted)

Pour les SaaS débiteurs (perte nette):
```
Multiple = Multiple_sain × (1 - ratio_perte) + multiple_distressed × ratio_perte
```

**Exemple**:
- Sain : 8x EBITA
- Distressed : 3x EBITA  
- Perte EBITA : 40% du CA
- Multiple final : (8 × 0.6) + (3 × 0.4) = 6.0x

---

## Méthodes Spécifiques (3ème génération)

### G. Valeur des Données et des Actifs Digitaux

#### Données Clients
- **Valeur des données** : 500€-5K€ par client actif
- **Base de données** : 10K€-500K€ (selon taille et qualité)
- **Historique d'utilisation** : 3-12 mois de données = +20-50%

#### Actifs Technologiques
- **Code source** : 50-300K€ (selon complexité)
- **Infrastructure** : 10-100K€ (selon scale)
- **Brevets/IP** : 10K€-2M€ (selon innovation)
- **Intégrations partenaires** : 5-50K€

#### Portée et Scalabilité
- **APIs publiques** : +10-30K€
- **SDKs disponibles** : +5-20K€
- **Écosystème développeurs** : +10-100K€
- **Intégrations marketplace** : +5-50K€

### H. Valeur du Passif Technique

**Tech debt**:
- **MVP** : -10-20% de la valeur
- **Product-market fit** : -5-10%
- **Tech stack désuète** : -20-50%
- **Scalability limitée** : -15-30%

**Obligations techniques**:
- **Refonte nécessaire** : 50-200K€
- **Modernisation stack** : 100-500K€
- **Sécurité à jour** : +10-20%
- **Documentation complète** : +5-15%

---

## Facteurs Correctifs Multiples

### I. Correctifs Sectoriels

| Facteur | Impact | Description |
|---------|--------|-------------|
| **Concentration client > 20%** | -20% à -40% | Risque dépendance |
| **CAC > LTV** | -30% à -50% | Modèle non rentable |
| **Churn > 15%** | -25% à -45% | Rotation excessive |
| **Durée de cycle > 18 mois** | -15% à -25% | ROI trop long |
| **GTM (Go-to-Market)** | -10% à -20% | Positionnement faible |

### J. Correctifs de Détresse

| Stade | Impact | Actions Correctives |
|-------|--------|---------------------|
| **Early (Early Warning)** | -10% à -25% | Restructuration rapide possible |
| **Mid (Cash Crunch)** | -25% à -50% | Intervention nécessaire |
| **Late (Insolvency)** | -50% à -80% | Liquidation probable |

### K. Correctifs de Maturité

| Étape | Multiple | Caractéristiques |
|-------|----------|-----------------|
| **Startup** (0-3 ans) | 1-4x | Preuve de concept, learning phase |
| **Growth** (3-7 ans) | 4-8x | Traction établie, scale |
| **Mature** (7+ ans) | 6-12x | Établissement, stabilisé |

---

## Matrice de Scoring Valorisation

### Analyse des Critères Clés

| Critère | Poids | Score | Pondéré | Commentaires |
|--------|-------|-------|---------|--------------|
| **MRR & Croissance** | 30% | /10 | /3.0 | _____________ |
| **Churn & Retention** | 25% | /10 | /2.5 | _____________ |
| **CAC & Unit Economics** | 20% | /10 | /2.0 | _____________ |
| **Tech Stack** | 15% | /10 | /1.5 | _____________ |
| **Market Position** | 10% | /10 | /1.0 | _____________ |
| **TOTAL** | 100% | | **/10.0** | _____________ |

### Multiples Finaux (Guide Indicatif)

| Score Total | Multiple Indicatif | Valeur | Recommandation |
|-------------|-------------------|--------|----------------|
| **9-10** | 8-12x | Valeur pleine | Acquisition rapide |
| **7-8** | 6-8x | Valeur bonne | Deal à suivre |
| **5-6** | 4-6x | Valeur moyenne | Conditions nécessaires |
| **3-4** | 2-4x | Valeur réduite | Risques importants |
| **<3** | <2x | Valeur liquidative | À éviter ou restructuring |

---

## Synthèse Finale

### Méthodes Retenues (Top 3)

1. **MRR Adjusted** : _____________ × MRR = _____________
2. **Revenue Multiple Sectoriel** : _____________ × CA = _____________
3. **LTV/CAC Portfolio** : _____________ × base_clients = _____________

**Valeur médiane** : _____________

**Range de valorisation** : _____________ à _____________

**Points de vigilance** :
1. _____________
2. _____________
3. _____________

**Conditions suspensives** :
1. _____________
2. _____________
3. _____________

**Next steps** :
1. _____________
2. _____________
3. _____________

---

## Related
- [[brantham/knowledge/finance/valuation]]
- [[brantham/deals/template]]
- [[brantham/knowledge/market/saaS-trends]]
- [[brantham/knowledge/finance/unit-economics]]