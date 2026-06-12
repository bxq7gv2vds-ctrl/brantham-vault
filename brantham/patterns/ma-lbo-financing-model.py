#!/usr/bin/env python3
"""
Modèle de Financement M&A LBO (Leveraged Buyout)
=================================================

Modèle financier pour structurer des opérations d'acquisition avec effet de levier.
Calcul automatique de la structure de financement, rentabilité et ratios.

Usage:
    python ma-lbo-financing-model.py --acquisition-price 50000000 --ebitda 10000000 --equity 15000000

Author: Generated for Brantham Partners
Version: 1.0
"""

import numpy as np
import pandas as pd
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional
from enum import Enum
import argparse
import json
from datetime import datetime, timedelta


class LBOStructure(Enum):
    """Types de structures LBO"""
    TRADITIONAL = "Traditional"
    MANAGEMENT = "Management Buyout"
    SECONDARY = "Secondary Buyout"
    RECAPITALIZATION = "Recapitalization"


@dataclass
class LBOParameters:
    """Paramètres de base de l'opération LBO"""
    acquisition_price: float
    ebitda: float
    ebitda_growth: float = 0.08  # 8% croissance par défaut
    exit_multiple: float = 8.0   # Multiple de sortie
    holding_period: int = 5     # Années de détention
    tax_rate: float = 0.25      # 25% taux d'impôt
    depreciation_rate: float = 0.15  # 15% taux d'amortissement
    working_capital_change: float = 0.10  # 10% du CA variation BFR


class LBOFinancingModel:
    """Modèle de financement LBO complet"""

    # Multiples et conditions bancaires (France 2023-2024)
    BANK_TERMS = {
        'senior_debt': {
            'max_multiple': 4.0,  # 4x EBITDA
            'interest_rate': 0.05,  # 5%
            'margin': 0.002,  # 20 points de base
            'maturity': 7,
            'grace_period': 2
        },
        'mezzanine_debt': {
            'max_multiple': 1.5,  # 1.5x EBITDA
            'interest_rate': 0.10,  # 10%
            'equity_kicker': 0.10,  # 10% de participation
            'maturity': 7
        },
        'subordinated_debt': {
            'max_multiple': 1.0,  # 1x EBITDA
            'interest_rate': 0.12,  # 12%
            'maturity': 5
        }
    }

    def __init__(self, params: LBOParameters):
        self.params = params
        self.structure = self._calculate_structure()
        self.projections = self._generate_projections()
        self.return_metrics = self._calculate_returns()

    def _calculate_structure(self) -> Dict:
        """Calcule la structure de financement optimisée"""

        # Dette senior
        senior_max = self.params.ebitda * self.BANK_TERMS['senior_debt']['max_multiple']
        senior_debt = min(self.params.acquisition_price - self.params.equity, senior_max)

        # Dette mezzanine
        remaining_equity = self.params.acquisition_price - self.params.equity - senior_debt
        mezzanine_debt = min(remaining_equity,
                           self.params.ebitda * self.BANK_TERMS['mezzanine_debt']['max_multiple'])

        # Dette subordonnée
        subordinated_debt = self.params.acquisition_price - self.params.equity - senior_debt - mezzanine_debt

        # Vérification de la couverture
        total_debt = senior_debt + mezzanine_debt + subordinated_debt
        debt_ebitda = total_debt / self.params.ebitda

        return {
            'senior_debt': senior_debt,
            'mezzanine_debt': mezzanine_debt,
            'subordinated_debt': subordinated_debt,
            'total_debt': total_debt,
            'equity': self.params.equity,
            'debt_to_equity_ratio': total_debt / self.params.equity,
            'debt_ebitda_ratio': debt_ebitda,
            'leverage_ratio': total_debt / self.params.acquisition_price
        }

    def _generate_projections(self) -> pd.DataFrame:
        """Génère les projections financières sur la période de détention"""

        years = range(self.params.holding_period + 1)  # Inclut année 0
        projections = pd.DataFrame(index=years)

        # Hypothèses de croissance
        ebitda_base = self.params.ebitda
        ebitda_growth = self.params.ebitda_growth

        # Calcul des projections
        for year in years:
            if year == 0:
                # Année d'acquisition
                projections.loc[year, 'EBITDA'] = ebitda_base
                projections.loc[year, 'Revenues'] = ebitda_base / 0.15  # Hypothèse marge 15%
                projections.loc[year, 'Depreciation'] = ebitda_base * self.params.depreciation_rate
                projections.loc[year, 'Working Capital Change'] = 0
            else:
                # Années opérationnelles
                projections.loc[year, 'EBITDA'] = ebitda_base * (1 + ebitda_growth) ** year
                projections.loc[year, 'Revenues'] = projections.loc[year, 'EBITDA'] / 0.15
                projections.loc[year, 'Depreciation'] = projections.loc[year, 'EBITDA'] * self.params.depreciation_rate

                # Variation BFR
                working_capital_prev = projections.loc[year-1, 'Revenues'] * self.params.working_capital_change
                working_capital_current = projections.loc[year, 'Revenues'] * self.params.working_capital_change
                projections.loc[year, 'Working Capital Change'] = working_capital_current - working_capital_prev

        # Calcul des flux de trésorerie
        projections['EBIT'] = projections['EBITDA'] - projections['Depreciation']
        projections['Taxes'] = projections['EBIT'] * self.params.tax_rate
        projections['Net Income'] = projections['EBIT'] - projections['Taxes']
        projections['Free Cash Flow'] = (projections['EBITDA'] - projections['Taxes'] -
                                       projections['Working Capital Change'])

        # Intérêts et remboursements
        projections['Interest Expense'] = self._calculate_interest_payments()
        projections['Debt Repayment'] = self._calculate_debt_repayments()

        # Flux de trésorerie disponible
        projections['FCF Available'] = (projections['Free Cash Flow'] -
                                      projections['Interest Expense'] -
                                      projections['Debt Repayment'])

        return projections

    def _calculate_interest_payments(self) -> pd.Series:
        """Calcule les paiements d'intérêts par période"""
        interest_rates = {
            'senior': self.BANK_TERMS['senior_debt']['interest_rate'],
            'mezzanine': self.BANK_TERMS['mezzanine_debt']['interest_rate'],
            'subordinated': self.BANK_TERMS['subordinated_debt']['interest_rate']
        }

        payments = pd.Series(0.0, index=self.projections.index)

        # Intérêts sur la dette totale (hypothèse simplifiée)
        total_debt = self.structure['total_debt']

        # Grace period pour la dette senior
        grace_years = self.BANK_TERMS['senior_debt']['grace_period']

        for year in self.projections.index:
            if year <= grace_years:
                # Pendant la période de grâce, seulement les intérêts mezzanine et subordonnés
                payments[year] = (total_debt * 0.6 * interest_rates['mezzanine'] +
                                total_debt * 0.4 * interest_rates['subordinated'])
            else:
                # Après la période de grâce, tous les intérêts
                payments[year] = total_debt * (interest_rates['senior'] * 0.6 +
                                             interest_rates['mezzanine'] * 0.3 +
                                             interest_rates['subordinated'] * 0.1)

        return payments

    def _calculate_debt_repayments(self) -> pd.Series:
        """Calcule les remboursements de dette par période"""
        repayments = pd.Series(0.0, index=self.projections.index)

        total_debt = self.structure['total_debt']
        grace_years = self.BANK_TERMS['senior_debt']['grace_period']
        repayment_years = self.params.holding_period - grace_years

        # Remboursement linéaire après la période de grâce
        annual_repayment = total_debt / repayment_years if repayment_years > 0 else 0

        for year in self.projections.index:
            if year > grace_years and year <= self.params.holding_period:
                repayments[year] = annual_repayment

        return repayments

    def _calculate_returns(self) -> Dict:
        """Calcule les indicateurs de rentabilité"""

        # Valeur de sortie
        final_ebitda = self.projections.loc[self.params.holding_period, 'EBITDA']
        exit_value = final_ebitda * self.params.exit_multiple

        # Dette résiduelle
        remaining_debt = max(0, self.structure['total_debt'] -
                           self.projections['Debt Repayment'].sum())

        # Valeur de sortie nette pour les actionnaires
        exit_equity_value = exit_value - remaining_debt

        # Rentabilité
        equity_invested = self.params.equity
        multiple_invested = exit_equity_value / equity_invested

        # Calcul du IRR
        cash_flows = [ -equity_invested ] + list(self.projections['FCF Available'])
        irr = self._calculate_irr(cash_flows)

        # Durée de récupération
        cumulative_cash = 0
        payback_period = 0
        for year in range(1, len(self.projections)):
            cumulative_cash += self.projections.loc[year, 'FCF Available']
            if cumulative_cash >= equity_invested:
                payback_period = year
                break

        return {
            'exit_value': exit_value,
            'exit_equity_value': exit_equity_value,
            'remaining_debt': remaining_debt,
            'equity_multiple': multiple_invested,
            'irr': irr,
            'payback_period': payback_period,
            'total_cash_return': exit_equity_value,
            'profitability_index': (exit_equity_value + self.projections['FCF Available'].sum()) / equity_invested
        }

    def _calculate_irr(self, cash_flows: List[float]) -> float:
        """Calcule le TIR (Internal Rate of Return)"""
        try:
            return np.irr(cash_flows)
        except:
            return 0.0

    def get_financing_summary(self) -> Dict:
        """Résumé complet de la structure de financement"""

        return {
            'acquisition_price': self.params.acquisition_price,
            'ebitda': self.params.ebitda,
            'structure': self.structure,
            'bank_terms_used': self._get_used_bank_terms(),
            'leverage_metrics': self._get_leverage_metrics(),
            'covenant_analysis': self._analyze_covenants(),
            'risk_assessment': self._assess_risks()
        }

    def _get_used_bank_terms(self) -> Dict:
        """Récupère les conditions bancaires utilisées"""

        senior_used = self.structure['senior_debt'] / self.params.ebitda
        mezzanine_used = self.structure['mezzanine_debt'] / self.params.ebitda

        return {
            'senior_debt_usage': f"{senior_used:.1f}x / {self.BANK_TERMS['senior_debt']['max_multiple']:.1f}x",
            'mezzanine_debt_usage': f"{mezzanine_used:.1f}x / {self.BANK_TERMS['mezzanine_debt']['max_multiple']:.1f}x",
            'utilization_rate': (self.structure['total_debt'] /
                               (self.params.ebitda * (self.BANK_TERMS['senior_debt']['max_multiple'] +
                                                   self.BANK_TERMS['mezzanine_debt']['max_multiple']))) * 100
        }

    def _get_leverage_metrics(self) -> Dict:
        """Indicateurs de levier"""

        return {
            'debt_ebitda_ratio': self.structure['debt_ebitda_ratio'],
            'debt_equity_ratio': self.structure['debt_to_equity_ratio'],
            'leverage_ratio': self.structure['leverage_ratio'],
            'interest_coverage_ratio': (self.projections['EBITDA'] /
                                      self.projections['Interest Expense']).mean(),
            'debt_service_coverage_ratio': (self.projections['Free Cash Flow'] /
                                          (self.projections['Interest Expense'] +
                                           self.projections['Debt Repayment'])).mean()
        }

    def _analyze_covenants(self) -> Dict:
        """Analyse des conditions restrictives (covenants)"""

        dscr = self._get_leverage_metrics()['debt_service_coverage_ratio']
        debt_ebitda = self.structure['debt_ebitda_ratio']

        covenant_breaches = []

        # DSCR minimum typically 1.25x
        if dscr < 1.25:
            covenant_breaches.append({
                'type': 'DSCR',
                'required': 1.25,
                'actual': dscr,
                'severity': 'High'
            })

        # Debt/EBITDA maximum typically 4x
        if debt_ebitda > 4.0:
            covenant_breaches.append({
                'type': 'Debt/EBITDA',
                'required': 4.0,
                'actual': debt_ebitda,
                'severity': 'High'
            })

        return {
            'covenant_breaches': covenant_breaches,
            'overall_compliance': len(covenant_breaches) == 0,
            'key_ratios': {
                'DSCR': dscr,
                'Debt/EBITDA': debt_ebitda
            }
        }

    def _assess_risks(self) -> Dict:
        """Évaluation des risques associés à l'opération"""

        risks = []

        # Risque de levier
        if self.structure['debt_ebitda_ratio'] > 5.0:
            risks.append({
                'category': 'Leverage Risk',
                'description': 'Dette/EBITDA élevé (>5x)',
                'impact': 'High',
                'mitigation': 'Réduire dette ou augmenter EBITDA'
            })

        # Risque de refinancement
        if self.params.holding_period > 7:
            risks.append({
                'category': 'Refinancing Risk',
                'description': 'Période de détention longue > 7 ans',
                'impact': 'Medium',
                'mitigation': 'Plan de refinancement anticipé'
            })

        # Risque de sortie
        if self.params.exit_multiple < 7.0:
            risks.append({
                'category': 'Exit Risk',
                'description': 'Multiple de sortie bas (<7x)',
                'impact': 'Medium',
                'mitigation': 'Diversifier stratégie de sortie'
            })

        return {
            'risks_identified': risks,
            'overall_risk_score': len(risks),
            'risk_mitigation_plans': [risk['mitigation'] for risk in risks]
        }

    def generate_report(self) -> str:
        """Génère un rapport d'analyse LBO complet"""

        summary = self.get_financing_summary()
        returns = self.return_metrics

        report = f"""
RAPPORT D'ANALYSE LBO (LEVERAGED BUYOUT)
=====================================

INFORMATIONS DE BASE:
--------------------
- Prix d'acquisition: €{self.params.acquisition_price:,.0f}
- EBITDA: €{self.params.ebitda:,.0f}
- Période de détention: {self.params.holding_period} ans
- Multiple de sortie: {self.params.exit_multiple:.1f}x

STRUCTURE DE FINANCEMENT:
-------------------------
Dette Senior: €{self.structure['senior_debt']:,.0f} ({self.structure['senior_debt']/self.params.acquisition_price*100:.1f}%)
Dette Mezzanine: €{self.structure['mezzanine_debt']:,.0f} ({self.structure['mezzanine_debt']/self.params.acquisition_price*100:.1f}%)
Dette Subordonnée: €{self.structure['subordinated_debt']:,.0f} ({self.structure['subordinated_debt']/self.params.acquisition_price*100:.1f}%)
Capitaux Propres: €{self.structure['equity']:,.0f} ({self.structure['equity']/self.params.acquisition_price*100:.1f}%)
TOTAL: €{self.structure['total_debt'] + self.structure['equity']:,.0f}

INDICATEURS CLÉS:
------------------
- Ratio Dette/EBITDA: {self.structure['debt_ebitda_ratio']:.1f}x
- Ratio Dette/Capitaux Propres: {self.structure['debt_to_equity_ratio']:.1f}x
- Taux de levier: {self.structure['leverage_ratio']*100:.1f}%

RENTABILITÉ:
-------------
- Valeur de sortie: €{returns['exit_value']:,.0f}
- Valeur pour actionnaires: €{returns['exit_equity_value']:,.0f}
- Multiple investissement: {returns['equity_multiple']:.1f}x
- TIR (IRR): {returns['irr']*100:.1f}%
- Durée de récupération: {returns['payback_period']} ans

ANALYSE DES COVENANTS:
----------------------
DSCR moyen: {self._get_leverage_metrics()['debt_service_coverage_ratio']:.2f}x
Défauts de covenant: {len(summary['covenant_analysis']['covenant_breaches'])}
Conformité globale: {'Oui' if summary['covenant_analysis']['overall_compliance'] else 'Non'}

RISQUES IDENTIFIÉS:
------------------
Nombre de risques: {len(summary['risk_assessment']['risks_identified'])}
Risque global: {'Élevé' if len(summary['risk_assessment']['risks_identified']) > 2 else 'Moyen'}

RECOMMANDATIONS:
---------------
"""

        # Ajouter recommandations basées sur l'analyse
        if self.structure['debt_ebitda_ratio'] > 4.0:
            report += "⚠️  Ratio dette/EBITDA élevé - Considérer réduire la dette\n"

        if returns['irr'] < 0.20:
            report += "⚠️  TIR inférieur à 20% - Renégocier termes ou trouver synergies\n"

        if summary['covenant_analysis']['overall_compliance']:
            report += "✓ Tous les covenants sont respectés\n"

        return report


def main():
    """Fonction principale du script"""

    parser = argparse.ArgumentParser(description='Modèle de financement LBO')
    parser.add_argument('--acquisition-price', type=float, required=True,
                       help='Prix d\'acquisition en euros')
    parser.add_argument('--ebitda', type=float, required=True,
                       help='EBITDA annuel en euros')
    parser.add_argument('--equity', type=float, required=True,
                       help='Montant des capitaux propres en euros')
    parser.add_argument('--growth-rate', type=float, default=0.08,
                       help='Taux de croissance de l\'EBITDA (défaut: 8%)')
    parser.add_argument('--exit-multiple', type=float, default=8.0,
                       help='Multiple de sortie (défaut: 8.0)')
    parser.add_argument('--holding-period', type=int, default=5,
                       help='Période de détention en années (défaut: 5)')

    args = parser.parse_args()

    # Création des paramètres
    params = LBOParameters(
        acquisition_price=args.acquisition_price,
        ebitda=args.ebitda,
        equity=args.equity,
        ebitda_growth=args.growth_rate,
        exit_multiple=args.exit_multiple,
        holding_period=args.holding_period
    )

    # Exécution de l'analyse
    lbo_model = LBOFinancingModel(params)

    # Génération du rapport
    report = lbo_model.generate_report()

    # Export des résultats
    output_file = f"lbo_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    results = {
        'parameters': {
            'acquisition_price': args.acquisition_price,
            'ebitda': args.ebitda,
            'equity': args.equity,
            'growth_rate': args.growth_rate,
            'exit_multiple': args.exit_multiple,
            'holding_period': args.holding_period
        },
        'structure': lbo_model.structure,
        'returns': lbo_model.return_metrics,
        'summary': lbo_model.get_financing_summary()
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("RAPPORT D'ANALYSE LBO:")
    print("="*50)
    print(report)
    print(f"\nRésultats détaillés sauvegardés dans: {output_file}")


if __name__ == "__main__":
    main()
