---
name: earnout-vs-cash-simulator
description: Scenario modeler — comparer valuation nette (cash + earnout probable) vs. full cash
type: tool
date: 2026-06-13
---

# Earnout vs Cash Simulator

**Remplir les cases `[?]`, calcul automatique de la deal value réelle.**

---

## SCENARIO A : All Cash (Buyer offers)

```
Proposed Purchase Price:         $[? ex: 2,000,000]
├─ Seller gets immediately:     $[? ex: 2,000,000]
├─ Earnout:                     $0
├─ Seller confidence:           100% ✅

NET VALUE TO YOU (Year 0):       $[calculation auto]
```

**Avantages :**
- ✅ 100% cash today, no risk
- ✅ Can deploy capital immediately
- ✅ No earnout disputes

**Disadvantages :**
- ❌ Low valuation (buyer misprices your risk)
- ❌ If you believe in business, you're leaving upside on table

---

## SCENARIO B : Cash + Earnout (More realistic)

### Deal Terms

```
Purchase Price (PPA):            $[? ex: 2,000,000]
├─ Cash at close:               $[? ex: 1,200,000] = 60%
└─ Earnout potential:           $[? ex: 800,000] = 40%

Earnout tied to:                [REVENUE / EBITDA / MILESTONE]
├─ Target metric:               $[? ex: $1.5M revenue in Year 1]
├─ Your probability of hit:     [?]% (be honest: 60% / 80% / 90%?)
└─ If you hit = 100% earnout
    If you miss = 0% earnout
    (Or is there a pro-rata clause? Specify below)
```

### Probability-Weighted Value

**Scenario B1 : You hit earnout**
```
Cash at close:                  $[auto from above]
+ Earnout earned:              $[auto from above]
───────────────────────────────────────────
Total (if successful):          $[auto sum]

Probability of success:         [your %]
Expected value:                 $[auto × probability]
```

**Scenario B2 : You miss earnout**
```
Cash at close:                  $[auto from above]
+ Earnout earned:              $0
───────────────────────────────────────────
Total (if fail):               $[auto]

Probability of miss:            [100 - your %]
Expected value:                 $[auto × probability]
```

### EARNOUT NET VALUE (Scenario B)

```
Expected value (if hit × prob) + Expected value (if miss × prob)
= $[auto calc]

= Scenario A value × [your confidence multiplier]
```

---

## Comparison Matrix

```
Metric                      SCENARIO A        SCENARIO B       Delta
────────────────────────────────────────────────────────────────────
Headline valuation          $[A value]        $[B value]       [?]%
═════════════════════════════════════════════════════════════════════
Cash received today         $[A value]        $[B cash]        $[?]
Risk-adjusted value         $[A value]        $[B prob-adj]    [?]%
═════════════════════════════════════════════════════════════════════
Your confidence in deal     100%              [your %]         [gap]
Buyer confidence            [low]             [higher]         ✅
Alignment post-close        Poor              Good             ✅
Sleep quality               Good              So-so            [?]
```

---

## Decision Framework

| If scenario A / B delta... | Choose |
|---------------------------|--------|
| **A is 30%+ higher** | 🔴 **Take A (all cash)** — Earnout risk not worth it |
| **A is 10-30% higher** | 🟡 **Negotiate** — Push for more cash or lower earnout targets |
| **A is 0-10% higher** | 🟢 **Take B (earnout)** — If you're confident, upside is worth risk |
| **B is higher** | 🟢 **Take B** — Buyer believes more than you? Weird but take it. |

---

## Earnout Risk Factors

### Red Flags → Reduce your confidence %

| Risk factor | Impact | Adjust confidence |
|-------------|--------|-------------------|
| **Buyer will change roadmap post-close** | High | -20% |
| **Buyer won't commit marketing budget** | High | -15% |
| **Earnout target uses metric buyer controls** (e.g., pricing, distribution) | Very High | -30% |
| **Key team member leaving post-close** | High | -25% |
| **Customer concentration >40%** (risk of churn post-acquisition) | High | -20% |
| **Integration risk high** (Buyer = terrible acquirer) | Very High | -25% |
| **No earnout "true-up" clause** (buyer can pay $0 if misses by 1%) | Very High | -30% |

### Green Flags → Increase confidence %

| Green flag | Impact | Adjust confidence |
|-----------|--------|-------------------|
| **You're staying as CEO** | +10% |
| **Earnout tied to OKRs you control** | +15% |
| **Buyer has great earnout track record** | +10% |
| **Buyer puts earnout in escrow** (money set aside) | +10% |
| **Insurance policy on earnout** (R&W insurance covers earnout shortfall) | +15% |
| **Pro-rata earnout** ("If you hit 80% of target, you get 80% of earnout") | +15% |

---

## Real Example

### Your situation
```
Buyer offer:
  - $1M cash at close
  - $500k earnout if revenue hits $1.5M in Year 1
  - Headline: $1.5M

Your assessment:
  - You're staying as CEO: +10%
  - Revenue target reasonable? Yes, you're at $900k now: +5%
  - Earnout tied to revenue (buyer controls via sales/marketing support):
    - Buyer won't hire sales team: -20%
    - Buyer promises marketing budget in LOI: +10%
  - Key engineer staying: +5%
  - No true-up clause: -10%
  ───────────────────────────────────
  Your net confidence: 50% baseline + 35% = 85%
```

### Calculation
```
Scenario B:
- Hit target (85% prob): $1M + $500k = $1.5M
- Miss target (15% prob): $1M + $0 = $1M

Expected value = (85% × $1.5M) + (15% × $1M) = $1.275M + $0.15M = $1.425M

Scenario A (all-cash comparison):
- Buyer says "If it's all cash, we can only do $1M"
- All-cash value: $1M

Decision: Earnout deal ($1.425M expected) > All-cash ($1M)
Take the earnout deal.
```

---

## Negotiation Playbook

### If earnout targets are impossible

```
Buyer: "Revenue must reach $2M in Year 1 or earnout is zero"
You: "That's 2.2x growth. Not achievable without:
     - Your sales team + budget
     - My team working full-time
     - Zach not leaving
     
     Here's what makes it possible:
     1. We hire 2 sales people (my cost: $200k)
     2. You provide marketing budget ($50k/mo)
     3. I stay as CEO for 2 years (equity vesting)
     
     If you commit to ^^ I'll take the earnout.
     If not, price must be all-cash higher."
```

### If buyer won't commit to earnout support

```
You: "Earnout tied to revenue but you won't commit to sales/marketing?
     That's heads I lose, tails you win.
     
     Option 1: Earnout based on OKRs WE control (team, product)
     Option 2: Increase cash component to 80%+
     Option 3: I walk."
```

---

## Tax Angle (Discuss with CPA)

```
Scenario A: All cash today
  Tax cost (capital gains):      [Your accountant fills in]
  Net after-tax value:           $[auto]

Scenario B: Earnout + cash over 2 years
  Year 1 tax cost:               [Accountant: typically lower]
  Year 2 tax cost:               [When earnout paid]
  Net after-tax value:           $[auto]

After-tax delta:                 Earnout may be better tax-wise (+5-15%)
```

---

## Final Checklist

Before accepting an earnout deal:

- [ ] Earnout targets are achievable with buyer's support (not unilateral)
- [ ] Earnout is pro-rata (80% target = 80% earnout, not zero)
- [ ] If you leave / pushed out early, earnout vests (good-leaver clause)
- [ ] Earnout capped at time (18-24 months max, not forever)
- [ ] Earnout amount in escrow or insured (not "we'll pay if we feel like it")
- [ ] You have audit rights (can verify numbers buyer reports)
- [ ] Buyer has credible earnout track record (they actually pay them)

If 4+ items are "no", earnout is risky. Push for more cash.

