---
name: tech-diligence-quickwin
description: 90-min audit : ce que buyer découvrira, et comment se préparer
metadata:
  type: decision
---

# TECH DILIGENCE — 90 MIN QUICKWIN

**Utilité:** Faire toi-même l'audit technique que buyer fera, en 90 minutes. Identifier les "deal-killers" avant soft shop. Preparer réponses honnêtes.

**Format:** Checklist + audit + résumé 1-page pour data room.

---

## SECTION 1 : CODEBASE HEALTH (30 min)

### 1.1 Code Ownership & IP
- [ ] All code is in company repo (no "founder's personal GitHub").
- [ ] No open-source copyleft (GPL) in production code without proper handling.
- [ ] All contributors have assignment agreements (ICs + contractors assign IP to company).
- [ ] No "key person" code that only one engineer understands.

**If FALSE:** Document why + remediation plan (e.g., "We reassigned X's code in Q2").

---

### 1.2 Architecture & Dependencies
- [ ] System architecture is documented (README, diagrams, or ADRs). Not "only in founder's head."
- [ ] <3 critical external dependencies (SaaS, APIs). Avoid single points of failure.
- [ ] No "custom ORM" or "hand-rolled crypto." Use standard libraries.
- [ ] Database schema is reasonable (no 5-year-old technical debt, can be maintained).

**If FALSE:** List top 3 architecture risks + timeline to fix.

---

### 1.3 Testing & Code Quality
- [ ] Unit test coverage >40%. (Not 100%, but non-zero.)
- [ ] Integration tests for critical paths (payment, auth, data export).
- [ ] No "commented-out dead code" > 50 lines. Clean repo.
- [ ] Linting / code style is automated (no manual review friction).

**If FALSE:** Explain coverage gaps + owner commitment to improve.

---

### 1.4 Deployment & DevOps
- [ ] Deployments are automated (CI/CD pipeline, not manual button-push).
- [ ] Staging environment matches production (not local-only testing).
- [ ] Rollback is automated or <2 min manual (no "call DevOps at 2am" story).
- [ ] Logs are centralized (not scattered across servers).

**If FALSE:** Document manual steps + timeline to automate.

---

## SECTION 2 : SECURITY & COMPLIANCE (30 min)

### 2.1 Data Security
- [ ] Customer data is encrypted at rest (TLS for transit, not optional).
- [ ] No plaintext passwords in code or DB.
- [ ] No API keys, secrets in git history (even old commits). If exists, keys rotated.
- [ ] HTTPS is enforced (no http://customer data).

**If FALSE:** Rotate keys immediately + document remediation.

---

### 2.2 Access Control
- [ ] Production access is role-based (not "everyone has admin").
- [ ] Admin accounts are <3 people.
- [ ] No shared passwords (everyone has own login).
- [ ] VPN or IP whitelist for prod access (not public internet).

**If FALSE:** Lock down access now.

---

### 2.3 Compliance (if relevant)
- [ ] GDPR: Can you delete customer data on request? Code audit = necessary.
- [ ] CCPA: Can you export customer data? Audit needed.
- [ ] SOC 2: If customer asks, can you share report? (Even if not certified, audit framework is good.)
- [ ] HIPAA/PCI: If not applicable, skip. If yes, ensure buyer inherits compliance.

**If FALSE:** Flag as "we handle [data type], buyer must certify post-close."

---

### 2.4 Incident Response
- [ ] You've had 0 major security incidents in last 2 years. (If >1, document root causes + fixes.)
- [ ] You have a process for handling security reports (bug bounty or responsible disclosure).
- [ ] No pending CVEs (check dependencies + known vulnerabilities).

**If FALSE:** Document incident + remediation proof.

---

## SECTION 3 : SCALABILITY & PERFORMANCE (20 min)

### 3.1 Database & Storage
- [ ] Database queries are indexed (no full-table scans on high-frequency queries).
- [ ] Database size <500 GB (if >500 GB, document strategy for migration).
- [ ] No hard-coded limits (e.g., "max 1000 customers" baked in).

**If FALSE:** Document scaling strategy + timeline.

---

### 3.2 Infrastructure
- [ ] You use managed services (AWS, GCP, Heroku, etc.), not self-hosted servers.
- [ ] Auto-scaling is configured (if traffic spikes, service scales automatically).
- [ ] No single server dependency (multi-AZ, load balanced).

**If FALSE:** Explain why self-hosted + buyer's migration plan.

---

### 3.3 Performance Monitoring
- [ ] You have dashboards (Datadog, New Relic, CloudWatch) for uptime + latency.
- [ ] P99 latency <1s for typical requests. (If slower, document why.)
- [ ] Uptime >99.5% in last 12 months. (If <99.5%, explain reasons.)

**If FALSE:** Document issues + root causes.

---

## SECTION 4 : TECHNICAL DEBT & KNOWN ISSUES (10 min)

### 4.1 List Top 5 Technical Debts
1. _____________________________ (timeline to fix: ___ months)
2. _____________________________ (timeline to fix: ___ months)
3. _____________________________ (timeline to fix: ___ months)
4. _____________________________ (timeline to fix: ___ months)
5. _____________________________ (timeline to fix: ___ months)

**Scoring:**
- If all 5 are <3 months to fix: LOW RISK
- If 2-3 are 3-6 months: MEDIUM RISK
- If 1+ are >6 months or "unfixable": HIGH RISK

---

### 4.2 Product Limitations (Known Unknowns)
- Does product scale to X customers? (If no, document limit + why.)
- Does product work in [region]? (Compliance, latency, language?)
- Does product integrate with [popular tool]? (If not, customer ask = integrations team?)

---

## SECTION 5 : TEAM & DOCUMENTATION (10 min)

### 5.1 Knowledge Distribution
- [ ] >1 engineer can deploy code (not bottleneck).
- [ ] >1 engineer understands architecture (not key-person risk).
- [ ] Runbooks exist for common ops tasks (e.g., "how to rotate DB credentials").
- [ ] Onboarding takes <1 week for mid-level engineer (not 3 months).

**If FALSE:** Document knowledge gaps + owner.

---

### 5.2 Documentation
- [ ] README explains how to run code locally (setup is <30 min).
- [ ] Architecture decision records (ADRs) explain why tech choices were made.
- [ ] API docs exist (even if rough).
- [ ] Database schema is documented (not inferred from code).

**If FALSE:** Invest 2-3 days in docs.

---

## YOUR AUDIT SUMMARY (1-page)

```markdown
# Technical Due Diligence Summary

## Overall Assessment
Risk Level: [ ] LOW  [ ] MEDIUM  [ ] HIGH

## Key Findings

### Strengths
- (List 2-3 positive findings)

### Concerns
- (List 2-3 material concerns)

### Remediation Plan
- (Timeline to fix each concern)

## Deal-Killer Risks (if any)
- [ ] Critical security issue
- [ ] Unmitigable scalability issue
- [ ] IP ownership unclear
- [ ] No documentation for key systems
- [ ] Customer concentration on 1 tech vendor

## Buyer FAQ Prep
**Q: How is the code organized?**  
A: [Your answer]

**Q: What's the biggest technical debt?**  
A: [Your honest answer + remediation timeline]

**Q: Can the system scale to 100k users?**  
A: [Yes / No / Depends on: ...]

**Q: What happens if [key engineer] leaves?**  
A: [Succession plan / Risk / Timeline to mitigate]

## Recommendation
[ ] Ready for buyer audit (address minor issues post-LOI)
[ ] Fix X before soft shop (will discovery-fail otherwise)
[ ] Hold & improve before soft shop (too many red flags)
```

---

## QUICK CHECKLIST

- [ ] Spent 90 minutes on this audit
- [ ] Identified top 3 tech risks
- [ ] Have honest answers to "what's the biggest technical debt?"
- [ ] Documented known limitations (not hiding them)
- [ ] Have remediation timeline for critical issues
- [ ] Ready to show code to buyer without shame

**Date audited:** __________  
**Auditor:** __________  
**Overall risk level:** __________
## Related

- [[_system/MOC-decisions]]
- [[brantham/_MOC]]