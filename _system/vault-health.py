#!/usr/bin/env python3
"""
Vault Content Health Checker
Detects: stale data, uncompiled raw sources, concept whitespots, orphan mentions.
Usage: python3 vault-health.py [--report <output.md>]
"""

import os
import re
import sys
import yaml
from pathlib import Path
from datetime import datetime, date
from collections import defaultdict, Counter

VAULT_ROOT = Path("/Users/paul/vault")
TODAY = date.today()
STALE_DAYS = 365  # Stats older than this are flagged


# ─── Utilities ────────────────────────────────────────────────────────────────

def read_file(path):
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""

def parse_frontmatter(content):
    if not content.startswith("---"):
        return {}, content
    end = content.find("---", 3)
    if end == -1:
        return {}, content
    try:
        fm = yaml.safe_load(content[3:end])
        return fm or {}, content[end + 3:]
    except Exception:
        return {}, content

def extract_dates_from_text(text):
    """Find all dates in text (YYYY-MM-DD or YYYY format near numbers)."""
    patterns = [
        r'\b(20\d{2}-\d{2}-\d{2})\b',
        r'\b(20\d{2})\b',
    ]
    found = []
    for pattern in patterns:
        for m in re.finditer(pattern, text):
            raw = m.group(1)
            try:
                if len(raw) == 4:
                    d = date(int(raw), 1, 1)
                else:
                    d = date.fromisoformat(raw)
                found.append((d, m.start()))
            except ValueError:
                pass
    return found

def extract_wikilinks(content):
    return re.findall(r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]', content)

def all_md_files(subpath="", exclude_system=False):
    base = VAULT_ROOT / subpath if subpath else VAULT_ROOT
    for f in sorted(base.rglob("*.md")):
        if exclude_system and "_system" in f.parts:
            continue
        yield f


# ─── Check 1: Uncompiled Raw Sources ──────────────────────────────────────────

def check_uncompiled_raw():
    """Raw files with empty compiled_into field."""
    issues = []
    raw_dir = VAULT_ROOT / "brantham/knowledge/raw"
    if not raw_dir.exists():
        return issues

    for f in raw_dir.glob("*.md"):
        if f.name == "README.md":
            continue
        content = read_file(f)
        fm, _ = parse_frontmatter(content)
        compiled = fm.get("compiled_into", [])
        if not compiled:
            issues.append({
                "file": f.relative_to(VAULT_ROOT),
                "title": fm.get("title", f.stem),
                "ingested": fm.get("date_ingested", "?"),
            })
    return issues


# ─── Check 2: Stale Stats in Concept Articles ─────────────────────────────────

def check_stale_stats():
    """Find concept files with data points dated > STALE_DAYS ago."""
    issues = []
    concepts_dir = VAULT_ROOT / "brantham/knowledge/concepts"
    if not concepts_dir.exists():
        return issues

    # Also scan main knowledge subdirs
    scan_dirs = [concepts_dir] + [
        VAULT_ROOT / "brantham/knowledge" / d
        for d in ["finance", "legal", "market", "procedures", "acteurs", "sectors"]
        if (VAULT_ROOT / "brantham/knowledge" / d).exists()
    ]

    for d in scan_dirs:
        for f in d.glob("*.md"):
            content = read_file(f)
            fm, body = parse_frontmatter(content)
            if fm.get("type") not in ("concept", None):
                continue

            # Look for lines with numbers (stats) and dates nearby
            stale_lines = []
            lines = body.split("\n")
            for i, line in enumerate(lines):
                # Check if line has a year reference that's old
                year_matches = re.findall(r'\b(20\d{2})\b', line)
                for yr in year_matches:
                    try:
                        age = TODAY.year - int(yr)
                        if age >= int(STALE_DAYS / 365) and re.search(r'\d+\s*[%€kKMm]', line):
                            stale_lines.append(f"L{i+1}: {line.strip()[:80]}")
                    except ValueError:
                        pass

            if stale_lines:
                issues.append({
                    "file": f.relative_to(VAULT_ROOT),
                    "stale_lines": stale_lines[:3],
                })

    return issues


# ─── Check 3: Orphan Mentions (concepts without an article) ───────────────────

def check_orphan_mentions():
    """Find wikilinks pointing to non-existent vault files — true article candidates."""
    # Build index of all existing vault files (path stems)
    existing_files = set()
    for f in all_md_files():
        # Index by full path relative to vault (no extension)
        rel = str(f.relative_to(VAULT_ROOT).with_suffix(""))
        existing_files.add(rel.lower())
        existing_files.add(f.stem.lower())  # also by stem alone

    broken_links = Counter()
    broken_link_examples = defaultdict(list)  # link -> list of source files
    skip_dirs = {"_system"}

    for f in all_md_files(exclude_system=True):
        if any(s in f.parts for s in skip_dirs):
            continue
        content = read_file(f)
        _, body = parse_frontmatter(content)

        for link in extract_wikilinks(body):
            # Normalize: remove alias, strip whitespace
            link_clean = link.split("|")[0].strip().lower()
            link_stem = Path(link_clean).stem.lower()

            # Check if target exists
            if link_clean not in existing_files and link_stem not in existing_files:
                broken_links[link_clean] += 1
                if f.relative_to(VAULT_ROOT) not in broken_link_examples[link_clean]:
                    broken_link_examples[link_clean].append(str(f.relative_to(VAULT_ROOT)))

    # Return broken links referenced 2+ times (genuine candidates)
    orphans = []
    for link, count in broken_links.most_common(30):
        if count >= 2:
            orphans.append({
                "term": link,
                "count": count,
                "examples": broken_link_examples[link][:2],
            })

    return orphans[:20]


# ─── Check 4: Knowledge Map Whitespots ────────────────────────────────────────

def check_knowledge_whitespots():
    """Subdirs in knowledge/ with very few files (potential whitespots)."""
    issues = []
    knowledge_dir = VAULT_ROOT / "brantham/knowledge"
    if not knowledge_dir.exists():
        return issues

    for subdir in sorted(knowledge_dir.iterdir()):
        if not subdir.is_dir() or subdir.name in ("raw", "concepts"):
            continue
        md_files = list(subdir.glob("*.md"))
        if len(md_files) <= 1:
            issues.append({
                "dir": subdir.relative_to(VAULT_ROOT),
                "count": len(md_files),
            })

    return issues


# ─── Check 5: Files Without Related Section ───────────────────────────────────

def check_missing_related():
    """Count files by type that are missing ## Related."""
    missing = []
    for f in all_md_files(exclude_system=True):
        content = read_file(f)
        fm, body = parse_frontmatter(content)
        ftype = fm.get("type", "")
        if ftype in ("concept", "raw-source", "ingested", "pattern", "decision", "bug", "session", "assumption"):
            if "## Related" not in body:
                missing.append({"file": f.relative_to(VAULT_ROOT), "type": ftype})
    return missing


# ─── Report Generation ────────────────────────────────────────────────────────

def generate_report(results):
    lines = [
        f"---",
        f"type: health-report",
        f"date: {TODAY.isoformat()}",
        f"generated_by: vault-health.py",
        f"---",
        f"",
        f"# Vault Health Report — {TODAY.isoformat()}",
        f"",
    ]

    # Summary
    total_issues = sum(len(v) for v in results.values())
    lines += [
        f"## Summary",
        f"",
        f"| Check | Issues |",
        f"|-------|--------|",
        f"| Uncompiled raw sources | {len(results['uncompiled'])} |",
        f"| Stale stats in concepts | {len(results['stale'])} |",
        f"| Orphan mentions (no article) | {len(results['orphans'])} |",
        f"| Knowledge whitespots | {len(results['whitespots'])} |",
        f"| Missing ## Related | {len(results['missing_related'])} |",
        f"",
        f"**Total issues: {total_issues}**",
        f"",
    ]

    # Uncompiled raw
    if results["uncompiled"]:
        lines += [f"## Uncompiled Raw Sources", f""]
        lines += [f"Sources ingérées mais pas encore compilées en concept :"]
        lines += [""]
        for item in results["uncompiled"]:
            lines.append(f"- `{item['file']}` — {item['title']} (ingested: {item['ingested']})")
        lines.append("")

    # Stale stats
    if results["stale"]:
        lines += [f"## Stale Stats (>1 year)", f""]
        for item in results["stale"]:
            lines.append(f"- `{item['file']}`")
            for sl in item["stale_lines"]:
                lines.append(f"  - {sl}")
        lines.append("")

    # Orphan mentions (broken wikilinks)
    if results["orphans"]:
        lines += [f"## Broken Wikilinks — Article Candidates", f""]
        lines += [f"Wikilinks référencés mais sans fichier cible — à créer ou à corriger :"]
        lines += [""]
        for item in results["orphans"][:15]:
            examples_str = ", ".join(f"`{e}`" for e in item["examples"])
            lines.append(f"- `[[{item['term']}]]` ({item['count']}x) — dans {examples_str}")
        lines.append("")

    # Whitespots
    if results["whitespots"]:
        lines += [f"## Knowledge Whitespots", f""]
        for item in results["whitespots"]:
            lines.append(f"- `{item['dir']}` — seulement {item['count']} fichier(s)")
        lines.append("")

    # Missing related
    if results["missing_related"]:
        lines += [f"## Missing ## Related Section ({len(results['missing_related'])} files)", f""]
        lines += [f"Corriger avec: `python3 vault-linker.py fix`", f""]
        for item in results["missing_related"][:10]:
            lines.append(f"- `{item['file']}` ({item['type']})")
        if len(results["missing_related"]) > 10:
            lines.append(f"- ... et {len(results['missing_related']) - 10} autres")
        lines.append("")

    lines += [
        "## Related",
        "",
        "- [[brantham/_MOC]]",
        "- [[_system/MOC-master]]",
    ]

    return "\n".join(lines)


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    report_path = None
    if "--report" in sys.argv:
        idx = sys.argv.index("--report")
        if idx + 1 < len(sys.argv):
            report_path = Path(sys.argv[idx + 1])

    print(f"Running vault health check — {TODAY.isoformat()}")
    print(f"Vault: {VAULT_ROOT}\n")

    results = {
        "uncompiled": check_uncompiled_raw(),
        "stale": check_stale_stats(),
        "orphans": check_orphan_mentions(),
        "whitespots": check_knowledge_whitespots(),
        "missing_related": check_missing_related(),
    }

    report = generate_report(results)

    if report_path:
        report_path.write_text(report, encoding="utf-8")
        print(f"Report saved: {report_path}")
    else:
        print(report)

    total = sum(len(v) for v in results.values())
    return 0 if total == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
