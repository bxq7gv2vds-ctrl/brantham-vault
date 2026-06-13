# Customer Concentration Risk Analysis

## Quick Scan (5 minutes)

| Metric | Formula | Benchmark | Your Score |
|---|---|---|---|
| **Top 1 customer** | (ARR of #1) / Total ARR | <15% = healthy | ___% |
| **Top 5 customers** | (Sum ARR #1-5) / Total ARR | <50% = healthy | ___% |
| **Top 10 customers** | (Sum ARR #1-10) / Total ARR | <70% = healthy | ___% |
| **Herfindahl Index** | Σ(market share %)² | <1500 = healthy | ___ |

**Red flags:**
- Top customer > 25% = buyer views as single-point-of-failure
- Top 5 > 60% = buyer concerned about integration risk
- Top 10 > 80% = very concentrated; may require earnout structure

---

## Full Analysis Template

### 1. Customer Concentration Table

| Rank | Customer Name | ARR | % of Total | Churn Risk | Renewal Date | Notes |
|---|---|---|---|---|---|---|
| 1 | Acme Corp | $500k | 20% | Low | 2026-Q3 | Strategic, multi-year contract |
| 2 | Beta Inc | $300k | 12% | Medium | 2026-Q2 | Uses 1 product, evaluating alternatives |
| 3 | Gamma LLC | $250k | 10% | Low | 2027-Q1 | Growing usage, high NPS |
| 4 | Delta Co | $200k | 8% | High | 2026-Q4 | Price-sensitive, buyer has legacy system |
| 5 | Epsilon Ltd | $150k | 6% | Low | 2026-Q4 | Sticky, API integration deep |
| ... | ... | ... | ... | ... | ... | ... |
| **Total** | **2,500 customers** | **$2.5M ARR** | **100%** | | | |

---

### 2. Churn Risk by Customer Tier

#### Critical Risk Tier (>$100k each, high loss impact)
- [ ] Acme Corp: $500k, churn risk = **HIGH** (why?)
  - Reason: Single buyer (CFO leaves = deal goes south)
  - Mitigation: Get multi-stakeholder NDA; embed support team
  - Action: Schedule executive alignment call before M&A goes public

#### Strategic Tier ($25k–$100k each)
- [ ] List top 10 here
  - Which are sticky (NPS 8+, multi-year, deep integration)?
  - Which are at-risk (price-sensitive, using alternative)?

#### Transactional Tier (<$25k each)
- [ ] Most won't churn post-acquisition
- [ ] Flag exceptions: Competitors (might switch), price-sensitive (might leave)

---

### 3. Retention Playbook (For buyer's integration)

**Buyer's concern:** "Will they stick around after acquisition?"

**Your prep (before LOI):**

| Customer Tier | Action | Timeline |
|---|---|---|
| Top 5 | Schedule post-announcement calls; announce new benefits (buyer backing) | Week 1 post-close |
| Top 10 | Handoff to buyer's account management | Week 2–4 |
| Top 20 | Bulk announcement (email + webinar) | Week 1 |
| Remainder | Auto-renewal, no action | -- |

**Tie to earnout (if buyer proposes it):**
- "If you're concerned about Top 5 churn, let's tie X% of earnout to retention rate ≥ 95%"
- Shows you're confident; aligns incentives

---

### 4. Customer Concentration Red Flags

**If top customer is:**
- **Your own founder's prior company** → Major red flag (not a real customer)
- **Owned by buyer or buyer's competitor** → Disclose upfront
- **Under contract review/renegotiation** → Mention in diligence
- **Paying below-market rates** → Flag for earnout risk (buyer will raise prices post-close)

**If multiple customers are concentrated in one industry:**
- Example: 60% of revenue from "Financial Services"
- Buyer concern: Industry downturn = correlated churn
- Mitigation: Show you're diversifying; prove product works across verticals

---

### 5. Sensitivity Analysis

**Scenario 1: Lose Top Customer (ARR $500k)**
- New total: $2.0M (20% loss)
- Earnout impact: If earnout tied to ARR growth, you lose that $500k upside
- **Mitigation:** Lock customer contract extensions before M&A announcement

**Scenario 2: Top 5 All Churn (ARR $1.4M combined)**
- New total: $1.1M (56% loss)
- **Likelihood:** Very low (would take catastrophic integration failure)
- **Mitigation:** Buyer shouldn't close if top 5 are at risk

**Scenario 3: Each customer churns at historical rate (e.g., 5% annually)**
- Projected 24-month churn: $250k
- Post-close ARR expectation: $2.25M (declining from $2.5M)
- **Mitigation:** If buyer forecasts $3M post-close, set realistic expectations

---

### 6. Questions to Prepare For (Buyer Will Ask)

| Question | Your Answer | Red Flag If... |
|---|---|---|
| "Why is Acme 20% of revenue?" | "Acme is strategic; we've been with them 4 years; they're growing." | You say "they're our only/best customer" |
| "Will Acme stay post-close?" | "Yes, we've confirmed with their CFO; they're excited about [benefit]." | You're uncertain or haven't asked them |
| "What if Acme leaves?" | "We'd lose $500k ARR, but NRR is positive, so other customers grow. Unlikely." | You panic or avoid the Q |
| "How diversified is your customer base?" | "We have $2.5M ARR across 500+ customers; top 5 = 50%." | You don't know your own concentration |
| "Has any customer complained about the acquisition?" | "No; we've confirmed with top 10 that they see synergies." | Any customer has expressed concern |

---

### 7. Defensive Measures (Before You Talk to Buyers)

**Pre-LOI actions:**
- [ ] Lock top 5 customers into multi-year contracts (if close to renewal)
- [ ] Get written customer references (testimonials) from top 5
- [ ] Schedule executive visibility calls (CEO + top customer CEO) on product strategy
- [ ] Document NPS / CSAT by customer (proves they're happy)
- [ ] Get top customer approvals for change-of-control language in master agreements

**In LOI / Diligence:**
- [ ] Offer customer reference calls to buyer (proactive, not defensive)
- [ ] Provide NRR by customer cohort (shows you're retaining)
- [ ] Show pipeline of new customers (buyer wants to see growth didn't stall)

---

### 8. Earnout Tie-In

**Buyer may propose:**
- "30% of earnout is tied to retaining top 5 customers (>90% retention)"

**Your negotiation:**
- "Agree, but I don't control retention post-close — you do. Tie it to NPS or usage growth instead."
- Or: "OK if you retain me as VP Customer Success for 24 months to manage handoff."

---

## Export to Buyer (Anonymized)

Create a customer concentration summary for buyer:

```
Customer Concentration:
- Top customer: 20% of ARR
- Top 5: 50% of ARR
- Top 10: 70% of ARR

Churn rate: 5% annual
NRR: 110% (expansion revenue offsets churn)

Concentration risk: MODERATE
- Diversified across 500+ customers
- No single customer >$1M ARR
- Sticky product (high switching costs)

Retention confidence: HIGH
- Top 5 customers contacted pre-LOI
- All confirmed interest in staying
- Strategic alignment evident
```

**Keeps you credible; flags risk openly.**
