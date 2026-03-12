---
type: pattern
project: brantham
date: 2026-03-12
category: content
tags: [teaser, pptx, llm]
---

# Teaser PPTX Generation Pattern

## Problem
Generate professional M&A teaser documents from analysis data.

## Solution
1. Read analyse.md for the deal
2. LLM synthesizes all fields in one call (synthesize_all_fields -> JSON)
3. Apply to Template Teaser.pptx
4. Shape matching by position (cm): find_shape_by_pos() + euclidean tolerance 0.25
5. Server routes: POST /api/deals/:slug/generate-teaser, GET /api/deals/:slug/teaser.pptx

Template location: /Users/paul/Desktop/Template Teaser.pptx

## When to Use
Generating professional PPTX documents from structured data.

## Gotchas
- Shape matching is position-based (fragile to template changes)
- Use single LLM call for all fields (cheaper, more consistent)
- Template must be maintained separately
