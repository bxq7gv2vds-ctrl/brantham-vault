---
name: seller-prep-checklist
description: Pre-process checklist (3 mois avant) — financials, légal, opérations
metadata:
  type: checklist
  created: 2026-06-12
---

# Seller Prep Checklist — 90 Days Before Launch

Complete 3-4 months before you want to start selling. Fixes are faster if you're not under pressure.

---

## Phase 1: Financial Cleanup (Weeks 1-4)

### Revenue & Bookings
- [ ] **Revenue Definition**: Document exactly how you recognize revenue
  - [ ] Document customer contracts (all > $[X]K)
  - [ ] List any discounts/credits applied (last 12m)
  - [ ] Confirm ASC 606 / IFRS recognition method
  
- [ ] **Trailing 12-Month Financials** (audited or reviewed, not compiled)
  - [ ] P&L: Revenue, COGS, OpEx (by function)
  - [ ] Balance sheet: Assets, liabilities, equity
  - [ ] Cash flow: Operating, investing, financing
  - [ ] Get from: Accountant or CFO (not founder estimate)

- [ ] **Customer Contracts**: Create customer roll
  - [ ] [Spreadsheet]: Customer name, ARR, renewal date, contract term, auto-renewal?
  - [ ] Flag any special terms: discounts, payment plans, performance guarantees
  - [ ] List "at risk" renewals in next 12m

- [ ] **Monthly Revenue Trending** (last 24 months)
  - [ ] Graph: ARR trend (smoothed 3-month)
  - [ ] Mark any unusual spikes/drops (acquisitions, churn events)
  - [ ] Calculate: YoY growth rate + QoQ trend

### Profitability & Unit Economics
- [ ] **Gross Margin Calculation** (by revenue stream)
  - [ ] COGS breakdown: Cloud hosting, processing fees, support hours
  - [ ] Allocate payroll (product + CS team) to COGS
  - [ ] Result: Gross margin % (target buyer expectation: >60% SaaS)

- [ ] **CAC & Payback Period**
  - [ ] S&M spend (last 12m): Salaries, tools, events, ads
  - [ ] New customers acquired (count, not revenue)
  - [ ] CAC = total S&M / new customer count
  - [ ] Payback = CAC / (ACV × gross margin %) in months
  - [ ] Target: <12 months payback

- [ ] **Churn & NRR Calculation**
  - [ ] Monthly churn (last 12m): [Churned ARR / starting ARR]
  - [ ] Annual churn: (1 - (1 - monthly_churn)^12) × 100
  - [ ] Expansion revenue (upsells, cross-sells) by month
  - [ ] NRR = (ending ARR / starting ARR) including expansion
  - [ ] Red flag if: Churn >8%/m or NRR <90%

### Normalizing Adjustments (EBITDA)
Buyer will want to see "core EBITDA" (what real cash business generates):

- [ ] **One-time costs** (remove from EBITDA for multiple purposes)
  - [ ] Stock options acceleration cost (if plan to vest post-close)
  - [ ] Severance / contractor terminations
  - [ ] One-time consulting, legal, audit fees
  - [ ] Facility transition costs

- [ ] **Related-party transactions** (disclose + adjust)
  - [ ] Founder salary vs. market rate
  - [ ] Office rent from founder-owned property
  - [ ] Related-party loans
  - [ ] Founder personal expenses billed to company

- [ ] **Normalized EBITDA**: 
  Document = (Operating income) + D&A + (less: one-time costs) + (related-party adjustments)

### Accounting Standards & Records
- [ ] **Chart of accounts review** (with accountant)
  - [ ] Consistent allocation of expenses to P&L
  - [ ] No unusual reclassifications (red flag: hiding spend)
  - [ ] Revenue recognition consistent (no gray areas)

- [ ] **Bank reconciliation & debt schedule**
  - [ ] All bank accounts listed + balances
  - [ ] Outstanding debt: principal, interest rate, maturity, covenants
  - [ ] Loans from founders (terms, repayment schedule)

---

## Phase 2: Legal & Cap Table Cleanup (Weeks 2-5)

### Cap Table
- [ ] **Clean cap table** (Excel or Pulley, all 3 sheets filled)
  - [ ] Common stock: Founder shares (vesting schedule)
  - [ ] Options: All option holders, grant date, vesting, exercise price
  - [ ] Preferred stock: All rounds, terms, conversion rights
  - [ ] Warrants / convertible notes: All outstanding instruments
  - [ ] Fully diluted % (as if all options exercised): [X]% founder, [Y]% investors, [Z]% options

- [ ] **Founder vesting** (CRITICAL)
  - [ ] Current vesting schedule: [X] months total, [Y] month cliff
  - [ ] Unvested shares: [X]% of total
  - [ ] Post-sale acceleration clause: Does it exist? Remove it now (buyers hate it)
  - [ ] Buyer question: "Will founder's equity fully vest post-close?" (answer: ideally no)

- [ ] **Investor agreements** (list of all funding)
  - [ ] List all rounds: Series [X], amount, lead, date
  - [ ] Major terms: Liquidation preference (1x, 2x?), board seats, protective provisions
  - [ ] Conversion: Do preferred convert to common at sale? (check docs)
  - [ ] Pro-rata rights: Any investor has right to more equity? (disclose)

- [ ] **Option pool & option agreements**
  - [ ] Total options granted + outstanding: [X]
  - [ ] Option pool size vs. reserved: (ensure pool isn't over-committed)
  - [ ] Acceleration clauses: Single/double trigger? (clean up if contentious)
  - [ ] Tax issues: ISO vs NSO, [X] employees with underwater options (address before close)

### Contracts & IP
- [ ] **Customer contracts** (sampling, not all)
  - [ ] 3-5 large contracts (>$[X]K): Get full terms
  - [ ] Customer agreement (template): Standard vs. non-standard terms
  - [ ] Any change-of-control provisions? (buyer must approve retention)
  - [ ] Any termination-for-convenience clauses? (can customer cancel anytime?)

- [ ] **Vendor/SaaS agreements** (identify critical ones)
  - [ ] Cloud infra (AWS, GCP, Azure): Cost, commitment, change-of-control?
  - [ ] Any exclusivity / non-compete with vendors
  - [ ] Escrow or insurance details
  - [ ] Payment terms (early termination penalties?)

- [ ] **Intellectual property**
  - [ ] Patents: List all filed (utility, design, international)
  - [ ] Trademarks: [Company name], logo, product names (registered or TM)
  - [ ] Copyrights: Code, documentation (automatic, but document anyway)
  - [ ] Third-party IP: Any open-source (GPL, MIT, etc.)? Document usage
  - [ ] Inventor agreements: All engineers signed IP assignment? (critical)

- [ ] **Employment & IP assignment**
  - [ ] All current employees: Signed employment agreement + IP assignment
  - [ ] Contractor agreements: Specify IP ownership
  - [ ] Any employee disputes (wrongful termination claims)? Disclose

### Regulatory & Compliance
- [ ] **Data privacy & security**
  - [ ] GDPR compliance: Do you process EU data? Privacy policy updated?
  - [ ] Data processing agreements (DPA): All vendors signed?
  - [ ] CCPA (if US): California residents data handling documented
  - [ ] Security certifications: SOC2? ISO27001? (Good to have, not critical)

- [ ] **Tax compliance**
  - [ ] Sales tax nexus: State-by-state registration (if applicable)
  - [ ] State business licenses: Valid, not expired
  - [ ] Payroll tax filings: Current, no outstanding amounts
  - [ ] Income tax returns: Last 2 years filed + copies
  - [ ] Estimated tax payments: Current, no penalties

- [ ] **Insurance**
  - [ ] General liability: Coverage amount, carrier, expiration
  - [ ] E&O / D&O insurance: Exists?
  - [ ] Workers' compensation: Filed, current
  - [ ] Cyber insurance: (Nice to have, emerging requirement)

- [ ] **Employee matters**
  - [ ] No pending claims (wrongful termination, discrimination)
  - [ ] WARN act (if planning layoffs post-close, 60d notice)
  - [ ] No undocumented workers
  - [ ] Benefits: COBRA obligations, 401k status

---

## Phase 3: Operations & Data Cleanup (Weeks 3-6)

### Product & Technology
- [ ] **Code quality audit**
  - [ ] Documentation: README, architecture, setup guide exists
  - [ ] Test coverage: >60% (or document why lower)
  - [ ] Dependency status: Any ancient libraries? Security vulnerabilities?
  - [ ] Deployment process: Automated, repeatable, documented
  - [ ] Disaster recovery: Backup schedule, recovery tested

- [ ] **Infrastructure & data**
  - [ ] Data backups: 30-day retention, tested restore procedure
  - [ ] Database: Migration plan documented (if on old legacy DB)
  - [ ] Performance: Page load, API latency, uptime documented
  - [ ] Monitoring: Error tracking, performance monitoring, alerting in place

- [ ] **Product roadmap**
  - [ ] Next 6-12 months: Write roadmap (for buyer visibility)
  - [ ] Technical debt: Top 3 items listed (not a surprise in DD)
  - [ ] Feature prioritization: How do you decide? (process doc)

### Customer & Revenue
- [ ] **Customer success metrics**
  - [ ] NPS survey results (or customer satisfaction measurement)
  - [ ] Customer health score: Documented, tracked monthly
  - [ ] Churn root cause analysis: Why do customers leave? (last 5 exits)
  - [ ] Reference customers: List of 5-10 willing to speak to buyer

- [ ] **Sales & marketing assets**
  - [ ] Case studies: 2-3 detailed wins (with metrics)
  - [ ] Sales deck: Current, reflects realistic use cases
  - [ ] Marketing collateral: Website, SDRs, content (clean and updated)

### People & Culture
- [ ] **Org chart**
  - [ ] Current structure: Roles, reporting lines
  - [ ] Headcount plan: Hiring needs next 12 months
  - [ ] Compensation: Salaries, bonuses, equity (documented, not surprises)

- [ ] **Key person risk**
  - [ ] CTO resignation risk: Low/medium/high + mitigation
  - [ ] VP Sales resignation risk: Low/medium/high + mitigation
  - [ ] Identify: Who must stay post-close? Why?

---

## Phase 4: M&A Positioning (Weeks 4-8)

### Materials Preparation
- [ ] **One-pager**: [Traction + unique value, 1 page]
- [ ] **CIM**: [Full confidential information memo, 15-20 pages]
- [ ] **Pitch deck**: [Executive version, 10-15 slides]
- [ ] **Customer list**: Top 20, anonymized unless buyer gets NDA
- [ ] **Financials package**:
  - [ ] Last 2 years (P&L, BS, CF)
  - [ ] Last 4 quarters (detailed P&L)
  - [ ] 3-year projection (conservative base case)

### Data Room Structure
- [ ] Create virtual data room (Intralinks, Merrill, Citrix)
- [ ] Organize by category:
  ```
  /Financial (P&L, BS, CF, cap table, tax returns)
  /Legal (cap table docs, employee agreements, IP assignments)
  /Contracts (customer agreements, vendor agreements, insurance)
  /Product (roadmap, technical docs, architecture)
  /Marketing (case studies, pitch deck, CIM, one-pager)
  /Customer (customer list, NPS data, case studies)
  /Operations (org chart, employee handbook, policies)
  ```
- [ ] Upload all docs (don't create "folders only", populate with actual files)
- [ ] Version control: Date files, update manifest as changes come

---

## Phase 5: Team & Board Alignment (Week 8-9)

### Board Communication
- [ ] **Board memo**: Explain M&A intent to board (if you have one)
  - [ ] Why now (market conditions, growth stage, strategic options)
  - [ ] Timeline (6-9 months typical)
  - [ ] Target buyer profiles (strategic, PE, financial)
  - [ ] Valuation expectations (range, not specific number yet)

- [ ] **Board approval**: Get authorization to explore (formal resolution)

### Team Communication
- [ ] **Leadership team**: Brief key people (not all company yet)
  - [ ] "We're exploring strategic options" (vague, intentional)
  - [ ] "Keep doing your job, this may not happen"
  - [ ] "If we get serious, I'll tell you"
  - [ ] NDA if needed (usually not for internal team)

- [ ] **No leaks**: Brief people 1:1, not in group (controls messaging)

---

## Phase 6: Advisor & Professional Prep (Week 8-10)

### Legal & Finance Advisors
- [ ] **M&A attorney**: Engaged, reviewed cap table, key contracts
- [ ] **Investment banker** (optional but recommended if >$10M):
  - [ ] Engaged to help with buyer identification + negotiation
  - [ ] Fee structure: Retainer + success fee (typically 0.75-1.5%)
  
- [ ] **Tax advisor**: Reviewed transaction structure impacts
  - [ ] Stock sale vs. asset sale (major tax implications)
  - [ ] Founder personal tax (earnout treatment, capital gains)
  - [ ] Company-level taxes (cash position impact)

### Professional Materials
- [ ] **Banker pitch list**: If using banker, they have target list
- [ ] **Advisor agreements**: NDA, engagement letter signed
- [ ] **Timeline**: 6-9 month realistic timeline communicated

---

## Red Flags to Fix Before Launch

### Financial
- ❌ "Churn is 15%/month" → Fix: Product improvements, pricing strategy
- ❌ "Revenue mix is 70% one customer" → Fix: Diversify, or accept discount
- ❌ "EBITDA negative and no path to profitability" → Fix: Unit economics clear
- ❌ "Large write-downs or adjustments" → Fix: Document normalized EBITDA

### Legal
- ❌ "Founder equity not vesting" → Fix: Set vesting schedule before process
- ❌ "Investors have drag-along rights blocked" → Fix: Get approval before sale
- ❌ "Employee IP not assigned to company" → Fix: Retroactive IP assignment
- ❌ "Pending litigation or tax audit" → Fix: Disclose, get resolution or escrow

### Operations
- ❌ "Key person dependency" → Fix: Cross-train, document knowledge
- ❌ "Product architecture is spaghetti" → Fix: Document it, accept premium discount
- ❌ "No customers under NDA willing to speak" → Fix: Build references list
- ❌ "Compliance issues (GDPR, data security)" → Fix: Audit + remediate

---

## Pre-Launch Readiness Checklist

### Financial
- [ ] 2 years of audited / reviewed financials
- [ ] Cap table clean, fully diluted share count confirmed
- [ ] Customer concentration analysis (top 5 = [X]%)
- [ ] NRR + churn + CAC payback calculated
- [ ] Normalized EBITDA reconciled

### Legal
- [ ] All employees signed IP assignments
- [ ] Major contracts (>$[X]K) reviewed + summarized
- [ ] No pending litigation or IP disputes
- [ ] Tax returns filed, current, no liens

### Operations
- [ ] Product roadmap documented
- [ ] Code quality audit done, technical debt listed
- [ ] 5+ customer references ready (willing to speak)
- [ ] Org chart + headcount plan clear

### M&A Materials
- [ ] CIM drafted + board approved
- [ ] Data room populated (100+ documents minimum)
- [ ] Pitch deck practiced (2 version: 10-slide + 30-slide)
- [ ] Banker engaged (if applicable)

---

## Timeline: Weeks 1-10

```
Week 1-2:  Financial cleanup (accountant review)
Week 2-3:  Cap table + legal docs
Week 3-4:  IP audit + contract review
Week 4-6:  Operations audit (tech, product, customer)
Week 6-8:  M&A materials (CIM, deck, data room)
Week 8-9:  Board + team alignment
Week 9-10: Advisor prep + timeline confirmation

Week 11+:  Ready to start buyer conversations
```

**Use case**: Copy this, work through in order, check boxes. By week 11, you're ready to call your first buyer.
## Related
## Related
## Related
