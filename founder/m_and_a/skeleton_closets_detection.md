---
name: skeleton_closets_detection
description: Checklist litige, dettes cachées, dépendances clés pour éviter surprises DD
metadata:
  type: checklist
  created: 2026-06-12
---

# Skeleton Closets Detection — Pré-DD Audit Interne

**Objectif :** Identifier les **mauvaises surprises** avant que buyer les découvre lors de DD. Un "surprise" découvert par buyer = -30 à -50% réduction offre.

Mieux vaut les déclarer proactivement et négocier → moins pire que caché.

---

## **Section 1 : Litiges & Menaces Légales**

### **Litiges Actifs**

| Type | Opponent | Status | Amount ($) | Severity | Disclosure? |
|---|---|---|---|---|---|
| Employment lawsuit | Former employee X | Discovery phase | $250k | HIGH | YES (disclose) |
| IP infringement claim | Competitor Y | Demand letter | $500k threat | MEDIUM | YES |
| Breach of contract | Client Z | Resolved | Settled $50k | LOW | Maybe not |

### **Checklist Litiges:**
- [ ] Any active lawsuits? (Federal, state, arbitration)
- [ ] Demand letters received? (From competitors, customers, employees)
- [ ] Settlement agreements signed? (Confidentiality clause?)
- [ ] Injunctions against company? (Non-competes, restraining orders)
- [ ] Employment disputes? (Discrimination, wage claims, wrongful termination)
- [ ] Class action involvement? (As defendant?)
- [ ] Regulatory investigations? (FTC, state AG, labor board)

**Red flag:** Active litigation with potential $1M+ exposure = buyer walks

---

## **Section 2 : Dettes & Financial Obligations**

### **Debt Schedule**

| Creditor | Type | Amount | Term | Maturity | Prepayment Penalty? | Buyer Assumption? |
|---|---|---|---|---|---|---|
| Bank ABC | Term Loan | $500k | 5yr | 2027-06-01 | 2% | Buyer pays off |
| Venture Debt Fund | SAFE/Convertible | $200k | 10yr | 2030-12-31 | NO | Buyer pays off |
| Equipment Financing | Lease | $50k | 3yr | 2026-12-31 | Buyout $10k | Buyer assumes |

### **Checklist Dettes:**
- [ ] Bank loans: terms, covenants, personal guarantees?
- [ ] Venture debt: conversion terms if company acquired?
- [ ] Equipment leases: buyout clauses, transfer approval?
- [ ] Vendor payables > $50k: any disputes?
- [ ] Deferred revenue > $100k: contingent liabilities?
- [ ] Tax liens: any IRS, state tax liens filed?
- [ ] Personal guarantees: founder liable after sale? (Get release!)

**Template Personal Guarantee Review:**
```
Loan: [Name]
Personal Guarantee: [Founder names]
Surviving closing? [YES / NO]
→ ACTION: Negotiate release of personal guarantee as closing condition
```

**Red flag:** $500k personal guarantee surviving acquisition = founder still liable

---

## **Section 3 : Dépendances Clés & Single Points of Failure**

### **People Dependencies**

| Role | Person | Tenure | Unique Knowledge | Retention? | Replacement Difficulty |
|---|---|---|---|---|---|
| VP Engineering | Engineer A | 8 years | Algorithm, architecture | ⚠️ FLIGHT RISK | Very hard (6-12 months) |
| Sales Lead | Salesperson B | 3 years | Customer relationships | Medium | Medium (3-6 months) |
| Product Mgr | Product C | 1 year | Roadmap knowledge | Low | Easy (1-3 months) |

**Checklist:**
- [ ] Who would leave if founder steps down?
- [ ] Who knows critical algorithms, integrations, customer relationships?
- [ ] Any employees with non-competes preventing work post-sale?
- [ ] Key contractors (not employees)? Retained post-deal?
- [ ] Founder as "person of trust" for customers?

**Action:** Retention packages for key people (equity rollover, stay bonus)

---

### **Technology Dependencies**

| Dependency | Type | Owner | Risk if Lost | Mitigation |
|---|---|---|---|---|
| AWS account hosting | Infrastructure | Company | Service outage if access lost | Multi-admin, documented |
| Stripe API integration | Payment processor | Company | Payment processing halts | Escrow account? |
| Third-party SaaS | Data analytics | Company | Data pipeline breaks | License portable? |
| Datadog monitoring | Ops | Single engineer email | Alerts not monitored | Team admin access? |

**Checklist:**
- [ ] AWS/GCP account: multi-admin access documented?
- [ ] API keys stored securely (not in GitHub)?
- [ ] Critical service integrations documented?
- [ ] Sole engineer can't hold company hostage (admin access)?
- [ ] Database backups regular & tested?
- [ ] Vendor lock-in: can data be exported?

**Red flag:** Only engineer X knows how to deploy = buyer loses 2 months post-deal

---

### **Customer Dependencies**

| Customer | % Revenue | Contract | Renewal Risk | Relationship Owner |
|---|---|---|---|---|
| Client A | 20% | Auto-renew | LOW | Sales VP (staying) |
| Client B | 15% | Manual | HIGH | Founder only (leaving?) |

**Checklist:**
- [ ] Top customer account managed by single person?
- [ ] Key customer knows only founder? (High flight risk)
- [ ] Major contracts expiring within 12 months?

**Action:** Introduce buyer to key accounts, transition account ownership

---

## **Section 4 : Compliance & Regulatory Risks**

### **Data Privacy & Security**

- [ ] GDPR compliant? (Privacy policy, data agreements, export rights)
- [ ] CCPA compliant? (California privacy laws)
- [ ] SOC 2 Type II? (Enterprise SaaS customers demand this)
- [ ] HIPAA (if healthcare)? PCI-DSS (if payments)?
- [ ] Penetration testing done? Any critical findings?
- [ ] Security incident history? (Data breach, ransomware, unauthorized access)
- [ ] Data retention policy? (How long do you keep customer data post-cancellation?)

**Red flag:** GDPR violation with $1M+ potential fine = deal value cut significantly

---

### **Employment & Labor**

- [ ] All employees properly classified? (W-2 vs 1099, no misclassification)
- [ ] Wage & hour compliant? (Overtime, breaks, minimum wage)
- [ ] Worker's compensation coverage valid?
- [ ] I-9 forms on file (immigration compliance)?
- [ ] Employee handbook current & compliant?
- [ ] Severance obligations if buyer lays off staff? (WARN Act, notice periods)

**Red flag:** IRS finds 1099 contractor should be W-2 = penalties + buyer liability

---

### **Taxes (Federal, State, International)**

- [ ] Federal & state tax returns filed timely?
- [ ] Tax debt or liens? (IRS installment plans?)
- [ ] Sales tax collected & remitted? (Nexus in multiple states?)
- [ ] Payroll tax current? (Federal, state unemployment)
- [ ] International revenue: VAT / GST registered where needed?
- [ ] R&D tax credits claimed? (If applicable, add to cash)

**Checklist:**
```
[ ] Last 3 years federal tax returns filed
[ ] Last 3 years state tax returns (each jurisdiction)
[ ] Payroll tax filings current (no back taxes)
[ ] Sales tax liability audit (if applicable)
[ ] IRS correspondence: any audit notices?
[ ] Tax liens or IRS debt: any?
```

---

## **Section 5 : Material Contracts Red Flags**

### **Contracts to Flag:**

| Contract Type | Flag | Action |
|---|---|---|
| Customer contract | "Change of control" clause = must notify/consent | **Get written waiver before sale** |
| Vendor contract | Auto-terminates on ownership change | Renegotiate or disclose |
| Key person insurance | Insured person = founder, beneficiary = company | Buyer inherits risk |
| Board seats | Investor has board seat, veto on sale | Need investor approval |
| Co-founder agreements | Drag-along, tag-along rights? | Ensure aligned interests |
| Employment offers | Guaranteed bonuses upon acquisition? | Liability if buyer lays off |

**Template for each:**
```
Contract: [Name]
Counterparty: [Company]
Change of Control: [YES/NO]
If YES:
  - What happens? [Terminates / Renegotiates / Requires consent]
  - Is consent likely? [HIGH / MEDIUM / LOW]
  - Action: [Get waiver / Disclose / Negotiate escrow]
```

---

## **Section 6 : Environmental, Health & Safety (if applicable)**

- [ ] Any environmental permits? (Compliant?)
- [ ] Hazardous material storage? (Compliance audit)
- [ ] Workplace safety incidents? (OSHA recordable events?)
- [ ] Asbestos, mold in offices? (Real estate environmental risk)

**Likely irrelevant for pure SaaS, but check if:**
- Hardware manufacturing
- Physical product
- Labs or facilities

---

## **Section 7 : IP Disputes (separate from audit_IP)**

- [ ] Cease & desist letters received? (From competitors claiming infringement)
- [ ] Prior art search done? (Freedom to operate?)
- [ ] Google, Apple, Microsoft patents threaten your tech?
- [ ] Employee disputes over IP ownership?
- [ ] Co-founder IP disputes? (Who owns what?)

**Action:** Get IP indemnification insurance quote (typical: 1-2% deal value)

---

## **Section 8 : Related Party Transactions**

| Transaction | Counterparty | Amount | Terms | Disclosed? |
|---|---|---|---|---|
| Consulting | Founder's brother | $50k/yr | Vague SOW | NO (RED FLAG) |
| Rent | Founder's property | $5k/mo | Above market | Maybe unfair |
| Software license | Founder's other co. | $20k/yr | Unclear value | Maybe double-dip |

**Checklist:**
- [ ] Any payments to founder family members? (Fair market value?)
- [ ] Rent paid to founder-owned property? (Above/below market?)
- [ ] Side businesses of founder? (Conflict with main company?)
- [ ] Founder personal expenses paid by company? (Car, travel, insurance)

**Red flag:** Founder-to-company transfers never documented = buyer suspect underreported EBITDA

---

## **Section 9 : Insurance Coverage**

| Policy | Type | Coverage | Premium | Expiry | Adequate? |
|---|---|---|---|---|---|
| General Liability | Commercial | $1M | $5k/yr | 2026-12-31 | Yes |
| Directors & Officers | D&O | $2M | $15k/yr | 2026-12-31 | Adequate |
| Cyber Liability | Cyber | $1M | $8k/yr | 2026-06-30 | ⚠️ Expired soon |

- [ ] All policies with current premium?
- [ ] D&O tail coverage available post-sale?
- [ ] Representations & warranty insurance quote obtained?

---

## **The Master Skeleton Closets Checklist**

Print this and go through **with honesty**:

```
CRITICAL (Deal-killing if discovered):
[ ] Active litigation with >$1M exposure
[ ] GPL code in proprietary product
[ ] Founder personal guarantee on $1M+ debt (surviving acquisition)
[ ] Major customer (>15% revenue) with auto-termination on sale
[ ] Tax lien or IRS audit
[ ] Regulatory investigation (FTC, SEC)

MAJOR (30-50% valuation cut):
[ ] Key engineer planning to leave
[ ] GDPR/CCPA compliance gaps
[ ] Payroll tax back-owed
[ ] Customer concentration >50% top-3

MEDIUM (10-30% cut):
[ ] No SOC 2 Type II (for enterprise SaaS)
[ ] Misclassified contractors
[ ] Unclear IP ownership (co-founder dispute)
[ ] Change-of-control clauses on major customer contracts

MINOR (Disclose but < 5% impact):
[ ] Related-party transactions above market rates
[ ] Insurance expiring within 6 months
[ ] Small employment disputes (settled)
```

---

## **Before Dataroom Opening:**

1. [ ] Audit this checklist with **legal counsel** (attorney-client privilege)
2. [ ] Make list of **must-disclose** items (contractual or legal obligation)
3. [ ] Prepare narrative for each:
   - What happened?
   - Current status?
   - Resolution plan?
   - Impact on deal?
4. [ ] Quantify exposure on each (worst-case, likely-case, best-case)
5. [ ] Work with advisor: disclose early = less discount than hidden discovery

**Philosophy:** A disclosed issue = negotiable. A hidden issue discovered = deal dies or 50% off.
