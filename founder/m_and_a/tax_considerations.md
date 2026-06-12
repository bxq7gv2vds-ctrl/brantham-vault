---
name: tax_considerations
description: Fiscalité M&A — optimisation vendeur, earnout, payment structure
metadata:
  type: reference
  format: checklist
  version: 1.0
---

# Tax Planning M&A — Vendeur checklist

**Jurisdiction:** France + EU. Consult local tax lawyer. NOT legal/tax advice.

---

## **BEFORE SIGNING LOI**

- [ ] Consult tax lawyer (not generalist—M&A specialist)
- [ ] Determine gain on sale (FMV - cost basis = taxable gain)
- [ ] Check if eligible for French capital gains tax rates (33.33% vs 45%)
- [ ] Identify if any losses to carry forward (offset gains)
- [ ] Check state/local taxes (if EU cross-border deal)
- [ ] Structure: Asset sale vs. stock sale impact on taxable gain

---

## **KEY TAX IMPACTS (France example)**

### **Capital gains tax (stock sale)**

```
Sale price: €500k
Seller's cost basis: €100k
Gain: €400k

Tax rate (France): 33.33% on capital gains + social contributions (17.2%)
= ~51.5% combined tax

Tax due: €206k
Net proceeds: €294k
```

### **Earnout taxation**

```
Earnout received: €50k / year

Tax treatment: Ordinary income (not capital gain)
= Taxed at marginal rate (45% in France)
+ Social contributions (17.2%)
= ~62% tax

Tax due per €50k earnout: €31k/year
Net: €19k/year
```

**Impact:** Earnout is WORSE tax treatment than base price.
→ Negotiate higher base price, lower earnout (if possible).

---

## **DEAL STRUCTURE OPTIMIZATION**

### **Option A: All cash at close (most tax-efficient)**

```
Structure: €500k cash day 1
Tax: Lump-sum capital gain = €400k × 51.5% = €206k tax
Net proceeds: €294k
```

**Pros:** Immediate liquidity, simple.
**Cons:** High upfront tax bill.

### **Option B: Earnout spread (defers taxes)**

```
Structure: €400k cash + €100k earnout (€50k × 2 years)
Tax:
├─ Year 1 capital gain: €300k × 51.5% = €154.5k
├─ Year 1 earnout: €50k × 62% = €31k
├─ Total Y1 tax: €185.5k (vs €206k upfront)

├─ Year 2 earnout: €50k × 62% = €31k
├─ Total Y2 tax: €31k
└─ Total net proceeds: €294k (same, but deferred)
```

**Pros:** Spreads tax liability, improves cash flow timing.
**Cons:** Earnout is higher tax rate (ordinary income).

### **Option C: Seller note (financing structure)**

```
Structure: €300k cash + €200k seller note (5-year, 3% interest)
Tax treatment:
├─ Principal repayment: NOT taxed (return of capital)
├─ Interest: Ordinary income (€30k/year × 62%)
└─ Capital gain: €300k × 51.5% = €154.5k

Total tax impact: Lower than all-cash, if structured right.
```

**Pros:** Stretches cash over time, reduces immediate tax hit.
**Cons:** Risk if buyer defaults on note.

---

## **OPTIMIZATION STRATEGIES** (per jurisdiction)

### **France-based seller**

```
✓ Claim "small business stock" exemption (if eligible)
  → Potentially 0% tax on first portion (if < €500k gains)
  
✗ Timing doesn't matter (no holding period advantage)

✓ Offset gains with prior-year losses (if any)

✓ Negotiate installment sale (defers gain recognition)
  → If earnout achieves <25% of proceeds, might defer gain
```

### **Luxembourg / Ireland cross-border**

```
✓ Consider IP holding structure pre-sale
  → Separate IP licensing from product
  → IP sale taxed favorably in some jurisdictions
  
⚠️ Consult transfer pricing specialist
```

---

## **CHECKLIST: BEFORE CLOSING**

- [ ] Tax lawyer confirms deal structure
- [ ] Estimate total tax liability (base + earnout)
- [ ] Plan for quarterly estimated tax payments (France)
- [ ] Identify any non-deductible closing costs
- [ ] Confirm earnout tax treatment with accountant
- [ ] Escrow arrangement doesn't trigger early tax
- [ ] Seller note interest rate is reasonable (IRS impute rules)

---

## **EARNOUT vs. BASE PRICE TRADE-OFF**

### **Scenario A: €400k cash + €100k earnout**

```
Taxes: €154.5k (capital gain) + €31k (earnout Y1) = €185.5k
Net Y1: €400k - €154.5k = €245.5k + €19k earnout = €264.5k
```

### **Scenario B: €500k cash**

```
Taxes: €206k (capital gain)
Net: €294k (immediate liquidity)
```

**Outcome:** €294k (all cash, now) vs. €264.5k (first year, with earnout risk).
→ If you need cash, all-cash better. If can wait, earnout fine but risky.

---

## **EARNOUT TAX PITFALL**

Earnout is usually taxed as **ordinary income**, not capital gain.

```
❌ "I'll take lower base price + high earnout"
   → Pay more tax overall

✓ "I want max base price, min earnout"
   → Lower total tax exposure
```

**Exception:** If earnout is contingent on selling company to 3rd party again
→ Might be capital gain. Consult lawyer.

---

## **RED FLAGS (tax nightmare)**

```
❌ Buyer wants "working capital" holdback, then disputes it
   → Can trigger tax on disputed amount

❌ Earnout structured as "profit sharing"
   → May trigger self-employment tax (in EU, social contributions)

❌ Non-compete payment listed as "earnout" (should be separate)
   → Different tax treatment

❌ Foreign buyer, no withholding tax agreement
   → Buyer withholds 20%, you chase refund for years
```

---

## **CLOSING DAY TAX CHECKLIST**

- [ ] Confirm wire amount = price per LOI (not adjusted for surprise "taxes")
- [ ] Escrow arrangement doesn't trigger deemed realization
- [ ] Earnout doesn't start accruing immediately (deferred)
- [ ] Seller note has documented interest rate (IRS rules)
- [ ] Confirm no retroactive effective date (could trigger prior-year tax)
- [ ] Receive closing statement (buyer & seller agree on gain basis)

---

## **POST-CLOSE TAX OBLIGATIONS**

### **Year 1 of earnout**

```
Quarterly estimated tax payments: Q1, Q2, Q3, Q4
├─ Estimate total earnout income (you + CPA)
├─ Pay 25% each quarter
└─ Reconcile in tax return (April next year)

Capital gains tax: File by April 15 (EU varies)
```

### **Each earnout year**

- File tax return including earnout as ordinary income
- If earnout < expected, claim overpayment refund
- Track basis per earnout receipt (separate 1099s per year)

---

## **USEFUL FORMULAE**

### **Tax-optimized deal structure**

```
If marginal tax rate (capital gain) = 51.5%
   And earnout tax rate = 62%

Then: 
  Max base price = X
  Min earnout = Y
  
Where: X ≥ (Total EV × 75%)
       Y ≤ (Total EV × 25%)

Example: EV €500k
  ✓ Base €375k + earnout €125k = lower total tax
  ✓ But earnout risk = you lose if buyer doesn't hit targets
```

### **Escrow impact on taxes**

```
Escrow held ≠ taxed immediately (in most jurisdictions)
Escrow released = taxed when received (or upon agreement)

So: €50k in escrow during Y1
    If released in Y2 = tax hit in Y2 (not Y1)
```

---

## **FINAL ADVICE**

1. **Hire tax specialist 2 months before LOI** — not 2 weeks before close
2. **Earnout is MORE tax-inefficient** — push for higher base price
3. **Installment sales defer taxes** — useful if you want to spread income
4. **Escrow timing matters** — negotiate when it's taxed (usually upon release)
5. **Earnout measurement = tax documentation** — keep clean records
6. **Cross-border deals** — hire international tax firm (transfer pricing)
7. **Non-compete payment** — separate from earnout, different tax treatment

**Bottom line:** You can save €20-50k in taxes with good structuring.
Hire a specialist. ROI = 10:1.

