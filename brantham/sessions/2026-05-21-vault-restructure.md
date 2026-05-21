---
type: session
project: brantham
date: 2026-05-21
---

# Session — Restructuration vault Brantham

## Objectif

Rendre le vault plus léger, navigable, et supprimer le contenu hors-sujet ou redondant.

## Supprimé (~281 Mo)

| Contenu | Raison |
|---------|--------|
| `knowledge/raw/rl-foundations/` (107 Mo) | Cours RL, hors M&A |
| `deals/infra/dataroom/*.pdf` (141 Mo) | Doublon Google Drive + AJ |
| `sessions/auto-enrichment-*.md` (~50 fichiers) | Logs cron, redondant DB |
| `sessions/auto-health-*.md` | Logs cron health |
| `deals/aj-feed/` (39 fichiers) | Gardé 2 derniers jours |
| PNGs LinkedIn dupliqués | navy + meme 3 Mo |

## Restructuré

- `deals/infra/` → `deals/active/infra/` (deal actif)
- `brantham/_MOC.md` : 276 → ~70 lignes (hub navigation)
- `deals/_MOC.md` : tableau deals actifs + identified
- `sessions/_MOC.md` : index sessions humaines
- `aj-feed/_INDEX.md` : 2 entrées seulement
- `tc-paris-extraction/grilles/_schema.md` : stub liens cassés
- `.gitignore` : PDFs dataroom, pycache

## Taille

339 Mo → **58 Mo**

## Related

- [[brantham/_MOC]]
- [[brantham/reports/health-2026-05-21]]
- [[brantham/deals/_MOC]]
- [[brantham/sessions/_MOC]]
