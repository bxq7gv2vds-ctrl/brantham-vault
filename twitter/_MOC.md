---
type: moc
project: twitter
updated: 2026-04-13
---

# Twitter Content Engine — Map of Content

## Mission
Infrastructure autonome qui apprend en continu pour construire le personal brand de Paul Roulleau sur CT FR.
Angle unique : **Le Réaliste IA** — builder avec données terrain réelles (3 918 PME scrapées, agents en prod, deals réels).

## Statut
- **Phase** : production — infrastructure complète déployée
- **Objectif** : 50 tweets/jour (4 originaux + 46 replies/QTs)
- **Apprentissage** : boucle persona continue (feed → vault → persona → génération → feedback)

## Agent Config
- [[twitter/agent/COWORK-PROMPT]] — Prompt principal (instructions completes)
- [[twitter/agent/paul-profile]] — Profil de Paul (evolue avec le temps)
- [[twitter/agent/voice-card]] — Persona / ton / style d'ecriture
- [[twitter/agent/blacklist]] — Mots et patterns AI interdits

## Comptes & Niche
- [[twitter/agent/accounts/tier-list]] — Comptes a suivre et analyser

## Directories
- `twitter/agent/niche/` — Learnings sur la niche (topics, trends)
- `twitter/agent/accounts/` — Analyses de comptes individuels
- `twitter/agent/patterns/` — Ce qui marche (hooks, formats, timing)
- `twitter/agent/drafts/` — Brouillons de tweets
- `twitter/agent/metrics/` — Performance tracking + rapports hebdo
- `twitter/digests/` — Digests quotidiens du feed

## Architecture
```
Paul (Claude Code) <--claude-peers--> Twitter Agent (Cowork)
                                        |
                                        Playwright → Browser → x.com
                                        Read/Write → vault/twitter/
                                        QMD → recherche vault
```

## Strategie cle
- 70% replies strategiques / 30% contenu original
- Burstiness haute (anti-AI detection)
- Few-shot des top comptes pour cloner les patterns
- Learning loop : chaque edit/rejet de Paul = signal
- Phase observation 3 jours avant de poster
## Related
- [[_system/MOC-master]]
- [[twitter/agent/COWORK-PROMPT]]
- [[twitter/agent/voice-card]]
- [[twitter/agent/accounts/tier-list]]
