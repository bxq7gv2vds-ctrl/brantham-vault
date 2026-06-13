---
name: loi-key-terms-explainer
description: 10 LOI key terms (price, earnout, reps, escrow) — expliqué simplement
metadata:
  type: reference
---

# LOI KEY TERMS — EXPLAINER

**Utilité** : Understand each term, know market ranges, spot red flags.

---

## 1. PURCHASE PRICE (Base Cash)

**Definition:** Cash you get at closing. Usually split between upfront and holdback.

**Example:**
- Deal valuation: $20M
- Upfront cash: $16M (80%)
- Holdback (escrow): $4M (20%) ← paid later if no reps issues

**Your negotiation:**
- **Ask for:** 85-90% upfront (most cash in your pocket)
- **Expect:** 80-85% upfront (market)
- **Red flag:** <80% upfront OR >90 days holdback (you're financing buyer's risk)

**Market data:**
- Strategic buyer: 80-90% upfront
- PE buyer: 70-85% upfront (want holdback to claw back if issues)
- Venture: 85-95% upfront (founder-friendly)

---

## 2. EARNOUT (Performance-Based Payment)

**Definition:** You get additional cash if business hits targets post-close.

**Example:**
- Base deal: $16M
- Earnout: $4M (if you hit $2.5M ARR by end of Year 1)
- Total: $20M (if earnout hits)

**Your negotiation:**
- **Ask for:** <20% total deal (lower earnout = less risk)
- **Expect:** 20-30% total (market)
- **Red flag:** >40% earnout (you're funding buyer's upside)

**Structure options:**
- **Metric-based:** Earnout = ARR > $2.5M → you get $X
- **Time-based:** $X paid quarterly, annually
- **Hybrid:** $X if ARR > $2.5M AND you're still CEO

**Key risk:** Earnout RARELY gets paid in full.
- Strategic buyer changes roadmap → your product features cut → earnout metrics miss
- PE buyer squeezes expenses → can't hit growth targets
- Valuation dispute → buyer lowballs ARR definition

**True value:** Multiply earnout by 50-75% (probability-weighted). Use [Earnout Calculator](earnout_true_value_calculator.py).

---

## 3. REPS & WARRANTIES CAP

**Definition:** Maximum liability if buyer sues you for breach (e.g., "you said the code was clean but it has GPL license").

**Example:**
- Deal: $20M
- Reps cap: 1% = $200k (max buyer can recover)
- Beyond $200k, buyer's out of luck

**Your negotiation:**
- **Ask for:** 0.5% (very founder-friendly)
- **Expect:** 1% (market for software)
- **Red flag:** >1.5% (buyer is pushing risk onto you)

**By category:**
- Tax reps: Often carved out (different cap, longer tail)
- General reps: 1% standard
- Title/IP reps: Sometimes 2-3% (important)

**Dynamics:**
- Strategic buyer: Often accepts 0.5-1% (they're bigger, can absorb loss)
- PE buyer: Wants 1-2% (want seller skin in the game)
- Venture: Usually 0.5% (founder-friendly)

---

## 4. BASKET (Threshold Before Reps Cap Kicks In)

**Definition:** Buyer must accumulate claims totaling [Basket amount] before you pay anything.

**Example:**
- Reps cap: $200k
- Basket: $50k
- If claims total $40k → buyer gets $0 (below basket)
- If claims total $60k → buyer gets $10k (above basket)

**Your negotiation:**
- **Ask for:** 0.5-1% of deal (high basket = fewer claims stick)
- **Expect:** 0.25-0.5% (market)
- **Red flag:** <0.25% (too easy for buyer to make claims)

**Formula:**
- Deal: $20M
- Basket you should ask: $100k-200k
- Basket buyer will ask: $50k-100k
- Market outcome: $75k-100k

---

## 5. TAIL (How Long Buyer Can Sue You)

**Definition:** Deadline for buyer to sue you for breach. After tail, you're off the hook.

**Example:**
- Closing: January 1, 2027
- General reps tail: 18 months (you're liable until July 1, 2028)
- Tax reps tail: 3 years (longer because tax audits take time)

**Your negotiation:**
- **Ask for:** 12-18 months general, 3 years tax
- **Expect:** 18 months general, 3-4 years tax
- **Red flag:** >24 months general, >4 years tax (excessive)

**Why it matters:** After tail expires, buyer can't sue you (except taxes, which have longer statute of limitations).

---

## 6. INDEMNITY INSURANCE (Tail Insurance)

**Definition:** Insurance policy that covers reps claims after escrow runs out.

**Example:**
- Escrow (your holdback): $4M, releases after 18 months
- Tail insurance: $2M policy, covers claims for 3 years
- If buyer finds a reps breach in Year 2 (after escrow released), insurance pays

**Your negotiation:**
- **Ask for:** Buyer pays for insurance (cheaper than holdback)
- **Expect:** 50/50 split or buyer pays (market)
- **Red flag:** Founder pays for insurance (expensive, defeats purpose)

**Cost:** ~1-2% of coverage amount. For $2M coverage, costs $20k-40k.

**Reality:** Insurance is cheaper than escrow. Why?
- Escrow: $4M locked 18 months (opportunity cost to you)
- Insurance: $2M coverage, $40k premium, released immediately

**Smart deal:** Small escrow ($0.5-1M) + insurance ($1-2M coverage) = better for you.

---

## 7. PURCHASE PRICE ADJUSTMENT (Closing Payment Calculation)

**Definition:** How they calculate what you actually get at closing.

**Formula:**
```
Base purchase price ($X)
- Cash paid by company (can reduce your proceeds)
- Debt paid off (your company had a loan)
+ Working capital adjustment (cash, receivables, payables)
= Net amount you get at closing
```

**Example:**
- Base price: $20M
- Cash in company: $500k (reduces proceeds, buyer gets this)
- Debt: $1M (paid off at close, reduces proceeds)
- NWC adjustment: +$200k (you had more receivables than expected)
- **Net to you: $20M - $500k - $1M + $200k = $18.7M**

**Red flag:** Check that calculations are:
- [ ] Net working capital is defined (AR, AP, inventory, not cash/debt)
- [ ] NWC measurement date is clear (signing vs closing)
- [ ] Buyer's accounting is reasonable (get pre-approval from your accountant)

---

## 8. CLOSING CONDITIONS (Deal Killers)

**Definition:** Things that must happen for deal to close. If they don't, deal can fall apart.

**Common conditions:**
- [ ] Material adverse change (business doesn't collapse)
- [ ] Customer consent (contracts assign to buyer)
- [ ] No litigation (nobody sues to block deal)
- [ ] Regulatory approval (if needed)
- [ ] Financing (if buyer is borrowing money)

**Your negotiation:**
- **Push for:** Narrow, objective conditions (e.g., "material adverse change" defined precisely)
- **Resist:** Vague conditions (e.g., "general satisfaction")
- **Red flag:** "Financing condition" = buyer might not have cash (risky)

**What can kill deals:**
- Customer churn >X% before close
- Key person leaves
- Lawsuit filed against your company
- Regulatory investigation opens
- Buyer's funding falls through

---

## 9. NON-COMPETE (Founder Restrictions)

**Definition:** After close, you can't start a competing business for [X years] in [geography].

**Example:**
- Non-compete: 3 years, worldwide
- Non-solicit: 2 years (can't hire employees or solicit customers)

**Your negotiation:**
- **Ask for:** 1-2 years, limited geography (USA only?)
- **Expect:** 2-3 years, broad geography
- **Red flag:** >3 years or overly broad (unenforceable anyway, but legal risk)

**Reality check:**
- 3-year worldwide = extremely restrictive (you're locked out)
- But also legally unenforceable in many states (California = non-competes void)
- Negotiate to something reasonable

**Market:**
- Strategic buyer: 2-3 years (want to block competition)
- PE/Venture: 1-2 years (more flexible)

---

## 10. FOUNDER ROLE POST-CLOSE

**Definition:** What's your job after the deal? Title, comp, expectations?

**Scenarios:**
- **Scenario A:** You're CEO, reporting to buyer's board (keep power)
- **Scenario B:** You're VP Product, reporting to buyer's CPO (less power)
- **Scenario C:** Advisor role (1-2 days/week, not involved day-to-day)
- **Scenario D:** Clean exit (you're done, earnout payments only)

**Your negotiation:**
- **Ask for:** What you actually want (be honest)
- **Get it in writing:** Employment agreement, not just verbal promise
- **Clawback:** Earnout adjusts if you leave (keeps you committed)

**Red flag:** Role is undefined ("We'll figure it out after close" = recipe for conflict)

---

## MARKET SNAPSHOT (Typical Software Deal, $10-50M)

| Term | Strategic | PE | Venture |
|------|-----------|----|---------| 
| Upfront cash | 85-90% | 70-80% | 85-95% |
| Earnout % | 10-20% | 30-50% | 5-15% |
| Reps cap | 0.5-1% | 1-1.5% | 0.5% |
| Basket | $50-100k | $50-100k | $25-50k |
| Tail | 18m general, 3y tax | 18m general, 3y tax | 12-18m general |
| Non-compete | 2-3 years, worldwide | 2-3 years | 1-2 years |

---

## RED FLAG SUMMARY

🚩 Earnout >40% of total deal  
🚩 Reps cap >1.5%  
🚩 Basket <$25k  
🚩 Tail >24 months general reps  
🚩 Non-compete >3 years  
🚩 Financing condition (buyer doesn't have cash)  
🚩 Founder role undefined  
🚩 Escrow >20% and >24 months  
🚩 No tail insurance (leaves you exposed after escrow)  
🚩 IP reps uncapped (huge risk)  

---

## NEXT STEPS

1. **Get this LOI template:** [LOI Template](template_loi_saas.md)
2. **Run through each term:** Use this explainer
3. **Negotiate:** Know your walk-away for each term
4. **Red flag check:** Are any of your terms above red flags?
5. **Get legal review:** Have a lawyer review before you sign

**Pro tip:** Negotiate LOI HARD. It's easier to change before signing than after. Post-signing, everything tightens.
## Related
