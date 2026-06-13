---
name: template-customer-contract-audit
description: Spreadsheet template — Audit 100% des contrats clients pour risques change-of-control et termination
metadata:
  type: template
  created: 2026-06-13
---

# Customer Contract Audit Template

Use this to flag every customer contract clause that could break the deal.

## Instructions

1. Export all customer contracts into a folder
2. For each contract, fill one row in the spreadsheet below
3. Flag any "YES" or unusual terms → discuss with buyer's legal team ASAP

## Audit Spreadsheet

| Customer Name | ARR | Contract Sig. Date | Renewal Date | Change-of-Control Clause? | Termination for Convenience? | Termination Fee? | Automatic Renewal? | Non-Assignable? | Other Risks | Risk Level | Mitigation Plan |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Customer A | $100k | 2024-03-01 | 2025-03-01 | YES - can terminate | NO | N/A | YES | YES - must renegotiate | Long tail liability (3yr) | HIGH | Get written consent before LOI |
| Customer B | $50k | 2023-06-15 | 2026-06-15 | NO | YES (30d notice) | 3mo fees | NO | NO | Standard terms | LOW | Nothing needed |
| Customer C | $200k | 2022-01-01 | Evergreen | NO | NO | N/A | YES | NO | Evergreen contract risky (stuck) | MEDIUM | Renegotiate termination clause pre-LOI |
| Customer D | $30k | 2025-01-10 | 2025-07-10 | YES + approval required | YES | Full refund if <6mo | YES | YES | Multiple red flags | CRITICAL | Need explicit buyer waiver |

## Field Definitions

**Customer Name:** Legal entity name on contract

**ARR:** Annual Recurring Revenue for this customer

**Contract Sig. Date:** When contract was signed

**Renewal Date:** Next renewal/expiry date (or "Evergreen" if no termination clause)

**Change-of-Control Clause?**
- `NO` = customer has no say if you get acquired
- `YES - can terminate` = customer can terminate if acquired (risk)
- `YES - approval required` = customer must approve (very risky)
- `YES - price adjustment` = customer can renegotiate price post-acquisition

**Termination for Convenience?**
- `YES (Xd notice)` = customer can terminate anytime with X days' notice
- `NO` = customer locked in until renewal
- `YES - early termination` = customer can bail out early with penalty

**Termination Fee:**
- `None` or `N/A` = no penalty if customer leaves
- `X mo fees` = penalty = X months of fees
- `Full refund` = customer gets refund of unused portion (dangerous)

**Automatic Renewal?**
- `YES` = contract auto-renews unless customer opts out
- `NO` = expires on date, customer must affirmatively renew
- `Evergreen` = rolls forward indefinitely unless either party terminates

**Non-Assignable?**
- `YES` = contract says you cannot transfer this to another company without customer's written consent
- `NO` = contract is assignable (standard)

**Other Risks:** Free-text. e.g., "3-year minimum commitment," "customer has MFN clause," "vendor lock-in after migration"

**Risk Level:**
- `LOW` = standard terms, no acquisition concern
- `MEDIUM` = some risk (e.g., change-of-control clause but low $ or short term)
- `HIGH` = significant risk (e.g., large $ + change-of-control + requires approval)
- `CRITICAL` = deal-breaking (e.g., largest customer can terminate, no consent process)

**Mitigation Plan:**
- `Nothing needed` = standard
- `Get written consent before LOI` = customer agrees in writing to assignment/waives change-of-control
- `Renegotiate pre-LOI` = update terms before entering LOI (e.g., extend renewal, remove change-of-control)
- `Buyer assumption` = buyer accepts as-is (buyer decision)
- `Need escrow` = holdback $ to cover potential churn

---

## Summary Metrics

After audit is complete, calculate:

| Metric | Calculation | Threshold | Action |
|---|---|---|---|
| **Concentration Risk** | (Top 3 customers' ARR) / (Total ARR) | > 25% = high risk | Flag buyer in data room |
| **Change-of-Control Exposure** | (ARR with COC clauses) / (Total ARR) | > 15% = material risk | Require buyer consent or holdback |
| **Termination for Convenience Exposure** | (ARR with annual termination rights) / (Total ARR) | > 30% = elevated churn risk | Disclose prominently |
| **Non-Assignable % | (ARR non-assignable) / (Total ARR) | > 5% = operational risk | Need consent letters pre-close |

---

## Negotiation Tactics by Risk Level

### **CRITICAL Risks** (e.g., largest customer can terminate on acquisition)

**Option A: Get Customer Consent Pre-LOI**
```
Dear [Customer],

We are exploring strategic opportunities to accelerate growth. We want to ensure continuity of our service to you. 

Could we schedule a call to discuss your comfort with potential new ownership structures? Our goal is for this change to be seamless for you.

[Customer says YES] → Get written consent to assignment + waiver of change-of-control
```

**Option B: Buyer Accepts As-Is (Not Recommended)**
If customer is huge and we can't get consent, buyer must accept contract risk. Usually requires:
- Holdback/escrow = 6 months of customer fees
- Buyer indemnity = seller liable if customer terminates within 12 months
- Customer success plan = buyer commits $X to win back customer if dissatisfied

**Option C: Exclude from Sale**
Offer to keep that customer contract yourself (very rare, complicated).

### **HIGH Risks** (e.g., change-of-control + approval required, but medium-sized customer)

Get customer consent ASAP. Template email:

```
Dear [Customer],

As we grow, we're exploring partnerships with strategic investors/acquirers. We wanted to give you a heads-up and confirm you'd be comfortable with new ownership. 

Importantly, [NEW OWNER] is deeply committed to [your use case]. We'll maintain 100% service continuity, and you'll have direct access to [resource].

Can we schedule a 20-minute call to discuss this?
```

When they say yes → send formal assignment + consent letter to sign.

### **MEDIUM Risks** (e.g., change-of-control clause but customer is small or contract ending soon)

Disclose to buyer but don't need proactive customer consent. Let buyer's legal team address in due diligence.

### **LOW Risks** (standard terms)

No action needed. Include in data room.

---

## Red Flags to Watch For

| Clause | Impact | Action |
|---|---|---|
| "Services may not be transferred without written consent" | Buyer needs permission to serve customer | Get consent letter ASAP |
| "If acquired, customer may terminate for free" | Customer can leave post-acquisition | Customer consent required or escrow |
| "Pricing may increase post-acquisition" | You can't raise prices after sale | Buyer incentive to churn (bad) |
| "Automatic termination on change of control" | Customer leaves automatically | CRITICAL — must get written waiver |
| "Termination fee = full refund if < 1 year" | Customer can get money back | Holdback needed for short-contract customers |
| "Master Services Agreement + SOW" | If MSA has bad COC clause, all SOWs affected | Review MSA only, not 100 SOWs |
| "Most Favored Nation" clause | Customer tied to best pricing you offer | Budget for price parity obligations |

---

## Audit Checklist

- [ ] Collected ALL customer contracts (check email, Box, Salesforce, legal folder)
- [ ] Each contract row completed with all 12 fields
- [ ] Risk level assigned (LOW/MEDIUM/HIGH/CRITICAL)
- [ ] Concentration metrics calculated
- [ ] Change-of-control exposure % calculated
- [ ] CRITICAL risks identified and mitigation plan assigned
- [ ] Shared with M&A advisor / lawyer
- [ ] Customer consent letters prepared for HIGH/CRITICAL risks
- [ ] Summary page ("Summary" tab) created for buyer data room
- [ ] Sent to buyer's legal team in LOI phase

---

**Pro Tip:** Don't stress about every contract. Most SaaS contracts have boilerplate change-of-control clauses that don't create real risk. Focus on (1) largest customers, (2) oldest/manually-negotiated contracts, and (3) any contract signed by a lawyer (smells like real teeth).**
