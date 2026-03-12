---
type: bug-fix
project: brantham
date: 2026-03-06
component: agents
severity: medium
tags: [agents, parser]
---

# Handoff commercial raw wrapper parse_error

## Symptom
Commercial handoff data coming through as raw wrapper with parse_error.

## Root Cause
Handoff data format not properly parsed.

## Fix
Implement parse_handoff() Python function to properly extract structured data from handoff wrapper.
