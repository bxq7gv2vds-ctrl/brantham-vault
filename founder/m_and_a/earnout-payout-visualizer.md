---
name: earnout_payout_visualizer
description: Earnout structure simulator showing payout scenarios (cash + tax impact)
version: 1.0
date: 2026-06-12
---

# EARNOUT PAYOUT VISUALIZER

**Play with different earnout structures. See payout scenarios.**

---

## SCENARIO BUILDER

### YOUR DEAL PARAMETERS

```
Purchase Price (Total):                    $[____]M
├─ Cash (Day 1):                           $[____]M  ([____]%)
├─ Earnout (Year 1-2):                     $[____]M  ([____]%)
└─ Equity Rollover (if founder):           $[____]M  ([____]%)

Earnout Duration:                          [12] months (or [24] months)
Earnout Metrics:
  1. [Revenue target]:          $[____]M   (weight: [____]%)
  2. [Churn target]:            <[____]%   (weight: [____]%)
  3. [Customer count]:          [____]     (weight: [____]%)
```

---

## SCENARIO 1: BASE CASE (90% Achievement)

**Assumptions:** You hit 90% of earnout targets (realistic).

```
Earnout Payout:                            $[____]M × 90%    = $[____]M
Less: Federal Income Tax (37% top rate):   $[____]M × 37%    = -$[____]M
Less: State Income Tax (CA 13.3%):         $[____]M × 13.3%  = -$[____]M
Less: Medicare Surtax (0.9%):              $[____]M × 0.9%   = -$[____]M

NET EARNOUT PROCEEDS:                                          $[____]M

---

FULL TRANSACTION PAYOUT:
├─ Cash (Day 1):                           $[____]M (after taxes: $[____]M)
├─ Earnout (Year 1-2):                     $[____]M (after taxes: $[____]M)
├─ Equity Rollover Value (at year 2):      $[____]M (after taxes: $[____]M)

TOTAL NET PROCEEDS (after all taxes):                          $[____]M

---

ANNUALIZED NET TAKE-HOME (over 2 years):                      $[____]M / year
```

---

## SCENARIO 2: CONSERVATIVE CASE (70% Achievement)

**Assumptions:** You hit 70% of targets (tougher integration, team churn).

```
Earnout Payout:                            $[____]M × 70%    = $[____]M
Less: Taxes (50.2% effective):                                 -$[____]M

NET EARNOUT PROCEEDS:                                          $[____]M

TOTAL NET PROCEEDS (cash + earnout):                           $[____]M

Difference vs. Base Case:                                      -$[____]M
```

---

## SCENARIO 3: OPTIMISTIC CASE (110% Achievement)

**Assumptions:** You overachieve targets (rare but possible).

```
Earnout Payout (capped):                   $[____]M × 100%   = $[____]M
  (Note: Most deals have 100% cap; check SPA.)
Less: Taxes:                                                   -$[____]M

NET EARNOUT PROCEEDS:                                          $[____]M

TOTAL NET PROCEEDS (cash + earnout):                           $[____]M

Difference vs. Base Case:                                      +$[____]M
  (Note: Limited upside if capped at 100%.)
```

---

## SCENARIO MATRIX: OUTCOME MAPPING

| Achievement % | Earnout Earned | Net After Tax | Total Deal Value (net) |
|---|---|---|---|
| 50% | $[X]M | $[Y]M | $[Z]M |
| 70% | $[X]M | $[Y]M | $[Z]M |
| 90% (Expected) | $[X]M | $[Y]M | $[Z]M |
| 100% | $[X]M | $[Y]M | $[Z]M |
| 110%+ | $[X]M (capped) | $[Y]M | $[Z]M |

**Payout cliff:** Is there a [X]% threshold you must hit to get earnout credit?  
If yes, probability of hitting [X]% = [____]%

---

## TAX IMPLICATIONS

### Federal Income Tax

```
Ordinary Income (W-2 wages):                [____]% of earnout
  → Taxed at marginal rate: 37%

Long-term Capital Gains (equity rollover): [____]% of rollover value
  → Taxed at: 20%

Short-term Capital Gains (if liquidated early):
  → Taxed at: 37%
```

### State Income Tax (varies by state)

```
California (if resident):                  13.3% additional
New York (if resident):                    10.9% additional
Texas (if resident):                       0% (no income tax)
```

### Alternative Minimum Tax (AMT)

```
If your total income exceeds $[X], you may owe AMT.
AMT rate: 26-28%

AMT exposure: [HIGH / MEDIUM / LOW]
  (Consult accountant)
```

### Employment Tax

```
Earnout paid as [bonus / 1099 / equity]:   [____]

If paid as bonus: FICA tax (12.4% SS + 2.9% Medicare) already 
paid by company, not you.

If paid as 1099: You pay both employer + employee share (15.3% total).
```

---

## COMPARATIVE PAYOUT SCENARIOS

### Scenario A: 60% Cash / 40% Earnout

```
Year 0:
├─ Cash at close:  $[X]M (net after taxes: $[Y]M)

Year 1-2:
├─ Earnout (if achieved): $[Z]M (net after taxes: $[W]M)

Total net: $[TOTAL]M
Risk to you: High (rely on acquirer's execution)
```

### Scenario B: 80% Cash / 20% Earnout

```
Year 0:
├─ Cash at close: $[X]M (net: $[Y]M)

Year 1-2:
├─ Earnout (small upside): $[Z]M (net: $[W]M)

Total net: $[TOTAL]M
Risk to you: Low (most value secure on Day 1)
```

### Scenario C: 100% Cash (No Earnout)

```
Year 0:
├─ Cash at close: $[X]M (net: $[Y]M)

Total net: $[TOTAL]M
Risk to you: None (all cash immediately)
Note: Typically only possible if valuation is lower.
```

---

## EARNOUT STRUCTURE DECISIONS

### How should earnout be calculated?

| Approach | Pros | Cons | Typical |
|----------|------|------|---------|
| **Cash-on-hand** | Easy to track, no disputes | Doesn't count AR/deferred | 30% of deals |
| **GAAP Revenue** | Standard, auditable | Takes longer to close | 40% of deals |
| **Billings** | Faster recognition | Doesn't account for refunds | 20% of deals |
| **Custom formula** | Flexible | Disputeable | 10% of deals |

**Recommendation:** GAAP Revenue (auditable, standard).

### Who measures & certifies achievement?

```
Option 1: Acquirer's Finance Team (biased toward underreporting)
Option 2: Independent 3rd Party (costs $[20-50]k, neutral)
Option 3: You + Acquirer agree (informal, faster)

Recommendation: Combination (acquirer reports, you audit quarterly).
```

### What's the dispute resolution process?

```
If acquirer says you missed targets but you disagree:

1. Initial disagreement (Day 1-30): Escalate to CFO call
2. Escalation (Day 31-60): Engage accountant for review
3. Final (Day 61+): Arbitration clause kicks in

Cost of dispute: $[10-50]k in legal fees
Risk: You might lose earnout while fighting

Recommendation: Detailed earnout language in SPA to avoid disputes.
```

---

## 🎯 EARNOUT MOTIVATION STRATEGIES

### Vesting Schedule (Monthly)

```
Month 1-6:   0% payout (threshold period)
Month 7-12:  25% of earnout available
Month 13-18: 50% of earnout available
Month 19-24: 100% of earnout available

Psychology: Spreads payout over time, reduces lump-sum tax shock.
```

### Milestone-Based (Achievable)

```
Milestone 1 (M6): Hit $[X]M ARR      → Earn $[Y]M
Milestone 2 (M12): Retain [X]% customers → Earn $[Y]M
Milestone 3 (M18): Add [X] enterprise customers → Earn $[Y]M
Milestone 4 (M24): Hit [X]M ARR target → Earn $[Y]M
```

### Combo (Recommended)

```
Base earnout: $[X]M for hitting [target]
Bonus: +[X]% if you exceed by [Y]%
Claw-back: -[X]% if you miss by more than [Y]%

Example: Hit target = $1M, exceed by 10% = $1.2M, miss by 20% = $0.8M
```

---

## ⚠️ EARNOUT RISK FACTORS

### Risk 1: Acquirer Manipulates Metrics

```
Red flags:
□ Acquirer changes accounting post-close
□ One-time charges reduce "revenue"
□ Product bundling hides your product's contribution
□ Customer churn accelerates unexpectedly

Mitigation:
✓ Lock in chart of accounts day 1
✓ Define "revenue" as [specific line item in P&L]
✓ Establish customer list with baseline churn rate
✓ Quarterly certification by independent accountant
```

### Risk 2: Acquirer Integrates Your Product (Loses Identity)

```
If earnout is tied to [your product's revenue], but acquirer 
merges it into larger platform:
→ Hard to track [your product's] contribution
→ You lose earnout credit

Mitigation:
✓ Keep-separate earnout metrics (separate P&L for [Y] months)
✓ Or, tie earnout to broader metrics (total company revenue)
✓ Or, tie earnout to qualitative milestones (team retention, integration)
```

### Risk 3: Key Team Members Leave (Integration Fails)

```
If your team is required for earnout achievement but people bail:
→ You own the problem, not acquirer
→ You don't get earnout

Mitigation:
✓ Negotiate "change of control" earnout (pays out if key people leave)
✓ Or, tie earnout to non-people metrics (retention, revenue)
✓ Or, build retention bonuses separate from earnout
```

---

## 📋 EARNOUT CHECKLIST

- [ ] Earnout % is [X]% of total purchase price (benchmark: 15-35%)
- [ ] Earnout duration is [X] months (benchmark: 12-24 months)
- [ ] Earnout metrics are tied to [specific KPIs] (not subjective)
- [ ] Thresholds are achievable (hit [X]% of historical performance)
- [ ] Dispute resolution is defined (arbitration, not litigation)
- [ ] Accounting is locked in (chart of accounts, revenue definitions)
- [ ] Tax treatment is clear (bonus vs. capital gains vs. 1099)
- [ ] Vesting schedule is smooth (monthly or milestone-based, not cliff)
- [ ] Claw-back is limited (e.g., only for fraud, not underperformance)
- [ ] Key person provisions are in place (if you care about retention)

---

**Created:** 2026-06-12  
**For:** Soren Mendy (earnout planning)  
**Time to use:** 10 min (fill in your numbers, simulate scenarios)  
**Note:** Always consult with tax accountant + lawyer before finalizing earnout structure

