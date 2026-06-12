---
name: deal-killer-matrix
description: Matrice 3 min — quand marcher vs. quand négocier (décision rapide)
---

# Deal-Killer vs Negotiable Matrix

**Utilité** : pendant DD, il y aura 100 problèmes. Sachez lesquels = walk-away vs. price-adjustment.

---

## 🛑 DEAL-KILLERS (Walk away immediately)

Si VOUS voyez ces problèmes avant de signer LOI:

| Issue | Why It's Fatal | Action |
|-------|-----------------|--------|
| **Founder misalignment** | Co-founder won't accept terms. Board split. | Resolve internally BEFORE soft shop |
| **Active litigation** | Undisclosed lawsuit pending, patent troll, SEC investigation | Kill deal. Fix first. |
| **Top 3 customers = >70% ARR** | Loss of even one = catastrophic for earnout | Re-negotiate customer contracts to be longer before soft shop |
| **Churn >10%/month** | Buyer assumes retention = death spiral post-sale | Only proceed if buyer accepts and lowers price 30%+ |
| **IP owned by 3rd party** | Key IP with freelancer/cofounder outside company | Buy it back before LOI or it's dead |
| **You're burned out** | You need a rest, not 6 months of closing | Don't do the deal. Step back. |
| **No clear BATNA** | You don't know your walk-away price | Calculate first. Otherwise you'll panic and accept anything. |
| **Cap table disaster** | >20 shareholders, conflicting terms, conversibles unclear | Clean it up or you'll get stuck in closing for 3 months |
| **Earnout trigger buyer can't control** | Metric depends on 3rd party or external market | Don't accept. Structure it differently. |
| **Founder doesn't want to stay** | Buyer explicitly wants you post-close, you want to exit | Clarify role expectations NOW. If misaligned = disaster. |

---

## 🟡 NEGOTIABLE (Price or term adjustment)

If BUYER discovers these, they'll demand a price cut. Agree to adjust vs. walk.

| Issue | Buyer's Demand | Counter-Offer |
|-------|-----------------|-------------------|
| **Customer churn 8-10%/month** | Reduce price 15% | Reduce 8%, cap earnout at 15% |
| **One key engineer wants to leave** | Reduce price 10%, key-person retention bonus | Reduce 5%, 2x salary retention bonus |
| **Tech debt moderate** | Reduce price 12%, post-close engineering budget | 6% reduction, buyer gets 90-day engineering sprint |
| **Revenue recognition ambiguous** | Reduce price 8%, audit + true-up | Agree on recognition method + audit, 4% reduction |
| **Customer concentration 50-60%** | Reduce price 20% | 12% reduction if top customer signs long renewal |
| **Earnout metrics not hit by close** | Remove earnout entirely | Convert to 12-month holdback instead (less risky) |
| **Minor IP gaps** | Reduce price 5% | Indemnify via reps insurance ($250k) |
| **Vendor lock-in (AWS proprietary)** | Reduce price 10% | 6% reduction, post-close portability plan |
| **Data quality issues (duplicates, PII)** | Reduce price 7% | Cleanup budget post-close, 3% reduction |
| **Board doesn't approve sale** | Deal off | Board governance refresher, shareholder vote, then re-propose |

---

## ✅ NOT AN ISSUE (Don't even mention)

Buyer discovers → buyers don't care, doesn't affect price:

- Product roadmap disagrees with buyer's vision (buyer will rebuild anyway)
- Founding team drama (if resolved before LOI, no problem)
- Previous failed acquisition attempts (buyer doesn't know, not your job to say)
- Salaries below market (team staying for earnout, not a problem)
- Office lease expensive (remote-first anyway)
- Legacy integrations with dead APIs (buyer will deprecate)

---

## DECISION TREE (During DD)

```
Buyer finds problem X

  → Is it on the DEAL-KILLER list?
    YES → RUN. Don't negotiate.
    NO  → Continue

  → Is it on the NEGOTIABLE list?
    YES → Agree to price reduction or term change
    NO  → Explain, move on

  → Problem seems new/unique?
    → Assess: can buyer's engineering fix it?
       YES → Not your problem, price stays same
       NO  → You pay via price reduction, data, or escrow
```

---

## TACTICAL SCRIPT

When buyer escalates an issue:

```
Buyer: "You didn't disclose that top customer is on month-to-month contract."

You: "That's accurate. Here's what we know:
  • Customer is 6 months without churn (data attached)
  • We've started their 2-year renewal (signed draft attached)
  • If you want to de-risk: [adjust price 8% OR cap earnout OR extend holdback]
  
  Which tradeoff works for you?"
```

**Key moves:**
- Don't get defensive
- Offer multiple options (price vs. earnout vs. holdback vs. insurance)
- Data > excuses
- If on NEGOTIABLE list = this is normal, you're not trying to hide anything

---

## ESCALATION PROTOCOL

```
Minor issue (< $500k impact):
  Your counsel handles with buyer counsel
  → You approve, move on

Medium issue ($500k - $2M impact):
  You + your counsel call buyer + buyer counsel
  → Agree on tradeoff in 1 call

Major issue (> $2M impact, or earnout-dependent):
  You call buyer CEO directly
  → If can't align → invoke break fee OR renegotiate LOI entirely
```

---

## Common Bluffing Signals (Buyer is negotiating, not walking)

Even if buyer says "this kills the deal," they're probably bluffing if:

- ✓ They've already invested $200k in DD
- ✓ They haven't invoked MAC clause yet
- ✓ They're asking for "adjustments" not walking
- ✓ Board already approved the deal

**Real walk signals:**
- ❌ "We're taking deal to competitor" (and they have one lined up)
- ❌ Board votes no
- ❌ Buyer's revenue drops 40% (MAC clause invoked)
- ❌ Buyer's financing falls through

---

**Last updated**: 2026-06-12
