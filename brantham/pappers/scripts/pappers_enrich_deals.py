#!/usr/bin/env python3
"""
pappers_enrich_deals.py — Enrich existing vault deals with Pappers data.

Scans vault/brantham/deals/active/ for deals with a SIREN,
fetches Pappers data, and creates/updates entreprise fiches.

Usage:
  uv run pappers_enrich_deals.py              # All active deals
  uv run pappers_enrich_deals.py --deal mld   # Specific deal
  uv run pappers_enrich_deals.py --dry-run    # Preview only
"""

import argparse
import os
import re
import sys
from pathlib import Path

VAULT = Path(os.environ.get("VAULT_PATH", "/Users/paul/vault"))
DEALS_DIR = VAULT / "brantham" / "deals" / "active"
PAPPERS_DIR = VAULT / "brantham" / "pappers"

# Import from pappers_fetch
sys.path.insert(0, str(PAPPERS_DIR / "scripts"))


def extract_siren(filepath: Path) -> str | None:
    """Extract SIREN from deal frontmatter."""
    content = filepath.read_text()
    match = re.search(r"^siren:\s*[\"']?(\d{9})[\"']?", content, re.MULTILINE)
    return match.group(1) if match else None


def extract_field(filepath: Path, field: str) -> str:
    content = filepath.read_text()
    match = re.search(rf"^{field}:\s*(.+)$", content, re.MULTILINE)
    return match.group(1).strip().strip('"').strip("'") if match else ""


def main():
    parser = argparse.ArgumentParser(description="Enrich deals with Pappers data")
    parser.add_argument("--deal", help="Specific deal slug")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    from pappers_fetch import fetch_entreprise, get_api_key, write_entreprise, write_dirigeant, write_beneficiaire

    api_key = get_api_key()

    # Find deal files
    if args.deal:
        deal_files = list(DEALS_DIR.glob(f"*{args.deal}*"))
    else:
        deal_files = list(DEALS_DIR.glob("*.md"))

    if not deal_files:
        print("No deal files found.")
        return

    enriched = 0
    skipped = 0
    tokens = 0

    for deal_file in deal_files:
        siren = extract_siren(deal_file)
        entreprise = extract_field(deal_file, "entreprise")

        if not siren:
            print(f"SKIP {deal_file.name}: no SIREN")
            skipped += 1
            continue

        # Check if already enriched
        existing = list((PAPPERS_DIR / "entreprises").glob(f"{siren}-*.md"))
        if existing:
            print(f"SKIP {deal_file.name}: already enriched ({existing[0].name})")
            skipped += 1
            continue

        print(f"\nEnriching {deal_file.name} (SIREN: {siren})...")

        if args.dry_run:
            print(f"  [DRY RUN] Would fetch {siren}")
            continue

        try:
            data = fetch_entreprise(siren, api_key)
            denom = data.get("denomination", entreprise)
            tokens += 1

            write_entreprise(data)

            for d in (data.get("representants", []) or [])[:20]:
                write_dirigeant(d, siren, denom)

            for b in (data.get("beneficiaires_effectifs", []) or [])[:20]:
                write_beneficiaire(b, siren, denom)

            enriched += 1

            # Add wikilink back to deal
            deal_content = deal_file.read_text()
            from pappers_fetch import slugify
            e_slug = slugify(denom)
            pappers_link = f"[[brantham/pappers/entreprises/{siren}-{e_slug}]]"
            if pappers_link not in deal_content:
                if "## Notes" in deal_content:
                    deal_content = deal_content.replace(
                        "## Notes",
                        f"## Fiche Pappers\n\n{pappers_link}\n\n## Notes"
                    )
                    deal_file.write_text(deal_content)
                    print(f"  -> Added Pappers link to {deal_file.name}")

        except Exception as e:
            print(f"  ERROR: {e}")

    print(f"\nDone. Enriched: {enriched}, Skipped: {skipped}, Tokens: {tokens}")


if __name__ == "__main__":
    main()
