---
name: earnout_failure_playbook
description: Pourquoi 80% des earnouts échouent — red flags et comment les négocier
metadata:
  type: playbook
  created: 2026-06-12
---

# Earnout Failure Playbook — Why 80% Fail

**Reality:** Founders miss earnouts ~80% of the time. Buyer changes strategy post-close and deprioritizes your product.

**Goal:** Negotiate earnouts you can actually win, or avoid them entirely.

---

## Why Earnouts Fail

### 1. **Buyer Kills Distribution**
**Scenario:** Buyer promised to cross-sell to existing customer base. Post-close, they deprioritize your product for their priorities.

**Red flag:** No specific go-to-market plan in LOI. Vague "synergies" language.

**Defense:**
- [ ] Require earnout metric **not dependent on buyer's actions** (e.g., exclude new logos added via buyer's channel)
- [ ] Tie earnout to **product adoption within buyer's org** (usage metrics, not just revenue)
- [ ] Demand weekly access to sales data proving effort

---

### 2. **Buyer Changes Product Strategy**
**Scenario:** You built a standalone product. Buyer acquired you to shut down competitor, then shelves your product.

**Red flag:** Buyer is larger competitor, or acquisition is "acqui-hire" disguised as strategic.

**Defense:**
- [ ] Earnout tied to **user engagement**, not revenue (can't be killed by product pivot)
- [ ] Require buyer commits to **maintaining current product roadmap** for 12 months
- [ ] Request **board seat or observer rights** (catch strategy changes early)

---

### 3. **Founder Not Hired / Forced Out**
**Scenario:** You stay only 8 months (supposed to be 24). Earnout requires you to be employed at close date.

**Red flag:** LOI says "founder employment at will" or vague on retention terms.

**Defense:**
- [ ] Earnout **vests independently** of employment (paid regardless of termination)
- [ ] OR require buyer to pay earnout **even if they fire you without cause**
- [ ] Negotiate **severance protection**: if fired without cause in first 12m, earn 50% of earnout
- [ ] Get written PM job description before signing; any "material change" = termination protection triggered

---

### 4. **Metric Gets Redefined**
**Scenario:** LOI says "ARR >$5M by Dec 31". Post-close, buyer changes how ARR is calculated (excludes annual contracts, counts differently, etc.)

**Red flag:** Earnout metric is undefined or subjective (e.g., "achieve growth targets as agreed with buyer").

**Defense:**
- [ ] Specify metric in **concrete, auditable terms**: "[GAAP] ARR per [customer] including [contract types X, Y, Z]"
- [ ] Require **independent audit** of earnout calculation by third party
- [ ] Include **escalation clause**: disputes resolved by [neutral accountant / arbitration]

---

### 5. **Customer Churn Post-Close**
**Scenario:** You hit $5M ARR at close. During earnout period, buyer loses key customers or they churn. Earnout requires $5M sustained.

**Red flag:** Earnout tied to absolute revenue, not net new / growth relative to baseline.

**Defense:**
- [ ] Metric: "ARR growth of +$X relative to [close date baseline]"
- [ ] NOT: "Absolute $Y ARR" (inherited risk gets shifted to you)
- [ ] For established customers: protect against churn by allowing replacement revenue

---

### 6. **Integration Disasters Hurt Performance**
**Scenario:** Buyer integrates product poorly, breaks APIs, loses customers due to bad migration.

**Red flag:** Earnout doesn't account for buyer's operational risk post-close.

**Defense:**
- [ ] Earnout metric excludes customers lost due to [buyer's migration / integration / API changes]
- [ ] Require buyer to **maintain current product SLA** (uptime, feature parity)
- [ ] Tie earnout to **product engagement**, not just customers (harder to manipulate)

---

### 7. **Buyer Recognizes Revenue Differently**
**Scenario:** LOI: "ARR." Post-close, buyer insists on ASC 606 (which defers revenue), making it hard to hit ARR target.

**Red flag:** "ARR" definition isn't precise; doesn't specify ASC 606 vs. cash basis.

**Defense:**
- [ ] Define metric in writing: "Revenue per [IRS / GAAP cash basis / ASC 606 without deferral]"
- [ ] Reference prior financial statements as baseline definition
- [ ] Get buyer's CFO to sign that definition **before close**

---

### 8. **Other Products Cannibalize Yours**
**Scenario:** Buyer integrates your product into their core platform, making it free to customers. Earnout requires revenue targets.

**Red flag:** Earnout tied to revenue; buyer has incentive to bundle/commoditize.

**Defense:**
- [ ] Metric: **"Product usage"** or **"customers deployed"** instead of revenue
- [ ] Require buyer to monetize your product (charge for it, don't bundler)
- [ ] Include carve-out: if bundled, earnout calculated on **equivalent ASP** of unbundled version

---

## Earnout Negotiation Strategy

### Option A: Avoid Earnout Entirely
**If possible**, push for all cash:
> "We prefer all cash at close. Earnout introduces misaligned incentives post-close. Rather than bet on execution risks we can't control, let's price the business fairly with cash today."

**Cost:** Buyer wants lower all-cash price (~20% discount to earnout scenario).

**Worth it?** If earnout >30% of total comp or >24 months, YES.

---

### Option B: Low-Risk Earnout
**Structure:**
- **Metric:** Product usage / engagement, not revenue
- **Target:** Conservative (achievable with 80% probability)
- **Duration:** 12 months (not 24+)
- **Percentage:** <20% of total comp
- **Vesting:** Independent of employment

**Example:**
> "Earnout of $1M (10% of base price) if [PRODUCT] has ≥500 active users and ≥80% NPS by Dec 31, 2027. Measured by [independent audit]. Earnout vests regardless of employment."

---

### Option C: Structured with Milestones
Break earnout into **early-achievable + stretch**:

```
Tranche 1: $500k for hitting 60% of target by Month 6 → Proof of concept
Tranche 2: $500k for 100% of target by Month 12 → Full achievement

(Avoids "all or nothing" cliff — reduces buyer's incentive to kill product)
```

---

### Option D: Buyer Bonus (Not Earnout)
**Reframe:** Instead of "earnout for seller," offer "bonus pool for team":
> "We'd like to set aside $2M for team bonuses if we achieve [goal]. Aligns everyone post-close."

**Advantage:** 
- Buyer sees it as employee retention, not seller payout
- Team stays motivated (not just you)
- Easier to negotiate (not adversarial)

---

## Earnout Negotiation Tactics

### During LOI / SPA Negotiation

**Your leverage:**
1. **Tie earnout to uncontrollable metrics** → Buyer wants it tied to their effort
2. **Demand independent audit** → Buyer wants self-calculated
3. **Short duration** (12m) → Buyer wants 24m+
4. **Early tranches** → Buyer wants back-loaded (keep incentive)

**Proposal flow:**
```
Round 1: "Earnout 25%, tied to ARR growth"
         ↓
Buyer: "That's too low for buyer risk. Make it tied to revenue, 36 months"
         ↓
Round 2: "We'll do 15%, tied to product adoption (not buyer's sales), 12 months. 
         Buyer covers all costs; earnout paid regardless of our employment."
         ↓
Buyer: "Deal, but we need 18-month duration and some revenue component"
         ↓
Round 3: "18 months max. 60% tied to engagement, 40% tied to revenue growth (net of churn). 
         No earnout claw-back if we're terminated without cause."
```

---

## Red Flags in Earnout Terms

| 🚩 Flag | ✅ Fix | Priority |
|--------|--------|----------|
| Earnout >30% of comp | Cap at 20% or demand all cash | CRITICAL |
| Duration >24 months | Negotiate down to 12-18m | CRITICAL |
| Metric is vague ("growth targets TBD") | Specify in dollars/units/engagement | CRITICAL |
| Earnout tied to your employment | Make it independent | HIGH |
| No audit rights; buyer calculates | Demand third-party audit | HIGH |
| Buyer can change metric post-close | Lock it in SPA; make immutable | HIGH |
| Revenue metric (all risk on buyer) | Tie to growth/engagement | MEDIUM |
| Back-loaded (all earnout at Month 24) | Front-load or add tranches | MEDIUM |

---

## Earnout Success Checklist

**Before signing, verify:**

- [ ] Metric is **specific, auditable, objective** (not subjective or subject to buyer interpretation)
- [ ] Earnout **vests independently** of employment
- [ ] Duration is **≤18 months** (ideally 12)
- [ ] Percentage is **<25% of total comp**
- [ ] Metric is **achievable with 70%+ probability** (not a lottery ticket)
- [ ] **Independent audit rights** included (you can audit buyer's calculation)
- [ ] **Escalation clause** for disputes (not left to buyer's judgment)
- [ ] Metric is **not dependent on buyer's actions** (distribution, go-to-market, etc.)
- [ ] Early tranches exist (don't wait 24m for payout)
- [ ] **Severance protection** if fired without cause during earnout period
- [ ] **Change of control** clause (if buyer is acquired, earnout is still paid)

---

## Examples of Good vs. Bad Earnout Metrics

### ❌ Bad (high failure risk)
- "ARR ≥ $10M by Dec 31, 2027" (absolute metric; inherited churn risk)
- "Achieve aggressive growth targets TBD" (undefined)
- "Product revenue targets as agreed with buyer" (subjective; buyer can redefine)
- "Seller must remain employed" (wrongly ties to employment)

### ✅ Good (high achievement probability)
- "Product monthly active users ≥1,000 by Dec 31, 2027" (engagement; buyer can't kill if deprioritizes)
- "ARR growth of +50% relative to close-date baseline, excluding customer churn" (net new; controls for inherited risk)
- "≥200 customers using [feature X] by June 30, 2027, per [audit firm] annual audit" (specific, audited, objective)
- "Earnout paid regardless of employment termination (unless for cause related to fraud)" (independent vesting)

---

## Post-Close: Tracking Earnout

**Monthly checklist (if you're tracking earnout):**

- [ ] Verify metric reported by buyer matches your calculation
- [ ] Request data pull / audit trail monthly (don't wait until end)
- [ ] Flag discrepancies within 30 days (hard to dispute later)
- [ ] Loop in M&A counsel if buyer refuses audit access
- [ ] Document all communications (metric definitions, data requests, results)
- [ ] **Don't assume it will pay out** — plan cash flow as if you'll get $0

---

## Real Example: Why $1M Earnout Became $0

**Deal:** SaaS company, $3M ARR at close. Earnout: $1M if ARR ≥$4M by Dec 31 (16 months out).

**What happened:**
1. Buyer promised to cross-sell to 500-person sales team
2. Post-close, buyer's sales org was busy with other products; only 2 sales reps pushed the product
3. Company grew only to $3.2M ARR (net new was +$0.5M, but inherited customers churned -$0.3M)
4. Earnout was "tied to absolute $4M ARR" → **Founder got $0**

**What should have been negotiated:**
```
Earnout: $1M if company achieves:
  - ARR growth of +$1M relative to close date, OR
  - 500+ monthly active users, OR
  - 100+ new logos acquired

Earnout vests 50% at Month 8 (early test), 50% at Month 16 (full).
If buyer doesn't provide sales resources, earnout tied to engagement metrics instead.
```

---

## Bottom Line

> **Earnouts almost never pay out. Negotiate as if you won't get it. Structure for success if you do.**

- Avoid if possible (demand cash; accept lower valuation)
- If required, cap at 12-18 months, <20% of comp
- Tie to metrics buyer can't kill (engagement, not revenue)
- Get independent audit rights
- Make it independent of your employment
- Front-load tranches (don't wait 24 months for payout)
## Related
## Related
## Related
