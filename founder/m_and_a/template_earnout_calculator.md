# Earnout Calculator — Deal Structure Generator

## Formula Templates

### 1. **Revenue-based Earnout** (most common)
```
Earnout = Base × (Actual Revenue / Target Revenue) × Payout %
```
**Example:**
- Base purchase price: $5M cash at close
- Earnout target: Additional $1M if you hit $10M ARR (from $8M at close) in 24 months
- Payout: $1M × (Actual Revenue / $10M) × 100% (linear)

| Month 0 | Actual Revenue | Progress to $10M | Earned | Paid (if monthly) |
|---|---|---|---|---|
| Close | $8.0M | 80% | $0 | $0 |
| +6m | $8.5M | 85% | $50k | $50k |
| +12m | $9.0M | 90% | $100k | $50k |
| +18m | $9.5M | 95% | $150k | $50k |
| +24m | $10.5M | 105% | $150k (capped) | $0 (final) |

**Pros:** Aligns seller with growth, buyer sees value creation  
**Cons:** Seller depends on buyer execution

---

### 2. **EBITDA-based Earnout** (for mature businesses)
```
Earnout = (Actual EBITDA - Target EBITDA) × Payout % × Holdback Period
```
**Example:**
- Target EBITDA: $2M at year 1 post-close
- Earnout: $250k if actual EBITDA ≥ $2.2M
- Payout: 100% × (Actual EBITDA – $2M) / $2M, max $250k

| Scenario | EBITDA | Earnout % | Amount |
|---|---|---|---|
| Below target | $1.9M | 0% | $0 |
| On target | $2.0M | 0% | $0 |
| +10% beat | $2.2M | 100% | $250k (capped) |
| +20% beat | $2.4M | 100% | $250k (capped) |

---

### 3. **Milestone-based Earnout** (product launches, KPIs)
```
Earnout = Sum of milestone payments if each condition met
```
**Example:**
- $200k if product feature X launches by Q4
- $150k if NPS ≥ 70
- $150k if customer churn < 5% annual
- **Total possible:** $500k over 18 months

| Milestone | Target | Proof Required | Payout | Timeline |
|---|---|---|---|---|
| Feature launch | RTM by 2026-Q4 | Roadmap + demo | $200k | 18m from close |
| NPS threshold | ≥70 | Annual survey | $150k | 12m from close |
| Churn target | <5% annual | Monthly reports | $150k | 24m from close |

---

### 4. **Tiered Earnout** (Buyer-friendly risk mitigation)
```
Year 1: 50% of earned
Year 2: 50% of year 1 + remainder
```
**Example: $1M earnout pool**
- Year 1 (Month 0–12): Earn up to $500k, seller gets $250k immediately
- Year 2 (Month 12–24): Remaining $500k + year 1 holdback paid if conditions met

**Pro:** Buyer reduces risk of seller departure; seller gets some cash sooner

---

## Negotiation Playbook

| Buyer Says | Seller Counter | Rationale |
|---|---|---|
| "Earnout should be 50% of price" | "30% max; I'm confident, not hopeful" | At 50%, you're betting seller's execution, not buyer's |
| "Earnout vests over 36 months" | "24 months max; 36m = no founder incentive" | Founder focus decreases after 24m; buyer has full control |
| "We measure success on EBITDA, not revenue" | "Revenue is fine; EBITDA too dependent on buyer cost cuts" | Buyer might slash headcount = false negatives |
| "Earnout is capped at 90% of commitment" | "100% or I walk; you control the levers" | If buyer fails on ops, you shouldn't subsidize their mistakes |
| "Earnout only paid if 80%+ target hit" | "Pro-rata payout starting at 80%; or revenue-based instead" | Cliff structures are founder-unfriendly |

---

## Tax Planning (US / Investor)

**Deferred payment risk:**
- Earnout = ordinary income, taxed in year earned (not at close)
- If $500k earnout over 24m: ~$250k tax liability deferred 24m
- **Plan:** Keep 40% in escrow for taxes, release at milestone

**Earnout + Section 1202 planning:**
- Capital gains treatment only on purchase price at close
- Earnout taxed as ordinary income (unless structured as "contingent proceeds")
- Consult tax attorney to maximize cap gains vs. ordinary income split

---

## Red Flags

⚠️ Buyer wants to measure earnout on metrics they control (cost cuts, headcount):
- Counter: Revenue or net retention only

⚠️ Earnout vests based on "buyer discretion":
- Counter: Objective, third-party verified metrics only

⚠️ No earnout documentation (handshake deal):
- Counter: Formal schedule in purchase agreement, with escrow

⚠️ Earnout holdback in buyer's account, not escrow:
- Counter: Escrow with neutral third party (title company, bank)
