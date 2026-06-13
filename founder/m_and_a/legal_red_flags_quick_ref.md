---
name: legal_red_flags_quick_ref
description: 30 SPA clauses to audit in 5 minutes — Red flags, what to push back, why it matters
type: reference
date: 2026-06-13
---

# LEGAL RED FLAGS — SPA QUICK REFERENCE

**Use case:** SPA (Share Purchase Agreement) just arrived. You have 30 min to identify deal-breakers.  
**Format:** 30 clauses organized by risk level (🔴 critical, 🟡 negotiate, 🟢 minor)  
**Effort:** 5–10 min to scan. 30 min to negotiate.

---

## 🔴 CRITICAL (Deal-breaker level)

**If you see these, escalate to your lawyer immediately. These can kill the deal.**

| # | Clause | Red Flag | What to Do |
|---|--------|----------|-----------|
| 1 | **Representations & Warranties** (R&W) | Unlimited survival (e.g., "5-year tail" or no sunset) | Negotiate: 12–18 month tail max for most, 3 years for IP/tax only |
| 2 | **Indemnification basket** | Basket >2% of purchase price, or no minimum claim amount | Counter: Basket should be 0.5–1% of price; minimum claim $25K |
| 3 | **Indemnification cap** | No cap on founder indemnity (unlimited liability) | Counter: Cap at 15–20% of purchase price; carve-out for fraud only |
| 4 | **Earnout clawback** | Earnout can be clawed back indefinitely for failures defined post-close | Counter: Earnout clawback only for fraud; define metrics upfront, no retroactive changes |
| 5 | **IP indemnity** | Broad IP indemnity without carve-out for open-source or licensed code | Counter: Exclude all open-source (Apache, MIT, GPL), vendor licenses, and 3rd-party APIs |
| 6 | **Earn-out condition** | Metrics defined vaguely (e.g., "achieve revenue goals at buyer's discretion") | Counter: Objective KPIs only (revenue, churn, NPS); buyer cannot change definition mid-way |
| 7 | **Change of control** | Customer contracts have termination rights if acquired (you lose revenue post-close) | Counter: Get written waiver from top 5 customers *before* signing SPA; if not possible, reduce price by that revenue |
| 8 | **Founder non-compete** | Non-compete 5+ years, nationwide or global, blocks all SaaS/adjacent verticals | Counter: 2–3 years, geographic limit (1 country), narrow (direct competitor only, not entire category) |
| 9 | **Funds escrow** | Money held back >15% of price, or escrow release tied to impossible conditions | Counter: <10% escrow; release on 12-month anniversary regardless of earnout performance |
| 10 | **Tax indemnity** | Unlimited tax indemnity tail (buyer indemnified for founder's past tax issues indefinitely) | Counter: Tax indemnity capped at purchase price; survival 5–7 years max |

---

## 🟡 NEGOTIATE (High-priority, but not deal-killers)

**You can live with these, but push back. This is where deals are won/lost.**

| # | Clause | Red Flag | Counter-Offer |
|---|--------|----------|---|
| 11 | **Condition precedent: Employee retention** | Buyer can reduce purchase price if >X% of employees leave before close | Counter: Reduce threshold (e.g., >20% vs >10%); limit price reduction to 5–10% max |
| 12 | **Earnout trigger** | Earnout tied to metrics you don't control (e.g., buyer's sales team performance) | Counter: Tie only to metrics you control (product, churn, NPS, customer acquisition); exclude buyer's P&L |
| 13 | **Material Adverse Effect (MAE)** | Overly broad definition (e.g., any revenue dip >5%) | Counter: MAE only for existential threats (loss of customer >25% revenue, key employee death, regulatory ban) |
| 14 | **Affiliate transactions** | Buyer can sell your company to a third party without founder consent | Counter: Add consent right for certain buyers (e.g., direct competitor, hostile acquirer); right of first refusal |
| 15 | **Amend & restate** | Buyer can force you to amend articles of incorporation / bylaws post-close without consent | Counter: Require founder consent for any amendments affecting founder rights for 12–24 months |
| 16 | **Covenant: Financial forecasting** | Seller required to provide "best efforts" forecast of next 3 years; miss = damages | Counter: Change to "reasonable efforts"; cap damages for forecast misses at X amount |
| 17 | **Pro-rata earnout** | If earnout is $2M, but buyer delays initiatives, you only get $1M earnout (pro-rated) | Counter: Earnout is minimum; bonus tied to actual performance, not buyer's execution |
| 18 | **Buyer can change business model** | Buyer can pivot product away from your roadmap without reducing earnout targets | Counter: Earnout targets only apply if buyer keeps product/customer base within X% of pre-close state |
| 19 | **Clawback for customer refunds** | If customer demands refund after close (chargeback, dispute), earnout reduced | Counter: Only for fraudulent refunds; exclude legitimate chargebacks (credit card reversals don't trigger clawback) |
| 20 | **Data room access post-close** | Buyer retains access to your confidential data (customer lists, pricing, source code) indefinitely | Counter: Data room access terminates 12 months post-close; exceptions for litigation/regulatory |

---

## 🟢 MINOR (Worth noting, but won't tank the deal)

**These are common, buyer-friendly clauses. You can negotiate softly or accept.**

| # | Clause | Red Flag | Negotiation |
|---|--------|----------|---|
| 21 | **Purchase price adjustment** | Post-close true-up for working capital, inventory, etc. (net adjustment ±5% of price) | Accept: Standard practice. Ensure calculation method is clear upfront. |
| 22 | **Broker fees** | Buyer pays transaction fees (if you used a broker). Cost reduces your take-home. | Accept: Usually unavoidable. Negotiate who pays (ideally buyer). |
| 23 | **Exclusive remedy** | Indemnification is sole remedy for breaches (no fraud exception) | Push back lightly: Add carve-out for fraud / willful breach. |
| 24 | **Escrow agent** | Buyer-selected escrow agent (buyer picks the referee = bias) | Counter: Mutually agreed escrow agent (e.g., Wilmington Trust, Computershare). |
| 25 | **Dispute resolution** | Disputes go to arbitration (binding, faster) vs litigation (slower, appeals available) | Accept: Arbitration is actually faster for you. Specify arbitrator location (neutral ground). |
| 26 | **Governing law** | Delaware (buyer's favorite, pro-buyer case law) vs your home state | Accept Delaware: Standard for M&A. Likely won't matter. |
| 27 | **Closing conditions** | Buyer retains right to walk if anything material changes (soft MAC) | Accept: Standard risk allocation. Ensure "material" is defined tightly (see MAE definition). |
| 28 | **Seller lockup** | You can't sell shares of buyer for 180 days post-close (if deal is part stock) | Accept: Standard, reduces insider trading risk. Often waived for founders. |
| 29 | **Consent letters** | Buyer wants letters from top 3 customers confirming they'll stick post-close | Accept: Standard. You already know the answer; helps smooth transition. |
| 30 | **Definition of EBITDA** | Buyer uses their specific definition (add-backs differ from yours) | Negotiate: Get buyer's definition in writing upfront; match in earnout KPIs. |

---

## RAPID AUDIT CHECKLIST

**Print this. Scan your SPA in <10 min:**

```
🔴 CRITICAL — STOP if ANY of these are hostile:
  ☐ R&W survival >18 months?
  ☐ Indemnity cap >20% of price OR no cap?
  ☐ Earnout clawback unlimited or undefined?
  ☐ IP indemnity includes open-source without carve-out?
  ☐ Earnout metrics defined vaguely (buyer discretion)?
  ☐ Top 3 customers can terminate if acquired?
  ☐ Founder non-compete >3 years?
  ☐ Escrow >15% of price?

🟡 NEGOTIATE — HIGH PRIORITY:
  ☐ Employee retention tied to >20% threshold?
  ☐ Earnout driven by buyer's execution (not your metrics)?
  ☐ MAE definition includes minor revenue dips (<25%)?
  ☐ Buyer can pivot product without adjusting earnout?
  ☐ Clawback for routine customer refunds?
  ☐ Data room access extends >12 months?

🟢 MINOR — Acceptable if needed:
  ☐ Working capital adjustment ±5%?
  ☐ Escrow agent buyer-selected (but push for neutral)?
  ☐ Dispute resolution = arbitration?
  ☐ Non-compete in buyer's home state law?
```

---

## COMMON NEGOTIATION MOVES

### If Buyer Pushes Hard on R&W Survival

**Buyer wants:** 3–5 year tail (protect against hidden liabilities)  
**You counter:** 
- 18 months for general R&W
- 3 years for IP/tax only
- Baskets/caps that reduce risk for buyer (cheaper insurance)

### If Buyer Adds Clawback for Earnout

**Buyer wants:** If any customer churns, earnout is reduced proportionally  
**You counter:**
- Earnout is *minimum*, not claw-able
- Carve-out: Exclude churned customers from earnout metric (not a reduction)
- Alternative: Earnout is fixed; buyer holds retention bonus separately

### If Buyer Owns Your Metrics Post-Close

**Buyer wants:** "Achieve revenue goal of $X or earnout is zero" (buyer controls sales spend)  
**You counter:**
- Metric = unit economics (LTV, CAC, churn) that you control, not gross revenue
- Gross revenue only if buyer commits $Y to sales/marketing
- Revenue earnout capped at "reasonable growth" (e.g., 20% YoY); faster = claw-able

---

## IF YOU'RE STUCK, CALL YOUR LAWYER

**Red flag indicators you need legal:**
- Clause 1, 3, 4, 6, or 10 is non-standard
- Earnout is >40% of total deal value (high risk)
- Founder employment/non-compete duration >3 years
- Indemnity basket or cap is >$1M or undefined
- You don't understand a clause (don't assume it's fine)

---

## RELATED DOCUMENTS

- `warranty_indemnity_risks.md` — Deep dive on warranties/indemnities (1.5h read)
- `founder_transition_guide.md` — Non-compete and role negotiations
- `preclosing_checklist_100.md` — Full SPA review (item 43–60 = legal clauses)
- `competitive_response_playbook.md` — If you're negotiating price simultaneously

