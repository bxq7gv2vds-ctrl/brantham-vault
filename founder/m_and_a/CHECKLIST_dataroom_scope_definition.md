---
name: checklist-dataroom-scope-definition
description: Checklist — What to prepare, when to release, phased access strategy
metadata:
  type: checklist
  created: 2026-06-13
---

# Data Room Scope Definition

Use this to decide what goes in the data room and in what order.

## Phase 1: Pre-NDA (Public-Safe Only)

Release **BEFORE** any confidentiality agreement is signed. This is your teaser.

- [ ] 1-page executive summary (no numbers, just vision + traction)
- [ ] Product screenshots or demo link
- [ ] Team bios (short, LinkedIn-style)
- [ ] 3–5 customer logos (anonymized if needed: "$20M B2B SaaS company")
- [ ] High-level growth chart (last 3 years, no per-customer detail)

**Phased release:** Give access via secure link (Notion, Google Drive) with view-only access. No download.

---

## Phase 2: Post-NDA, Pre-LOI ("Customer-Light")

Released after buyer signs basic NDA. Still protects you from strategic shopping.

**Financial (Last 3 years):**
- [ ] Annual tax returns (full with schedules)
- [ ] YTD P&L (month-by-month, no cost per customer)
- [ ] Balance sheet (YTD vs prior year)
- [ ] Cash flow summary (quarterly, not daily)
- [ ] Bank account statements (last 6 months, last 3 transactions per page redacted)

**Product / Operations:**
- [ ] Feature roadmap (next 12 months, anonymized risks)
- [ ] Customer metrics summary (cohort analysis, without customer names)
- [ ] Churn analysis (by segment, not per customer)
- [ ] Sales pipeline (aggregate, not named deals)
- [ ] Pricing sheet (current + historical)

**Team:**
- [ ] Org chart
- [ ] Headcount summary + plan (next 12 months)
- [ ] Key person employment agreements (founder + critical hires)

**Legal / Compliance:**
- [ ] Company formation docs (Certificate of Incorporation, bylaws)
- [ ] Equity cap table (fully diluted, all option pools)
- [ ] List of material contracts (not full text, just titles + termination clauses)
- [ ] Insurance policies (summary, not full docs)
- [ ] Privacy policy + terms of service

**Technology (High-Level):**
- [ ] System architecture diagram (boxes, no IP exposure)
- [ ] Tech stack (languages, databases, hosting)
- [ ] Security summary (certifications: SOC 2, ISO 27001, etc.; last audit date)
- [ ] Disaster recovery + uptime SLA (no internal passwords)

**Phased Release:** Release in tranches (financial → team → legal → tech) to control pacing.

---

## Phase 3: Post-LOI ("Full Access")

Released after buyer signs LOI. Now you can release sensitive data.

**Customer Contracts:**
- [ ] All customer contracts (show per-customer economics, multi-year deals, termination terms)
- [ ] Contracts with largest 10 customers (name + revenue detail)
- [ ] List of any change-of-control contract clauses (e.g., "customer can terminate if acquired")

**Deep Financial:**
- [ ] Monthly P&L (last 24 months)
- [ ] Customer LTV/CAC analysis (by acquisition source)
- [ ] Gross margin detail (by customer segment, product line)
- [ ] OpEx breakdown (by department, team)
- [ ] Cash position detail (all bank accounts, outstanding payables/receivables)
- [ ] Debt schedules (term loans, lines of credit, payment terms)

**Deep Legal:**
- [ ] Full contracts (all material agreements)
- [ ] IP documentation (patent filings, copyrights, trademarks, licensing)
- [ ] Employee agreements (all non-standard clauses, non-competes)
- [ ] Litigation history (copies of settled cases, ongoing exposure)
- [ ] Tax returns with full schedules (all years)
- [ ] Regulatory compliance records (data privacy audits, industry certifications)

**Technology Deep Dive:**
- [ ] Code repositories access (if buyer needs technical DD)
- [ ] Infrastructure documentation (cloud hosting, disaster recovery playbooks)
- [ ] Customer data security protocols (backup frequency, encryption, compliance)
- [ ] Third-party integrations (list of all APIs, data flows)
- [ ] Known technical debt (component list, estimated refactor effort)

**Board / Stakeholder:**
- [ ] Board meeting minutes (last 8 quarters)
- [ ] Investor agreements (SAFEs, convertible notes, equity docs)
- [ ] Any shareholder communications re: sale process

---

## What NOT to Include (Ever)

- [ ] Personal emails / Slack conversations (outside of formal agreements)
- [ ] Draft versions of contracts (only final signed versions)
- [ ] Salary information for individual employees (aggregate only)
- [ ] Sensitive customer feedback / complaint letters
- [ ] Internal competitive analysis documents (if they show you're worried)
- [ ] Founder personal financial docs (tax returns, loans, assets)
- [ ] Privileged attorney-client communications (marked "PRIVILEGED")

---

## Access Control Strategy

| Phase | Who | Duration | Expiry | Download? |
|---|---|---|---|---|
| Pre-NDA | Anyone | Until LOI | Never | No, link-only view |
| Post-NDA | Qualified buyer team (CFO, legal) | Until LOI or 90 days | Revoke upon deal close | Yes, but tracked |
| Post-LOI | Full buyer team + advisors | Until close | Indefinite | Yes, tracked |

**Tool recommendation:** Intralinks, Citrix ShareFile, or Databox (all track access, allow revocation, show who viewed what, when).

---

## Tactical Timing

**Week 1:** Release Phase 1 (teaser). Goal: prove you're real.
**Week 2–3:** Post-NDA, release Phase 2 incrementally (3–5 docs/day). Goal: control pacing, show no red flags.
**Week 4+:** Post-LOI, release Phase 3 (dump full data room in one go). Goal: final due diligence.

**Red flag avoidance:** If buyer waits >1 week between each phase for documents, they're either (a) not serious, or (b) found something concerning. Flag your advisor.

---

## Redaction Strategy

Before releasing ANY document:
- Redact employee names → "Employee A, Employee B" or "salesperson"
- Redact customer names → use initials or customer segment ("Fortune 500 retailer")
- Redact exact revenue per customer → use ranges ("$50–100k ARR")
- Keep total revenue, not individual customer detail (until Post-LOI)

This protects:
1. Employee privacy (they don't know you're selling yet)
2. Customer confidentiality (competitors don't learn your client list)
3. Your leverage (buyer doesn't know who your biggest customers are until committed)

---

## Checklists by Buyer Type

**Strategic Buyer** → Extra focus: customer contracts (change-of-control), tech deep dive (integration risk), market/competitive positioning
**PE Buyer** → Extra focus: financials deep dive, management team info, customer concentration, debt covenants
**Founder Acquirer** → Extra focus: technology architecture, customer support playbooks, team retention
**Investor/Roll-up** → Extra focus: unit economics, COGS structure, customer LTV by cohort

---

**Pro Tip:** Use a **Data Room Index** (Google Sheet) to track every document, its sensitivity level (public/confidential/privileged), who has access, and when it was accessed. Share this with buyer's legal team so they know what's available without you hand-holding.**
