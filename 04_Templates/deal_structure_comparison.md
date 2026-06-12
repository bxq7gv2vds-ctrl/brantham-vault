---
name: deal_structure_comparison
type: template
version: 1.0
date: 2026-06-12
---

# Comparateur Deal Structures — Asset Sale vs Equity Sale vs Merger

**Usage:** Décider rapidement quelle structure utiliser selon tax situation, liabilities, et objectifs.

---

## 1. ASSET SALE vs EQUITY SALE: Quick Reference

| Aspect | Asset Sale | Equity Sale | Winner |
|--------|-----------|-----------|--------|
| **What you sell** | Specific assets (IP, customer contracts, code) | Entire company (100% shares) | Equity if clean; Asset if baggage |
| **Buyer assumes liabilities?** | No (buyer carefully selects) | Yes (buyer gets everything) | Asset (seller avoids old debts) |
| **Tax efficiency for seller** | Poor (asset gains taxed as income) | Good (capital gains rates) | Equity |
| **Tax efficiency for buyer** | Good (step-up basis) | Poor (no step-up) | Asset (lower buyer price = higher seller deal%) |
| **Due diligence scope** | Narrower (specific assets only) | Entire company | Asset (faster DD) |
| **Time to close** | Faster (3-4 months) | Slower (4-6 months) | Asset |
| **Regulatory risk** | Lower (not transferring entity) | Higher (change of control) | Asset |
| **Escrow period** | 12 months | 18 months | Asset |
| **Earnout complexity** | Simpler (tied to asset performance) | Complex (tied to company revenue) | Asset |

---

## 2. ASSET SALE (Recommended if: Multiple liabilities, tax optimization possible)

### Structure
```
Buyer acquires:
  ✅ Technology (IP, patents, copyrights)
  ✅ Customer contracts (with consent)
  ✅ Employees (if wants to hire)
  ✅ Physical assets (servers, office equipment)
  ✅ Goodwill / brand (if negotiated)

Seller retains:
  ❌ Old liabilities (taxes, lawsuits, loans)
  ❌ Lease obligations
  ❌ Warranty claims
  ❌ Uncollected AR (optional to transfer)
```

### Tax Treatment (France Example)

**If seller is EIRL/SARL (pass-through entity):**
- Asset gains taxed as **ordinary income** (45% tax on gains)
- NOT capital gains (25%)
- = Worse tax treatment than equity sale
- **Mitigation:** Structure as "company liquidation" (different rules)

**If seller is SAS (corporation):**
- Asset sale = **ordinary gains** (33% corporate tax)
- Equity sale = capital gains (19% tax)
- **Equity sale is 40% more tax-efficient**

### Pros
✅ Avoid unknown liabilities
✅ Faster closing (no escrow period long)
✅ Buyer can't clawback post-close (bought specific assets, not entity)
✅ Good if seller has old tax/employment issues

### Cons
❌ Worse tax treatment for seller (ordinary gains, not capital)
❌ Asset sale agreement = 50+ pages (complex)
❌ Some contracts don't transfer (require consent from counterparty)
❌ May need to wind down original company (tax burden)

### Deal Formula
```
Price = Seller revenue × [2-5x multiple] - Liabilities retained
        (Adjusted by: customer concentration, growth rate)

Example:
  Revenue: $5M
  Multiple: 4x → $20M gross
  Seller liabilities retained: $2M (old loan)
  Seller debt to payoff: $1M
  ____________
  Net to seller: $17M
```

### Typical Timeline: 3-4 months
```
D0:   LOI signed (asset sale structure agreed)
D20:  Asset acquisition agreement drafted (complex, 50+ pages)
D40:  Customer consent obtained for key contracts (can delay 4-6 weeks)
D55:  R&W insurance finalized
D70:  Regulatory/third-party consents done
D85:  Asset transfer + closing adjustments
D90:  Funds transfer + asset handover
```

---

## 3. EQUITY SALE (Recommended if: Clean balance sheet, tax-optimized, simple close)

### Structure
```
Buyer acquires:
  ✅ 100% of company shares
  ✅ All assets (IP, contracts, customers, cash)
  ✅ All liabilities (debt, lawsuits, tax exposure)
  ✅ All goodwill

Seller's role:
  ❌ No longer owns company
  ❌ May stay for transition period (90 days - 1 year)
  ❌ Subject to reps & warranties for 18-24 months (escrow)
```

### Tax Treatment (France Example)

**If seller is SAS (corporation):**
- Sale of shares = **capital gains** (19% tax in France)
- Preferred treatment (not ordinary income)
- **Cleanest tax structure**

**If seller is SARL:**
- Capital gains still apply (still 19%)
- But liable for corporate tax on liquidation (if company gets wound down)

### Pros
✅ Better tax treatment (capital gains vs. ordinary)
✅ Simpler agreement (standard SPA, 40-50 pages)
✅ No consent needed for most contracts (automatic transfer)
✅ Buyer takes all liabilities (not seller's problem)
✅ Can include earn-out (tied to company revenue post-close)

### Cons
❌ Escrow period = long (18-24 months, seller money held)
❌ Reps & warranties breaches = clawback from escrow
❌ Buyer assumes all liabilities (may negotiate lower price to offset)
❌ If company has unknown liabilities, seller exposed (up to escrow amount)

### Deal Formula
```
Price = Seller revenue × [4-7x multiple] - Debt assumed by buyer
        (Adjusted by: unit economics, growth, customer concentration)

Example:
  Revenue: $5M
  Multiple: 5x → $25M gross
  Less: Buyer assumes debt = $3M
  Less: Working capital adjustment = -$500K
  ____________
  Net to seller: $21.5M
```

### Typical Timeline: 4-6 months
```
D0:   LOI signed (equity sale structure agreed)
D15:  SPA (Share Purchase Agreement) drafted (standard template)
D35:  Financial/tech/legal DD running in parallel
D60:  LOI signed (binding purchase agreement)
D70:  R&W insurance finalized
D85:  Closing conditions finalized (regulatory, consents)
D110: SPA signed (binding agreement)
D130: Closing conditions satisfied
D140: Funds transfer + cap table transfer + keys handover
```

---

## 4. MERGER / STOCK-FOR-STOCK (Recommended if: Buyer's stock valuable, seller wants equity upside)

### Structure
```
Buyer's shareholders vote to merge with Seller.
Result:
  - Seller shareholders get Buyer stock (or mixed stock + cash)
  - Seller ceases to exist (merged into Buyer)
  - Buyer absorbs all assets + liabilities

Example:
  Buyer stock worth $30M
  Seller gets $25M of Buyer stock
  Sellers own ~5-10% of combined company
```

### Tax Treatment
**If structured as "tax-free reorganization" (IRC 368):**
- No immediate tax on stock exchange
- Seller defers tax until stock is sold later
- **Most tax-efficient long-term**

**If cash component > 25%:**
- Becomes "partially taxable reorganization"
- Seller owes tax on cash received

### Pros
✅ Tax-free if structured correctly (deferred until stock sale)
✅ Seller maintains upside (owns 5-10% of combined entity)
✅ Buyer's stock = liquid (can sell later)
✅ Valuation more favorable (stock valued at higher multiple)
✅ Simpler closing (stock swap, less escrow)

### Cons
❌ Requires Buyer's board approval (not always possible)
❌ Seller takes risk on Buyer's stock (could drop in value)
❌ Not possible if Buyer is private (hard to value stock)
❌ Seller may not want long-term equity (wants liquidity now)
❌ Buyer's existing shareholders may object (dilution concerns)

### Deal Formula
```
Price = Seller revenue × [4-7x multiple] × Buyer's P/E multiple adjustment
        
Example:
  Seller revenue: $5M
  Multiple: 5x → $25M valuation
  Buyer's stock: $1B valuation, willing to trade 2.5% ownership
  = Buyer stock worth $25M
  Seller gets 2.5% of combined $1.025B = same economic outcome
```

### Typical Timeline: 5-8 months (includes shareholder votes)
```
D0-D30:  LOI negotiation (stock ratio, cash/stock mix)
D30-D60: Merger agreement drafted (complex, shareholder votes required)
D60-D90: Buyer board + shareholder vote
D90-D120: Seller shareholder vote + regulatory filings
D120-D150: Antitrust review (if required)
D150+: Closing (when all votes approved)
```

---

## 5. DECISION MATRIX: Which Structure for YOU?

| Situation | Best Structure | Why |
|-----------|---|---|
| **Clean balance sheet, tax optimized** | Equity Sale | Capital gains tax, simple SPA, standard close |
| **Old liabilities, messy tax history** | Asset Sale | Isolate liabilities, start fresh, avoid escrow risk |
| **Buyer is PE or strategic with stock** | Stock-for-Stock | Tax-free, maintain upside, less cash pressure |
| **Seller wants clean break, no long-term ties** | Equity Sale | Full escrow, then walk away (or Earnout) |
| **Buyer doesn't have cash, only stock** | Stock-for-Stock | Only way to close deal |
| **Multiple sellers (founders + investors)** | Equity Sale | Simpler to divide proceeds pro-rata |
| **Company has IP licensing issues** | Asset Sale | Only transfer specific, unencumbered assets |

---

## 6. TAX IMPACT CALCULATOR (France)

### Scenario A: Equity Sale
```
Company revenue: €5M/year
Sale price: €25M
Basis (original investment): €1M
Capital gain: €24M
Tax rate: 19% (capital gains in France)
Tax owed: €4.56M
NET TO SELLER: €20.44M
```

### Scenario B: Asset Sale
```
Same sale price: €25M
Taxed as ordinary income (not capital gain): 45% rate
Tax owed: €11.25M
NET TO SELLER: €13.75M

⚠️ €6.7M MORE TAX than equity sale!
```

**Recommendation:** If clean balance sheet → Equity Sale (40-50% more net to seller)

---

## 7. SPA TEMPLATE — ULTRA-CONDENSED (3-page version)

```
═══════════════════════════════════════════════════════════════════
SHARE PURCHASE AGREEMENT (SPA)
═══════════════════════════════════════════════════════════════════

PARTIES:
  Seller: [COMPANY NAME], SAS, located at [ADDRESS]
  Buyer: [ACQUIRER NAME], [ENTITY TYPE], located at [ADDRESS]

TRANSACTION:
  Seller sells to Buyer 100% of shares of [TARGET] for [€PRICE]

───────────────────────────────────────────────────────────────────
1. PURCHASE PRICE & PAYMENT

  Purchase Price: €[X] million
  
  Payment:
    Closing Payment (upfront):  €[X] million
    Escrow (held 18 months):    €[Y] million (10-15% of price)
    Earnout (contingent):       €[Z] million (12-24 months)

  Working Capital Adjustment:
    Target WC: €[X] million
    Actual WC at closing: [to be calculated]
    If actual < target: Buyer pays Seller difference
    If actual > target: Seller pays Buyer difference

2. REPRESENTATIONS & WARRANTIES (Seller represents)

  2.1 Organization
    [ ] Company is properly organized, valid SAS
    [ ] Authorized to execute this agreement

  2.2 Capitalization
    [ ] Shares listed below represent 100% ownership:
        - Founder A: [X] shares
        - Founder B: [Y] shares
    [ ] No other shares, options, or convertible instruments

  2.3 Financial Statements
    [ ] 3 years of audited financials provided (P&L, BS, CF)
    [ ] GAAP/local standards compliant
    [ ] No undisclosed liabilities
    [ ] Revenue, EBITDA, growth = as represented

  2.4 Contracts
    [ ] All material contracts (>€100K) listed in Schedule A
    [ ] No change-of-control clauses trigger termination
    [ ] Customer concentration: Top 10 = [X]% of revenue

  2.5 Intellectual Property
    [ ] All IP owned by Company or properly licensed
    [ ] No infringement claims pending
    [ ] All employee/founder IP properly assigned

  2.6 Litigation
    [ ] No pending or threatened lawsuits
    [ ] No regulatory actions
    [ ] Accrued liabilities = €[X] (fully reserved)

  2.7 Compliance
    [ ] GDPR compliant (DPA in place for all processors)
    [ ] Tax filings up to date
    [ ] No employment disputes

3. CLOSING CONDITIONS

  3.1 Seller shall have completed:
    [ ] Executed all ancillary agreements
    [ ] Obtained third-party consents for key contracts
    [ ] No material adverse change in business

  3.2 Buyer shall have completed:
    [ ] Financing commitment obtained
    [ ] Key customer consent letters received
    [ ] Antitrust clearance (if applicable)

4. INDEMNIFICATION & ESCROW

  4.1 Escrow Account
    €[Y] million held in escrow for 18 months
    Released pro-rata as claims are resolved

  4.2 Indemnification Claims
    Seller indemnifies Buyer for breaches of reps/warranties
    Threshold: €[X] (de minimis = no claim < this)
    Basket: First €[Y] of claims not recovered
    Cap: Seller liability = 10-15% of purchase price
    Surviving period: 18 months (except tax, IP = 6 years)

  4.3 R&W Insurance
    Buyer to obtain €[X] million policy (2% of price cost)
    Seller pays: [Negotiated share, typically 50-70%]
    Policy covers: Breaches of reps/warranties
    Insurer = Primary; Escrow = Secondary

5. EARNOUT (if applicable)

  5.1 Earnout Amount: €[Z] million
  5.2 Earnout Conditions:
    [ ] Year 1: Revenue > €6M = 50% payout
    [ ] Year 2: NRR > 110% & Retention > 95% = 50% payout
    [ ] Payment within 30 days of achieving condition

6. EMPLOYEE & FOUNDER MATTERS

  6.1 Employment Agreements
    [ ] Founder to remain as [TITLE] for [12-24] months
    [ ] Salary: €[X]/year, benefits as per offer letter
    [ ] Non-solicitation: [X] years, [X] mile radius

  6.2 Founder Earnout Eligibility
    Founder must remain employed to earn earnout
    Termination without cause = earnout vested pro-rata

7. CONFIDENTIALITY & ANNOUNCEMENTS

  [ ] Announcement to be made jointly by [DATE]
  [ ] Press release: Draft 1 due [DATE], mutual approval
  [ ] Confidentiality: Survives 2 years post-close

8. GOVERNING LAW

  This SPA is governed by and construed in accordance with 
  the laws of France, without regard to conflicts.
  
  Exclusive jurisdiction: Commercial Courts of [PARIS/LYON/etc]

═══════════════════════════════════════════════════════════════════
SCHEDULES (Attached)

  Schedule A: Material Contracts (list of contracts >€100K)
  Schedule B: Cap Table (share ownership breakdown)
  Schedule C: Intellectual Property (patents, trademarks, licenses)
  Schedule D: Exceptions to Reps & Warranties
  Schedule E: Employee List (names, salary, equity)
  Schedule F: Customer List (names, contract value, renewal dates)

═══════════════════════════════════════════════════════════════════
SIGNATURE BLOCK

Seller:
  ____________________  Date: ______
  [Founder Name], CEO

Buyer:
  ____________________  Date: ______
  [Buyer Name], by: [CFO/General Counsel]
```

---

## 8. QUICK CHECKLIST: Choose Your Structure

- [ ] Is balance sheet clean (no old debts/lawsuits)? → **Equity Sale**
- [ ] Do you want long-term stock upside? → **Stock-for-Stock**
- [ ] Are there unknown liabilities / tax issues? → **Asset Sale**
- [ ] Is buyer PE firm (has cash, wants quick close)? → **Equity Sale**
- [ ] Does buyer lack cash (only stock available)? → **Stock-for-Stock**
- [ ] Is this a consolidation (buyer wants rid of you post-close)? → **Asset Sale**

**Once decided:** Use template above (Equity Sale standard), modify for Asset Sale per legal counsel.
## Related
