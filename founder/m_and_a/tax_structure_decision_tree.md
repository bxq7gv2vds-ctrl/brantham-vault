---
name: tax-structure-decision-tree
description: Asset deal vs share deal — French & US tax implications, timing, earnout impacts
type: framework
---

# Tax Structure Decision Tree — Asset vs Share Deal

**Utilisation** : Avec ton conseil fiscal (expert-comptable / tax lawyer). Ne pas décider seul.

**Contexte français** : Sell-side (founder) tax varies wildly by structure. Can save €100K+ with right choice.

---

## Decision Tree (Interactive)

```
START HERE
├─ Où est votre siège? (FR / US / EU / autre?)
│
├─ SI FRANCE:
│  ├─ Part personnelle (vous = > 50% du capital?)
│  │  ├─ OUI → ARTICLE 150-0 B ter (plus-value long terme)
│  │  │   └─ Asset deal?
│  │  │       ├─ OUI: 19% tax (+ 3.8% prélèvements sociaux) = 23% total
│  │  │       └─ NON: Share deal = exempt si respectes conditions (< 75K/an)
│  │  └─ NON → Régime des sociétés (impôt sur les sociétés, puis dividende)
│  │
│  └─ EBITDA positive?
│     ├─ OUI: Asset deal permet déduction amortissements post-vente
│     └─ NON: Share deal mieux (pas de passif à reprendre)
│
├─ SI US:
│  ├─ S-corp ou C-corp?
│  │  ├─ C-corp: Double tax (corp + personal). Asset deal worse. Go share deal + 338h election.
│  │  └─ S-corp: Pass-through. Asset deal OK if buyer can depreciate.
│  │
│  └─ Earn-out?
│     ├─ OUI: Share deal (plus flexibility on timing)
│     └─ NON: Asset deal (buyer wants cost basis step-up)
│
└─ SI UE/AUTRE:
   └─ Parlez avec tax advisor (varies by country)
```

---

## Simplified Comparison Table

| Factor | Asset Deal | Share Deal | Winner |
|--------|------------|-----------|--------|
| **French tax (perso)** | 23% (articles 150-0 B ter) | 0-45% (depends on status) | Asset ✓ |
| **US tax (if C-corp)** | Double tax | Double tax + 338h | Tie (both bad) |
| **Buyer preference** | Wants deductions | Wants clean slate | Varies |
| **Earnout feasibility** | Harder (reps tied to assets) | Easier (tied to company performance) | Share ✓ |
| **Seller liability post-close** | Lower (few reps) | Higher (all reps) | Asset ✓ |
| **Speed to close** | Slower (asset transfer + tax filings) | Faster (share transfer) | Share ✓ |
| **Working capital adjustments** | Rare | Standard | Asset ✓ |
| **Debt assumption** | Buyer assumes specific debts | Seller liable | Asset ✓ |
| **Employee contracts** | Buyer must agree to TUPE | Automatic | Asset ✓ |

---

## Real Scenarios

### Scenario 1: French SaaS Founder, Profitable

**Profile** : €500K ARR, €50K EBITDA/year, you own 100%.

**Asset deal** :
- Gain (€250K − €100K cost base) = €150K
- Tax: €150K × 23% = €34.5K
- **Take-home: €215.5K**

**Share deal** (if structured as personal sale) :
- Same gain = €150K
- Tax: Depends on holding period. If 5+ years, could be 0% under certain conditions.
- **Take-home: €250K (if exempt) vs €150K (if taxed at 45%)**

**→ Decision** : Share deal if you qualify for exemption. Otherwise asset deal.

---

### Scenario 2: US SaaS, C-Corp, Buyer Wants Deductions

**Profile** : $2M ARR, C-corp, buyer wants to depreciate software + goodwill.

**Share deal + Section 338(h)(10) election** :
- Buyer gets cost basis step-up (can depreciate intangibles)
- Seller pays capital gains tax (15% qualified)
- **Cleaner, faster**

**Asset deal** :
- Buyer gets immediate deductions
- Seller pays capital gains + recapture (25% on goodwill depreciation)
- **More complex, slower**

**→ Decision** : Share deal with 338(h)(10) election.

---

### Scenario 3: Multiple Earnouts (Retention Risk)

**Profile** : Seller wants to stay 2 years, earn-out tied to customer retention.

**Asset deal** :
- Representations & warranties tied to specific assets (customer lists, IP)
- If earn-out misses, seller liable for reps breach
- **High risk for seller**

**Share deal** :
- Earn-out tied to company KPIs (revenue, retention, margins)
- Cap seller liability separately from earn-out
- **Better for seller with earnout**

**→ Decision** : Share deal with earn-out structure.

---

## Key Questions to Ask Your Tax Advisor

1. **"What's my effective tax rate under asset deal vs share deal in [my jurisdiction]?"**
   - Get numbers, not opinions.

2. **"If I structure this as X, can the buyer claim 338(h)(10) / similar cost basis adjustment?"**
   - Affects buyer willingness to close.

3. **"What's the impact of earn-outs on my tax filing? Do they count as capital gains or income?"**
   - Can swing your rate 10-20%.

4. **"Are there any one-time exemptions I might qualify for (holding period, job creation, etc.)?"**
   - Worth asking in France, Canada, Australia.

5. **"What if the deal closes Jan 1 vs Dec 31? Tax year impact?"**
   - Often overlooked, can save €5-10K.

---

## Timeline Impact

| Structure | French tax filing | Earnout timing | Goodwill deduction |
|-----------|------------------|-----------------|-------------------|
| **Asset deal** | Day 1 (immediate income) | Counted year-by-year | Buyer depreciates |
| **Share deal** | Year of sale (delayed if close late) | Easier to defer into next year | Buyer's problem |

**→ Recommendation** : If you expect earn-out to hit in year 2-3, negotiate share deal + spread earn-out over time = lower tax hit per year.

---

## Decision Framework (TL;DR)

```
IF French + profitable + own 100% → Asset deal (likely 23% tax)
IF US C-corp → Share deal with 338(h)(10)
IF earnout involved → Share deal (more flexible)
IF buyer wants clean liability → Asset deal
IF you want speed → Share deal
IF you want full tax optimization → Talk to big 4 firm (spend €5K, save €50K+)
```

---

## Next Steps

1. **Consult** : Meet with tax advisor (expert-comptable or international firm)
2. **Model** : Use real financials to calculate take-home under both scenarios
3. **Negotiate** : Tell buyer your structure preference early (affects their offer)
4. **Document** : Get written tax opinion (useful for earnout disputes later)

---

## Resources

- **France** : Ordre des Experts-Comptables (find advisor: oec.fr)
- **US** : Tax attorney specializing in M&A (search: "Section 338(h)(10) specialist")
- **EU** : KPMG / Deloitte M&A tax guides (free downloads)
