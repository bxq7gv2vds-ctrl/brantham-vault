# M&A Deal Pipeline Tracker — Airtable/Sheets Template

## Quick Setup (Copy to Google Sheets)

### Schema

| Column | Type | Example | Notes |
|---|---|---|---|
| **Buyer Name** | Text | Acme Corp | |
| **Industry** | Single Select | SaaS / PE / Strategic | Filter by |
| **Stage** | Single Select | Prospecting / Warm / LOI / Close | Key metric |
| **Contact Name** | Text | John Smith (VP Corp Dev) | |
| **Contact Email** | Email | john@acme.com | |
| **Phone** | Phone | +1-555-0123 | |
| **Last Touch Date** | Date | 2026-06-13 | Auto-calculated (today if contacted) |
| **Days Since Last Touch** | Formula | `=TODAY()-[Last Touch Date]` | Red if >10 days |
| **Intro Method** | Single Select | Warm intro / Cold / Advisor / Inbound | Track sourcing |
| **Interest Level** | Rating | ⭐⭐⭐⭐ (4/5) | Your gut assessment |
| **Likelihood to Close** | % | 15% | Your estimate |
| **Price Range** | Currency | $4M–$6M | Your target range |
| **Timeline** | Text | "60–90 days from LOI" | Buyer's estimate |
| **Deal Status Notes** | Text | "Waiting on their CFO review; following up 2026-06-15" | Free text; update weekly |
| **Next Action** | Text | "Send technical due diligence doc" | What YOU do next |
| **Action Owner** | Text | Founder / Advisor | Assign accountability |
| **Due Date** | Date | 2026-06-20 | When to take action |
| **Confidence Signal** | Single Select | CFO involved / Legal engaged / Product demo done / Data room access | High-signal activities |
| **Red Flag** | Text | "CEO changed; unclear if acquisition is still priority" | Anything worrying you |

---

## Sample Data

| Buyer | Stage | Last Touch | Days | Interest | Likelihood | Price | Notes | Next Action | Due |
|---|---|---|---|---|---|---|---|---|---|
| **Acme Corp (Strategic)** | Warm | 2026-06-12 | 1 | ⭐⭐⭐⭐ | 40% | $5M–$6M | VP Corp Dev excited; waiting on CEO sign-off | CEO intro call | 2026-06-20 |
| **Beta PE (Financial)** | LOI | 2026-06-10 | 3 | ⭐⭐⭐ | 60% | $4M–$5M | LOI draft received; legal reviewing | Redline & return LOI | 2026-06-17 |
| **Gamma Tuck-In (Acq)** | Prospecting | 2026-06-05 | 8 | ⭐⭐⭐⭐⭐ | 10% | $3M–$4M | Cold outreach; VP Product replied; scheduling call | Send product demo link | 2026-06-15 |
| **Delta Founder (Angel)** | Warm | 2026-05-30 | 14 | ⭐⭐ | 5% | $2M–$3M | Warm intro 2 weeks ago; no response yet | Re-confirm interest | 2026-06-20 |

---

## Key Metrics

### Sourcing Funnel (This Month)

```
Prospecting:     5 buyers
Warm:           10 buyers
LOI:             2 buyers (Acme, Beta)
Close:           0 buyers (expected 1 in 60 days)
```

**Conversion rates:**
- Prospecting → Warm: 50% (contact them; half will engage)
- Warm → LOI: 20% (high-touch talks; 1 in 5 gets serious)
- LOI → Close: 70% (if LOI, usually closes; rare walk-away)

**Velocity:** 2–3 LOIs per 60 days is healthy.

---

## Status Definitions

| Stage | Definition | Example Actions | Timeline |
|---|---|---|---|
| **Prospecting** | Initial outreach; no response yet | Send email, cold call, LinkedIn | 0–2 weeks |
| **Warm** | They've responded; exploring interest | Product demo, initial call, send overview | 2–4 weeks |
| **Serious** | Multi-call process; diligence questions starting | Share financials, customer list, tech overview | 4–8 weeks |
| **LOI** | Letter of Intent signed; exclusivity active | Diligence, negotiations, legal drafting | 8–12 weeks |
| **Close** | Purchase agreement finalized; closing docs signed | Final walkthrough, wire transfer, earnout setup | 12–16 weeks (or concurrent with LOI final negotiations) |
| **Closed** | Money transferred; integration begins | 100-day integration plan starts | Post-close |

---

## Deal Confidence Scoring

For each buyer in "Warm" or "Serious" stage, score 0–80 points:

| Signal | Points | Evidence |
|---|---|---|
| Intro'd by mutual acquaintance | 10 | Email shows "intro'd by [name]" |
| They requested product demo | 5 | "Can we see your product?" |
| Called you (not you called them) | 5 | Inbound interest |
| VP+ involved in calls | 10 | VP Corp Dev, CEO, or CFO on call |
| Legal engaged (drafting LOI) | 15 | LOI draft shared |
| Reference calls with customers | 15 | "Can we talk to your customers?" |
| Data room access granted | 10 | Buyer's team accessing data |
| Technical diligence requested | 5 | "We'd like to review your code" |
| Financing confirmed (not contingent) | 10 | "We have committed capital" |

**Scoring:**
- 0–20: Exploratory (won't close without significant effort)
- 20–40: Interested (maybe closes; too early to tell)
- 40–60: Serious (likely to close; continue momentum)
- 60–80: Very likely (close within timeline)
- 80+: Closing soon (finalize terms, not strategy)

---

## Weekly Update Ritual

**Every Friday at 4pm (15 minutes):**

1. Update "Last Touch Date" for each deal (did you talk to them this week? If no, it increments)
2. Refresh "Days Since Last Touch" (auto-calculates)
3. Red-flag any deals >10 days silent (send follow-up)
4. Update "Next Action" & "Due Date" based on last call
5. Note any "Deal Status Changes" (e.g., "CFO now involved" or "They're slow-walking")
6. Commit to one action per deal next week

**2-minute example:**
```
🟢 Acme (Warm) — Last touched 2 days ago; CEO intro scheduled 6/20 ✓
🟡 Beta (LOI) — Last touched 3 days ago; waiting on legal review; remind them Monday
🔴 Gamma (Prosp) — Last touched 8 days ago; send follow-up Friday evening
⚫ Delta (Warm) — Last touched 14 days ago; consider walking away if no response by Friday
```

---

## Red Flag Monitoring

**Auto-alerts (add these to your tracker):**

| Condition | Alert | Action |
|---|---|---|
| Last Touch > 7 days | 🔴 Stalled | Send: "Following up on acquisition interest. Still interested?" |
| Last Touch > 14 days | 🔴 🔴 Dead | Mark as "unlikely to close"; move on or walk |
| Interest ≤ 2/5 stars | 🟡 Lukewarm | Focus energy on higher-probability deals |
| Likelihood < 20% but high interest | 🟡 Fishing | Buyer is curious; unlikely to offer; don't waste time |
| Red flag noted (e.g., "CEO unsure") | 🟡 Watch | Reach out to confirm nothing changed |

---

## Negotiation Tracker (Once in LOI)

When a deal moves to "LOI" stage, create a separate sheet:

| Term | Buyer Initial | Your Counteroffer | Latest | Agreed Y/N |
|---|---|---|---|---|
| **Cash at close** | $4.0M | $5.0M | $4.5M | ❌ |
| **Earnout** | $500k | $1.0M | $750k | ✓ |
| **Timeline** | 30 days | 60 days | 45 days | ✓ |
| **Non-compete** | 24m global | 12m narrow | 18m US | ❌ |
| **Founder role** | CEO, 24m | Advisory only | VP Product, 12m | ⏳ |

**Update daily during LOI negotiation.**

---

## Monthly Summary Report

First Friday of each month, create this 1-pager:

```
M&A Pipeline — June 2026

**Stage Distribution:**
- Prospecting: 5 buyers (10% close likelihood)
- Warm: 10 buyers (25% close likelihood)
- Serious: 3 buyers (60% close likelihood)
- LOI: 2 buyers (70% close likelihood)

**Weighted Forecast:**
- Expected closes in next 60 days: 1–2 deals
- Likely price range: $4M–$6M
- Earnout: 20–30% of price

**This Month's Wins:**
- Beta PE moved from Warm → LOI (new LOI!)
- Acme Corp VP Corp Dev scheduled CEO intro (progress)

**This Month's Losses:**
- Delta Founder went silent 2 weeks; marked unlikely to close

**Next Month's Priority:**
- Close Beta PE LOI negotiations
- Move Acme Corp → LOI
- Replace dead deals with 3–5 new warm prospects
```

---

## Quick Start

1. Copy template above to Google Sheets
2. Add your 5–10 current buyer prospects
3. Score each on "Likelihood %" (gut estimate)
4. Sort by "Likelihood" descending
5. Set phone reminders for "Due Date" on next actions
6. Update every Friday (5 minutes)

**Target:** 1 new LOI every 4–6 weeks = healthy pipeline velocity.
