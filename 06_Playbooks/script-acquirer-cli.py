#!/usr/bin/env python3
"""
CLI Tool: Acquirer Vertical Search & Scoring

Usage:
    python3 script-acquirer-cli.py search --vertical "SaaS" --region "EU" --min-revenue 100M
    python3 script-acquirer-cli.py score --name "TechGiant Corp" --file acquisitions.csv
    python3 script-acquirer-cli.py report --format json > acquirers_ranked.json

Dependencies: pandas, requests (optional for live scraping)
"""

import argparse
import csv
import json
from dataclasses import dataclass
from typing import List
import sys

@dataclass
class Acquirer:
    name: str
    vertical: str
    region: str
    revenue_usd_m: float
    ebitda_pct: float
    track_record: int
    cash_position: str
    fit_score: float = None
    overall_score: float = None
    recommendation: str = None

# Acquirer database (mock — replace with real CRUNCHBASE / LINKEDIN scraper)
ACQUIRERS_DB = [
    Acquirer("Salesforce", "CRM/Platform", "US", 35_000, 18, 12, "High", 8.5),
    Acquirer("HubSpot", "MarTech/CRM", "US", 2_100, 12, 5, "High", 7.8),
    Acquirer("Zapier", "Integration", "US", 850, 25, 8, "Medium", 7.2),
    Acquirer("Amplitude", "Analytics", "US", 180, -5, 2, "Medium", 6.1),
    Acquirer("Notion Labs", "Productivity", "US", 600, 0, 0, "Low", 5.5),
    Acquirer("Stripe", "Fintech/Payments", "US", 7_000, 35, 4, "Very High", 8.9),
    Acquirer("Shopify", "E-commerce", "CA", 6_700, 28, 8, "Very High", 8.7),
    Acquirer("Atlassian", "DevOps/Collab", "AU", 3_200, 22, 11, "High", 8.4),
    Acquirer("Intercom", "Customer Comms", "IE", 250, 8, 3, "Medium", 6.8),
    Acquirer("Twilio", "Comms APIs", "US", 2_800, 8, 9, "Medium", 7.5),
]

class AcquirerCLI:
    def __init__(self):
        self.db = ACQUIRERS_DB

    def search(self, vertical=None, region=None, min_revenue=0, max_revenue=999_999):
        """Search acquirers by vertical, region, revenue"""
        results = [
            acq for acq in self.db
            if (vertical is None or vertical.lower() in acq.vertical.lower())
            and (region is None or region.upper() in acq.region.upper())
            and min_revenue <= acq.revenue_usd_m <= max_revenue
        ]
        return sorted(results, key=lambda x: x.revenue_usd_m, reverse=True)

    def score(self, acquirer: Acquirer, user_scores: dict):
        """
        Calculate overall score based on:
        - user_scores: dict with keys = criteria (strategy, finance, track_record, etc)
        - pre-weighted based on template
        """
        weights = {
            "strategy": 0.25,
            "finance": 0.20,
            "track_record": 0.20,
            "integration": 0.15,
            "legal": 0.15,
            "culture": 0.05,
        }

        total = sum(
            user_scores.get(k, 5) * v for k, v in weights.items()
        )

        return round(total, 1)

    def print_search_results(self, results: List[Acquirer]):
        """Pretty-print search results"""
        if not results:
            print("❌ No acquirers found matching criteria")
            return

        print(f"\n📊 Found {len(results)} acquirers:\n")
        print(f"{'Rank':<5} {'Name':<20} {'Vertical':<20} {'Region':<8} {'Revenue':<12} {'EBITDA':<8}")
        print("-" * 80)

        for i, acq in enumerate(results, 1):
            print(f"{i:<5} {acq.name:<20} {acq.vertical:<20} {acq.region:<8} ${acq.revenue_usd_m:>9,.0f}M {acq.ebitda_pct:>6}%")

    def print_score_matrix(self, acquirer: Acquirer):
        """Display scoring matrix template for user input"""
        print(f"\n📋 Scoring Matrix for {acquirer.name}")
        print("=" * 60)
        print("\nEnter score (0-10) for each criterion:")
        print("  (Press Enter to skip, defaults = 5)\n")

        criteria = ["strategy", "finance", "track_record", "integration", "legal", "culture"]
        scores = {}

        for crit in criteria:
            try:
                val = input(f"  {crit.upper():.<30} ")
                scores[crit] = float(val) if val else 5.0
            except ValueError:
                scores[crit] = 5.0
                print(f"    → defaulting to 5")

        overall = self.score(acquirer, scores)
        recommendation = self._get_recommendation(overall)

        print(f"\n✅ OVERALL SCORE: {overall}/100")
        print(f"📌 RECOMMENDATION: {recommendation}")

        return scores, overall

    def _get_recommendation(self, score: float) -> str:
        if score >= 90:
            return "🟢 Green Light — pursue aggressively"
        elif score >= 75:
            return "🟡 Good Option — explore further"
        elif score >= 60:
            return "🟠 Explore, but vet deeper"
        elif score >= 45:
            return "🔴 Secondary Option — only if needed"
        else:
            return "⛔ Yellow Flag — proceed with caution"

def main():
    parser = argparse.ArgumentParser(
        description="Acquirer vertical search & scoring CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Search SaaS acquirers in Europe with >$100M revenue
  %(prog)s search --vertical "SaaS" --region "EU" --min-revenue 100

  # Interactive scoring for a specific acquirer
  %(prog)s score --name "Salesforce"

  # Export all acquirers as JSON
  %(prog)s export --format json > acquirers.json
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Search command
    search_parser = subparsers.add_parser("search", help="Search acquirers by criteria")
    search_parser.add_argument("--vertical", type=str, help="Product vertical (e.g., 'SaaS', 'FinTech')")
    search_parser.add_argument("--region", type=str, help="Geographic region (US, EU, APAC, etc)")
    search_parser.add_argument("--min-revenue", type=float, default=0, help="Min annual revenue ($M)")
    search_parser.add_argument("--max-revenue", type=float, default=999_999, help="Max annual revenue ($M)")

    # Score command
    score_parser = subparsers.add_parser("score", help="Score an acquirer interactively")
    score_parser.add_argument("--name", type=str, required=True, help="Acquirer name")

    # Export command
    export_parser = subparsers.add_parser("export", help="Export acquirer database")
    export_parser.add_argument("--format", choices=["json", "csv"], default="json", help="Output format")

    args = parser.parse_args()
    cli = AcquirerCLI()

    if args.command == "search":
        results = cli.search(
            vertical=args.vertical,
            region=args.region,
            min_revenue=args.min_revenue,
            max_revenue=args.max_revenue
        )
        cli.print_search_results(results)

    elif args.command == "score":
        # Find acquirer by name
        match = [a for a in cli.db if args.name.lower() in a.name.lower()]
        if not match:
            print(f"❌ Acquirer '{args.name}' not found")
            sys.exit(1)

        acquirer = match[0]
        scores, overall = cli.print_score_matrix(acquirer)

    elif args.command == "export":
        if args.format == "json":
            data = [
                {
                    "name": a.name,
                    "vertical": a.vertical,
                    "region": a.region,
                    "revenue_m": a.revenue_usd_m,
                    "ebitda_pct": a.ebitda_pct,
                }
                for a in cli.db
            ]
            print(json.dumps(data, indent=2))
        else:  # csv
            writer = csv.DictWriter(sys.stdout, fieldnames=["Name", "Vertical", "Region", "Revenue_M", "EBITDA_%"])
            writer.writeheader()
            for a in cli.db:
                writer.writerow({
                    "Name": a.name,
                    "Vertical": a.vertical,
                    "Region": a.region,
                    "Revenue_M": f"{a.revenue_usd_m:.0f}",
                    "EBITDA_%": a.ebitda_pct
                })

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
