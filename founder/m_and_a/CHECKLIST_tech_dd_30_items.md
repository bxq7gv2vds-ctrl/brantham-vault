---
name: checklist-tech-dd-30-items
description: 30-item checklist — Répondre aux questions tech due diligence du buyer
metadata:
  type: checklist
  created: 2026-06-13
---

# Tech Due Diligence — 30-Item Checklist

Buyers will ask about your technology. Use this checklist to prepare answers (and spot your own red flags early).

## Before Meeting the Buyer's Tech Team

- [ ] Map your **system architecture** (boxes + arrows, no code exposure)
- [ ] List all **third-party dependencies** (APIs, libraries, services)
- [ ] Document your **deployment/DevOps process** (how code gets to production)
- [ ] Audit your **security posture** (SSL, encryption, access controls, compliance)
- [ ] Assess your **technical debt** (rough estimate: how many months to clean up?)
- [ ] Review **uptime/reliability** (average SLA, worst incidents, MTTR)
- [ ] Inventory your **data** (size, growth rate, backup strategy)
- [ ] Assess **team capability** (can they maintain/scale the system?)

---

## The 30 Questions (Answer Each)

### Architecture & Technology Stack (1–5)

- [ ] **1. System Design:** Describe your overall architecture (monolith, microservices, serverless, etc.). What are the main components?
  - *Red flag:* Spaghetti code, no clear architecture, key knowledge in one person's head

- [ ] **2. Technology Stack:** What languages, databases, frameworks, hosting do you use? Why those choices?
  - *Red flag:* Outdated tech (Python 2, old Rails version), no clear reason for choices

- [ ] **3. Scalability:** How does your system scale? What's your current load? At what point would it break?
  - *Red flag:* Never scaled beyond current load, no load testing, single point of failure

- [ ] **4. Performance:** What are your key latency metrics (API response time, page load, query execution)? How do you monitor?
  - *Red flag:* No monitoring, slow queries, 5+ second page loads for core features

- [ ] **5. Infrastructure:** Where is your code hosted? On-prem, cloud (AWS/GCP/Azure)? How is it deployed?
  - *Red flag:* Manual deployments, shared hosting, no backup infrastructure

---

### Security & Compliance (6–12)

- [ ] **6. Data Encryption:** How do you encrypt data in transit and at rest? What algorithms, key management?
  - *Red flag:* No encryption, home-grown encryption, keys stored in code

- [ ] **7. Authentication & Authorization:** How do users log in? How do you control access (RBAC, OAuth, API tokens)?
  - *Red flag:* Plain-text passwords, weak session management, no role-based access

- [ ] **8. Vulnerability Testing:** Do you run SAST/DAST, penetration testing, dependency scanning? How often?
  - *Red flag:* Never tested for vulnerabilities, no CI/CD security scanning, outdated dependencies

- [ ] **9. Compliance:** Are you SOC 2, ISO 27001, HIPAA, GDPR, PCI-DSS certified? If not, why not?
  - *Red flag:* No certifications, customers asking for them, can't pass audit

- [ ] **10. Incident Response:** Do you have a process for security incidents (breach notification, log retention, forensics)?
  - *Red flag:* No incident plan, slow response times, inadequate logging

- [ ] **11. Customer Data Isolation:** How do you ensure multi-tenant isolation (if applicable)? How do you prevent data leakage?
  - *Red flag:* Shared data, no isolation, cross-customer visibility bugs

- [ ] **12. Access Controls:** Who has access to production? How are credentials managed (secrets, SSH keys)?
  - *Red flag:* Everyone has production access, passwords in shared docs, no audit trail

---

### Operations & Reliability (13–18)

- [ ] **13. Uptime & SLA:** What's your actual uptime %? Do you have an SLA? What's your MTTR for incidents?
  - *Red flag:* <99.5% uptime, no SLA, MTTR >1 hour for critical issues

- [ ] **14. Backups & Disaster Recovery:** How often do you back up? How long to restore? Have you tested?
  - *Red flag:* No backups, manual backups, restore untested, >1 hour RTO

- [ ] **15. Monitoring & Alerting:** What tools do you use (DataDog, New Relic, Prometheus)? What metrics do you track?
  - *Red flag:* Manual monitoring, no alerting, can't spot issues until customers complain

- [ ] **16. Logging:** Do you log all important events? How long do you retain? Can you search by customer/user?
  - *Red flag:* No logging, lost logs after 30 days, can't trace customer issues

- [ ] **17. Database Health:** What's your database size? Growth rate? Any schema migration challenges?
  - *Red flag:* Massive tech debt in schema, slow queries, indexes not optimized, no replication

- [ ] **18. Known Issues / Technical Debt:** What are your biggest technical debt items? How much effort to fix?
  - *Red flag:* Extensive debt (6+ months to fix), key features built on unstable foundations, no plan to fix

---

### Development & Deployment (19–24)

- [ ] **19. Development Process:** Do you use version control (git)? Code review process? CI/CD?
  - *Red flag:* No version control, code review is optional, deployments are manual

- [ ] **20. Testing:** Do you have unit tests, integration tests, end-to-end tests? What's your coverage %?
  - *Red flag:* No tests, tests are flaky, <50% coverage, tests only run manually

- [ ] **21. Deployment Frequency:** How often do you deploy? How long does a typical deployment take?
  - *Red flag:* Quarterly releases, deployments take 4+ hours, high failure rate

- [ ] **22. Rollback Capability:** If a deployment breaks production, how quickly can you roll back?
  - *Red flag:* No rollback plan, manual rollback, >30min RTO

- [ ] **23. Documentation:** Do you have architecture docs, runbooks, API documentation, README?
  - *Red flag:* No documentation, documentation is outdated, key knowledge only in one person's head

- [ ] **24. Branching Strategy:** Do you use feature branches, release branches, hotfix branches? Any strategy?
  - *Red flag:* Everyone commits to main, no release process, chaos during hotfixes

---

### Technical Debt & Maintainability (25–27)

- [ ] **25. Code Quality:** What's your average technical debt ratio (e.g., using SonarQube)? Any major code smells?
  - *Red flag:* High debt (>20%), cyclomatic complexity off the charts, unmaintainable functions

- [ ] **26. Dependencies:** How many external libraries/frameworks do you depend on? How often do you update?
  - *Red flag:* Hundreds of outdated dependencies, critical security patches unpatched for months

- [ ] **27. Scalability Headroom:** If you 10x your customer base overnight, what would break first?
  - *Red flag:* Multiple components would break, no clear upgrade path, architectural rewrite needed

---

### Team & Knowledge (28–30)

- [ ] **28. Team Expertise:** Who are your best engineers? What are they experts in? Key person risk?
  - *Red flag:* One genius holding up the system, others can't understand the code

- [ ] **29. Onboarding New Developers:** How long does it take a new engineer to be productive? Any major bottlenecks?
  - *Red flag:* 6+ months to onboard, no documentation, all context in one person's head

- [ ] **30. Vendor Lock-In:** Are you locked into any vendor tech (AWS, proprietary databases, third-party services)?
  - *Red flag:* Completely dependent on one vendor, migrating would take months

---

## Scoring Your Tech (Rate Yourself Honestly)

| Score | Tech Health | Action |
|---|---|---|
| **27–30 (90–100%)** | EXCELLENT. Few tech risks. Buyer will be happy. | Emphasize modernization, scalability, security in data room. |
| **24–26 (80–90%)** | GOOD. Some tech debt, but manageable. | Acknowledge debt, have a roadmap, emphasize team capability. |
| **20–23 (67–80%)** | FAIR. Meaningful tech debt, some red flags. | Be honest about areas of concern. Offer to pair buyer's eng with your team during DD. |
| **15–19 (50–67%)** | POOR. Major tech debt, reliability concerns. | Prepare detailed debt roadmap, estimate cost to fix, explain why it didn't matter for your customers. |
| **< 15 (< 50%)** | CRITICAL. Buyer may ask for major valuation cuts. | Consider fixing biggest issues before M&A process, or be ready to negotiate price down significantly. |

---

## Red Flags That Kill Deals

| Red Flag | Impact | Mitigation |
|---|---|---|
| **No source code / lost code** | Buyer can't maintain product | [Almost impossible to fix] |
| **Massive scale issues** | Buyer can't integrate your customers | Upgrade infrastructure before sale, show roadmap |
| **No tests, untestable code** | Buyer can't refactor safely | Add basic tests pre-sale, acknowledge debt |
| **Security breaches in history** | Regulatory/compliance risk | Full disclosure, insurance, remediation details |
| **Customer data breaches** | Legal liability | Insurance, disclosure, show improvements |
| **Zero monitoring/logging** | Buyer can't operate product | Implement basic monitoring pre-sale |
| **Unmaintainable / undocumented** | Buyer needs 6+ months to understand | Document key areas, assign eng to explain |

---

## How to Present (During Tech DD Interview)

**Do:**
- Be honest about debt and tradeoffs
- Explain WHY you made certain choices (speed vs scalability, etc.)
- Show you have a roadmap to fix things
- Emphasize team capability (can you improve the system?)
- Demo the product working smoothly (confidence boost)

**Don't:**
- Oversell ("It's enterprise-grade" when it's not)
- Blame external factors (customer growth, lack of funding, etc.)
- Hide red flags (buyer will find them, and it kills trust)
- Get defensive (debt is normal; acknowledge and move on)

---

## Post-Interview Deliverables (For Buyer's Tech Team)

After the tech DD call, provide:

- [ ] System architecture diagram (Lucidchart / Miro, exportable)
- [ ] Technology stack summary (languages, frameworks, databases, hosting, 1-pager)
- [ ] API documentation (OpenAPI / Swagger, if applicable)
- [ ] Infrastructure overview (how it's deployed, scaling strategy)
- [ ] Security assessment (SOC 2 report, penetration test results if available)
- [ ] Technical debt inventory (list of 5–10 biggest items, effort estimate)
- [ ] Team structure (org chart, responsibilities, key experts)
- [ ] Deployment process diagram (code commit → production, step-by-step)
- [ ] Monitoring/alerting overview (what metrics you track, how you alert)
- [ ] Roadmap (next 12 months product + tech improvements)

---

**Pro Tip: Have your CTO/Head of Eng prepare answers for this checklist. This is where the deal gets technical, and you need someone credible presenting (not sales).**
