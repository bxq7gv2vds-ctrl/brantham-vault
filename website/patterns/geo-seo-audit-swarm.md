---
title: "Pattern — Audit SEO multi-agents avec swarm"
date: 2026-03-21
project: website
type: pattern
---

# Audit SEO multi-agents avec swarm

## Quand l'utiliser
Site avec 50+ pages a auditer. Un seul agent ne peut pas tout lire en une passe.

## Pattern
1. Lister toutes les pages (find *.html)
2. Split en batches de 15-20 pages
3. Dispatch 4 agents en parallele, chacun avec un batch
4. Checklist par page : title, meta, canonical, OG, schemas, H1, speakable, liens internes, word count
5. Collecter les rapports, fusionner les issues
6. Prioriser P0/P1/P2
7. Dispatch workers de fix en parallele (par fichier, pas de conflits)

## Attention
- Les agents auditeurs surestiment parfois les longueurs de meta (encodage guillemets)
- Verifier manuellement les cas limites
- Les pages generees vs manuelles ont des structures differentes — adapter les checks

## Related
- [[_system/MOC-patterns]]
- [[website/_MOC]]
- [[remember/2026-03-21]]
- [[website/audits/2026-03-21-seo-geo-audit]]
- [[website/bugs/2026-03-21-contenu-duplique-geo-secteur]]
- [[website/sessions/2026-03-21]]
- [[brantham/sessions/2026-03-21-scan]]
- [[brantham/bugs/2026-03-06-agent-auth-401]]
