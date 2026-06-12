---
name: debt_equity_scenarios
description: Calcul 3 structures capitales (all-cash, seller note, mixed) avec impact seller
version: 1.0
---

# DEBT/EQUITY SCENARIOS — 3 Deal Structures

Comparaison seller downside pour : **All-Cash** vs **Seller Note** vs **Mixed (Cash + Note + Equity)**

## Scenario 1: ALL-CASH (Buyer Financed)

| Item | Formula | Example (Acq=$5M) |
|------|---------|-------------------|
| **Buyer's Debt** | LBO @ 4x EBITDA | $2M (EBITDA=$500k) |
| **Buyer's Equity** | Remainder | $3M |
| **Seller Gets** | Cash day 1 | **$5,000,000** |
| **Seller Risk** | None | ✓ Clean |
| **Seller Upside** | None post-close | Fixed |

**Implication Seller** : Pas de ride-along. Acheteur risque 3x sur 5 ans → pression à réduire prix ("financeability").

---

## Scenario 2: SELLER NOTE (10-20% du deal)

| Item | Formula | Example (Seller Note=$1M) |
|------|---------|--------------------------|
| **Cash at Close** | Deal Price - Note | $4M |
| **Seller Note** | Unsecured or 2nd lien | $1M |
| **Note Terms** | 3-5 yr, 6-8% APR | $20k/month |
| **Interest Income** | $1M × 7% = $70k/yr | +$70k/yr for 3 yrs |
| **Principal+Int.** | Received over 3-5yr | Deferred $350k revenue |
| **Default Risk** | If buyer fails | ⚠️ Subordinated |
| **Tax on Note** | Reported over time | Spread over 3-5 yr |

**Implication Seller** : 
- ✓ Higher effective price (cash + interest)
- ⚠️ Tied to buyer success (collection risk)
- ✓ 2-3 yr earnout proxy (downside protection)

**Example Waterfall:**
- Buyer signs LOI at $5M (asking)
- Buyer's EBITDA = $400k → financeable at 2.5x = $1M debt capacity
- Buyer equity = $1.5M available
- Buyer offers: $2.5M cash + $2.5M seller note
- Seller gets $2.5M day 1 + $41.7k/mo (5yr @ 6.67%) = **$5.0M + $2.5k interest** = $2.5M lower risk than full $5M cash upfront

---

## Scenario 3: MIXED (Cash + Note + Equity Kicker)

| Item | Formula | Example |
|------|---------|---------|
| **Cash at Close** | Buyer's liquid | $3M |
| **Seller Note** | Deferral | $1M (3yr @ 6%) |
| **Equity Kicker** | If EBITDA > $X | 5% of buyer |
| **Earnout** | Revenue milestone | +$500k if $10M revenue |
| **Total Upside** | All components | $3M + $1.18M note + $500k earnout = **$4.68M** |
| **Downside** | If buyer fails | $3M + partial note |

**Implication Seller** :
- Buyer commits < cash → lower all-in buyer equity
- Seller stays partially on the hook (note risk)
- **Seller has upside if buyer grows** ← asymmetric risk-reward
- Note accrues interest → hidden sweetener

---

## DECISION TREE: Which to Choose?

```
Start
  ├─ Buyer is financial buyer (PE, strategic)?
  │   └─ YES → Prefer All-Cash (they have debt capacity)
  │   └─ NO  → Offer Seller Note (lower buyer risk, better structure)
  │
  ├─ Do you trust buyer's ability to hit earnout?
  │   └─ YES → Accept Mixed (note + equity kicker)
  │   └─ NO  → Insist on Cash (don't speculate)
  │
  ├─ Is financing the deal constraint?
  │   └─ YES → Seller Note solves it (Acq can pay $3M cash + $2M note)
  │   └─ NO  → All-Cash (cleaner for you)
  │
  └─ Final: Default to All-Cash unless buyer
     shows strong growth trajectory + you're staying post-close.
```

---

## TAX IMPACT QUICK REFERENCE

| Structure | Seller Tax Status | Note |
|-----------|------------------|------|
| **All-Cash** | Lump-sum capital gain (Section 1202 if eligible) | Pay in year 1 |
| **Seller Note** | Installment sale (Section 453) | Defer taxes over 5yr |
| **Equity Kicker** | Capital gain on stock (if appreciated) | Tax at ordinary rates if income |

**Action:** Run with your CPA — installment sales can defer $500k-$2M in year-1 tax liability.

---

## CALCULATOR (Copy-Paste Values)

```
ALL-CASH SCENARIO
─────────────────────
Deal Price (all-cash):        $______
Buyer's Debt Capacity (4x):   $______ 
Buyer's Equity Needed:        $______
Seller receives at close:     $______
Seller tax on gain:           $______ (consult CPA)

SELLER NOTE SCENARIO
─────────────────────
Deal Price:                   $______
Cash at close:                $______
Seller note amount:           $______
Note APR (%):                 _____%
Note term (years):            ______
Monthly payment:              $______
Total interest over term:     $______
Effective deal value:         $______ (cash + interest)

MIXED SCENARIO
─────────────────────
Cash at close:                $______
Note principal:               $______
Note annual interest:         $______
Equity kicker (% if earned):  _____%
Earnout potential:            $______
Total upside:                 $______ (best case)
Downside (no earnout):        $______ (cash + note)

RECOMMENDATION
─────────────────────
Use if: ___________________________________
Avoid if: _________________________________
```

---

## RED FLAGS BY STRUCTURE

**All-Cash Red Flags:**
- Buyer is overleveraged (debt > 5x EBITDA) → refinancing risk
- No equity skin → buyer cuts costs to hit debt service

**Seller Note Red Flags:**
- Buyer has negative cash flow → can't service note
- Buyer has competing debt → you're subordinated
- Buyer's lease/rent = 50%+ of revenue → fixed costs kill discretionary cash

**Mixed Deal Red Flags:**
- Earnout tied to vague KPI ("achieve synergies")
- Equity kicker dilutable (not locked in percentage)
- Note is unsecured & no second lien on buyer's assets

---

**Sauvegarder cette fiche + calculateur Excel dans `/vault/founder/m-and-a/tools/`**
