---
name: m-a-valuation-multiples
description: Modèle d'évaluation utilisant les multiples sectoriels courants pour les transactions M&A
metadata:
  type: pattern
  date: 2026-06-12
  category: m-a
  project: founder
---

# Modèle d'Évaluation M&A - Multiples Sectoriels

## Introduction aux Multiples d'Évaluation

Les multiples sont des ratios qui comparent la valeur d'une entreprise à une mesure financière spécifique, permettant des comparaisons rapides entre entreprises et secteurs.

## Multiples Courants par Secteur

### 🏭 SaaS & Software
**Multiples Clés:**
- **Revenue Multiple**: 6-12x (dépend de la marge)
- **EBITDA Multiple**: 20-40x (high growth)
- **Revenue EBITDA**: 1.5-3.0x
- **ARR Multiple**: 10-20x (annual recurring revenue)

**Facteurs d'Ajustement:**
- Taux de croissance (30%+ → +50% de la multiple)
- Taux de rétention (>90% → +30%)
- LTV/CAC ratio (>3x → +40%)
- Marge brute (>80% → +25%)

### 🏦 FinTech & Fintech
**Multiples Clés:**
- **Revenue Multiple**: 4-10x
- **Profit Multiple**: 15-30x
- **Loan Book Multiple**: 1.5-3.0x
- **Customer Acquisition Cost**: 2-4x LTV

**Facteurs d'Ajustement:**
- Regulation compliance (+20% si solide)
- User growth rate (mois/mois)
- NPS score (>50 → +30%)
- Platform scalability

### 🛍️ E-commerce & Retail
**Multiples Clés:**
- **Revenue Multiple**: 0.5-3.0x
- **EBITDA Multiple**: 8-15x
- **Gross Multiple**: 0.3-1.5x
- **Customer Value Multiple**: 200-500€ par client

**Facteurs d'Ajustement:**
- Marges brutes (>25% → +20%)
- Customer acquisition cost (<100€ → +25%)
- Repeat purchase rate (>40% → +30%)
- Inventory turnover (>6x → +15%)

### 🏥 Healthcare & MedTech
**Multiples Clés:**
- **Revenue Multiple**: 3-8x
- **EBITDA Multiple**: 12-25x
- **Patient/Subscriber Multiple**: 1,000-5,000€
- **Market Share Multiple**: 0.5-2.0x

**Facteurs d'Ajustement:**
- Regulatory approvals (+30% si obtenues)
- IP portfolio strength
- Clinical trial phase (phase III → +50%)
- Reimbursement coverage (>80% → +40%)

### 🎮 Gaming & Entertainment
**Multiples Clés:**
- **Revenue Multiple**: 4-10x
- **DAU/MAU Multiple**: 10-50€ par utilisateur
- **Gross Margin Multiple**: 15-30x
- **ARPPU Multiple**: 100-500€

**Facteurs d'Ajustement:**
- User engagement metrics (play time >30min/jour → +35%)
- Retention rate (>25% at 30 days → +40%)
- IP value/franchises
- Platform diversification

### 📢 Marketing & AdTech
**Multiples Clés:**
- **Revenue Multiple**: 5-12x
- **EBITDA Multiple**: 18-35x
- **ROAS Multiple**: 3-8x
- **Platform Scale Multiple**: 0.1-1.0x du marché

**Facteurs d'Ajustement:**
- Customer concentration (<20% → +25%)
- Technology moat
- Data quality score
- Client lifetime value

## Méthodologie d'Application

### 1. Sélection des Multiples Pertinents
```python
# Logique de sélection par secteur
def select_multiples(sector):
    if sector == 'SaaS':
        return ['Revenue', 'EBITDA', 'ARR', 'Revenue/EBITDA']
    elif sector == 'E-commerce':
        return ['Revenue', 'EBITDA', 'Gross', 'Customer_Value']
    elif sector == 'FinTech':
        return ['Revenue', 'Profit', 'Loan_Book', 'LTV/CAC']
```

### 2. Calcul de la Valeur d'Entreprise
```markdown
Étapes:
1. Trouver les données financières (revenus, EBITDA)
2. Identifier les multiples sectoriels (benchmarks)
3. Appliquer les multiples pour obtenir fourchette
4. Ajuster pour spécificités de l'entreprise
5. Calculer la valeur nette (après dettes)
```

### 3. Ajustements de Valeur

#### 🟢 Ajustements Positifs
- **Leadership de marché** (+15-30%)
- **Technologie propriétaire** (+20-40%)
- **Diversification clients** (+10-25%)
- **Croissance rapide** (>20% → +30%)
- **Équipe de gestion** (+15-25%)

#### 🔴 Ajustements Négatifs
- **Dépendance client** (>20% → -15%)
- **Technologie dépassée** (-20-35%)
- **Risques réglementaires** (-25-40%)
- **Intégration difficile** (-15-30%)
- **Déclin de croissance** (<5% → -20%)

### 4. Détermination de la Fourchette de Valorisation

#### Étape 1: Multiples de Référence
```markdown
Sources:
- Precedentes transactions similaires
- Analyse des multiples actuels du marché
- Conseil en M&A (Lazard, Goldman Sachs)
- Base de données (PitchBook, Mergermarket)

Exemple SaaS:
- Multiple médian: 8x revenue
- Multiple bas: 6x (croissance <20%)
- Multiple haut: 12x (croissance >40%)
```

#### Étape 2: Application et Ajustement
```markdown
Valeur d'entreprise = Revenus × Multiple × (1 + Ajustements)

Exemple:
- Revenus: €10M
- Multiple de base: 8x
- Ajustements: +20% (technologie) -10% (concentration client)
- Valeur: €10M × 8 × 1.1 = €88M
```

#### Étape 3: Valeur Nette
```markdown
Valeur actionnariaire = Valeur d'entreprise - Dettes nets + Trésorerie

Exemple:
- Valeur d'entreprise: €88M
- Dettes nets: €15M
- Trésorerie: €5M
- Valeur actionnariaire: €78M
```

## Outils de Benchmarking

### 📊 Plateformes de Données
- **PitchBook**: Données transactions multiples
- **Mergermarket**: Transactions récentes par secteur
- **Capital IQ**: Multiples sectoriels
- **S&P Capital IQ**: Analyse comparative

### 🔄 Méthodologie de Benchmarking
1. **Identification des pairs** (même taille, secteur, géo)
2. **Collecte des multiples** (6-12 mois récents)
3. **Calcul des médianes** (sectoriel et par taille)
4. **Analyse des écarts** (pourquoi différences ?)
5. **Application ajustée** (spécificités)

## Modèle d'Évaluation Pratique

### Template Excel/Google Sheets
```markdown
Sections:
- Données financières historiques (3 ans)
- Multiples sectoriels (benchmarks)
- Ajustements spécifiques
- Calcul de la fourchette
- Sensibilité analyse
```

### Calculateur Rapide
```markdown
Input:
- Revenus annuels: €[X]
- EBITDA: €[Y] 
- Multiple sectoriel: [Z]
- Ajustements: ±[A]%

Output:
- Valeur d'entreprise: €[Calculation]
- Valeur par action: €[Result]
- Fourchette: €[Min] - €[Max]
```

## Facteurs Clés de Success

### 🎯 Facteurs Qualitatifs
- **Équipe de management** (expérience, stabilité)
- **Positionnement concurrentiel** (défenses, différenciation)
- **Scalabilité** (modèle économique, infrastructure)
- **Intégration potentielle** (synergies culturelles)

### 📈 Facteurs Quantitatifs
- **Croissance organique** (CAGR >15% idéal)
- **Rentabilité** (EBITDA >20% sauf SaaS)
- **Liquidité** (trésorerie >6 mois de CA)
- **Leverage** (dette <3x EBITDA)

## Limitations des Multiples

### ⚠️ Risques d'Utilisation
- **Cycles de marché** (peuvent être déphasés)
- **Taille d'échantillon** (peut être limité)
- **Spécificités locales** (multiples non applicables)
- **Secteurs en transition** (anciens modèles défaillants)

### 🔍 Bonnes Pratiques
- **Triangulation** (utiliser 3+ méthodes)
- **Contexte** (tendance du marché)
- **Sensibilité** (scénarios pessimiste/réaliste/optimiste)
- **Documentation** (justifier les hypothèses)

## Related
[[_system/MOC-patterns]]
[[founder/_MOC]]

---

## Related
[[_system/MOC-patterns]]
[[founder/_MOC]]