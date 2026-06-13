---
name: script-due-diligence-call-60min
description: Script pour due diligence call (60 min) avec acheteur + advisors
metadata:
  type: reference
  created: 2026-06-13
---

# Due Diligence Call Script (60 Minutes)
**Participants**: Buyer (CEO/CFO), Legal counsel, Accountant, Technical advisor  
**Seller side**: Founder (CEO), CFO, CTO (technical Q&A)

---

## PRE-CALL (15 MIN BEFORE)

**Checklist:**
- ✓ All participants on Zoom 5 min early (test audio/video)
- ✓ Slides queued up (or just use data room walk-through)
- ✓ Q&A document open on screen (for reference)
- ✓ Financial spreadsheet ready (for detailed Qs)
- ✓ Customer reference list visible (in case they ask for calls)

**Tone**: Professional, prepared, but relaxed. You've done this before.

---

## OPENING (3 MIN)

**Founder**:

"Thanks everyone for taking the time today. I know this is a busy process, so I'll be respectful of time.

Here's our plan for the next hour:

**0–15 min**: Quick overview of [Company] — what we've built, why it works  
**15–40 min**: Deep dive on [financials / product / customers] — your advisors take the lead here  
**40–55 min**: Strategic questions — synergies, integration, team  
**55–60 min**: Open Q&A, next steps

Sound good?"

[Buyer confirms]

**Founder continues:**

"One ground rule: we're going to be completely transparent with you. If we don't know an answer, we'll say so and follow up within [24 hours]. Does that work?"

---

## SECTION 1: COMPANY OVERVIEW (8 MIN)

**Founder** (5 min max):

"So, [Company] solves [specific pain point] for [customer segment].

Here's the thesis:
- **Problem**: [Customer segment] currently spends [X hours/year] or [X $] trying to [pain point]. There's no good solution.
- **Our solution**: [Product name] does [what it does] in [time / cost]. [Key differentiator].
- **Traction**: We've grown to [ARR] with [# customers], growing [X]% MoM.

Why now?
- [Tailwind 1: regulatory / technology / customer behavior]
- [Tailwind 2]
- [Competitive threat]

Why we're exploring this:
- We could build this alone, but [acquire faster / reach more customers / combine with your platform].

[Show 1 screenshot of product] — this is what it looks like.

Questions so far?"

[Answer any clarifications — keep it light]

---

## SECTION 2: FINANCIAL DEEP DIVE (20 MIN)

**Buyer's CFO / Accountant takes lead. Seller's CFO responds.**

**Questions You'll Get:**

### Revenue & Growth

**Q**: "Walk us through your revenue model."

**CFO response**:  
"We have [X customers] generating $[ARR]M in annual recurring revenue.

Breakdown:
- [Segment A]: [# customers] at avg $[X]/month = [revenue %]
- [Segment B]: [# customers] at avg $[Y]/month = [revenue %]
- [Services revenue]: [revenue %]

Growth trajectory:
- [12 months ago]: $[X]M ARR
- [Today]: $[Y]M ARR
- That's [Z]% YoY growth, or [W]% MoM (last 3 months)

We're on track to hit $[projection] by EOY."

---

### Customer Economics

**Q**: "What's your CAC and payback period?"

**CFO**:  
"CAC is about $[X]. Payback in [Y] months.

Here's the bridge:
- Average customer value: $[LTV] over [typical customer lifetime]
- LTV:CAC is [X]:1, which is healthy for our category.

By segment:
- [Segment A]: $[X] CAC, [Y]-month payback (best)
- [Segment B]: $[X] CAC, [Y]-month payback

We're actually improving this every quarter as we optimize sales."

---

### Profitability & Burn

**Q**: "When will you be profitable?"

**CFO**:  
"We're actually already [unit-profitable / approaching cash-flow break-even].

Our gross margin is [X]%, which supports this.

Operating expenses:
- Payroll: $[X]K/month
- Infrastructure: $[X]K/month
- S&M: $[X]K/month
- Admin: $[X]K/month

At our current burn, we have [X] months of runway, but we don't need it — we're [generating positive cash flow / very close].

Key assumption: we keep growing at [Y]% MoM."

---

### Churn & Retention

**Q**: "What's your churn rate? Any concentration risk?"

**CFO**:  
"Monthly gross churn: [X]%. But our net retention is [Y]%, meaning customers are expanding their usage.

Top customer: [X]% of revenue. Top 5: [X]% of revenue. Really healthy diversification.

Churn drivers:
- [Reason 1]: [X]% (going out of business / budget cuts)
- [Reason 2]: [X]% (found cheaper alternative)

We're actively working to reduce churn through [customer success initiatives / product roadmap]."

---

**Buyer's team takes detailed notes. Let them ask follow-ups — don't fill silences.**

---

## SECTION 3: PRODUCT & TECHNOLOGY (12 MIN)

**Buyer's Technical Advisor takes lead. Seller's CTO responds.**

**Founder** (brief intro):  
"[CTO] will walk you through the tech stack and architecture. Take it away."

**CTO** (5 min):

"Our product is built on [tech stack]. Here's the architecture:

**Frontend**: [React / Vue] — 50K lines of code, well-tested, modular components.  
**Backend**: [Node.js / Python] — [X] microservices, containerized, runs on Kubernetes.  
**Database**: [PostgreSQL / MongoDB] — replicates across [X] regions, sub-millisecond latency.  
**Infrastructure**: Fully on [AWS / GCP] — no custom hardware.

**Scalability**: Current prod handles [X] concurrent users. For 10x growth, we'd need to scale [these specific components]. Estimated effort: [2–4 weeks engineer time], no product downtime.

**Code quality**: We have [X]% test coverage, automated CI/CD, code review on all PRs. [# security audits] to date; no major issues.

**IP**: All code is original; we don't have GPL or copyleft dependencies. We use [#] open-source libraries (MIT/Apache licenses), all properly attributed.

Any questions on tech debt, scalability, or security?"

---

**Technical Advisor likely asks:**

**Q**: "What about technical debt? What would we inherit?"

**CTO**:  
"We're pretty clean, honestly. Known items:
- [Legacy payment module] — low priority, can be refactored in [2 weeks]
- [Monolithic API] — starting migration to microservices next quarter (not blocking)

Nothing alarming. [Link to technical roadmap]."

---

**Q**: "How many engineers does this take to maintain?"

**CTO**:  
"[X] FTE for [Y] services. We're fairly lean — lots of automation. Onboarding new engineers takes [3–4 weeks]."

---

## SECTION 4: CUSTOMERS & PARTNERSHIPS (10 MIN)

**Founder** resumes:

"Let's talk about customers. [CFO] can provide references if you'd like. We're happy to facilitate 2–3 customer calls as part of diligence.

Our top customers are:
- [Cust A]: [description], using [feature], expanding [direction]
- [Cust B]: [description], very happy, [expansion potential]
- [Cust C]: [description], has some [minor issue, being addressed]

No customer has contractually left; all are renewing.

Partnerships:
- [Partner 1]: [Strategic value]
- [Partner 2]: [Revenue driver]

None of these are exclusive; we can optimize post-close."

---

**Buyer's team may ask:**

**Q**: "Can we speak to [Customer A]?"

**Founder**:  
"Absolutely. We'll set that up this week. [Customer] is enthusiastic — they'll give you the real story."

---

## SECTION 5: LEGAL & COMPLIANCE (5 MIN)

**Founder** or **CFO**:

"Quick legal overview:

- **IP ownership**: All ours. Trademarks registered in [jurisdictions]. [# patents] issued, [# pending].
- **Compliance**: [GDPR / SOC 2 / HIPAA-ready]. No major regulatory exposure.
- **Contracts**: All customer agreements are in data room. [Folder path]. Standard terms; no unusual obligations.
- **Litigation**: None. No employee disputes, IP disputes, or customer lawsuits.
- **Insurance**: [D&O, liability, etc.] — current policies on file.

Any questions?"

---

## SECTION 6: TEAM & RETENTION (5 MIN)

**Founder**:

"Here's our team structure:

- **Me [Founder]**: [Background], staying post-close for [X years]
- **[CTO]**: [Background], staying post-close, leading integration
- **[VP Sales]**: [Background], open to [staying / transition]
- **[Key Hires]**: [Brief bios]

Key retention:
- All core team on [employment agreements / retention bonuses post-close]
- Single-trigger acceleration: [50]% of equity vests upon close (retains remaining)
- No unusual severance or golden parachutes

We're betting on this working long-term, and our comp structure reflects that."

---

**Buyer likely asks:**

**Q**: "Will [CTO] stay?"

**Founder**:  
"Yes. We've already had that conversation. [CTO] is excited about the [platform expansion / customer base / team size]. We'll have a retention agreement in place before LOI."

---

## SECTION 7: DEAL STRUCTURE & NEXT STEPS (3 MIN)

**Founder** (last 3 min):

"Here's where we're at:

**What we've covered today:**
- ✓ Company overview
- ✓ Financials & unit economics
- ✓ Product & tech
- ✓ Customers & traction
- ✓ Team & retention

**What's next:**
1. You review all this with your advisors (this week)
2. We meet again [DATE] to discuss serious terms (price, earnout structure)
3. If there's mutual interest, we move to LOI (target: [DATE])
4. Diligence runs in parallel with legal negotiations

**Data room access:**
- Opens tomorrow [DATE] — [link or credentials]
- All docs are organized: financials, contracts, IP, team, compliance
- You can ask Qs anytime; we'll respond within [24 hours]

**Timeline:**
- LOI signed: [TARGET DATE]
- Close: [45–60] days later

Does this make sense?"

---

## Q&A / OPEN FLOOR (2 MIN)

**Founder**:  
"Before we wrap, anything else we should clarify?"

[Answer any remaining Qs]

**Founder closes:**  
"Great. This was really helpful. We're excited about the possibility of working together. [Buyer], when can we schedule the next call?"

[Set date / time]

**Founder**:  
"Perfect. I'll send a recap email within the hour with action items and data room access. Thanks again for your time."

---

## POST-CALL (WITHIN 1 HOUR)

**Send recap email** to buyer + advisors:

```
Subject: [Company] due diligence call — recap + next steps

Hi [Buyer Name],

Thanks for the focused discussion today. Here's what we covered:

**Key Metrics:**
- ARR: $[X]M ([Z]% YoY growth)
- Customers: [#] (top customer [X]% of revenue)
- CAC payback: [X] months; LTV:CAC [Y]:1
- Gross margin: [Z]%

**Product:** [X]-person eng team, [Y] microservices, scales to [Z] concurrent users

**Team:** [X] FTE, [Y]% vested; [CTO] committed through [DATE]

**Next Steps:**
1. You review financials + code repo (data room access: [link])
2. Customer reference calls: I'll set up [2–3] for [next week]
3. Our legal team will prepare LOI draft (expect by [DATE])
4. We meet again [DATE] to discuss deal terms

**Action items:**
- [Your name]: Deliver commitment letter (if financing involved)
- [My name]: Customer references + code access + preliminary SPA draft

Data room password: [SECURE DELIVERY METHOD]

Looking forward to moving this forward.

Best,
[Founder]
```

---

## OBJECTION HANDLING (Quick Ref)

| Objection | Response |
|-----------|----------|
| **"Churn is higher than we expected"** | "True, but it's [normal for segment] and improving each quarter. Plus, our net retention is positive." |
| **"Your tech is messy"** | "Fair feedback. We prioritize shipping over perfection, but here's the refactoring plan: [timeline]." |
| **"Competitor just raised $[X]M"** | "Competition validates the market. We're differentiated by [key advantage]. Plus, this deal gets you to market faster." |
| **"We need more diligence"** | "Absolutely. Here's what we'll provide: [list]. What's the timeline?" |
| **"Price seems high"** | "We're open to discuss. What would change your view on valuation?" |
## Related
