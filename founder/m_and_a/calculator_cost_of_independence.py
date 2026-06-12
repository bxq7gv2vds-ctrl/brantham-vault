#!/usr/bin/env python3
"""
Cost of Independence Calculator
Quantifie l'opportunity cost de rester indépendant vs vendre.
"""

import json
from dataclasses import dataclass

@dataclass
class IndependenceModel:
    """Modèle financier: rester indépendant"""
    current_arr: float              # ARR actuel
    growth_rate_percent: float      # croissance annuelle esperée
    burn_rate_monthly: float        # burn rate USD/mois
    runway_months: int              # cash runway
    salary_founder: float           # salaire fondateur
    years_horizon: int              # horizon 5/7/10 ans

    def runway_depletion_date(self) -> tuple[int, str]:
        """Combien de mois avant cash = 0?"""
        cash = self.runway_months
        return (cash, f"{cash} mois")

    def arr_at_year(self, year: int) -> float:
        """ARR projetée à Year N"""
        return self.current_arr * ((1 + self.growth_rate_percent/100) ** year)

    def cash_balance_at_month(self, month: int) -> float:
        """Solde cash à month N"""
        return (self.runway_months * -self.burn_rate_monthly) - (self.burn_rate_monthly * month)

    def breakeven_month(self) -> int:
        """Quand cash = 0?"""
        if self.burn_rate_monthly <= 0:
            return 999  # nunca si revenue > expenses
        return int(self.runway_months * -1)  # runway negativo = déjà déjà dead

    def value_at_horizon(self) -> float:
        """
        Exit value dans N ans, en fonction croissance ARR.
        Hypothèse: SaaS multiple de 4-6x ARR.
        """
        future_arr = self.arr_at_year(self.years_horizon)
        saas_multiple = 5  # mid-point
        return future_arr * saas_multiple

    def founder_wealth_retained(self) -> float:
        """
        Founder wealth si reste indépendant:
        = total profit cumulé sur N ans - impôts - living costs
        """
        total_profit = 0
        for year in range(1, self.years_horizon + 1):
            arr = self.arr_at_year(year)
            margin = 0.4  # assume 40% EBITDA margin
            profit = arr * margin - (self.salary_founder * 12)
            total_profit += profit

        # Rough tax: 30%
        after_tax = total_profit * 0.70
        return after_tax

    def breakeven_analysis(self) -> dict:
        """Scenario: quand cash = 0 et que faire?"""
        month_zero = self.breakeven_month()
        return {
            "months_until_cash_depleted": month_zero,
            "arr_at_depletion": self.arr_at_year(month_zero // 12) if month_zero > 0 else None,
            "outcome": "DEAD" if month_zero < 999 else "PROFITABLE"
        }

def compare_exit_vs_independence():
    """Compare: Exit now @ X vs stay & build"""
    print("\n=== COST OF INDEPENDENCE CALCULATOR ===\n")

    model = IndependenceModel(
        current_arr=500_000,        # $500k ARR
        growth_rate_percent=50,     # 50% YoY
        burn_rate_monthly=-8_000,   # burn -$8k/mo (negative = loss)
        runway_months=12,           # 12 months cash
        salary_founder=150_000,     # $150k/year
        years_horizon=5
    )

    # Scenario 1: Stay independent 5 years
    future_arr = model.arr_at_year(5)
    future_value = model.value_at_horizon()
    wealth = model.founder_wealth_retained()
    breakeven = model.breakeven_analysis()

    print(f"🏢 STAY INDEPENDENT (5 years):")
    print(f"  Current ARR:           ${model.current_arr:,.0f}")
    print(f"  Projected ARR @ Year 5: ${future_arr:,.0f}")
    print(f"  Est. Exit Value @ Yr5: ${future_value:,.0f}")
    print(f"  Founder Wealth:        ${wealth:,.0f}")
    print(f"  Runway Status:         {breakeven['outcome']}")
    print()

    # Scenario 2: Sell now @ 5x ARR
    exit_value_now = model.current_arr * 5
    after_tax_cash = exit_value_now * 0.75  # est. taxes
    print(f"💰 EXIT NOW (5x ARR multiple):")
    print(f"  Current Value:         ${exit_value_now:,.0f}")
    print(f"  After Taxes (est.):    ${after_tax_cash:,.0f}")
    print()

    # Comparison
    upside_to_stay = future_value - exit_value_now
    print(f"📊 COMPARISON:")
    print(f"  Exit now value:        ${exit_value_now:,.0f}")
    print(f"  Stay 5yr value:        ${future_value:,.0f}")
    print(f"  Upside if stay:        ${upside_to_stay:,.0f}")
    print(f"  Risk if stay:          Runway = {model.runway_months} months (cash death @ month {breakeven['months_until_cash_depleted']})")

if __name__ == "__main__":
    compare_exit_vs_independence()
