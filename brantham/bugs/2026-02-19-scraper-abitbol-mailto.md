---
type: bug-fix
project: brantham
date: 2026-02-19
component: scraping
severity: low
tags: [scraping, abitbol]
---

# Abitbol scraper mailto: in href

## Symptom
Abitbol scraper following mailto: links as regular URLs.

## Root Cause
Custom parser not filtering out mailto: protocol in href attributes.

## Fix
Filter href attributes to skip mailto: protocol.

## Related
- [[_system/MOC-bugs]]
- [[brantham/_MOC]]
- [[brantham/bugs/2026-02-19-pipeline-cron-delivery]]
- [[brantham/bugs/2026-02-19-llm-glm47-content-null]]
- [[brantham/bugs/2026-02-19-scraper-gemweb-false-positives]]
