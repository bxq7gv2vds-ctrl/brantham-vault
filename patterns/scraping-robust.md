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
