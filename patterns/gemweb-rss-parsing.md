---
type: pattern
project: brantham
date: 2026-03-12
category: scraping
tags: [gemweb, rss, scraping]
---

# Gemweb RSS Triple-Encoded HTML Parsing

## Problem
Gemweb RSS feeds have description content that is triple-encoded HTML.

## Solution
Decode in stages: XML entity decode -> HTML entity decode -> strip tags -> extract text. Custom parser for each decode stage.

## When to Use
Parsing Gemweb RSS feeds for AJ announcements.

## Gotchas
- Filter out table elements (false positives from filters)
- 14 Gemweb RSS sources with slightly different formats
- Partial scans can pollute the diff
