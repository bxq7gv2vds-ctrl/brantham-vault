---
name: customer_concentration_mapping
description: Analyse top-20 clients, concentration risk, churn, LTV pour DD
metadata:
  type: template
  created: 2026-06-12
---

# Cartographie Clients Top-20 — Due Diligence Ready

## **Pourquoi? (Acheteurs demandent TOUJOURS)**
- **Red flag #1:** Top-1 client = X% revenue → acquéreur baisse offre 30-50%
- **Red flag #2:** Churn élevé ou imprévisible → valuation baisse 20%
- **Opportunité:** Si clients heureux + retenus → prime de valuation +10-15%

---

## **Template : Top-20 Clients**

| Rank | Client Nom | ARR ($k) | % Total | Contrat Début | Fin | Churn Risk | LTV ($k) | Gross Margin % | Notes |
|------|-----------|----------|---------|---------------|-----|-----------|---------|---|---------|
| 1 | **Client A** | 150 | 18% | 2022-01 | 2026-01 | LOW | 400 | 75% | Strategic, renewal certain |
| 2 | **Client B** | 120 | 15% | 2023-06 | 2026-06 | MEDIUM | 250 | 70% | Pilot → expansion potential |
| 3 | **Client C** | 95 | 12% | 2021-03 | 2025-03 | HIGH | 180 | 65% | Exploring alternatives (watch) |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 20 | **Client T** | 18 | 2% | 2023-12 | 2026-12 | LOW | 50 | 60% | Small, stable |
| **Total Top-20** | | **~750** | **~93%** | | | | | | **Concentration = concern?** |

---

## **Section 2 : Concentration Risk Analysis**

| Métrique | Valeur | Sain? | Acquéreur réaction |
|----------|--------|-------|-------------------|
| Top-1 Client % | **X%** | <15% bon, >25% red flag | Si >20%: -30% offre |
| Top-3 Clients % | **X%** | <40% bon, >50% problème | >50% = due diligence intensive |
| Top-5 Clients % | **X%** | <60% bon, >70% concentration | >70% = earnout + holdback |
| Herfindahl Index | | <0.10 sain | <0.15 acceptable |
| Customer Concentration Score | **X/10** | >7 = problème | <5 = premium + |

**Calcul Herfindahl:** Σ(% client)²
- <0.10 = diversifié ✅
- 0.10-0.15 = acceptable
- >0.15 = concentrated ⚠️

---

## **Section 3 : Churn & Retention**

| Cohort | Customers Started | Year 1 Retention | Year 2 Retention | Year 3 Retention | NRR % |
|--------|------------------|------------------|------------------|------------------|-------|
| **Vintage 2023** | 15 | 73% | 55% | 40% | 115% |
| **Vintage 2022** | 22 | 68% | 48% | | 108% |
| **Vintage 2021** | 18 | 71% | | | 112% |

**Key questions :**
- Churn reason #1? (Feature gap? Price? Market shift? Bad fit?)
- Downgrade vs. full churn ratio?
- If churned: sont-ils chez concurrent?

---

## **Section 4 : LTV Analysis**

**LTV = (Gross Margin $ / Monthly Churn %) × Customer Lifespan (months)**

| Client | Initial ARR | Gross Margin % | Upsell/Expansion | Expected Lifespan | **LTV** | CAC | LTV/CAC |
|--------|----------|---|---|---|---|---|---|
| A | $150k | 75% | +15%/yr | 60mo | $650k | $20k | 32x ✅ |
| B | $120k | 70% | +5%/yr | 36mo | $280k | $15k | 19x ✅ |
| C | $95k | 65% | 0% | 24mo | $120k | $25k | 4.8x ⚠️ |

**Acquéreur benchmark:** LTV/CAC > 3 = bon, >5 = excellent

---

## **Section 5 : Contrats & Terms à Valider**

Pour **chaque** top-5 client:
- [ ] Contrat signé: date, durée, renewal clause
- [ ] Auto-renew? Ou manual? (crucial pour retention)
- [ ] Clausule de changement de contrôle? (Buyer doit assumer?)
- [ ] Prix locked-in ou augmentation annuelle?
- [ ] Support level inclus?
- [ ] Données client critiques? (GDPR, data portability?)

**Template checklist:**
```
Client A:
- Contract date: ________
- Term: _____ months
- Auto-renew: YES / NO
- Change of control clause: YES / NO (risk?)
- Renewal likelihood: ____%
- Owner contact: ___________
```

---

## **Section 6 : Customer Reference Calls (Pour acquéreur)**

Sélectionner 5 clients **heureux** (mélange: grand, moyen, petit):
1. **Référent 1:** Large account, strategic partnership
2. **Référent 2:** Medium account, good growth
3. **Référent 3:** Small account, happy user
4. **Référent 4:** Old customer, 3+ years
5. **Référent 5:** Bonus: churn risk (honest!), why hesitant?

**Script de consentement:**
> "Merci pour la relation. Pour faciliter un potentiel changement de propriétaire, un acquéreur voudrait t'appeler (15min) pour vérifier que le service continuera à marcher pour toi. OK?"

---

## **Red Flags à détecter AVANT:**

- ❌ Top client = 35% revenue, contrat expire dans 6 mois, pas signé renewal
- ❌ Churn = 10% QoQ (industry median 3-5%)
- ❌ Tous les clients sont via **une** autre plateforme (ex: intégration unique AWS)
- ❌ Client dominant = fournisseur/partenaire de l'acheteur (conflit)
- ❌ Produit = feature de leur système, pas business indépendant

---

## **Livrable final pour dataroom:**
- **File 1:** `Customer_List_Top20_Anonymized.xlsx` (revenus, dates, risk)
- **File 2:** `Customer_Concentration_Analysis.pdf` (graphs, HHI, cohort retention)
- **File 3:** `Reference_Call_List.docx` (5 noms, contact, topic)
- **File 4:** `Churn_Analysis_Cohort.xlsx` (vintage cohorts, NRR)

---

## **À faire avant donnees à buyer:**
1. [ ] Anonymize clients si demandé (Client A, B, C) ou révéler? → Décider avec advisor
2. [ ] Vérifier contrats: aucune clause de consentement nécessaire avant DD
3. [ ] Préparer story: pourquoi top-3? Comment les retenir post-deal?
