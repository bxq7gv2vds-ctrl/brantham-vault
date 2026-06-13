---
name: legal-red-flags-vs-fixes
description: Legal issues que un buyer découvrira en DD — impact valuation + fix ou kill
type: playbook
date: 2026-06-13
---

# Legal Red Flags vs. Fixes — Data Room

**Chaque flag a un coût. Calculez-le avant que buyer le découvre.**

---

## TIER 1 : DEAL-KILLERS (Abort or massive discount)

### Flag 1A : IP Ownership Unclear

**Trigger :** Code/patents not clearly owned by your company

```
Example: You hired contractor 5 years ago, no IP assignment agreement
         → Code is partly theirs, partly yours
         → You can't fully warrant tech to buyer
```

**Impact :** -30 to -50% valuation (or deal dies)

**Fix :**
- [ ] Track down contractor → get retroactive IP assignment ($$ settlement)
- [ ] If impossible → disclosure to buyer + representation insurance
- [ ] Timeline: 2-3 weeks (if contractor responsive)

**Cost of fix :** $5k-$50k (contractor buyout) vs. -$500k valuation hit

---

### Flag 1B : Material Litigation Pending

**Trigger :** Any lawsuit that could affect company (employee, customer, IP)

```
Example: Former CTO suing for equity / IP / non-compete violation
         → Buyer can't close until settled or dismissed
```

**Impact :** -40 to -100% valuation (or deal blocked)

**Fix :**
- [ ] Settle lawsuit before LOI
- [ ] If settlement: get dismissal + non-disclosure
- [ ] If ongoing: escrow portion of purchase price for settlement
- [ ] Timeline: 2-8 weeks (litigation slow)

**Cost of fix :** Settlement amount vs. deal dies

---

### Flag 1C : Customer Contracts Have "Change of Control" Clause

**Trigger :** "If acquired, customer can terminate"

```
Example: 3 of your 10 customers have "change of control" exit clause
         → They'll churn post-close
         → Earnout destroyed
```

**Impact :** -20 to -40% valuation (customer loss)

**Fix :**
- [ ] BEFORE LOI: Call those customers, get waiver email ("We're OK with change of control")
- [ ] Add to data room as "Customer Retention Commitments"
- [ ] If customer refuses: negotiate with buyer (they may keep customer incentivized)
- [ ] Timeline: 1 week (urgent)

**Cost of fix :** $0 (just ask) or discount to retain them

---

### Flag 1D : Regulatory / Compliance Violation

**Trigger :** GDPR, CCPA, SOC2, healthcare law violations

```
Example: You process EU user data, have no Data Processing Agreement
         → GDPR violation = €20M fine
         → Buyer liable post-acquisition
```

**Impact :** -50 to -100% valuation (or deal dies)

**Fix :**
- [ ] Audit NOW (hire compliance lawyer)
- [ ] Remediate violations before LOI
- [ ] Get SOC2 / attestation if missing
- [ ] Document all compliance (data rooms)
- [ ] Timeline: 4-8 weeks (long, but essential)

**Cost of fix :** $10k-$50k (audit + fixes) vs. deal dies

---

## TIER 2 : MAJOR (Significant discount)

### Flag 2A : Material Contracts Expiring Soon

**Trigger :** Key vendor/supplier contract expires in next 12 months

```
Example: Cloud hosting contract at $50k/year expires in 6 months
         → No renewal terms agreed
         → Buyer worried: hosting cost might 3x
```

**Impact :** -10 to -20% valuation

**Fix :**
- [ ] Negotiate renewal BEFORE LOI (lock in rates)
- [ ] Get LOI from vendor confirming rates
- [ ] Add to data room: "Material Contracts Schedule"
- [ ] Timeline: 2-4 weeks

**Cost of fix :** $0 (just negotiate) or 5-10% rate increase to lock in

---

### Flag 2B : Employee IP Assignment Missing

**Trigger :** Early employees never signed IP assignment (common at small startups)

```
Example: Your CTO wrote core algorithm, no IP assignment agreement
         → Technically CTO could claim ownership
```

**Impact :** -5 to -15% valuation (representation insurance costs)

**Fix :**
- [ ] Get retroactive IP assignments from all employees (sign letters)
- [ ] If employee refuses: higher representation insurance
- [ ] Add to data room: "IP Assignment Agreements Schedule"
- [ ] Timeline: 1-2 weeks

**Cost of fix :** $0 (employee usually signs) vs. $20k-$100k insurance premium

---

### Flag 2C : Tax Issues (Unpaid Taxes, Disputes)

**Trigger :** Unpaid payroll taxes, state sales taxes, IRS disputes

```
Example: You didn't file sales tax for 2 years (small revenue)
         → State can audit, assess penalties
         → Buyer liable post-acquisition
```

**Impact :** -10 to -30% valuation

**Fix :**
- [ ] Audit tax compliance NOW (hire CPA)
- [ ] File all missing returns (accept penalties if necessary)
- [ ] Get IRS/state clearance letters
- [ ] Timeline: 4-12 weeks (can be slow)

**Cost of fix :** Back taxes + penalties ($5k-$50k) vs. -10% valuation

---

### Flag 2D : Shareholder / Cap Table Issues

**Trigger :** Unclear share ownership, missing signature, founder equity dispute

```
Example: You have 80% equity but co-founder disputes (says 50/50 verbal)
         → Deal blocked until resolved
```

**Impact :** -10 to -50% valuation (dispute settlement)

**Fix :**
- [ ] Get legal opinion: clear ownership
- [ ] If dispute: settle with co-founder (mediation, buyout, or split proceeds)
- [ ] Get signed consent from all shareholders for sale
- [ ] Timeline: 2-6 weeks (mediation can drag)

**Cost of fix :** $10k-$100k settlement vs. deal dies

---

### Flag 2E : Customer Data Privacy Issues

**Trigger :** Customer data not encrypted, backup practices weak

```
Example: Customer PII stored in plain text, no backups
         → Breach risk = liability
         → Buyer's insurance underwriters will balk
```

**Impact :** -5 to -20% valuation

**Fix :**
- [ ] Implement encryption at rest / in transit (2-4 weeks)
- [ ] Document backup / disaster recovery plan
- [ ] Get third-party audit (SOC2 if feasible)
- [ ] Timeline: 2-8 weeks

**Cost of fix :** $5k-$20k (engineering + audit) vs. -10% valuation

---

## TIER 3 : MINOR (Negotiable, small discount)

### Flag 3A : Intellectual Property Not Registered

**Trigger :** Trademark / Patent / Copyright not formally registered

```
Example: Your product name is famous but trademark not registered
         → Someone could steal it post-acquisition
```

**Impact :** -2 to -5% valuation

**Fix :**
- [ ] File trademark / patent within 30 days of LOI
- [ ] Cost: ~$2k per filing
- [ ] Buyer may wait for registration or indemnify
- [ ] Timeline: 1 week to file, 6 months to register

**Cost of fix :** $2k-$5k (filing) vs. -2% valuation

---

### Flag 3B : Vendor Contracts Lack NDA / Confidentiality

**Trigger :** Vendor could claim trade secret / customer list is theirs

```
Example: You use OpenAI API, no NDA that restricts them from seeing data
         → Not a deal-killer but flag
```

**Impact :** -0 to -5% valuation (representation insurance)

**Fix :**
- [ ] Review critical vendor contracts (3-5 agreements)
- [ ] Add NDA / data confidentiality clauses if missing
- [ ] Document in data room
- [ ] Timeline: 1 week

**Cost of fix :** $0 (vendor usually agrees) vs. $5k insurance

---

### Flag 3C : Employment Agreements Lack Non-Compete / Non-Solicit

**Trigger :** Employees free to compete or solicit customers post-sale

```
Example: Your engineer leaves post-close, starts competing company
         → Takes customers with him
```

**Impact :** -0 to -5% valuation

**Fix :**
- [ ] Get signed non-competes + non-solicits from all key employees (1 year standard)
- [ ] Do BEFORE LOI (post-LOI is awkward)
- [ ] Timeline: 1 week

**Cost of fix :** $0 (standard clause) or $5k legal review

---

## Pre-Close Audit Checklist

### IP
- [ ] All code/patents/trademarks clearly owned by company (no contractor ambiguity)
- [ ] All employees signed IP assignments
- [ ] All vendor contracts allow use of their tech/services in context of sale

### Contracts
- [ ] All material customer contracts reviewed (no hidden "change of control" clauses)
- [ ] All vendor contracts reviewed (no surprise termination clauses)
- [ ] Employment agreements have non-compete / non-solicits

### Compliance
- [ ] Tax returns filed and up-to-date
- [ ] No pending tax disputes
- [ ] GDPR / CCPA / SOC2 audit completed (if applicable)
- [ ] No regulatory violations

### Litigation
- [ ] No pending lawsuits (or settled)
- [ ] No IP disputes
- [ ] No employee disputes

### Equity
- [ ] Cap table clear (no disputes)
- [ ] All shareholders will sign consent to sale

---

## Disclosure Strategy

**If you find a flag, disclose PROACTIVELY:**

```
Buyer: "Any legal issues we should know about?"
You: "Yes. [Flag]. Here's the issue and here's how we fixed it."

vs.

Buyer discovers flag in DD:
You: "We were going to mention that..."
→ Buyer thinks you hid it, deal at risk
```

**Proactive disclosure = -5 to -10% valuation**
**Discovered later = -20 to -50% valuation**

---

## Budget: Pre-Closing Legal

```
Item                          Cost        Timeline
════════════════════════════════════════════════════
Compliance audit (if needed)   $10k–$50k   4-8 weeks
IP assignment review           $2k–$5k     2-3 weeks
Contract review (20 docs)      $5k–$15k    2-4 weeks
Cap table audit                $1k–$3k     1 week
Litigation/dispute search      $0–$10k     1-2 weeks
Representation insurance       $20k–$100k  1-2 weeks (post-LOI)
────────────────────────────────────────────────────
TOTAL BUDGET                   $38k–$183k  4-8 weeks
```

**Start now, not when buyer appears.**

