---
name: keep_separate_vs_merge_decision
description: Scoring matrix to decide whether to keep acquired company separate or merge (with examples)
version: 1.0
date: 2026-06-12
---

# KEEP SEPARATE VS MERGE — DECISION MATRIX

**Score your acquisition. Determines: valuation, earnout structure, integration roadmap.**

---

## QUICK SCORING (5 MINUTES)

Rate each factor 1-5 (1=Keep Separate | 5=Merge):

| Factor | Score (1-5) | Your Answer | Reasoning |
|--------|------------|-------------|-----------|
| **Product overlap with acquirer's product?** | [1-5] | | 1=Unique, 5=Duplicate |
| **Sales channel alignment?** | [1-5] | | 1=Different ICP, 5=Identical targets |
| **Technology stack compatibility?** | [1-5] | | 1=Incompatible, 5=Drop-in integration |
| **Customer base overlap?** | [1-5] | | 1=No overlap, 5=100% overlap |
| **Brand identity value?** | [1-5] | | 1=Critical to keep, 5=Generic brand |
| **Team skill complementarity?** | [1-5] | | 1=Specialized, 5=Overlapping roles |
| **Cost savings potential?** | [1-5] | | 1=None, 5=High (shared infra, sales, G&A) |
| **Integration risk?** | [1-5] | | 1=Prohibitive risk, 5=Low risk |
| **Speed to market (post-acquisition)?** | [1-5] | | 1=Keep separate = faster, 5=Merge = faster |
| **Acquirer's strategic reason?** | [1-5] | | 1=Keep separate, 5=Full integration |

**Total Score: [____] / 50**

| Score | Recommendation |
|-------|---|
| **10-20** | **KEEP SEPARATE** (independent P&L, brand, team) |
| **21-35** | **HYBRID** (maintain product, share ops) |
| **36-50** | **MERGE** (consolidate fully) |

---

## DETAILED FRAMEWORK

### 1. PRODUCT ARCHITECTURE

**Score: 1-5 (1=Keep separate, 5=Merge)**

#### Keep Separate (Score 1-2):
```
✓ Product is fundamentally different
✓ Complements acquirer's product without cannibalizing
✓ Serves different use case / workflow
✓ Has independent value for acquirer's customers

Example: Acquirer = CRM. You = AI email writer.
→ Keep separate; bundle as add-on.
```

#### Merge (Score 4-5):
```
✓ Product is direct replacement for existing feature
✓ Same workflow, different implementation
✓ Could consolidate into acquirer's product
✓ Doing so saves engineering effort

Example: Acquirer = Analytics dashboard. You = Analytics dashboard.
→ Merge; pick best implementation.
```

---

### 2. CUSTOMER SEGMENT ALIGNMENT

**Score: 1-5 (1=Different ICP, 5=Identical)**

#### Keep Separate (Score 1-2):
```
Your ICP: [industry/size/segment]
Acquirer ICP: [different industry/size/segment]

Overlap: <30%

→ Keep separate sales team, marketing, support.
→ Cross-sell opportunity but distinct go-to-market.

Example: You serve SMB agencies. Acquirer serves enterprise finance.
```

#### Merge (Score 4-5):
```
Your ICP: [industry/size/segment]
Acquirer ICP: [same]

Overlap: >70%

→ Merge sales team, marketing, support.
→ 1-2 sales team handles both products.

Example: Both serve mid-market SaaS companies.
```

---

### 3. TECHNOLOGY COMPATIBILITY

**Score: 1-5 (1=Incompatible, 5=Drop-in)**

#### Keep Separate (Score 1-2):
```
Your tech: [stack details]
Acquirer tech: [stack details]

Compatibility:
□ Different databases (migrating data is risky)
□ Different languages (hard to consolidate team)
□ Different infrastructure (separate deploy pipelines)
□ API integrations required (but not seamless)

Merge cost estimate: $[500k-2M] in engineering effort
Merge timeline: 9-18 months

→ Keep separate; integrate via APIs.
```

#### Merge (Score 4-5):
```
Your tech: [stack details]
Acquirer tech: [same stack]

Compatibility:
✓ Same language, database, infra
✓ Easy to consolidate teams
✓ Code can be merged with minimal refactor
✓ Shared infrastructure (same CDN, region, etc.)

Merge cost estimate: $[100-300k] in engineering effort
Merge timeline: 3-6 months

→ Merge immediately; consolidate teams.
```

---

### 4. CUSTOMER BASE OVERLAP

**Score: 1-5 (1=No overlap, 5=100% overlap)**

#### Keep Separate (Score 1-2):
```
Your top 10 customers vs. Acquirer's top 10 customers:
Overlap: <20% (mostly different customers)

→ Keep separate product, sales, support.
→ Cross-sell becomes growth lever.

Example: You = Slack apps. Acquirer = Salesforce.
Some overlap, but many Salesforce customers don't use Slack.
Keep separate, cross-sell aggressively.
```

#### Merge (Score 4-5):
```
Your top 10 customers vs. Acquirer's top 10 customers:
Overlap: >80% (same customers)

→ Merge product, sales, support.
→ Consolidating reduces friction, improves UX.

Example: You = Email marketing. Acquirer = HubSpot.
HubSpot customers expect email in HubSpot, not separate tool.
Merge immediately.
```

---

### 5. TEAM & ORGANIZATIONAL FIT

**Score: 1-5 (1=Specialized team needed, 5=Overlapping roles)**

#### Keep Separate (Score 1-2):
```
Your team: [specialized skills]
Acquirer team: [different skills]

Examples:
- You have ML engineers; acquirer doesn't → keep team intact
- You have domain experts (healthcare compliance); acquirer lacks this → keep separate
- Team has strong product vision; better as independent P&L

Org structure: [YourCo] + [Acquirer] as two units
Integration: Loose (API integration, shared finance/legal only)
```

#### Merge (Score 4-5):
```
Your team: [similar skills to acquirer]
Acquirer team: [same skills]

Examples:
- Both have React engineers → consolidate frontend team
- Both have data engineers → consolidate data stack
- Roles overlap significantly → merge teams

Org structure: Flattened (consolidate overlapping roles)
Integration: Deep (shared teams, shared roadmap)
```

---

### 6. SYNERGY POTENTIAL (Cost Savings)

**Score: 1-5 (1=No synergies, 5=High synergies)**

#### Keep Separate (Score 1-2):
```
Potential cost savings: <10% of combined costs

Reasons:
□ Different infrastructure (can't consolidate)
□ Different support teams (different expertise)
□ Different sales channels (separate reps needed)

Example: You = B2B product. Acquirer = B2C product.
Can't merge sales, support, or marketing. Keep separate.
```

#### Merge (Score 4-5):
```
Potential cost savings: >30% of combined costs

Synergies:
✓ Shared infrastructure (one AWS account, one Kubernetes cluster)
✓ Consolidated support team (train once, support both)
✓ Shared sales team (1 rep sells both products)
✓ Consolidated G&A (shared finance, legal, HR)

Cost reduction estimate: $[X] in Year 1, $[Y] in Year 2

Example: You = Analytics v2. Acquirer = Analytics v1.
Merge immediately. Share team, infra, support. Save $500k/year in G&A.
```

---

### 7. BRAND & MARKET POSITIONING

**Score: 1-5 (1=Keep brand, 5=Rebrand/consolidate)**

#### Keep Separate (Score 1-2):
```
Your brand: Recognizable, valued by customers
Acquirer brand: Different market positioning

Examples:
- You = premium brand; acquirer = mass market → keep separate
- You have high brand loyalty; customers came for YOUR product → keep brand
- You serve different segment; rebranding would confuse → keep separate

Recommendation: Keep [YourCo] as independent brand, sub-brand of acquirer.
```

#### Merge (Score 4-5):
```
Your brand: Not critical to customers
Acquirer brand: Stronger in market

Examples:
- Customers care about product, not brand → merge under acquirer brand
- Acquirer brand is stronger → leverage for co-marketing
- Product feature, not standalone service → rebrand as acquirer feature

Recommendation: Consolidate under acquirer brand. Stop marketing [YourCo] name.
```

---

## COMBINED SCENARIO ANALYSIS

### Scenario A: Keep Separate
**Best for:** Different products, overlapping customers, distinct brands.

```
Year 1 Financials (Post-Close):
├─ [YourCo] P&L: Independent
├─ Shared Services: Finance, Legal, HR only
├─ Cost Structure: Largely unchanged
│
├─ Revenue: $[baseline]M + $[cross-sell upside]M = $[X]M
├─ Costs: $[baseline] (no synergies) = $[Y]M
├─ EBITDA: [Y]% margin

Synergy Realization: Slow (12-24 months for cross-sell)
Team Churn Risk: Low (team remains intact)
Integration Risk: Low
Customer Retention: High (no disruption)

Valuation Impact: +0% (reflects keep-separate strategy)
Earnout Structure: Easier (own P&L, easy metrics)
```

### Scenario B: Hybrid (Moderate Integration)
**Best for:** Complementary products, some team consolidation, shared ops.

```
Year 1 Financials (Post-Close):
├─ [YourCo] P&L: Blended with shared services
├─ Shared Services: Finance, Legal, HR, Support
├─ Product: Remains separate, but shared infrastructure
│
├─ Revenue: $[baseline]M + $[cross-sell]M = $[X]M
├─ Costs: $[baseline] - $[synergies]M = $[Y]M
├─ EBITDA: [Y]% margin (improves by 5-10%)

Synergy Realization: Moderate (8-12 months)
Team Churn Risk: Moderate (some consolidation)
Integration Risk: Moderate
Customer Retention: High (product unchanged)

Valuation Impact: +10-15% (synergy upside)
Earnout Structure: Moderate (blended metrics)
```

### Scenario C: Full Merge
**Best for:** Similar products, overlapping teams, consolidation benefits.

```
Year 1 Financials (Post-Close):
├─ [YourCo] merged into acquirer
├─ No separate P&L
├─ Shared: Everything (product, team, ops, support)
│
├─ Revenue: $[baseline + integration gains]M = $[X]M
├─ Costs: $[baseline] - $[major synergies]M = $[Y]M
├─ EBITDA: [Y]% margin (improves by 15-30%)

Synergy Realization: Fast (3-6 months)
Team Churn Risk: HIGH (team consolidation, layoffs likely)
Integration Risk: HIGH
Customer Retention: Moderate (migration risk, churn possible)

Valuation Impact: +20-30% (synergy upside, but riskier)
Earnout Structure: Harder (blended metrics, harder to isolate [YourCo] contribution)
```

---

## DECISION TREE

```
1. Is your product a direct replacement of acquirer's product?
   ├─ YES → Consider MERGE (Score 4-5)
   └─ NO → Go to Q2

2. Do you serve the same customer segment as acquirer?
   ├─ YES (>70% overlap) → Consider MERGE
   ├─ SOME (30-70% overlap) → Consider HYBRID
   └─ NO (<30% overlap) → Consider KEEP SEPARATE

3. Do your teams have overlapping roles?
   ├─ YES (engineers, PM, design) → Consider MERGE
   ├─ SOME (1-2 overlaps) → Consider HYBRID
   └─ NO (specialized team) → Consider KEEP SEPARATE

4. What's the cost of integration?
   ├─ HIGH ($1M+, 12+ months) → KEEP SEPARATE or HYBRID
   ├─ MODERATE ($300k-1M, 6-12 months) → HYBRID
   └─ LOW (<$300k, <6 months) → MERGE

5. How valuable is [YourCo]'s brand / independence?
   ├─ CRITICAL → KEEP SEPARATE
   ├─ MODERATE → HYBRID
   └─ LOW → MERGE

FINAL RECOMMENDATION: [Weighted score above]
```

---

## POST-DECISION: INTEGRATION ROADMAP

### If KEEP SEPARATE:
```
Month 1: Establish independent P&L tracking
Month 1-3: Define API contracts (how products integrate)
Month 3-6: Launch cross-sell program (sell both products together)
Month 6-12: Monitor churn, retention, expansion
```

### If HYBRID:
```
Month 1: Consolidate finance, legal, HR
Month 1-2: Define shared infrastructure (databases, APIs)
Month 2-4: Migrate to shared infra (phased)
Month 4-6: Consolidate some teams (support, ops)
Month 6-12: Evaluate full merger feasibility
```

### If MERGE:
```
Month 1: Create merged org chart, define roles
Month 1-2: Begin code integration (branches, testing)
Month 2-3: Migrate customer base (beta, phased)
Month 3-4: Consolidate teams, manage churn
Month 4-6: Full product consolidation, sunset old platform
Month 6-12: Optimize, realize full synergies
```

---

**Created:** 2026-06-12  
**For:** Soren Mendy (integration planning)  
**Time to use:** 10 min (score yourself, see recommendation)  
**Note:** This decision should be made collaboratively with acquirer's leadership, not unilaterally.

