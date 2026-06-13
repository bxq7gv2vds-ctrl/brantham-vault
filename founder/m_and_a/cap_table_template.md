---
name: cap_table_template
description: Cap table template avec vesting, liquidation préférence, et scénarios post-vente
metadata:
  type: template
  created: 2026-06-12
---

# Cap Table Template — M&A Ready

**Purpose:** Show all equity holders, vesting status, dilution, and payoff post-acquisition.

---

## Structure Minimale

| Name | Type | Shares | % | Strike | Vesting | Status |
|------|------|--------|---|--------|---------|--------|
| Founder A | Common | 500k | 40% | — | Vested | Employee |
| Founder B | Common | 300k | 24% | — | Vested | Employee |
| Seed Investor | Preferred | 200k | 16% | $0.50 | — | Board |
| Series A Lead | Preferred | 150k | 12% | $2.00 | — | Board |
| Advisor | Options | 50k | 4% | $1.00 | 4yr/1yr cliff | Vesting |
| Employees | Options | 70k | 5.6% | $1.00-2.50 | 4yr/1yr cliff | Vesting |
| **Total** | | **1.27M** | **100%** | — | — | |

---

## Key Columns Explained

**Shares:** Current shares outstanding  
**%:** Ownership percentage (Shares / Total × 100)  
**Strike:** Option price (what option holder pays to exercise)  
**Vesting:** Cliff + vesting schedule (e.g., "4yr/1yr" = 1 year cliff, then monthly vest)  
**Status:** Vested / Unvested / Exercised / Cancelled

---

## Liquidation Preference (Post-Sale)

Add column: **Pref Multiple**

```
Seed Series (200k shares):     1× preference
Series A (150k shares):        1× preference
```

**Example:** Deal closes at $10M.

```
Liquidation Waterfall:
1. Seed Investors get 1× their investment first ($[X])
2. Series A Investors get 1× their investment next ($[Y])
3. Remaining goes pro-rata to all shareholders

Result: Founders may get $0 if prefs consume all proceeds.
```

**Action:** Understand your pref structure; know your downside scenario.

---

## Vesting Schedule Details

**Standard Tech Company:**
```
Grant: 100k options
Vesting: 4-year vest with 1-year cliff
Meaning:
  Year 0-1: 0 shares vest (cliff period)
  Year 1: 25k shares vested (1/4th)
  Year 2: 50k vested (cumulative)
  Year 3: 75k vested
  Year 4: 100k vested (fully vested)
```

**For M&A:**
- **Acceleration:** Acquiring buyer may offer acceleration clause (e.g., "50% of unvested vests on close")
- **Double-trigger:** Vesting only if (1) change of control AND (2) you're fired without cause within 12m
- **Ask for:** Full acceleration upon change of control (reduces risk of getting stuck)

---

## Tax Implications (Founder Must Know)

| Scenario | Tax Impact |
|----------|-----------|
| Exercised options (before sale) | Exercise at $X; sell at $Y; pay tax on (Y-X) gain |
| Unexercised options (sale happens) | Options converted to deal consideration; tax on conversion |
| NSO (non-qualified options) | Ordinary income tax on exercise gain |
| ISO (incentive stock options) | Potentially lower capital gains tax (complex; use CPA) |

**Action:** Have CPA model your personal tax scenario for different deal prices.

---

## Pre-LOI Cap Table Checklist

- [ ] All shareholders identified (no surprises)
- [ ] Vesting schedules documented (cliff + monthly)
- [ ] Pref structures clarified (who has what priority)
- [ ] Unvested options calculated (what vests on close)
- [ ] Acceleration clauses identified (what triggers full vest)
- [ ] Tax implications modeled (with CPA)

---

## Deal Payoff Example

**Company sale: $10M enterprise value**

Assume:
- Seed pref: 1× = $2M (initial investment)
- Series A pref: 1× = $5M (initial investment)
- Remaining: $3M split pro-rata

```
| Holder | Shares | % | Pref | Pref Payout | Pro-rata | Total |
|--------|--------|---|------|-------------|----------|-------|
| Founder A | 500k | 40% | None | $0 | $1.2M | $1.2M |
| Founder B | 300k | 24% | None | $0 | $0.72M | $0.72M |
| Seed (pref) | 200k | 16% | 1× | $2M | — | $2M |
| Series A (pref) | 150k | 12% | 1× | $5M | — | $5M |
| **Total** | 1.15M | 100% | | $7M | $3M | $10M |
```

**Founder payoff:** $1.92M combined (far below "founder owns 64%" implies)

**Lesson:** Preference stack matters more than % ownership for small deals.

---

## M&A Data Room Requirement

**Create:** Cap table with annotations

```
cap_table_v3_FINAL_20260612.xlsx
  └─ Sheet 1: Current state
  └─ Sheet 2: Fully diluted (assuming all options exercised)
  └─ Sheet 3: Liquidation waterfall
  └─ Sheet 4: Post-sale payoff (sample $5M, $10M, $15M scenarios)
  └─ Annotations: Flag complex terms, pref details, pending equity events
```

Upload to data room under `/2_Legal/Cap_Table/`.
## Related
## Related
## Related
## Related
