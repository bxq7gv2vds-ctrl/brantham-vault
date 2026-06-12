---
name: m_and_a_mistakes_to_avoid
type: playbook
version: 1.0
date: 2026-06-12
---

# M&A Erreurs Courantes — Comment Les Éviter

**Usage:** Checklist des 25 erreurs les plus coûteuses en M&A. Chacune a coûté $1M+ à vendeurs similaires.

---

## 🔴 ERREUR #1 — Ne Pas Préparer La Data Room à l'Avance

**Coût típico:** Delay 4-6 semaines | Lost deal 30% cas

### Problème
- Data room créée 10j avant LOI (juste avant access)
- Documents désorganisés (no folders, 500 files in root)
- Financials in 10 different formats (Excel, PDF, scans)
- Acquirer wastes 2 weeks finding what they need

### Solution
✅ Préparer data room **60 jours avant** outreach

**Checklist 60 Days Pre-Outreach:**
- [ ] 3 years audited financials (P&L, BS, CF) in clean Excel
- [ ] All monthly financials last 24 months
- [ ] Cap table (updated, show vesting schedules)
- [ ] Customer contracts (top 20 by revenue, templated deals)
- [ ] Employee agreements (all signed offers, equity grants)
- [ ] IP assignments (all founders signed document assigning IP)
- [ ] Tax compliance (3 years tax returns, no audit open)
- [ ] Legal (any litigation? claims? D&O insurance docs)

**VDR Folder Structure:**
```
/01_FINANCIAL
  /Audited_FY2023 (4-5 files)
  /Monthly_P&L_2024
  /Monthly_P&L_2025
  /Cap_Table
  /Bank_Statements

/02_CUSTOMER
  /Top_20_Contracts (signed, current)
  /Customer_List (names, ARR, renewal dates)
  /NPS_Surveys

/03_TECHNOLOGY
  /Architecture_Diagram.pdf
  /Code_Repo_Access (GitHub link)
  /Infrastructure_Costs.xlsx
  /Security_Audit_2024.pdf

/04_LEGAL & COMPLIANCE
  /Corporate_Documents (bylaws, board minutes)
  /IP_Assignments (founder agreements)
  /Employment_Agreements
  /Tax_Returns (last 3y)
  /D&O_Insurance

/05_TEAM
  /Employee_List (names, title, salary, vesting)
  /Org_Chart.pdf
  /Key_Bios (CEO, CTO, Sales Lead)

/06_OPERATIONS
  /Lease_Agreement
  /Vendor_Contracts (>€100K)
  /Insurance_Policies
```

---

## 🔴 ERREUR #2 — Founder Left Out of Deal Negotiation

**Coût típico:** $2-5M lost | Lower valuation | Team exodus post-close

### Problème
- Founder delegated deal to CFO/lawyer ("I'll focus on product")
- Buyer gets better terms (loose earnout, bad retention terms)
- Founder surprised post-close (didn't know he was staying as "VP Integration")
- Result: Founder leaves in M3, earnout at risk

### Solution
✅ Founder = lead negotiator (with CFO/lawyer support)

**Founder's Role in M&A:**
- [ ] Week 0: Founder leads first call with buyer (chemistry + vision alignment)
- [ ] Week 1-2: Founder + CFO present financial model together
- [ ] Week 3-4: Founder negotiates earnout KPIs (revenue, NRR, retention)
- [ ] Week 4-5: Founder + CTO decide: "Keep Separate vs Merge" post-close
- [ ] Week 6-8: Founder negotiates role/title/autonomy post-close
- [ ] Week 8-12: Founder reviews SPA final version (especially earnout terms)
- [ ] Day 0: Founder on call at closing (not delegate)

**Critical Decisions Only Founder Can Make:**
- "Do I want to stay? For how long? Doing what?"
- "Is this buyer aligned with our product vision?"
- "Am I comfortable with the culture fit?"

---

## 🔴 ERREUR #3 — Vague Earnout KPIs (Litigation Risk)

**Coût típico:** $500K-$2M escrow battle | 2-year arbitration | Team distracted

### Problème
```
SPA says:
  "Year 1 Earnout: If revenue targets are 'met' = $5M"
  
Problem: What is "revenue targets"? 
  - Acquirer defines it as: New logos only (€0.5M realized)
  - Seller thought it meant: All revenue continuation (€6M, above plan)
  
Result: $5M earnout fight over definition. Escrow litigation.
```

### Solution
✅ Write earnout formula to 2 decimal places, in SPA

**Good Earnout Language:**
```
5.1 EARNOUT — YEAR 1 (Months 0-12 Post-Close)

Earnout = €5,000,000 if and only if:

Condition A: "Revenue" (as defined below) ≥ €6,000,000
Condition B: "Net Revenue Retention" ≥ 105%

Definitions:
  "Revenue" = Invoiced annual contract value from customers 
              with active contracts as of Month 12.
              Excludes: refunds, chargebacks, discounts >30%.
              Methodology: GAAP, consistent with historical reporting.
              Calculation: [Attachment D, Excel model] updated monthly.

  "NRR" = (Beginning ARR - Churn + Expansion) / Beginning ARR
          Beginning ARR = €5.5M (as of Month 0)
          Calculated per [Attachment E] metrics definition

Measurement & Payment:
  - Measured on last day of Month 12
  - Calculated within 30 days post-measurement
  - Paid within 45 days, or dispute to arbitration
  
Dispute Resolution:
  - If parties disagree on calculation, use 
    [INDEPENDENT AUDITOR] within 20 days
  - Auditor's calculation = binding and final
  - Cost split 50/50 between Seller and Buyer

Conditions:
  - Seller must remain employed through Month 12 
    (pro-rata if termination without cause before M12)
  - Business must not be materially transferred 
    (earnout voids if Buyer sells division to third party)
```

**Avoid These Vague Terms:**
❌ "Meet revenue targets"
❌ "Growth in line with plan"
❌ "Successful integration"
❌ "Mutual satisfaction"

---

## 🔴 ERREUR #4 — No Key Person Retention Plan

**Coût típico:** CTO leaves in M2 | Revenue declines | Earnout at risk

### Problème
- Deal closes
- CTO sees she now reports to "Acquirer's VP Engineering" (not autonomous)
- New managers want to "consolidate tech stacks"
- By M3, CTO gets offer from ex-colleague (25% raise, keep autonomy)
- CTO leaves, taking 50% of team

### Solution
✅ Lock retention **before SPA signature**

**Retention Plan Template:**
```
6.1 KEY PERSON RETENTION

Covered Employees:
  [ ] CTO: [Name]
  [ ] VP Sales: [Name]
  [ ] VP Product: [Name]
  [ ] Lead Backend Eng: [Name]

Retention Commitment (Buyer):
  Year 1: Keep all covered employees in current role (or equivalent)
          No material reduction in authority
          Reporting line: [Specify, e.g., "CTO reports to Acq CTO, 
                           has product autonomy"]
  
  Year 2: [Specify if roles can change, e.g., "CTO can transition 
           to advisory role, so long as successor is mutually agreed"]

Retention Bonus (Paid by Acquirer):
  Per Employee:
    CTO: €500,000 (€250K Month 12, €250K Month 24)
    VP Sales: €250,000 (€125K Month 12, €125K Month 24)
    [etc]
  
  Total: €[X] million
  
  Vesting:
    If employee stays through Month 12: 50% vest (€[X] paid)
    If employee stays through Month 24: 100% vest (€[X] paid)
    
  Clawback:
    If employee voluntarily resigns before M12: No bonus paid
    If employee fired for cause: No bonus paid
    If employee fired without cause: Pro-rata bonus vested

6.2 EARNOUT IMPACT

  Earnout KPIs assume these employees remain through measurement period.
  If any key person leaves, earnout measurement adjusted:
    - For first 3 months: No adjustment
    - For months 4-12: Reduce earnout target by [X]% per person lost
    
  Example:
    CTO leaves M4: Revenue target reduced by 5% (reflects reduced eng capacity)
```

---

## 🔴 ERREUR #5 — Customer Concentration Risk Not Disclosed (Liability)

**Coût típico:** $1-3M escrow clawback | Post-close customer loss

### Problème
- Seller reports "€5M ARR" in LOI
- DD shows: Top 3 customers = 60% of revenue
- Buyer already signed LOI
- Post-close, 1 customer churns (contract ends, didn't renew)
- Buyer claims: "We were misled on customer stability"
- Escrow battle over €2M

### Solution
✅ Proactively disclose concentration + provide customer refs

**Pre-LOI Customer Disclosure:**
```
"Customer Concentration Risk

Top 10 customers = 65% of total ARR (€3.25M of €5M)

Top 5 Customers:
  1. [Company A]    — €800K ARR, renews June 2027 (CONFIRMED)
                      Contact: [CFO name], [email]
  2. [Company B]    — €750K ARR, renews Sept 2027 (CONFIRMED)
                      Contact: [CEO name], [email]
  3. [Company C]    — €600K ARR, renews March 2027 (AT RISK — renegotiating)
                      Contact: [VP Ops name], [email]
  4. [Company D]    — €400K ARR, expires Feb 2027, didn't renew yet
                      Contact: [General Mgr name], [email]
  5. [Company E]    — €380K ARR, renews Jan 2027 (CONFIRMED)
                      Contact: [CRO name], [email]

Mitigation:
  - We've locked 4/5 customers with LOI from them
  - Company D = we're in active renewal discussion (proposal sent)
  - Company C = we're addressing their concerns (new feature coming M2)

Buyer Due Diligence:
  Buyer may call all 5 customer references directly (mutual intro).
"
```

**Customer Ref Call (Buyer Conduct):**
- Buyer calls top 5 customer CFOs/CROs
- Asks: "How critical is this product? Are you renewing?" etc.
- Seller attends call (optional, but recommended)
- This transparency = **prevents escrow disputes**

---

## 🔴 ERREUR #6 — No IP Assignment from Founders

**Coût típico:** $2-5M holdback | Non-transferable IP | Deal may rescind

### Problème
- Seller is SAS (legal entity)
- But founder developed 80% of product on personal laptop
- No written agreement assigning IP to company
- Buyer discovers: "Wait, does Founder own the code?"
- Deal unravels, or 20% escrow holdback

### Solution
✅ Get **IP Assignment Agreement** signed **before LOI**

**IP Assignment Agreement (Founder to Company):**
```
INTELLECTUAL PROPERTY ASSIGNMENT AGREEMENT

Between: [Founder Name] ("Assignor")
And:     [Company Name], SAS ("Assignee")
Date:    [DD/MM/YYYY]

WHEREAS, Assignor has developed certain intellectual property 
while employed by Assignee, and this agreement formalizes ownership.

1. ASSIGNMENT

Assignor hereby assigns to Assignee, effective as of [START DATE], 
all right, title, and interest in:

  (a) All software, code, algorithms, and technical documentation
  (b) All inventions, patents, and patent applications
  (c) All trademarks, trade names, and domain names developed
  (d) All databases, documentation, and technical works
  
Created or developed by Assignor:
  - While employed/engaged by Assignee
  - Using Assignee's resources (equipment, facilities)
  - Whether before or after date hereof (retroactive assignment)

2. COPYRIGHTS & MORAL RIGHTS

Assignor waives all moral rights and copyright claims to the 
above intellectual property, and authorizes Assignee to:
  - Register copyrights in Assignee's name
  - Modify, create derivative works, sublicense

3. EXCLUDED ITEMS

Assignor retains ownership of:
  - [Pre-existing software Assignor owned before employment]
  - [Personal projects unrelated to Assignee's business]
  
[List any exceptions]

4. COOPERATION & ASSISTANCE

Assignor agrees to:
  - Sign any documents necessary to perfect Assignee's ownership
  - Cooperate with patent applications, registrations
  - Assist in IP due diligence for future M&A

5. GOVERNING LAW

Governed by French law, jurisdiction = courts of [Paris/Lyon/etc]

IN WITNESS WHEREOF:

Assignor: _____________________  Date: _______
          [Founder Name]

Assignee: _____________________  Date: _______
          [Company Name], by: [CEO]
```

**Timeline:** Get this signed **immediately** (even if not selling soon)

---

## 🔴 ERREUR #7 — Sales Pipeline Overstated (Growth Lie)

**Coût típico:** $2-3M escrow clawback | Buyer assumes false revenue

### Problème
- Seller says: "€3M pipeline, 50% close rate = €1.5M revenue next 12mo"
- Buyer adds this to valuation model (€5M current + €1.5M pipeline = €6.5M)
- Post-close: Pipeline collapses (many "deals" fake or cold leads)
- Only €200K closed in Year 1
- Earnout targets missed by €500K
- Escrow battle

### Solution
✅ Define "pipeline" carefully, with due diligence

**Sales Pipeline Disclosure (Honest Version):**
```
Sales Pipeline — €3,000,000 Forecast

TIER 1 — LIKELY (70%+ probability, >€100K deal size)
  [Customer Name]  €250K  Proposal sent D10, demo D15, 
                          contract review in-progress. 
                          Expected close: April 2026. Contact: [VP Sales]
  [Customer Name]  €180K  3-month POC ending March 15, 
                          likely to convert. Contact: [Account Mgr]
  [Total T1]:      €900K

TIER 2 — PROBABLE (40% probability, >€50K deal)
  [Customer Name]  €300K  Initial meeting D5, needs board approval. 
                          Expected close Q2 2026. Contact: [Sales Lead]
  [Total T2]:      €400K

TIER 3 — EXPLORATORY (5-10% probability)
  [10+ smaller leads]: €700K   Early-stage discussions, 
                               likely 0-2 will close. Contact: [Lead Gen]

Total Pipeline: €2,000K (T1+T2+T3)

Adjusted for Close Rate: 
  T1 (70% × €900K) = €630K
  T2 (40% × €400K) = €160K
  T3 (5% × €700K)  = €35K
  _______________
  Realistic Y1 forecast: €825K

(Not €1.5M as might be assumed from "€3M pipeline at 50%")
```

**Buyer Due Diligence on Pipeline:**
- Buyer calls 3-5 pipeline prospects directly
- Asks: "Where are you in evaluation?"
- Transparency kills disputes later

---

## 🔴 ERREUR #8 — Failing to Negotiate Non-Dilution Clause

**Coût típico:** $200K-$1M earnout reduction | Tax inefficiency

### Problème
```
SPA Earnout: €5M if revenue hits €6M

Between signing & close (60 days), Seller raises $1M new equity at lower valuation
(dilutes existing shares by 15%)

Earnout now triggers: 
  If revenue = €6M, 
  Seller's 85% share × earnout formula = only €4.25M received

Buyer says: "This was our deal, not your cap table problem"
```

### Solution
✅ Lock cap table in SPA (no new dilution)

---

## 🔴 ERREUR #9 — Not Locking Customer Consent Letters Pre-Close

**Coût típico:** Delay 8-12 weeks | Deal closes late | Earnout timeline slips

### Problème
- SPA signed: "Deal closes when all customer change-of-control consents obtained"
- Seller thought: "Our top customers always consent, should be easy"
- Reality: 3 of top 10 customers slow-roll consent (want to renegotiate price)
- Close delayed 3 months
- Earnout clock keeps ticking anyway (measurement starts post-close, no extension)
- If earnout measured at fixed date, it's now in Q2 not Q1 (seasonality matters)

### Solution
✅ Get customer consents **parallel to SPA negotiation**

**Pre-SPA Customer Outreach:**
```
[D0 — Day 0, when LOI signed]

Seller reaches out to Top 20 customers:

"Hi [Customer CFO/CEO],

We're excited to share that we've agreed to be acquired by [Buyer]. 
This is great news for you because:

  - [Buyer's platform] integrates with ours → more value
  - [Buyer's sales team] will support you → faster deployment
  - [Buyer's R&D] expands roadmap → new features coming

Your contract includes a change-of-control clause, so we want to 
get your approval before closing (likely in 120 days).

Can we schedule a 30-min call this week to discuss?

We expect this to be a formality (your contract terms stay the same), 
but want to make sure you're on board.

Best, [Founder]"

Result: 
  - 90% of customers say "yes" in 1 week
  - 10% want to "discuss" (takes 2-3 weeks)
  - By D30, you have 80%+ consent letters
  - SPA closing condition = already 80% satisfied
  - Close happens on-time
```

---

## 🔴 ERREUR #10 — Earnout KPIs Not Board-Approved

**Coût típico:** Post-close dispute, board rejects earnout calculation

### Problème
- Seller negotiated earnout with Buyer's VP BD
- SPA signed with earnout tied to "Customer NRR ≥ 110%"
- 12 months later, revenue target met, but NRR = 108%
- Buyer's finance team says: "NRR methodology different from what we expected"
- Board refuses to pay
- Escrow litigation ensues

### Solution
✅ Get Buyer's **CFO + Board sign-off** on earnout formula **in SPA**

---

## Final Checklist: 25 Avoid-at-All-Costs Mistakes

- [ ] 1. Data room not organized (pre-prepared 60 days prior)
- [ ] 2. Founder not leading negotiations
- [ ] 3. Earnout KPIs vague (missing 2 decimals of precision)
- [ ] 4. Key person retention not locked (pre-SPA)
- [ ] 5. Customer concentration not disclosed transparently
- [ ] 6. No IP assignment agreement (founder → company)
- [ ] 7. Sales pipeline overstated (no tiers / due diligence)
- [ ] 8. No non-dilution clause (pre-closing equity raises)
- [ ] 9. Customer consents not obtained until post-LOI
- [ ] 10. Earnout formula not board-approved by Buyer

- [ ] 11. No customer reference calls (buyer's due diligence)
- [ ] 12. Tech debt hidden (will cost $500K+ to fix post-close)
- [ ] 13. Employee agreements not signed (can't enforce non-compete)
- [ ] 14. Lease not assignable to buyer (forces breakage cost)
- [ ] 15. Regulatory licenses missing (GDPR, SOC2, industry-specific)

- [ ] 16. Tax filings not clean (open audits, penalties)
- [ ] 17. Related-party transactions not documented (IRS red flag)
- [ ] 18. Supplier contracts have auto-renewal clauses (cost surge post-close)
- [ ] 19. No R&W insurance quote (escrow will be 20% instead of 10%)
- [ ] 20. SPA drafted too quickly (3 days, not 2 weeks of negotiation)

- [ ] 21. Earnout metric doesn't align with post-close strategy (EBITDA if buyer plans cost cuts)
- [ ] 22. Seller team splits after close (no co-founder unity on deal terms)
- [ ] 23. NDA shared too early (signals weak negotiating position)
- [ ] 24. Multiple simultaneous buyers (not coordinated, breeds distrust)
- [ ] 25. Post-close transition plan not documented (earnout at risk from chaos)

---

**Golden Rule:** 
> "If something is ambiguous, it will be litigated in escrow. Write it down now in SPA, 
> or pay lawyers €500/hour later to fight it out."

