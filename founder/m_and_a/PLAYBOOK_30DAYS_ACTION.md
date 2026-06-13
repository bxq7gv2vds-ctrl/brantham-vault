---
name: playbook-30days-action
description: Feuille de route 30 jours : 15 tâches critiques séquencées, responsable + deadline
metadata:
  type: project
---

# PLAYBOOK 30 JOURS — ACTION SEQUENCE

**Utilité:** Pas de détails, juste ordre du jour + DRI (Directly Responsible Individual) + deadline.  
Tout ce qui bloque soft shop doit être terminé dans cette fenêtre.

---

## PHASE 0 : DÉCISION (Jour 0 — 24h)

### Task 1: Go/No-Go Call
**DRI:** All founders  
**Deadline:** Jour 0 (today)  
**Action:** Complete [AUDIT_READINESS_SELF_CHECK.md](AUDIT_READINESS_SELF_CHECK.md) together. Compare scores. If <20 total, PAUSE. If >20, proceed.

**Output:** Filled audit. Written decision: "We will soft shop" or "We will wait X months and retry."

---

## PHASE 1 : FOUNDATION (Jours 1-7)

### Task 2: Founder Alignment
**DRI:** Lead founder  
**Deadline:** Jour 2  
**Action:** 1-on-1 with each co-founder. Align on: target price, earnout % acceptable, founder stay bonus, walk-away price, timeline.

**Output:** Signed 1-page [Founder Alignment](template_founder_alignment_agreement.md) doc (price range, earnout, tie-breaker if dispute).

---

### Task 3: Cap Table Cleanup
**DRI:** CFO or finance founder  
**Deadline:** Jour 3  
**Action:** Fill [cap_table_template.md](cap_table_template.md) with actuals. Shares, vesting cliffs, options issued, strike prices, warrant exercises. Have each founder sign off.

**Output:** Final cap table. All parties agree on dilution % at each round.

---

### Task 4: BATNA Definition
**DRI:** Lead founder  
**Deadline:** Jour 4  
**Action:** Use [batna_calculator.md](batna_calculator.md). Calculate: (1) cost of staying independent next 3 years, (2) next funding round dilution, (3) "walk away" price. Reference [calculator_cost_of_independence.py](calculator_cost_of_independence.py).

**Output:** BATNA card. "We will not accept <$X. We will walk if deal <$Y."

---

### Task 5: Financials Audit
**DRI:** CFO or bookkeeper  
**Deadline:** Jour 5  
**Action:** Compile clean 24-month historique: P&L, cash flow, AR aging, churn rate, NRR. Use [checklist_dd_financial_response.md](checklist_dd_financial_response.md). Flag any anomalies (one-time revenue, seasonal dips, margin decline).

**Output:** Clean financials file. Auditor review (not full audit, just fact-check). Aucun "buyer surprise" possible.

---

### Task 6: Key Risk Inventory
**DRI:** Product + Tech lead  
**Deadline:** Jour 6  
**Action:** Itemize top 5 product/tech risks buyer will find: tech debt, customer concentration, feature gaps, churn drivers, architecture issues. Be honest. Use [red_flags_m_et_a.md](red_flags_m_et_a.md) as checklist.

**Output:** 1-page risk doc. "Here's what buyer will discover, and why we're not worried because..." (prep for DD).

---

### Task 7: Legal Baseline
**DRI:** Counsel or founder  
**Deadline:** Jour 7  
**Action:** Confirm: (1) IP is consolidated under company, (2) customer contracts have no "change of control" blockers, (3) employment is fully compliant (no payroll tax owing), (4) no pending litigation. Use [warranty_indemnity_risks.md](warranty_indemnity_risks.md).

**Output:** Legal sign-off memo. "We are aware of no material liability."

---

## PHASE 2 : VALUATION & PRICE (Jours 8-14)

### Task 8: DCF Build
**DRI:** CFO  
**Deadline:** Jour 8  
**Action:** Complete [valuation_dcf_template.md](valuation_dcf_template.md). 5-year forecast: revenue (conservative + base + stretch), margin, WACC, terminal value. Build 3 scenarios.

**Output:** DCF model. "Fair value = $X-$Y. Anchor price (1.3×) = $Z."

---

### Task 9: Comparable Analysis
**DRI:** CFO or analyst  
**Deadline:** Jour 9  
**Action:** Find 5-8 recent SaaS deals in your segment (similar ARR, growth, churn). Extract multiples (price/ARR, price/EBITDA). Reference [benchmarks_saas_valuation_2026.md](benchmarks_saas_valuation_2026.md).

**Output:** Comps table. "Market is paying 6-8× ARR for [your segment]."

---

### Task 10: Price Range Decision
**DRI:** Lead founder + CFO  
**Deadline:** Jour 10  
**Action:** Combine DCF + comps + BATNA. Write down: (1) Walk-away price, (2) Fair value range, (3) Anchor price (opening ask), (4) Ceiling (take-it-now). Store only in vault (never email).

**Output:** Pricing strategy doc (confidential). "We anchor at $X. Fair value is $X-$Y. We walk away at <$Z."

---

### Task 11: Earnout Modeling
**DRI:** CFO  
**Deadline:** Jour 11  
**Action:** Use [calculatrice_earnout.md](calculatrice_earnout.md). Model: (1) what earnout % is fair, (2) what metric (ARR growth, profit, customer count), (3) 3-year payout schedule. Calculate risk-adjusted expected value.

**Output:** Earnout scenarios. "We prefer all-cash, but if earnout, structure must be: $X upfront, $Y on 3-year ARR growth milestone."

---

### Task 12: Advisor/Broker Decision
**DRI:** Lead founder  
**Deadline:** Jour 12  
**Action:** Decide: hire M&A advisor (broker) or do self-directed soft shop? Reference [advisor_selection_fees.md](advisor_selection_fees.md). If hiring, vet 3-5 brokers (fees, references, warm intros to buyers).

**Output:** Signed engagement letter (if advisor) OR written decision to self-direct.

---

### Task 13: Buyer List Draft
**DRI:** Lead founder + CFO  
**Deadline:** Jour 13  
**Action:** Use [buyer_profiles_signals.md](buyer_profiles_signals.md) + [scoring_matrix_target_saas.md](scoring_matrix_target_saas.md). List 15-20 potential buyers (strategic + PE + venture). Score each: (1) fit (synergies?), (2) cash (can afford?), (3) speed (decision time?).

**Output:** Ranked buyer list. "Top 5 targets: [Company A], [Company B], [Company C]..."

---

### Task 14: Teaser Deck Outline
**DRI:** Lead founder  
**Deadline:** Jour 14  
**Action:** Draft slide structure (no numbers, no price): Slide 1 = problem/size, Slide 2 = solution, Slide 3 = traction (generic), Slide 4 = why now. Reference [pitch_deck_buyer_targeting.md](pitch_deck_buyer_targeting.md). Design should be clean, not hype.

**Output:** Draft deck (Figma/Keynote). Slide count = 5-8. No valuations, no pricing.

---

## PHASE 3 : OUTREACH & LOI (Jours 15-30)

### Task 15: Soft Shop Kickoff
**DRI:** Lead founder (or advisor)  
**Deadline:** Jour 15  
**Action:** Send NDA (use [nda_template_seller.md](nda_template_seller.md)) + teaser to top 5 buyers. Personal email from founder. Tone: exploratory, not desperate. "Exploring strategic options." Reference [buyer_outreach_playbook.md](buyer_outreach_playbook.md) for template.

**Output:** 5 emails sent. NDA signed back within 5 days. Expect 2-3 meetings scheduled.

---

### FINAL CHECKPOINT (Day 30)

**Expected state:**
- [ ] Founder alignment = locked in
- [ ] Cap table = clean + signed
- [ ] BATNA = written + agreed
- [ ] Financials = audited for buyer surprises
- [ ] Price range = defined (confidential)
- [ ] Top 5 buyers = identified + ranked
- [ ] Teaser deck = drafted
- [ ] Soft shop = launched (3-5 buyers have NDA + teaser)

**Metrics:**
- Target = 2-3 LOI discussions started by Day 30
- If <1, either buyer list weak OR teaser deck isn't compelling. Iterate.

---

## OWNER & TIMELINE

| Task | DRI | Day Due | Status |
|------|-----|---------|--------|
| Go/No-Go | Founders | 0 | |
| Founder Alignment | Lead | 2 | |
| Cap Table | CFO | 3 | |
| BATNA | Lead | 4 | |
| Financials | CFO | 5 | |
| Risk Inventory | Tech | 6 | |
| Legal Baseline | Counsel | 7 | |
| DCF | CFO | 8 | |
| Comps | CFO | 9 | |
| Price Decision | Lead+CFO | 10 | |
| Earnout Model | CFO | 11 | |
| Advisor Decision | Lead | 12 | |
| Buyer List | Lead+CFO | 13 | |
| Teaser Outline | Lead | 14 | |
| Soft Shop Kickoff | Lead | 15 | |

---

**Start Date:** _________  
**Day 15 Checkpoint:** _________  
**Day 30 Checkpoint:** _________
## Related
