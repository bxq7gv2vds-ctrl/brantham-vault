---
type: bug-fix
project: brantham
date: 2026-02-19
component: llm
severity: high
tags: [llm, glm, agents]
---

# GLM-4.7 (NIM) returns content=null

## Symptom
LLM responses from GLM-4.7 via NIM had content=null in the response object.

## Root Cause
GLM-4.7 puts the actual content in reasoning_content field, not content.

## Fix
Extract from reasoning_content when content is null. Also set MAX_TOKENS >= 3000.

## Prevention
Always check both content and reasoning_content fields when integrating new LLM providers.
