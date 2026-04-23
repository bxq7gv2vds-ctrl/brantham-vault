---
type: index
project: brantham
updated: 2026-03-27
---

# Brantham — Cowork Prompts Index

6 agents Cowork + 1 send brief. Une seule fois par jour. Un seul email à 10h00 avec tout.

## Schedule quotidien (avril 2026)

Pipeline en 2 modes : **batch matin** (sourcing + check) puis **event-driven** (déclenché par Paul via Telegram GO).

### Batch matin (cron Cowork)
```
07h00  → 01-sourcing.md          (scan 31 sites AJ + BODACC, score, notif Telegram par opp GO/WATCH)
07h15  → 05-morning-brief.md     (brief Paul + Soren — plan du jour)
08h00  → 02-pipeline-check.md    (alertes deadlines, état pipeline)
10h00  → 08-send-brief.md        ← UN SEUL EMAIL recap (deals scrapes, deals en cours)
```

### Event-driven (déclenché par clic Telegram GO ou queue)

Déclenchement automatique en cascade :
```
notify_telegram listen
    ↓ (Paul clique GO sur Telegram)
~/.openclaw/agents/_shared/queue/buyer-hunt-<slug>-*.json
    ↓
03-deal-analysis.md   (analyse deal → analysé)
    ↓
04-buyer-hunt.md      (30-50 acheteurs qualifiés, CA ≥3×)
    ↓
07-contact-enricher.md (enrichit top 30 + génère outreach-emails.json + outreach-linkedin.md)
    ↓
~/.openclaw/agents/_shared/queue/outreach-<slug>-*.json
    ↓
09-outreach-draft.md  (crée drafts Gmail via API + notif Telegram "drafts prets")
```

Volume cible : **100 mails outreach/jour + 30-40 DMs LinkedIn/jour**.

## Agents

| Fichier | Agent | Schedule | Mission |
|---------|-------|----------|---------|
| [[01-sourcing]] | Sourcing | 07h00 | Scrape AJ + BODACC, score, met à jour OPPORTUNITIES.md |
| [[05-morning-brief]] | Morning Brief | 07h15 | Brief actionnable Paul + Soren |
| [[02-pipeline-check]] | Pipeline Check | 08h00 | Surveille deadlines, alertes rouges/oranges |
| [[03-deal-analysis]] | Deal Analysis | 08h30 | Analyse financière + juridique sur infos publiques |
| [[04-buyer-hunt]] | Buyer Hunt | 09h00 | Sourcing 15-25 acheteurs qualifiés par deal |
| [[07-contact-enricher]] | Contact Enricher | 09h30 | Enrichissement emails + LinkedIn décideurs |
| [[08-send-brief]] | Send Brief | 10h00 | UN email avec tout : pipeline + outreach prêts + actions |

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
