# Synergy Analysis Framework

**Utilité** : quantifier où buyer obtient valeur (justifie premium; détermine earnout).

---

## Catégories de Synergies (30+ axes)

### A. Revenue Synergies (Cross-Sell)

| Synergy | Mechanism | Example | Year 1 Impact |
|---------|-----------|---------|---------------|
| Customer cross-sell | Your prod → buyer's 500k base | "Sell your $2k/month module to buyer's customers @ 20% adoption" | +$20M ARR |
| Geographic expansion | Product to new regions buyer serves | "Expand to EMEA via buyer's offices (currently US-only)" | +$8M ARR |
| Vertical expansion | Buyer's vertical gets your product | "Adapt for manufacturing; buyer has 50k mfg customers" | +$12M ARR |
| Upsell bundling | Package your prod + buyer's suite | "$50M → $65M bundle; 10% attach rate" | +$1.5M ARR |
| Land + expand | Use your sticky product to land, buyer expands | "Your product lands; buyer sells 3–5x more revenue per customer" | +$5M ARR |

**Conservative assumption** : 10–20% of target customer base adopts in year 1.

### B. Cost Synergies (Consolidation)

| Synergy | Cost Savings | Impact | Notes |
|---------|--------------|--------|-------|
| Sales overlap elimination | One CRO instead of two | $500k/year | Consolidate sales teams, close duplicates |
| G&A consolidation | CFO, controller, HR → shared | $1.5M/year | Merge finance/HR with buyer |
| Duplicate functions | Support, ops, legal → shared | $2M/year | Buyer absorbs your ops team |
| Cloud/infrastructure deduplication | Consolidate AWS, data warehouses | $800k/year | Run on buyer's stack → save licensing |
| Marketing streamline | Stop buyer duplicate campaigns | $600k/year | Marketing efficiency |
| **Total G&A elimination** | | **$5.3M/year** | |

**Typical cost synergy** : 10–15% of combined OpEx.

### C. Technology Synergies

| Synergy | Value | Timeline |
|---------|-------|----------|
| Accelerate product roadmap | Save 6–12 months R&D → faster market reach | Year 1–2 |
| Reduce technical debt | Consolidate code bases, eliminate legacy | Year 1–2 |
| Data moat enhancement | Combine data assets → stronger ML | Year 1–2 |
| API/integration leverage | Your API becomes buyer's standard | Year 1–2 |
| Security/compliance alignment | Merge compliance programs, reduce audit cost | Year 1 |

---

## Template: $5M ARR SaaS Deal

**ASSUMPTIONS:**
- Your ARR: $5M, growth 50%, margin 40%
- Buyer: $200M ARR, 50k customers, enterprise-focused
- Buyer margin: 60%
- Consolidation cost: $2M (one-time, year 1)

---

### REVENUE SYNERGIES (Year 1–3 projection)

```
1. CROSS-SELL TO BUYER'S CUSTOMER BASE

   Buyer's customer base: 50,000 accounts
   Your product fit: "Manages [X] problem that 40% of buyer's base has"
   
   Year 1:
   - Target: 1% adoption = 500 customers × $2k/month = $12M ARR (on annualized basis)
   - But realistic ramp: Q1 launch → Q2–Q4 sales → 3–4 months average time-to-revenue
   - Conservative year 1 capture: $6M ARR (half year ramp)
   
   Year 2:
   - 3% adoption (network effects, integration) = $30M ARR gross
   - Year 2 capture: +$18M ARR
   
   Year 3:
   - 5% adoption (mature) = $50M ARR
   - Year 3 capture: +$20M ARR (incremental)

CROSS-SELL FORECAST:
   Year 1: $6M (conservative)
   Year 2: +$18M (acceleration)
   Year 3: +$20M (sustained)

2. GEOGRAPHIC EXPANSION

   Your footprint: US only ($5M ARR)
   Buyer footprint: US + EMEA + APAC
   
   Expansion via buyer:
   - EMEA: 30% of US revenue potential = $1.5M → Year 1 = $750k (ramp)
   - APAC: 20% of US potential = $1M → Year 1 = $500k (ramp)
   
   Year 1 geographic upside: +$1.25M ARR

3. VERTICAL EXPANSION

   Your vertical: SaaS/tech only
   Buyer's verticals: Finance, Healthcare, Insurance
   
   Adaptation cost: $500k
   Healthcare fit: Medium (requires compliance work)
   - Addressable: $200k/year → Year 1 = $50k
   
   Finance fit: High (quick to adapt)
   - Addressable: $500k/year → Year 1 = $250k
   
   Year 1 vertical upside: +$300k ARR

TOTAL REVENUE SYNERGIES, YEAR 1: $6M + $1.25M + $0.3M = $7.55M ARR
```

---

### COST SYNERGIES (Year 1–2)

```
1. SALES FUNCTION CONSOLIDATION

   Your sales: $1.5M/year (1 VP Sales, 2 AEs, 1 SDR)
   Buyer sales: 50-person team, $15M/year
   
   Overlap: VPs of Sales, some customer segments
   - Consolidate your 3 AEs into buyer's org → save $400k
   - Eliminate your VP Sales → save $250k
   - Share SDR pool → save $150k
   
   Year 1 sales savings: -$800k

2. G&A CONSOLIDATION

   Your G&A: $2M/year (CFO, controller, HR, legal)
   Buyer already has: Full finance/HR/legal teams
   
   Eliminate redundancy:
   - Your CFO role: absorbed into buyer's finance → -$300k
   - Controller: merged → -$200k
   - HR shared services: -$150k
   - Legal: buyer's counsel → -$100k
   - Consolidation cost (severance, transition): +$500k one-time
   
   Net year 1: -$750k + $500k = -$250k
   Net year 2+: -$750k/year sustainable

3. TECHNOLOGY COST CONSOLIDATION

   Your infrastructure: $800k/year (AWS, data warehouse, licensing)
   Consolidate onto buyer's stack:
   - AWS consolidation → -$300k
   - Data warehouse → -$250k
   - Software licenses → -$150k
   - Migration cost: +$200k one-time
   
   Net year 1: -$700k + $200k = -$500k
   Net year 2+: -$700k sustainable

4. MARKETING OPTIMIZATION

   Your marketing: $600k/year
   Buyer already markets to your target → eliminate paid campaigns
   - Buyer absorbs your customer acquisition
   - Save paid ads, event sponsorships → -$300k
   - Keep product marketing content → -$100k
   
   Net savings: -$400k

TOTAL COST SYNERGIES:
   Year 1: $800k + $250k + $500k + $400k = $1.95M (net of consolidation $700k) = $1.25M
   Year 2+: $800k + $750k + $700k + $400k = $2.65M
```

---

### VALUATION IMPACT

```
SYNERGY VALUATION FORMULA:

Synergy Value = (Revenue Synergies × EBITDA Margin + Cost Synergies) / Discount Rate

INPUTS:
- Revenue synergies year 1: $7.55M
- Synergy EBITDA margin: 60% (high margin, faster capture)
- Cost synergies year 1: $1.25M
- Discount rate (buyer's WACC): 10%
- Sustainable synergy year 2+: $8M/year ($3M cost + $5M revenue synergy)

CALCULATION:
Year 1 synergy EBITDA:
  = ($7.55M × 60%) + $1.25M = $4.53M + $1.25M = $5.78M

Sustainable synergy (years 2+):
  = ($5M × 60%) + $2.65M = $3M + $2.65M = $5.65M

NPV of synergies (perpetual growth model):
  = $5.78M (Y1) / 1.10 + $5.65M (perpetuity) / (0.10 × 1.10)
  = $5.25M + $51.4M = $56.65M

SYNERGY VALUATION: ~$55–60M

This justifies buyer paying:
  - Base valuation: $5M ARR × 6x = $30M
  + Synergy premium: +$55M
  = Total: ~$85M (17x ARR!)

But buyer won't capture all synergies:
  - Realistic capture: 50% = $27.5M synergy value
  = Justified price: $30M + $27.5M = $57.5M (~11x ARR)

TARGET NEGOTIATION RANGE: $50–65M
```

---

## Key Synergy Scenarios

| Scenario | Revenue Synergies | Cost Synergies | Total Synergy Value | Justified Price |
|----------|------------------|-----------------|---------------------|-----------------|
| **Conservative** (30% capture) | $3M | $1.5M | $12M | $36M (7x) |
| **Base Case** (50% capture) | $5M | $2.5M | $27M | $57M (11x) |
| **Optimistic** (75% capture) | $7M | $3.5M | $45M | $75M (15x) |

---

## Red Flags (Synergies Don't Materialize)

🚩 Revenue synergies slow if:
- Buyer's sales team unmotivated (compensation misaligned)
- Your product requires training (adoption friction)
- Customer overlap overstated

🚩 Cost synergies blocked if:
- Buyer's teams protective of headcount
- Regulatory/union constraints (can't eliminate roles)
- Consolidation more expensive than estimated

---

## Earnout Structure (Align Incentives)

```
EARNOUT TRIGGER = capture of synergies

Base deal: $50M cash

Earnout:
- If $4M+ revenue synergies captured in year 1 → +$5M earnout
- If $2.5M+ cost synergies realized → +$2.5M earnout
- Max earnout: +$7.5M

This aligns founder incentive (stay, make synergies work) with buyer's value (capture promised upside)
```

---

## Communicating to Buyer

```
"We've modeled $55M of synergy value from:
  • $7.5M cross-sell revenue (conservative 1% adoption of your 50k base)
  • $2.6M annual cost savings (G&A consolidation)
  
At 50% capture rate, that's $27.5M of value for you.
Justifies a price of ~$55–65M for the $5M ARR business.

We're comfortable with earnout tied to synergy realization — 
let's both succeed on this."
```
