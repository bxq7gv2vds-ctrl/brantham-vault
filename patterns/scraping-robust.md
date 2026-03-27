---
type: pattern
project: brantham
date: 2026-03-12
category: scraping
tags: [scraping, bodacc, parser]
---

# Robust Scraping Pattern

## Problem
20+ AJ sources with different formats, encodings, and structures. False positives, partial scans, encoding issues.

## Solution
- Gemweb RSS: description is triple-encoded HTML -> custom parser to decode
- AJRS: blocks separated by #XXXX -> split parser
- Dates: multiple formats -> normalize to ISO YYYY-MM-DD
- Placeholder date 2100-01-01 = "no deadline" -> clear it
- Filter mailto: links, table filters, navigation elements
- Always validate scraped content against expected format before ingesting
- Partial scans pollute diff -> track scan completeness

## When to Use
Any web scraping of French legal/judicial sources.

## Gotchas
- Always check for encoding issues (triple-encoded HTML is common)
- Gemweb filter tables create false positives
- Some sources use JS rendering (need headless browser)

## Related
- [[_system/MOC-patterns]]
- [[patterns/agent-orchestration]]
- [[patterns/gemweb-rss-parsing]]
- [[patterns/teaser-pptx-generation]]
- [[patterns/prefect-pipeline]]
- [[brantham/patterns/scoring-patterns]]
- [[brantham/patterns/teaser-patterns]]
- [[brantham/patterns/acheteur-mapping]]
- [[founder/journal/2026-03-12]]
- [[founder/decisions/2026-03-12-unified-vault]]
- [[brantham/bugs/2026-02-19-scraper-abitbol-mailto]]
- [[brantham/bugs/2026-02-19-llm-glm47-content-null]]
- [[brantham/bugs/2026-02-19-scraper-gemweb-false-positives]]
