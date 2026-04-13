#!/usr/bin/env python3
"""
Fix short wikilinks in vault knowledge files.
Replaces [[filename]] with [[full/path/to/filename]] and adds missing bidirectional links.
"""
import re
from pathlib import Path

VAULT = Path("/Users/paul/vault")

# Mapping of short filename -> full path (without .md)
SHORT_TO_FULL = {
    "_knowledge-map": "brantham/knowledge/_knowledge-map",
    "banques-cellules-restructuring": "brantham/knowledge/acteurs/banques-cellules-restructuring",
    "ecosysteme-restructuring": "brantham/knowledge/acteurs/ecosysteme-restructuring",
    "assurance-credit": "brantham/knowledge/finance/assurance-credit",
    "assurances-ma-distressed": "brantham/knowledge/finance/assurances-ma-distressed",
    "comptabilite-crise": "brantham/knowledge/finance/comptabilite-crise",
    "financial-modeling-distressed": "brantham/knowledge/finance/financial-modeling-distressed",
    "fiscalite-restructuration": "brantham/knowledge/finance/fiscalite-restructuration",
    "pi-actifs-incorporels-distressed": "brantham/knowledge/finance/pi-actifs-incorporels-distressed",
    "restructuration-dette": "brantham/knowledge/finance/restructuration-dette",
    "valorisation-distressed": "brantham/knowledge/finance/valorisation-distressed",
    "concurrence-distressed": "brantham/knowledge/legal/concurrence-distressed",
    "contrats-baux-en-procedure": "brantham/knowledge/legal/contrats-baux-en-procedure",
    "droit-europeen-insolvabilite": "brantham/knowledge/legal/droit-europeen-insolvabilite",
    "droit-social-restructuration": "brantham/knowledge/legal/droit-social-restructuration",
    "nullites-periode-suspecte": "brantham/knowledge/legal/nullites-periode-suspecte",
    "passif-environnemental": "brantham/knowledge/legal/passif-environnemental",
    "plans-de-cession": "brantham/knowledge/legal/plans-de-cession",
    "plans-de-continuation": "brantham/knowledge/legal/plans-de-continuation",
    "rang-des-creances": "brantham/knowledge/legal/rang-des-creances",
    "responsabilite-tiers": "brantham/knowledge/legal/responsabilite-tiers",
    "sanctions-dirigeants": "brantham/knowledge/legal/sanctions-dirigeants",
    "suretes-en-procedure-collective": "brantham/knowledge/legal/suretes-en-procedure-collective",
    "cas-casino-groupe": "brantham/knowledge/market/cas-casino-groupe",
    "cas-emblematiques-france": "brantham/knowledge/market/cas-emblematiques-france",
    "cas-orpea-emeis": "brantham/knowledge/market/cas-orpea-emeis",
    "stats-defaillances-2025": "brantham/knowledge/market/stats-defaillances-2025",
    "liquidation-judiciaire": "brantham/knowledge/procedures/liquidation-judiciaire",
    "lj-simplifiee": "brantham/knowledge/procedures/lj-simplifiee",
    "mandat-ad-hoc-conciliation": "brantham/knowledge/procedures/mandat-ad-hoc-conciliation",
    "redressement-judiciaire": "brantham/knowledge/procedures/redressement-judiciaire",
    "sauvegarde-acceleree-sfa": "brantham/knowledge/procedures/sauvegarde-acceleree-sfa",
    "sauvegarde": "brantham/knowledge/procedures/sauvegarde",
    "due-diligence-distressed": "brantham/knowledge/process/due-diligence-distressed",
    "encheres-surencheres": "brantham/knowledge/process/encheres-surencheres",
    "structuration-offres-reprise": "brantham/knowledge/process/structuration-offres-reprise",
    "audience-tribunal": "brantham/knowledge/process/audience-tribunal",
    "post-closing-execution": "brantham/knowledge/process/post-closing-execution",
    "integration-post-acquisition": "brantham/knowledge/process/integration-post-acquisition",
    "turnaround-operationnel": "brantham/knowledge/process/turnaround-operationnel",
    "agriculture-agroalimentaire": "brantham/knowledge/sectors/agriculture-agroalimentaire",
    "btp-construction": "brantham/knowledge/sectors/btp-construction",
    "immobilier": "brantham/knowledge/sectors/immobilier",
    "industrie-manufacturiere": "brantham/knowledge/sectors/industrie-manufacturiere",
    "restauration-hotellerie": "brantham/knowledge/sectors/restauration-hotellerie",
    "retail-commerce": "brantham/knowledge/sectors/retail-commerce",
    "tech-startups": "brantham/knowledge/sectors/tech-startups",
    "communication-parties-prenantes": "brantham/knowledge/skills/communication-parties-prenantes",
    "ethique-repreneur": "brantham/knowledge/skills/ethique-repreneur",
    "negociation-crise": "brantham/knowledge/skills/negociation-crise",
    "quick-scan-diagnostic": "brantham/knowledge/skills/quick-scan-diagnostic",
    "programme-formation": "brantham/knowledge/training/programme-formation",
    "glossaire-distressed": "brantham/knowledge/glossary/glossaire-distressed",
}


def fix_short_wikilinks(content):
    """Replace [[short-name]] and [[short-name|alias]] with full paths."""
    changes = 0

    def replacer(match):
        nonlocal changes
        inner = match.group(1)

        # Handle aliases: [[target|alias]]
        if "|" in inner:
            target, alias = inner.split("|", 1)
        else:
            target = inner
            alias = None

        target = target.strip()

        # Skip if already a full path (contains /)
        if "/" in target:
            return match.group(0)

        # Look up in mapping
        if target in SHORT_TO_FULL:
            full_path = SHORT_TO_FULL[target]
            changes += 1
            if alias:
                return f"[[{full_path}|{alias}]]"
            else:
                return f"[[{full_path}]]"

        return match.group(0)

    new_content = re.sub(r'\[\[([^\]]+)\]\]', replacer, content)
    return new_content, changes


def fix_bidirectional_links():
    """Find files that link to others but aren't linked back. Add missing backlinks."""
    # Build graph of all links
    links = {}  # file_path -> set of linked paths
    all_files = {}

    for md_file in VAULT.rglob("*.md"):
        rel = str(md_file.relative_to(VAULT))
        if any(skip in rel for skip in [".obsidian", ".trash", "templates", "scripts"]):
            continue
        content = md_file.read_text(encoding="utf-8", errors="ignore")
        all_files[rel] = md_file

        # Extract all wikilink targets
        targets = set()
        for match in re.finditer(r'\[\[([^\]|]+)', content):
            target = match.group(1).strip()
            if not target.endswith(".md"):
                target += ".md"
            targets.add(target)
        links[rel] = targets

    # Find missing backlinks
    missing = []
    for source, targets in links.items():
        for target in targets:
            if target in links and source not in links[target]:
                # target exists and doesn't link back to source
                # Only care about content files, not MOCs
                if "_MOC" in source or "MOC-" in source:
                    continue
                if "_MOC" in target or "MOC-" in target:
                    continue
                source_no_ext = source.replace(".md", "")
                missing.append((target, source_no_ext))

    # Group by target file
    from collections import defaultdict
    to_add = defaultdict(list)
    for target, source_link in missing:
        to_add[target].append(source_link)

    added = 0
    for target_path, backlinks in to_add.items():
        if target_path not in all_files:
            continue

        md_file = all_files[target_path]
        content = md_file.read_text(encoding="utf-8", errors="ignore")

        # Only add links that aren't already present
        new_links = []
        for bl in backlinks:
            if f"[[{bl}]]" not in content and f"[[{bl}|" not in content:
                new_links.append(bl)

        if not new_links:
            continue

        # Add to existing Related section or create one
        if "## Related" in content:
            insert_links = "\n".join(f"- [[{bl}]]" for bl in new_links[:5])  # Cap at 5
            content = content.rstrip() + "\n" + insert_links + "\n"
        else:
            insert_links = "\n".join(f"- [[{bl}]]" for bl in new_links[:5])
            content = content.rstrip() + f"\n\n## Related\n{insert_links}\n"

        md_file.write_text(content, encoding="utf-8")
        added += len(new_links)
        print(f"  + backlinks: {target_path} (+{len(new_links)} links)")

    return added


def main():
    # Phase 1: Fix short wikilinks
    print("=== Phase 1: Fixing short wikilinks ===")
    total_files = 0
    total_changes = 0

    for md_file in VAULT.rglob("*.md"):
        rel = str(md_file.relative_to(VAULT))
        if any(skip in rel for skip in [".obsidian", ".trash", "scripts"]):
            continue

        content = md_file.read_text(encoding="utf-8", errors="ignore")
        new_content, changes = fix_short_wikilinks(content)

        if changes > 0:
            md_file.write_text(new_content, encoding="utf-8")
            total_files += 1
            total_changes += changes
            print(f"  + {rel} ({changes} links fixed)")

    print(f"\nPhase 1 done: {total_changes} short wikilinks fixed in {total_files} files")

    # Phase 2: Fix bidirectional links
    print("\n=== Phase 2: Fixing bidirectional links ===")
    added = fix_bidirectional_links()
    print(f"\nPhase 2 done: {added} backlinks added")


if __name__ == "__main__":
    main()
