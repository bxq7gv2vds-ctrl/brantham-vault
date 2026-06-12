---
name: data_room_checklist_60items
description: Checklist 60 items pour data room — hiérarchisé par criticité pour acheteurs SaaS
metadata:
  type: checklist
  created: 2026-06-12
---

# Data Room Checklist — 60 Items (Priorité & Format)

**Pour:** Founder préparing vente SaaS  
**Durée setup:** 3-5 jours  
**Scope:** Financial, Legal, Tech, Customers, IP, Compliance

---

## TIER 1 : CRITICAL (15 items) — Les 3 premiers jours

### Financial (5)
- [ ] **Tax returns** (corporate + personal, last 3 years) — PDF + original
- [ ] **Income statement** (last 3 years, monthly YTD) — Excel, audited/reviewed preferred
- [ ] **Balance sheet** (current + last 2 years) — with explanations of anomalies
- [ ] **Cash flow statement** (last 2 years monthly) — shows burn rate + runway
- [ ] **ARR breakdown by customer** (top 20, trailing 12 months) — Excel with churn tracking

### Legal (5)
- [ ] **Cap table** (latest, all instruments) — Excel with vesting schedules
- [ ] **Articles of incorporation** (bylaws, amendments) — clean copies
- [ ] **Shareholder agreements** (all investor docs) — redacted if sensitive
- [ ] **Board minutes** (last 3 years) — shows decisions, conflicts
- [ ] **Employment agreements** (founder + key hires) — non-competes highlighted

### Tech (3)
- [ ] **Architecture diagram** (current stack) — 1-pager explaining scaling
- [ ] **Security audit report** (recent, 3rdparty) — or executive summary
- [ ] **Infrastructure setup** (AWS/GCP account structure, backups) — access checklist

### Customers (2)
- [ ] **Top 20 customer contracts** — sorted by ARR, note NDA status
- [ ] **Churn analysis** (last 24 months by cohort) — shows retention risk

---

## TIER 2 : HIGH (20 items) — Days 4-7

### Financial (7)
- [ ] **Unit economics spreadsheet** — CAC, LTV, payback period
- [ ] **Pricing model** (current + historical changes) — with rationale
- [ ] **Payroll + benefits breakdown** (headcount by role, cost) — Excel
- [ ] **Rent/facilities** (lease terms, remaining duration) — PDF
- [ ] **Debt schedule** (loans, credit lines, terms) — balance + maturity
- [ ] **Insurance policies** — D&O, general liability, cyber
- [ ] **Customer acquisition channels** (cost per channel, conversion rates) — spreadsheet

### Legal (6)
- [ ] **Vendor contracts** (top 10 by spend) — note any termination clauses
- [ ] **Lease agreement** (office/data center) — termination terms
- [ ] **IP assignment** (founder → company) — all founders, all IP types
- [ ] **Confidentiality agreements** (NDAs, non-solicitation) — key employees
- [ ] **Debt agreements** (terms, covenants, prepayment penalties) — lender approval for sale?
- [ ] **Affiliate agreements** (partnerships, resellers, etc.) — check for change-of-control clauses

### Tech (4)
- [ ] **Dependency audit** (all open-source + commercial libraries) — list with licenses
- [ ] **Test coverage report** (unit, integration, E2E %) — recent run
- [ ] **Uptime/performance SLA history** (last 24 months) — shows stability
- [ ] **Security incidents log** (breaches, vulnerabilities, fixes) — transparency = trust

### Customers (3)
- [ ] **Customer list** (all 100+ if small, stratified sample if large) — with MRR/ARR
- [ ] **Expansion revenue** (upsells, cross-sells) — last 24m by customer
- [ ] **Contract terms summary** — duration, auto-renewal, cancellation terms

---

## TIER 3 : MEDIUM (15 items) — Days 8-10

### Financial (4)
- [ ] **Forward projections** (3-5 year model) — conservative, realistic base case
- [ ] **Cost breakdowns** — COGS, R&D, S&M, G&A %, trends
- [ ] **Working capital analysis** — receivables/payables aging
- [ ] **Facilities costs** (utilities, maintenance forecasts) — post-close obligations

### Legal (5)
- [ ] **Litigation history** — no pending lawsuits? List any threats
- [ ] **Regulatory compliance** (SOC 2 / ISO 27001 / HIPAA if applicable) — certs/audit reports
- [ ] **Product liability insurance** — coverage terms
- [ ] **Board resolutions** (recent, authorizing sale) — shows proper governance
- [ ] **Capitalization history** (seed/Series rounds, SAFEs, etc.) — explain each

### Tech (3)
- [ ] **Database schema** (main entities, relationships) — visual + documentation
- [ ] **Disaster recovery plan** — tested, RTO/RPO targets
- [ ] **API documentation** (integrations, webhooks, deprecated endpoints) — developer-facing

### Customers (2)
- [ ] **NPS score** (historical trend, recent survey) — shows satisfaction
- [ ] **Competitor win/loss analysis** — why do they leave? Why choose you?

### IP (1)
- [ ] **Trademark registrations** (USPTO status, international) — pending?

---

## TIER 4 : BASELINE (10 items) — Days 11-14

### Compliance & HR (5)
- [ ] **Employee handbook** — policies, benefits, termination
- [ ] **Equity grants log** — all options, RSUs, vesting status
- [ ] **Payroll records** — last 2 years W2s, 1099s, taxes paid
- [ ] **Benefit plans** — health insurance, 401k, deferred comp details
- [ ] **Background checks** (if required by industry) — documentation

### Tech (2)
- [ ] **Code repository access** — GitHub/GitLab for audit
- [ ] **CI/CD pipeline configuration** — GitHub Actions/Buildkite setup

### Legal (3)
- [ ] **Insurance policy copies** — full terms, not just declarations
- [ ] **Tax correspondence** — any audits, notices, resolutions
- [ ] **Board observer agreements** (if VC-backed) — restrictions?

---

## TIER 5 : NICE-TO-HAVE (0 points, contextual)

- [ ] **Founder blog posts / thought leadership** — shows credibility
- [ ] **Customer testimonials & case studies** — marketing materials
- [ ] **Press releases & media coverage** — traction signal
- [ ] **Awards / recognition** — validating third-party endorsements
- [ ] **Team headshots / bios** — for cultural fit assessment
- [ ] **Product roadmap** (sanitized) — future vision clarity
- [ ] **Slack/Discord channel screenshots** — community engagement

---

## Data Room Organization (Folder Structure)

```
/data-room/
├─ 1_Financial/
│  ├─ Tax_Returns/
│  ├─ Financials (audited)/
│  ├─ Projections/
│  └─ Unit_Economics/
├─ 2_Legal/
│  ├─ Cap_Table/
│  ├─ Incorporation/
│  ├─ Shareholder_Agreements/
│  ├─ Employment/
│  ├─ Contracts (Vendor + Customer)/
│  └─ Litigation/
├─ 3_Technology/
│  ├─ Architecture/
│  ├─ Security_Audit/
│  ├─ Dependencies/
│  ├─ Code (GitHub access link)/
│  └─ Infrastructure/
├─ 4_Customers/
│  ├─ Top_20_Contracts/
│  ├─ Customer_List/
│  ├─ Churn_Analysis/
│  └─ NPS/
├─ 5_IP/
│  ├─ Trademarks/
│  ├─ Patents/
│  └─ Copyright (assignments)/
├─ 6_Compliance/
│  ├─ SOC2/
│  ├─ GDPR/CCPA/
│  └─ Insurance/
└─ README.txt (access instructions, last updated date)
```

---

## Setup Mechanics

### Pre-Close (Founder)
1. **T-7d:** Gather all Tier 1 items
2. **T-5d:** Organize, name files consistently (YYYY-MM-DD format)
3. **T-3d:** Redact sensitive info (salaries, investor terms) if needed
4. **T-0:** Upload to Intralinks / Merrill DataSite / custom SharePoint
5. **Test access** with your M&A advisor before buyer sees

### During Diligence (Buyer Access)
- **Request log:** Buyer sees what you upload, not before
- **Q&A turnaround:** Commit to 24-48h response on follow-ups
- **Access hours:** 9am-6pm your time (don't leave it open 24/7 = suggests carelessness)
- **Viewing restrictions:** IP access read-only, no downloads (unless waived)

### Red Flags (What to Fix Before Uploading)
- ❌ Outdated financial statements → Get latest P&L
- ❌ Contradictory revenue figures → Reconcile with accountant
- ❌ Missing customer contracts → Recreate LOI if lost
- ❌ Unsigned IP assignments → Have founder sign immediately
- ❌ Open litigation → Settle or disclose with legal counsel opinion
- ❌ No security audit → Commission one ($10-30k) — worth it
- ❌ High churn hidden → Disclose with retention plan

---

## Scoring & Audit

Use this checklist weekly:

| Tier | Items | Must-Haves | Your Score |
|------|-------|-----------|-----------|
| T1 | 15 | 15/15 | ___ |
| T2 | 20 | 18/20 | ___ |
| T3 | 15 | 12/15 | ___ |
| T4 | 10 | 8/10 | ___ |
| **Ready to Share?** | **60** | **≥53/60** | ___ |

**If score <53:** Not ready; focus on gaps before showing to buyer.

---

## Tips for Success

1. **Narrative over exhaustion** — Don't upload everything; tell a story (3-year growth, path to profitability)
2. **Recent is better than perfect** — A clean March statement beats a polished January one
3. **Transparency = credibility** — Flag issues yourself; buyers respect honesty
4. **Advisor review** — Have M&A counsel vet before upload (catches legal landmines)
5. **Dry run** — Share with friendly investor for feedback; iterate before real buyer sees
## Related
