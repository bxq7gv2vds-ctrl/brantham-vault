#!/usr/bin/env python3
"""
Batch add wikilinks to vault files that lack cross-references.
Scans all .md files, identifies related files by date/project/type,
and appends a ## Related section with appropriate wikilinks.
"""
import os
import re
import yaml
from pathlib import Path
from collections import defaultdict
from datetime import datetime

VAULT = Path("/Users/paul/vault")
SKIP_DIRS = {"_system", ".obsidian", ".trash"}
SKIP_FILES = {"_MOC.md", "MOC-master.md", "MOC-decisions.md", "MOC-bugs.md",
              "MOC-patterns.md", "MOC-assumptions.md", "BOARD.md"}

# MOC mapping by type
MOC_MAP = {
    "bug-fix": "_system/MOC-bugs",
    "decision": "_system/MOC-decisions",
    "pattern": "_system/MOC-patterns",
    "assumption": "_system/MOC-assumptions",
}

# Project MOC mapping by path prefix
PROJECT_MOC = {
    "brantham": "brantham/_MOC",
    "website": "website/_MOC",
    "founder": "_system/MOC-master",
    "patterns": "_system/MOC-patterns",
    "twitter": "_system/MOC-master",
}


def parse_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return {}, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        fm = {}
    body = "---".join(parts[2:])
    return fm, body


def has_related_section(content):
    """Check if file already has a Related section."""
    return bool(re.search(r'^##\s+Related', content, re.MULTILINE))


def has_wikilinks(content):
    """Check if content has actual wikilinks (not in frontmatter)."""
    _, body = parse_frontmatter(content)
    return bool(re.findall(r'\[\[(?!decision-link|bug-link|pattern-link)[^\]]+\]\]', body))


def get_project_from_path(rel_path):
    """Determine project from file path."""
    parts = rel_path.parts
    if parts:
        return parts[0]
    return "founder"


def extract_date(fm, filename):
    """Extract date from frontmatter or filename."""
    if fm.get("date"):
        d = str(fm["date"])[:10]
        if re.match(r'\d{4}-\d{2}-\d{2}', d):
            return d
    match = re.match(r'(\d{4}-\d{2}-\d{2})', filename)
    if match:
        return match.group(1)
    return None


def build_index(vault_path):
    """Build index of all vault files by date, type, project."""
    files = {}
    by_date = defaultdict(list)
    by_type = defaultdict(list)
    by_project = defaultdict(list)

    for md_file in vault_path.rglob("*.md"):
        rel = md_file.relative_to(vault_path)

        # Skip system files, MOCs, templates
        if any(part.startswith(".") for part in rel.parts):
            continue
        if rel.parts[0] in SKIP_DIRS and rel.parts[-1] not in SKIP_FILES:
            if "templates" in str(rel) or "scripts" in str(rel):
                continue
        if rel.name in SKIP_FILES:
            continue
        if "_MOC" in rel.name:
            continue
        if "templates" in str(rel):
            continue
        if "scripts" in str(rel):
            continue

        content = md_file.read_text(encoding="utf-8", errors="ignore")
        fm, body = parse_frontmatter(content)

        project = get_project_from_path(rel)
        file_type = fm.get("type", "unknown")
        date = extract_date(fm, rel.name)

        info = {
            "path": rel,
            "abs_path": md_file,
            "fm": fm,
            "type": file_type,
            "project": project,
            "date": date,
            "has_related": has_related_section(content),
            "has_wikilinks": has_wikilinks(content),
            "content": content,
        }

        files[str(rel)] = info
        if date:
            by_date[date].append(info)
        by_type[file_type].append(info)
        by_project[project].append(info)

    return files, by_date, by_type, by_project


def generate_related_links(info, by_date, by_type, files):
    """Generate wikilinks for a file based on context."""
    links = []
    rel_path = info["path"]
    project = info["project"]
    file_type = info["type"]
    date = info["date"]
    rel_str = str(rel_path)

    # 1. Type-specific MOC link
    if file_type in MOC_MAP:
        links.append(f"[[{MOC_MAP[file_type]}]]")

    # 2. Project MOC link
    if project in PROJECT_MOC:
        moc = PROJECT_MOC[project]
        if f"[[{moc}]]" not in links:
            links.append(f"[[{moc}]]")

    # 3. Same-date siblings (session <-> bug <-> decision <-> pattern)
    if date and date in by_date:
        for sibling in by_date[date]:
            sib_path = str(sibling["path"])
            if sib_path == rel_str:
                continue
            # Don't link to daily plans or twitter digests from unrelated files
            sib_type = sibling["type"]
            if sib_type in ("daily-plan",):
                continue
            if sibling["project"] == "twitter" and project != "twitter":
                continue
            # Remove .md extension for wikilink
            link_path = str(sibling["path"]).replace(".md", "")
            link = f"[[{link_path}]]"
            if link not in links:
                links.append(link)

    # 4. Type-specific cross-links from content analysis
    content_lower = info["content"].lower()

    # If bug mentions a pattern name, link it
    if file_type == "bug-fix":
        for f_info in by_type.get("pattern", []):
            pattern_name = f_info["path"].stem.lower()
            if len(pattern_name) > 5 and pattern_name in content_lower:
                link_path = str(f_info["path"]).replace(".md", "")
                link = f"[[{link_path}]]"
                if link not in links:
                    links.append(link)

    # If pattern mentions a bug, link it
    if file_type == "pattern":
        for f_info in by_type.get("bug-fix", []):
            bug_name = f_info["path"].stem.lower()
            # Extract key terms from bug name
            terms = [t for t in bug_name.split("-") if len(t) > 4 and not t.isdigit()]
            if any(t in content_lower for t in terms):
                link_path = str(f_info["path"]).replace(".md", "")
                link = f"[[{link_path}]]"
                if link not in links:
                    links.append(link)

    # If decision references assumptions in frontmatter
    if file_type == "decision" and info["fm"].get("linked_assumptions"):
        for assumption in info["fm"]["linked_assumptions"]:
            if assumption:
                links.append(f"[[founder/assumptions/{assumption}]]")

    # Link to strategy if decision
    if file_type == "decision":
        strategy_link = "[[founder/strategy/current-strategy]]"
        if strategy_link not in links:
            links.append(strategy_link)

    return links


def append_related_section(file_path, content, links):
    """Append ## Related section to file content."""
    if not links:
        return False

    # Build the section
    section = "\n\n## Related\n"
    for link in links:
        section += f"- {link}\n"

    # Append to file
    new_content = content.rstrip() + section
    file_path.write_text(new_content, encoding="utf-8")
    return True


def main():
    print("Scanning vault...")
    files, by_date, by_type, by_project = build_index(VAULT)
    print(f"Found {len(files)} files")

    updated = 0
    skipped = 0
    already_ok = 0

    for rel_str, info in sorted(files.items()):
        # Skip files that already have a Related section
        if info["has_related"]:
            already_ok += 1
            continue

        # Generate links
        links = generate_related_links(info, by_date, by_type, files)

        if not links:
            skipped += 1
            continue

        # Check if file already has these wikilinks
        if info["has_wikilinks"]:
            # Still add Related section if it doesn't exist, even if some links are present
            pass

        success = append_related_section(info["abs_path"], info["content"], links)
        if success:
            updated += 1
            print(f"  + {rel_str} ({len(links)} links)")
        else:
            skipped += 1

    print(f"\nDone:")
    print(f"  Updated: {updated}")
    print(f"  Already had Related: {already_ok}")
    print(f"  Skipped (no links to add): {skipped}")
    print(f"  Total: {len(files)}")


if __name__ == "__main__":
    main()
