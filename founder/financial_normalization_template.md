---
name: financial_normalization_template
description: EBITDA add-backs & revenue normalization — 3 scenarii (conservative/base/aggressive)
type: template
date: 2026-06-12
---

# Financial Normalization Template — Buyer DD

**Purpose:** Adjust GAAP financials to "run-rate" or "normalized" EBITDA (remove one-time items, add back synergies).

**Key insight:** Buyers value normalized EBITDA (12–18x multiple), not GAAP EBITDA (5–8x).

---

## FRAMEWORK

**Normalized EBITDA = GAAP Net Income + Taxes + Interest + D&A + Adjustments**

Where Adjustments include:
- **One-time costs** (severances, restructuring, legal fees from old litigation)
- **Synergy add-backs** (headcount reduction post-merge, cost consolidation)
- **Stock-based comp** (non-cash, should be normalized out)
- **Related-party items** (office rent from founder's building, etc.)

---

## SCENARIO 1: CONSERVATIVE (Buyer-Friendly)

**Use when:** Buyer is skeptical, you want to over-deliver.

| Item | Amount | Justification |
|---|---|---|
| **GAAP Net Income** | $[2.0]M | |
| **+ Taxes (25%)** | $[0.5]M | Estimate federal/state |
| **+ Interest (debt)** | $[0.2]M | Small bank loan |
| **+ D&A (non-cash)** | $[0.3]M | SaaS capitalization |
| **+ Stock-based comp** | $[0.4]M | Employee options (fully-diluted grants) |
| **+ One-time legal** | $[0.1]M | IP litigation (resolved) |
| **- Synergy add-back** | ($[0.2]M) | Headcount overlap (conservative) |
| **= Normalized EBITDA** | **$[3.3]M** | |

**Implied valuation (at 15x EBITDA):** $49.5M

**Buyer advantage:** You're "safe" on numbers. Credibility boost for earnout.

---

## SCENARIO 2: BASE CASE (Balanced)

**Use when:** You have strong financials, buyer is sophisticated.

| Item | Amount | Justification |
|---|---|---|
| **GAAP Net Income** | $[2.0]M | |
| **+ Taxes (25%)** | $[0.5]M | Federal/state combined |
| **+ Interest (debt)** | $[0.2]M | Bank loan rate 5% |
| **+ D&A (non-cash)** | $[0.3]M | Straight-line SaaS amortization |
| **+ Stock-based comp** | $[0.5]M | Fully-diluted grants + ESPP |
| **+ One-time legal** | $[0.1]M | IP defense (resolved) |
| **+ Severance (one-time)** | $[0.2]M | Consultant exit arrangements |
| **+ Related-party rent** | $[0.1]M | Founder building sublease (market rate) |
| **- Buyer cost synergies** | ($[0.3]M) | Headcount + vendor consolidation |
| **- Buyer revenue impact** | —| (Assume neutral short-term) |
| **= Normalized EBITDA** | **$[3.6]M** | |

**Implied valuation (at 15x EBITDA):** $54M

**Buyer perspective:** Realistic, defensible, achievable earnout.

---

## SCENARIO 3: AGGRESSIVE (Seller-Friendly)

**Use when:** You have strong optionality (multiple buyers), high growth.

| Item | Amount | Justification |
|---|---|---|
| **GAAP Net Income** | $[2.0]M | |
| **+ Taxes (25%)** | $[0.5]M | |
| **+ Interest (debt)** | $[0.2]M | |
| **+ D&A (non-cash)** | $[0.3]M | |
| **+ Stock-based comp** | $[0.6]M | Full option pool, high turnover |
| **+ One-time legal** | $[0.1]M | |
| **+ Severance** | $[0.2]M | |
| **+ Related-party** | $[0.15]M | Founder office rent + consulting |
| **+ Lost synergies** | $[0.2]M | "We'll lose [X] once integrated" |
| **- Buyer cost synergies** | ($[0.4]M) | (Reduced estimate) |
| **= Normalized EBITDA** | **$[3.95]M** | |

**Implied valuation (at 16x EBITDA):** $63.2M

**Warning:** Buyer will challenge "lost synergies" and "related-party." Only use if you have other offers.

---

## COMMON ADJUSTMENTS (Detailed)

### ✅ TYPICALLY ACCEPTED

| Item | Typical Range | Notes |
|---|---|---|
| Stock-based comp | 10–20% of payroll | Fully-diluted grants, ESPP, options |
| One-time legal | $50K–$500K | Old IP litigation, not recurring |
| Severance (departure) | $100K–$500K | Key person left, one-time cost |
| Non-recurring consulting | $50K–$200K | Founder paying for interim, one-time |
| D&A (non-cash) | 5–15% of revenue | Capitalized software, server costs |
| One-time restructuring | $100K–$1M | Facility exit, rebrand, not recurring |

### ⚠️ OFTEN QUESTIONED

| Item | Typical Range | Why Buyer Pushes Back |
|---|---|---|
| Related-party transactions | $50K–$500K | Potential overcharging; want market rate |
| "Lost synergies" | $100K–$1M | Speculative; hard to prove impact |
| Accrued but unpaid taxes | $100K–$500K | Depends on jurisdiction, audit risk |
| Vendor volume discounts | $50K–$500K | Will buyer get same discount? Prove it. |
| Customer-specific costs | $50K–$200K | Is this really one-time? |

### ❌ RARELY ACCEPTED

| Item | Why Buyer Rejects |
|---|---|
| Revenue reserves (not recognized) | If it's not GAAP, don't claim it. |
| "Deferred revenue will grow 3x" | Speculative; use base revenue only. |
| Synergies buyer won't achieve | Buyer doesn't want your hypotheticals. |
| Tax adjustments (ambitious read) | Risky; tax authorities may disagree. |

---

## SAMPLE WORKING CAPITAL ADJUSTMENT

**Working capital** = Current Assets − Current Liabilities  
**Most common:** Accounts Receivable + Inventory − Accounts Payable

**Example calculation:**
```
Target working capital (% of revenue): 15%
YoY revenue: $[10]M
Target WC = $[10]M × 15% = $[1.5]M

At close:
- Current assets: $[2.0]M (AR, cash deposits)
- Current liabilities: $[0.4]M (AP, accrued expenses)
- Actual WC = $[1.6]M

Adjustment: Seller owes buyer $[0.1]M (WC above target)
If WC fell to $[1.3]M, buyer owes seller $[0.2]M
```

**SPA clause:**
```
If Closing Date Working Capital > Target WC, Buyer shall pay Seller [excess].
If Closing Date Working Capital < Target WC, Seller shall reimburse Buyer [shortage].
```

---

## REVENUE RUN-RATE (Alternative to EBITDA)

**If EBITDA is volatile, use revenue multiple instead:**

```
LTM (Last Twelve Month) Revenue: $[10]M
Forward Run-Rate (assume +30% growth): $[13]M

Buyer valuation at 5x run-rate revenue: $65M
(Alternative: 4–6x, depends on growth, margin, risk)
```

---

## TEMPLATES FOR BUYER PRESENTATIONS

### Simple 1-Pager (for teaser)
```
FINANCIAL SUMMARY

LTM Revenue: $[10]M | +[30]% YoY
Gross Margin: [75]% | Improving
Operating Margin: [20]%
Normalized EBITDA: $[3.6]M | 36% margin
Customers: [500] | NRR [120]% | Churn [3]%

Valuation Reference: [15x EBITDA] = $[54]M
```

### Detailed (for DD)
```
GAAP FINANCIALS (Last 3 Years)
[Table with P&L, balance sheet, cash flow]

NORMALIZATION SCHEDULE
[Table with add-backs per scenario above]

WORKING CAPITAL ANALYSIS
[Table with target vs. actual]

EARNOUT METRICS
[Table with KPI targets for years 1–2]
```

---

## NEGOTIATION TACTICS

**If buyer challenges a big adjustment:**

| Challenge | Your Response |
|---|---|
| "That's too aggressive" | "Here's our comparable (Crunchbase, recent exit). We're actually conservative." |
| "We won't get that synergy" | "Reduce the adjustment by 50%, we'll do it together during integration." |
| "Your SBC is too high" | "Fully diluted shares, per ASC 718. Remove it or accept higher earnout." |
| "One-time costs are [X]" | "Okay, but recurring structure let's agree on [definition] so earnout is clear." |

**Goal:** Move from aggressive → base case scenario (credibility + earnout buy-in).

---

## CHECKLIST

- [ ] Gather last 3 years audited financials (or accountant-reviewed)
- [ ] Build normalized EBITDA bridge (conservative, base, aggressive)
- [ ] Identify 3–5 biggest add-backs (stock comp, legal, one-time)
- [ ] Calculate working capital target (% of revenue, justified)
- [ ] Document earnout KPI targets (revenue, customer retention, etc.)
- [ ] Prepare buyer presentation (1-pager + detailed schedule)
- [ ] Align with advisor/accountant before sharing with buyer
- [ ] Be ready to defend each number (audit trail, invoices, contracts)

---

## SUCCESS METRICS

✅ **Buyer accepts ≥80% of adjustments** → Credible presentation  
✅ **Normalized EBITDA >30% margin** → Attractive multiple  
✅ **Earnout targets achievable (>85% likely)** → Earnout gets paid
## Related
