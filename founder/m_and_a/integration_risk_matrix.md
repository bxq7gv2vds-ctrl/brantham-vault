---
name: integration-risk-matrix
description: Risques post-close (team, produit, clients) — probabilité, impact, mitigation
metadata:
  type: tool
  created: 2026-06-12
---

# Integration Risk Matrix — Post-Close Scenarios

Use this BEFORE closing to identify risks. Update quarterly post-close. Focus = prevent surprises.

---

## How to Use

1. **List all risks** that could derail integration (see categories below)
2. **Score each**: Probability (1-5) × Impact (1-5) = Priority
3. **Assign owner**: Someone watches each risk
4. **Mitigation plan**: Specific action to reduce probability or impact
5. **Monitor weekly** first month, then monthly

---

## Risk Categories & Examples

### CATEGORY 1: TEAM / PEOPLE RISK 👥

| Risk | Prob (1-5) | Impact (1-5) | Priority | Mitigation |
|------|-----------|-------------|----------|------------|
| **CTO leaves post-close** | 3 | 5 | 15 🔴 | Retention bonus ($X) locked pre-close, new title, clear roadmap |
| **VP Sales leaves** | 2 | 4 | 8 | Role clarity, new quota agreed, equity bonus structure |
| **Key engineer walks** | 3 | 3 | 9 | Skip-level lunches with buyer exec, equity package disclosed |
| **Team morale tanks (exodus)** | 4 | 4 | 16 🔴 | All-hands day 1, communication plan, confirm job security |
| **Culture clash (your team vs buyer)** | 3 | 3 | 9 | Joint culture workshop pre-close, joint rituals post-close |
| **Buyer replaces your mgmt** | 2 | 5 | 10 | Negotiate "100-day no changes" clause in LOI |
| **Salary/equity misalignment** | 3 | 2 | 6 | Pre-close: salary benchmarking, equity conversation |

**Mitigation Owner**: HR + Founder (retention = critical)

### CATEGORY 2: PRODUCT / TECHNICAL RISK 🛠️

| Risk | Prob | Impact | Priority | Mitigation |
|------|------|--------|----------|------------|
| **Code quality issues block merge** | 2 | 4 | 8 | Pre-close technical audit + roadmap |
| **Infra migration fails / downtime** | 2 | 5 | 10 | Dry run 60 days before, parallel running 2 weeks |
| **Data loss / backup failure** | 1 | 5 | 5 | Backup tested, recovery procedure documented |
| **Cybersecurity incident discovered** | 1 | 5 | 5 | SOC2 audit pre-close, pen test results shared |
| **Vendor lock-in prevents integration** | 2 | 3 | 6 | Pre-close: list all vendor contracts, switching costs |
| **Customer bugs spike post-close** | 3 | 3 | 9 | Dedicated support team assigned, SLA agreed |

**Mitigation Owner**: CTO + Buyer CTO (technical diligence clear)

### CATEGORY 3: CUSTOMER / REVENUE RISK 📊

| Risk | Prob | Impact | Priority | Mitigation |
|------|------|--------|----------|------------|
| **Top customer churns (big revenue loss)** | 2 | 5 | 10 | CEO call pre-close, joint onboarding plan |
| **Customer concentration spike** | 3 | 3 | 9 | Identify top 5 + assign success managers |
| **Churn accelerates post-close** | 3 | 4 | 12 🟡 | Customer comms plan, no product changes first 30 days |
| **Pricing / packaging confusion** | 2 | 2 | 4 | Pre-close: confirm pricing strategy, no changes post-close |
| **Cross-sell fails (no synergy)** | 3 | 2 | 6 | Pilot before full commitment, metrics clear |
| **Sales team performance drops** | 2 | 3 | 6 | Compensation structure finalized, quota agreed |

**Mitigation Owner**: VP Sales + Buyer VP Sales (customer comms = first priority)

### CATEGORY 4: FINANCIAL / EARNOUT RISK 💰

| Risk | Prob | Impact | Priority | Mitigation |
|------|------|--------|----------|------------|
| **Miss earnout targets (revenue shortfall)** | 3 | 4 | 12 🟡 | Conservative projections, floor payment agreed, metrics within control |
| **EBITDA earnout killed by cost cuts** | 2 | 4 | 8 | Earnout tied to revenue/NRR (seller controls), not EBITDA |
| **Buyer disputes earnout calculation** | 2 | 3 | 6 | Independent audit clause, dispute resolution pre-agreed |
| **Escrow claim surprises you** | 2 | 3 | 6 | Cap = escrow, basket $50K+, 12-month survival max |
| **Tax liability discovered post-close** | 2 | 3 | 6 | Tax audit pre-close, reserve for known issues |

**Mitigation Owner**: CFO + M&A counsel (financial agreements clear before signing)

### CATEGORY 5: STRATEGIC / ALIGNMENT RISK 🎯

| Risk | Prob | Impact | Priority | Mitigation |
|------|------|--------|----------|------------|
| **Buyer changes strategy (kills your product)** | 2 | 5 | 10 | Product roadmap locked for Year 1 (separate agreement) |
| **Integration takes 2x longer** | 3 | 2 | 6 | Milestone-based integration plan, weekly governance |
| **Buyer's priorities shift (delays synergies)** | 3 | 2 | 6 | Synergy goals documented in LOI, tracked monthly |
| **Founder role ambiguous / misaligned** | 3 | 3 | 9 | Written job description, reporting line, decision rights clear |
| **Board meddling in integration** | 2 | 2 | 4 | Clear decision-making authority documented |

**Mitigation Owner**: Founder + Buyer CEO (role clarity = critical)

### CATEGORY 6: EXTERNAL / MARKET RISK 🌍

| Risk | Prob | Impact | Priority | Mitigation |
|------|------|--------|----------|------------|
| **Market downturn kills demand** | 2 | 3 | 6 | No control; accept as risk. Monitor for options. |
| **Competitor launches, undercutting price** | 2 | 2 | 4 | No control; focus on differentiation. |
| **Regulatory change (GDPR, CCPA tightens)** | 2 | 2 | 4 | Compliance audit done, roadmap clear. |
| **Key industry customer bankruptcy** | 1 | 4 | 4 | Concentration audit; diversification plan. |

**Mitigation Owner**: CEO (observe, don't over-plan for external risks)

---

## Priority Matrix (Visualization)

```
        IMPACT
        5 (Critical)  │  
    4 (High)         │     10🔴  
    3 (Medium)       │  8   9   15🔴  16🔴
    2 (Low)          │  4   6    12🟡  12🟡
    1 (Minimal)      │  1   2    3     4
                     └──────────────────────
                     1   2   3    4    5
                     PROBABILITY
```

**🔴 RED (Priority 15+)**: Immediate action, weekly checks
**🟡 YELLOW (Priority 10-14)**: Important, bi-weekly checks
**🟢 GREEN (Priority <10)**: Monitor, monthly reviews

---

## Top 3 Risk Mitigation Actions (Pre-Close)

### Action 1: Team Retention Plan
```
Owner: HR / Founder

By signing day, confirm:
☑ All key people have signed retention bonus agreements
☑ New titles / roles documented and agreed
☑ Equity acceleration (if any) clarified
☑ Post-close responsibilities defined

Cost: $[X] retention bonuses (earmarked in deal structure)
Timeline: Finalize by LOI signing, execute pre-close
```

### Action 2: Customer Comms & Win-Back Plan
```
Owner: VP Sales / VP Success

By signing day, prepare:
☑ Customer announcement email (pre-written, reviewed by buyer)
☑ CEO talking points (top 5 customer calls)
☑ Win-back kit (for any concerns)
☑ Product roadmap highlights (show progress)

Timeline: Send day 1, CEO calls day 2-3
```

### Action 3: Product / Technical Lock-Down
```
Owner: CTO

30 days pre-close, confirm:
☑ No major refactors or code changes (stability first)
☑ Technical audit completed (no surprises)
☑ Infra migration plan approved (if applicable)
☑ Disaster recovery tested

Timeline: Freeze day 30, unfreeze day 1 post-close
```

---

## Weekly Risk Review (First 30 Days)

**Every Monday morning, update this:**

| Risk | Prob | Impact | Current Status | Action |
|------|------|--------|---|---|
| CTO retention | 3 | 5 | On track ✓ | Continue skip-level lunches |
| Customer churn | 3 | 4 | Alert 🟡 | CEO call to [Customer X] today |
| Code merge | 2 | 4 | On track ✓ | Demo to buyer Friday |
| Earnout clarity | 2 | 3 | On track ✓ | Spreadsheet shared, no disputes yet |

**Red flags that escalate**:
- If Prob increases (e.g., "CTO said he's thinking about leaving")
- If Impact increases (e.g., "second customer threatening to leave")
- If mitigation fails (e.g., "retention bonus didn't convince engineer")

**Escalation process**: Alert Founder + Buyer CEO same day.

---

## Decision Rules: When to Escalate

**ESCALATE IMMEDIATELY (call buyer CEO same day):**
- Any key person resignation or threat
- Any top-3 customer threatens to leave
- Any major technical issue (data loss, security breach)
- Any earnout metric looks like it'll miss by >10%
- Any legal claim or regulatory issue

**ESCALATE WEEKLY (Monday morning call):**
- Any yellow-flag risk trending toward red
- Any new risk identified that wasn't pre-identified
- Any mitigation plan that isn't working

**ESCALATE MONTHLY (steering committee):**
- All risks reviewed, re-scored
- Integration roadmap adjusted if needed
- Synergy targets on track?

---

## Post-Close Review (Day 90, Month 6, Year 1)

**Day 90 Review:**
```
✓ Which risks materialized? (Why were we wrong?)
✓ Which risks didn't happen? (Why were we overly cautious?)
✓ New risks emerged? (What didn't we foresee?)
✓ Mitigation plan working? (Adjust what isn't)
```

**Month 6 Review:**
```
✓ Is integration on track?
✓ Team retention: Anyone unexpected left? Anyone we thought would leave, didn't?
✓ Revenue: On plan? Above? Below? Why?
✓ Earnout targets: Pace to hit? On track?
```

**Year 1 Review:**
```
✓ Deal thesis validated?
✓ Synergies realized?
✓ Earnout hit? (If relevant)
✓ Lessons learned for next M&A?
```

---

## Template: Your Risk Matrix (Fill This In)

```
INTEGRATION RISKS — [Your Company] + [Buyer Name]

TEAM RISKS
- CTO retention: Prob 3, Impact 5 → Owner: HR
  Mitigation: $[X] bonus locked, new title = VP Engineering
  
- [Your risk]: Prob __, Impact __ → Owner: [Name]
  Mitigation: [Action]

PRODUCT RISKS
- Code merge complexity: Prob 2, Impact 4 → Owner: CTO
  Mitigation: Dry run pre-close, parallel 2 weeks
  
- [Your risk]: Prob __, Impact __ → Owner: [Name]
  Mitigation: [Action]

CUSTOMER RISKS
- Top customer churn: Prob 2, Impact 5 → Owner: VP Sales
  Mitigation: CEO call pre-close, joint success plan
  
- [Your risk]: Prob __, Impact __ → Owner: [Name]
  Mitigation: [Action]

[Continue for other categories]

SUMMARY
Red flags (15+): [X] → Immediate action
Yellow flags (10-14): [Y] → Weekly monitoring
Green flags (<10): [Z] → Monthly review

Highest leverage action: [What single thing reduces most risk?]
Owner accountability: [Who's responsible for overall risk management?]
```

---

## Golden Rule

**The best risk mitigation = pre-close conversation + explicit agreement.**

Don't hope things will work out post-close. Discuss risks openly with buyer, document agreements, assign owners, and track weekly.

**Use case**: Week 1 of diligence, share this with buyer to start risk conversation. "Here are the integration risks we see. How do we mitigate together?"
## Related
## Related
## Related
