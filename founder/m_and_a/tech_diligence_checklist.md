---
name: tech_diligence_checklist
description: Tech due diligence checklist — ce qu'un acheteur cherche vraiment dans le code/infra
metadata:
  type: checklist
  created: 2026-06-12
---

# Tech Diligence Checklist — What Buyers Actually Care About

**Goal:** Identify tech risks BEFORE buyer discovers them; prepare defensible answers.

---

## Core Concerns (Ranked by Impact)

### 1. **Scalability & Infrastructure** (40% of tech risk)

**Buyer questions:**
- How much traffic/scale can your infrastructure handle?
- What's your current usage headroom?
- Have you hit capacity limits before?

**Your prep:**
- [ ] Load test results (last 6 months)
- [ ] Peak traffic metrics (concurrent users, requests/sec)
- [ ] Infrastructure diagram (AWS regions, CDN, databases)
- [ ] Capacity forecast (when will we hit limits?)
- [ ] Scaling history (how did you scale from $1M to $3M ARR?)

**Red flag:** "We've never stress-tested" → Buyer will assume it breaks under 2x load.

---

### 2. **Code Quality & Maintenance** (25% of tech risk)

**Buyer questions:**
- How maintainable is this codebase?
- Will we need to rewrite it in 2 years?

**Your prep:**
- [ ] Code organization (clear structure? Modules? Monolith?)
- [ ] Test coverage (unit / integration / E2E %)
- [ ] Documentation (README, architecture, deployment?)
- [ ] Tech debt inventory ("Here's what needs attention")
- [ ] Code review process (PRs? Standards?)

**Red flag:** <50% test coverage → Buyer fears refactoring costs.

---

### 3. **Dependency Hygiene** (15% of tech risk)

**Buyer questions:**
- Are you using libraries that are EOL or risky?
- How many dependencies do you have? Are they maintained?

**Your prep:**
- [ ] Dependency audit (tool: `npm audit`, `pip audit`, `cargo audit`)
- [ ] Critical dependencies (list libraries with EOL dates)
- [ ] License compliance (no GPL in proprietary code?)
- [ ] Patch cadence (how often do you update libs?)

**Red flag:** 50+ unpatched vulnerabilities → Immediate security remediation required.

---

### 4. **Security & Compliance** (12% of tech risk)

**Buyer questions:**
- Have you been hacked?
- Do you comply with SOC2 / GDPR / HIPAA?

**Your prep:**
- [ ] Security audit results (recent, 3rdparty preferred)
- [ ] Incident history (breaches, vulnerabilities, response)
- [ ] Compliance certs (SOC2, ISO 27001, etc.)
- [ ] Data handling (encryption, access controls, logs)
- [ ] GDPR / CCPA readiness (data deletion, consent, DPO?)

**Red flag:** No third-party security audit → Buyer budgets $50k for one.

---

### 5. **Performance & Reliability** (8% of tech risk)

**Buyer questions:**
- What's your uptime?
- How fast is your product?
- Can you handle a 10x traffic spike?

**Your prep:**
- [ ] Uptime data (last 24 months, %)
- [ ] Incident response plan (page oncall? SLA? MTTR?)
- [ ] Performance benchmarks (API latency, page load time)
- [ ] Disaster recovery / backup strategy (RTO, RPO)
- [ ] Monitoring setup (what are you tracking?)

**Red flag:** <99.5% uptime → Buyer factor in reliability costs.

---

## File Structure You Should Prepare

```
/Technical_Audit/
├─ Architecture.md (1-pager with diagram)
├─ Infrastructure.md (AWS setup, scaling limits, capacity)
├─ Deployment.md (CI/CD pipeline, release process)
├─ Security_Audit_Report.pdf (3rdparty, recent)
├─ Dependencies.json (all libraries + versions + licenses)
├─ Test_Coverage_Report.txt (unit %, integration %, E2E %)
├─ Uptime_Dashboard_Screenshot.png (last 90 days)
├─ Performance_Metrics.xlsx (API latency, page load, throughput)
├─ Code_Quality_Assessment.md (tech debt inventory + timeline)
├─ Incidents_Log.md (security / outages, response, resolution)
└─ Disaster_Recovery_Plan.md (RTO/RPO, backup frequency)
```

---

## Critical Questions (Prepare Answers)

| Question | Good Answer | Bad Answer |
|----------|-------------|-----------|
| "What's your tech stack?" | "Node.js/React + PostgreSQL + AWS. [Rationale for each choice]" | "Whatever was trendy when we built it" |
| "Have you stress-tested?" | "Yes; handles 10x current load before hitting limits" | "Not really; it seems fine" |
| "What's your test coverage?" | "75% unit, 60% integration, 40% E2E" | "We test manually" |
| "Any security incidents?" | "One in [YEAR]; [swift remediation + mitigation]" | "None that we know of" |
| "How do you monitor?" | "[Datadog/New Relic]; alerts for [specific metrics]" | "We check logs manually" |
| "What's your biggest tech debt?" | "[Specific]: [Timeline to fix]" | "Not much; codebase is clean" |

---

## Assessment Scorecard for Buyer

Use this to grade your own tech risk:

| Area | Status | Impact | Fix Timeline |
|------|--------|--------|--------------|
| Scalability | ✅ Good / ⚠️ OK / 🔴 Risky | [%] of deal value | [Months] |
| Code quality | ✅ Good / ⚠️ OK / 🔴 Risky | [%] of deal value | [Months] |
| Dependencies | ✅ Good / ⚠️ OK / 🔴 Risky | [%] of deal value | [Months] |
| Security | ✅ Good / ⚠️ OK / 🔴 Risky | [%] of deal value | [Months] |
| Performance | ✅ Good / ⚠️ OK / 🔴 Risky | [%] of deal value | [Months] |
| **Total Risk** | | **~X% deal value discount** | |

**If total risk = $1M discount, adjust asking price down by $1M OR plan to fix before sale.**

---

## Pre-Sale Tech Checklist (60 days out)

- [ ] Run security audit (third-party if possible)
- [ ] Patch all critical vulnerabilities
- [ ] Achieve >70% test coverage (unit + integration)
- [ ] Update dependencies to latest stable
- [ ] Document architecture (1-pager with diagram)
- [ ] Document deployment process (README for buyer)
- [ ] Run load test; document capacity headroom
- [ ] Verify uptime (recent 6 months)
- [ ] Log all incidents from last 12 months + remediation
- [ ] Create disaster recovery runbook
- [ ] Get code review from external CTO/advisor (catch blind spots)

**Timeline:** If multiple issues, start 6 months before sale.

---

## Red Flags You'll Be Asked About

🚩 **Monolithic codebase** → Buyer assumes hard to modify
🚩 **Custom infra** (not AWS/GCP) → Buyer worries about migration
🚩 **Founder-written code** → Buyer questions maintainability
🚩 **No monitoring** → Buyer budgets for observability platform
🚩 **Manual deployment** → Buyer plans to automate
🚩 **High incident rate** → Buyer negotiates reliability SLA
🚩 **Outdated dependencies** → Buyer fears security risks

**For each:** Provide mitigation plan (hiring CTO, modernizing stack, etc.)

---

## Buyer's Tech Assessment Duration

- **Quick scan:** 2 weeks (access code, run tests, architecture review)
- **Deep dive:** 4-6 weeks (security audit, load testing, code review)
- **Complex deal:** 8-12 weeks (if you need significant modernization)

**Timeline:** Assume 6 weeks; plan data room access accordingly.
## Related
## Related
