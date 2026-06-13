---
name: tool-walkaway-price-calculator
description: Formula + decision framework — Comment calculer ta valuation minimum inacceptable
metadata:
  type: tool
  created: 2026-06-13
---

# Walkaway Price Calculator

Your walkaway price = the minimum offer at which you say "no" and continue alone.

## Method 1: 3-Year Earnings Power (Simple)

```
Walkaway = (Projected EBITDA Year 3) × 6x ÷ 1.15

Rationale:
  - Year 3 EBITDA is realistic, not aspirational
  - 6x is baseline SaaS multiple
  - ÷1.15 = discount for certainty (buyer pays for known, not speculative)

Example: You project $5M EBITDA in Year 3
  Walkaway = $5M × 6 ÷ 1.15 = $26.1M
```

## Method 2: NPV of Staying Independent (Rigorous)

```
Walkaway = (Year 1 EBITDA × (1 + growth%) ^ years) × (1 - risk_discount)
         × (1 - time_value_of_money_discount)

Example: Year 1 EBITDA = $2M, 3-year growth = 40%/yr, years = 3
  Year 3 EBITDA = $2M × 1.40^3 = $5.5M
  Risk discount (40%) = 0.60 (you might miss targets)
  Time value (3 yr @ 10%) = 0.75
  Walkaway = $5.5M × 0.60 × 0.75 = $2.5M × 6x = $15M
```

## Method 3: Founder-Specific Runway (Best for Bootstrapped)

```
Walkaway = (Runway remaining in months) × (Monthly burn) 
         + (Founder replacement opportunity cost × years until liquidity)

Example: 
  You have $500k runway (12 months at $40k/mo burn)
  Founder opportunity cost = $150k/yr (salary you could earn elsewhere)
  Expected independent liquidity = 5 years
  
  Walkaway = $500k + ($150k × 5) = $500k + $750k = $1.25M
```

## Method 4: Debt-Based Walkaway (If Financing Available)

```
If you can borrow against EBITDA:
  Maximum debt capacity = Year 1 EBITDA × 3.5x
  Your ownership = current equity value
  Walkaway = (Debt capacity + equity) / 2
  
  (Conservative: accept 50% of available value in liquidity)
```

## Real-World Walkaway Examples

| Scenario | Year 1 EBITDA | Method 1 (Simple) | Method 2 (NPV) | Method 3 (Runway) | **Actual Walkaway** |
|---|---|---|---|---|---|
| Bootstrapped SaaS, $2M EBITDA, 20% growth, 12mo runway | $2M | $10.4M | $8.2M | $3.5M | **$8–10M** |
| VC-backed, $5M EBITDA, 50% growth, diluted | $5M | $26.1M | $35M | N/A | **$22–30M** |
| Consulting biz, $500k EBITDA, flat, burnout risk | $500k | $2.6M | $1.2M | $0.8M | **$1.5–2M** |

## The Psychology

**Anchor high (30% above walkaway)**, then concede slowly:
- Buyer opens: $5M
- You counter: $15M (1.5x walkaway)
- Final: ~$11M (slightly above walkaway) = win

**Never negotiate below walkaway** unless:
- Buyer offers strategic value (distribution, technology, team)
- Terms include earnout (future upside recovery)
- Stock payment (illiquidity premium justified)

## Negotiation Playbook: Using Walkaway as Pressure

When buyer lowballs:
> "I appreciate the offer, but at $X it's not rational for me to sell. My understandable alternative is to stay independent, reinvest, and sell in 3 years at higher valuation. So my minimum is $Y."

This works because:
1. You sound rational, not emotional
2. Buyer knows you have a real alternative
3. You've set a floor they must breach

## Red Flags: When Your Walkaway is Wrong

| Warning Sign | What It Means |
|---|---|
| Walkaway < buyer's opening offer | You're dramatically undervaluing yourself |
| Walkaway > 50x current year EBITDA | You're unrealistic (reset it) |
| You keep moving walkaway down as deal progresses | Sunk-cost fallacy; hold firm or walk |
| Walkaway includes emotional factors | Separate ego (I deserve $X) from market (I can get $X) |

---

**Use this tool at start of M&A process. Update only if fundamentals change (market downturn, churn spike, etc.), not emotions.**
