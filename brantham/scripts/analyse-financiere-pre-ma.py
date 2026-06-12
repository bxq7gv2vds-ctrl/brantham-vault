#!/usr/bin/env python3
"""
Script d'analyse financière pré-M&A
Évaluation rapide des cibles potentielles et identification des opportunités
Auteur: Claude
Date: 2026-06-12
Version: 1.0
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from dataclasses import dataclass
from typing import List, Dict, Optional
import json
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

@dataclass
class FinancialMetrics:
    """Structure pour stocker les indicateurs financiers clés"""
    revenue_growth: float
    ebitda_margin: float
    net_margin: float
    debt_to_ebitda: float
    current_ratio: float
    roe: float
    roa: float
    cash_conversion_cycle: float
    capex_intensity: float
    working_capital_ratio: float

@dataclass
class ValuationMetrics:
    """Structure pour les métriques d'évaluation"""
    ev_ebitda: float
    pe_ratio: float
    pb_ratio: float
    ps_ratio: float
    ev_revenue: float
    dividend_yield: float

@dataclass
class RiskMetrics:
    """Structure pour les indicateurs de risque"""
    financial_health_score: float
    volatility_score: float
    concentration_risk: float
    liquidity_risk: float

class FinancialAnalysis:
    """Classe principale pour l'analyse financière pré-M&A"""

    def __init__(self):
        self.sectors_config = {
            'Tech': {
                'ebitda_margin_min': 15.0,
                'revenue_growth_min': 15.0,
                'debt_to_ebitda_max': 3.0,
                'roe_min': 12.0
            },
            'Healthcare': {
                'ebitda_margin_min': 20.0,
                'revenue_growth_min': 10.0,
                'debt_to_ebitda_max': 4.0,
                'roe_min': 15.0
            },
            'Consumer': {
                'ebitda_margin_min': 12.0,
                'revenue_growth_min': 8.0,
                'debt_to_ebitda_max': 2.5,
                'roe_min': 10.0
            },
            'Industrial': {
                'ebitda_margin_min': 10.0,
                'revenue_growth_min': 6.0,
                'debt_to_ebitda_max': 3.5,
                'roe_min': 8.0
            }
        }

    def calculate_financial_metrics(self, financial_data: Dict) -> FinancialMetrics:
        """Calcule les indicateurs financiers à partir des données brutes"""

        try:
            # Calcul des métriques de croissance
            revenue_growth = self._calculate_growth_rate(
                financial_data.get('revenues', [])
            )

            # Marges
            ebitda_margin = financial_data.get('ebitda', 0) / max(financial_data.get('revenues', [1])[-1], 1) * 100
            net_margin = financial_data.get('net_income', 0) / max(financial_data.get('revenues', [1])[-1], 1) * 100

            # Levier financier
            debt_to_ebitda = financial_data.get('total_debt', 0) / max(financial_data.get('ebitda', 1), 1)

            # Liquidité
            current_ratio = financial_data.get('current_assets', 0) / max(financial_data.get('current_liabilities', 1), 1)

            # Rentabilité
            roe = financial_data.get('net_income', 0) / max(financial_data.get('shareholders_equity', 1), 1) * 100
            roa = financial_data.get('net_income', 0) / max(financial_data.get('total_assets', 1), 1) * 100

            # Cycle de conversion
            ccc = self._calculate_cash_conversion_cycle(financial_data)

            # Intensité capex
            capex_intensity = financial_data.get('capex', 0) / max(financial_data.get('revenues', [1])[-1], 1) * 100

            # BFR
            working_capital_ratio = self._calculate_working_capital_ratio(financial_data)

            return FinancialMetrics(
                revenue_growth=revenue_growth,
                ebitda_margin=ebitda_margin,
                net_margin=net_margin,
                debt_to_ebitda=debt_to_ebitda,
                current_ratio=current_ratio,
                roe=roe,
                roa=roa,
                cash_conversion_cycle=ccc,
                capex_intensity=capex_intensity,
                working_capital_ratio=working_capital_ratio
            )

        except Exception as e:
            print(f"Erreur dans le calcul des métriques financières: {e}")
            return None

    def calculate_valuation_metrics(self, valuation_data: Dict) -> ValuationMetrics:
        """Calcule les métriques d'évaluation"""

        try:
            ev_ebitda = valuation_data.get('ev', 0) / max(valuation_data.get('ebitda', 1), 1)
            pe_ratio = valuation_data.get('share_price', 0) / max(valuation_data.get('eps', 1), 1)
            pb_ratio = valuation_data.get('share_price', 0) / max(valuation_data.get('book_value_per_share', 1), 1)
            ps_ratio = valuation_data.get('share_price', 0) / max(valuation_data.get('revenue_per_share', 1), 1)
            ev_revenue = valuation_data.get('ev', 0) / max(valuation_data.get('revenue', 1), 1)
            dividend_yield = valuation_data.get('dividend_yield', 0)

            return ValuationMetrics(
                ev_ebitda=ev_ebitda,
                pe_ratio=pe_ratio,
                pb_ratio=pb_ratio,
                ps_ratio=ps_ratio,
                ev_revenue=ev_revenue,
                dividend_yield=dividend_yield
            )

        except Exception as e:
            print(f"Erreur dans le calcul des métriques d'évaluation: {e}")
            return None

    def assess_financial_health(self, metrics: FinancialMetrics, sector: str) -> float:
        """Évalue la santé financière sur 100 points"""

        config = self.sectors_config.get(sector, self.sectors_config['Industrial'])
        score = 0

        # Croissance du CA (15%)
        if metrics.revenue_growth >= config['revenue_growth_min']:
            score += 15
        else:
            score += max(0, 15 - (config['revenue_growth_min'] - metrics.revenue_growth) * 0.5)

        # Marge EBITDA (20%)
        if metrics.ebitda_margin >= config['ebitda_margin_min']:
            score += 20
        else:
            score += max(0, 20 - (config['ebitda_margin_min'] - metrics.ebitda_margin) * 0.3)

        # Levier financier (15%)
        if metrics.debt_to_ebitda <= config['debt_to_ebitda_max']:
            score += 15
        else:
            score += max(0, 15 - (metrics.debt_to_ebitda - config['debt_to_ebitda_max']) * 2)

        # Rentabilité (20%)
        if metrics.roe >= config['roe_min']:
            score += 20
        else:
            score += max(0, 20 - (config['roe_min'] - metrics.roe) * 0.5)

        # Liquidité (15%)
        if metrics.current_ratio >= 1.5:
            score += 15
        elif metrics.current_ratio >= 1.0:
            score += 10
        else:
            score += max(0, 10 - (1.5 - metrics.current_ratio) * 5)

        # Cycle de trésorerie (15%)
        if metrics.cash_conversion_cycle <= 60:
            score += 15
        elif metrics.cash_conversion_cycle <= 90:
            score += 10
        else:
            score += max(0, 10 - (metrics.cash_conversion_cycle - 90) * 0.1)

        return min(100, max(0, score))

    def generate_financial_report(self, company_data: Dict, sector: str) -> Dict:
        """Génère un rapport d'analyse financière complet"""

        # Calcul des métriques
        financial_metrics = self.calculate_financial_metrics(company_data.get('financials', {}))
        valuation_metrics = self.calculate_valuation_metrics(company_data.get('valuation', {}))

        if not financial_metrics or not valuation_metrics:
            return {"error": "Données financières insuffisantes"}

        # Évaluation de la santé financière
        health_score = self.assess_financial_health(financial_metrics, sector)

        # Analyse des ratios de valorisation
        valuation_assessment = self.assess_valuation(valuation_metrics, sector)

        # Identification des risques
        risks = self.identify_financial_risks(financial_metrics, valuation_metrics)

        # Recommendations
        recommendations = self.generate_recommendations(financial_metrics, valuation_metrics, health_score, sector)

        return {
            "company_name": company_data.get('name', 'Unknown'),
            "sector": sector,
            "analysis_date": datetime.now().strftime('%Y-%m-%d'),
            "financial_health_score": health_score,
            "financial_metrics": {
                "revenue_growth_pct": financial_metrics.revenue_growth,
                "ebitda_margin_pct": financial_metrics.ebitda_margin,
                "net_margin_pct": financial_metrics.net_margin,
                "debt_to_ebitda_ratio": financial_metrics.debt_to_ebitda,
                "current_ratio": financial_metrics.current_ratio,
                "roe_pct": financial_metrics.roe,
                "roa_pct": financial_metrics.roa,
                "cash_conversion_cycle_days": financial_metrics.cash_conversion_cycle,
                "capex_intensity_pct": financial_metrics.capex_intensity,
                "working_capital_ratio": financial_metrics.working_capital_ratio
            },
            "valuation_metrics": {
                "ev_ebitda_multiple": valuation_metrics.ev_ebitda,
                "pe_ratio": valuation_metrics.pe_ratio,
                "pb_ratio": valuation_metrics.pb_ratio,
                "ps_ratio": valuation_metrics.ps_ratio,
                "ev_revenue_multiple": valuation_metrics.ev_revenue,
                "dividend_yield_pct": valuation_metrics.dividend_yield
            },
            "valuation_assessment": valuation_assessment,
            "identified_risks": risks,
            "recommendations": recommendations,
            "overall_assessment": self.get_overall_assessment(health_score, valuation_assessment, risks)
        }

    def assess_valuation(self, metrics: ValuationMetrics, sector: str) -> Dict:
        """Évalue si la valorisation est attractive"""

        valuation_config = {
            'Tech': {'ev_ebitda_range': (8, 15), 'pe_range': (15, 30)},
            'Healthcare': {'ev_ebitda_range': (10, 20), 'pe_range': (20, 40)},
            'Consumer': {'ev_ebitda_range': (6, 12), 'pe_range': (12, 25)},
            'Industrial': {'ev_ebitda_range': (5, 10), 'pe_range': (10, 20)}
        }

        config = valuation_config.get(sector, valuation_config['Industrial'])
        ev_min, ev_max = config['ev_ebitda_range']
        pe_min, pe_max = config['pe_range']

        assessment = {
            "valuation_multiple_status": "Fair",
            "premium_discount": "Fair",
            "comments": []
        }

        # Analyse EV/EBITDA
        if metrics.ev_ebitda < ev_min:
            assessment["valuation_multiple_status"] = "Discount"
            assessment["premium_discount"] = "Discount"
            assessment["comments"].append(f"EV/EBITDA ({metrics.ev_ebitda:.1fx}) below sector range ({ev_min}-{ev_max}x)")
        elif metrics.ev_ebitda > ev_max:
            assessment["valuation_multiple_status"] = "Premium"
            assessment["premium_discount"] = "Premium"
            assessment["comments"].append(f"EV/EBITDA ({metrics.ev_ebitda:.1f}x) above sector range ({ev_min}-{ev_max}x)")

        # Analyse P/E
        if metrics.pe_ratio < pe_min:
            assessment["comments"].append(f"P/E ratio ({metrics.pe_ratio:.1f}) below sector range ({pe_min}-{pe_max})")
        elif metrics.pe_ratio > pe_max:
            assessment["comments"].append(f"P/E ratio ({metrics.pe_ratio:.1f}) above sector range ({pe_min}-{pe_max})")

        return assessment

    def identify_financial_risks(self, financial: FinancialMetrics, valuation: ValuationMetrics) -> List[str]:
        """Identifie les risques financiers potentiels"""

        risks = []

        # Risques de liquidité
        if financial.current_ratio < 1.0:
            risks.append("Liquidité insuffisante (ratio < 1)")

        # Risques de levier
        if financial.debt_to_ebitda > 5:
            risks.append("Endettement élevé (D/E > 5x)")

        # Risques de rentabilité
        if financial.roe < 5:
            risks.append("Rentabilité faible (ROE < 5%)")

        # Risques de trésorerie
        if financial.cash_conversion_cycle > 120:
            risks.append("Cycle de conversion de trésorerie long (>120j)")

        # Risques de valorisation
        if valuation.ev_ebitda > 20:
            risks.append("Valorisation élevée (EV/EBITDA > 20x)")

        if valuation.pe_ratio > 50:
            risks.append("Valorisation élevée (P/E > 50x)")

        return risks if risks else ["Pas de risques financiers majeurs identifiés"]

    def generate_recommendations(self, financial: FinancialMetrics, valuation: ValuationMetrics,
                               health_score: float, sector: str) -> List[str]:
        """Génère des recommandations d'action"""

        recommendations = []

        if health_score < 70:
            recommendations.append("Renforcer la santé financière avant acquisition")

        if financial.debt_to_ebitda > 3:
            recommendations.append("Négocier des clauses d'endettement cible")

        if financial.revenue_growth < sector_metrics := self.sectors_config.get(sector, {}).get('revenue_growth_min', 10):
            recommendations.append("Vérifier la soutenabilité de la croissance")

        if valuation.ev_ebitda < 5:
            recommendations.append("Opportunité de valorisation attractive - proposer offre compétitive")

        if financial.cash_conversion_cycle > 90:
            recommendations.append("Plan de réduction du cycle de conversion de trésorerie nécessaire")

        return recommendations if recommendations else ["Acquisition recommandée - opportunité attractive"]

    def get_overall_assessment(self, health_score: float, valuation: Dict, risks: List[str]) -> str:
        """Donne une évaluation globale de l'opportunité"""

        risk_count = len([r for r in risks if r != "Pas de risques financiers majeurs identifiés"])

        if health_score >= 80 and risk_count == 0:
            return "OPPORTUNITÉ EXCEPTIONNELLE - À ACQUÉRIR URGENTEMENT"
        elif health_score >= 70 and risk_count <= 1:
            return "OPPORTUNITÉ ATTRACTIVE - ACQUÉRIR"
        elif health_score >= 60 and risk_count <= 2:
            return "OPPORTUNITÉ MODERÉE - ÉVALUER LES CONDITIONS"
        else:
            return "OPPORTUNITÉ LIMITÉE - À RÉÉVALUER"

    def _calculate_growth_rate(self, revenues: List[float]) -> float:
        """Calcule le taux de croissance annuel moyen"""
        if len(revenues) < 2:
            return 0.0

        # CAGR (Compound Annual Growth Rate)
        return (revenues[-1] / revenues[0]) ** (1/(len(revenues)-1)) - 1 if revenues[0] > 0 else 0

    def _calculate_cash_conversion_cycle(self, data: Dict) -> float:
        """Calcule le cycle de conversion de trésorerie"""

        # DIO = (Inventory / COGS) * 365
        dios = 0
        if data.get('cost_of_goods_sold', 0) > 0:
            dios = (data.get('inventory', 0) / data['cost_of_goods_sold']) * 365

        # DSO = (Receivables / Revenue) * 365
        dso = 0
        if data.get('revenues', [0])[-1] > 0:
            dso = (data.get('accounts_receivable', 0) / data['revenues'][-1]) * 365

        # DPO = (Payables / COGS) * 365
        dpo = 0
        if data.get('cost_of_goods_sold', 0) > 0:
            dpo = (data.get('accounts_payable', 0) / data['cost_of_goods_sold']) * 365

        return dios + dso - dpo

    def _calculate_working_capital_ratio(self, data: Dict) -> float:
        """Calcule le ratio de fonds de roulement"""

        current_assets = data.get('current_assets', 0)
        current_liabilities = data.get('current_liabilities', 0)
        total_assets = data.get('total_assets', 1)

        working_capital = current_assets - current_liabilities
        return working_capital / total_assets

def load_sample_data():
    """Charge des données d'exemple pour démonstration"""

    sample_companies = {
        "TechCorp": {
            "name": "TechCorp",
            "sector": "Tech",
            "financials": {
                "revenues": [1000000, 1200000, 1450000, 1800000],
                "ebitda": [200000, 280000, 380000, 500000],
                "net_income": [100000, 150000, 220000, 300000],
                "total_debt": 800000,
                "current_assets": 1500000,
                "current_liabilities": 800000,
                "total_assets": 5000000,
                "shareholders_equity": 2500000,
                "inventory": 300000,
                "accounts_receivable": 600000,
                "accounts_payable": 400000,
                "cost_of_goods_sold": 1200000,
                "capex": 200000,
                "working_capital": 700000
            },
            "valuation": {
                "ev": 12000000,
                "share_price": 50,
                "eps": 2.5,
                "book_value_per_share": 25,
                "revenue_per_share": 15,
                "revenue": 1800000,
                "ebitda": 500000,
                "dividend_yield": 1.5
            }
        },
        "HealthMed": {
            "name": "HealthMed",
            "sector": "Healthcare",
            "financials": {
                "revenues": [800000, 900000, 1000000, 1150000],
                "ebitda": [300000, 350000, 400000, 500000],
                "net_income": [200000, 250000, 300000, 400000],
                "total_debt": 1000000,
                "current_assets": 1800000,
                "current_liabilities": 700000,
                "total_assets": 6000000,
                "shareholders_equity": 3500000,
                "inventory": 500000,
                "accounts_receivable": 400000,
                "accounts_payable": 300000,
                "cost_of_goods_sold": 800000,
                "capex": 150000,
                "working_capital": 1200000
            },
            "valuation": {
                "ev": 15000000,
                "share_price": 60,
                "eps": 4.0,
                "book_value_per_share": 35,
                "revenue_per_share": 11.5,
                "revenue": 1150000,
                "ebitda": 500000,
                "dividend_yield": 2.0
            }
        }
    }

    return sample_companies

def main():
    """Fonction principale - exécute l'analyse"""

    # Initialisation de l'analyseur
    analyzer = FinancialAnalysis()

    # Chargement des données d'exemple
    sample_data = load_sample_data()

    print("=" * 80)
    print("ANALYSE FINANCIÈRE PRÉ-M&A")
    print("=" * 80)

    # Analyse de chaque entreprise
    results = {}
    for company_name, company_data in sample_data.items():
        print(f"\n🔍 Analyse de {company_name} ({company_data['sector']})")
        print("-" * 50)

        result = analyzer.generate_financial_report(company_data, company_data['sector'])
        results[company_name] = result

        # Affichage des résultats clés
        print(f"📊 Score de santé financière: {result['financial_health_score']:.1f}/100")
        print(f"💰 Croissance du CA: {result['financial_metrics']['revenue_growth_pct']:.1f}%")
        print(f"📈 Marge EBITDA: {result['financial_metrics']['ebitda_margin_pct']:.1f}%")
        print(f"🏦 Levier D/EBITDA: {result['financial_metrics']['debt_to_ebitda_ratio']:.1f}x")
        print(f"⚖️ Ratio actuel/passif: {result['financial_metrics']['current_ratio']:.1f}")
        print(f"📊 ROE: {result['financial_metrics']['roe_pct']:.1f}%")
        print(f"🎯 Évaluation globale: {result['overall_assessment']}")

        # Risques identifiés
        print(f"\n⚠️ Risques identifiés:")
        for risk in result['identified_risks']:
            print(f"   • {risk}")

        # Recommandations
        print(f"\n💡 Recommandations:")
        for rec in result['recommendations']:
            print(f"   • {rec}")

    # Sauvegarde des résultats
    with open('/Users/paul/vault/brantham/reports/financial-analysis-results.json', 'w') as f:
        json.dump(results, f, indent=2, default=str)

    print(f"\n📄 Rapport sauvegardé: /Users/paul/vault/brantham/reports/financial-analysis-results.json")

    return results

if __name__ == "__main__":
    main()