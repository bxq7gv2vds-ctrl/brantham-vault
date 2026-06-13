---
name: deal_decision_tree_quick
description: 10-question flowchart to go/no-go on a buyer (2 min to answer)
type: tool
created: 2026-06-13
status: production
---

# DEAL DECISION TREE — 2-MINUTE GO/NO-GO

**Purpose:** Kill bad deals early. 10 binary questions = clear GO or NO-GO  
**When to use:** After receiving LOI, before engaging lawyers/advisors  
**Time:** 2 minutes  

---

## THE FLOWCHART

```
START: "Should I pursue this deal?"
    │
    ├─ Q1: Did buyer provide valuation ≥ your minimum ask (BATNA)?
    │   ├─ NO  → See "VALUATION PATH" (below)
    │   └─ YES → Q2
    │
    ├─ Q2: Is >80% of deal price due at close (not earnout)?
    │   ├─ NO  → See "EARNOUT PATH" (below)
    │   └─ YES → Q3
    │
    ├─ Q3: Can you get 30-day wire transfer + cash in escrow?
    │   ├─ NO  → See "PAYMENT RISK" (below)
    │   └─ YES → Q4
    │
    ├─ Q4: Has buyer closed ≥2 similar deals in past 3 years?
    │   ├─ NO  → See "FIRST-TIME BUYER" (below)
    │   └─ YES → Q5
    │
    ├─ Q5: Are you staying on post-close (title/role defined)?
    │   ├─ NO  → See "EXIT STRATEGY" (below)
    │   └─ YES → Q6
    │
    ├─ Q6: Do you have <20% customer concentration (top 3 = <60% ARR)?
    │   ├─ NO  → See "CUSTOMER RISK" (below)
    │   └─ YES → Q7
    │
    ├─ Q7: Is earnout logic (if any) based on YOUR metrics, not combined?
    │   ├─ NO  → See "EARNOUT MANIPULATION" (below)
    │   └─ YES → Q8
    │
    ├─ Q8: Is buyer NOT a direct competitor or "acqui-hire" type?
    │   ├─ NO  → See "COMPETITOR PATH" (below)
    │   └─ YES → Q9
    │
    ├─ Q9: Do you trust the buyer's CFO/COO (gut check)?
    │   ├─ NO  → See "TRUST ISSUE" (below)
    │   └─ YES → Q10
    │
    └─ Q10: Would you feel OK explaining this to investors/advisors?
        ├─ NO  → ❌ NO-GO (something feels wrong)
        └─ YES → ✅ GREEN LIGHT (proceed with negotiation)
```

---

## PATH 1: VALUATION SHORTFALL

**Q1 = NO: Valuation < BATNA**

| If gap is... | Your move |
|---|---|
| **<5% below ask** | Counter with DCF justification, see if they move |
| **5-15% below ask** | Ask for earnout bumps or better payment terms to close gap |
| **15-25% below ask** | Demand urgent face-to-face with their CFO (maybe they misunderstood your business) |
| **>25% below ask** | ❌ **KILL IT.** You'll regret it post-close. See `batna_card_template.md` |

**Action:** Re-read `valuation_defense_playbook.md` + run `financial_normalization_template.md`

---

## PATH 2: EARNOUT DOMINATES (>50% of deal price)

**Q2 = NO: ≤80% cash at close**

| Earnout % | Scenario | Risk Level | Next Step |
|---|---|---|---|
| **20-35%** | Standard (acceptable) | 🟢 Low | Proceed to Q3 |
| **35-50%** | Elevated | 🟡 Medium | Demand 1-year max, NOT 3-year. See `template_earnout_calculator.md` |
| **50-75%** | High | 🔴 High | Walk unless buyer is top-10 public co with perfect track record |
| **>75%** | Unrealistic | 🔴 Critical | ❌ **KILL IT.** You're financing their acquisition. Not a real offer. |

**Action:** Run `earnout_failure_playbook.md` to see all ways buyer can deprioritize post-close

---

## PATH 3: PAYMENT RISK

**Q3 = NO: <30-day wire + escrow unclear**

| Payment scenario | Red flag? | What to demand |
|---|---|---|
| **Day 1: 100% wired** | 🟢 No | Great (standard for strategic acquirers) |
| **Day 30: 100% wired** | 🟢 No | Acceptable (typical for mid-market) |
| **Day 60: 100% wired** | 🟡 Maybe | Ask why. If no good reason, push for escrow release timeline |
| **Day 90+: Partial wire** | 🔴 Yes | Seller financing? That's their problem, not yours. |
| **Earnout depends on buyer funding** | 🔴 Critical | ❌ **KILL IT.** Earnout becomes non-recourse. |

**Action:** Demand `reps_and_warranties_insurance.md` to back up earnout

---

## PATH 4: FIRST-TIME BUYER

**Q4 = NO: <2 acquisitions in track record**

| Buyer profile | Risk | Mitigant |
|---|---|---|
| **Startup acquiring first time** | 🔴 High | Demand escrow 40%+, reps & warranties insurance, lawyer-friendly SPA terms |
| **PE fund, 1st acquisition ever** | 🟡 Medium | OK if well-funded and experienced founder in team. Demand strong SPA |
| **Strategic, first in category** | 🟡 Medium | Check if they acquired in OTHER categories (signals competence) |
| **Acquired before but not closing** | 🔴 Critical | ❌ **KILL IT** (unless there's a blameless reason — market crash, etc) |

**Action:** Request Crunchbase/PitchBook history + talk to founders of their prior acquisitions

---

## PATH 5: EXIT STRATEGY

**Q5 = NO: You're not staying post-close**

| Scenario | OK? | Comment |
|---|---|---|
| **"Clean exit" — you leave immediately** | 🟢 Yes | OK if earnout is ZERO or <10%, paid from escrow not operations |
| **"Founder advisor" — 6-month role** | 🟡 Maybe | Can work if you're NOT measured on earnout KPIs. Otherwise you're stuck. |
| **"You're CEO until Y1 ends"** | 🟡 Maybe | Earnout likely tied to your performance. Demand retention bonus separate from earnout. |
| **"You leave, earnout = $0"** | 🔴 Red flag | Buyer is signaling they don't value you post-deal. Why are they acquiring? |

**Action:** Review `founder_transition_guide.md` — negotiate your exact role + comp NOW (before LOI)

---

## PATH 6: CUSTOMER CONCENTRATION

**Q6 = NO: Top 3 customers = >60% ARR**

| Concentration | Risk | Mitigation |
|---|---|---|
| **Top 3 = 40-50% ARR** | 🟡 Medium | Acceptable if churn <3% + long contracts |
| **Top 3 = 50-60% ARR** | 🔴 High | Buyer will demand earnout heavily weighted to THEM (see escrow ↑) |
| **Top 3 = 60-75% ARR** | 🔴 Critical | Buyer will discount valuation 20-30%. Renegotiate or walk. |
| **Top 3 = >75% ARR** | 🔴 Kill-level risk | ❌ **Your valuation isn't real.** It depends entirely on 3 customers staying. |

**Action:** Provide `template_customer_concentration_analysis.md` with churn trend + retention letter from top 3 customers

---

## PATH 7: EARNOUT IS BUYER-CONTROLLED

**Q7 = NO: Earnout based on "combined company" metrics**

| Earnout basis | Manipulation risk | Fix |
|---|---|---|
| **YOUR standalone ARR** | 🟢 Low | Good — buyer can't game this as easily |
| **Combined ARR (yours + theirs)** | 🔴 High | Buyer can slow marketing to your product → earnout dies |
| **"Contribution to buyer profit"** | 🔴 Critical | Buyer allocates costs → earnout = $0. ❌ **WALK.** |
| **"Whatever buyer decides Q&A shows"** | 🔴 Trap | You're signing blank check. ❌ **KILL IT.** |

**Action:** Demand `standalone_metric_definition.md` in SPA Exhibit A (exact ARR calc = YOUR business only)

---

## PATH 8: COMPETITOR TRAP

**Q8 = NO: Buyer is direct competitor or acqui-hire**

| Type | Risk | Outcome post-close |
|---|---|---|
| **Direct competitor (same market)** | 🔴 High | Buyer kills your product, users migrate to theirs (earnout dies) |
| **Acqui-hire (buying team, not product)** | 🟡 Medium | Your product gets shelved. Earnout likely = $0. You're now employee of acquirer |
| **Complement (not competing)** | 🟢 Low | Product lives, gets integrated. Standard acquisition. |
| **"Kill competitor" tuck-in** | 🔴 Kill-level | ❌ **Don't sell if you're not comfortable with shutdown.** |

**Action:** Ask buyer directly: "Walk me through post-close roadmap for my product." If vague = red flag.

---

## PATH 9: TRUST ISSUE

**Q9 = NO: You don't trust their CFO/COO**

**This is the gut check.** Red flags:
- ❌ They won't share cap table or recent financials
- ❌ Vague on how earnout will be calculated
- ❌ Changed story between first call and LOI
- ❌ Avoided your due diligence questions
- ❌ They seem desperate (negative signal — why?)

**Action:** 
- Call someone who worked with them (LinkedIn, email intro)
- Ask your advisor: "Do you feel OK about this buyer?"
- If advisor hesitates = walk

---

## PATH 10: ADVISOR SMELL TEST

**Q10 = NO: You feel uncomfortable explaining this deal**

**This is your final veto.** If you can't explain to investors/friends why this makes sense = something's wrong.

Common reasons:
- ❌ Valuation feels low but you can't articulate why
- ❌ Earnout terms are too aggressive
- ❌ Buyer's culture is toxic
- ❌ You'd be lying to your team about post-close plans
- ❌ Deal structure punishes failure too hard

**Action:** **WALK.** You'll feel better in 6 months. A bad deal is worse than no deal.

---

## SCORING SUMMARY

```
✅ Green lights (all Q1-Q10 = YES)
   → Proceed with negotiation
   → Engage M&A counsel + advisor
   → Expect close in 60-90 days

🟡 1-2 yellow flags (some questions = context-dependent)
   → Proceed, but get lawyer review + advisor input
   → Address issues in LOI redline
   → Expect negotiation + 90-120 days to close

🔴 1+ red flag (any path 1-8 triggered)
   → Address immediately or walk
   → Red flags compound risk exponentially
   → Don't ignore your gut

❌ Kill signals (earnout >50%, customer concentration >70%, trust issue, competitor trap)
   → Walk now. Better deals exist.
   → Your time is worth more than fighting these battles.
```

---

## USAGE

Print this + fill out during LOI review (takes 2 min). Share with your M&A lawyer + advisor. Use their input to decide whether to proceed.

**Related:**
- `batna_card_template.md` — Know your walkaway price before using this
- `integration_risk_matrix_2_0.md` — What happens if you proceed with yellow/red flags
- `FOUNDER_NEGOTIATION_SCRIPTS.md` — What to say when answering these Qs to buyer
