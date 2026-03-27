#!/usr/bin/env python3
"""
Vault Wikilink Auditor & Auto-Linker
Scans all .md files in vault, identifies missing wikilinks, applies fixes.
"""

import os
import re
from pathlib import Path
from collections import defaultdict

VAULT_ROOT = Path("/Users/paul/vault")

# File patterns and their linking rules
LINKING_RULES = {
    "decision": {
        "backlinks": ["[[_system/MOC-decisions]]", "[[brantham/_MOC]]"],
        "optional": ["[[_system/MOC-assumptions]]", "[[founder/strategy/current-strategy]]"],
    },
    "bug": {
        "backlinks": ["[[_system/MOC-bugs]]", "[[brantham/_MOC]]"],
        "optional": ["[[brantham/patterns/", "[[founder/sessions/"],
    },
    "pattern": {
        "backlinks": ["[[_system/MOC-patterns]]", "[[brantham/_MOC]]"],
        "optional": ["[[brantham/bugs/"],
    },
    "session": {
        "backlinks": ["[[brantham/_MOC]]", "[[website/_MOC]]"],
        "optional": ["[[founder/daily/", "[[founder/decisions/", "[[founder/assumptions/"],
    },
    "assumption": {
        "backlinks": ["[[_system/MOC-assumptions]]", "[[brantham/_MOC]]"],
        "optional": ["[[_system/MOC-decisions]]", "[[founder/strategy/"],
    },
}

def detect_file_type(file_path):
    """Detect file type from path and frontmatter."""
    path = file_path.relative_to(VAULT_ROOT)
    path_str = str(path)

    # Pattern matching
    if "decisions" in path_str:
        return "decision"
    elif "bugs" in path_str:
        return "bug"
    elif "patterns" in path_str:
        return "pattern"
    elif "sessions" in path_str:
        return "session"
    elif "assumptions" in path_str:
        return "assumption"
    elif "_MOC" in path_str:
        return "moc"

    # Check frontmatter
    try:
        with open(file_path, "r") as f:
            content = f.read()
            if content.startswith("---"):
                match = re.search(r'type:\s*(\w+)', content)
                if match:
                    return match.group(1)
    except:
        pass

    return "unknown"

def has_related_section(content):
    """Check if file has ## Related section with wikilinks."""
    related_match = re.search(r'## Related.*?(?=\n##|\Z)', content, re.DOTALL)
    if not related_match:
        return False

    related_section = related_match.group(0)
    return "[[" in related_section

def extract_existing_wikilinks(content):
    """Extract all wikilinks from content."""
    return re.findall(r'\[\[([^\]]+)\]\]', content)

def audit():
    """Scan vault and report missing wikilinks."""
    stats = defaultdict(list)

    for file_path in sorted(VAULT_ROOT.glob("**/*.md")):
        if "_system" in str(file_path) or file_path.name == "MEMORY.md":
            continue

        file_type = detect_file_type(file_path)

        try:
            with open(file_path, "r") as f:
                content = f.read()
        except:
            continue

        has_related = has_related_section(content)
        existing_links = extract_existing_wikilinks(content)

        if file_type != "unknown" and not has_related:
            stats[file_type].append({
                "path": file_path.relative_to(VAULT_ROOT),
                "links": len(existing_links),
            })

    # Print report
    print("\n=== VAULT WIKILINK AUDIT ===\n")
    total_missing = 0
    for ftype in ["decision", "bug", "pattern", "session", "assumption"]:
        if ftype in stats:
            files = stats[ftype]
            print(f"❌ {ftype.upper()}: {len(files)} files missing ## Related")
            total_missing += len(files)
            for item in files[:3]:  # Show first 3
                print(f"   - {item['path']}")
            if len(files) > 3:
                print(f"   ... and {len(files) - 3} more")

    print(f"\n📊 Total files needing links: {total_missing}\n")
    return stats

def generate_related_section(file_type, file_path, existing_links):
    """Generate ## Related section based on file type and path."""
    lines = ["", "## Related", ""]

    if file_type not in LINKING_RULES:
        return "\n".join(lines)

    rules = LINKING_RULES[file_type]
    links_to_add = set()

    # Add backlinks
    for link in rules.get("backlinks", []):
        links_to_add.add(link)

    # Parse date from filename for cross-day linking
    match = re.search(r'(\d{4})-(\d{2})-(\d{2})', file_path.name)
    if match and file_type in ["decision", "bug", "pattern", "session"]:
        # Link to same-day session/decisions
        date = f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
        if file_type == "session":
            links_to_add.add(f"[[founder/daily/{date}-auto-brief.md|Daily — {date}]]")

    # Convert set to sorted list
    for link in sorted(links_to_add):
        if link not in existing_links:
            lines.append(f"- {link}")

    return "\n".join(lines)

def auto_link_file(file_path):
    """Add missing ## Related section to file."""
    file_type = detect_file_type(file_path)

    if file_type == "unknown":
        return False

    try:
        with open(file_path, "r") as f:
            content = f.read()
    except:
        return False

    if has_related_section(content):
        return False  # Already has links

    existing_links = extract_existing_wikilinks(content)
    related_section = generate_related_section(file_type, file_path, existing_links)

    # Append ## Related section
    new_content = content.rstrip() + related_section

    try:
        with open(file_path, "w") as f:
            f.write(new_content)
        return True
    except:
        return False

def batch_link():
    """Apply auto-linking to all files missing ## Related."""
    stats = audit()

    updated = 0
    for ftype in stats:
        for item in stats[ftype]:
            file_path = VAULT_ROOT / item["path"]
            if auto_link_file(file_path):
                updated += 1

    print(f"\n✅ Updated {updated} files with wikilinks")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "fix":
        batch_link()
    else:
        audit()
