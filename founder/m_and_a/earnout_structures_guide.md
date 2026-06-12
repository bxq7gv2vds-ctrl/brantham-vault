---
name: earnout-structures-guide
description: Types d'earnout, formules, pièges, et négociation
metadata:
  type: guide
  created: 2026-06-12
---

# Earnout Structures — What to Accept, What to Avoid

Use this before LOI negotiation. Earnouts are the new "stock option" — they can be worth 30-50% of deal.

---

## The Basics

**Earnout definition:** Buyer pays you cash AFTER closing if company hits targets.

**Example:**
```
Deal at signing: $10M cash
Earnout: $5M if hit $15M ARR by Dec 2027
  → If hit: You get $10M + $5M = $15M total
  → If miss: You get $10M only
```

---

## Earnout Structures (Pick ONE, or negotiate blend)

### Structure 1: Revenue Milestone

**What it is**: You get paid if revenue hits targets.

```
Example deal structure:
  Cash at close: $10M
  Earnout Year 1: 
    - If ARR hits $12M by Dec 2026 → $2M bonus
    - If ARR hits $14M by Dec 2026 → $3M bonus
  Earnout Year 2:
    - If ARR hits $18M by Dec 2027 → $2M bonus
```

**Pros:**
- Buyer aligns incentive (cares about YOUR revenue)
- Easiest to measure (objective)
- Standard in SaaS

**Cons:**
- If product fails, you don't get paid (unfair if buyer killed product)
- Buyer can deliberately slow sales (not recommended but happens)
- Churn risk: If top customer leaves, you miss target (not your fault)

**Red flags to negotiate:**
- ❌ Don't accept: "ARR including products we haven't bought yet"
  → Counter: "ARR from [your product] only"
- ❌ Don't accept: "Revenue from other business lines"
  → Counter: "Revenue from customers we identify before close"

---

### Structure 2: EBITDA / Profitability Milestone

**What it is**: You get paid if earnings (operating profit) hit targets.

```
Example:
  Cash at close: $10M
  Earnout Year 1:
    - If EBITDA >$1M → $1.5M bonus
    - If EBITDA >$2M → $2.5M bonus
  Year 2:
    - If EBITDA >$3M → $2M bonus
```

**Pros:**
- Buyer can't grow you into loss (they manage costs)
- Rewards profitability, not just revenue

**Cons:**
- Buyer controls all expenses (can cut your team to hit EBITDA)
- Buyer defines what's "EBITDA" (grey areas)
- You lose control of investments

**Red flags:**
- ❌ Don't accept: "EBITDA = revenue - all operating expenses"
  → Counter: "Normalized EBITDA excluding one-time items + synergy costs"
- ❌ Don't accept: "Buyer can eliminate your team post-close"
  → Counter: "If earn-out targets require your team, can't reduce payroll"

---

### Structure 3: Customer Retention Earnout

**What it is**: You get paid if customers stick around.

```
Example:
  Cash at close: $10M
  Earnout Year 1:
    - If >90% of customers stay → $3M bonus
    - If >95% of customers stay → $4M bonus (vs. baseline expectation of 85%)
```

**Pros:**
- Buyer incentivizes keeping your customers (good for you)
- Aligns with reality (your job post-close is retention)
- Protects you from churn risk

**Cons:**
- Buyer can't let customers leave even if non-strategic (locks them in)
- Hard to measure fairly (what counts as "customer" vs. downgrade?)

**Red flags:**
- ❌ Don't accept: "90% retention means zero churn month-over-month"
  → Counter: "Annual retention = ending ARR / starting ARR"
- ❌ Don't accept: "Buyer's cost-cutting kills retention, but you pay the price"
  → Counter: "If buyer reduces support, cap liability"

---

### Structure 4: Product Milestone Earnout

**What it is**: You get paid if product features are built / adopted.

```
Example:
  Cash at close: $10M
  Earnout Year 1:
    - If [Feature X] shipped + [Y] customers use it → $2M
    - If API integration completed → $1M
  Year 2:
    - If [Product Y] launched → $2M
```

**Pros:**
- Ensures buyer invests in YOUR product (not abandonment)
- Objective measure

**Cons:**
- Buyer can "ship feature but nobody uses it" (game the system)
- Product roadmap priorities shift (not your control)
- Hard to measure adoption fairly

**Red flags:**
- ❌ Don't accept: "Feature shipped" (even if broken)
  → Counter: "Feature shipped AND 50%+ customers activated"
- ❌ Don't accept: "Buyer decides what counts as shipped"
  → Counter: "Shipped = live in production, >90% uptime, no critical bugs"

---

### Structure 5: Blended Earnout

**What it is**: Combination of 2+ metrics above.

```
Example (most common):
  Cash at close: $8M
  Earnout Year 1 (Year 2 similar):
    - 50% if ARR hits $12M
    - 30% if customer retention >92%
    - 20% if EBITDA >$1M
    
  Result: Multiple paths to earn 100% earnout, not "all or nothing"
```

**Pros:**
- Buyer and you both have influence (shared incentive)
- Protects you from single-metric risk
- More realistic

**Cons:**
- Complex calculation (disputes likely)
- Hard to understand and communicate

**Red flags:** Ensure total earnout target is clear and achievable.

---

## Earnout Negotiation Tactics

### Tactic 1: Propose Double-Sided Earnout
```
Standard: You get $X if ARR hits $15M

Better (win-win):
  - If ARR > $15M: You get $5M + [bonus 10% of incremental revenue]
  - If ARR $12-15M: You get $2.5M (partial credit)
  - If ARR < $12M: You get $1M (downside protection)

Why: Buyer wins if you over-perform, you get floor.
```

### Tactic 2: Tie Earnout to Metrics Buyer Controls
```
Bad: "ARR must hit $15M" 
  → Buyer reduced sales team, ARR falls, you lose earnout

Better: "Revenue from customers signed before close" 
  OR "NRR must be >95%" (you control this via product)
```

### Tactic 3: Build in Escalators
```
Example:
  Year 1: Hit $12M → $2M earnout
  Year 2: Hit $15M → $3M earnout (not "additional $3M", refresh level)
  
  Why: Earnout targets rise as buyer scale grows
```

### Tactic 4: Escrow as Backup
```
If earnout too risky:
  - Get 50% cash at close + 50% in escrow
  - Escrow released: 50% after year 1, 50% after year 2
  - Better than earnout (guaranteed vs. contingent)
```

---

## Red Flags: Earnouts NOT to Accept

| Red Flag | Why Bad | Your Counter |
|----------|---------|--------------|
| "Earnout if buyer's CFO approves" | No objective measure | "If targets hit, payout automatic" |
| "Earnout funded from synergies" | If synergies don't materialize, you don't get paid | "Funded from [revenue/EBITDA] regardless" |
| "Seller must work to earn earnout" (implied) | You become employee, no security | "Earnout independent of role" |
| "No cap on what counts as revenue" | Buyer can shift definitions | "Revenue = [specific customer types/products]" |
| "Earnout vests only if you're still employed" | Buyer can fire you, you lose earnout | "Earnout paid regardless of employment" |

---

## Earnout Payout Timeline (Negotiate These)

### Timeline 1: Annual Payment (Typical)
```
Close: June 2026
Year 1 earnout earned: Dec 2026 (hits revenue target)
Payout: Jan 2027

Pro: Faster feedback
Con: If you miss, another chance in Year 2
```

### Timeline 2: Deferred Annual (Safer)
```
Close: June 2026
Year 1 measurement: Dec 2026
Payout: Jan 2028 (delayed 12 months from earn date)

Pro: Buyer ensures no refund needed later
Con: You wait longer for cash
```

### Timeline 3: Lump Sum at End (Riskiest)
```
Close: June 2026
Year 1 & 2 combined: Dec 2027
Payout: Jan 2028

Pro: One payment, simpler
Con: If miss Year 1, no progress on Year 2
```

**Recommend**: Annual payment + 30-day holdback (for audit verification).

---

## Earnout Caps & Collars (What to Negotiate)

### Cap (Maximum you can earn)
```
Example: "Earnout capped at $5M"
Meaning: Even if you over-perform, max payout is $5M

Buyer wants: Limit their liability
You want: No cap (you outperformed, deserve it)

Compromise: No hard cap, but "shared upside" model
  - Above $15M: Earnout = 50% of the excess
  - Example: Hit $17M → $5M + (50% × $2M) = $6M earnout
```

### Floor (Minimum you can earn)
```
Example: "If you hit >80% of target, you get 50% earnout"
Meaning: Partial credit for near-misses

You want: Floor protection (don't lose everything for 5% miss)
Buyer wants: Binary (all or nothing)

Compromise: Stepped earnout
  - 90-100% of target = 100% earnout
  - 80-90% of target = 50% earnout
  - <80% = $0 (hard floor)
```

---

## Dispute Prevention (Critical)

### Dispute: "The number buyer reported doesn't match our records"

**Prevention**:
- [ ] Define revenue exactly: "Trailing 12-month ARR per customer invoice dates"
- [ ] Audit process: "Independent accounting firm audits annually"
- [ ] Dispute window: "30 days after earnout report to object"
- [ ] Tie-breaker: "If dispute, average of both calculations"

### Dispute: "Buyer didn't invest in our product, sabotaged earnout"

**Prevention**:
- [ ] Product roadmap locked for Year 1 (separate agreement)
- [ ] Minimum headcount: "Must maintain [X] engineers on product"
- [ ] Earnout metric tied to seller's control (NRR, customer health, not just revenue)

### Dispute: "Buyer cut costs post-close, killed EBITDA earnout"

**Prevention**:
- [ ] Define "normalized EBITDA" excluding one-time costs
- [ ] Specify what counts: "PayPal engineering costs, but not buyer's G&A allocation"
- [ ] Create formula: "Revenue × [X]% gross margin, minus [specific expenses]"

---

## Earnout Negotiation Cheat Sheet

**Your ask** (high anchor):
```
$12M cash + $8M earnout (weighted):
  - 40% ARR hit $20M by Dec 2027
  - 30% Customer retention >95%
  - 20% EBITDA margin >15%
  - 10% Product milestones (shipped 3 features)
```

**Walk-away** (low floor):
```
$15M cash + $3M earnout (simple):
  - 100% if ARR hits $16M in year 1
  - Or equivalent in different metric
  - Paid annually, no cap
  - Independent audit, 30-day dispute window
```

**Preferred middle ground** (what you'd accept):
```
$13M cash + $5M earnout:
  - 50% based on ARR growth (80% of target = 50% payout)
  - 30% customer retention bonus
  - 20% floor payment (minimum $1M)
  - Paid by Jan 31 of following year
  - Earnout paid regardless of role/employment
```

---

## Quick Checklist: Is This Earnout OK?

✅ Accept if:
- [ ] Metric is within seller's control (NRR, customer retention)
- [ ] Payment automatic upon achievement (no board vote needed)
- [ ] Dispute resolution is clear
- [ ] You get 30-50% of total deal as earnout (reasonable)
- [ ] Earnout period is 1-2 years (not 3+)

❌ Reject if:
- [ ] Metric buyer controls (EBITDA, cost cuts)
- [ ] "At buyer's discretion" language anywhere
- [ ] No cap on earnout payment (buyer can claim you owe)
- [ ] Earnout requires you to stay employed (implicitly)
- [ ] Earnout period > 2 years (unlikely to hit targets)

**Use case**: Before LOI signing, confirm earnout terms make sense.
