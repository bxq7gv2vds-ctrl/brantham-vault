---
name: integration_timeline
description: Post-close integration — timeline 100 jours, métriques, plans customer/team
metadata:
  type: reference
  format: project_template
  version: 1.0
---

# Integration Timeline — 100 jours post-close

**Template pour acheteur & vendeur — objectifs, milestones, success metrics.**

---

## **WEEK 1-2 : Quick wins & stabilization**

| Jour | Milestone | Owner | Success Criteria |
|------|-----------|-------|-----------------|
| **D1** | **Closing signed & announces to market** | CEO | Press release, customer notification |
| **D1** | Product access preserved (no migrations yet) | CTO | All customers access product via same URL |
| **D2** | Customer call blitz (top 20) | Sales + Vendor | 0 churn signals, 90%+ positive sentiment |
| **D3** | Employee meeting: integration plan | HR | Org chart, roles clear, no surprise resignations |
| **D4** | Email system migration (if applicable) | IT | New domain email live, old domain forwarded 90 days |
| **D5** | Legal review: customer contracts | Legal | No change-of-control breaches identified |
| **D7** | Payroll integration (if applicable) | Finance | First post-close payroll executed on time |
| **D10** | Data security audit | Security | No vendor data exposed, GDPR compliant |

**Win condition:** Zero customer notifications of surprise, zero unplanned employee departures.

---

## **WEEK 3-4 : Product & customer migration**

| Milestone | Detail | Risk |
|-----------|--------|------|
| **Product integration kickoff** | Plan feature parity (if combining products) | "New product worse than old" → churn |
| **Customer transition SOP** | Whose support team owns account? | Confusion → tickets unanswered |
| **API integration (if applicable)** | Connect data / workflows | Data loss or duplication |
| **Brand/naming (if rebranding)** | Update UI, domain, docs | User confusion, lost SEO |

**Owner:** Product + customer success co-own.

---

## **MONTH 2 : Deep integration & optimizations**

| Task | Timeline | Owner | Earnout Impact |
|------|----------|-------|-----------------|
| Infrastructure consolidation | Week 5-6 | CTO | Cost reduction (not customer-facing) |
| Sales process integration | Week 5-8 | Sales | New logo velocity (earnout metric?) |
| Duplicate customer deduplication | Week 6-8 | Data team | Accurate ARR calculation (earnout!) |
| Pricing alignment (if applicable) | Week 7-8 | Product/Finance | Avoid churn on price increases |
| Vendor key person involvement | All | Vendor | Ensure retention targets met |

---

## **MONTH 3 : Stabilization & full integration**

| Task | Timeline | Success |
|------|----------|---------|
| All systems migrated | Day 70 | No data in old systems |
| Customer training complete | Day 75 | NPS stable or improving |
| Cost synergies realized | Day 90 | Savings materialized (optional) |
| Earnout targets on track | Day 90 | Retention ≥ [target]%, ARR ≥ [target]€ |

---

## **SUCCESS METRICS (Weekly tracking)**

### **Customer Metrics** ⭐ (Earnout linked)

```
Weekly dashboard:
├─ Churn (new): # customers lost this week [Target: 0-1 max]
├─ Retention rate (YTD): % from day 0 still active [Target: ≥95% first 30 days]
├─ Expansion: # customers upgrading [Target: baseline+]
├─ NPS: survey 5% of base monthly [Target: maintain or +5]
├─ Tickets/support volume: rising or stable? [Target: stable]
└─ Key customer sentiment (top 20): any concerns? [Target: all green]
```

### **Operational Metrics**

```
├─ Team churn: any unexpected departures? [Target: 0]
├─ Payroll/benefits: on-time, no issues? [Target: 100%]
├─ System uptime: any outages? [Target: >99.9%]
├─ Support response time: maintained? [Target: <24h]
└─ Product bugs introduced: any critical? [Target: 0 critical]
```

### **Earnout-specific metrics** 🎯

```
Day 30:  Validate customer list integrity (no double-count)
Day 45:  Mid-point check on churn, expansion
Day 60:  Projection: will we hit Y1 targets?
Day 90:  Final Y1 baseline lock (for earnout calculation)

Calculation:
├─ Retention: (# customers_day90 / # customers_day0) × 100 [≥85%?]
├─ ARR: €[day0] → €[day90] [growth ≥X%?]
└─ Churn: monthly rate [<5%?]
```

---

## **CRITICAL PATH : Things that kill earnout**

### 🚫 High-risk integration decisions

```
❌ Shutting down legacy product too quickly
   → Customers forced to migrate or leave
   → Earnout targets miss
   
❌ Raising prices immediately post-close
   → Churn spike
   → Earnout targets miss
   
❌ Key people leave / customer success degraded
   → Support tickets spike, NPS drops
   → Hidden churn (cancellations not noticed)
   
❌ Data migration bugs / data loss
   → Customer trust broken
   → Immediate churn
   
❌ Vendor not actively involved (consulting ended too early)
   → Customer relationships strained
   → Churn in vendors' relationships
```

### ✓ Protect earnout targets

```
MUST-DO:
1. Vendor (founder) stays active 12 months (even part-time)
   → customer confidence critical
   
2. Freeze pricing for 12 months
   → customer retention lock
   
3. Maintain feature parity during integration
   → no feature downgrades
   
4. Dedicated customer success during transition
   → same people, same SLAs
   
5. Monthly earnout tracking dashboard
   → catch churn early, fix
```

---

## **STAKEHOLDER ROLES**

### **Buyer CEO**
- Owns overall integration success
- Updates to vendor (founder) monthly
- Makes trade-off decisions (speed vs. customer care)

### **Vendor (Founder)**
- Consults on customer relationships
- Joins key customer calls (as advisor/founder)
- Monthly verification of earnout metrics
- Advises on product decisions (prevents churn)

### **Customer Success Owner** (critical role)
- Owns customer retention
- Primary contact for each account
- Reports weekly churn/expansion
- Escalates concerns to vendor (founder)

### **Finance/FP&A**
- Calculates earnout monthly
- Reconciles ARR per customer
- Prepares earnout verification report

---

## **VENDOR'S ROLE POST-CLOSE**

### Recommended engagement

```
Month 1: Full-time (on-site or video)
├─ Daily customer calls (top 20)
├─ Product roadmap discussions
└─ Integration decisions (co-design)

Month 2: 50% (part-time consulting)
├─ Weekly customer calls
├─ Quarterly business reviews
└─ Escalation for at-risk accounts

Month 3+: 10-20% (advisory)
├─ Monthly check-ins
├─ New customer on-boarding calls
└─ As-needed for high-value accounts
```

**Compensation:** Earnout + consulting fees (if extended beyond retention period).

---

## **INTEGRATION CHECKLIST**

### **Legal/Admin**
- [ ] Customer contracts reviewed (no termination rights triggered)
- [ ] Employment agreements executed (all team)
- [ ] IP transfer documented
- [ ] Insurance updated (D&O coverage continues)
- [ ] Tax filings updated

### **Operational**
- [ ] Finance systems integrated
- [ ] IT systems migrated (email, Slack, etc.)
- [ ] Vendor contracts renegotiated (discounts from consolidation)
- [ ] HR policies aligned (vacation, benefits, etc.)

### **Customer**
- [ ] All customers notified (positive framing)
- [ ] Support continuity documented
- [ ] SLAs maintained or improved
- [ ] Onboarding process unchanged (30 days)
- [ ] Billing system integrated (no double-billing)

### **Product**
- [ ] No feature regressions
- [ ] Data migration tested & verified
- [ ] APIs documented
- [ ] Roadmap shared with customers

### **Finance/Earnout**
- [ ] Earnout measurement system live
- [ ] Monthly reporting established
- [ ] Customer list locked (for earnout baseline)
- [ ] Churn tracking automated
- [ ] ARR reconciliation process built

---

## **RED FLAGS (integration gone wrong)**

🚨 **Monitor for these daily:**

```
❌ Unplanned customer cancellation (especially top 10)
❌ Multiple support tickets from same customer
❌ Key vendor employee doesn't show up
❌ Finance can't reconcile customer list (merger/acquisition debt?)
❌ Email system down (communication breakdown)
❌ Product outage >1 hour
❌ Customer calls buyer's leadership (bypassing normal escalation)
❌ Earnout metrics show decline vs. baseline
```

**If any red flag → immediate escalation to CEO + vendor (founder).**

---

## **WEEK-BY-WEEK CHECKLIST**

```
Week 1: Customers stay, team stays, systems work
Week 2: Integration communication sent, key questions answered
Week 3: Product migrations started, zero unplanned churn
Week 4: Customer transitions on track, feedback positive
Week 5-6: Cost synergies identified, roadmap shared with customers
Week 7-8: Earnout tracking dashboard live, targets on pace
Week 9-10: Duplicate data resolved, ARR locked for earnout
Week 11-12: Month 3 review, earnout projection green, team morale solid

Success = Day 90: Zero unplanned customer churn, earnout targets achievable.
```

