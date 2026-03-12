---
type: bug-fix
project: brantham
date: 2026-02-19
component: scraping
severity: medium
tags: [scraping, gemweb]
---

# Gemweb scraper false positives from table filters

## Symptom
Gemweb RSS scraper producing false positive results from filtered table elements.

## Root Cause
Parser was picking up filter/navigation elements as content.

## Fix
Custom parser to skip table filter elements.

## Prevention
Always validate scraped content against expected format before ingesting.
