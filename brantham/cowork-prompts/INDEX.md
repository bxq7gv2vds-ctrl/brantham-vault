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
07h15  → 05-morning-brief.md     (brief Paul + Soren — plan du jour)
08h00  → 02-pipeline-check.md    (alertes deadlines, état pipeline)
08h30  → 03-deal-analysis.md     (analyse deals detecte → analysé)
09h00  → 04-buyer-hunt.md        (sourcing acheteurs → acheteurs_identifiés)
09h30  → 07-contact-enricher.md  (enrichissement contacts → prêt outreach)

12h00  → 01-sourcing.md          (scan midi)

14h00  → 04-buyer-hunt.md        (2ème run si nouveaux deals analysés)
15h00  → 03-deal-analysis.md     (2ème run si nouveaux deals détectés)
16h00  → 07-contact-enricher.md  (2ème run si nouveaux acheteurs)
17h00  → 02-pipeline-check.md    (bilan fin de journée)

19h30  → 01-sourcing.md          (scan soir)
```

## Agents

| Fichier | Agent | Schedule | Mission |
|---------|-------|----------|---------|
| [[01-sourcing]] | Sourcing | 07h / 12h / 19h30 | Scrape AJ + BODACC, score, met à jour OPPORTUNITIES.md |
| [[05-morning-brief]] | Morning Brief | 07h15 | Brief actionnable Paul + Soren |
| [[02-pipeline-check]] | Pipeline Check | 08h / 17h | Surveille deadlines, alertes rouges/oranges |
| [[03-deal-analysis]] | Deal Analysis | 08h30 / 15h | Analyse financière + juridique sur infos publiques |
| [[04-buyer-hunt]] | Buyer Hunt | 09h / 14h | Sourcing 15-25 acheteurs qualifiés par deal |
| [[07-contact-enricher]] | Contact Enricher | 09h30 / 16h | Enrichissement emails + LinkedIn décideurs |

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
