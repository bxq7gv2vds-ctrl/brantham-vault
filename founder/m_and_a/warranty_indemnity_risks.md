---
name: warranty-indemnity-risks
description: Représentations et warranties — ce qu'on disclose, caps, holdbacks
metadata:
  type: guide
  created: 2026-06-12
---

# Warranty & Indemnity Risk Guide — What You're Liable For

Use this during LOI term sheet negotiation. Warranties = promises about company. Breaches = you pay.

---

## The Setup

**Representation & Warranty (Reps)**: You promise "X is true about our company."

**Indemnification**: If you lied about X, you pay buyer damages.

**Escrow / Holdback**: Buyer keeps $[X] of sale proceeds as security, releases after 12-18 months if no breaches found.

---

## Common Reps & Your Risk Level

### Rep 1: Financial Statements are Accurate ⚠️ HIGH RISK

**What buyer needs:**
```
"Your last 2 years of P&L / BS / CF are accurate and complete."
```

**Your exposure:**
- If revenue overstated by 5% → Buyer asks for $[X]M refund
- If hidden debt → Escrow claim
- If inventory/receivables misstated → Liability

**What to do:**
- Get accountant to review (not just "compiled" statements)
- Disclose any estimates or one-time items upfront
- Have "normalizing adjustments" doc ready (explain differences)

**Negotiating the rep:**
```
Your version:
"Financial statements fairly present, in all material respects, 
consistent with past practice and accounting methods."

Add carve-outs:
"Except as disclosed in [Schedule X], or items consistent with 
ordinary course of business, or disclosed to buyer prior to LOI."
```

---

### Rep 2: Contracts with Customers (No Hidden Terms) ⚠️ HIGH RISK

**What buyer needs:**
```
"Customer agreements are as shown in data room. 
No hidden discounts, side letters, or special terms."
```

**Your exposure:**
```
Example: You told buyer top customer pays $1M/year.
Reality: You've promised 50% discount next renewal (secret side letter).
Buyer finds out → Indemnification claim for $[X]M (estimated loss).
```

**What to do:**
- Audit all customer agreements for:
  - Undisclosed discounts
  - Side letters or email "commitments" (get in writing)
  - Verbal promises (document them)
  - Price locks / escalation caps that aren't in main contract

**Negotiating the rep:**
```
Your version:
"Customer agreements are as provided to buyer. 
No material side letters except [List any known exceptions]."

Add carve-out:
"Ordinary course amendments, price increases consistent with contract terms."
```

---

### Rep 3: No Pending Litigation / Claims 🔴 CRITICAL

**What buyer needs:**
```
"No lawsuits, regulatory investigations, IP disputes, 
or claims that might affect company value."
```

**Your exposure:**
```
Example: Employee discrimination claim (settled confidentially).
If buyer discovers → Full indemnification for full claim amount + legal fees.
```

**What to do:**
- Audit with employment lawyer:
  - Any terminated employees threatening suit
  - Any wage/hour complaints
  - Any workplace discrimination / harassment claims
  
- Audit with IP lawyer:
  - Any patent challenge letters received
  - Any "cease and desist" demands
  - Any employee IP disputes

**Negotiating the rep:**
```
Your version:
"No pending litigation except [List known minor items: 
$X customer dispute, small contract disagreement].
No claims we're aware of would be material."

Define "material":
"Material = claim > $[X] or affecting >1% of revenue."
```

---

### Rep 4: Intellectual Property — You Own It All ⚠️ HIGH RISK

**What buyer needs:**
```
"Your code, patents, trademarks are owned by company, not co-founder's 
previous employer, not open-source, not co-created."
```

**Your exposure:**
```
Example: Engineer was hired from BigTech, brought code from prior role.
BigTech sues for IP theft → Buyer sues you for indemnification ($[X]M).
```

**What to do:**
- Audit all code / patents:
  - Run code scan (FOSSA, Black Duck) for unlicensed open-source
  - Check all engineer IP assignments are signed
  - Check any contractor agreements have IP assignment
  - Check founding code wasn't "inspired by" previous employer
  
- Get legal opinion: "IP audit clean" letter (shows diligence)

**Negotiating the rep:**
```
Your version:
"Company owns / controls all IP as disclosed. 
We have reviewed all code for open-source dependencies listed in [file].
We have secured all necessary licenses and IP assignments."

Exception:
"Except as disclosed on [Schedule X - List any concerns]."
```

---

### Rep 5: Compliance with Laws & Regulations ⚠️ MEDIUM RISK

**What buyer needs:**
```
"No violations of labor law, tax law, data privacy, 
environmental regs, securities law, etc."
```

**Your exposure:**
```
Example: You haven't filed sales tax in California (nexus).
Buyer discovers $[X]K liability → Indemnification claim.
```

**What to do:**
- Compliance checklist:
  - [ ] Sales tax: Registered in all states where you have nexus?
  - [ ] Payroll tax: All filings current? No penalties?
  - [ ] Income tax: Returns filed, no liens?
  - [ ] GDPR: If EU customers, processing compliant?
  - [ ] CCPA: If California customers, handling data correctly?
  - [ ] Labor: No wage/hour violations, independent contractor misclassifications?

**Negotiating the rep:**
```
Your version:
"Company in material compliance with all applicable laws.
Any non-material issues disclosed in [Schedule X].
Material = issue creating liability > $[X]."
```

---

### Rep 6: No Employee Commitments Beyond What's Documented

**What buyer needs:**
```
"No oral promises to employees (equity, bonuses, retention agreements) 
that aren't in writing."
```

**Your exposure:**
```
Example: You promised CTO "double equity if we stay through year 1 post-close."
Email only, not in offer letter.
CTO is now an issue, buyer wants indemnification.
```

**What to do:**
- Audit all employee agreements:
  - [ ] Employment agreements signed by all employees
  - [ ] Offer letters state equity, equity vesting, bonus structure
  - [ ] Any retention bonuses documented + disclosed to buyer
  - [ ] Any deferred compensation written down
  - [ ] Founders: vesting schedules in writing

**Negotiating the rep:**
```
Your version:
"Employment agreements with all personnel are as provided. 
No material undisclosed promises regarding compensation, equity, 
or other benefits except [List any known exceptions]."
```

---

### Rep 7: No Material Adverse Change (MAC)

**What buyer needs:**
```
"No events have occurred that materially hurt company value."
```

**Your exposure:**
```
This is vague, buyer-friendly. Avoid accepting.
```

**Negotiating the rep (PUSH BACK HARD):**
```
Don't accept: "No material adverse change in any respect."

Counter: "No material adverse change, meaning:
  - Single event causing >10% revenue loss
  - Customer concentration change >20 points
  - Key person departure
  
Specifically excludes:
  - Market-wide recession
  - Industry downturns
  - Changes that don't affect buyer's synergies"
```

---

## Caps & Baskets (Limit Your Liability)

### Basket (Threshold Before You Pay)

**Standard**: Buyer won't bother escrow claim if <$[X].

```
Example:
  Escrow: $2M
  Basket: $50K
  
  Means: Buyer must have $50K+ in claims before 
         you have to pay anything from escrow.
```

**Negotiate this**:
- High basket (better for you): $100K or 1% of purchase price
- Low basket (buyer wants): $10K or 0.5%
- Compromise: $50K or 0.75%

### Cap (Maximum You Pay)

**Standard**: You won't pay more than [X].

```
Example:
  Escrow: $2M (10% of deal size)
  Cap on reps: $2M
  
  Means: Even if buyer claims $10M in damages,
         max you pay from escrow is $2M.
```

**Negotiate this**:
- Standard: Cap = Escrow amount (so you're protected)
- Buyer wants: Cap = [Higher, 25% of deal]
- Compromise: Cap = Escrow amount + [small additional amount]

### Survival Period (How Long Buyer Can Claim)

**Standard**: Most reps survive 12-18 months, some longer.

```
Timeline:
  Close: June 2026
  Survival: 18 months = Dec 2027
  
  After Dec 2027, buyer can't claim on escrow
  (unless specific claims like indemnification taxes, IP)
```

**Negotiate this (shorter is better for you)**:
- 12 months = good (buyer has 1 year to find issues)
- 18 months = standard
- 24 months = bad (too long, buyer can delay)
- Exceptions (longer survival):
  - Tax reps: 3-5 years (tax authorities can audit)
  - IP reps: 3-5 years (patent suit can take time)
  - Environmental: 3-5 years (liability long-tail)

---

## Common Reps to Dispute Early

### Dispute 1: "No IP Infringement from Third Parties"

**Buyer wants**: "Your product doesn't infringe any third-party IP."

**Why this is unfair**: Patent trolls could sue anyone.

**Your counter**:
```
"Company has not received notice of infringement. 
Company not aware of any infringement.
Except for non-material uses of open-source [as disclosed]."
```

### Dispute 2: "All Employees Have Signed IP Assignments"

**Buyer wants**: 100% of employees.

**Reality**: You probably have 1-2 employees without signed docs.

**Your counter**:
```
"All employees except [list employees] have signed IP assignments.
For [those employees], we assert work-for-hire and common-law 
assignment under [jurisdiction] law."
```

### Dispute 3: "No Product Liability Claims"

**Buyer wants**: Your product never harmed anyone.

**Why this is unfair**: One angry customer could claim anything.

**Your counter**:
```
"No known product liability claims. 
No claims asserted in writing that we're aware of.
Material only if claim > $[X]."
```

---

## Indemnification Carve-Outs (What You DON'T Have to Pay For)

**These should be IN the agreement**:

```
Seller does not indemnify buyer for:

1. Buyer's integration failures
   (e.g., "we integrated your code wrong")

2. Market conditions
   (e.g., "recession killed your revenue")

3. Buyer's operational decisions
   (e.g., "we cut your team, product quality fell")

4. Changes in law
   (e.g., "GDPR compliance became stricter")

5. Buyer's technology/products
   (e.g., "our legacy system has bugs")

6. Third-party technology
   (e.g., "AWS went down")
```

**Push for**: Explicit carve-outs for any known risk area.

---

## Escrow Mechanics (How the Holdback Works)

### Standard Escrow Structure

```
Deal: $20M purchase price
Escrow holdback: 10% = $2M
Buyer controls escrow, you can't touch it.

Timeline:
  Close: June 2026
  Surviving period: June 2026 - Dec 2027 (18 months)
  
  December 2027:
    - If NO claims: $2M released to you
    - If claims: Disputed amount held back, rest released
    - If claims substantiated: Amount paid to buyer from escrow
```

### Negotiating Escrow Terms

**Better for you**:
- Shorter hold period (12 months vs. 18)
- Lower escrow % (7-8% vs. 10%)
- Seller's representative to defend claims (not buyer dictates)
- Basket (threshold) applies per-claim AND in aggregate
- Claims must be asserted in writing with specific damages

**Ask for**:
```
"Escrow of 7% for 12 months. Claims must be 
asserted in writing before December [date], 
with documentation of damages. Seller's counsel 
can defend. Buyer must mitigate damages."
```

---

## Checking Your Exposure: Red Flags

### RED FLAG 1: Reps Survive >24 Months
**Issue**: You'll be in escrow jail for 2+ years.
**Action**: Push back. 18 months MAX for most reps.

### RED FLAG 2: Cap = 50% of Purchase Price
**Issue**: If escrow is $2M, but cap is $10M, you're exposed beyond escrow.
**Action**: Ensure cap = escrow amount.

### RED FLAG 3: "Buyer Can Claim Anything as Indemnification"
**Issue**: Buyer will try to shift integration failures to you.
**Action**: Explicit carve-outs for buyer's actions, market conditions.

### RED FLAG 4: No Basket Threshold
**Issue**: Buyer will claim $1K issues, nickel-and-dime you.
**Action**: Insist on basket ($50K+).

### RED FLAG 5: Reps Are Broad & Undefined
**Issue**: "No material adverse change" is buyer-friendly, vague.
**Action**: Define "material" (>$X, >Y% of revenue, etc.).

---

## Reps Checklist: What to Disclose Upfront

Pre-emptively disclose (shows good faith):

- [ ] Any customer concentration issues (top customer = X% of revenue)
- [ ] Any customer churn risk (customer X considering leaving)
- [ ] Any employee issues (recent termination, threat of litigation)
- [ ] Any IP concerns (open-source dependencies, engineer from competitive firm)
- [ ] Any regulatory issues (sales tax gap, GDPR compliance pending)
- [ ] Any pending claims (even small ones)
- [ ] Any undisclosed side agreements (price discounts, special terms)

**Why**: If you disclose, you get protection (reps exclude disclosed items).

---

## Quick Negotiation Script

**When buyer proposes aggressive reps:**

```
Buyer: "We need strong reps for comfort. 
       The usual cap is 25% of purchase price."

You: "I understand. Let me propose:
     - 10% escrow (standard for SaaS acquisitions)
     - 12-month survival for most reps
     - Specific cap = 10% = escrow amount
     - $50K basket to avoid noise
     - Explicit carve-outs for buyer actions, market conditions
     
     This protects us both:
     - You have $2M cushion for legitimate claims
     - I'm not exposed to speculative damages
     - We can close faster if we agree now."
```

---

## Template: Your Reps Position (One Page)

**Share with buyer early (Week 2-3 of diligence):**

```
SELLER'S REPRESENTATIONS POSITION

Standard Reps (12-month survival):
✓ Financial statements accurate
✓ Customer contracts as shown (no side agreements)
✓ IP owned / controlled as disclosed
✓ Compliance with laws (material breaches >$X)
✓ Employees properly documented

Carve-Outs (we're not liable):
✗ Buyer's integration failures
✗ Market conditions (recession, industry downturns)
✗ Buyer's team reductions affecting product
✗ Changes in law post-closing
✗ Third-party technology issues

Escrow: 10% for 12 months, then released
Cap on indemnification: 10% (= escrow)
Basket: $50K per claim, $100K aggregate

Special Items (longer survival):
- Tax matters: 3 years (standard for M&A)
- IP infringement: 3 years (patent suits take time)
- Environmental: 3 years (if applicable)
```

---

## Use Case

Before LOI: Share this guide with your lawyer. Identify your key risks, prepare defenses. Before signing: Confirm escrow amount, cap, survival periods are reasonable.
## Related
## Related
## Related
## Related
