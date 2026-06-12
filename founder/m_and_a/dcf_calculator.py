#!/usr/bin/env python3
"""
M&A DCF Multi-Scenario Calculator
Calcule enterprise value across pessimistic / base / optimistic scenarios
Usage: python3 dcf_calculator.py
"""

import json
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Scenario:
    name: str
    revenue_growth: List[float]  # 5-year growth rates (%)
    ebitda_margin_y5: float      # EBITDA margin year 5 (%)
    wacc: float                  # Weighted avg cost of capital (%)
    terminal_growth: float       # Terminal growth rate (%)

class DCFCalculator:
    def __init__(self, current_arr: float, current_ebitda_margin: float = 0.20):
        self.current_arr = current_arr
        self.current_ebitda_margin = current_ebitda_margin

    def calculate_scenario(self, scenario: Scenario) -> Dict:
        """Calculate NPV for a single scenario"""

        # Forecast revenue & EBITDA
        revenues = [self.current_arr]
        ebitdas = []

        for i, growth in enumerate(scenario.revenue_growth):
            next_rev = revenues[-1] * (1 + growth)
            revenues.append(next_rev)

            # Gradually improve EBITDA margin
            current_margin = self.current_ebitda_margin + (
                (scenario.ebitda_margin_y5 - self.current_ebitda_margin) * (i + 1) / len(scenario.revenue_growth)
            )
            ebitda = next_rev * current_margin
            ebitdas.append(ebitda)

        # Discount cash flows
        pv_ebitdas = []
        for i, ebitda in enumerate(ebitdas):
            discount_factor = 1 / ((1 + scenario.wacc) ** (i + 1))
            pv = ebitda * discount_factor
            pv_ebitdas.append(pv)

        # Terminal value (Gordon growth model)
        terminal_ebitda = ebitdas[-1] * (1 + scenario.terminal_growth)
        terminal_value = terminal_ebitda / (scenario.wacc - scenario.terminal_growth)
        pv_terminal = terminal_value / ((1 + scenario.wacc) ** len(scenario.revenue_growth))

        # Enterprise value
        enterprise_value = sum(pv_ebitdas) + pv_terminal

        return {
            "scenario": scenario.name,
            "revenues_y5": revenues[-1],
            "ebitda_y5": ebitdas[-1],
            "pv_forecast_ebitdas": sum(pv_ebitdas),
            "pv_terminal_value": pv_terminal,
            "enterprise_value": enterprise_value,
            "multiple_on_arr": enterprise_value / self.current_arr,
        }

    def compare_scenarios(self, scenarios: List[Scenario]) -> Dict:
        """Run all scenarios and compare"""
        results = []
        for scenario in scenarios:
            results.append(self.calculate_scenario(scenario))

        return {
            "current_arr": self.current_arr,
            "scenarios": results,
            "range": {
                "low": results[0]["enterprise_value"],
                "base": results[1]["enterprise_value"],
                "high": results[2]["enterprise_value"],
            }
        }

def main():
    # Example: $5M ARR company
    calculator = DCFCalculator(current_arr=5_000_000, current_ebitda_margin=0.15)

    # Define 3 scenarios
    scenarios = [
        Scenario(
            name="Pessimistic",
            revenue_growth=[0.30, 0.25, 0.20, 0.15, 0.10],
            ebitda_margin_y5=0.25,
            wacc=0.12,
            terminal_growth=0.03
        ),
        Scenario(
            name="Base",
            revenue_growth=[0.50, 0.45, 0.35, 0.25, 0.15],
            ebitda_margin_y5=0.35,
            wacc=0.10,
            terminal_growth=0.03
        ),
        Scenario(
            name="Optimistic",
            revenue_growth=[0.80, 0.70, 0.50, 0.40, 0.30],
            ebitda_margin_y5=0.40,
            wacc=0.08,
            terminal_growth=0.04
        ),
    ]

    results = calculator.compare_scenarios(scenarios)

    # Display results
    print("\n" + "="*70)
    print(f"DCF VALUATION ANALYSIS — {results['current_arr']/1e6:.1f}M ARR Company")
    print("="*70)

    for result in results["scenarios"]:
        print(f"\n{result['scenario'].upper()}")
        print(f"  Year 5 Revenue:        ${result['revenues_y5']/1e6:.1f}M")
        print(f"  Year 5 EBITDA:         ${result['ebitda_y5']/1e6:.1f}M")
        print(f"  Enterprise Value:      ${result['enterprise_value']/1e6:.1f}M")
        print(f"  Multiple on ARR:       {result['multiple_on_arr']:.1f}x")

    print(f"\n{'VALUATION RANGE'}")
    print(f"  Low:                   ${results['range']['low']/1e6:.1f}M")
    print(f"  Base:                  ${results['range']['base']/1e6:.1f}M")
    print(f"  High:                  ${results['range']['high']/1e6:.1f}M")

    print("\n" + "="*70)
    print("INTERPRETATION:")
    print(f"  Your BATNA ask:        ${results['range']['base']/1e6 * 1.3:.1f}M (base × 1.3)")
    print(f"  Walk-away minimum:     ${results['range']['low']/1e6 * 0.8:.1f}M (low × 0.8)")
    print("="*70 + "\n")

    # Save to JSON for easy import
    with open(Path(__file__).parent / "dcf_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("✓ Results saved to dcf_results.json")

if __name__ == "__main__":
    main()
