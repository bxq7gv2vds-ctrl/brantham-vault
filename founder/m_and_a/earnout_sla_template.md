# Earnout SLA — KPI Tracking & Payment Mechanics

**Objectif :** Template opérationnel pour mesurer/tracker earnout post-close; éviter disputes post-acquisition.

---

## EARNOUT AGREEMENT EXHIBIT

**Parties:** [SELLER], [BUYER]  
**Earnout Period:** [DATE] to [DATE] (typically 12–24 months)  
**Total Earnout Opportunity:** $[X]M

---

## TARGET METRICS & PAYOUT STRUCTURE

| Metric | Target (Year 1) | Target (Year 2) | Payout if Hit |
|--------|---|---|---|
| **ARR (Annual Recurring Revenue)** | $[6.0]M | $[7.5]M | $[1.5]M @ Y1 / $[1.0]M @ Y2 |
| **Gross Margin** | >70% | >72% | $[250k] if avg >70% |
| **Net Revenue Retention** | >110% | >115% | $[250k] if avg >115% |
| **Customer Count** | >100 | >130 | $[250k] if >130 by EOY2 |
| **Max Earnout Payout** | — | — | **$[3.5]M** |

---

## MEASUREMENT & CALCULATION

**Data Source:** Buyer's audited financial statements (GAAP)

**Timing:** 
- Q4 Year 1 measurement → payout within 30 days (if KPI hit)
- Q4 Year 2 measurement → payout within 30 days (if KPI hit)

**Calculation Example:**
```
ARR Target = $6.0M (Y1)
Actual ARR = $5.8M (Q4 Y1)
Hit? NO → $0 earnout for ARR
(No partial credit; binary: hit or miss)
```

**NRR Calculation:**
```
Cohort 2024-Q4 revenue (end of period) = $1.2M
Same cohort revenue 1 year earlier = $1.0M
NRR = $1.2M / $1.0M = 120% ✅
(If ≥110%, bonus unlocked)
```

---

## AUDIT & DISPUTE RESOLUTION

**Seller Audit Rights:**
- [ ] Quarterly access to buyer's P&L and KPI metrics
- [ ] Right to engage independent accountant to verify
- [ ] Buyer provides variance explanations (why miss target)
- [ ] Cost of audit split 50/50 if seller-initiated

**Dispute Timeline:**
1. Buyer delivers KPI summary (within 30 days of quarter-end)
2. Seller has 15 days to dispute
3. If disputed: independent accountant decides within 10 days
4. Decision is final; loser pays auditor fee

**If Undercalculation Detected:**
- Buyer pays earnout + interest (8% annual) on late payment

---

## ADJUSTMENTS & EXCLUSIONS

**Buyer Cannot Reduce Earnout If:**
- ❌ Buyer cuts product investment (KPI not Seller's fault)
- ❌ Buyer shifts resources to other business units
- ❌ General market downturn affects growth
- ❌ Buyer changes strategy post-close
- ❌ Buyer lays off Seller's team (increases churn artificially)

**Earnout Automatically Adjusts IF:**
- ✅ Material customer churn (>$500k ARR lost unexpectedly) → escalation clause
- ✅ Regulatory change preventing revenue recognition → adjustment formula
- ✅ Acquisition target company itself is acquired → earnout accelerates to cash payout

---

## EXAMPLES — EARNOUT SCENARIOS

**Scenario A: Full Success**
```
Y1 ARR Target: $6.0M → Actual: $6.2M ✅ → Earnout: $1.5M paid
Y1 NRR Target: >110% → Actual: 115% ✅ → Earnout: $250k paid
Y1 GrossMargin: >70% → Actual: 72% ✅ → Earnout: $250k paid
TOTAL Y1 EARNOUT: $2.0M paid (within 30 days)
```

**Scenario B: Partial Hit**
```
Y1 ARR Target: $6.0M → Actual: $5.2M ❌ → No earnout ($0)
Y1 NRR Target: >110% → Actual: 112% ✅ → Earnout: $250k paid
TOTAL Y1 EARNOUT: $250k paid
(Note: No partial credit on ARR miss; all-or-nothing)
```

**Scenario C: Full Miss**
```
Y1 ARR Target: $6.0M → Actual: $4.8M ❌
Y1 NRR Target: >110% → Actual: 105% ❌
Y1 Margin Target: >70% → Actual: 65% ❌
TOTAL Y1 EARNOUT: $0 (no payment despite effort)
```

---

## BUYER UNDERINVESTMENT PROTECTION (CRITICAL)

**Red Flag:** Buyer deliberately cuts budget to block earnout. **Solution:** Minimum investment clause.

**Buyer Commits To:**
- Sales/marketing spend ≥ $[X] annually (audited)
- Product team ≥ [N] engineers dedicated to Seller's product
- If Buyer cuts spend <$X, earnout KPI threshold reduced by [X]%

**Example:**
```
If Buyer commits $2M sales spend → 
  But only spends $1.2M (40% cut) → 
    ARR target reduced to $5.4M (from $6.0M)
```

---

## FOUNDER/TEAM RETENTION & EARNOUT

**Risk:** Founder leaves post-close; earnout derailed. **Solution:** Retention linkage.

**If Key Team Member Leaves:**
- Earnout reduced by [X]% per departure
- Exception: Buyer forced layoff (Buyer absorbs the loss)

**Example:**
```
CTO leaves voluntarily (Q2 Y1) → 
  Y1 earnout reduced to 80% of payout
(but if Buyer fired CTO, Buyer doesn't get earnout benefit)
```

---

## TAX TREATMENT OF EARNOUT

**Standard:** Earnout is taxable income to Seller (not capital gains)

**Optimize:** Negotiate holdback/earnout structure pre-close
- Option 1: Higher base price (capital gains), lower earnout (tax inefficient)
- Option 2: Lower base, higher earnout + retention bonus (deductible for buyer; still ordinary income for seller)

**Seller's CPA To Confirm:** 1099-MISC filing by Buyer within 30 days of earnout payout

---

## ESCROW VS EARNOUT (KEY DIFFERENCE)

| Mechanism | Holdback | Purpose | Release |
|---|---|---|---|
| **Escrow** | 10–15% of base price | Secured against reps&warranty claims | 12–18 months |
| **Earnout** | 15–30% of total consideration | Reward for hitting KPI post-close | Upon KPI hit |

**Example Deal Structure:**
```
Total Deal: $50M
- Base price: $35M (paid at close)
  ├── Net to Seller: $35M (after 10% escrow hold = $3.5M escrowed)
- Earnout: $15M (if KPI hit by EOY2)
Total possible to Seller: $50M (if escrow released + earnout paid)
Minimum to Seller: $31.5M (if escrow never released + earnout missed)
```

---

## SAMPLE EARNOUT SCHEDULE

**Quarterly KPI Tracking Dashboard**

```
EARNOUT TRACKING — [SELLER_NAME] Earnout Agreement

Quarter | Metric | Target | Actual | Status | Payment | Notes |
---------|--------|--------|--------|--------|---------|--------|
Q4-Y1 | ARR | $6.0M | $6.1M | ✅ Hit | $1.5M | Paid 1/15/2026 |
Q4-Y1 | NRR | >110% | 115% | ✅ Hit | $250k | Paid 1/15/2026 |
Q4-Y1 | Margin | >70% | 71% | ✅ Hit | $250k | Paid 1/15/2026 |
Q1-Y2 | ARR | $6.5M | $5.9M | ⏳ TBD | — | In progress |
Q2-Y2 | ARR | $7.0M | — | — | — | Future |
```

(To be updated quarterly)

---

## WHAT TO AVOID

❌ **Vague KPI definitions** (e.g., "revenue growth" without baseline)  
❌ **Buyer-controlled metrics** (e.g., earnout tied to Buyer's decision to hire)  
❌ **No audit rights** (Seller can't verify Buyer's numbers)  
❌ **Long measurement lag** (earnout paid 6 months after period-end = cash flow risk)  
❌ **No minimum investment clause** (Buyer slashes budget, kills KPI)  

---

Créé : 2026-06-13 | À signer comme Exhibit to Purchase Agreement
