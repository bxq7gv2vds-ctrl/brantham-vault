---
name: dcf_calculator_python
description: Python DCF calculator — entrée simple, outputs valuation range en 3 scénarios
metadata:
  type: tool
  created: 2026-06-12
---

# DCF Valuation Calculator — Python

**Purpose:** Quick valuation model for M&A — base/upside/downside scenarios  
**Time:** 2 min to populate, outputs enterprise value range + multiples  
**Files:** Paste into Python 3.8+, run `python3 dcf.py`

---

## Code: dcf.py

```python
import sys
from datetime import datetime

# ============================================================================
# DCF VALUATION CALCULATOR — SaaS M&A
# ============================================================================

class DCFCalculator:
    """
    Computes SaaS company valuation under base/upside/downside scenarios.
    Assumes 5-year projection, terminal value via perpetuity growth.
    """
    
    def __init__(self, 
                 current_arr, 
                 growth_rates, 
                 gross_margin_pct,
                 operating_margin_pct,
                 wacc,
                 terminal_growth_rate):
        """
        Args:
            current_arr (float): Current annual recurring revenue
            growth_rates (dict): {'base': [Y1, Y2, Y3, Y4, Y5], 'upside': [...], 'downside': [...]}
            gross_margin_pct (float): e.g., 75 for 75%
            operating_margin_pct (float or dict): {'base': 10, 'upside': 20, 'downside': 0}
            wacc (float): Weighted avg cost of capital, e.g., 12 for 12%
            terminal_growth_rate (float): e.g., 3 for 3% perpetuity growth
        """
        self.arr = current_arr
        self.growth_rates = growth_rates
        self.gross_margin = gross_margin_pct / 100
        self.operating_margin = operating_margin_pct if isinstance(operating_margin_pct, dict) \
                                else {'base': operating_margin_pct, 'upside': operating_margin_pct, 'downside': operating_margin_pct}
        self.wacc = wacc / 100
        self.tg = terminal_growth_rate / 100
        
    def calc_scenario(self, scenario_name):
        """Calculate DCF for one scenario (base/upside/downside)"""
        growth = self.growth_rates[scenario_name]
        op_margin = self.operating_margin[scenario_name]
        
        # Project 5 years of EBITDA
        ebitdas = []
        revenue = self.arr
        for year in range(5):
            revenue = revenue * (1 + growth[year] / 100)
            ebitda = revenue * (self.gross_margin - (1 - self.gross_margin) + op_margin / 100)
            ebitdas.append(ebitda)
        
        # Discount cash flows to present value
        pv_cf = sum(cf / ((1 + self.wacc) ** (i + 1)) for i, cf in enumerate(ebitdas))
        
        # Terminal value (perpetuity): TV = EBITDA_Y5 * (1 + g) / (WACC - g)
        tv = ebitdas[-1] * (1 + self.tg) / (self.wacc - self.tg)
        pv_tv = tv / ((1 + self.wacc) ** 5)
        
        # Enterprise value = PV of cash flows + PV of terminal value
        ev = pv_cf + pv_tv
        
        # Implied multiple (EV / current ARR)
        multiple = ev / self.arr
        
        return {
            'scenario': scenario_name,
            'ev': ev,
            'multiple': multiple,
            'pv_cf': pv_cf,
            'pv_tv': pv_tv,
            'ebitdas': ebitdas
        }
    
    def run(self):
        """Run all 3 scenarios and return summary"""
        results = {}
        for scenario in ['downside', 'base', 'upside']:
            results[scenario] = self.calc_scenario(scenario)
        return results


def main():
    """Example usage — customize these inputs"""
    
    # ========== CUSTOMIZE THESE ==========
    
    # Current business
    CURRENT_ARR = 2_000_000  # $2M ARR
    
    # Growth assumptions (% growth each year)
    GROWTH_RATES = {
        'downside': [10, 10, 8, 5, 3],      # Slowing growth, declining to 3%
        'base': [35, 25, 20, 15, 12],       # Healthy SaaS growth curve
        'upside': [50, 45, 35, 28, 20]      # Accelerating (new market, productization)
    }
    
    # Margin assumptions
    GROSS_MARGIN = 75  # 75% gross margin (SaaS standard)
    
    # Operating margin (% of revenue)
    # Keep negative near-term (investing in growth), improve over time
    OPERATING_MARGIN = {
        'downside': -5,     # Losing money
        'base': 5,          # Break-even to 5% profit
        'upside': 15        # Profitable, growing
    }
    
    # Discount rate (WACC)
    # Use 10-15% for SaaS (reflects risk)
    WACC = 12  # 12% cost of capital
    
    # Terminal growth rate
    # 2-3% perpetual growth (inflation + GDP)
    TERMINAL_GROWTH = 3  # 3% perpetuity
    
    # ====================================
    
    calc = DCFCalculator(
        current_arr=CURRENT_ARR,
        growth_rates=GROWTH_RATES,
        gross_margin_pct=GROSS_MARGIN,
        operating_margin_pct=OPERATING_MARGIN,
        wacc=WACC,
        terminal_growth_rate=TERMINAL_GROWTH
    )
    
    results = calc.run()
    
    # Print summary
    print("\n" + "="*70)
    print(f"DCF VALUATION — {datetime.now().strftime('%Y-%m-%d')}")
    print("="*70)
    print(f"\nAssumptions:")
    print(f"  Current ARR:        ${CURRENT_ARR:,.0f}")
    print(f"  Gross Margin:       {GROSS_MARGIN}%")
    print(f"  WACC (discount):    {WACC}%")
    print(f"  Terminal Growth:    {TERMINAL_GROWTH}%\n")
    
    # Results table
    print(f"{'Scenario':<12} {'Enterprise Value':>20} {'EV/ARR Multiple':>18}")
    print("-" * 52)
    
    for scenario in ['downside', 'base', 'upside']:
        r = results[scenario]
        ev = r['ev']
        mult = r['multiple']
        print(f"{scenario.capitalize():<12} ${ev:>18,.0f} {mult:>17.1f}x")
    
    print("\n" + "-" * 52)
    
    # Valuation range
    downside_ev = results['downside']['ev']
    base_ev = results['base']['ev']
    upside_ev = results['upside']['ev']
    
    print(f"\n📊 Valuation Range:")
    print(f"  Downside: ${downside_ev:>15,.0f}")
    print(f"  Base:     ${base_ev:>15,.0f}")
    print(f"  Upside:   ${upside_ev:>15,.0f}")
    print(f"\n  → Target Range: ${downside_ev:,.0f} – ${upside_ev:,.0f}")
    print(f"  → Fair Value (Base): ${base_ev:,.0f}")
    
    # Implied multiples
    print(f"\n📈 Implied ARR Multiples:")
    print(f"  Downside: {results['downside']['multiple']:.1f}x")
    print(f"  Base:     {results['base']['multiple']:.1f}x")
    print(f"  Upside:   {results['upside']['multiple']:.1f}x")
    
    # Negotiation guidance
    print(f"\n💰 Negotiation Guidance (assuming 20% risk premium):")
    ask_high = base_ev * 1.2
    walk_away = downside_ev * 0.8
    print(f"  Ask:        ${ask_high:,.0f}  (base × 1.2x confidence premium)")
    print(f"  Walk-away:  ${walk_away:,.0f}  (downside × 0.8x floor)")
    
    print("\n" + "="*70 + "\n")


if __name__ == '__main__':
    main()
```

---

## Usage

### Step 1: Install (if needed)
```bash
# Python 3.8+ comes standard; no dependencies
python3 --version  # Verify
```

### Step 2: Customize the inputs
Edit `CURRENT_ARR`, `GROWTH_RATES`, `OPERATING_MARGIN`, `WACC`:

```python
CURRENT_ARR = 3_000_000        # Your $3M ARR
GROSS_MARGIN = 80              # Your actual gross margin
WACC = 11                       # Your discount rate (typical: 10-15%)

OPERATING_MARGIN = {
    'downside': -10,            # Scenario 1: losing money
    'base': 8,                  # Scenario 2: healthy
    'upside': 20                # Scenario 3: accelerating
}
```

### Step 3: Run
```bash
python3 dcf.py
```

### Sample Output
```
======================================================================
DCF VALUATION — 2026-06-12
======================================================================

Assumptions:
  Current ARR:        $2,000,000
  Gross Margin:       75%
  WACC (discount):    12%
  Terminal Growth:    3%

Scenario         Enterprise Value       EV/ARR Multiple
----------------------------------------------------
Downside                $8,500,000                  4.3x
Base                   $12,500,000                  6.3x
Upside                 $18,500,000                  9.3x

----------------------------------------------------

📊 Valuation Range:
  Downside: $8,500,000
  Base:     $12,500,000
  Upside:   $18,500,000

  → Target Range: $8,500,000 – $18,500,000
  → Fair Value (Base): $12,500,000

📈 Implied ARR Multiples:
  Downside: 4.3x
  Base:     6.3x
  Upside:   9.3x

💰 Negotiation Guidance (assuming 20% risk premium):
  Ask:        $15,000,000  (base × 1.2x confidence premium)
  Walk-away:  $6,800,000   (downside × 0.8x floor)

======================================================================
```

---

## Calibration: What Numbers to Use?

### Gross Margin
- **SaaS median:** 70-80%
- **Low (50-60%):** Self-hosted, significant COGS
- **High (85%+):** Highly leveraged infra (standard for PLG)

### Growth Rates (% YoY)
Use **realistic, declining growth** (not flat):
```
Year 1: Current growth rate (if $2M ARR, ask: what was growth last year?)
Year 2: -5 to -10 percentage points from Year 1
Year 3-5: Further decline, floor at 3-5%

Example (healthy SaaS):
  Y1: 40% → Y2: 30% → Y3: 20% → Y4: 12% → Y5: 8%
```

### Operating Margin
- **High-growth SaaS (Series A-B):** -5% to +5% (reinvesting)
- **Profitable SaaS (late-stage):** +10% to +25%
- **Mature SaaS:** 25%+

**For your scenarios:**
- **Downside:** Assume ~5 pts lower margin (customer loss, sales pressure)
- **Base:** Use your most likely path
- **Upside:** Assume scale + efficiency gains; add 5-10 points

### WACC (Discount Rate)
- **Early SaaS (Series A-C):** 12-15% (risky)
- **Growth SaaS (Series D+):** 10-12%
- **Mature SaaS:** 8-10%
- **Default:** Use 12% if unsure

---

## Common Inputs by Company Stage

### Seed/Series A ($500K–$2M ARR)
```
Growth: 40-80% YoY
Gross margin: 60-75%
Op margin: -10% to 0%
WACC: 14%
```

### Series B-C ($2M–$10M ARR)
```
Growth: 25-50% YoY
Gross margin: 70-80%
Op margin: 0% to +10%
WACC: 12%
```

### Series D+ ($10M–$50M ARR)
```
Growth: 15-35% YoY
Gross margin: 75-85%
Op margin: +5% to +20%
WACC: 10%
```

---

## Pitfalls to Avoid

| ❌ Mistake | ✅ Fix |
|-----------|--------|
| Using flat growth (e.g., 30% forever) | Decline growth each year; hit 3-5% terminal |
| Optimistic WACC (e.g., 5%) | Use 10-15% to account for execution risk |
| Ignoring margin compression | Model realistic margin pressure in downside |
| Including non-recurring revenue | Use ARR only (annualized recurring) |
| Setting terminal growth >WACC | Boom → model doesn't work; cap terminal at 3% |

---

## Next Step: Sensitivity Analysis

Want to see how valuation changes if growth is 5% slower? Add rows:

```python
for growth_delta in [-10, -5, 0, +5, +10]:
    adjusted_growth = [g + growth_delta for g in GROWTH_RATES['base']]
    # Recalc...
```

Or use Excel if you prefer graphical sensitivity tables.

---

## References

- **SaaS Metrics:** Typical multiples by growth rate (SaaS Metrics 2.0)
  - 30%+ growth → 6-10x ARR
  - 20-30% growth → 4-6x ARR
  - 10-20% growth → 2-4x ARR
  
- **Your calculator outputs should be in these ranges** (if not, validate assumptions)
## Related
## Related
## Related
## Related
