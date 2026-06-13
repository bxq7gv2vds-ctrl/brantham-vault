---
name: pricing_strategy_initial_ask
description: How to set your initial asking price — multiples, comps, scenarios, anchoring
type: playbook
date: 2026-06-13
---

# HOW TO SET YOUR INITIAL ASKING PRICE

**Timeline:** Deploy 1–2 weeks *before* outreach  
**Effort:** 30–60 min  
**Output:** Your "magic number" + confidence range (−20% / +30%)

---

## STEP 1: GATHER YOUR NUMBERS (10 min)

**You need:**
- **Revenue (last 12 mo)** — GTM, subscriptions, SaaS ARR
- **EBITDA or net profit** — Last 3 years (trend matters)
- **Growth rate** — YoY %, especially last 2 quarters
- **Customer concentration** — Top 5 revenue %
- **Churn rate** — Monthly or annual % (or NPS if pre-revenue)
- **Cash on hand** — How much runway you have (zero/debt affects price)

**If pre-revenue or nascent:**
- Users or DAU (daily active users)
- Market size expansion (3-year addressable market)
- Founder/team pedigree (raised money from VC? Prior exits?)

---

## STEP 2: APPLY THE FOUR METHODS

### Method 1: **SaaS Multiples** (Most Common)

**Formula:** `Revenue × Multiple = Valuation`

**Benchmark multiples by growth rate:**

| ARR | Growth | Multiple | Example |
|-----|--------|----------|---------|
| $1–5M | <40% YoY | 3–5× | $3M ARR @ 4× = $12M |
| $5–10M | 40–100% YoY | 5–8× | $7M ARR @ 7× = $49M |
| $10M+ | >100% YoY | 8–15× | $15M ARR @ 12× = $180M |

**How to use:**
1. Find your ARR + growth rate
2. Look up the range in table above
3. Pick conservative (low), base case (mid), aggressive (high)
4. This gives you 3 scenarios

**Example (hypothetical SaaS startup):**
- ARR: $2.5M
- Growth: 85% YoY
- Land in: "$5–10M with 40–100% growth" row
- Multiple range: 5–8×
- **Conservative:** $2.5M × 5 = **$12.5M**
- **Base case:** $2.5M × 6.5 = **$16.25M**
- **Aggressive:** $2.5M × 8 = **$20M**

---

### Method 2: **Industry Comps** (Anchor Validation)

**Find 3–5 public or recent M&A deals in your space:**

**Where to find:**
- PitchBook, Crunchbase, TechCrunch (recent M&A announcements)
- LinkedIn (message founders of acquired companies, ask for range)
- SEC filings (if you have public comps)

**Extract from each:**
- Acquisition price
- Target's revenue at time of acquisition
- Implied multiple
- Growth rate (if available)

**Example comps table:**

| Company | Year | Revenue | Price | Multiple | Growth |
|---------|------|---------|-------|----------|--------|
| Comp A | 2025 | $5M | $40M | 8× | 60% |
| Comp B | 2024 | $3.2M | $24M | 7.5× | 50% |
| Comp C | 2026 | $6M | $50M | 8.3× | 80% |
| **Average** | — | — | — | **7.9×** | **63%** |

**Your comparable:** $2.5M ARR × 7.9× = **$19.75M**

---

### Method 3: **DCF (Discounted Cash Flow)**

**For buyers who demand it** (bigger acquirers, strategic buyers).

**Simple 5-year DCF:**

```
Year 1: Net cash flow (after ops) = $X
Year 2: $X × (1 + growth %)
Year 3: $X × (1 + growth %)^2
...
Terminal value = Year 5 cash × (1 + perpetual growth %) / (discount rate - growth %)

Present value = Sum of discounted years + discounted terminal value
```

**Conservative assumptions:**
- Perpetual growth: 3% (market maturity)
- Discount rate (WACC): 10–15% (risk of M&A integration)

**Aggressive assumptions:**
- Perpetual growth: 8% (if you're a platform winner)
- Discount rate: 8% (low risk, large platform)

**You probably won't need this for your initial ask,** but have it ready for LOI phase if buyer pushes back on multiples.

---

### Method 4: **Risk-Adjusted Haircut**

**Deduct for risks that reduce buyer confidence:**

| Risk | Haircut |
|------|---------|
| Customer concentration >30% | −10% |
| Churn rate >10% annually | −10% |
| Founder-dependent (no COO/CFO) | −15% |
| Pre-product-market-fit (early stage) | −20–40% |
| Declining revenue (last 2 quarters) | −15% |
| Technical debt / legacy codebase | −10% |
| Zero IP / all open-source | −20% |
| No moat (easy to replicate) | −15% |

**Example:** Your base case is $16.25M.
- Customer concentration: −10%
- Early technical debt: −10%
- **Adjusted:** $16.25M × 0.8 = **$13M**

---

## STEP 3: TRIANGULATE YOUR RANGE

**You now have 4 data points:**

| Method | Result |
|--------|--------|
| Multiples (base case) | $16.25M |
| Multiples (aggressive) | $20M |
| Comps validation | $19.75M |
| Risk-adjusted | $13M |

**Your pricing strategy:**

| Price Point | Use Case |
|-------------|----------|
| **$13M** | Walk-away minimum (risk-adjusted reality) |
| **$16.25M** | Initial ask (credible, data-backed) |
| **$19.75M** | High-end anchor (claim comps, then negotiate) |
| **$20M** | Absolute ceiling (never go above, even if pushed) |

---

## STEP 4: ANCHOR & ANCHORING PSYCHOLOGY

**Rule:** Whoever speaks a number first anchors the negotiation.

**You want to anchor:**
- **Email:** Mention $16.25M–$19.75M *before* a call (email gives you time to compose, less pressure)
- **Call:** Let buyer speak first (forces them to anchor low, you counter-push)
- **Written teaser:** "Asking price: $16–20M" (range feels more credible than exact)

**Anchoring examples:**

❌ **Bad:** No mention of price in initial email → Buyer opens with "$8M, take it or leave it"

✅ **Good:** "We're looking at a $16–20M range based on SaaS multiples + comps. Happy to discuss" → Buyer anchors at $15M (closer to your ask)

---

## STEP 5: PREPARE COUNTER-ANCHORING RESPONSES

**When buyer says:** "That's way too high, we're thinking $10M"

**You say (pick one):**

1. **Comps** — "SaaS companies at our growth rate ($2.5M ARR, 85% YoY) trade at 6.5–8× in market. That's $16–20M. I've got 3 recent comps I can share."

2. **Multiple math** — "Our ARR is $2.5M growing 85% YoY. Your team just closed [Competitor Y] at $20M ARR × 8× = $160M. We're smaller but higher growth. 7× gets us to $17.5M."

3. **Growth story** — "We're 6 months away from $3.5M ARR. At $10M, you're buying us at 2.8× on trailing. That's pre-market-fit pricing. Wait 6 months and it's 3× anyway."

4. **Walk-away** — "I appreciate the offer, but $10M doesn't reflect our growth trajectory or market comps. I'm looking at $16M+. If you can't get there, let's revisit in 6 months."

---

## STEP 6: BUILD YOUR BATNA (Walk-Away Price)

**What's the *lowest* you'll accept?**

- **Option 1:** Continue bootstrapping (how long runway? what profit?)
- **Option 2:** Raise another round of VC (what valuation?)
- **Option 3:** Sell to a different buyer at a better price (2–3 other options in pipeline?)

**Your BATNA price = Walk-away price**

Example:
- Base case ask: $16.25M
- BATNA (lowest walk-away): $12.5M (conservative multiple method)
- Target (ideal): $20M (aggressive multiple + comps validation)

**In negotiation:** Never disclose your BATNA. Use it internally to know when to walk.

---

## QUICK REFERENCE CARD

**Fill this in before your first buyer call:**

```
COMPANY: _______________
ARR (last 12 mo): $ _______________
YoY Growth: ________ %

VALUATION RANGE:
  Conservative (low multiple): $ _______________
  Base case (your ask): $ _______________
  Aggressive (ceiling): $ _______________
  Risk-adjusted minimum: $ _______________

MY INITIAL ASK: $ _______________
MY BATNA (walk-away): $ _______________

TOP 3 COMP MULTIPLES: _____× , _____× , _____×

OPEN TO ADJUST FOR:
  ☐ All-cash (vs earnout)
  ☐ Faster integration (extra $X for quick exit)
  ☐ Equity in acquirer (upside vs certainty trade)
```

---

## COMMON MISTAKES

| Mistake | Why It Fails | Fix |
|---------|-------------|-----|
| Ask for $50M when ARR is $2M | Buyer laughs, walks out | Use method 1–2, not wishful thinking |
| Ask same price to all buyers | Strategic buyers pay 2–3× more than PE | Segment your ask ($16M for PE, $25M for strategic) |
| Disclose your BATNA | Buyer anchors below it | Keep it secret, internal only |
| Never move from initial ask | Signals either desperation or stubbornness | Move 5–10% per round, max |
| Ignore risk-adjusted haircut | Buyer brings it up, you look naive | Own your risks, pre-adjust, regain credibility |

---

## NEXT ACTIONS

1. **Fill the quick reference card above** (5 min)
2. **Gather 3–5 comparable M&A deals** in your space (10 min)
3. **Calculate your 4 scenarios** (multiples, comps, DCF, risk-adjusted) (15 min)
4. **Write your initial email** using `email_templates_m_and_a.md` → Mention your range in sentence 2

---

**Related files:**
- `12_MULTIPLES_BENCHMARKS_INDUSTRY.md` — By-industry multiples (SaaS vs marketplace vs B2C)
- `email_templates_m_and_a.md` — How to mention price in outreach
- `competitive_response_playbook.md` — Counter when buyer lowballs you
- `financial_normalization_template.md` — Build EBITDA defense for your price

