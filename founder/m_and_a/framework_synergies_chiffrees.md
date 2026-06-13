---
name: framework-synergies-chiffrees
description: Framework pour identifier et chiffrer synergies (revenue + cost) avec acquéreur
metadata:
  type: reference
  created: 2026-06-13
---

# Framework Synergies Chiffrées

**Goal**: Quantify what you're worth to *this specific buyer* (often 20–50% more than standalone value).

---

## REVENUE SYNERGIES (30–60% of total)

### 1. Cross-Selling to Buyer's Customer Base

**Question**: How many of buyer's customers would benefit from your product?

**Calculation**:
- Buyer's customer base: [#] customers
- % likely to adopt your product: [X]%
- Average deal size with your product: $[Y]
- Uptake timeline: [24 months]

**Result**:
```
Buyer's customers: 5,000
Likely adoption: 30%
Deal size: $50K
Timeline: 24 months to full adoption

Revenue synergy: (5,000 × 30% × $50K) / 24 = $31.25M ARR
```

**Impact on price**: If buyer sees $31M revenue upside, they can justify paying you $10M–$15M more.

---

### 2. Upselling to Your Customers

**Question**: What else can buyer sell to your customers?

**Calculation**:
- Your customers: [#]
- Avg new product adoption: [X]%
- ARPU (additional) from buyer's product: $[Y]/customer/year
- Adoption timeline: [12–36 months]

**Result**:
```
Your customers: 200
Likely to buy buyer's product: 50%
ARPU (buyer's other product): $30K
Timeline: 12 months

Revenue synergy: 200 × 50% × $30K = $3M/year
```

---

### 3. Entering New Markets

**Question**: Can your product serve buyer's adjacent markets?

**Example**:
- Your product: vertical-specific (e.g., construction software)
- Buyer serves [3 verticals]
- Your product applicable to [other 2 verticals]
- TAM in those verticals: $[X]M
- Realistic capture: [X]%

**Result**:
```
New verticals TAM: $500M
Realistic capture (year 3): 2%
Annual revenue opportunity: $10M
```

---

## COST SYNERGIES (40–70% of total)

### 1. R&D Efficiency

**Question**: How much do both companies spend on R&D?

**Calculation**:
- Your R&D: $[X]M/year
- Buyer's R&D: $[Y]M/year
- Overlap to eliminate: [Z]%
- Annual savings: (X + Y) × Z%

**Example**:
```
Your R&D: $1M/year
Buyer's R&D: $5M/year
Eliminate overlap: 30%

Annual savings: ($1M + $5M) × 30% = $1.8M/year
```

---

### 2. Sales & Marketing Consolidation

**Question**: Can buyer's sales team sell your product? Can you piggyback on their brand?

**Calculation**:
- Your S&M spend: $[X]M/year
- % you can eliminate (use buyer's team instead): [Y]%
- Annual savings: X × Y%

**Example**:
```
Your S&M spend: $2M/year
Can eliminate (buyer takes over): 60%

Annual savings: $2M × 60% = $1.2M/year
```

---

### 3. Infrastructure & Operations

**Question**: Can you consolidate clouds, offices, tools?

**Calculation**:
- Your infrastructure cost: $[X]M/year
- Buyer's infrastructure cost: $[Y]M/year
- Duplication: [Z]%
- Annual savings: (X + Y) × Z%

**Example**:
```
Your cloud cost: $500K/year
Buyer's cloud cost: $2M/year
Eliminate duplication: 40%

Annual savings: ($500K + $2M) × 40% = $1M/year
```

---

### 4. Back-Office Consolidation (HR, Finance, Legal)

**Calculation**:
- Your admin/ops headcount: [# FTE]
- Cost per FTE: $[X]/year
- % overlap with buyer: [Z]%
- Annual savings: (# FTE × X) × Z%

**Example**:
```
Your finance/HR/legal team: 3 FTE
Cost per FTE: $150K
Eliminate overlap: 50%

Annual savings: 3 × $150K × 50% = $225K/year
```

---

## TOTAL SYNERGY CALCULATION

| Synergy | Year 1 | Year 2 | Year 3 | 3-Year Total |
|---------|--------|--------|--------|--------------|
| **Cross-sell to buyer's base** | $5M | $20M | $31M | $56M |
| **Upsell to your customers** | $1M | $2M | $3M | $6M |
| **New market entry** | $0 | $2M | $10M | $12M |
| **R&D savings** | $1.8M | $1.8M | $1.8M | $5.4M |
| **S&M savings** | $1.2M | $1.2M | $1.2M | $3.6M |
| **Infrastructure savings** | $1M | $1M | $1M | $3M |
| **Back-office savings** | $225K | $225K | $225K | $675K |
| **TOTAL** | **$10.2M** | **$28.2M** | **$48.2M** | **$86.6M** |

---

## TRANSLATING TO VALUATION PREMIUM

**3-year synergy value: $86.6M**

Apply a **discount for integration risk** (buyer expects 30–50% of synergies won't materialize):

```
Conservative case: $86.6M × 50% = $43.3M synergy value
Mid case: $86.6M × 65% = $56.3M synergy value
Optimistic: $86.6M × 80% = $69.3M synergy value
```

**This justifies a price uplift to buyer of:**
```
Buyer can pay up to:
- 30% of synergy value in Year 1 = $43.3M × 30% = $13M premium
- Or split 50/50 with seller: $43.3M × 50% = $21.6M premium
```

---

## NEGOTIATION TACTIC

**Use synergies to justify price in LOI:**

```
Email to buyer:

"We've identified $[X]M in identifiable synergies over 3 years:
- Cross-sell to your [#] customers: $[X]M
- R&D consolidation: $[X]M
- S&M efficiency: $[X]M
- New market entry: $[X]M

Even at 50% realization, that's $[Y]M. We think a fair 
acquisition price reflects [X]% of these synergies accruing to us.

This supports our ask of $[price]."
```

---

## SANITY CHECKS

- Synergy numbers should be **conservative**, not aspirational
- Risk discount should be **30–50%** (be realistic about integration)
- Buyer typically gets **50–70%** of synergies; you get 30–50%
- If buyer claims synergies are double what you calculated, **be skeptical**

