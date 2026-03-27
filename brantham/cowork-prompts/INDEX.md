---
type: index
project: brantham
updated: 2026-03-27
---

# Brantham — Cowork Prompts Index

6 agents Cowork, chacun envoie un email après son run. Une seule fois par jour.

## Schedule quotidien

```
07h00  → 01-sourcing.md          → email "[Brantham] Sourcing 07h00 — X GO détectés"
07h15  → 05-morning-brief.md     → email "[Brantham] Morning Brief 07h15 — X alertes rouges"
08h00  → 02-pipeline-check.md    → email "[Brantham] Pipeline Check 08h00 — score X/100"
08h30  → 03-deal-analysis.md     → email "[Brantham] Deal Analysis 08h30 — [slug] score X/100"
09h00  → 04-buyer-hunt.md        → email "[Brantham] Buyer Hunt 09h00 — X acheteurs qualifiés"
09h30  → 07-contact-enricher.md  → email "[Brantham] Contact Enricher 09h30 — X contacts prêts"
```

Chaque email contient : ce que l'agent vient de faire + l'état complet du pipeline + les emails outreach prêts.

## Agents

| Fichier | Agent | Schedule | Mission |
|---------|-------|----------|---------|
| [[01-sourcing]] | Sourcing | 07h00 | Scrape AJ + BODACC, score, met à jour OPPORTUNITIES.md |
| [[05-morning-brief]] | Morning Brief | 07h15 | Brief actionnable Paul + Soren |
| [[02-pipeline-check]] | Pipeline Check | 08h00 | Surveille deadlines, alertes rouges/oranges |
| [[03-deal-analysis]] | Deal Analysis | 08h30 | Analyse financière + juridique sur infos publiques |
| [[04-buyer-hunt]] | Buyer Hunt | 09h00 | Sourcing 15-25 acheteurs qualifiés par deal |
| [[07-contact-enricher]] | Contact Enricher | 09h30 | Enrichissement emails + LinkedIn décideurs |

## Agréger tous les outputs

Chaque agent écrit un JSON dans `vault/brantham/cowork-outputs/`. Pour tout lire en un seul rapport :

```bash
# Rapport du jour
python3 /Users/paul/Downloads/brantham-pipeline/collect_outputs.py

# Rapport d'une date précise
python3 /Users/paul/Downloads/brantham-pipeline/collect_outputs.py --date 2026-03-27

# Tout l'historique
python3 /Users/paul/Downloads/brantham-pipeline/collect_outputs.py --all
```

Output → `vault/brantham/cowork-outputs/REPORT-YYYY-MM-DD.md`

Contient : résumé exécutif, actions Paul/Soren, détail par agent, erreurs, fichiers produits.

## État partagé (lire/écrire)

```
BRAIN.md        : ~/.openclaw/agents/_shared/BRAIN.md
OPPORTUNITIES   : ~/.openclaw/agents/_shared/OPPORTUNITIES.md
Deals           : /Users/paul/Downloads/brantham-pipeline/deals/[slug]/
Dashboard API   : http://localhost:3000
```

## Pipeline des statuts

```
detecte → en_analyse → analysé → acheteurs_identifiés → contacts_enrichis → en_approche → clos
   ↑            ↑          ↑              ↑                   ↑
sourcing    deal-analysis  [manuel]    buyer-hunt       contact-enricher     [Soren]
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
