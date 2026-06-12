---
title: Clauses Légales + Earn-out Structure + Reps & Warranties
created: 2026-06-12
category: legal
status: active
---

# Clauses légales + Earn-out + Reps & Warranties essentiels

---

## A. Reps & Warranties : La clé pour limiter votre risque

**Définition** : Déclarations sur l'état de la company. Si faux, vous êtes responsable.

### 1. Reps clés (limite dégâts = cap indemnity at 10-15% de prix)

| Rep | Votre position | Pourquoi important |
|-----||----|
| **Cap table accurate** | Tous propriétaires listés, % correct | Sinon, litige post-deal |
| **Financial statements accurate** | P&L/balance sheet vraies | Risk de restatement |
| **Customer contracts valid** | Tous clients = contrats signés | Sinon, customers peuvent partir |
| **IP owned or licensed** | Code = vous le possédez | Si breach = responsabilité |
| **No material litigation** | Pas de lawsuits pending | Risk de judgment |
| **Compliance** | SOC2, GDPR, taxes à jour | Regulatory fines |
| **Employees/contractors** | Pas d'undisclosed employment issues | Sudden resignations |
| **No material adverse change** | Business stable (no hidden crises) | Catch-all protection |

### 2. Reps que vous rejetez (red flags si acheteur insiste)

- ❌ "Revenue is recurring" (50% obligation?) → trop vague
- ❌ "No material defects" (product?) → trop large
- ❌ "All customers happy" (impossible à prouver)
- ❌ "No future liabilities" (unknowns exist)

### 3. Indemnification cap structure

**Standard deal** :
```
Basket: $100k (don't claim unless damages > $100k)
Cap: 15% of purchase price ($7.5M if price = $50M)
Survival: 18-24 months (reps expire after this)
Escrow: 10-15% of price held for 18 months to cover claims

Clawback: If total indemnity claims exceed cap, 
you pay from escrow + pocket
```

**Pro move** : Negotiate separate cap for:
- **Tax matters** (higher cap = 25%, more risk)
- **IP** (higher cap = 20%, critical)
- **Fraud** (no cap, but difficult to prove)
- **Everything else** (10-15% cap, acceptable)

---

## B. Earn-out Structure (tied to your performance)

### Option 1: Revenue-based (most common)

```
Structure: $60M purchase price
           + $10M earn-out (2 years)
           
Year 1: If ARR reaches $6.2M → earn $3M
        If ARR reaches $6.5M → earn $4M
        If ARR reaches $6.8M+ → earn $5M

Year 2: If ARR reaches $7.8M → earn $2M
        If ARR reaches $8.2M → earn $3M
        If ARR reaches $8.8M+ → earn $5M

Negociation: You want low bar (achievable), 
           acheteur wants high bar (stretch)
           
           Meet 70% way: 15% revenue growth target 
           = reasonable + achievable
```

### Option 2: NRR/retention-based (better for you)

```
Earn-out tied to RETENTION (not new growth = de-risked)

Year 1: Maintain NRR >100% → $3M paid
        Maintain NRR >110% → $4M paid
        Reach NRR >120% → $5M paid

Why better: You control this (product + service).
Acheteur's sales team can't kill earn-out.
```

### Option 3: EBITDA-based (rare, less relevant)

```
Usually applies to profitable companies.
Year 1: If EBITDA > $500k → $2M paid
Year 2: If EBITDA > $1M → $3M paid
```

---

## C. Earn-out pitfalls (watch out!)

🚩 **Trap 1: Earn-out tied to things you can't control**
```
❌ "Earn-out if we hit $100M ARR" 
   (acheteur's sales team is responsible; you're powerless)

✅ "Earn-out if NRR >110% & churn <3%" 
   (you control product + service)
```

🚩 **Trap 2: Earn-out calculation vague**
```
❌ "Good faith efforts to achieve targets"
   (what if they sandbag? no recourse)

✅ "ARR calculated per SaaS standard: MRR × 12, 
   quarterly audited by independent accountant"
```

🚩 **Trap 3: Earn-out forfeiture if you leave**
```
❌ "If you resign, earn-out forfeited"
   (you can't protect your money if relationship sours)

✅ "If you leave for good cause (constructive dismissal), 
   earn-out vests normally. 
   If you leave for no cause, earn-out accelerates 
   to next payout (you get cash immediately)"
```

---

## D. Escrow (holdback) terms

**What** : 10-15% of purchase price held for 18-24 months.  
**Why** : Gives acheteur recourse if you lied (reps not true).

### Negotiate escrow release:

| Timing | Structure | Implication |
|--------|-----------|-------------|
| **12 months** | Better for you (money back sooner) | Acheteur loses leverage faster |
| **18 months** | Standard | Balanced |
| **24 months** | Acheteur leverage (longer hold) | Avoid if possible |

**Pro move** :
```
"We propose 10% escrow (not 15%), released 12 months 
if no claims. You want 15% escrow, 18 month release?

Compromise: 12% escrow, released at:
- 50% at 12 months (if no claims)
- Remaining 50% at 18 months

This way: you get money back on schedule, 
we have time to handle surprises."
```

---

## E. Key clauses to fight for

### Clause 1: Non-shop / Exclusivity termination

**Acheteur wants** : "You can't talk to other buyers"  
**Your position** : "Only after NDA + mutual exclusivity date"

```
✅ "Exclusive discussions for 30 days. 
   If we reach LOI, exclusive for additional 60 days.
   Either party can terminate if major gap not closed."

❌ "Exclusive forever" (trap if negotiations stall)
```

### Clause 2: Closing conditions

**Typical** :
```
- Reps remain true (no material adverse change)
- Financing obtained (buyer's bank approves)
- Regulatory approval (antitrust, if applies)
- Key employees stay (sign employment agreements)
```

**Fight for** : "Financing" should be buyer's risk, not yours.
```
✅ "Buyer has committed financing. If financing falls through, 
   you can terminate and retain $5M break-up fee"

❌ "Buyer will use best efforts to raise financing" 
   (vague, buyer has out)
```

### Clause 3: Confidentiality / Non-compete

**Non-compete** :
- ✅ 1-2 years is reasonable
- ❌ 5 years = too long (restricts your future career)

```
Fair: "Cannot start or work at direct competitor 
      in same product category for 2 years. 
      Exception: can consult (not full-time work) after 1 year."
```

**Non-solicit employees** :
- ✅ 1-2 years OK
- ❌ 3+ years unreasonable (people move)

---

## F. Tax implications (critical!)

### Stock sale vs. Asset sale

| Type | Founder outcome | Tax rate |
|------|-----------------|----------|
| **Stock sale** | Long-term capital gain (if >1y hold) | 20% federal (US) + state |
| **Asset sale** | Ordinary income on some + cap gains | 37% federal + state (worse) |

**For France** :
- **Vente PME** (small cap gains exemption) : 0% to 50% tax (depends structure)
- **Vente holding** : 12.8% (prélèvement forfaitaire)
- **Earn-out** : Traité comme revenu (37.5%) sauf si capital gain

**Action** : Talk to tax lawyer BEFORE signing. Structure matters.

---

## G. Post-deal holdback (what happens if things go wrong)

**Example**: You get $50M price, $10M escrow, $5M earn-out.

```
Day 1: Receive $40M cash in bank
(Acheteur keeps $10M escrow, $5M earn-out)

Month 12: Acheteur discovers you didn't disclose a customer lawsuit
         Claims $2M indemnification
         → Escrow reduced $2M, you lose $2M from escrow release

Month 18: Escrow released (if no additional claims)
         But you already lost $2M
         → Net: $48M, not $50M

Year 2: Hit earn-out targets → $5M paid
        → Total received: $53M (but lost 2 years waiting)
```

**Moral** : Escrow is leverage. Minimize by:
1. Clean reps (no hidden issues)
2. Detailed disclosure (proactive = less surprise)
3. Accurate financial statements

---

## H. Founder stay-on terms (critical if applicable)

**Template if you're staying as CEO**:

```
Title: Chief Product Officer (not just "consultant")
Salary: $500k/year (market rate)
Equity: $2M in acquirer equity (golden handcuffs)
  - Vest over 4 years
  - Accelerate 50% if constructive dismissal

Earn-out bonus: $5M additional if you hit milestones
  - You can't walk away from it (unless they fire you)
  
Runway: 24-36 months integration, then decision
  - After 36 months, can leave + earn-out vests fully

Non-compete waiver: If you leave after 24 months, 
  non-compete doesn't apply (you've paid your dues)
```

---

## Summary: Red flags in SPA (Stock Purchase Agreement)

🚩 **Red flags = walk away** :
- [ ] No dollar cap on indemnification
- [ ] Earn-out tied to things you don't control
- [ ] Non-compete >3 years
- [ ] Escrow clawback undefined
- [ ] Financing contingency (buyer can walk free)
- [ ] Survival period >24 months on reps

✅ **Green lights** :
- [ ] 10-15% indemnity cap
- [ ] NRR/retention-based earn-out
- [ ] 1-2 year non-compete
- [ ] Defined escrow release terms
- [ ] Financing secured (not contingent)
- [ ] 18 month rep survival max
