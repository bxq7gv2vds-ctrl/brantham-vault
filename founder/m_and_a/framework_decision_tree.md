---
name: framework-decision-tree
description: Framework de decision tree (go/no-go par buyer) — quick evaluation
metadata:
  type: reference
  created: 2026-06-13
---

# Decision Tree — Go/No-Go per Buyer

**Use this to quickly decide: Should we pursue this buyer seriously?**

---

## THE TREE

```
START: Buyer approaches or you're considering outreach

├─ Q1: Is this buyer real? (Legitimate company, real decision-maker)
│  ├─ NO → STOP. Move to next buyer.
│  └─ YES → Q2
│
├─ Q2: Do they have strategic fit OR financial capacity?
│  ├─ NO → STOP. (Small buyer with no synergy = low offer)
│  └─ YES → Q3
│
├─ Q3: Are they willing to move fast (<90 days to close)?
│  ├─ NO → LOW PRIORITY (add to Cohort C; revisit later)
│  └─ YES → Q4
│
├─ Q4: Are we aligned on price ballpark? (Within 20% of our ask)
│  ├─ NO → NEGOTIATE FIRST (before investing diligence time)
│  └─ YES → Q5
│
├─ Q5: Do we want to work with them long-term? (Culture fit, vision)
│  ├─ NO → EXPLORE but not with enthusiasm (low engagement)
│  └─ YES → GO. Prioritize engagement.
│
└─ OUTPUT: Go/No-Go decision
```

---

## DETAILED QUESTIONS & SCORING

For each buyer, answer these 5 questions. Score 1–4 (1 = No, 4 = Yes).

### Q1: BUYER LEGITIMACY (Pass/Fail)

**Real buyer?**
- ✓ Company has >$100M revenue OR >$[X]M funding
- ✓ Acquisition track record (acquired 2+ companies in past 5 yrs)
- ✓ Decision-maker (CFO, CEO, VP Corp Dev) signing the NDA
- ✓ Financing in place (cash on balance sheet OR committed credit)

**Score: 1–4**
- 1 = Unknown, probably not legitimate
- 4 = Clearly legit; high-profile acquirer

**Threshold**: <2 = STOP. Don't proceed.

---

### Q2: STRATEGIC FIT OR CAPACITY (1–4)

**Strategic fit?**
- Does buyer's platform benefit from our product?
- Can they upsell to existing customers?
- Do we have complementary customer bases?

**OR Financial capacity?**
- Buyer has $[X]M+ cash available for acquisition
- Financing partner committed
- Not dependent on selling other assets

**Score:**
- 1 = No fit, limited capital
- 2 = Weak fit, OR weak capital position
- 3 = Good fit OR strong capital
- 4 = Strong fit AND strong capital

**Threshold**: <2 = STOP (unless price is astronomical).

---

### Q3: SPEED/TIMELINE (1–4)

**Can they close in <90 days?**
- All-cash deal? (Fast)
- Financing committed? (Medium)
- Regulatory approval needed? (Slow)
- Internal approvals required? (Variable)

**Score:**
- 1 = 180+ days (too slow)
- 2 = 120–180 days (slow)
- 3 = 60–120 days (normal)
- 4 = <60 days (very fast)

**Threshold**: <2 = Add to Cohort C (reserve buyers).

---

### Q4: PRICE ALIGNMENT (1–4)

**Are we in ballpark?**

1. You want: $[X]M
2. Buyer's opening: $[Y]M
3. Difference: $[Z]M

**Calculate**: Z / X = % gap

**Score:**
- 1 = >50% gap (e.g., you want $20M, they offer $10M)
- 2 = 30–50% gap (you want $20M, they offer $12M)
- 3 = 10–30% gap (you want $20M, they offer $15M)
- 4 = <10% gap (you want $20M, they offer $18–20M)

**Threshold**: <2 = Negotiate first before investing diligence time. Only proceed if they're willing to move to 20% gap.

---

### Q5: CULTURE / VISION ALIGNMENT (1–4)

**Do we want to work with these people?**

**Red flags (low score):**
- ✗ They want to replace you immediately
- ✗ Product kill (shut down your product)
- ✗ Opposite values (you're bootstrapped, they're PE money-grab)
- ✗ Bad reputation (glassdoor reviews are terrible)

**Green flags (high score):**
- ✓ They want to keep team intact
- ✓ Expand your product (not kill it)
- ✓ Shared vision for customer-first approach
- ✓ Employees rave about working there

**Score:**
- 1 = Deal-breaker culture misalignment
- 2 = Significant tension; would tolerate for right price
- 3 = Acceptable; no major red flags
- 4 = Great fit; would be excited to work with them

**Threshold**: <2 = Only pursue if price is exceptional (>50% above target). Otherwise, move on.

---

## AGGREGATED SCORING

| Question | Weight | Buyer A | Buyer B | Buyer C |
|----------|--------|---------|---------|---------|
| **Q1: Legitimacy** | Pass/Fail | ✓ | ✓ | ✗ STOP |
| **Q2: Fit/Capacity** | 20% | 4 | 2 | — |
| **Q3: Speed** | 20% | 3 | 1 | — |
| **Q4: Price** | 30% | 3 | 4 | — |
| **Q5: Culture** | 30% | 4 | 2 | — |
| **WEIGHTED TOTAL** | **100%** | **3.4** | **2.2** | **REJECT** |

---

## DECISION LOGIC

| Score | Decision | Action |
|-------|----------|--------|
| **≥3.5** | GO | Cohort A: prioritize, fast-track diligence |
| **3.0–3.5** | WARM MAYBE | Cohort A: proceed, but watch for red flags |
| **2.5–3.0** | MAYBE | Cohort B: engage, but no exclusivity |
| **2.0–2.5** | COOL | Cohort C: light-touch, revisit if A/B stall |
| **<2.0** | NO-GO | Reject or defer indefinitely |

---

## EXAMPLES

### Example 1: Strategic Acquirer (High Score)

**Buyer**: Salesforce acquiring niche CRM add-on

- Q1: Legitimacy = ✓ (Fortune 500)
- Q2: Fit/Capacity = 4 (perfect product fit, M&A track record)
- Q3: Speed = 4 (all-cash, can close 45 days)
- Q4: Price = 3 ($15M vs. your $18M ask — 17% gap)
- Q5: Culture = 4 (great employer, your team excited to join)

**Score: 3.7 → GO (Cohort A)**

---

### Example 2: PE Fund (Medium Score)

**Buyer**: Mid-market PE fund buying for add-on

- Q1: Legitimacy = ✓ (real fund, $500M AUM)
- Q2: Fit/Capacity = 3 (financial capacity good, product fit okay)
- Q3: Speed = 2 (needs lender approval, 120+ days)
- Q4: Price = 4 ($18M offered; you wanted $18M)
- Q5: Culture = 2 (PE culture; no promise your team stays)

**Score: 2.8 → MAYBE (Cohort B)**

---

### Example 3: Weak Buyer (Low Score)

**Buyer**: Random holding company with no track record

- Q1: Legitimacy = ✗ (STOP HERE)

**Score: REJECT**

---

## WHEN TO REVISIT / CHANGE SCORE

| Event | Action |
|-------|--------|
| **Buyer improves offer** | Rescore Q4 (price) |
| **Buyer commits financing** | Rescore Q3 (speed) |
| **Buyer's CEO vouches for culture** | Rescore Q5 |
| **You learn buyer has integration issues** | Rescore Q5 (downward) |
| **Buyer goes silent >2 weeks** | Treat as REJECT; move on |

---

## QUICK SUMMARY

Use this tree to decide in **<15 minutes**:

1. Is buyer real?
2. Do they have fit or money?
3. Can they close fast?
4. Is price in ballpark?
5. Do we want to work with them?

If mostly YES = **GO** (Cohort A)  
If mostly MAYBE = **EXPLORE** (Cohort B)  
If mostly NO = **SKIP** (Cohort C or reject)

