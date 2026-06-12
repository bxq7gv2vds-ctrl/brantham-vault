#!/usr/bin/env python3
"""
EARNOUT TRUE VALUE CALCULATOR
Shows probability-weighted value of an earnout vs upfront cash.
Usage: python3 earnout_true_value_calculator.py
"""

def earnout_calculator():
    """Interactive earnout true value simulator."""

    print("\n" + "="*60)
    print("EARNOUT TRUE VALUE CALCULATOR")
    print("="*60)
    print("\nThis tool calculates the REAL present-value of an earnout,")
    print("accounting for probability of hitting targets, discount rate, and risk.\n")

    # Gather inputs
    print("--- DEAL STRUCTURE ---")
    upfront_cash = float(input("Upfront cash payment ($M): "))
    earnout_pct = float(input("Earnout % of base valuation (%): "))
    earnout_amount = earnout_pct / 100 * (upfront_cash / (1 - earnout_pct / 100))  # Rough calc
    print(f"Estimated earnout amount: ${earnout_amount:.2f}M")
    earnout_amount = float(input("Earnout amount ($M) [override if different]: ") or earnout_amount)

    earnout_duration = int(input("Earnout period (months): "))

    print("\n--- SUCCESS SCENARIOS ---")
    print("What's the probability you hit each milestone?")
    prob_year1 = float(input("Year 1 targets (0-100%): ")) / 100
    prob_year2 = float(input("Year 2 targets (0-100%): ")) / 100 if earnout_duration > 12 else 0.0
    prob_year3 = float(input("Year 3 targets (0-100%): ")) / 100 if earnout_duration > 24 else 0.0

    print("\n--- RISK FACTORS ---")
    buyover_integration_risk = float(input("Integration risk (0-100%, e.g., 30 for 30%): ")) / 100
    founder_retention_risk = float(input("Founder/team departure risk (0-100%): ")) / 100
    buyer_metric_change_risk = float(input("Buyer changes success metrics risk (0-100%): ")) / 100
    discount_rate = float(input("Your discount rate / time-value of money (%, e.g., 10): ")) / 100

    print("\n" + "="*60)
    print("RESULTS")
    print("="*60)

    # Calculate probability-weighted earnout
    # Assume linear earnout (third paid each year or monthly)
    if earnout_duration <= 12:
        prob_success = prob_year1
        avg_months = 6  # avg payout timing
    elif earnout_duration <= 24:
        prob_success = (prob_year1 * prob_year2)  # both years must hit
        avg_months = 12
    else:
        prob_success = (prob_year1 * prob_year2 * prob_year3)
        avg_months = 18

    # Apply risk factors
    prob_success *= (1 - buyover_integration_risk) * (1 - founder_retention_risk) * (1 - buyer_metric_change_risk)

    # Discount to present value
    years_to_payout = avg_months / 12
    discount_factor = 1 / ((1 + discount_rate) ** years_to_payout)

    earnout_pv = earnout_amount * prob_success * discount_factor

    print(f"\nEarnout Success Probability: {prob_success*100:.1f}%")
    print(f"Average Payout Delay: {avg_months} months")
    print(f"Discount Factor (@{discount_rate*100:.0f}% rate): {discount_factor:.3f}")
    print(f"\nEarnout Amount: ${earnout_amount:.2f}M")
    print(f"Expected Value (prob-weighted): ${earnout_amount * prob_success:.2f}M")
    print(f"Present Value (discounted): ${earnout_pv:.2f}M")
    print(f"\n" + "-"*60)

    total_cash = upfront_cash + earnout_pv
    print(f"Upfront Cash:     ${upfront_cash:.2f}M")
    print(f"Earnout (PV):     ${earnout_pv:.2f}M (expected, risk-adjusted)")
    print(f"Total Deal Value: ${total_cash:.2f}M (realistic)")
    print(f"\n" + "-"*60)

    # Compare to alternative (stay independent, IPO, etc.)
    print(f"\nCOMPARISON TO BATNA (staying independent)")
    batna_value = float(input("What's your 3-year BATNA value if you stay independent? ($M): "))
    batna_growth_rate = float(input("Expected annual growth if independent (%): ")) / 100
    batna_future_value = batna_value * ((1 + batna_growth_rate) ** (earnout_duration / 12))

    print(f"\nBATNA (staying independent):")
    print(f"  Today value: ${batna_value:.2f}M")
    print(f"  Growth rate: {batna_growth_rate*100:.0f}% annually")
    print(f"  Value in {earnout_duration} months: ${batna_future_value:.2f}M")

    # Decision
    print(f"\n" + "="*60)
    print("DECISION")
    print("="*60)
    if total_cash > batna_future_value:
        delta = ((total_cash - batna_future_value) / batna_future_value) * 100
        print(f"✅ TAKE THE DEAL")
        print(f"   You get ${total_cash:.2f}M (realistic) vs ${batna_future_value:.2f}M (BATNA)")
        print(f"   Premium: +{delta:.0f}%")
    else:
        delta = ((batna_future_value - total_cash) / total_cash) * 100
        print(f"❌ REJECT THIS DEAL")
        print(f"   You get ${total_cash:.2f}M (realistic) vs ${batna_future_value:.2f}M (BATNA)")
        print(f"   Gap: {delta:.0f}% shortfall")

    # Sensitivity analysis
    print(f"\n" + "="*60)
    print("SENSITIVITY: What if earnout success probability changes?")
    print("="*60)
    for sensitivity_prob in [0.25, 0.50, 0.75, 1.0]:
        adjusted_pv = earnout_amount * sensitivity_prob * discount_factor
        adjusted_total = upfront_cash + adjusted_pv
        print(f"  If {sensitivity_prob*100:.0f}% success → Total deal = ${adjusted_total:.2f}M")

    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    earnout_calculator()
    # Allow re-run
    while input("Run again? (y/n): ").lower() == 'y':
        earnout_calculator()
