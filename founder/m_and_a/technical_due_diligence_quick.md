---
title: Technical Due Diligence (Code, Infra, Security) + Data Room
created: 2026-06-12
category: diligence
status: active
---

# Technical Due Diligence + Data Room Checklist

---

## A. Code Quality assessment (1-2 days)

### Checklist

- [ ] Repository cloned, architecture scanned
- [ ] Languages & framework versions noted
- [ ] Test coverage measured (aim >70%)
- [ ] Code scan tool run (SonarQube, CodeClimate)
- [ ] Dependency audit (npm audit, pip audit, cargo audit)
- [ ] Open source licenses scanned (no AGPL surprises)
- [ ] Security scan (SAST = static analysis for vulns)
- [ ] Tech debt estimated (story points for modernization)

### Red flags

🚩 No tests (manual QA only) = high risk
🚩 Framework EOL (Rails 4, Django 1.x, old Node)
🚩 Huge codebase (>500k LOC, hard to maintain)
🚩 Spaghetti monolith (no clear architecture)
🚩 Open CVEs in dependencies (unpatched vulnerabilities)

---

## B. Infrastructure assessment (1-2 days)

### Questions to answer

```
Hosting:
- Cloud provider: AWS / GCP / Azure / hybrid?
- Regions: US-only? EU for GDPR? Multi-region failover?
- Current monthly bill: $___k?

Compute:
- Containerized? (Docker, Kubernetes?)
- Auto-scaling? (can handle 5x peak?)
- Monitoring (Datadog, New Relic, custom)?

Database:
- Type: PostgreSQL / MySQL / MongoDB?
- Size: ___ GB? Growing _% per month?
- Replication: primary-replica? Multi-region?
- Backups: daily? Off-site? Recovery tested?
- Performance: any slow queries logged?

Load testing:
- Tested @ what multiplier? (2x? 5x? 10x peak?)
- Results: latency p99? Error rate?
- Scaling strategy: add more servers? Caching? CDN?
```

### Green lights

✅ Cloud-native (AWS/GCP)
✅ Containerized (Docker/K8s)
✅ Auto-scaling configured
✅ Multi-region backup
✅ Load tested to 5x+
✅ <100ms p99 latency

---

## C. Security & Compliance (2-3 days)

### Critical checklist

- [ ] Security audit done in last 12 months? (external preferred)
- [ ] Pen test results (any critical vulns?)
- [ ] SOC2 Type II? (Audit in progress? Target date?)
- [ ] GDPR Data Processing Agreement (if EU customers)
- [ ] Data encryption (TLS 1.3 in transit, AES-256 at rest)
- [ ] IAM (AWS/Okta)? MFA enabled on all admin accounts?
- [ ] Vulnerability scanning tool running (Snyk, FOSSA)
- [ ] Incident response plan documented

### Known CVEs check

```bash
# Run on codebase
npm audit
pip audit
cargo audit
# Check for high/critical unpatched
```

Red flags:
- 🚩 Unpatched critical CVEs
- 🚩 No encryption at rest (customer data in plaintext!)
- 🚩 No MFA on production access
- 🚩 No incident response plan

---

## D. Operations & Monitoring

### Checklist

- [ ] Logging system (ELK, Datadog, Splunk)
- [ ] Metrics dashboard (CPU, memory, latency, errors)
- [ ] Alerting configured (automatic pages on issues)
- [ ] On-call rotation (who covers nights/weekends?)
- [ ] Runbooks for common operations
- [ ] Disaster recovery: RPO/RTO defined
- [ ] Last backup recovery test (when?)
- [ ] SLA uptime target (99%? 99.5%? 99.9%?)

### Red flags

🚩 No monitoring (flying blind)
🚩 No alerting (manual watching of dashboards)
🚩 DR never tested (can't actually restore)
🚩 No runbooks (tribal knowledge, person-dependent)

---

## E. Data room folder structure (100+ docs)

### /01_EXECUTIVE

```
- Company_Overview_1pager.pdf
- Executive_Summary_2pager.md
- Pitch_Deck_Final.pdf
- Organization Chart (with bios)
- Key_Metrics_Dashboard.xlsx
```

### /02_FINANCIALS

```
- P&L_12months_monthly.xlsx
- Balance_Sheet_latest.xlsx
- Cashflow_3years.xlsx
- Cap_Table_fully_diluted.xlsx
- Customer_LTV_Cohort_Analysis.xlsx
- Revenue_Breakdown_recurring_vs_oneoff.xlsx
- Audit_Report (if available) / Accountant_Review
```

### /03_LEGAL

```
- Articles_of_Incorporation.pdf
- Bylaws.pdf
- Board_Minutes_last_12months/
  - 2024_Q1_minutes.pdf
  - 2024_Q2_minutes.pdf
  - ... etc
- Cap_Table_original_docs/
  - Equity_grants_agreements.pdf
  - Equity_option_grants.pdf
- IP_Assignment_Agreements/
  - Founder_IP_assignment.pdf
  - Employee_IP_assignment.pdf
- Patents_and_Trademarks.pdf
```

### /04_COMMERCIAL

```
- Customer_List_Master.xlsx
  (Columns: Name, ARR, Churn Date, Contract End, NPS Score)
- Top_10_Customers_contracts.pdf (redacted)
- Standard_Customer_Contract_Template.pdf
- Case_Studies_3-5_major_customers.pdf
- Competitive_Analysis.pdf
- Market_Research_TAM_SAM_SOM.pdf
- Press_Coverage_media_kit.pdf
- NPS_Survey_Results_latest.xlsx
```

### /05_TECHNICAL

```
- Architecture_Overview_diagram.pdf
- Tech_Stack_Inventory.pdf (languages, frameworks, versions)
- API_Documentation_Swagger.pdf
- Database_Schema.pdf
- Infrastructure_Diagram.pdf
- Security_Audit_Report.pdf (external audit, if done)
- Penetration_Test_Results.pdf
- Roadmap_Next_12_months.pdf
- Code_Repository_Access (GitHub/GitLab link with read-only access)
```

### /06_HR

```
- Organization_Chart_detailed.pdf
- Executive_Team_bios.pdf
- Key_Employee_Retention_Agreements.pdf
- Equity_Option_Plan_Docs.pdf
- Employee_Handbook.pdf
- Compensation_Summary.xlsx (salary bands, not individual salaries)
- Headcount_Growth_Plan.xlsx
```

### /07_CUSTOMER_SUPPORT

```
- Support_Ticket_Volume_trends.xlsx
- NPS_Survey_historical.xlsx
- Customer_Satisfaction_scores.xlsx
- Customer_Churn_Analysis.xlsx (why customers leave)
- Feature_Request_Top_10.xlsx
```

### /08_CONTRACTS

```
- Customer_Agreements_representative_sample/ (redacted)
- Vendor_Contracts_key_ones/
  - AWS_contract.pdf
  - Stripe_agreement.pdf
- Service_Level_Agreements_SLAs.pdf
- Non-disclosure_agreements.pdf
```

---

## F. Data room access & security

### Setup

- Use Intralinks / Firmex / VirtualDataRoom.com
- Two-factor authentication required
- Watermark on all PDFs (shows who downloaded what)
- Download limitations (if sensitive) or unrestricted
- Visitor log (see who accessed what, when)

### Batches of access

```
Tier 1 (Initial): Teaser + NDA + 1-pager
Tier 2 (Post-LOI): Full P&L, cap table, customer list, tech overview
Tier 3 (Diligence): Code access, detailed contracts, security audit
Tier 4 (Final): HR details, executive employment terms, sensitive IP
```

---

## G. What NOT to include in data room

❌ Personal information (employee SSNs, credit cards)
❌ Passwords, API keys, credentials
❌ Pending litigation details (attorney-client privilege issues)
❌ Unredacted salaries (just salary bands)
❌ Sensitive customer data (redact customer names if needed)
❌ Third-party NDAs that forbid sharing

---

## H. Red flags from tech diligence

| Finding | Severity | Mitigation |
|---------|----------|------------|
| No tests | 🔴 High | Can add tests pre-deal, but risky |
| Tech debt >25% | 🟠 Medium | Make clear plan, timeline |
| Open CVEs | 🔴 High | Patch before sale (deal-breaker) |
| No monitoring | 🟠 Medium | Implement immediately |
| Key person dependency | 🔴 High | Get retention agreement |
| Outdated framework | 🟡 Low-med | Modernization roadmap |
| Single point of failure | 🔴 High | Add redundancy before deal |

---

## I. Fast technical audit (4-8 hours)

If you're evaluating to BUY:

```
Hour 1: Clone repo, check structure (languages, size)
Hour 2: Run tests, code scans (SonarQube)
Hour 3: Architecture review (monolith? Microservices?)
Hour 4: Infrastructure review (cloud, scaling, monitoring)
Hour 5: Security audit (CVEs, encryption, IAM)
Hour 6: Ask CTO walkthrough questions
Hour 7: Load test results review
Hour 8: Write report (red flags, summary, go/no-go)
```

Output: 1-2 page technical assessment.

---

## Summary: Tech due diligence scorecard

| Category | Green | Yellow | Red |
|----------|-------|--------|-----|
| **Code quality** | >70% tests | 50-70% tests | <50% tests |
| **Framework** | Current | 1-2 versions old | EOL |
| **Infra** | Cloud-native + scaling | Cloud, no scaling | On-prem, brittle |
| **Security** | Audit clean | Minor findings | Critical CVEs |
| **Monitoring** | Full stack | Partial | None |
| **Operations** | Runbooks, on-call | Informal | Person-dependent |

All green = buy. 1-2 yellows = manageable. Any reds = escalate.
