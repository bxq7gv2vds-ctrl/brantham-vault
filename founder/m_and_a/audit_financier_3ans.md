---
name: audit_financier_3ans
description: Normalisation financière 3 années (revenus, EBITDA, ajustements)
metadata:
  type: template
  created: 2026-06-12
---

# Audit Financier 3-Ans — Template Normalisation

## **Section 1 : Revenus Normalisés**

| Année | ARR Brut | Ajustements | ARR Normalisé | Notes |
|-------|----------|-------------|-----------------|-------|
| Y-2   | $        | $           | $               | Inclure upsells, churn estimé |
| Y-1   | $        | $           | $               | |
| Y     | $        | $           | $               | |

**Ajustements communs :**
- Revenus non-récurrents (setup fees, services) → **exclure**
- Contrats annulés mid-year → **extrapoler perte complète**
- Nouvelles acquisitions (si < 6 mois) → **annualiser**
- Commissions ou discounts maison → **normaliser**

---

## **Section 2 : EBITDA Ajusté**

| Catégorie | Y-2 | Y-1 | Y | Notes |
|-----------|-----|-----|---|-------|
| **Revenus** | | | | |
| Cost of Goods Sold (COGS) | | | | Hosting, support, delivery |
| **Gross Margin** | | | | Target: 60-80% SaaS |
| **Operating Expenses** | | | | |
| Sales & Marketing | | | | % Revenus, trend? |
| R&D | | | | Produit, tech debt |
| G&A | | | | Admin, finance, legal, HR |
| **Operating Income (EBIT)** | | | | |
| D&A | | | | Ajouter back |
| **EBITDA** | | | | |
| Add-backs (déductions) | | | | Voir ci-dessous |
| **Adjusted EBITDA** | | | | **Clé pour valuation** |

### **Add-backs typiques :**
- Rémunération du fondateur excessif
- Dépenses non-récurrentes (litigation, restructure)
- Stock-based comp (si acquéreur embauche l'équipe)
- Rent exceptionnelle (loyer anormalement bas/haut)
- Voyage, voiture, insurance perso du fondateur
- Consulting, advisory fees payés à insiders

**Add-backs REJETÉS par acheteurs :**
- "Efficiencies" hypothétiques post-deal
- Coûts d'intégration future
- Dépenses qui ne sont PAS vraies (fiction accounting)

---

## **Section 3 : Burn Rate & Cash Metrics**

| Métrique | Y-2 | Y-1 | Y | Trend |
|----------|-----|-----|---|-------|
| Net Burn (si applicable) | $ | $ | $ | Croissance ou profitabilité? |
| Months of Runway | | | | Si negative: critère disqualifiant |
| CAC Payback | | | | Mois pour récupérer coût acquisition |
| Cash Conversion | | | | ARR → Cash (crédit clients?) |

---

## **Section 4 : Growth Profile**

| Année | YoY Growth | Notes |
|-------|-----------|-------|
| Y-2 → Y-1 | % | Accélération ou ralentissement? |
| Y-1 → Y | % | |
| Forecast Y+1 | % | Basé sur pipeline, contrats signés |

**Rule of 40:** Growth% + EBITDA Margin% ≥ 40 = forte acquisition

---

## **Section 5 : Ajustements spécifiques à ton biz**

### Pour **Alliance Coiffure** (si SaaS):
- [ ] Revenus SaaS vs services professionnels (séparer)
- [ ] Contrats de coiffeurs → churn trimestriel? Annuel?
- [ ] Produits/packages à la carte vs abonnement → récurrence réelle
- [ ] Saison? (été < hiver pour coiffure?) → saisonnalité

### Pour **LAT-ARB Bot** (si service/logiciel trading):
- [ ] Revenus: frais de performance, accès API, données?
- [ ] Utilisateurs actifs vs inactifs
- [ ] P&L du bot lui-même (costs vs net fees)

---

## **À faire avant valuation :**
1. [ ] Revoir avec comptable: tous ajustements justifiés
2. [ ] Benchmark: ton EBITDA% vs industrie (SaaS 40-50% médian)
3. [ ] Red flags: **si EBITDA ajusté < 10% revenus = difficile à vendre**
4. [ ] Décompiler la croissance: organique vs acquisition vs prix increase?

---

## **Livrable final pour dataroom :**
- Fichier: `Financial_Statements_Normalized_3Y.xlsx` 
- Contient: P&L brut, adjustments schedule, EBITDA calc, summary page
## Related
