---
name: analyse-sensibilite-prix
description: Analyse de sensibilité (impact de ±10% / ±20% prix sur outcomes)
metadata:
  type: reference
  created: 2026-06-13
---

# Analyse de Sensibilité — Prix

**Goal**: Understand impact of price changes on your real take-home (after tax, earnout risk).

---

## SETUP

**Key inputs:**
- Base valuation: $[X]M
- Cash component: [X]%
- Earnout component: [Y]%
- Earnout risk factor: [Z]% (likelihood of hitting targets)
- Personal tax rate: [T]% (federal + state)
- Your ownership %: [S]%

---

## SIMPLE MODEL

| Scenario | Base Price | Cash Take | Earnout @ Risk | Tax | Net to You |
|----------|------------|-----------|----------------|-----|-----------|
| **Base case** | $20M | $14M (70%) | $6M × 70% = $4.2M | -35% | **$12.9M** |
| **+10% price** | $22M | $15.4M | $6.6M × 70% = $4.6M | -35% | **$14.1M** |
| **+20% price** | $24M | $16.8M | $7.2M × 70% = $5.0M | -35% | **$15.4M** |
| **−10% price** | $18M | $12.6M | $5.4M × 70% = $3.8M | -35% | **$11.6M** |
| **−20% price** | $16M | $11.2M | $4.8M × 70% = $3.4M | -35% | **$10.1M** |

---

## DETAILED SENSITIVITY TABLE

### Scenario: Base $20M, 50% ownership, 70% tax on cash + 50% on earnout

```
Price    | Cash Portion | Earnout | Total Value | Your % | Tax | Net |
---------|--------------|---------|-------------|--------|-----|-----|
$15M     | $10.5M       | $4.5M   | $15M        | 50% × $7.5M = $7.5M | -$2.6M | $4.9M
$16M     | $11.2M       | $4.8M   | $16M        | 50% × $8M = $8M | -$2.8M | $5.2M
$17M     | $11.9M       | $5.1M   | $17M        | 50% × $8.5M = $8.5M | -$3.0M | $5.5M
$18M     | $12.6M       | $5.4M   | $18M        | 50% × $9M = $9M | -$3.2M | $5.8M
$19M     | $13.3M       | $5.7M   | $19M        | 50% × $9.5M = $9.5M | -$3.3M | $6.2M
$20M     | $14M         | $6M     | $20M        | 50% × $10M = $10M | -$3.5M | $6.5M
$21M     | $14.7M       | $6.3M   | $21M        | 50% × $10.5M = $10.5M | -$3.7M | $6.8M
$22M     | $15.4M       | $6.6M   | $22M        | 50% × $11M = $11M | -$3.9M | $7.1M
$23M     | $16.1M       | $6.9M   | $23M        | 50% × $11.5M = $11.5M | -$4.0M | $7.5M
$24M     | $16.8M       | $7.2M   | $24M        | 50% × $12M = $12M | -$4.2M | $7.8M
$25M     | $17.5M       | $7.5M   | $25M        | 50% × $12.5M = $12.5M | -$4.4M | $8.1M
```

---

## IMPACT OF EARNOUT STRUCTURE

**All else equal, what matters most is: % that's cash vs. earnout**

| Structure | Cash | Earnout | At-Risk Value | Risk | Net (50% own) |
|-----------|------|---------|---------------|------|---------------|
| **All cash** | $20M | $0 | $10M | None | $10M |
| **75% cash** | $15M | $5M | $7.5M + $2.5M risk | -$2.5M | $7.5M |
| **50% cash** | $10M | $10M | $5M + $5M risk | -$5M | $5M |
| **25% cash** | $5M | $15M | $2.5M + $7.5M risk | -$7.5M | $2.5M |

**Key insight**: A $20M deal that's all-cash = $10M net to you.  
But a $20M deal that's 50% earnout = $5M net to you (if you're risk-averse).

---

## CASH FLOW IMPACT BY SCENARIO

| Scenario | Close Date | Cash at Close | Earnout Payment | When | Total 36 Months |
|----------|------------|---------------|-----------------|------|-----------------|
| **Low earnout hit (50%)** | Q1 | $10M | $2.5M | Q3 2026 | $12.5M |
| **Target hit (100%)** | Q1 | $10M | $5M | Q3 2026 | $15M |
| **Exceed (120%)** | Q1 | $10M | $6M | Q3 2026 | $16M |
| **Miss (0%)** | Q1 | $10M | $0 | — | $10M |

---

## NEGOTIATION ANCHOR POINTS

Use sensitivity analysis to set your:

**Anchor (opening ask):**  
- High cash component (you want it locked in)
- Generous earnout targets (you believe you'll hit them)
- Example: "$25M: $18M cash (72%), $7M earnout on [easy targets]"

**Walk-away (minimum):**  
- Net present value (after tax) of at least $[X]M
- Example: "Won't accept <$15M net, which means $20M gross at 50/50 cash/earnout"

**Deal sweet spot:**  
- $[X]M × 65% cash, $[X]M × 35% earnout on achievable targets
- Balances buyer's caution with your upside

---

## TAX CONSIDERATIONS (Ask Your CPA)

**Key differences by structure:**

| Consideration | Impact |
|---------------|--------|
| **Stock vs. cash** | Stock may defer tax; earnout is typically taxed year-by-year |
| **Section 338(h)(10) election** | Can optimize tax on asset sale vs. stock sale |
| **Installment sale** | Spreading cash/earnout over years can smooth your tax burden |
| **LTCG vs. ordinary income** | Earnout based on revenue = ordinary income; equity = LTCG (lower rate) |

**Action**: Get your CPA/tax attorney involved **before signing LOI**, not after.

---

## EXAMPLE WALKTHROUGH

**Your situation:**
- Fair valuation: $20M
- You own: 40%
- Your net: 40% × $20M = $8M gross
- You want: $6M net after tax
- Tax rate: 35%

**Work backwards:**
- $6M net / (1 - 0.35) = $9.2M gross needed
- So you need: $9.2M / 40% = $23M company valuation

**Or if accepting earnout:**
- $20M company value, 50% cash = $10M cash at close
- Your 40% × $10M = $4M at close (after 35% tax ≈ $2.6M net)
- Earnout: $10M × 50% = $5M earnout over 12 months
- Your 40% × $5M = $2M earnout (after tax ≈ $1.3M net)
- **Total net: $2.6M + $1.3M = $3.9M (LOWER than your $6M target)**

**Conclusion**: At $20M valuation, you need 70%+ cash to hit your $6M net target.

---

## DECISION FRAMEWORK

Use this matrix to decide whether to accept an offer:

```
IF price is:
  < $18M → Walking
  $18M–$22M → Negotiate for more cash %
  $22M–$25M → Acceptable if cash % high enough
  >$25M → Strong accept (hit your number)

IF earnout % is:
  <25% → Can accept lower cash price
  25–50% → Reasonable (if targets are achievable)
  >50% → Reject (too risky; ask for higher base)

IF cash % is:
  <50% → Only accept if price is +25% premium
  50–70% → Healthy (balances both sides)
  >70% → Buyer is conservative; good sign
```

