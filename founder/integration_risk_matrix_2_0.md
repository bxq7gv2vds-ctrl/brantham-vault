---
name: integration_risk_matrix_2_0
description: Post-close integration risk matrix — buyer perspective + remediation playbook
type: template
date: 2026-06-12
---

# Integration Risk Matrix 2.0 — Buyer & Seller Perspective

**When:** During DD + SPA negotiation (pre-close), then execute post-close  
**Audience:** Buyer (due diligence), Seller (mitigation + earnout protection)  
**Goal:** Identify integration risks early, build remediation roadmap

---

## FRAMEWORK: Risk Matrix (4 Quadrants)

```
        LOW LIKELIHOOD ← → HIGH LIKELIHOOD
         ↑
         │  (Low risk)      (Medium risk)
 H I G H │                  Q2: Monitor
 I M P A │  Q1: Accept      Q4: Avoid
 C T     │
  │      │  (Medium risk)   (High risk)
  │      │  Q3: Mitigate    
  ↓      │  
         LOW                HIGH
      ← IMPACT →
```

---

## RISK CATEGORIES (20 Items)

### CATEGORY A: PRODUCT INTEGRATION (5 Risks)

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| **A1: Code incompatibility** | Medium | High | Audit codebase Q1; plan 3-mo integration roadmap | CTO |
| **A2: Data model mismatch** | Medium | High | Schema migration test (Q1); ETL pipeline (M3) | Data Lead |
| **A3: API compatibility** | Low | Medium | Maintain legacy API for 12 months; versioning strategy | Eng Lead |
| **A4: Feature duplication** | High | Low | Decide Keep-Separate vs Merge by M1; communicate decision | PM |
| **A5: Technical debt carryover** | High | Medium | Document debt; prioritize top 3 items for M1–M3 fixes | CTO |

### CATEGORY B: CUSTOMER/REVENUE (4 Risks)

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| **B1: Customer churn** | High | High | Win-back kit; founder outreach top 20; NPS tracking weekly | Founder/CS |
| **B2: Pricing conflict** | Medium | High | Lock pricing 12 months; communicate clearly; plan renewal strategy | CFO |
| **B3: SLA degradation** | Low | Medium | Baseline SLAs by M1; no degradation without 90-day notice | Support Lead |
| **B4: Sales overlap (channel conflict)** | Medium | Medium | Define territory; agree on customer assignment; no poaching | Sales Lead |

### CATEGORY C: TEAM/CULTURE (4 Risks)

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| **C1: Key person departure** | High | High | Retention bonuses M0; clear role post-close; founder commitment | HR + Founder |
| **C2: Culture clash** | Medium | High | Weekly all-hands; document values; integrate gradually (not overnight) | Founder/People |
| **C3: Reporting lines unclear** | Medium | Medium | Org chart finalized by D0; communication plan; skip-level meetings allowed | CEO/HR |
| **C4: Compensation misalignment** | Medium | Medium | Match buyer's comp framework quickly (week 1); equity clarity | CFO/HR |

### CATEGORY D: OPERATIONS (4 Risks)

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| **D1: Vendor lock-in** | Medium | Low | Audit contracts for change-of-control clauses; renegotiate if needed | Ops |
| **D2: Data security/compliance issue** | Low | High | SOC 2 audit by M1; GDPR/CCPA audit; security incidents disclosed | Sec/Compliance |
| **D3: Legacy system dependencies** | High | Medium | Document all legacy integrations by M1; plan migration (M3+) | Ops/Eng |
| **D4: Scalability gaps** | Low | Medium | Load testing Q2 (combined scale); infrastructure upgrade plan | Infra |

### CATEGORY E: FINANCIAL (3 Risks)

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| **E1: Working capital drain** | Low | High | Baseline WC requirement agreed in SPA; post-close audit by M2 | CFO |
| **E2: Earnout metric miss** | Medium | High | Weekly KPI tracking; shared dashboard; transparent measurement | Founder/CFO |
| **E3: Hidden liabilities (tax, legal)** | Low | High | Tax audit + tax clearance certs pre-close; reserve escrow for contingencies | CFO/Legal |

---

## SAMPLE RISK MATRIX (Populated)

| Rank | Risk | Risk Level | Q1 Action | Q2 Action | Q3 Action | Q4 Action | Earnout Impact? |
|---|---|---|---|---|---|---|---|
| 1 | B1: Customer churn | 🔴 HIGH | Win-back kit + founder calls | Weekly NPS tracking | Renewal push | Evaluate retention | YES (metric) |
| 2 | C1: Key person departure | 🔴 HIGH | Retention bonus signed | Monthly 1:1s | Career growth plan | Transition planning | YES (implicit) |
| 3 | A1: Code incompatibility | 🟡 MEDIUM | Codebase audit | Integration design | Pilot integration | Full rollout | If "Merger" plan |
| 4 | A2: Data model mismatch | 🟡 MEDIUM | Data audit | ETL design | Build pipeline | Data migration | If "Merger" plan |
| 5 | A5: Technical debt | 🟡 MEDIUM | Identify top 3 items | Fix debt item #1 | Fix debt item #2 | Debt cleared (80%) | If impacts perf |
| 6 | B2: Pricing conflict | 🟡 MEDIUM | Confirm pricing locks | Plan renewals | Execute renewals | Post-renewal analysis | If pricing churn |
| 7 | C2: Culture clash | 🟡 MEDIUM | Values alignment session | Monthly all-hands | Culture survey | Pulse check | If attrition rises |
| 8 | D3: Legacy systems | 🟡 MEDIUM | Map integrations | Plan migration | Pilot migration | Full legacy sunset | If impacts product |
| 9 | D1: Vendor lock-in | 🟢 LOW | Audit contracts | Renegotiate critical | Consolidate | Monitor | NO |
| 10 | A3: API compatibility | 🟢 LOW | Maintain legacy API | Version strategy | Gradual sunset | Legacy API EOL | NO |

---

## EARNOUT PROTECTION (Seller Perspective)

**Critical question:** Which integration risks directly impact your earnout metric?

### Example: Earnout Metric = "Customer Retention ≥ 85%"

**Risks that could trigger churn:**
- B1: Customer churn (direct)
- C1: Key person departure (indirect; team quality impacts support quality)
- B3: SLA degradation (indirect; poor support = lower satisfaction = churn)
- A1–A5: Product bugs (indirect; product quality impacts retention)

**Mitigation for seller:**
- Weekly churn tracking (own the data, not buyer's responsibility)
- Founder personal calls with at-risk accounts
- SLA monitoring (escalate if degrading)
- Product bug prioritization (involve founder in decisions)
- Document all churn causes (if buyer changes pricing, you're not liable)

**SPA Protection Clause:**
```
Earnout KPI = Customer Retention ≥ 85% (measured per [formula])
Seller not liable for churn resulting from:
- Buyer pricing changes post-M6
- Buyer SLA degradation (>10% vs. baseline)
- Buyer product changes (bugs, feature removals)

Seller responsible for:
- Product stability (maintain release quality)
- Customer relationship (founder outreach for high-value accounts)
- Support quality (respond to escalations <24h)
```

---

## 100-DAY INTEGRATION PLAYBOOK

### Days 1–14: Stabilization

**Monday (D0):**
- All-hands meeting (buyer CEO + founder)
- Announce integration plan (60-day roadmap shared)
- Clarify reporting lines, decision authority

**Days 2–5:**
- Knowledge transfer kicks off (founder + key team)
- Customer win-back outreach (top 20 accounts, founder calls)
- Data audit begins (engineering team inventory)

**Days 6–14:**
- Weekly integration sync (buyer + seller leadership)
- Customer feedback surveys (NPS, retention risk early warning)
- Engineering assessment (codebase quality, technical debt)

**KPIs to track:**
- Customer churn: 0%
- Employee retention: 100% (no departures)
- Open integration blockers: <5

### Days 15–45: Planning

**Week 3:**
- Product integration decision (Keep-Separate vs. Merge)
- Data migration plan finalized
- Org structure settled (reporting lines confirmed)

**Week 4:**
- SPA earnout dashboard live (weekly KPI reporting)
- Customer renewal push begins (high-value accounts)
- Engineering roadmap aligned (Q1 priorities)

**Week 5–6:**
- Integration pilots begin (non-critical systems first)
- Team training (new tools, buyer systems)
- Vendor renegotiation (key contracts)

**KPIs to track:**
- Customer churn: <1%
- Employee retention: 100%
- Integration milestone completion: 80%+

### Days 46–100: Execution

**Week 7–10:**
- Product feature shipping (aligned roadmap)
- Data migration (if "Merger" path)
- Customer success handoff (from seller to buyer team)
- Earnout metric tracking (weekly dashboard reviews)

**Week 11–14:**
- Integration sprint completion
- Team org integration (reporting lines solidified)
- Vendor consolidation (if applicable)

**KPIs to track:**
- Customer churn: <2% (target)
- Employee retention: 95%+ (1 planned departure acceptable)
- Earnout metrics: On-track for 80%+ payout
- Product shipping velocity: >5 features/month

---

## RED FLAGS TO ESCALATE IMMEDIATELY

| Red Flag | Action | Owner |
|---|---|---|
| 2+ key team members leave in first month | Board escalation; re-negotiate earnout | Founder + HR |
| Customer churn >3% in first month | Founder emergency calls; review SLA | Founder + CS |
| Product bug blocking customer use | Emergency fix; escalate to buyer CTO | CTO |
| Buyer changes pricing without notice | Legal escalation; earnout dispute risk | Legal |
| Earning target(s) off-track by M1 | Forecast revised; mitigation plan | Founder + CFO |
| Vendor contract terminated unexpectedly | Contingency plan; renegotiate | Ops |
| Compliance/security issue discovered | Legal review; disclosure to buyer | Compliance |

---

## POST-CLOSE REVIEW SCHEDULE

| Milestone | Timeline | Review Items | Owner |
|---|---|---|---|
| **30-Day Pulse** | D30 | Churn? Team retention? Earnout on-track? | Board |
| **90-Day Deep Dive** | D90 | Integration progress? Blockers? Earnout trajectory? | Board + Buyer CEO |
| **6-Month Check-In** | M6 | Earnout achievability? Any structural changes needed? | Board + Buyer |
| **12-Month Assessment** | M12 | Earnout payout probability? Founder role working? | Board + Buyer CEO |

---

## SELLER CHECKLIST: RISK MANAGEMENT PRE-CLOSE

- [ ] Map integration risks (A1–E3 above)
- [ ] Identify earnout-critical risks (B1, C1, A1–A5)
- [ ] Negotiate SPA earnout clauses (protection against buyer-caused churn)
- [ ] Plan 100-day roadmap (daily execution, weekly reviews)
- [ ] Set up earnout dashboard (shared with buyer, weekly reviews)
- [ ] Brief team on integration (clear roadmap, manage expectations)
- [ ] Build contingency fund (for escalations, remediation)
- [ ] Document all decisions in writing (paper trail for disputes)

---

## SUCCESS METRICS (Post-Close)

✅ **Churn <2%** (first 90 days)  
✅ **Team retention 100%** (first 30 days), 95%+ (through M12)  
✅ **Earnout on-track 80%+** (probability by M6)  
✅ **Integration milestones 90%+ complete** (by D90)  
✅ **Zero customer escalations** (resolved within SLA)  
✅ **Zero compliance/security incidents** (clean integration)
## Related
