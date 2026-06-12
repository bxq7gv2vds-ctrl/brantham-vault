---
name: post_acquisition_tech_scorecard
type: template
version: 1.0
date: 2026-06-12
---

# Post-Acquisition Technical Scorecard — Intégration Réussie

**Usage:** Évaluer risques techniques avant & après closing. Décider : "keep separate" vs "merge" vs "sunset".

---

## 1. PRE-ACQUISITION ASSESSMENT (Jour -30 à -1)

Remplir cette section **avant LOI**, basée sur Tech DD.

### Architecture Compatibility Score

| Critère | Score (1-5) | Notes | Integration Risk |
|---------|-----------|-------|-----------------|
| **Language/Framework alignment** | _ | Ex: "Go → Go (low) vs Go → Java (high)" | __ |
| **Database architecture** | _ | Ex: "PostgreSQL → PostgreSQL (easy) vs NoSQL migration needed" | __ |
| **API maturity** | _ | Can each system call the other's APIs cleanly? | __ |
| **Deployment methodology** | _ | Both CI/CD? Both manual? Incompatible patterns? | __ |
| **Infrastructure (cloud, on-prem)** | _ | Same provider? Different regions/costs? | __ |
| **Codebase quality** | _ | Is codebase well-documented? Tests coverage? | __ |
| **Tech debt estimate** | _ | Refactor months needed (pre-merge) | __ |
| **Security/compliance posture** | _ | Both SOC2? One missing certs? | __ |

**Compatibility Score = Avg / 5 = ___%**

**Interpretation:**
- **4-5:** Low integration risk → Can merge codebases within 3-6 months
- **3-4:** Medium risk → Keep separate 6-12 months, API-first integration
- **2-3:** High risk → Likely sunset one product or major refactor (12-24mo)
- **<2:** Severe risk → Recommend portfolio approach (keep as separate products)

---

### Key Person Risk Assessment

| Role | Name | Essential? | Risk Level | Retention Plan |
|------|------|-----------|-----------|-----------------|
| **CTO/Lead Architect** | ___ | Y/N | Low/Med/High | $__ earnout, title |
| **Lead Backend Eng** | ___ | Y/N | Low/Med/High | $__ earnout, autonomy |
| **Lead Frontend Eng** | ___ | Y/N | Low/Med/High | $__ earnout, remote OK |
| **Product Manager** | ___ | Y/N | Low/Med/High | $__ earnout, no reorg 12mo |
| **DevOps/Infrastructure** | ___ | Y/N | Low/Med/High | $__ earnout, no changes |

**Key Person Retention Target:** ≥80% retention of "Essential=Y" by month 6

---

## 2. INTEGRATION ROADMAP (Months 0-24)

### Phase 0: Stabilization (Months 0-3)
**Goal:** Keep lights on, no disruption to customers.

| Milestone | Week | Owner | Status |
|-----------|------|-------|--------|
| API contracts defined | W1 | CTO | _ |
| Incident response playbook shared | W1 | DevOps | _ |
| Customer communication plan drafted | W1 | PM | _ |
| SLA/uptime targets agreed | W2 | Ops | _ |
| Security audit (acquirer's pentest) | W2-W3 | Security | _ |
| Shared monitoring/alerting (read-only) | W3 | DevOps | _ |
| First integration meeting (roadmap) | W4 | CTO + Acq CTO | _ |

**Success Criteria:** Zero downtime for acquired product, on-time releases continue.

---

### Phase 1: API Integration (Months 3-6)
**Goal:** Acquired product's data accessible via APIs to acquirer's platform.

| Milestone | Month | Owner | Status |
|-----------|-------|-------|--------|
| **Data synchronization** (read-only) | M3-M4 | Backend | _ |
| **Customer portal migration** (dual-login) | M4 | Frontend | _ |
| **Billing/revenue recognition** integrated | M4-M5 | Finance | _ |
| **User authentication unified** (SSO if applicable) | M5 | Auth team | _ |
| **First feature cross-sell** shipped | M5-M6 | Product | _ |

**Success Criteria:** Customers can access both products from single dashboard, no manual data sync.

---

### Phase 2: Codebase Consolidation (Months 6-12) — *Optional*
**Goal:** Merge codebases IF compatibility score ≥3.5 AND team alignment strong.

| Milestone | Month | Owner | Status |
|-----------|-------|-------|--------|
| **Shared libraries extracted** | M6-M7 | Backend | _ |
| **Monorepo structure decided** | M7 | CTO | _ |
| **First service migrated** (non-critical) | M8-M9 | Backend | _ |
| **Documentation unified** | M9 | Tech lead | _ |
| **Testing infrastructure consolidated** | M10 | QA/DevOps | _ |

**Go/No-Go Decision at M6:**
- [ ] **GO:** Compatibility ≥3.5, tech debt <200 days, team all-in
- [ ] **NO-GO:** Keep as separate products, API-driven integration only

**Success Criteria:** Code quality maintained (test coverage >80%), deployment frequency ≥1/week per service.

---

### Phase 3: Platform Unification (Months 12-24) — *Strategic*
**Goal:** Single product vision, unified UX, consolidated operations.

| Milestone | Month | Owner | Status |
|-----------|-------|-------|--------|
| **Sunset decision** (old product vs new) | M12 | CEO + Product | _ |
| **UX/branding aligned** | M12-M14 | Design | _ |
| **Customer migration plan** (if sunsetting) | M14 | CS | _ |
| **Final monolith merge** (if applicable) | M15-M18 | Eng | _ |
| **Launch unified product** | M18-M24 | Entire team | _ |

**Success Criteria:** 95%+ customer retention post-unification, NPS stable or improved.

---

## 3. TECHNICAL RISK MATRIX

Identify 5-10 biggest technical risks post-close. Rate severity & mitigation.

| Risk | Severity (1-5) | Probability (1-5) | Mitigation | Owner |
|------|---|---|-----------|-------|
| **Database migration deadlock** | 4 | 3 | Pilot with 10% data first; dual-write period 4w | Backend |
| **Customer auth system incompatible** | 5 | 2 | Build adapter layer; customers see no change | Auth |
| **Payment processing integration fail** | 5 | 1 | Run parallel billing 8w; verify parity daily | Finance/Eng |
| **Infrastructure cost explosion** | 3 | 4 | Audit cloud usage; consolidate regions M4 | DevOps |
| **Key engineer leaves post-close** | 4 | 3 | $__k retention bonus; autonomy guarantee | HR |
| **Security compliance gap** (SOC2 vs not) | 4 | 2 | Audit acquirer's auditor; fast-track cert | Security |
| **Major product bug post-merge** | 3 | 2 | Increase test coverage to 85%; ship slower M0-M3 | QA |
| **Data loss during migration** | 5 | 1 | 3x backup, point-in-time recovery tested | DevOps |

**Overall Technical Risk Score = (Σ Severity × Probability) / 40 = __/5**

- **<2:** Low risk → proceed with standard integration
- **2-3:** Medium risk → add 2-4 extra engineers, extend timeline by 20%
- **3-4:** High risk → consider keeping separate longer, phased approach
- **>4:** Critical risk → escalate to CEO, may require deal restructure

---

## 4. OPERATING MODEL: KEEP OR MERGE?

**Decision Matrix — What to Do with Acquired Tech**

### Option A: Keep Separate (Portfolio Approach)
**Use if:** Compatibility <3, product has distinct customers, strategic autonomy valuable

| Aspect | Model |
|--------|-------|
| **Engineering teams** | Separate, report to different PMs |
| **Codebases** | Independent repos, own CI/CD pipelines |
| **Infrastructure** | Separate cloud accounts / clusters (can optimize later) |
| **Releases** | Independent cadence, no coupling |
| **Data integration** | API-based sync (read-only or event-driven) |
| **Shared services** | Auth (if possible), logging, monitoring |
| **Timeline** | Indefinite; reassess annually |

**Pros:** Low risk, fast time-to-value, preserve distinct brand/culture
**Cons:** Operational overhead (2 teams), missed cross-sell opportunities, higher cloud costs

---

### Option B: Merge After 6-12 Months (Consolidation)
**Use if:** Compatibility ≥3.5, natural product fit, cost savings valuable

| Aspect | Model |
|--------|-------|
| **Engineering teams** | Unified under acquirer's CTO, but preserve sub-teams by feature |
| **Codebases** | Gradual consolidation; monorepo by M12 |
| **Infrastructure** | Unified cloud account, shared databases by M9 |
| **Releases** | Aligned cadence; feature flagging for independent rollouts |
| **Data integration** | Direct database access; eventual single source of truth |
| **Shared services** | All services shared (auth, payments, logging, monitoring) |
| **Timeline** | 12-18 months to full consolidation |

**Pros:** Streamlined ops, cost efficient, unified product experience
**Cons:** Higher technical risk, longer timeline, key person risk

---

### Option C: Hybrid (Best of Both)
**Use if:** Want merged business logic but separate ops initially

| Aspect | Model |
|--------|-------|
| **Engineering teams** | Separate teams for 12mo, then gradual merge by feature |
| **Codebases** | Shared libraries from month 3; keep app code separate until M12 |
| **Infrastructure** | Acquirer's platform, but isolated databases until M9 (migration plan by M6) |
| **Releases** | Aligned infrastructure; separate feature releases |
| **Data integration** | API-first (M0-M6), then direct integration after M6 |
| **Shared services** | Auth, payments, monitoring shared by M3 |
| **Timeline** | 18-24 months; flexibility to stay separate longer if issues |

**Pros:** Balance speed & safety, reduce technical debt gradually, preserve stability
**Cons:** Moderate complexity, requires clear communication

---

## 5. POST-CLOSE CHECKLIST (Day 0-7)

- [ ] **Day 0:** All systems still up, no customer-facing changes
- [ ] **Day 1:** Acquirer's CTO has admin access to all systems (read-only OK)
- [ ] **Day 1:** First engineering sync scheduled (weekly cadence)
- [ ] **Day 2:** Incident playbook tested (war game: "What if X goes down?")
- [ ] **Day 3:** Security audit results reviewed; remediation plan drafted
- [ ] **Day 3:** Key person retention bonuses wired (first tranche)
- [ ] **Day 5:** Integration roadmap finalized (phased approach agreed)
- [ ] **Day 5:** Customer comms sent (reassurance + timeline for integrations)
- [ ] **Day 7:** First integration sprint planned (M0-M3 deliverables locked)

---

## 6. SUCCESS METRICS (12 Months Post-Close)

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| **Product uptime** | >99.9% | __ | 🟢/🟡/🔴 |
| **Customer retention** | >95% | __ | 🟢/🟡/🔴 |
| **Deployment frequency** | ≥2x/week | __ | 🟢/🟡/🔴 |
| **Key engineer retention** | ≥80% | __ | 🟢/🟡/🔴 |
| **Tech debt reduction** | -20% | __ | 🟢/🟡/🔴 |
| **Cost per customer** | -15% | __ | 🟢/🟡/🔴 |
| **Cross-sell revenue** | >$__/mo | __ | 🟢/🟡/🔴 |
| **NPS change** | Stable or +5 | __ | 🟢/🟡/🔴 |

**Success = 7/8 metrics green by M12**

---

## 7. ESCALATION TRIGGERS

If any of these happen, escalate to CEO immediately:

- 🚩 **Key engineer leaves** (especially CTO or lead architect)
- 🚩 **Customer churn >15%** in first 6 months
- 🚩 **Major security breach** discovered post-close
- 🚩 **Tech debt grows** instead of shrinks (codebase deteriorating)
- 🚩 **Acquisition cost grows** >20% vs. planned (cloud overspend)
- 🚩 **Integration delays >4 weeks** vs. roadmap (timeline slip)
- 🚩 **Data loss or corruption** incident
- 🚩 **Customer contract breach** (SLA violation, feature removal)

---

## TEMPLATE USAGE

**Pre-LOI (D30-D50):**
- Complete Sections 1-2 (assessment + roadmap)
- Share with buyer's CTO to align expectations
- Use to negotiate retention bonuses, earnout structure

**Post-LOI (D50-D95):**
- Finalize Sections 3-4 (risk matrix, operating model)
- Lock in "Keep Separate vs Merge" decision
- Publish to integration planning team

**Pre-Closing (D95-D120):**
- Prepare Section 5 (Day 0-7 checklist)
- Run war games on critical scenarios
- Confirm key person agreements

**Post-Closing (D120+):**
- Track Section 6 (success metrics) monthly
- Monitor escalation triggers
- Update integration roadmap if variance >10%
## Related
