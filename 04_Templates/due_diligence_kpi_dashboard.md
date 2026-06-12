---
name: due_diligence_kpi_dashboard
type: template
version: 1.0
date: 2026-06-12
---

# Tableau de Bord KPI — Due Diligence M&A

**Usage:** Suivre en temps réel la complétude + risques de DD (financial, tech, legal). Target : 95%+ complétude avant SPA signature.

---

## 1. Score Global de DD (Target: 95%+)

```
╔════════════════════════════════════════════╗
║   Due Diligence Progress Dashboard         ║
╠════════════════════════════════════════════╣
║ Financial DD        [████████░░]  84%     ║
║ Technical DD        [███████░░░]  70%     ║
║ Legal DD            [██████░░░░]  60%     ║
║ Commercial DD       [████████░░]  81%     ║
║ Compliance/Tax      [█████░░░░░]  54%     ║
╠════════════════════════════════════════════╣
║ OVERALL DD SCORE    [███████░░░]  74%     ║
║ Target by LOI       [██████░░░░]  80%     ║
║ Target by SPA       [███████████] 95%     ║
╚════════════════════════════════════════════╝
```

---

## 2. Financial DD — Checklist (40 items, 30 days)

### Tier 1: Critical (Must-Have by Day 30)
- [ ] **YTD P&L** (Jan-May 2026) + YoY comparison, GAAP
  - Status: __ | Owner: ___ | Est. Days Remaining: _
- [ ] **Balance Sheet** (latest month-end + YTD) with cash, debt, AR aging
  - Status: __ | Owner: ___ | Est. Days Remaining: _
- [ ] **Cash Flow Statement** (12 months historical + forecast 12mo)
  - Status: __ | Owner: ___ | Est. Days Remaining: _
- [ ] **Revenue Breakdown** (by product, customer segment, geography, contract type)
  - Status: __ | Owner: ___ | Est. Days Remaining: _
- [ ] **Customer concentration** (top 20 customers = X% revenue, churn rate)
  - Status: __ | Owner: ___ | Est. Days Remaining: _
- [ ] **Headcount & payroll** (current, historical 24mo, contractors)
  - Status: __ | Owner: ___ | Est. Days Remaining: _
- [ ] **Cap table & option pool** (all shares, fully-diluted, vesting schedules)
  - Status: __ | Owner: ___ | Est. Days Remaining: _
- [ ] **Debt agreements** (loans, lines of credit, covenants, refinancing risk)
  - Status: __ | Owner: ___ | Est. Days Remaining: _

**Tier 1 Completeness:** `__/8` (Target by D30: 100%)

### Tier 2: Important (Must-Have by Day 50)
- [ ] **Monthly financials 24mo** (not just YTD) — see trend
- [ ] **Debt schedules** + covenants compliance testing
- [ ] **Related party transactions** (founder loans, cross-dealings)
- [ ] **ARR/MRR** + expansion vs. churn cohort analysis
- [ ] **Unit economics** (CAC, LTV, payback, gross margin %)
- [ ] **Audit trail** (who prepared P&L, controls, reconciliations)
- [ ] **Changes in accounting** (recognized revenue differently last year?)
- [ ] **Post-period events** (commitments, contingencies post-balance sheet date)

**Tier 2 Completeness:** `__/8` (Target by D50: 80%)

### Tier 3: Supporting (For SPA reps)
- [ ] EBITDA adjustments (add-backs: one-time, stock comp, founder perks)
- [ ] Tax provision analysis (effective tax rate, state/local, deferred taxes)
- [ ] Warranty/liability claims history (insurance, customer disputes)
- [ ] Material contracts affecting revenue (procurement, big customer deals)
- [ ] Intercompany transactions (if multi-entity)
- [ ] Lease obligations (real estate, software, hardware)
- [ ] Pension/benefits liabilities (401k match, health insurance accruals)
- [ ] Revenue recognition policy audit (per ASC 606, look for red flags)

**Tier 3 Completeness:** `__/8` (Target by D70: 100%)

**Financial DD Score = (Tier1 + Tier2×0.8 + Tier3×0.5) / 24 × 100 = ___%**

---

## 3. Technical DD — Checklist (25 items, 25 days)

### Architecture & Code Quality (8 items)
- [ ] **Codebase review** (GitHub/GitLab access, 1-2 key code paths audited)
  - Pain: __ | Tech debt: __ | % Legacy code: __ | Owner: ___
- [ ] **Architecture diagram** (how do data flow, 3rd-party integrations, DBs)
  - Red flags (monolith, single point of failure): __ | Owner: ___
- [ ] **Deployment pipeline** (CI/CD, test coverage, incident response)
  - Deployment frequency: __ | Lead time: __ | Owner: ___
- [ ] **Database schema** (size, growth rate, indexing strategy)
  - Size GB: __ | Growth mo: __ | Major tables: __ | Owner: ___
- [ ] **Security review** (OWASP top 10, known CVEs, penetration testing done?)
  - Vulnerabilities found: __ | Critical: __ | Owner: ___
- [ ] **Performance/scalability** (load tested to __ RPS, p95 latency __)
  - Current RPS: __ | P95ms: __ | Bottleneck: __ | Owner: ___
- [ ] **Disaster recovery** (backup strategy, RTO/RPO, tested failover)
  - RTO: __ | RPO: __ | Last test: __ | Owner: ___
- [ ] **Tech stack maturity** (languages, frameworks, EOL risk)
  - Stack: __ | End-of-life risk: __ | Migration effort: __ | Owner: ___

**Architecture Score: `__/8`**

### Infrastructure & DevOps (6 items)
- [ ] **Cloud infra audit** (AWS/GCP/Azure regions, cost, reserved vs on-demand)
  - Provider: __ | Monthly cost: $__ | Optimization potential: __ | Owner: ___
- [ ] **Infrastructure-as-code** (Terraform, CloudFormation, or manual?)
  - IaC coverage: __% | Version controlled: Y/N | Owner: ___
- [ ] **Monitoring & alerting** (Datadog, NewRelic, CloudWatch — what's covered?)
  - Tool: __ | MTTR: __ | Alert fatigue: __ | Owner: ___
- [ ] **Vendor lock-in** (AWS-specific services, proprietary APIs)
  - Lock-in risk: Low/Med/High | Mitigation: __ | Owner: ___
- [ ] **Compliance & data residency** (GDPR, SOC2, industry-specific)
  - Certs: __ | Audit schedule: __ | Owner: ___
- [ ] **Cost benchmarking** (is $__/mo typical for __ scale? overspend risk?)
  - Spend vs. Benchmark: __% over | Savings potential: $__/mo | Owner: ___

**Infrastructure Score: `__/6`**

### Dependencies & Integrations (6 items)
- [ ] **Third-party APIs** (Stripe, Twilio, Salesforce — deeply integrated?)
  - Critical integrations: __ | Switching cost: __ | Owner: ___
- [ ] **Open-source dependencies** (license audit, security patches, EOL tracking)
  - Count: __ | GPL dependencies: __ | EOL count: __ | Owner: ___
- [ ] **Data integrations** (ETL, webhooks, API clients — custom built?)
  - % custom vs. managed: __ | Brittle points: __ | Owner: ___
- [ ] **Embedded libraries** (vs. microservices — easy to rip out?)
  - Coupling risk: Low/Med/High | Decoupling effort: __ | Owner: ___
- [ ] **API stability** (backward compat, versioning, deprecation plan)
  - Versions supported: __ | Breaking changes: __/yr | Owner: ___
- [ ] **SDK/Plugin ecosystem** (customer-facing, how much revenue?)
  - Revenue from integrations: $__/mo | Ecosystem stickiness: __ | Owner: ___

**Integration Score: `__/6`**

### People & Knowledge (5 items)
- [ ] **Engineering team depth** (# senior devs, knowledge concentration)
  - Senior devs: __ | Architects: __ | Bus factor: __ | Owner: ___
- [ ] **Onboarding time** (how long to become productive, docs quality)
  - Days to deploy: __ | Doc quality: Poor/Fair/Good | Owner: ___
- [ ] **Turnover risk** (retention agreements, key person risk)
  - Turnover rate: __% | Key people staying: Y/N | Owner: ___
- [ ] **Tech debt backlog** (estimated refactor effort, prioritized?)
  - Tech debt estimate: __mo | % of sprint capacity: __ | Owner: ___
- [ ] **Innovation velocity** (time to ship features, experimentation culture)
  - Feature lead time: __d | Experiments/mo: __ | Owner: ___

**People Score: `__/5`**

**Technical DD Score = (Architecture + Infrastructure + Integration + People) / 25 × 100 = ___%**

---

## 4. Legal DD — Checklist (35 items, 28 days)

### Contracts & Commitments (12 items)
- [ ] **Customer contracts** (count, average term, auto-renewal, termination clauses)
  - Count: __ | Avg term: __ mo | Change-of-control clauses: __ (##) | Owner: ___
- [ ] **Vendor contracts** (critical vendors, switching costs, auto-renew)
  - Critical: __ | Auto-renew risk: __ | Owner: ___
- [ ] **Employment agreements** (stock options, severance, non-compete)
  - # with severance: __ | Change-of-control clauses: __ | Owner: ___
- [ ] **Board resolutions** (all decisions properly documented, quorum met)
  - Compliance: __ | Gaps: __ | Owner: ___
- [ ] **Intellectual property** (patents, trademarks, copyrights, licenses)
  - Patents: __ | Pending: __ | Trade secrets: __ | Owner: ___
- [ ] **Data processing agreements** (GDPR DPA with customers, processors)
  - DPA count: __ | Updated: Y/N | GDPR compliance: Y/N | Owner: ___
- [ ] **Insurance policies** (D&O, liability, cyber, coverage gaps)
  - D&O: $__ | Retention: $__ | Owner: ___
- [ ] **Regulatory licenses** (if SaaS, any industry regs?)
  - Licenses: __ | Renewal dates: __ | Owner: ___
- [ ] **Real estate** (office leases, co-location agreements)
  - Leases: __ | Break clauses: __ | Owner: ___
- [ ] **Debt agreements** (terms, covenants, prepayment penalties)
  - Debt: $__ | Prepay penalty: __ | Owner: ___
- [ ] **Related-party contracts** (founder arrangements, family members)
  - Count: __ | Arm's length: Y/N | Owner: ___
- [ ] **Affiliate agreements** (any related entities?)
  - Entities: __ | Intercompany flow: $__ | Owner: ___

**Contracts Score: `__/12`**

### Litigation & Compliance (10 items)
- [ ] **Litigation history** (lawsuits, settlements, threatened claims)
  - Active cases: __ | Settled: __ | Accrued: $__ | Owner: ___
- [ ] **Regulatory actions** (FDA, FTC, state AG, etc.)
  - Inquiries: __ | Enforcement: __ | Owner: ___
- [ ] **Tax compliance** (income tax, sales tax, withholding)
  - Audits pending: Y/N | Accruals: $__ | Owner: ___
- [ ] **Employment law** (wage & hour, discrimination, union)
  - Claims: __ | Accrued: $__ | Owner: ___
- [ ] **Contractual disputes** (with customers, vendors, partners)
  - Disputes: __ | Potential liability: $__ | Owner: ___
- [ ] **Compliance audit** (SOC2, ISO, industry standards met?)
  - Certs: __ | Audit schedule: __ | Owner: ___
- [ ] **Anti-corruption** (FCPA, bribery, export controls)
  - Risk: Low/Med/High | Owner: ___
- [ ] **Privacy & data security** (GDPR, CCPA, state laws)
  - Breaches: __ | Remediation: __ | Owner: ___
- [ ] **Environmental & health** (if physical product, hazmat, waste)
  - Exposure: __ | Owner: ___
- [ ] **Government contracts** (FAR compliance, security clearances)
  - Contracts: __ | Clearances: __ | Owner: ___

**Litigation Score: `__/10`**

### Intellectual Property (8 items)
- [ ] **Patent portfolio** (granted, pending, freedom-to-operate audit)
  - Granted: __ | Pending: __ | FTO risk: Low/Med/High | Owner: ___
- [ ] **Trademark registrations** (US, EU, China if needed)
  - Registered: __ | Pending: __ | Owner: ___
- [ ] **Copyright ownership** (all code, docs, artwork assigned to company?)
  - Assignment audit: __% complete | Gaps: __ | Owner: ___
- [ ] **Open-source compliance** (GPL/MIT/Apache usage, disclosure)
  - GPL dependencies: __ | Disclosure done: Y/N | Owner: ___
- [ ] **Trade secret protection** (NDAs with employees, access controls)
  - Employees signed: __% | Access controls: Y/N | Owner: ___
- [ ] **Founder IP assignment** (did founder properly assign pre-existing IP?)
  - Assignment: Y/N | Gaps: __ | Owner: ___
- [ ] **Third-party IP claims** (cease & desist, licensing disputes)
  - Claims: __ | Pending: __ | Owner: ___
- [ ] **Domain names & assets** (all registered to company? expiration dates?)
  - Domains: __ | Registered owner: __ | Owner: ___

**IP Score: `__/8`**

### Organizational (5 items)
- [ ] **Corporate structure** (subsidiaries, holding companies, multi-entity)
  - Structure: __ | Simplification needed: Y/N | Owner: ___
- [ ] **Cap table accuracy** (all shares issued, options granted, no discrepancies)
  - Accuracy: __% | Audit: __ | Owner: ___
- [ ] **Minority shareholder rights** (drag-along, anti-dilution, liquidation pref)
  - Clauses: __ | Issues: __ | Owner: ___
- [ ] **Founder/Employee agreements** (clawback, claw-back holdback, post-close terms)
  - Agreements: __ | Compliance: Y/N | Owner: ___
- [ ] **Disclosure documents** (stock purchase, SAFE, operating agreement accuracy)
  - Accuracy: __% | Owner: ___

**Organizational Score: `__/5`**

**Legal DD Score = (Contracts + Litigation + IP + Organization) / 35 × 100 = ___%**

---

## 5. Commercial DD — Checklist (20 items, 20 days)

### Customers & Revenue (8 items)
- [ ] **Customer list** (name, contract value, renewal date, key contact)
  - Count: __ | Top 10 = __% revenue | Owner: ___
- [ ] **Product mix** (which products = revenue, which are loss-leader)
  - Product A: __% | Product B: __% | Owner: ___
- [ ] **Pricing strategy** (is pricing optimized, or has it been static 3y?)
  - Last increase: __ mo ago | Elasticity tested: Y/N | Owner: ___
- [ ] **Contract terms** (avg contract value, term length, renewal rate)
  - ACV: $__ | Term: __ mo | NRR: __% | Owner: ___
- [ ] **Customer segmentation** (by industry, company size, use case)
  - Segments: __ | Concentration: __ | Owner: ___
- [ ] **Win/loss analysis** (why lost deals, competitor positioning)
  - Win rate: __% | Avg sales cycle: __ d | Owner: ___
- [ ] **Geographic breakdown** (which regions, concentration risk)
  - US: __% | EU: __% | Owner: ___
- [ ] **Customer health** (NPS, support tickets, feature requests trends)
  - NPS: __ | Churn risk: __ | Owner: ___

**Customer Score: `__/8`**

### Market & Competition (6 items)
- [ ] **Market size** (TAM, SAM, market growth rate)
  - TAM: $__ | Growth: __% YoY | Owner: ___
- [ ] **Competitive positioning** (vs. 3 main competitors, feature parity)
  - Competitors: __ | Differentiation: __ | Owner: ___
- [ ] **Market trends** (consolidation, buyer preferences, emerging threats)
  - Trends: __ | Threat: __ | Owner: ___
- [ ] **Barriers to entry** (what prevents new competitors)
  - Moat: Strong/Medium/Weak | Owner: ___
- [ ] **Partnership ecosystem** (integrations, channels, strategic relationships)
  - Partners: __ | Channel revenue: $__/mo | Owner: ___
- [ ] **Brand perception** (customer loyalty, brand awareness vs. competitors)
  - Brand NPS: __ | Loyalty: __% | Owner: ___

**Market Score: `__/6`**

### Sales & Marketing (6 items)
- [ ] **Sales organization** (team size, quota attainment, hiring pipeline)
  - Reps: __ | Quota: __% | Owner: ___
- [ ] **Marketing ROI** (CAC, payback, channel efficiency)
  - CAC: $__ | Payback: __ mo | Owner: ___
- [ ] **Sales pipeline** (forecast accuracy, pipeline health, typical stages)
  - Accuracy: __% | Pipeline: $__/mo | Owner: ___
- [ ] **Sales cycle** (typical length, deal progression, bottlenecks)
  - Cycle: __ d | Close rate: __% | Owner: ___
- [ ] **Customer acquisition strategy** (direct sales, self-serve, marketplace)
  - Channel mix: __ | Growth strategy: __ | Owner: ___
- [ ] **Retention & upsell** (expansion revenue, churn, account management)
  - NRR: __% | Churn: __% | Upsell: $__/mo | Owner: ___

**Sales Score: `__/6`**

**Commercial DD Score = (Customer + Market + Sales) / 20 × 100 = ___%**

---

## 6. Compliance & Tax DD — Checklist (15 items, 25 days)

- [ ] **Tax structure optimization** (is company optimized for acquirer's tax regime?)
  - Status: __ | Opportunity: $__/yr | Owner: ___
- [ ] **Sales tax nexus** (collected correctly in all states/countries?)
  - Compliance: __% | Exposure: $__ | Owner: ___
- [ ] **Employee withholding** (all 1099s, W-2s filed correctly)
  - Compliance: Y/N | Accruals: $__ | Owner: ___
- [ ] **International operations** (if EU/APAC, local tax filings?)
  - Entities: __ | Compliance: Y/N | Owner: ___
- [ ] **Transfer pricing** (if inter-company transactions, arms-length price?)
  - Documentation: Y/N | Owner: ___
- [ ] **Export controls** (ITAR, EAR if tech product)
  - Exposed: Y/N | Risk: __ | Owner: ___
- [ ] **AML/KYC** (if fintech, customer verification)
  - Compliance: Y/N | Owner: ___
- [ ] **Sanctions screening** (if cross-border, OFAC checks)
  - Screening: Y/N | Owner: ___
- [ ] **Cannabis/alcohol** (if applicable, state-level compliance)
  - Status: N/A | Owner: ___
- [ ] **Environmental permits** (if manufacturing, waste management)
  - Status: N/A | Owner: ___
- [ ] **Cyber insurance** (coverage, claims history, renewal terms)
  - Coverage: $__ | Claims: __ | Owner: ___
- [ ] **Directors & officers insurance** (D&O, tail coverage post-close)
  - Coverage: $__ | Tail terms: __ | Owner: ___
- [ ] **Product liability** (if physical product, insurance adequacy)
  - Coverage: $__ | Claims: __ | Owner: ___
- [ ] **Recall history** (product defects, customer impacts)
  - Recalls: __ | Impact: __ | Owner: ___
- [ ] **ESG compliance** (if large acquirer, environmental/social governance)
  - Status: __ | Gaps: __ | Owner: ___

**Compliance Score: `__/15` × (100/15) = ___%**

---

## 7. Integration Risk Dashboard

| Risk Area | Score (0-10) | Mitigation | Owner |
|-----------|---|-----------|-------|
| **Tech integration** | __ | Keep teams separate 6mo, API-first | CTO |
| **Sales/customer retention** | __ | Lock key customers in SPA, CEO on board | BD |
| **Engineering talent loss** | __ | Retention bonuses 18mo earnout, keep autonomy | HR |
| **Culture clash** | __ | Town halls, transparency on acquirer plans | CEO |
| **Regulatory/compliance** | __ | Legal counsel on integration task force | Legal |

**Overall Integration Risk = Avg of above = __/10 (target <6)**

---

## 8. Decision Matrix: Go/No-Go

| Metric | Target | Actual | Gap | Status |
|--------|--------|--------|-----|--------|
| Financial DD Completeness | 95% | __% | __ | 🔴 |
| Technical DD Completeness | 90% | __% | __ | 🔴 |
| Legal DD Completeness | 95% | __% | __ | 🔴 |
| Commercial DD Completeness | 85% | __% | __ | 🔴 |
| Red flags (critical issues) | 0 | __ | __ | 🟡 |
| Acquirer interest (score 1-10) | 8+ | __ | __ | 🟡 |
| Deal economics alignment | 95% | __% | __ | 🔴 |

**GO/NO-GO Decision:**
- [ ] **GO:** All greens + ≤1 yellow
- [ ] **CONDITIONAL GO:** 1-2 reds, but fixable by D45
- [ ] **HOLD:** 3+ reds, needs escalation
- [ ] **NO-GO:** Critical issues found, walk

---

## Update Cadence

- **Weekly** (D14-D60): Update tab by Wed, discuss Fri
- **Bi-weekly** (D60+): Escalate reds to CEO, discuss board-level risk
- **Pre-LOI (D50-D60):** Daily updates, owner accountability
- **Pre-SPA (D80-D95):** Daily, all reds must be resolved or mitigated
## Related
