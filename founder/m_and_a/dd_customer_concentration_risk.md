---
name: dd-customer-concentration-risk
description: Deep-dive checklist — customer concentration, churn risk, contract volatility
metadata:
  type: checklist
  created: 2026-06-12
---

# Due Diligence: Customer Concentration & Retention Risk

**Use this in data room OR buyer's onsite diligence week. Focus = will customers leave post-close?**

---

## Part 1: Concentration (Red Lights)

### Revenue Concentration
```
Calculate (use trailing 12 months):

Top 3 customers = [   ] % of ARR       ← >30% = RISK
Top 10 customers = [   ] % of ARR      ← >50% = MAJOR RISK
Top 1 customer = [   ] % of ARR         ← >20% = DEAL-BREAKER

If >30%, mark "CONCENTRATION RISK" and do customer meetings
```

### Geographic Concentration
```
North America = [   ] %        ← If >70% and acquired by EU buyer = risk
Europe = [   ] %
Asia-Pacific = [   ] %
Other = [   ] %

Red flag: >80% single region + acquirer has no local presence there
```

### Vertical/Industry Concentration
```
Tech = [   ] % of ARR
Financial Services = [   ] %
Healthcare = [   ] %
Retail = [   ] %
Other = [   ] %

Red flag: >60% in single industry if that industry in recession cycle
```

### Customer Tenure (Longevity)
```
Customers <1 year = [   ] %     ← >30% = sticky questions needed
Customers 1-3 years = [   ] %
Customers 3+ years = [   ] %    ← Ideal = >60%

Calculate: Avg customer lifetime = (total ARR / annual churn ARR)
Result = ___ years
```

---

## Part 2: Churn Deep-Dive (Critical Path)

### Trailing 12-Month Churn
```
Month  | Starting ARR | Churned | %/mo
-------|--------------|---------|-----
Jan    | $[X]M       | $[Y]K   | [Z]%
Feb    | ...         | ...     | ...
Dec    | ...         | ...     | ...
       | **AVERAGE** |         | [__]%/mo

Annual = (1 - (1 - avg_monthly)^12) × 100 = [__]%
```

### Churn Drivers (Why did they leave?)
```
For each churned customer (last 12m):
Name      | ARR Lost | Reason           | Avoidable?
----------|----------|------------------|----------
Acme Inc  | $150K    | Competitive loss | Maybe
Beta Co   | $80K     | Economic slowdown| No
...

Avoidable = product issues, service failure, price shock
Non-avoidable = customer ran out of money, went out of business
```

**Red flag churn categories:**
- ❌ "Replaced us with [competitor]" (product issue)
- ❌ "Too expensive, looked for cheaper option" (pricing too high)
- ❌ "Couldn't get support" (service issue)
- ✅ "Company acquired" (good riddance)
- ✅ "Out of business" (macro, not our fault)

### NRR (Net Revenue Retention) — Real Health Metric
```
ARR Year 0 (Jan opening) = $[X]M
ARR Year 1 (Jan opening) = $[Y]M
Expansion (upsell + cross-sell) = $[Z]M
Churn (downgrades + cancels) = -$[W]M

NRR = (Y / X) × 100 = [__]%

80-90% = slow decline (problem)
90-100% = flat (acceptable for mature SaaS)
100-120% = expansion (good)
120%+ = exceptional
```

---

## Part 3: Contract Risk (Buyer Diligence Must-Do)

### Top 20 Customers — Deep File Review

For each: Create a 1-page file with:

**[Customer Name]**
- [ ] Annual contract value (ACV): $[X]
- [ ] Auto-renewal or manual? (Auto = safer)
- [ ] Termination clause: Notice period = [X] days
- [ ] Price increases locked in? (How much? When?)
- [ ] SLA commitments (99.9% uptime = risky)
- [ ] Any discounts promised? (Multi-year deal = locked price)
- [ ] Key contacts (who can cancel? who loves us?)
- [ ] Relationship health (NPS score, support tickets, usage)
- [ ] "Most likely to churn"? (Y/N, why?)

### Red Flag Contract Terms
```
❌ Auto-renewal with cancellation right (they can exit anytime)
❌ Termination for convenience (buyer can cancel for any reason)
❌ Annual price increase cap (e.g., "no more than 10%")
❌ Sole supplier agreement (you're their only vendor = risky)
❌ Performance guarantees (SLA failures = credits/refunds)
❌ Price reduction if buyer acquires (weird but happens)

✅ Multi-year commitment (locked 3+ years)
✅ 90-day termination notice (not month-to-month)
✅ Annual escalation clauses (you can raise prices)
```

---

## Part 4: Customer Meetings (Buyer's DD Week)

### Customer List for Meetings
```
Tier 1 (Do NOT ask customer to call):
  - Top 5 by ARR (buyer will want to visit / call)
  
Tier 2 (Buyer will want to reference-check):
  - Random sample of 5 mid-market customers
  - 2-3 customers who churned recently
  
Tier 3 (Optional):
  - Customers in buyer's target vertical
  - Fastest-growing customers
```

### Pre-Call Prep for Top 5
- [ ] Schedule 30 min on phone with buyer present
- [ ] Prep customer: "Buyer will call to understand your use case"
- [ ] Send customer buyer's background (lower surprise)
- [ ] Brief buyer on each: key contact, use case, health, renewal date
- [ ] Ask buyer: "Any specific concerns to probe?" (e.g., SLA, migration risk)

### Buyer's Reference Call Script (You coach them)
```
"Hi [customer], thanks for taking time. We're excited about the acquisition.
Have a couple questions:

1. How critical is [product] to your business? (Understand stickiness)
2. Any concerns about the acquisition? (Uncover hidden risks)
3. Are you planning any changes to your stack? (Churn signal)
4. Would you be interested in [buyer's product]? (Synergy signal)

That's it. Let them talk."
```

### After Calls — Buyer's Summary (Ask for this)
```
Customer   | Stickiness | Risk Level | Synergy | Notes
-----------|------------|------------|---------|-------
Acme Inc   | High       | Low        | Medium  | Wants AI features
Beta Co    | Medium     | High       | Low     | Budget cuts coming
...
```

**Action**: If any "High risk," get founder on personal call to reassure.

---

## Part 5: Churn Sensitivity Analysis (Buyer Financial Model)

**Buyer will stress-test: "What if top customers churn?"**

Prepare responses:

```
Scenario 1: "What if top 5 customers leave in year 1?"
  Current ARR: $10M
  Top 5 = 40% = $4M
  Remaining = $6M
  → Buyer's underwriting should assume $6M floor

Scenario 2: "What if churn accelerates to [X]% post-close?"
  Current churn: 5%/mo
  If doubles to 10%: Annual loss = ~43% of base
  → This kills deal (show why it won't happen)

Scenario 3: "What if top buyer + integrations go wrong?"
  Top customer = Acme Inc, $1.5M
  They have API integration (switching cost = high)
  Migration effort = 3 months on their side
  → Stickiness = very high
```

---

## Part 6: Customer Success Health Scorecard (Buyer Reviews)

Build this in data room (weekly updated, last 4 weeks):

| Customer | NPS | Health | Renewal Date | Expansion Opportunity |
|----------|-----|--------|--------------|----------------------|
| Acme Inc | 45 | 🟢 Green | Jun 2026 | Up-sell add-on |
| Beta Co  | 12 | 🟡 Yellow | Sep 2026 | At risk? |
| Corp XYZ | 75 | 🟢 Green | Dec 2026 | Upsell | 

**Green** = Stickiness 90%+ | **Yellow** = 60-90% | **Red** = <60%

---

## Part 7: Conversation Prep (Buyer's Questions)

### "Why is [big customer] unhappy?"
**Answer format:**
```
"[Customer name] was upset about [specific issue] in [month].
We fixed it by [action taken]. They're back to [current NPS].
Related to broader [product issue]? Learning for buyer: [lesson]."
```
**Don't:** Minimize or deny. Buyer's due diligence will find it.

### "What happens if [big customer] leaves?"
**Answer format:**
```
"[Customer] is critical (4% of ARR). Risk factors:
  - Contract expires [month] (no auto-renewal)
  - Recently complained about [feature]
  - Competitive pressure from [competitor]

Mitigation:
  - Personal CEO relationship (strong)
  - Renewal conversation planned for [month]
  - Feature roadmap addresses [complaint] by [month]
```

### "Has customer concentration always been this high?"
**Answer format:**
```
"Yes, it's ~30% (top 3). But:
  - It's been stable (not climbing)
  - Average customer lifetime = 4 years (sticky)
  - We're diversifying (added [Y] new customers this year)
  - Next 12 months: target = reduce to 25% as we scale"
```

---

## Buyer's Go/No-Go Criteria (Risk Thresholds)

**Most buyers will walk if:**
- [ ] Top customer = >25% of ARR + no multi-year commitment
- [ ] Churn >15%/mo on average
- [ ] NRR <80% (declining fast)
- [ ] Top 3 customers want price reductions post-close
- [ ] Reference checks reveal "we're considering leaving"

**Acceptable risk:**
- [ ] Top customer = 10-20% of ARR + multi-year deal
- [ ] Churn = 4-8%/mo (normal SaaS)
- [ ] NRR = 95%+ (stable/growing)
- [ ] Tier 2 customers showing expansion (upsell working)

---

## Quick Checklist: DD Prep in 2 Hours

- [ ] Revenue concentration: Top 3 = __% (pass if <30%)
- [ ] Churn: Monthly = __%/mo, Annual = __% (pass if <8%/mo)
- [ ] NRR: ___% (pass if >90%)
- [ ] Contract file: Top 20 customers documented (in data room)
- [ ] Customer meeting list: Tier 1, Tier 2 identified + buyer prepped
- [ ] Churned customer analysis: Avoidable vs non-avoidable (by $)
- [ ] Red-flag contract terms: None found (or disclosed)
- [ ] Buyer's stress-test assumptions: Shared + discussed

**Use case**: Buyer's diligence team arrives day 1 → hand them this checklist + data room folder.
## Related
## Related
## Related
