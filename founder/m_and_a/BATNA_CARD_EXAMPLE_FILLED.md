---
name: batna-card-example-filled
description: Exemple rempli. BATNA = ton prix plancher. Utilisé en négociation secrètement.
metadata:
  type: decision
---

# BATNA CARD — EXAMPLE FILLED (SaaS Founder)

**What is this?** Your walk-away price + reasoning. Confidential. Used internally only. 
If deal <BATNA price, you stay independent.

**How to use:** Fill in blanks below with YOUR numbers. Store in encrypted vault (not Slack).

---

## CONTEXT

**Company:** TechFlow Analytics (hypothetical)  
**Current State:** $3M ARR, 40% YoY growth, 115% NRR, 18-person team  
**Filled by:** CEO + CFO  
**Date:** 2026-06-12  
**Valid through:** 2026-09-12 (quarterly refresh)

---

## OPTION A: STAY INDEPENDENT (Next 3 Years)

**Assumption:** Keep building, grow organically, no outside funding.

| Year | ARR | EBITDA (25% margin) | Owner's distributions | Notes |
|------|-----|---------------------|----------------------|-------|
| Y0 (2026) | $3M | $750k | $300k | Base case (no major investment) |
| Y1 (2027) | $4.5M (50% growth) | $1.125M | $450k | Hire 5 more, scale marketing |
| Y2 (2028) | $6.75M (50% growth) | $1.69M | $675k | Team reaches 28 people, ops mature |
| Y3 (2029) | $10M (48% growth) | $2.5M | $1M | Stable >$10M ARR business |

**3-Year Cumulative Owner Distributions:** $300k + $450k + $675k + $1M = **$2.425M**

**Plus:** You own 100% equity (no dilution). Business is yours, optionality is yours.

---

## OPTION B: RAISE VENTURE (Series B)

**Assumption:** Raise $5M at $20M valuation (25% dilution).

| Year | ARR | Ownership % | Owner's % of EBITDA | Your distribution |
|------|-----|-------------|---------------------|-------------------|
| Y1 | $5M | 75% | $375k | $375k |
| Y2 | $8M | 75% | $600k | $600k |
| Y3 | $12M | 75% | $900k | $900k |

**3-Year Owner Distributions:** $375k + $600k + $900k = **$1.875M**

**Problem:** $5M burn, team bloats, pressure to scale fast. Optionality is now board's, not yours.

---

## OPTION C: SELL TODAY

**Fair valuation estimate:**
- ARR: $3M
- Growth rate: 40% YoY
- Multiple: 10-12× (for 40% growth)
- **Fair value:** $30-36M (let's say $33M midpoint)

**Deal structure assumption:**
- 80% cash at close: $26.4M
- 20% earnout over 3 years: $6.6M
- Founder stay bonus: $1M (vesting: 36 months)

**Your take-home:**
- Cash at close: $26.4M (minus tax, minus legal fees ~$500k): **~$20M net**
- Earnout (if hit): $6.6M (minus tax): **~$5M net**
- Stay bonus: $1M: **$1M**
- **Total realized:** ~$26M (3-year window)

---

## BATNA CALCULATION

**Decision Framework:**

```
If deal offer < BATNA, I stay independent. If deal offer > BATNA, I consider it.

BATNA = max of:
  A) NPV(stay independent 3 years) + optionality premium
  B) NPV(raise Series B 3 years) (discard this, worse than A)
  C) Implicit value I place on staying independent

NPV(A) = $2.425M + [optionality premium: $5M] = $7.425M
NPV(C) = "I value my independence + my 100% ownership at least $8M"

BATNA price = $8M minimum.

But that's low-ball. Realistic BATNA for founder who has options:
BATNA = Fair value * 0.9 = $33M * 0.9 = $29.7M ≈ $30M
```

---

## YOUR BATNA CARD (Filled)

| Metric | Value | Reasoning |
|--------|-------|-----------|
| **Fair valuation (DCF + comps)** | $33M | $3M ARR × 11× multiple (40% growth) |
| **Confidence in fair value** | High | Based on recent comps: Company A ($30M on $2.8M ARR), Company B ($40M on $3.5M ARR) |
| **Walk-away price (BATNA)** | $26M | 0.8× fair value. Below this, I stay independent. |
| **Anchor price (opening ask)** | $45M | 1.35× fair value. Starting negotiation position. |
| **Acceptable range** | $30-40M | Between fair value and anchor. |
| **Absolute ceiling** | $50M | Above this feels frothy. I wouldn't believe it. |
| **Cash minimum at close** | 75% | Want $26M × 0.75 = $19.5M cash. Rest in earnout/escrow/stock. |
| **Earnout max** | 20% | Won't accept >20% in earnout. Too much risk. |
| **Founder stay requirement** | YES | Must stay 2-3 years in meaningful role (not sidelined). |
| **Post-close ownership** | 2-5% | New equity for staying + hitting earnout. Standard post-close refresh. |

---

## NEGOTIATION STRATEGY

**If buyer offers $32M (below BATNA):**
```
I say: "Appreciate the offer. I need $30M+ to walk away from independence. 
This is 9× our ARR, which is fair for 40% growth. 

Can you get to $35M? I'm willing to do 18% earnout on top if that helps."
```

**If buyer offers $38M (within range):**
```
I say: "That's close. I'd need 80% cash at close (not 70%), and then we have a deal. 
Let's structure: $30.4M cash, $7.6M earnout on ARR milestone."
```

**If buyer offers $45M+ (anchor or above):**
```
I say: "That's a serious offer. Let me discuss with co-founder and counsel. 
I'd like to confirm (1) 80% cash, (2) earnout is achievable, (3) I stay in product role. 
Then we move to LOI."
```

---

## RED FLAGS (Automatic Walk)

If buyer tries any of these, **BATNA overrides everything:**

- [ ] Offer <$26M (below BATNA). Not interested.
- [ ] Offer >80% earnout. Too much risk.
- [ ] Founder kicked out in 6 months. Loses stay bonus upside.
- [ ] Buyer is unstable (layoffs, financing risk). Can't trust earnout.
- [ ] Earnout metric is "buyer's cost savings" (uncontrollable). Walk.

If 1+ flags are true: **I decline and stay independent.**

---

## SENSITIVITY ANALYSIS

**What if:**

| Scenario | Impact | New BATNA |
|----------|--------|-----------|
| **Growth slows to 25% YoY** | Multiple drops 10-12× → $30-36M fair value | $24M (0.8× new fair) |
| **Churn spikes to 10%/month** | Multiple drops to 6× → $18M fair value | $14.4M (deal likely off table) |
| **A strategic buyer appears** | Multiple jumps to 14-16× → $42-48M fair value | $38M (0.9× new fair) |
| **Raise Series B successfully** | New valuation is $45M (pre), dilution is 25% | BATNA ≈ $30M (optionality worth less post-funding) |

---

## DECISION RULES

| Offer | Decision |
|-------|----------|
| <$26M | **HARD NO.** Stay independent. |
| $26-29M | **NO.** Below BATNA. Walk. |
| $30-35M | **MAYBE.** In range. Negotiate up or walk. |
| $36-45M | **SERIOUSLY CONSIDER.** At/above fair value. Discuss with co-founder + counsel. |
| >$45M | **VERY RARE.** If terms are good (80% cash, reasonable earnout, stay role), take it. |

---

## CO-FOUNDER ALIGNMENT

**My BATNA:** $26M minimum. I stay independent if <this.

**Co-founder's BATNA:** [FILL THIS IN]

**Are we aligned?** YES / NO

If NO, discuss and resolve before soft shop. If you disagree on BATNA, deal negotiations will expose it painfully later.

---

## CONFIDENTIALITY

🔒 **THIS IS CONFIDENTIAL.**

Store in encrypted vault. Do NOT share with:
- Buyers (ever)
- Advisors (unless under NDA)
- Investors (unless in board meeting)
- Employees (especially sales team)

If buyer learns your BATNA, your negotiating leverage vanishes.

---

**Card created:** 2026-06-12  
**Reviewed by:** [CEO + CFO]  
**Valid through:** 2026-09-12  
**Next refresh:** Q3 review

---

## HOW TO ADAPT THIS TO YOUR COMPANY

**Copy template above. Fill in:**
1. Your current ARR + growth rate
2. Your 3-year independent growth projection (conservative)
3. Your fair value (from DCF + comps)
4. Your walk-away price (BATNA) = 0.8-0.9× fair value
5. Your anchor price = 1.3-1.4× fair value
6. Your red flags (product, team, market, buyer-specific)

**Done.** You now have a BATNA card. Keep it private. Use it as your north star.
## Related

- [[_system/MOC-decisions]]
- [[brantham/_MOC]]