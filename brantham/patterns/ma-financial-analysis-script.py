#!/usr/bin/env python3
"""
Script d'Analyse Financière Pré-M&A
===================================

Analyse complète des métriques financières pour évaluer une cible M&A.
Framework automatisé avec calcul de multiples sectoriels et scoring de valorisation.
Adapté aux standards français et internationaux.

Auteur: Generated for Brantham Partners
Version: 1.0
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum
import json

class Sector(Enum):
    TECHNOLOGY = "Technology"
    HEALTHCARE = "Healthcare"
    INDUSTRIAL = "Industrial"
    CONSUMER = "Consumer"
    FINANCIAL = "Financial"
    SERVICES = "Services"

@dataclass
class FinancialData:
    """Structure de données financières standardisée"""
    revenue: float
    ebitda: float
    net_income: float
    total_assets: float
    total_debt: float
    shareholders_equity: float
    working_capital: float
    cash_flow: float
    fiscal_year: int
    sector: Sector

@dataclass
class ValuationMetrics:
    """Métriques de valorisation calculées"""
    ev_ebitda: float
    ev_revenue: float
    pe_ratio: float
    pb_ratio: float
    ps_ratio: float
    debt_equity_ratio: float
    current_ratio: float
    roe: float
    roa: float
    operating_margin: float
    net_margin: float

class MAFinancialAnalyzer:
    """Analyseur financier spécialisé pour M&A"""

    # Multiples sectoriels de référence (France 2023-2024)
    SECTOR_MULTIPLES = {
        Sector.TECHNOLOGY: {
            'ev_ebitda': {'min': 12.0, 'max': 25.0, 'avg': 18.5},
            'ev_revenue': {'min': 2.5, 'max': 8.0, 'avg': 4.2},
            'premium': 0.15
        },
        Sector.HEALTHCARE: {
            'ev_ebitda': {'min': 10.0, 'max': 20.0, 'avg': 15.0},
            'ev_revenue': {'min': 3.0, 'max': 6.0, 'avg': 4.5},
            'premium': 0.20
        },
        Sector.INDUSTRIAL: {
            'ev_ebitda': {'min': 8.0, 'max': 12.0, 'avg': 10.0},
            'ev_revenue': {'min': 1.0, 'max': 2.5, 'avg': 1.8},
            'premium': 0.10
        },
        Sector.CONSUMER: {
            'ev_ebitda': {'min': 9.0, 'max': 15.0, 'avg': 12.0},
            'ev_revenue': {'min': 1.5, 'max': 3.5, 'avg': 2.5},
            'premium': 0.12
        },
        Sector.FINANCIAL: {
            'ev_ebitda': {'min': 6.0, 'max': 10.0, 'avg': 8.0},
            'ev_revenue': {'min': 0.8, 'max': 2.0, 'avg': 1.5},
            'premium': 0.08
        },
        Sector.SERVICES: {
            'ev_ebitda': {'min': 8.0, 'max': 14.0, 'avg': 11.0},
            'ev_revenue': {'min': 1.2, 'max': 3.0, 'avg': 2.2},
            'premium': 0.10
        }
    }

    def __init__(self, financial_data: FinancialData):
        """Initialisation avec données financières"""
        self.data = financial_data
        self.metrics = self._calculate_metrics()

    def _calculate_metrics(self) -> ValuationMetrics:
        """Calcul de toutes les métriques financières"""
        return ValuationMetrics(
            ev_ebitda=self._calculate_ev_ebitda(),
            ev_revenue=self._calculate_ev_revenue(),
            pe_ratio=self._calculate_pe_ratio(),
            pb_ratio=self._calculate_pb_ratio(),
            ps_ratio=self._calculate_ps_ratio(),
            debt_equity_ratio=self._calculate_debt_equity_ratio(),
            current_ratio=self._calculate_current_ratio(),
            roe=self._calculate_roe(),
            roa=self._calculate_roa(),
            operating_margin=self._calculate_operating_margin(),
            net_margin=self._calculate_net_margin()
        )

    def _calculate_ev_ebitda(self) -> float:
        """Enterprise Value / EBITDA"""
        ev = self.data.total_assets - self.data.shareholders_equity + self.data.total_debt
        return ev / self.data.ebitda if self.data.ebitda > 0 else 0

    def _calculate_ev_revenue(self) -> float:
        """Enterprise Value / Revenue"""
        ev = self.data.total_assets - self.data.shareholders_equity + self.data.total_debt
        return ev / self.data.revenue if self.data.revenue > 0 else 0

    def _calculate_pe_ratio(self) -> float:
        """Price to Earnings"""
        return self.data.revenue / self.data.net_income if self.data.net_income > 0 else 0

    def _calculate_pb_ratio(self) -> float:
        """Price to Book"""
        return (self.data.total_assets - self.data.shareholders_equity + self.data.total_debt) / self.data.shareholders_equity if self.data.shareholders_equity > 0 else 0

    def _calculate_ps_ratio(self) -> float:
        """Price to Sales"""
        return (self.data.total_assets - self.data.shareholders_equity + self.data.total_debt) / self.data.revenue if self.data.revenue > 0 else 0

    def _calculate_debt_equity_ratio(self) -> float:
        """Total Debt / Shareholders Equity"""
        return self.data.total_debt / self.data.shareholders_equity if self.data.shareholders_equity > 0 else 0

    def _calculate_current_ratio(self) -> float:
        """Current Assets / Current Liabilities"""
        return self.data.working_capital / (self.data.total_assets - self.data.working_capital) if (self.data.total_assets - self.data.working_capital) > 0 else 0

    def _calculate_roe(self) -> float:
        """Return on Equity"""
        return self.data.net_income / self.data.shareholders_equity if self.data.shareholders_equity > 0 else 0

    def _calculate_roa(self) -> float:
        """Return on Assets"""
        return self.data.net_income / self.data.total_assets if self.data.total_assets > 0 else 0

    def _calculate_operating_margin(self) -> float:
        """Operating Margin"""
        return self.data.ebitda / self.data.revenue if self.data.revenue > 0 else 0

    def _calculate_net_margin(self) -> float:
        """Net Margin"""
        return self.data.net_income / self.data.revenue if self.data.revenue > 0 else 0

    def get_sector_benchmark(self) -> Dict[str, Dict]:
        """Retourne les références sectorielles"""
        return self.SECTOR_MULTIPLES.get(self.data.sector, {})

    def calculate_valuation_range(self) -> Tuple[float, float]:
        """Calcule la fourchette de valorisation basée sur les multiples sectoriels"""
        sector_bench = self.get_sector_benchmark()
        ev_ebitda_min = sector_bench['ev_ebitda']['min']
        ev_ebitda_max = sector_bench['ev_ebitda']['max']
        ev_ebitda_avg = sector_bench['ev_ebitda']['avg']

        # Enterprise Value basé sur EBITDA
        ev_min = self.data.ebitda * ev_ebitda_min
        ev_max = self.data.ebitda * ev_ebitda_max
        ev_avg = self.data.ebitda * ev_ebitda_avg

        # Application du premium M&A
        premium = sector_bench['premium']
        ev_min *= (1 + premium)
        ev_max *= (1 + premium)
        ev_avg *= (1 + premium)

        return ev_min, ev_max

    def get_financial_health_score(self) -> float:
        """Score de santé financière (0-100)"""
        scores = []

        # Rentabilité (25%)
        roe_score = min(self.metrics.roe * 100, 25)  # Jusqu'à 25 points
        scores.append(roe_score)

        # Levier financier (20%)
        debt_score = max(0, 20 - self.metrics.debt_equity_ratio * 10)  # Ratio < 2 = 20 points
        scores.append(debt_score)

        # Liquidité (15%)
        current_score = min(self.metrics.current_ratio * 10, 15)  # Ratio > 1.5 = 15 points
        scores.append(current_score)

        # Marge opérationnelle (25%)
        operating_score = min(self.metrics.operating_margin * 100, 25)
        scores.append(operating_score)

        # Croissance (15% - placeholder, nécessite données historiques)
        growth_score = 15  # À remplacer avec données réelles
        scores.append(growth_score)

        return sum(scores)

    def generate_report(self) -> str:
        """Génère un rapport d'analyse complet"""
        sector_bench = self.get_sector_benchmark()
        ev_min, ev_max = self.calculate_valuation_range()
        health_score = self.get_financial_health_score()

        report = f"""
RAPPORT D'ANALYSE FINANCIÈRE PRÉ-M&A
===================================

ENTREPRISE: {self.data.sector.value} - {self.data.fiscal_year}
--------------------------------------------------------

INDICATEURS CLÉS:
-----------------
- Chiffre d'affaires: €{self.data.revenue:,.0f}
- EBITDA: €{self.data.ebitda:,.0f}
- Résultat net: €{self.data.net_income:,.0f}
- Actifs totaux: €{self.data.total_assets:,.0f}
- Dette totale: €{self.data.total_debt:,.0f}
- Capitaux propres: €{self.data.shareholders_equity:,.0f}

MULTIPLES DE VALORISATION:
-------------------------
- EV/EBITDA: {self.metrics.ev_ebitda:.1f}x
- EV/Revenus: {self.metrics.ev_revenue:.1f}x
- P/E: {self.metrics.pe_ratio:.1f}x
- P/B: {self.metrics.pb_ratio:.1f}x
- P/S: {self.metrics.ps_ratio:.1f}x

SANTÉ FINANCIÈRE:
---------------
- Ratio dette/capitaux propres: {self.metrics.debt_equity_ratio:.2f}
- Ratio actuel: {self.metrics.current_ratio:.2f}
- ROE: {self.metrics.roe:.1%}
- ROA: {self.metrics.roa:.1%}
- Marge opérationnelle: {self.metrics.operating_margin:.1%}
- Marge nette: {self.metrics.net_margin:.1%}
- Score de santé financière: {health_score:.0f}/100

RÉFÉRENCES SECTORIELLES:
------------------------
- Multiples EV/EBITDA: {sector_bench['ev_ebitda']['min']:.1f}x - {sector_bench['ev_ebitda']['max']:.1f}x (moy: {sector_bench['ev_ebitda']['avg']:.1f}x)
- Multiples EV/Revenus: {sector_bench['ev_revenue']['min']:.1f}x - {sector_bench['ev_revenue']['max']:.1f}x (moy: {sector_bench['ev_revenue']['avg']:.1f}x)
- Premium M&A attendu: {sector_bench['premium']:.0%}

FOURCHETTE DE VALORISATION:
--------------------------
- Valeur d'entreprise (min): €{ev_min:,.0f}
- Valeur d'entreprise (max): €{ev_max:,.0f}
- Prime M&A appliquée: {sector_bench['premium']:.0%}

RECOMMANDATIONS STRATÉGIQUES:
---------------------------
"""

        # Analyse des risques
        if self.metrics.debt_equity_ratio > 3.0:
            report += "⚠️  Risque de levier financier élevé\n"
        if self.metrics.current_ratio < 1.0:
            report += "⚠️  Problèmes de liquidité à court terme\n"
        if self.metrics.operating_margin < 0.1:
            report += "⚠️  Marge opérationnelle faible (<10%)\n"
        if health_score < 60:
            report += "⚠️  Score de santé financière bas (<60)\n"

        # Opportunities
        if self.metrics.roe > 0.15:
            report += "✓ Bon rentabilité des capitaux propres (>15%)\n"
        if self.metrics.ev_ebitda < sector_bench['ev_ebitda']['avg']:
            report += "✓ Valorisation potentiellement attractive sous le secteur\n"

        report += f"\nCONCLUSION: {self._get_conclusion()}"

        return report

    def _get_conclusion(self) -> str:
        """Génère une conclusion basée sur l'analyse"""
        health_score = self.get_financial_health_score()
        sector_bench = self.get_sector_benchmark()

        if health_score >= 80:
            return "Entreprise très saine - Transaction recommandée"
        elif health_score >= 60:
            return "Entreprise saine avec points d'attention - Transaction viable"
        elif health_score >= 40:
            return "Entreprise avec risques significatifs - Renégociation des termes"
        else:
            return "Entreprise à haut risque - Transaction non recommandée"

def example_usage():
    """Exemple d'utilisation du script"""
    # Création des données financières fictives
    fin_data = FinancialData(
        revenue=50_000_000,      # 50M€ de CA
        ebitda=15_000_000,       # 15M€ d'EBITDA
        net_income=8_000_000,    # 8M€ de résultat net
        total_assets=100_000_000,# 100M€ d'actifs
        total_debt=25_000_000,   # 25M€ de dette
        shareholders_equity=60_000_000, # 60M€ de capitaux propres
        working_capital=20_000_000,    # 20M€ de BFR
        cash_flow=12_000_000,    # 12M€ de cash flow
        fiscal_year=2023,
        sector=Sector.TECHNOLOGY
    )

    # Analyse
    analyzer = MAFinancialAnalyzer(fin_data)
    report = analyzer.generate_report()

    # Export des résultats
    print(report)

    # Sauvegarde en JSON
    result = {
        'sector': fin_data.sector.value,
        'year': fin_data.fiscal_year,
        'metrics': {
            'ev_ebitda': analyzer.metrics.ev_ebitda,
            'ev_revenue': analyzer.metrics.ev_revenue,
            'pe_ratio': analyzer.metrics.pe_ratio,
            'health_score': analyzer.get_financial_health_score(),
            'valuation_range': analyzer.calculate_valuation_range()
        }
    }

    with open('ma_analysis_result.json', 'w') as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    example_usage()