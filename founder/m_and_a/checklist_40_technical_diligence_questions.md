---
name: checklist-40-technical-diligence
description: 40 critical technical due diligence questions for M&A buyers evaluating tech assets
metadata:
  type: checklist
  phase: diligence
  audience: buyer
---

# 40 TECHNICAL DUE DILIGENCE QUESTIONS

**For buyer's CTO/VP Eng to assess technical risk, scalability, debt, and moat.**

---

## SECTION A: ARCHITECTURE & SCALABILITY (1–8)

- [ ] What is the current system architecture? Monolith, microservices, hybrid?
- [ ] What is the primary tech stack (languages, frameworks, databases)?
- [ ] How many lines of code in the main product? What's the code distribution (backend %, frontend %, infrastructure %)?
- [ ] What's the current system capacity? Daily active users, transactions/sec, data volume (GB/TB)?
- [ ] Has the system been stress-tested? What's the breaking point (TPS, concurrent users)?
- [ ] What's the cloud infrastructure (AWS, GCP, Azure, on-premise)? Monthly cloud spend?
- [ ] What's the database strategy (primary DB, replication, sharding, caching layers)?
- [ ] Can the system scale to 10x, 100x current capacity? What's the roadmap?

---

## SECTION B: CODE QUALITY & DEBT (9–16)

- [ ] What's the test coverage (unit, integration, end-to-end)? Target: >70%.
- [ ] Are there automated testing pipelines? CI/CD setup (Jenkins, GitHub Actions, GitLab)?
- [ ] What's the code quality (static analysis, linting, code reviews)? Any critical issues?
- [ ] What's the technical debt backlog? Estimate: hours to pay down?
- [ ] Are there any legacy components that should be rewritten?
- [ ] What's the deployment frequency? Can you deploy multiple times/day?
- [ ] What's the rollback capability? Can you revert a bad deployment in <5 min?
- [ ] What's the error rate in production? Tracking via Sentry, DataDog, New Relic, etc.?

---

## SECTION C: SECURITY (17–24)

- [ ] Has the product undergone a security audit? By whom, when, and findings?
- [ ] What's the data encryption strategy (at-rest, in-transit)? TLS 1.2+?
- [ ] How is customer data isolated (multi-tenancy)? Any shared databases/caches?
- [ ] What's the access control model (RBAC, ABAC, SAML/SSO)?
- [ ] Are there any known vulnerabilities or CVEs? How are they tracked/patched?
- [ ] What's the incident response process? Any past breaches?
- [ ] Is there a bug bounty program? Any vulnerabilities reported?
- [ ] What compliance certifications exist (SOC2, ISO 27001, GDPR, HIPAA)?

---

## SECTION D: PERFORMANCE & RELIABILITY (25–30)

- [ ] What's the uptime SLA? What's actual uptime (last 12 months)? Any major outages?
- [ ] What's the average API response time? P95 and P99 latency?
- [ ] What's the database query performance? Any slow queries?
- [ ] What's the CDN/caching strategy? Is it effective?
- [ ] What's the disaster recovery plan? RTO and RPO?
- [ ] Are backups automated? How often tested (restoration drills)?

---

## SECTION E: INFRASTRUCTURE & OPERATIONS (31–35)

- [ ] What's the infrastructure-as-code setup (Terraform, CloudFormation)?
- [ ] What's the monitoring/alerting stack (Datadog, New Relic, CloudWatch)?
- [ ] What's the logging strategy (centralized logs, retention, searchability)?
- [ ] What's the on-call process? Runbooks available?
- [ ] What's the cost structure (per customer, per feature, per resource)? Can you model economics?

---

## SECTION F: INTELLECTUAL PROPERTY & THIRD-PARTY DEPENDENCIES (36–40)

- [ ] What's the open-source software inventory? Any GPL, AGPL, or restrictive licenses?
- [ ] What are the critical third-party dependencies (libraries, APIs, services)?
- [ ] Are there any vendor lock-ins (AWS, Twilio, Stripe, etc.)?
- [ ] What's the API/integration landscape (who relies on your APIs)?
- [ ] Are there any patent claims or IP disputes?

---

## DEEP DIVES — PROBE FURTHER ON:

**Architecture:**
- Is the architecture suitable for acquisition integration (can you combine codebases)?
- Can Buyer's engineers take ownership without domain knowledge?
- What's the learning curve for new engineers?

**Scalability:**
- What's the current bottleneck (database, API, compute)?
- Is there a scaling roadmap or is it ad-hoc?
- Can you scale horizontally (stateless) or are there stateful bottlenecks?

**Debt:**
- What would it cost to fix the worst technical debt?
- Is there "hidden" debt (undocumented systems, scripts in production)?
- How long would a rewrite take vs. incremental improvement?

**Performance:**
- Are performance issues blocking customer adoption?
- Is there a performance roadmap?
- What's the cost of latency/downtime to customers?

**Security:**
- Is there a security roadmap or incident response plan?
- What % of revenue goes to security (SIEM, pen testing, etc.)?
- Are there compliance mandates (HIPAA, PCI-DSS)?

---

## RED FLAGS — ESCALATE TO ADVISOR IF YOU SEE:

🚩 **Architecture red flags:**
- Monolith with >500k lines of code; high coupling
- No API versioning; customers tightly coupled to internal APIs
- Database schema too complex to document (>100 tables with unclear relationships)
- Scaling requires manual intervention (not automated)

🚩 **Code quality red flags:**
- Test coverage <30%; no automated testing
- CI/CD failures common; merges frequently break production
- Code reviews not enforced; no PR standards
- Multiple critical issues in static analysis

🚩 **Technical debt red flags:**
- Team estimates >6 months to pay down major debt
- Debt is actively blocking feature velocity
- No plan to address debt; "we'll fix it later" attitude
- Use of unsupported/EOL technologies (Python 2, Java 8)

🚩 **Security red flags:**
- No encryption for customer data (at-rest or in-transit)
- Multi-tenant data not properly isolated
- No SOC2 certification (especially for enterprise SaaS)
- Past security incidents without clear remediation
- No vulnerability disclosure process

🚩 **Reliability red flags:**
- Uptime <99%; multiple outages in past year
- No automated backups or RTO/RPO undefined
- On-call coverage incomplete or manual runbooks missing
- Database failures result in data loss (not just downtime)

🚩 **Dependencies red flags:**
- Critical vendor lock-in (custom Stripe integration, proprietary AWS features)
- GPL/AGPL open-source used in proprietary product (license violation)
- Undisclosed dependencies on external services (if they go down, so do you)
- No version pinning; updates break production

---

## TECHNICAL DUE DILIGENCE PROCESS

**Phase 1 — Desk Review (Buyer's engineering, 4–6 hours):**
1. Review architecture diagrams and system documentation
2. Analyze repository stats (code volume, commit history, contributors)
3. Review recent security audits, penetration test results
4. Check infrastructure costs (AWS bills, cloud console)

**Phase 2 — Technical Interview (Seller's CTO, 2–4 hours):**
1. Walk through architecture and key systems
2. Discuss technical debt, roadmap, and team capability
3. Ask about past outages, incidents, and lessons learned
4. Assess team depth (can they explain internals?)

**Phase 3 — Code & Infrastructure Review (Seller's CTO + Buyer's team, 4–8 hours):**
1. Clone repository; review code quality, tests, documentation
2. Access production infrastructure; review logs, monitoring, scaling
3. Ask for specific examples: "Show me how a feature ships" / "Walk me through a recent incident"
4. Test deployment and rollback processes

**Phase 4 — Security Deep Dive (3rd party if needed, 4–8 hours):**
1. Review encryption implementation
2. Test authentication and authorization
3. Verify compliance controls (if SOC2/HIPAA claimed)
4. Pen test critical functionality (with seller's permission)

---

## DOCUMENT CHECKLIST — REQUEST THESE:

- [ ] Architecture diagrams (system, data flow, deployment)
- [ ] Technology stack inventory (libraries, frameworks, databases, tools)
- [ ] Git repository access (read-only; review commit history, code structure)
- [ ] Infrastructure documentation (cloud setup, scaling, networking)
- [ ] Security audit reports (3rd party pentests, code reviews)
- [ ] Incident reports (past 2 years; outages, security incidents, resolution)
- [ ] Database schema documentation
- [ ] API documentation (rate limits, deprecations, support)
- [ ] Third-party dependency list (with license types)
- [ ] Performance metrics (APM dashboards, uptime stats, SLA reporting)
- [ ] Runbooks / on-call documentation
- [ ] Monitoring & alerting configuration (exported from DataDog, etc.)
- [ ] Deployment pipeline configuration (CI/CD scripts)
- [ ] Test coverage reports / test infrastructure documentation
- [ ] Open-source license compliance report
