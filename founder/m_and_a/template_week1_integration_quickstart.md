---
name: week1_integration_quickstart
description: Days 1-14 post-close — critical meetings, customer retention, team onboarding
metadata:
  type: decision
  created: 2026-06-13
  effort: 10min
---

# Week 1-2 Integration Quick-Start — Post-Close Playbook

**Objectif :** 14 jours = critical window. Founder + buyer ops must execute in lockstep.

---

## The 72-Hour Fire Hose (Days 0-3)

### Day 0 (Close Day)

**BEFORE market opens:**
- [ ] Escrow agent confirms receipt of funds (verify wire)
- [ ] Buyer's legal notifies you: close docs signed, effective

**BY 5 PM:**
- [ ] Founder + CEO get together (1:1, 30 min) — set tone for integration
- [ ] Buyer announces deal internally (email + all-hands if large)
- [ ] Your team gets internal brief (talking points, no surprises)

**EVENING:**
- [ ] Send email to all customers:
```
Subject: [Exciting News] — We've joined [Buyer]

Hi [Customer Name],

Effective today, we've joined [Buyer]. This means:
✅ Same product, better features (Buyer's roadmap + our innovation)
✅ Stronger support (Buyer's ops team backing ours)
✅ New integration opportunities (Buyer's ecosystem)

Your contract terms remain unchanged. Your success owner is [name + email].

Questions? Reply to this email or contact [success owner].

Cheers,
[Founder Name]
```

---

### Day 1 (First Monday)

**MORNING (9 AM):**
- [ ] Buyer's integration lead + founder kickoff (1 hour)
  - Share: 3-month integration roadmap
  - Define: weekly syncs, escalation path
  - Assign: owner for each function (Sales, CS, Ops, Product)

**10-11 AM:**
- [ ] All-hands to merged team (30 min)
  - Buyer's CEO speaks (cultural message)
  - Your CEO speaks (transition message)
  - Vision for product roadmap (next 90 days)

**11 AM-12 PM:**
- [ ] Customer Success emergency triage
  - Top 10 customers: 1:1 calls (you + buyer's CS lead)
  - Message: "You're critical; we're here to support"
  - Gauge churn risk (any customers looking to leave?)

**AFTERNOON:**
- [ ] Buyer's finance onboarding (1 hour)
  - You + buyer's CFO: accounting reconciliation
  - Any balance sheet items requiring action?

**BY 5 PM:**
- [ ] Publish internal wiki/Slack: "Integration Playbook" (link, roles, calendar)

---

### Day 2-3 (Tues-Wed)

**DAILY SYNC (30 min):**
- [ ] Buyer integration lead + founder (same time daily; builds trust)
- [ ] Agenda: blockers, quick wins, team sentiment

**CUSTOMER CALLS:**
- [ ] Top 20 customers: 15-min calls (success owner + buyer's rep)
- [ ] Script: "You're critical to our mission; we've got fresh support coming"

**TEAM MEETINGS:**
- [ ] Your team + buyer's parallel team (Sales, CS, Product, Ops)
- [ ] Agenda: workflows, process integration, tool access

**INTERNAL COMMS:**
- [ ] Create Slack channel: #integration-status
- [ ] Daily standup (async post, or 15-min video)

---

## Week 1 Focus: Customer Retention (Days 1-7)

### Daily Contact Schedule

| Contact | Tier | Medium | Cadence |
|---------|------|--------|---------|
| Top 5 customers | Tier A | 1:1 calls | Days 1, 3, 7 (then weekly) |
| Customers 6-20 | Tier B | email + call | Day 1, then call Day 7 |
| Customers 21-50 | Tier C | email | Day 1, then weekly email |
| Customers 50+ | Tier D | In-app announcement | Day 1 only |

### Message Template

```
EMAIL (To Tier A Customers, Day 1):

Subject: [Founder] — Let's talk about your success

Hi [Customer],

Today we joined [Buyer]. This is great news for you.

Why? [2-3 specific benefits for THIS customer based on their use case]
- E.g., "You'll get access to [Buyer]'s [feature] you've been asking for"
- E.g., "You'll have 24/7 support instead of our 9-5"

Let's jump on a call this week. [Calendar link].

Cheers,
[Founder]
```

### Red Flags to Document

If customer signals churn risk:
```
CHURN RISK LOG:
┌─────────────────────────────┐
│ Customer: [Name]            │
│ ARR: $[X]k                  │
│ Risk Level: 🔴 HIGH         │
│ Signal: [what they said]    │
│ Action: [win-back plan]     │
│ Owner: [Name] (buyer's CS)  │
└─────────────────────────────┘
```

---

## Week 2 Focus: Team Onboarding (Days 8-14)

### Day 8-9 (Mon-Tue): Systems Onboarding

- [ ] **Email migration** (if consolidating)
  - Old email still works? Or migrating to buyer's domain?
  - New email aliases set up

- [ ] **Tool access**
  - Slack: Add to buyer's workspace
  - GitHub: Grant access to repo(s) (what can you access? Security review?)
  - Salesforce/HubSpot: Sync customer data (no duplication)
  - Financial systems: Budget access for next quarter

- [ ] **Security onboarding**
  - VPN access (if required)
  - MFA enforcement (Google Authenticator or Okta)
  - Background check (if not done pre-close)

---

### Day 10-11 (Wed-Thu): Product & Roadmap Alignment

- [ ] **Product vision sync** (1 hour)
  - Your roadmap (next 6 months)
  - Buyer's roadmap (next 6 months)
  - Areas of overlap/conflict
  - Decisions: merge? Keep separate? Integrate?

- [ ] **Engineering integration plan**
  - Code review: merge your repo into buyer's monorepo?
  - Build pipeline: use buyer's CI/CD
  - Dependencies: what breaks if we consolidate?

- [ ] **Customer-facing feature commitment**
  - What must ship before [next customer release]?
  - Who owns? (Your PM or buyer's PM?)

---

### Day 12-14 (Fri-Sun): Strategy & Metrics

- [ ] **90-day integration goals** (frozen in writing)
  - Revenue: maintain or grow [%]
  - Churn: stay ≤ [X]%
  - NPS: maintain ≥ [X]
  - Team: 80%+ retention
  - Integration: [specific milestones]

- [ ] **Weekly reporting cadence** (for earnout tracking)
  - ARR dashboard (every Monday)
  - Churn analysis (every Wednesday)
  - Customer sentiment (weekly pulse check)

- [ ] **Monthly founder 1:1** with buyer CEO/CFO
  - What's working?
  - What's not?
  - Next month priorities

---

## Critical Decisions: Week 1-2

### Decision 1: Branding

**Question:** Do customers see "[Your Product]" or "[Buyer Product]"?

**Options:**
- A) Keep separate (months 0-6, then integrate)
- B) Co-brand immediately (e.g., "[Buyer] + [Your]")
- C) Rename under buyer brand (risky for retention)

**Recommendation:** Option A (keep separate for 6 months) → avoids churn shock

---

### Decision 2: Pricing & Packaging

**Question:** Do customer contracts change?

**Options:**
- A) Honor existing contracts (no change until renewal)
- B) Migrate to buyer's pricing (new contract negotiation)
- C) "Special legacy pricing" for existing customers, new pricing for new ones

**Recommendation:** Option A → Builds trust; renegotiate at renewal

---

### Decision 3: Customer Success Ownership

**Question:** Who owns the customer relationship?

**Options:**
- A) Your CSM continues (buyer's ops as backup)
- B) Buyer's CSM takes over immediately
- C) Dual ownership (1 month overlap, then hand-off)

**Recommendation:** Option C → Smooth transition; avoids relationship shock

---

## Week 1-2 Metrics Tracker

```
INTEGRATION HEALTH DASHBOARD

┌────────────────────────────────────────┐
│ CUSTOMER METRICS (Week 1-2)            │
├────────────────────────────────────────┤
│ Tier A calls completed:      [X]/[Y]   │
│ Tier B calls completed:      [X]/[Y]   │
│ Churn risk identified:       [X]       │
│ Churn risk mitigated:        [X]       │
│ NPS (pulse check):           [X]       │
│ Target: All A/B calls done by Day 7    │
└────────────────────────────────────────┘

┌────────────────────────────────────────┐
│ TEAM METRICS (Week 2)                  │
├────────────────────────────────────────┤
│ Departures announced:        [X]       │
│ Key roles filled (buyer):    [Y]/[Z]   │
│ System access granted:       [X]%      │
│ Target: 0 unexpected departures, 80% tools live
└────────────────────────────────────────┘

┌────────────────────────────────────────┐
│ FINANCIAL METRICS                      │
├────────────────────────────────────────┤
│ ARR verified:                $[X]M     │
│ % retention (vs pre-close):  [X]%      │
│ Accruals/deferred revenue:   OK? ✅    │
│ Target: 100% ARR retention by Day 14   │
└────────────────────────────────────────┘
```

---

## Week 1-2 Blocker Escalation

**If something blocks progress:**

| Issue | Owner | Escalation | Deadline |
|-------|-------|-----------|----------|
| Customer threatens churn | CSM → Buyer VP CS | 24 hours | Resolve by Day 3 |
| Engineering integration stuck | Your CTO → Buyer CTO | 48 hours | Unblock by Day 5 |
| Pricing conflict (customer wants old price, buyer wants new) | Sales → CFO | 72 hours | Resolve by Day 7 |
| Key team member quitting | You → Buyer CEO | 4 hours | Negotiated exit if needed |

---

## Success Criteria: Days 1-14

✅ **All Tier A customers contacted** (at least once)
✅ **Zero unexpected churn** (no customers announce departure)
✅ **100% team present** (no key departures without reason)
✅ **Earnout metrics baseline** (ARR, churn verified)
✅ **Weekly integration syncs locked in** (next 13 weeks scheduled)
✅ **Customer sentiment stable or positive** (NPS flat or improving)

---

## Post-Week 2 Transition

- Move to bi-weekly integration syncs (not daily)
- Monthly founder + buyer CEO business reviews
- Continue weekly customer metrics tracking
- Start Month 2: Product roadmap integration begins in earnest

---

**Impact:** Poor Week 1-2 integration = 5-10% customer churn risk. Good execution = 99%+ retention.
