---
name: earnout_agreement_template
description: Modèle d'earnout agreement — structure légale minimale, conditions claires
metadata:
  type: reference
  format: legal_template
  version: 1.0
---

# Earnout Agreement — Modèle complet

**Entre :** [SELLER NAME] (Vendor) et [BUYER] (Purchaser)
**RE :** Earnout payment contingent on customer retention & ARR targets
**Date :** [Signing Date]

---

## **1. EARNOUT OBLIGATION**

Purchaser shall pay Vendor the earnout as follows, **conditional on achievement of Targets**:

| Period | Condition | Amount | Payout Date |
|--------|-----------|--------|-------------|
| **Year 1** | Customer retention ≥ 85% | €[X] | Within 30 days of verification |
| **Year 2** | ARR growth ≥ [Y]% YoY | €[Z] | Within 30 days of verification |
| **Year 3** | Churn < [%] annualized | €[W] | Within 30 days of verification |

**Total earnout:** €[TOTAL] (capped)

---

## **2. DEFINITIONS**

### **Retention Rate**
```
Calculation as of measurement date:
(# Customers_retained / # Customers_at_closing) × 100

where:
- "Customer_at_closing" = customer with active contract on Closing Date
- "Customer_retained" = customer still paying/contracted at measurement date
- Churn is: customer did not renew, or notified non-renewal
```

### **ARR (Annual Recurring Revenue)**
```
= Sum of all active customer annual contract values as of measurement date
Exclude: One-time services, professional services revenue
Include: All renewal/expansion revenue
Measured Q by Q
```

### **Measurement Date**
```
Y1: [12 months post-closing], verified [date]
Y2: [24 months post-closing], verified [date]
Y3: [36 months post-closing], verified [date]
```

---

## **3. MEASUREMENT & VERIFICATION**

### Purchaser's obligation
- Calculate retention/ARR monthly
- Provide Vendor summary report **within 15 days of each measurement date**
- Report includes: customer list, ARR per customer, churn reasons

### Vendor's right to audit
- Vendor may request independent verification (Big 4 audit, €[X] cost)
- If audit shows variance > [3%], Purchaser pays audit costs
- Audit results binding on both parties

### Dispute resolution
```
Timeline:
D0: Purchaser sends report
D15: Vendor accepts or requests clarification
D30: If disputed, go to arbitration (per SPA)
D60: Arbitrator decision final & binding
```

---

## **4. PAYOUT CONDITIONS & CLAWBACK**

### Condition precedent: **Vendor retention**

Earnout paid **only if**:
- Vendor (Founder) remains employed OR has consulting agreement
- If Vendor terminated without cause before payment date: full earnout still paid
- If Vendor voluntarily resigns: earnout subject to [X%] reduction per month remaining

### Clawback clause

**Earnout reduced if:**
```
(a) Purchaser voluntarily reduces product/support (deprioritization)
    → Earnout not reduced (assumes good faith management)
    
(b) Purchaser deliberately acquires customer to inflate ARR
    → Earnout adjusted downward (bad faith prohibited)
    
(c) Purchaser's customer success team doesn't execute
    → Earnout not reduced (Vendor not liable for buyer's execution)
```

---

## **5. PAYMENT MECHANICS**

### Wire transfer instructions
```
Account: [VENDOR BANK ACCT]
Bank: [BANK NAME]
IBAN: [IBAN]
Amount: €[X] per earnout tranche
Wire by: [30 days post-verification]
```

### Tax treatment
```
Purchaser: Issues 1099 (US) or equiv (EU) for earnout
Vendor: Responsible for own tax liability
Earnout: Treated as contingent consideration (likely ordinary income)
```

### No escrow or holdback
```
Earnout is paid directly from Purchaser to Vendor
(separate from closing cash or SPA holdback)
```

---

## **6. NON-COMPETE & IP PROVISIONS**

### Non-compete during earnout period
```
Vendor shall not:
- Build competing product
- Solicit customers of [Product]
- Hire key employees away

Exception: Vendor may:
- Consult on [non-competing domain]
- Angel invest in other sectors
- Advisory board roles
```

### IP ownership post-close
```
All IP created during earnout period: owned by Purchaser
(Vendor assigns all work product to Purchaser)
```

---

## **7. REPRESENTATIONS & WARRANTIES**

### Vendor represents:
```
✓ Retention calculation basis is accurate
✓ Customer list at closing is complete
✓ No knowledge of pending cancellations
✓ Vendor is authorized to sign this agreement
```

### Purchaser represents:
```
✓ Financial ability to pay earnout
✓ Will conduct business in good faith (not sabotage to reduce earnout)
✓ Measurement methodology is objective
```

---

## **8. EARNOUT EXAMPLES**

### Example 1: Retention-based (most common)

```
Closing date: Jan 1, 2026
Customers at close: 50
ARR at close: €500k

Y1 Target: Retain 42+ customers (84%) by Jan 1, 2027
├─ If 43+ retained: Pay €50k earnout
├─ If 40-42 retained: Pay €25k earnout
└─ If <40 retained: Pay €0

Y2 Target: ARR ≥ €550k by Jan 1, 2028 (10% growth)
├─ If achieved: Pay €50k earnout
└─ If not: Pay €0
```

**Rationale:** Customer retention is strongest signal of product fit. ARR growth shows buyer can scale.

### Example 2: Churn-based (for mature products)

```
Closing churn rate: 8% annual
Y1 Target: Reduce to 5% annual churn

├─ If churn = 5%: Pay €75k
├─ If churn = 6%: Pay €50k
├─ If churn = 7%: Pay €25k
└─ If churn > 7%: Pay €0
```

**Rationale:** Churn reduction = product improvements, customer success execution.

### Example 3: Revenue + retention combo

```
Closing metrics:
├─ ARR: €1M
├─ Customers: 100
├─ Churn: 5%

Year 1 earnout (Jan 2027):
├─ Retention ≥ 90%: €50k
├─ + Churn < 7%: €30k
├─ + NPS improved 5+ points: €20k
└─ Total possible: €100k

(If customer retains but churn worsens, only 1st tranche paid, etc)
```

---

## **9. DISPUTE RESOLUTION**

### If Vendor believes earnout not paid fairly

```
Step 1: Written notice within 30 days of alleged breach
Step 2: Good faith negotiation (15 days)
Step 3: Expert determination (independent accountant, 30 days)
Step 4: If still disputed, arbitration (binding)
```

### Arbitration clause
```
Location: [Paris/London/NYC as per SPA]
Arbitrator: 1 neutral expert in software M&A
Decision: Final and binding
Costs: Losing party pays arbitrator fees
```

---

## **10. TERMINATION & SURVIVAL**

### What kills the earnout

```
✗ Vendor dies: Earnout paid to estate (vests by date of death)
✗ Vendor disabled: Earnout paid in full at next measurement
✓ Vendor voluntarily resigns: Earnout reduced per formula (see 4. above)
✗ Vendor non-competes breach: Earnout forfeited
```

### Earnout survives
```
✓ Acquisition by 3rd party of Purchaser (earnout transfers)
✓ Refinancing or recapitalization of Purchaser
✗ Bankruptcy of Purchaser: Earnout claim is unsecured (may not recover)
```

---

## **11. SIGNATURE**

```
VENDOR:

_________________________________    DATE: ____________
[VENDOR NAME]


PURCHASER:

_________________________________    DATE: ____________
[PURCHASER CEO/AUTHORIZED]
[PURCHASER COMPANY NAME]
```

---

## **NOTES ON USAGE**

1. **Keep it simple** — more than 3-4 earnout tranches = too complex
2. **Make targets achievable** — if 0% likelihood of payout, it's worth €0
3. **Measure independently** — auditor-verified is best, reduces dispute
4. **Link to business model** — earnout should reflect what buyer can control
5. **Escrow vs direct** — earnout is usually paid direct (not from holdback)
6. **Get it in writing** — LOI should outline structure, SPA/earnout agreement locks down
7. **Use third-party audit** — costs €2-5k, saves disputes worth €50k+

---

## **Red flags to watch**

```
❌ Earnout with no definition of "customer" or "ARR"
❌ Measurement by buyer alone (no independent verification)
❌ Earnout payable from buyer's EBITDA (can be manipulated)
❌ Earnout forgiven if founder leaves (indentured servitude)
❌ Clawback clause that lets buyer reduce retroactively
❌ Earnout payments delayed >60 days after verification
❌ No dispute resolution mechanism
```

✓ Best practice: Use Big 4 audit firm for annual verification (~€3-5k cost, but worth it).
## Related
