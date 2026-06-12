#!/usr/bin/env python3
"""
Earnout Expected Value Calculator
Quantifie la vraie valeur d'un earnout (vs cash) basée sur probabilité.
"""

def calculate_earnout_value(
    earnout_total: float,
    payout_schedule: list[tuple[str, float, float]],  # [(milestone, probability, payout %), ...]
    discount_rate: float = 0.15,  # 15% discount (risk)
    cash_alternative: float = None  # cash you'd get instead
) -> dict:
    """
    Args:
        earnout_total: montant total à gagner (ex: $1M)
        payout_schedule: [("Year 1 ARR > $1M", 0.60, 0.33), ("Year 2 ARR > $2M", 0.40, 0.33), ...]
        discount_rate: how much to discount for risk (default 15%)
        cash_alternative: what you'd get in cash instead (for comparison)

    Returns:
        dict with expected value, NPV, and comparison
    """

    print("\n=== EARNOUT EXPECTED VALUE ANALYZER ===\n")

    total_expected = 0
    total_probability = 0

    print(f"📊 Earnout Structure (Total: ${earnout_total:,.0f})")
    print("─" * 80)

    for i, (milestone, probability, payout_pct) in enumerate(payout_schedule, 1):
        payout = earnout_total * payout_pct
        expected = payout * probability
        discounted = expected / ((1 + discount_rate) ** i)

        total_expected += expected
        total_probability += probability

        print(f"\n[{i}] {milestone}")
        print(f"    Probability: {probability*100:.0f}%")
        print(f"    Payout if hit: ${payout:,.0f}")
        print(f"    Expected value: ${expected:,.0f}")
        print(f"    Discounted @ {discount_rate*100:.0f}%: ${discounted:,.0f}")

    print("\n" + "─" * 80)
    print(f"\n💰 SUMMARY:")
    print(f"    Total Expected Value (undiscounted): ${total_expected:,.0f}")
    print(f"    NPV (risk-adjusted @ {discount_rate*100:.0f}%): ${total_expected / ((1 + discount_rate) ** 1.5):,.0f}")
    print(f"    Implied Success Rate: {total_probability*100:.0f}%")

    # Comparison vs cash
    if cash_alternative:
        npv_earnout = total_expected / ((1 + discount_rate) ** 1.5)
        delta = cash_alternative - npv_earnout

        print(f"\n📈 VS. CASH ALTERNATIVE (${cash_alternative:,.0f}):")
        print(f"    Earnout NPV: ${npv_earnout:,.0f}")
        print(f"    Cash alternative: ${cash_alternative:,.0f}")
        print(f"    Delta: ${delta:,.0f} ({(delta/cash_alternative)*100:.0f}% premium for cash)")

        if npv_earnout < cash_alternative:
            print(f"\n    ⚠️  TAKE THE CASH (worth ${delta:,.0f} more)")
        else:
            print(f"\n    ✅ EARNOUT might be worth it (equiv. to ${npv_earnout:,.0f} cash)")

    return {
        "expected_value": total_expected,
        "npv": total_expected / ((1 + discount_rate) ** 1.5),
        "implied_success_rate": total_probability,
    }


if __name__ == "__main__":
    # EXAMPLE: $1M earnout over 3 years
    earnout_schedule = [
        ("Year 1: ARR > $1M", 0.70, 0.33),     # 70% chance of paying $330k
        ("Year 2: ARR > $1.5M", 0.50, 0.33),   # 50% chance of paying $330k
        ("Year 3: ARR > $2M", 0.35, 0.34),     # 35% chance of paying $340k
    ]

    result = calculate_earnout_value(
        earnout_total=1_000_000,
        payout_schedule=earnout_schedule,
        discount_rate=0.15,
        cash_alternative=600_000  # "They offered $600k cash instead"
    )

    print(f"\n\n🎯 DECISION THRESHOLD:")
    print(f"    If earnout_npv >= cash_alternative → negotiate harder on cash")
    print(f"    If earnout_npv < 0.7 × cash → decline earnout, take cash")
    print(f"\n    Your earnout is: {result['implied_success_rate']*100:.0f}% likely (realistic? achievable?)")
