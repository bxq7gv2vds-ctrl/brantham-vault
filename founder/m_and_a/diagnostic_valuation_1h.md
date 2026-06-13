---
name: diagnostic-valuation-1h
description: Diagnostic de valorisation rapide (60 min) — 3 approches, résultat exploitable
metadata:
  type: reference
  created: 2026-06-13
---

# Diagnostic de Valorisation (1 Heure)
**3 approaches rapides + consensus range**

---

## SETUP (5 MIN)

**Data you need:**
- Last 12 months revenue (ARR)
- Projected revenue (next 12 months)
- Gross margin %
- EBITDA or "profit" (positive or negative)
- [Optional] Comp acquisition prices (e.g., Slack at $27.7B / $12B revenue)

---

## APPROACH 1: REVENUE MULTIPLE (10 MIN)

**Formula**: Valuation = ARR × Multiple

**Step 1**: Current ARR?  
Example: $5M ARR

**Step 2**: What's the right multiple?

| Segment | Typical Multiple | Why |
|---------|-----------------|-----|
| **High-growth SaaS** (>100% YoY) | 15–30x | Venture-backed, proven model |
| **Mid-market SaaS** (50–100% YoY) | 8–15x | Strong growth, traction |
| **Slow-growth SaaS** (20–50% YoY) | 4–8x | Established, some traction |
| **Mature SaaS** (<20% YoY) | 2–4x | Stable, low risk, low growth |

**Step 3**: Apply multiple  
Example: $5M ARR × 10x (mid-market SaaS) = **$50M valuation**

**Sanity check:**  
- Compare to [publicly traded comp]: Datadog = 40x revenue, Slack = 15x, Zoom = 12x
- If your multiple is >40x, you're in "unicorn" territory (justify it)
- If <3x, you're valued like a boring business (push back or find better buyer)

---

## APPROACH 2: EBITDA OR DCF (15 MIN)

**If you have positive EBITDA:**

Formula: Valuation = EBITDA × Exit Multiple

Example:
- EBITDA: $1M/year
- Exit multiple (profitable SaaS): 10–15x EBITDA
- Valuation: $1M × 12x = **$12M**

---

**If still burning (negative EBITDA):**

Use **path to profitability** + projected EBITDA.

Example:
- Current: -$500K EBITDA
- Projected (in 18 months): +$2M EBITDA
- Apply multiple to **projected** EBITDA: $2M × 10x = $20M
- Discount for risk: $20M × 0.75 = **$15M valuation**

---

## APPROACH 3: CUSTOMER VALUE (15 MIN)

**Formula**: Valuation = (# Customers × LTV) + Growth Premium

**Step 1**: # customers × average LTV

Example:
- 100 customers
- Average LTV: $100K (customer lifetime value)
- Base value: $100 × $100K = $10M

**Step 2**: Growth premium (% uplift for growth potential)

- High growth (>100% YoY): +100% premium → $20M
- Mid growth (50–100%): +50% premium → $15M
- Slow growth (20–50%): +20% premium → $12M

**Step 3**: Apply market conditions

- Competitive market: -10% ($18M if high-growth)
- Oligopoly / rare: +20% ($24M if high-growth)

---

## TRIANGULATION (10 MIN)

**Now you have 3 estimates.** Triangulate:

| Approach | Valuation | Notes |
|----------|-----------|-------|
| **Revenue multiple** | $50M | Assumes standard 10x SaaS multiple |
| **EBITDA/Path to profit** | $15M | Conservative (path-to-profitability discount) |
| **Customer value** | $18M | Reflects growth + retention |
| **Consensus range** | **$15M–$50M** | Likely sweet spot: **$20M–$30M** |

---

## SENSE-CHECKING

**Ask yourself:**

- Does $[valuation] feel high relative to competitors? (Use Crunchbase/PitchBook)
- Would a PE buyer offer this price? (Typically lower than VC multiples)
- Would a strategic buyer offer more? (They can afford premium for synergies)
- Am I leaving money on the table? (If only 1–2 buyers, yes; if 3+, maybe fair)

---

## QUICK ADJUSTMENTS FOR YOUR SITUATION

| Situation | Valuation Adjustment |
|-----------|----------------------|
| **Founder committed to stay 3 years** | +10–15% (reduces integration risk) |
| **Zero churn, only growth** | +20% (exceptionally sticky) |
| **Regulatory/IP risk** | -15–30% (buyers will discount) |
| **Concentrated customer base** | -20% (if top 5 = >50% revenue) |
| **Key person dependency** | -25% (will leave immediately) |

---

## FINAL ANSWER

**"Our fair valuation range is $[X]M–$[Y]M."**

Use the **low end** in first conversations (leaves room to negotiate up).  
Use the **high end** when you have competitive offers.

---

## EXAMPLE OUTPUT (30 MIN WALKTHROUGH)

```
Company: TechStartup Inc.
Current ARR: $3M
YoY growth: 85%
EBITDA: -$200K, projected +$800K in 18 months
Customers: 25, avg LTV: $120K

APPROACH 1 (Revenue): $3M × 12x = $36M
APPROACH 2 (EBITDA): $800K × 10x × 0.75 discount = $6M
APPROACH 3 (Customer value): (25 × $120K) + 50% growth = $4.5M + $2.25M = $6.75M

Consensus: $6.75M–$36M
Likely range: $15M–$25M (mid-market SaaS acquiring for synergies)

Recommendation: Ask $22M, settle at $18M–$20M.
```
## Related
