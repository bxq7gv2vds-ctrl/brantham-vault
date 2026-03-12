---
type: pattern
project: brantham
date: 2026-03-12
category: data
tags: [prefect, pipeline, orchestration]
---

# Prefect Pipeline Pattern

## Problem
Complex multi-step data pipelines with dependencies, error handling, and scheduling.

## Solution
Prefect flows with sequential steps and error handling:
1. Each step is a Prefect task
2. Steps execute sequentially within a flow
3. Daily + weekly + monthly schedules via cron
4. Each step is idempotent (can be re-run safely)
5. Use launchd plist on macOS for scheduling (com.brantham.daily.plist at 07h00)

## When to Use
ETL pipelines, data enrichment, batch processing.

## Gotchas
- brew postgres@16 auto-restarts via launchd -- must kill before operations
- Materialized views need CONCURRENTLY for production refreshes
- Always use idempotent operations (INSERT ON CONFLICT)
