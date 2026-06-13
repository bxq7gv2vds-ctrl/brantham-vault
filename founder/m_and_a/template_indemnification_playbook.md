---
name: indemnification_playbook
description: Escrow, reps & warranties, indemnity caps, clawbacks (founder protection guide)
metadata:
  type: decision
  created: 2026-06-13
  effort: 15min
---

# Indemnification Playbook — How to Protect Your Deal

**Objectif :** Comprendre escrow mechanics, indemnity caps, survival periods, et négocier en position de force.

---

## Tier 1: Core Indemnification Concepts

### What is Indemnification?

**Simple:** Buyer claims you lied (or omitted truth) about the business. You pay damages (or escrow covers it).

**Example:**
```
You: "No pending customer churn"
Buyer (post-close): "Actually, $50k ARR just churned"
Buyer's remedy: Sue you for $50k + lost future value

YOUR HEDGE = Escrow (held in neutral account for 12-18 months)
```

---

## Tier 2: Escrow Mechanics (Your Protection)

### Standard Structure: 3-Tranche Model

| Component | % of Deal | Duration | Risk to Founder |
|-----------|-----------|----------|-----------------|
| **Cash at Close** | 70% | Immediate | None (you get this) |
| **Escrow Hold** | 20% | 12-18 months | 🟡 At risk if buyer claims |
| **Earnout** | 10% | 12-24 months | 🟡 At risk if you miss targets |

**Example: $10M deal**
```
At Close:      $7.0M cash → You
Escrow Hold:   $2.0M in account (buyer can draw if reps broken)
Earnout:       $1.0M (over 12 months, if targets hit)

Your real guaranteed: $7.0M + (up to) $3.0M = $10M
```

### Escrow Claim Process

1. **Buyer discovers breach** (e.g., IP issue, customer contract misrepresentation)
2. **Buyer submits claim** to escrow agent (30 days post-discovery window)
3. **You contest** (you have 30 days to respond; most claims get 50-50 split)
4. **Escrow holds** during dispute (can take 6-12 months)
5. **Settlement or arbitration** (rarely goes to full court)

**Key point:** Escrow agent is neutral; they hold funds, don't judge disputes.

---

## Tier 3: Reps & Warranties — What You're Liable For

### Seller's Standard Reps (What Buyer Protects Against)

| Rep | What It Means | Risk Level | How to Negotiate |
|-----|--------------|-----------|-----------------|
| **Authority & Power** | You own the company & can sell it | ✅ Low | Standard; almost no one contests |
| **Financial Statements** | Accuracy + GAAP compliant | 🔴 High | Ask buyer to audit pre-close |
| **IP & Trademarks** | You own tech, no open-source violations | 🔴 High | Do IP audit; disclose ambiguous areas |
| **Contracts** | All customer/vendor contracts disclosed | 🟡 Medium | Ask for escrow retention on clause disputes |
| **Compliance** | GDPR, CCPA, SOC2, no data breaches | 🟡 Medium | Disclose all prior breaches upfront |
| **Litigation** | No pending lawsuits | 🔴 High | Disclose all threatened claims |
| **Employees** | No wrongful termination, no wage disputes | 🔴 High | Clear departures 6+ months pre-sale |
| **No Material Adverse Changes (MAC)** | No major negative events since signing LOI | 🟡 Medium | Negotiate narrow MAC definition |

---

## Tier 4: Indemnity Caps (Your Negotiation Framework)

### Standard Cap Structure

```
Basket (Threshold):    $100k — claims < $100k are ignored
                       (you don't reimburse for small issues)

Individual Cap:        $500k — single claim can't exceed $500k
                       (one customer churn issue ≠ owed $10M)

Aggregate Cap:         $2M (example) — total escrow is $2M
                       (even if multiple claims, max is escrow balance)

Survive Period:        12 months (most reps) / 18 months (tax reps)
                       (after 12mo, buyer can't file new claims)
```

### Negotiation Strategy

**PUSH FOR:**
```
Basket: $250k (not $100k) — avoids nuisance claims
Individual Cap: $1M (not $500k) — reasonable single-claim limit
Aggregate Cap: 20% of deal (not 15%) — more escrow relief
Survive Period: 12 months (not 18) — reps expire faster
Materiality Scrape: If multiple claims > $2M, raises basket/cap
```

**PUSH BACK ON:**
```
❌ "Reps survive for 24+ months" → Standard is 12-18mo
❌ "Indemnity cap = 50% of deal" → Excessive; 15-20% is market
❌ "Materiality scrape" without threshold → Allows buyer to stack claims
❌ "IP reps survive for 3+ years" → Too risky; 18mo max
```

---

## Tier 5: Clawbacks (Post-Earnout Risks)

### Clawback Definition

**If you miss earnout milestones, buyer can claw back escrow funds.**

**Example:**
```
Earnout target: $10M ARR by M12
Your performance: $8.5M ARR
Shortfall: $1.5M

Buyer triggers clawback: Escrow releases $1.5M to buyer instead of to you
Your escrow relief: $500k instead of $2M
```

### Clawback Protection

**Standard framework:**
```
Tier 1 (100-90% of target): 0% clawback (full earnout)
Tier 2 (89-80%):           25% clawback
Tier 3 (79-70%):           50% clawback
Tier 4 (<70%):             100% clawback (lose it all)
```

**NEGOTIATE FOR:**
```
✅ "No clawback if shortfall < $250k" (materiality threshold)
✅ "Force majeure carve-out" (macro downturn, key customer loss doesn't trigger)
✅ "Shared risk model" — if buyer makes cost cuts that hurt revenue, clawback reduced
✅ "Earnout-only" structure — reps & warranties indemnity ≠ earnout clawback
```

---

## Tier 6: Survival Periods (Rep Expiration)

### Rep Survival Timeline

| Rep Type | Expires | Strategy |
|----------|---------|----------|
| **Standard (Financial, Contracts, Employees)** | 12 months | Let them expire; claim risk drops post-M12 |
| **Tax Reps** | 18 months | Tax audits take time; accept longer survive |
| **IP Reps** | 18 months | IP claims can surface late; costly to fight |
| **Litigation/Compliance** | 24 months | Lawsuits filed later; push back to 18mo |
| **Environmental/Hazmat** | 36+ months | Only if applicable; usually not for SaaS |

**Negotiation play:**
```
Buyer asks: "IP reps survive 36 months"
You counter: "No — 18 months standard. We'll keep limited escrow for IP after that (3% of deal)."
Result: Escrow fully released at M18 except IP reserve ($300k held until M36, then released).
```

---

## Tier 7: Pre-Close Indemnity Checklist

### Due Diligence (Avoid Claims)

- [ ] **Financial Audit** — Get external auditor to review FY-2, FY-1 financials (costs $20-40k, prevents buyer disputes)
- [ ] **IP Audit** — Confirm no open-source license violations (GPL, Apache, MIT compliance)
- [ ] **Customer Contract Review** — Verify no unusual payment terms, auto-renewal traps, termination for convenience clauses that let them leave post-close
- [ ] **Employee Review** — Confirm no wrongful termination pending, all severance paid, NDAs signed, no vesting cliffs within 12 months
- [ ] **Litigation Hold** — Search emails for "lawyer," "lawsuit," "claim" (past 3 years) to surface hidden threats
- [ ] **Compliance Checklist** — GDPR, CCPA, HIPAA, SOC2 status (get certifications pre-close)
- [ ] **Data Breach History** — Disclose all incidents (even minor), remediation steps
- [ ] **Tax Compliance** — Confirm payroll taxes paid, no back taxes owed, sales tax collected properly

### Disclosure Schedule (Your Safety Net)

```
DISCLOSURE SCHEDULE

Section 1: Litigation
- [List any pending/threatened lawsuits, even threatened ones]
- If empty, write "None known to seller"

Section 2: IP
- Open-source inventory
- Any contested IP (patents, trademarks, domain names)

Section 3: Customer Contracts
- List contracts with auto-renewal, termination for convenience, unusual terms

Section 4: Employee
- Any departures in past 12 months with contested claims
- Pending severance disputes

Section 5: Compliance
- Data breaches (dates, scope, remediation)
- GDPR/CCPA requests (frequency, patterns)
- SOC2 audit status & findings

[More detailed than you think necessary = fewer buyer claims post-close]
```

**Strategy:** Over-disclose. Buyer already suspicious; hidden info = clawback trigger. Disclosed = protected.

---

## Tier 8: Dispute Resolution (How Claims Get Settled)

### Dispute Mechanism

| Method | Timeline | Cost | Outcome |
|--------|----------|------|---------|
| **Negotiation (Escrow Agent)** | 30-60 days | $5-20k | 50-50 split common |
| **Mediation** | 60-90 days | $20-50k | Neutral facilitator; non-binding |
| **Arbitration** | 90-180 days | $50-100k | Binding decision; private |
| **Litigation** | 12-24 months | $200k+ | Public; appeals possible |

**Your playbook:**
```
1. If claim < $100k → Negotiate directly (escrow agent facilitates)
2. If claim $100k-$500k → Suggest mediation (saves legal fees)
3. If claim > $500k OR principal breached → Arbitration (faster than court)
4. If buyer makes unreasonable claim → Countersue for bad faith indemnity
```

---

## Tier 9: Negotiation Playbook — Key Phrases

### When Buyer Asks for High Escrow

**Buyer:** "We want 25% escrow for 18 months"

**You (counter):**
> "Market for SaaS is 15-20% for 12 months. Given our financial audit and customer concentration low, 20% / 12 months is fair. Any claims > $500k would be unusual; our reps are strong."

---

### When Buyer Demands High Indemnity Cap

**Buyer:** "Indemnity cap = 30% of deal"

**You (counter):**
> "Buyer already has 18 months to inspect. High cap incentivizes buyer to file nuisance claims. Market is 15-20%; we'll do 20% with materiality basket of $250k."

---

### When Buyer Tries to Tie Earnout to Indemnity Clawback

**Buyer:** "If you miss earnout, indemnity escrow also gets clawed back"

**You (counter):**
> "No. Earnout is separate from indemnity. Earnout covers business performance; indemnity covers misrepresentations. They're independent. Clawback applies to earnout only."

---

## Red Flags (Walk-Away Triggers)

🚩 **Indemnity cap > 30% of deal** → Market is 15-20%; buyer is risk-shifting
🚩 **Reps survive > 18 months** (except tax) → Excessive post-close exposure
🚩 **Materiality scrape** without threshold → Allows buyer to stack small claims into clawback
🚩 **Clawback applies to indemnity** (not just earnout) → Seller bears all risk
🚩 **MAC clause undefined** → Buyer can walk away post-LOI claiming "adverse change"

---

## Post-Close Indemnity Execution

### Month 1-3: Escrow Monitoring

- [ ] Escrow agent sends monthly balance statements (verify accuracy)
- [ ] Track any buyer inquiries about potential claims
- [ ] If buyer hints at claim, immediately engage counsel (pre-emptive response)

### Month 6: Half-Way Review

- [ ] Escrow agent releases any "obvious non-claims" (claims past materiality threshold)
- [ ] Prepare "survival period review" for remaining reps (any imminent expirations?)

### Month 12: Expiration Planning

- [ ] Track survive period expirations (standard = 12mo; tax = 18mo)
- [ ] 30 days before expiration, request escrow release (buyer must file claim by then)
- [ ] After expiration, reps are dead; buyer can't claim

### Month 18: Final Release

- [ ] Last escrow tranche released (unless earnout clawback triggered)
- [ ] Indemnity obligations essentially over

---

## Template: Indemnity Negotiation Summary

```
INDEMNITY TERMS AGREED

Escrow Amount:        $[X] ([X]% of deal)
Escrow Hold Period:   [12] months
Basket (Threshold):   $[250k]
Individual Cap:       $[X]
Aggregate Cap:        [same as escrow]
Materiality Scrape:   If aggregate claims > $[X], basket increases

SURVIVAL PERIODS
Standard Reps:        12 months from close
Tax Reps:             18 months from close
IP Reps:              18 months from close (limited post-18mo reserve: $300k until M24)

CLAWBACK (if earnout applicable)
Tiers:    100-90% = 0% | 89-80% = 25% | 79-70% = 50% | <70% = 100%
Force Majeure:  If ARR down >10% due to macro or buyer cost-cuts, clawback waived

DISPUTE RESOLUTION
Method:   Mediation (30 days) → Arbitration if unresolved
Cost-split: 50-50 unless clear breach

Signed: [DATE]
```

---

**Impact:** Prevents 10-15% of deal value loss to post-close disputes.
