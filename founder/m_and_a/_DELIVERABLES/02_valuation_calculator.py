#!/usr/bin/env python3
"""
SaaS Valuation Calculator — Multiples + DCF
Usage: python3 valuation_calculator.py
"""

def calculate_multiples(arr, multiples=None):
    """Calculate valuation by ARR multiple."""
    if multiples is None:
        multiples = [4, 5, 6, 7, 8, 10]

    results = {}
    for m in multiples:
        results[f"{m}x"] = arr * m
    return results

def calculate_dcf(
    arr_year0,
    growth_rates,  # list: [y1_rate, y2_rate, y3_rate]
    terminal_growth=0.03,
    wacc=0.12,
    ebitda_margin_terminal=0.35
):
    """
    DCF valuation: 3-year explicit forecast + terminal value.

    Args:
        arr_year0: Current ARR (€)
        growth_rates: [y1_growth%, y2_growth%, y3_growth%]
        terminal_growth: perpetuity growth rate (default 3%)
        wacc: discount rate (default 12% for SaaS startup)
        ebitda_margin_terminal: EBITDA margin in year 3 (default 35%)

    Returns:
        dict: pv_explicit, terminal_value, total_enterprise_value
    """

    years = {}
    arr = arr_year0
    pv = 0

    # Explicit forecast (3 years)
    for i, growth in enumerate(growth_rates, 1):
        arr = arr * (1 + growth)
        ebitda = arr * ebitda_margin_terminal  # assume improving margins
        pv_factor = 1 / ((1 + wacc) ** i)
        pv_year = ebitda * pv_factor

        years[f"Y{i}"] = {
            "arr": arr,
            "ebitda": ebitda,
            "pv_factor": pv_factor,
            "pv": pv_year,
        }
        pv += pv_year

    # Terminal Value (Gordon Growth)
    terminal_ebitda = years["Y3"]["ebitda"] * (1 + terminal_growth)
    terminal_value = (terminal_ebitda / (wacc - terminal_growth))
    pv_terminal = terminal_value / ((1 + wacc) ** 3)

    enterprise_value = pv + pv_terminal

    return {
        "explicit_forecast": years,
        "pv_explicit": round(pv, 0),
        "terminal_value": round(terminal_value, 0),
        "pv_terminal": round(pv_terminal, 0),
        "enterprise_value": round(enterprise_value, 0),
    }

def sensitivity_analysis(arr, base_growth, base_wacc):
    """
    Create sensitivity table: (growth rate, WACC) → valuation
    """
    growth_range = [base_growth - 0.2, base_growth - 0.1, base_growth, base_growth + 0.1, base_growth + 0.2]
    wacc_range = [base_wacc - 0.03, base_wacc - 0.015, base_wacc, base_wacc + 0.015, base_wacc + 0.03]

    table = {}
    for wacc in wacc_range:
        table[f"WACC {wacc*100:.1f}%"] = {}
        for growth in growth_range:
            dcf_result = calculate_dcf(
                arr,
                [growth, growth, growth],  # same growth 3 years
                wacc=wacc
            )
            table[f"WACC {wacc*100:.1f}%"][f"Growth {growth*100:.0f}%"] = dcf_result["enterprise_value"]

    return table

# ============================================================================
# EXAMPLE: ALLIANCE COIFFURE
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("ALLIANCE COIFFURE — VALUATION ANALYSIS")
    print("="*60)

    # Current metrics
    arr = 500_000  # €500k
    growth_rates = [0.50, 0.40, 0.30]  # Year 1: +50%, Y2: +40%, Y3: +30%
    wacc = 0.12  # 12% discount rate (typical SaaS startup)
    terminal_growth = 0.03  # 3% perpetuity growth

    # 1. MULTIPLE-BASED VALUATION
    print("\n1️⃣  MULTIPLE-BASED VALUATION")
    print("-" * 60)
    multiples = calculate_multiples(arr, multiples=[4, 5, 6, 7, 8])
    for multiple, value in multiples.items():
        print(f"   {multiple} ARR: €{value:,.0f}")

    # 2. DCF VALUATION (3 scenarios)
    print("\n2️⃣  DCF VALUATION (Bear / Base / Bull)")
    print("-" * 60)

    scenarios = {
        "BEAR (Slower growth)": {
            "growth": [0.30, 0.20, 0.15],
            "wacc": 0.14,
        },
        "BASE (Expected)": {
            "growth": [0.50, 0.40, 0.30],
            "wacc": 0.12,
        },
        "BULL (Upside case)": {
            "growth": [0.60, 0.50, 0.40],
            "wacc": 0.10,
        },
    }

    for scenario_name, params in scenarios.items():
        dcf = calculate_dcf(arr, params["growth"], wacc=params["wacc"])
        ev = dcf["enterprise_value"]
        implied_multiple = ev / arr
        print(f"\n   {scenario_name}")
        print(f"   Enterprise Value: €{ev:,.0f}")
        print(f"   Implied Multiple: {implied_multiple:.1f}x ARR")

    # 3. VALUATION RANGE
    print("\n3️⃣  VALUATION RANGE SUMMARY")
    print("-" * 60)
    bear = calculate_dcf(arr, [0.30, 0.20, 0.15], wacc=0.14)["enterprise_value"]
    base = calculate_dcf(arr, [0.50, 0.40, 0.30], wacc=0.12)["enterprise_value"]
    bull = calculate_dcf(arr, [0.60, 0.50, 0.40], wacc=0.10)["enterprise_value"]

    print(f"   Bear Case: €{bear:,.0f}")
    print(f"   Base Case: €{base:,.0f}  ← Most likely")
    print(f"   Bull Case: €{bull:,.0f}")
    print(f"\n   Range: €{bear:,.0f} — €{bull:,.0f}")
    print(f"   Midpoint: €{(bear + bull) / 2:,.0f}")

    # 4. DEAL STRUCTURE (60% cash + 40% earnout)
    print("\n4️⃣  DEAL STRUCTURE (Base Case)")
    print("-" * 60)
    total = base
    cash_40 = total * 0.40
    earnout_40 = total * 0.40
    founder_stay_20 = total * 0.20

    print(f"   Total Enterprise Value: €{total:,.0f}")
    print(f"   ├─ Cash at close (40%): €{cash_40:,.0f}")
    print(f"   ├─ Earnout 2yr (40%):   €{earnout_40:,.0f}")
    print(f"   └─ Founder equity (20%): €{founder_stay_20:,.0f}")

    print("\n" + "="*60 + "\n")
