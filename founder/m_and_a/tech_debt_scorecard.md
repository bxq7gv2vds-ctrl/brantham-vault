---
name: tech-debt-scorecard
description: 10-minute tech audit — what buyer will ask about, pre-empt it
type: audit
---

# Tech Debt Scorecard — 10-Min Audit

**Use** : Before buyer's technical DD. Score your codebase honestly. Surprises = lower offer.

---

## Quick Scoring (Rate each 1-10, 10=excellent)

| Area | Score | Notes |
|------|-------|-------|
| **Code Quality** | [_] | Modern stack? Tests? No legacy code? |
| **Architecture** | [_] | Modular, scalable, cloud-native? Or monolith? |
| **Debt Backlog** | [_] | Cleanness (10=zero known bugs; 1=pile of issues) |
| **Deployment** | [_] | CI/CD automated? Or manual releases? |
| **Monitoring** | [_] | Observability, alerting, dashboards in place? |
| **Security** | [_] | HTTPS, auth, data protection, audit logs? |
| **Performance** | [_] | Fast (P95 <500ms)? Or slow? Optimized? |
| **Scalability** | [_] | Handles 10x traffic? Or needs redesign? |
| **Documentation** | [_] | Onboarding clear? Setup instructions exist? |
| **Team Knowledge** | [_] | Others can maintain code (not vendor-locked to 1 person)? |

**Total Score** : Sum / 100. 
- **80-100** = Excellent (buyer happy, no price discount)
- **60-79** = Good (minor fixes, 5% price reduction)
- **40-59** = Problematic (needs investment, 10-20% reduction)
- **<40** = Risky (may kill deal or 30%+ haircut)

---

## Honest Assessment + Plan to Fix

**For each low score, have a plan:**

```
Code Quality: 6/10 (Legacy Rails 4 codebase, <50% test coverage)
├─ Impact: Buyer will worry about hiring engineers, velocity
├─ Fix plan: 
│   ├─ Week 1-4: Add integration tests for critical paths
│   ├─ Week 5-8: Upgrade Rails 5+ (backward compatible)
│   └─ Timeline: 2 months pre-close (show buyer progress)
└─ Cost: 160 dev hours (@$100/hr = $16K)
```

**Transparency** : Present this to buyer → builds trust → minimizes discount.

---

## Technical DD Checklist (What Buyer Will Ask)

✓ / ✗ / ? :
- [ ] Source code in version control (GitHub/GitLab)?
- [ ] Build/deploy fully automated?
- [ ] All 3rd-party dependencies tracked (no hidden licenses)?
- [ ] Security: HTTPS, encryption, auth working?
- [ ] Performance: <500ms P95 latency?
- [ ] Monitoring: Logs, metrics, alerting set up?
- [ ] Database: Backups tested? Scale plan documented?
- [ ] Code review process in place?
- [ ] Known technical debt documented in roadmap?
- [ ] Key person risk: Can others maintain the code?

**Score** : 8-10 ✓ marks = green light. <6 = negotiate.

---

## Typical Issues & Impact

| Issue | Impact on Price | Fix Timeline |
|-------|-----------------|--------------|
| No tests | -10% | 4-6 weeks |
| Legacy stack (Rails 3, PHP 5) | -15% | 3-6 months |
| Manual deployments | -5% | 1-2 weeks |
| No monitoring/alerting | -8% | 1 week |
| Key person risk (code only person X knows) | -20% | 2-3 months (knowledge transfer) |
| Security issues (weak auth, no encryption) | -25% (or kill deal) | 3-8 weeks |
| Unscalable DB (can't handle 10x) | -15% | 2-3 months (rebuild) |

---

## Pre-Close: Show Progress

**Week 1** : Run audit → identify gaps
**Week 2-3** : Fix highest-impact items (tests, monitoring, security)
**Week 4** : Document fixes → show buyer "we invested €50K in prep"

**Messaging to buyer** :
> "We ran an honest technical audit. Score: 72/100. We identified [X] gaps, and invested €50K to fix: added test coverage, upgraded monitoring, documented architecture. New score: 84/100. Here's the roadmap for remaining 16-point improvement."

---

## One-Pager for Data Room

```
TECHNOLOGY ASSESSMENT
Updated: [Date]

Current State:
├─ Stack: [Python 3.11, FastAPI, PostgreSQL, AWS]
├─ Deployment: Automated (GitHub Actions → ECS)
├─ Monitoring: DataDog (logs, metrics, APM)
├─ Test coverage: 72% (unit+integration)
└─ Technical debt score: 72/100

Key strengths:
✓ Cloud-native, fully automated deployment
✓ Comprehensive monitoring + alerting
✓ Modern stack (Python 3.11, no legacy)
✓ Scalable to 10x current load

Known gaps & remediation:
- Test coverage: 72% → Target 85% (4 weeks, €16K investment)
- Database backups: Tested quarterly → Now daily (1 week)
- Security: Awaiting SOC 2 audit (6 weeks)

Roadmap post-close:
├─ Q1 2027: SOC 2 Type II compliance
├─ Q2 2027: 10x capacity planning (DB sharding)
└─ Q3 2027: Mobile app (native iOS/Android)
```

---

## Red Flags to Disclose

If true, mention before buyer asks:
- "90% of codebase written by 1 person who might leave"
- "We use [paid library] without license; buyer inherits risk"
- "Database isn't backed up regularly"
- "No access logs; can't audit who accessed what"
- "Performance degrades >5x peak traffic"

**Framing** : "We've identified [X]. Here's the remediation plan. Cost/timeline. We've already started."

---

## Next Step
Run this audit TODAY. Fix what you can in 4 weeks. Show buyer "investment in quality = lower risk."
