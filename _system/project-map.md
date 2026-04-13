---
type: reference
updated: 2026-03-12
---

# Project File Map

All Brantham-related files and their locations.

## Brantham Partners — Repos

| Component | Location | Stack | Notes |
|-----------|----------|-------|-------|
| **Backend API** | `/Users/paul/Desktop/brantham-partners/api/` | FastAPI, 3900 lines | Main API, 50+ endpoints |
| **Data Pipeline** | `/Users/paul/Desktop/brantham-partners/` | Python, Prefect, PostgreSQL | Docker: postgres, redis, pgadmin |
| **Frontend Dashboard** | `/Users/paul/internal-tool/` | React 19, Vite 7, Zustand | Port 5174, proxy → 3000 |
| **Agent Pipeline** | `/Users/paul/Downloads/brantham-pipeline/` | Node.js server.js + 6 agents | Port 3000, 6 OpenClaw agents |
| **Memory Vault (ops)** | `/Users/paul/Desktop/brantham-partners/memory-vault/` | Markdown | BRAIN.md, agents/, deals/, pipeline/ |
| **Deals Archive** | `/Users/paul/brantham-vault/` | Markdown | 600+ deal files with YAML frontmatter |
| **Design / Next.js** | `/Users/paul/Desktop/brantham-next/` | Next.js, Tailwind | Design system, teaser template |
| **Data Scripts** | `/Users/paul/Downloads/brantham-data/` | Python, pandas, lifelines | Collectors, scorers, venv with Python 3 |
| **Pipeline Scripts** | `/Users/paul/Library/Brantham/scripts/` | Python, bash | Cron launcher, enrichment scripts |
| **Cron Config** | `/Users/paul/Library/LaunchAgents/com.brantham.daily.plist` | launchd | Daily 07h00 |
| **Teaser Template** | `/Users/paul/Desktop/Template Teaser.pptx` | PowerPoint | Shape matching by position |

## Website / SEO Machine

| Component | Location | Stack |
|-----------|----------|-------|
| **SEO Machine** | `/Users/paul/zura-inspired/` | Claude Code workspace, Python analytics |
| **WordPress plugin** | (within zura-inspired) | seo-machine-yoast-rest.php |

## Infrastructure

| Service | Location | Details |
|---------|----------|---------|
| **PostgreSQL 16** | Docker `brantham-data-postgres-1` | Port 5432, db: brantham |
| **Redis 7** | Docker | Cache |
| **pgAdmin** | Docker | DB admin |
| **Hetzner VPS** | 95.216.198.143 | Production deploy |
| **brew postgres@16** | Local | Auto-restarts via launchd — kill with `pg_ctl stop -D /opt/homebrew/var/postgresql@16 -m fast` |

## Unified Vault

| Component | Location |
|-----------|----------|
| **Vault root** | `/Users/paul/vault/` |
| **Old founder vault** | `/Users/paul/founder-vault/vault/` (superseded, was empty) |

## Python Environments

| Venv | Location | Purpose |
|------|----------|---------|
| Pipeline scripts | `/Users/paul/Library/Brantham/venv/bin/python3.14` | Cron pipeline |
| Data collectors | `/Users/paul/Downloads/brantham-data/venv/bin/python3` | pandas, lifelines |

## Greffe Extraction (one-off)

| Component | Location |
|-----------|----------|
| **TC Paris** | `/Users/paul/Downloads/Extraction-Greffe-TC-Paris-34---SAS-COSA/` |
