---
name: customer-churn-risk-calculator
description: Concentration analysis, churn risk scoring, retention playbook post-close
type: tool
---

# Customer Churn Risk Calculator

**Use** : Identify which customers are at risk of churning post-acquisition. Buyer will ask; pre-empt them.

**Impact** : Buyer will reduce offer by 2-5% if top 3 customers at risk. Knowing this = negotiating power.

---

## Part A: Concentration Scoring

| Rank | Customer | ARR | % of Total | Churn Risk (1-10) | Flag | Mitigation |
|------|----------|-----|-----------|------|------|-----------|
| 1 | [Name] | $[X] | [%] | [Score] | ⚠/✓ | [Plan] |
| 2 | [Name] | $[X] | [%] | [Score] | ⚠/✓ | [Plan] |
| 3 | [Name] | $[X] | [%] | [Score] | ⚠/✓ | [Plan] |
| **Top 3 Total** | — | $[X] | **[%]** | — | — | — |
| Top 10 Total | — | $[X] | [%] | — | — | — |

**Red flags** :
- Top 3 = >50% ARR → High concentration risk
- Top 1 = >25% ARR → Single customer risk (buyer will negotiate down)

**Example** :
| 1 | Acme Corp | $150K | 30% | 7 | ⚠ High | CEO replacement Q1 2027; need retention call |
| 2 | FastCo | $100K | 20% | 5 | ⚠ Medium | Using as pilot; scaling internally possible |
| 3 | LocalShop | $50K | 10% | 2 | ✓ Low | Happy customer 3+ years |
| **Top 3** | — | $300K | **60%** | — | ⚠ | — |

---

## Part B: Churn Risk Scoring

**For each customer, rate 1-10** :

| Factor | Low (1-3) | Medium (4-6) | High (7-10) |
|--------|-----------|-------------|------------|
| **Contract length** | 2+ years | 1 year | <1 year (month-to-month) |
| **Usage/engagement** | Daily active, multiple teams | Weekly, 1-2 team members | Inactive for 30+ days |
| **Relationship** | Executive sponsor + team | Department manager | Assigned to admin (no exec) |
| **Price sensitivity** | <5% of their budget | 5-10% of budget | >10% (shopping alternative) |
| **Competitive risk** | No direct competitor | 1-2 competitors exist | Buyer's competitor or acquirer's |
| **Internal dependency** | Mission-critical (integrated workflow) | Helpful but replaceable | Nice-to-have tool |
| **Renewal history** | Auto-renew, no questions | Renewed after discussion | Almost churned, convinced to stay |

**Scoring** : Sum all 6 factors (1-10 each) = total 6-60.
- **6-18** = Low risk (likely to stay)
- **19-36** = Medium risk (retention plan needed)
- **37-60** = High risk (risk of churn within 12 months post-acquisition)

---

## Part C: Retention Plan (Pre-Close)

**For each "High Risk" customer, present to buyer:**

```
Customer: Acme Corp (7/10 risk)
├─ Risk: CEO left Sept 2025; new CTO may audit tooling
├─ Countermeasure 1: Intro new CTO to [your] team (scheduled Day 5 post-close)
├─ Countermeasure 2: Offer 6-month price lock (vs increase)
├─ Countermeasure 3: Custom integration roadmap (showing value)
└─ Owner: [Your name] for 90 days, then transition to [buyer's person]
```

---

## Part D: Deal Impact Calculator

**Formula** : Expected churn impact on earnout

```
High-risk ARR × (Risk Score / 60) × (Churn probability) = Expected churn impact

Example:
$300K (top 3) × (7.5 avg / 60) × (50% churn prob in Y1) = $18.75K expected impact

If earnout is $500K and tied to retention:
Lost $18.75K = ~3.75% reduction in earnout potential
Buyer's offer: $1.5M cash - (3.75% × $500K earnout risk) = Negotiate for $481K earnout instead of $500K
```

**What to say to buyer** :
> "Our top 3 customers represent 60% of ARR. We've conducted risk assessment: 2 are very sticky (8+ year contracts), 1 is medium-risk (CEO transition coming). We have retention playbook: offer 6-month price lock, dedicated success manager, and custom roadmap. Risk mitigation = minimal churn post-close."

---

## Part E: Red Flags to Disclose Proactively

**Buyer will ask anyway. Better you say it first:**

- "Customer X is using our product as a pilot; they're building internal replacement"
  → **Action** : Timeline for build-out? Can you lock them into 2-year contract now?

- "Customer Y asked about alternatives in last renewal"
  → **Action** : Why? Price? Feature gap? Competitive product? Fix before sale or mention in SPA.

- "We just lost [name], a $[X] customer"
  → **Action** : Reason (bad fit, product gap, churn)? Was it avoidable?

**Disclosure strategy** :
- Week 1: Tell advisor & lawyer
- Week 2: Rehearse explanation
- Week 3: Proactively mention in buyer discovery ("We're transparent about...")
- Week 4: Document in data room under "Customer Risk Mitigation"

---

## Real Example

**SaaS: $500K ARR, 25 customers**

| Customer | ARR | Risk | Mitigation |
|----------|-----|------|-----------|
| Acme Corp | $150K | 7/10 | CEO transition; locked in 18-month extension last month |
| FastCo | $100K | 5/10 | Pilot; using for internal tool eval; offer custom integration |
| LocalShop | $50K | 2/10 | Very sticky; multi-team usage |
| **Top 3** | **$300K** | — | **Buyer confident 90%+ retention** |
| Long tail | $200K | 2-4/10 | Stable; low churn historically |

**Buyer messaging** :
> "60% of revenue is well-secured: Acme just extended 18 months, LocalShop has 5-year contract. FastCo is piloting, but we de-risk by offering 24-month term + exclusive integration. Historical churn: 3% annual. Post-acquisition, NRR = 95%+ is achievable with retention playbook."

---

## Template for Data Room

Create a one-pager for buyer data room:

```
CUSTOMER RETENTION RISK ASSESSMENT
Updated: [Date]

Summary:
├─ Total customers: [#]
├─ Concentration (top 3): [%]
├─ Avg contract length: [months]
├─ Historical churn rate: [%]/year
└─ Projected post-acquisition churn: [%]/year (with mitigation)

High-risk customers: [#] of [total] ([%])
├─ Customer A: [Mitigation plan]
├─ Customer B: [Mitigation plan]
└─ Customer C: [Mitigation plan]

Retention playbook (90 days post-close):
├─ Day 5: Executive intros
├─ Day 15: Custom roadmap presentations
├─ Day 30: Contract extensions for [X] customers
└─ Day 90: Full success transition complete
```

---

## Next Step
Run this analysis now (before soft shop). Use it to:
1. Negotiate higher price ("low churn risk")
2. Build confidence with buyer
3. Plan retention (your responsibility post-close)
