#!/usr/bin/env python3
"""
Script d'analyse financière pré-M&A
Usage: python ma-financial-analysis.py <target_company> <deal_size_millions>
Exemple: python ma-financial-analysis.py TechCorp 250
"""

import pandas as pd
import numpy as np
import sys
import argparse
from datetime import datetime, timedelta
from pathlib import Path

class MAFinancialAnalyzer:
    """Analyse financière pré-acquisition pour évaluation des cibles M&A"""

    def __init__(self, target_company, deal_size):
        self.target_company = target_company
        self.deal_size = float(deal_size)
        self.current_date = datetime.now()

        # Benchmarks sectoriels France 2024
        self.sector_benchmarks = {
            'technology': {
                'revenue_growth': 0.18,
                'ebitda_margin': 0.25,
                'debt_ratio': 0.35,
                'roe': 0.22,
                'current_ratio': 1.8
            },
            'healthcare': {
                'revenue_growth': 0.12,
                'ebitda_margin': 0.30,
                'debt_ratio': 0.40,
                'roe': 0.18,
                'current_ratio': 2.0
            },
            'industrial': {
                'revenue_growth': 0.08,
                'ebitda_margin': 0.20,
                'debt_ratio': 0.45,
                'roe': 0.15,
                'current_ratio': 1.6
            },
            'retail': {
                'revenue_growth': 0.05,
                'ebitda_margin': 0.15,
                'debt_ratio': 0.50,
                'roe': 0.12,
                'current_ratio': 1.4
            }
        }

    def analyze_financial_health(self, financial_data):
        """Analyse la santé financière de l'entreprise cible"""

        # Calcul des ratios financiers
        ratios = {}

        # Liquidité
        ratios['current_ratio'] = financial_data['current_assets'] / financial_data['current_liabilities']
        ratios['quick_ratio'] = (financial_data['current_assets'] - financial_data['inventory']) / financial_data['current_liabilities']

        # Levier financier
        ratios['debt_to_equity'] = financial_data['total_debt'] / financial_data['shareholders_equity']
        ratios['debt_ratio'] = financial_data['total_debt'] / financial_data['total_assets']

        # Rentabilité
        ratios['roe'] = financial_data['net_income'] / financial_data['shareholders_equity']
        ratios['roa'] = financial_data['net_income'] / financial_data['total_assets']
        ratios['gross_margin'] = (financial_data['revenue'] - financial_data['cogs']) / financial_data['revenue']
        ratios['ebitda_margin'] = financial_data['ebitda'] / financial_data['revenue']

        # Efficacité
        ratios['asset_turnover'] = financial_data['revenue'] / financial_data['total_assets']
        ratios['inventory_turnover'] = financial_data['cogs'] / financial_data['inventory']
        ratios['receivables_turnover'] = financial_data['revenue'] / financial_data['accounts_receivable']

        return ratios

    def calculate_valuation_metrics(self, financial_data, growth_rate):
        """Calcul les métriques d'évaluation"""

        metrics = {}

        # Multiples courants
        metrics['ev_revenue'] = self.deal_size / financial_data['revenue']
        metrics['ev_ebitda'] = self.deal_size / financial_data['ebitda']
        metrics['ev_ebitda_sector'] = self.deal_size / self.estimate_ebitda_growth(financial_data, growth_rate)

        # Valeur intrinsèque (DCF simple)
        terminal_value = self.estimate_terminal_value(financial_data, growth_rate)
        discount_rate = 0.10  # Taux d'actualisation typique

        # Valeur actuelle des flux de trésorerie
        fcf_year1 = financial_data['free_cash_flow'] * (1 + growth_rate)
        present_value_fcf = fcf_year1 / (1 + discount_rate)

        metrics['dcf_intrinsic_value'] = present_value_fcf + (terminal_value / ((1 + discount_rate) ** 5))
        metrics['dcf_discount'] = (metrics['dcf_intrinsic_value'] - self.deal_size) / self.deal_size

        # Comparaison avec benchmarks
        benchmarks = self.get_sector_benchmarks('technology')  # À adapter par secteur
        metrics['vs_benchmark_ebitda'] = (metrics['ev_ebitda'] - benchmarks['ebitda_margin']) / benchmarks['ebitda_margin']

        return metrics

    def estimate_ebitda_growth(self, financial_data, growth_rate):
        """Estime la croissance EBITDA sur 5 ans"""
        return financial_data['ebitda'] * ((1 + growth_rate) ** 5)

    def estimate_terminal_value(self, financial_data, growth_rate):
        """Estime la valeur terminale"""
        perpetual_growth_rate = 0.03  # Croissance perpétuelle à 3%
        terminal_value = (financial_data['free_cash_flow'] * (1 + growth_rate)) / (0.10 - perpetual_growth_rate)
        return terminal_value

    def get_sector_benchmarks(self, sector):
        """Récupère les benchmarks sectoriels"""
        return self.sector_benchmarks.get(sector, self.sector_benchmarks['technology'])

    def generate_due_diligence_financial_checklist(self, financial_data):
        """Génère une checklist financière pour la due diligence"""

        checklist = []

        # Documents financiers requis
        checklist.extend([
            ("Audit des 3 derniers exercices", True),
            ("Comptes consolidés vs standalone", True),
            ("Déclarations fiscales des 3 ans", True),
            ("Financial statements IFRS", True),
            ("Contracts clients (>50k€)", True)
        ])

        # Analyse de la dette
        if financial_data['total_debt'] > 0:
            checklist.extend([
                ("Loan covenants analysis", True),
                ("Restructuring agreements", True),
                ("Debt maturity schedule", True),
                ("Cross-default provisions", True)
            ])

        # Risques financiers
        checklist.extend([
            ("FX hedging review", True),
            ("Interest rate sensitivity", True),
            ("Commodity price exposure", True),
            ("Counterparty risk assessment", True)
        ])

        return checklist

    def assess_financial_risks(self, ratios, financial_data):
        """Évalue les risques financiers"""

        risks = []

        # Risques de liquidité
        if ratios['current_ratio'] < 1.5:
            risks.append({
                'category': 'Liquidité',
                'severity': 'Élevé',
                'description': 'Ratio actuel < 1.5',
                'mitigation': 'Exigences de trésorerie minimum'
            })

        # Risques de levier
        if ratios['debt_ratio'] > 0.5:
            risks.append({
                'category': 'Levier',
                'severity': 'Élevé',
                'description': 'Ratio dette > 50%',
                'mitigation': 'Restructuration de la dette ou clause de levier'
            })

        # Risques de rentabilité
        if ratios['ebitda_margin'] < 0.15:
            risks.append({
                'category': 'Rentabilité',
                'severity': 'Moyen',
                'description': 'Marge EBITDA < 15%',
                'mitigation': 'Plan d'optimisation coû'
            })

        return risks

    def generate_report(self):
        """Génère le rapport d'analyse financière complète"""

        # Exemple de données (à remplacer par vraies données)
        financial_data = {
            'revenue': 100000000,  # 100M€
            'ebitda': 25000000,   # 25M€
            'net_income': 15000000,  # 15M€
            'current_assets': 80000000,
            'current_liabilities': 50000000,
            'total_assets': 200000000,
            'total_debt': 80000000,
            'shareholders_equity': 120000000,
            'cogs': 75000000,
            'inventory': 20000000,
            'accounts_receivable': 30000000,
            'free_cash_flow': 20000000
        }

        growth_rate = 0.10  # 10% croissance attendue

        # Analyse financière
        ratios = self.analyze_financial_health(financial_data)

        # Évaluation
        valuation = self.calculate_valuation_metrics(financial_data, growth_rate)

        # Risques
        risks = self.assess_financial_risks(ratios, financial_data)

        # Checklist due diligence
        checklist = self.generate_due_diligence_financial_checklist(financial_data)

        # Création du rapport
        report = f"""
# Analyse Financière Pré-M&A - {self.target_company}
Généré le {self.current_date.strftime('%Y-%m-%d')}
Taille de la transaction: {self.deal_size/1000000:.1f}M€

## 1. Ratios Financiers Clés

| Ratio | Valeur | Benchmark | Écart |
|-------|--------|-----------|-------|
"""

        # Ajout des ratios
        for key, value in ratios.items():
            benchmark = self.get_sector_benchmarks('technology')
            benchmark_value = benchmark.get(key.replace('_', '_'), 0)
            if benchmark_value:
                gap = (value - benchmark_value) / benchmark_value * 100
                report += f"| {key.replace('_', ' ').title()} | {value:.2f} | {benchmark_value:.2f} | {gap:+.1f}% |\n"

        report += "\n## 2. Métriques d'Évaluation\n\n"

        # Ajout des métriques d'évaluation
        for key, value in valuation.items():
            if 'discount' in key:
                report += f"- {key.replace('_', ' ').title()}: {value*100:+.1f}%\n"
            else:
                report += f"- {key.replace('_', ' ').title()}: {value:,.0f}\n"

        report += "\n## 3. Risques Financiers\n\n"

        # Ajout des risques
        for risk in risks:
            report += f"### {risk['category']}\n"
            report += f"- **Sévérité**: {risk['severity']}\n"
            report += f"- **Description**: {risk['description']}\n"
            report += f"- **Mitigation**: {risk['mitigation']}\n\n"

        report += "## 4. Checklist Due Diligence Financière\n\n"

        # Ajout de la checklist
        for item, required in checklist:
            status = "✓" if required else "○"
            report += f"- {status} {item}\n"

        # Recommandations
        report += "\n## 5. Recommandations\n\n"

        # Recommandations basées sur l'analyse
        if valuation.get('dcf_discount', 0) < -0.1:
            report += "⚠️ La cible semble surévaluée par rapport à la valeur DCF\n"

        if ratios['debt_ratio'] > 0.5:
            report += "⚠️ Ratio de dette élevé - négocier des clauses de levier\n"

        if ratios['current_ratio'] < 1.5:
            report += "⚠️ Liquidité insuffisante - exiger amélioration trésorerie\n"

        return report

def main():
    parser = argparse.ArgumentParser(description='Analyse financière pré-M&A')
    parser.add_argument('target_company', help='Nom de l\'entreprise cible')
    parser.add_argument('deal_size', help='Taille de la transaction en millions d\'euros')
    parser.add_argument('--sector', default='technology', help='Secteur d\'activité')
    parser.add_argument('--growth_rate', type=float, default=0.1, help='Taux de croissance attendu')

    args = parser.parse_args()

    # Initialisation de l'analyseur
    analyzer = MAFinancialAnalyzer(args.target_company, args.deal_size)

    # Génération du rapport
    report = analyzer.generate_report()

    # Sauvegarde du rapport
    output_file = f"{args.target_company.lower().replace(' ', '-')}-ma-financial-analysis.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"Rapport d'analyse financière généré: {output_file}")

if __name__ == "__main__":
    main()