# Cap Table Waterfall Calculator

**Utilité** : voir qui reçoit quoi $ à différentes valuations (essentiel pour négociation).

---

## Tableau Exemple (à adapter)

```
╔════════════════════════════════════════════════════════════════════╗
║         CAP TABLE WATERFALL @ VALUATION = $50M ACQUISITION         ║
╚════════════════════════════════════════════════════════════════════╝

SHAREHOLDER           SHARES    %       AMOUNT($)   NOTES
────────────────────────────────────────────────────────────────
Founder A             1,000k    40%     $20.0M      40% common
Founder B             500k      20%     $10.0M      20% common
Early investors       250k      10%     $5.0M       Series Seed @ $2M
Series A (Sequoia)    400k      16%     $8.0M       Series A @ $15M post
Series B (Redpoint)   350k      14%     $7.0M       Series B @ $50M post
────────────────────────────────────────────────────────────────
TOTAL EQUITY          2,500k    100%    $50.0M
────────────────────────────────────────────────────────────────

ADJUSTMENTS (deductions from purchase price):
────────────────────────────────────────────────────────────────
Outstanding options (1M @ $5 strike)                 $5.0M vested
Accrued salary + bonuses                             $0.5M
Cap table payouts (advisor grants)                   $0.2M
────────────────────────────────────────────────────────────────
SUBTOTAL DEDUCTIONS                                  $5.7M

NET PROCEEDS (before taxes/escrow)                   $44.3M

────────────────────────────────────────────────────────────────

OPTION POOL VESTING (fully vested = paid from proceeds):
Employees holding 200k @ avg $8 strike              $1.6M cost to vested pool

EARNOUT SCENARIO (if $10M contingent on $100k ARR):
If hit → Founder A receives additional               $4.0M
        → Founder B receives additional               $2.0M
        → Series investors split remaining            $4.0M
────────────────────────────────────────────────────────────────
```

---

## Template Excel (Pseudocode)

**Columns:**
```
A. Shareholder Name
B. Shares Outstanding
C. % Ownership (= B / SUM(B))
D. Price Per Share @ Valuation X (= Valuation / SUM(B))
E. Amount at $30M (= B × D₃₀M)
F. Amount at $50M (= B × D₅₀M)
G. Amount at $100M (= B × D₁₀₀M)
H. Notes (round, dates, vesting status)
```

**Key rows:**
1. Common stock (founders) — 40%–60%
2. Preferred stock by round (Series A, B, C)
3. Options (vested + unvested)
4. Warrants (convertible)
5. SAFEs (if uncapped)
6. Subtotal equity
7. Less: option exercises (founders paying strike)
8. Less: accrued liabilities (salary, bonuses)
9. **Net proceeds available for distribution**
10. By class (common → preferred → options → SAFEs)

---

## Calculation Example

```
GIVEN:
- Acquisition price: $50M
- Total shares outstanding: 2.5M
- Option pool outstanding: 200k (avg $5 strike, 80% vested)

STEP 1: Determine liquidation waterfall order

Preferred shares have liquidation preferences (Series A/B typically 1x non-participating):
- Series B: 1x preference = $8M (350k shares @ initial $22.86 price)
- Series A: 1x preference = $5M (400k shares @ initial $12.5 price)
- [Repeat for all preferred tranches]

STEP 2: Distribute in order

1. Series B pref: $8M paid → $50M – $8M = $42M remaining
2. Series A pref: $5M paid → $42M – $5M = $37M remaining
3. Common + remaining prefs: split $37M by ownership
   - Founder A (40%): $37M × 40% = $14.8M
   - Founder B (20%): $37M × 20% = $7.4M
   - Seed (10%): $37M × 10% = $3.7M
   - Remaining prefs: pro-rata

STEP 3: Options exercise

Vested options: 160k @ $5 strike = $0.8M cost
- Founders / employees buy their shares
- Funded from their proceeds (top-up in 409A process)

STEP 4: Accrued payables

- Salary/bonuses: $0.5M (paid before closing)
- Tax/legal fees: ~$0.3M
- Advisor payouts: $0.2M

NET FOUNDER PROCEEDS (Founder A): $14.8M – $0.2M taxes ≈ $11.8M (after-tax)
```

---

## Sensitivity Table (What if valuation changes?)

```
                $30M        $50M        $75M        $100M
────────────────────────────────────────────────────────────
Founder A       $8.0M       $14.8M      $24.5M      $34.0M
Founder B       $4.0M       $7.4M       $12.3M      $17.0M
Series A        $4.8M       $5.0M       $8.5M       $12.0M
Series B        $8.0M       $8.0M       $11.2M      $15.0M
────────────────────────────────────────────────────────────
```

**Insight** : Below $30M, Series prefs "kick in" and compress common holder upside.

---

## How to Build This in Google Sheets / Excel

1. **Input sheet** :
   - Shareholder names, share count, share class
   - Series round info (price, preference, % held)
   - Option pool + strike prices

2. **Calculation sheet** :
   - =Total shares (sum all)
   - =Valuation slider (e.g., $30M–$100M range)
   - =Price per share = Valuation / Total shares
   - =Payout by holder = Shares × Price/share (capped by preferences)
   - =Taxes (rough: federal + state ~ 37%)
   - =Net proceeds (after taxes)

3. **Chart** :
   - X-axis: Valuation ($M)
   - Y-axis: Founder payout ($M)
   - Show impact of preferences (waterfall chart)

---

## Critical Gotchas

1. **Liquidation preferences are NOT equal to ownership %**
   - Non-participating preferred means: get pref + share in remaining
   - Participating preferred: get pref + share pari passu (rare, nasty for common)

2. **Fully diluted shares matter**
   - Many founders ignore options → cap table is off
   - Always use "fully diluted" for valuation math

3. **Earnout doesn't change waterfall, but DOES change founder take-home**
   - Base payout + earnout split per deal docs

4. **Taxes**
   - Asset sale (IP, product) = ordinary income (40%+ tax)
   - Stock sale (cleaner) = capital gains (20% fed + state = ~25%–30% total)
   - Ask accountant; this is rough

5. **Don't share internal waterfall with investors yet**
   - Share "we've modeled impact at various valuations" instead
   - Actual numbers are negotiation leverage
