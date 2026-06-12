---
name: earnout_simulator
description: Earn-out modeling tool — probability-weighted scenarios (base/upside/downside)
version: 1.0
---

# EARN-OUT SIMULATOR — Seller vs Buyer Math

## Problem Solved
Earnouts are **buyer protection** (pay less upfront, more if targets hit) and **seller risk** (might never collect). This tool models real payout scenarios.

---

## EXAMPLE: $5M Deal with $1M Earnout

### Buyer's View (Why They Offer It)
```
Asking price:              $5,000,000
Buyer's initial offer:     $3,500,000 (70% upfront)
Earnout trigger:           $10M revenue in Year 2
Earnout amount:            $1,500,000 (if achieved)
```
**Buyer Logic:** "We're buying a $3.5M business. If you can grow it to $10M under us, we'll pay $1.5M more. If you can't, we pay $3.5M. Your skin = shared upside."

### Seller's View (Your Reality Check)
```
Expected upfront cash:      $3,500,000 ✓
Expected earnout:           $1,500,000 × 40% probability = $600,000 (risk-weighted)
Expected total:             $4,100,000 vs $5,000,000 asking
```
**Seller Reality:** You're betting on buyer execution. If earnout misses, you get $3.5M and live with it.

---

## EARNOUT SIMULATOR — 3 Scenarios

| Scenario | Revenue Hit | Earnout Payout | Seller Total | Probability |
|----------|-----------|-----------------|--------------|-------------|
| **Downside** | $7M (miss 30%) | $0 | $3,500,000 | 20% |
| **Base Case** | $10M (hit) | $1,500,000 | $5,000,000 | 50% |
| **Upside** | $12M (beat 20%) | $2,000,000* | $5,500,000 | 30% |

**\* If earnout structure includes overage bonus (e.g., $1.5M for $10M + $250k per $1M above)*

### Expected Value (Risk-Weighted)
```
EV = (20% × $3.5M) + (50% × $5.0M) + (30% × $5.5M)
   = $0.7M + $2.5M + $1.65M
   = $4,850,000

vs

Original Ask: $5,000,000
Earnout Discount: $150,000 (3% haircut on deal)
```

---

## CALCULATOR — Copy-Paste Your Deal

```markdown
DEAL STRUCTURE
──────────────────────
Asking price:                    $________
Upfront cash offer:              $________
Earnout amount (total):          $________
Earnout trigger (e.g., "$10M"):  $________
Earnout period (e.g., "Year 2"): ________
Overage structure:               ________ (e.g., "+$50k per $500k above $10M")

SCENARIO INPUTS (Your Gut Estimate)
──────────────────────
Base case achievement:           _______ % (realistic hit rate, 50-70%)
Downside scenario:               _______ % (miss the target, 20-30%)
Upside scenario:                 _______ % (beat the target, 10-20%)

DOWNSIDE PAYOUT (Miss target)
──────────────────────
Earnout paid:                    $0 or $______ (partial credit if buyer negotiates)
Seller receives:                 $________

BASE CASE PAYOUT (Hit target)
──────────────────────
Earnout paid:                    $________
Seller receives:                 $________ (upfront + earnout)

UPSIDE PAYOUT (Beat target)
──────────────────────
Earnout paid:                    $________ (with overage)
Seller receives:                 $________ (upfront + earnout)

RISK-WEIGHTED EXPECTED VALUE
──────────────────────
EV = (Downside % × $___) + (Base % × $___) + (Upside % × $___)
   = $__________

Expected Total:                  $________
Original Ask:                    $________
Earnout "Discount":              $________ (the haircut for taking on earnout risk)
```

---

## RED FLAGS IN EARNOUT CLAUSES

| Red Flag | Example | Fix |
|----------|---------|-----|
| **Vague KPI** | "Achieve synergies" | Specify: "$10M EBITDA by Dec 31, 2027" |
| **Buyer Controls Metric** | Revenue = whatever buyer records | Audit right: 3rd-party monthly verification |
| **No Overage Bonus** | $1M if $10M, $0 if $11M | Add step-up: +$100k per $500k above $10M |
| **Earnout Cancels on Spinoff** | Buyer sells business to 3rd party | Add: Earnout survives sale (transferable) |
| **No Interest on Holdback** | Earnout paid 6mo late with no interest | Specify: Earn 2% annual if payment delays >30 days |
| **Buyer Discretion to Adjust** | "Based on buyer's reasonable efforts" | Specify: Buyer must maintain existing team/budget |

---

## PROTECTION STRATEGIES

### Strategy 1: Tiered Earnout
```
$10M revenue → $500k
$12M revenue → $750k total
$14M revenue → $1M total

Benefit: You get paid for growth at each tier.
Downside: More expensive for buyer → may lower upfront.
```

### Strategy 2: Earnout with "Earn-In" Cap
```
Max earnout payout: $1.5M
Hit target year 2: $750k paid
Hit target year 3: $750k paid
Total: $1.5M (capped at original promise)

Benefit: Buyer can't dodge by one bad year.
```

### Strategy 3: Holdback + Earnout (Hybrid)
```
Upfront:         $3.5M (50%)
Holdback (6mo):  $0.75M (10%) ← released on earnout hit
Earnout (Year 2): $0.75M (10%) ← if revenue target met

Benefit: 3-stage release = buyer incentive to preserve business.
```

### Strategy 4: Earnout with Seller Clawback (If You Stay)
```
If you stay as COO for 2 years, you get:
  ✓ Earnout if revenue hit (plus your salary)
  
If you leave, earnout is forfeited to other sellers/shareholders.

Benefit: Aligns your incentive with buyer's success.
```

---

## DEAL BREAKER QUESTIONS

Ask the buyer BEFORE signing LOI:

1. **How is earnout revenue calculated?** (GAAP? Buyer's internal? 3rd-party audit?)
2. **What if you spin off the division?** (Does earnout stay with me or go to buyer?)
3. **What if you fire my key people?** (Earnout waived or adjusted?)
4. **What if market tanks 30%?** (Do I get credit for market conditions?)
5. **Can you refinance debt using earnout as collateral?** (Will I lose it?)
6. **What happens if you get acquired?** (Does earnout survive your buyer's buyer?)

---

## SAMPLE EARNOUT CLAUSE (Protective Version)

```
EARNOUT DEFINITION
The Seller shall be entitled to earn out payments ("Earnout") 
subject to achievement of the following milestone:

TARGET: Net Revenue of $10,000,000 or greater in the 
fiscal year ending December 31, 2027 (as measured by 
GAAP, subject to independent audit by [Auditor]).

PAYOUT:
- If Target achieved: Earnout Payment = $1,500,000
- If Target exceeded by $2M+: Earnout Payment = $1,500,000 + 
  $100,000 for each $500,000 above target (capped at $2,000,000 total)

PAYMENT TIMING: Within 30 days of audited financial statement.

MEASUREMENT: 3rd-party independent accountant certifies 
achievement (cost split 50/50 between buyer and seller).

SURVIVAL: Earnout obligation survives change of buyer 
(e.g., acquisition, merger). Buyer shall not have right 
to cancel earnout due to operational changes post-close.

ADJUSTMENTS: Earnout is NOT adjusted for:
  - Market downturns
  - Regulatory changes
  - Industry headwinds

Earnout IS adjusted for:
  - One-time unusual items (litigation settlement, asset sale)
  - Buyer-initiated cost reductions affecting revenue
```

---

**Use this tool to pressure-test any earnout offer before signing LOI.**
