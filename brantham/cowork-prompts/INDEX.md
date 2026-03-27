---
type: index
project: brantham
updated: 2026-03-27
---

# Brantham — Cowork Prompts Index

7 agents Cowork pour automatiser toute la chaîne de deals. Copier-coller chaque prompt directement dans Cowork.

## Schedule quotidien

```
07h00  → 01-sourcing.md          (scan AJ + BODACC matin)
07h30  → 05-morning-brief.md     (agrège tout, plan du jour Paul + Soren)
09h00  → 02-pipeline-check.md    (surveillance deadlines, alertes)
10h00  → 03-deal-analysis.md     (analyse deals detecte → analysé)
11h00  → 04-buyer-hunt.md        (sourcing acheteurs analysé → acheteurs_identifiés)
12h00  → 01-sourcing.md          (scan midi)
14h00  → 04-buyer-hunt.md        (2ème run buyer hunt)
15h00  → 03-deal-analysis.md     (2ème run analyse)
16h00  → 07-contact-enricher.md  (enrichissement contacts → prêt outreach)
17h00  → 02-pipeline-check.md    (bilan soir)
19h30  → 01-sourcing.md          (scan soir)
```

## Agents

| Fichier | Agent | Schedule | Mission |
|---------|-------|----------|---------|
| [[01-sourcing]] | Sourcing | 07h/12h/19h30 | Scrape AJ + BODACC, score, met à jour OPPORTUNITIES.md |
| [[02-pipeline-check]] | Pipeline Check | 09h/17h | Surveille deadlines, alertes rouges/oranges |
| [[03-deal-analysis]] | Deal Analysis | 10h/15h | Analyse financière + juridique sur infos publiques |
| [[04-buyer-hunt]] | Buyer Hunt | 11h/14h | Sourcing 15-25 acheteurs qualifiés par deal |
| [[05-morning-brief]] | Morning Brief | 07h30 | Brief actionnable Paul + Soren |
| [[06-teaser-factory]] | Teaser Factory | 12h30 | Génération teaser markdown + email + PPTX |
| [[07-contact-enricher]] | Contact Enricher | 16h | Enrichissement emails + LinkedIn décideurs |

## État partagé (lire/écrire)

```
BRAIN.md        : ~/.openclaw/agents/_shared/BRAIN.md
OPPORTUNITIES   : ~/.openclaw/agents/_shared/OPPORTUNITIES.md
Deals           : /Users/paul/Downloads/brantham-pipeline/deals/[slug]/
Dashboard API   : http://localhost:3000
```

## Pipeline des statuts

```
detecte → en_analyse → analysé → teaser_rédigé → acheteurs_identifiés → contacts_enrichis → en_approche → clos
   ↑            ↑          ↑              ↑                  ↑                   ↑
sourcing    deal-analysis  teaser-factory  buyer-hunt    contact-enricher     [Soren]
```

## Règles communes à tous les agents

1. **Lire BRAIN.md + OPPORTUNITIES.md en premier** — toujours
2. **Mettre à jour BRAIN.md en fin de session** — toujours
3. **Ne jamais inventer un chiffre** — si absent → "ND"
4. **Ne pas empiéter sur le rôle d'un autre agent** — chacun son périmètre
5. **Signaler deadline < 14 jours dans BRAIN.md** — immédiatement

## Related
- [[brantham/COWORK-PROMPT]]
- [[brantham/context/process-end-to-end]]
- [[brantham/context/sow]]
- [[brantham/_MOC]]
