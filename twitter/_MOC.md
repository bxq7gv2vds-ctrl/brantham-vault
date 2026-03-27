---
type: moc
project: twitter
updated: 2026-03-26
---

# Twitter Growth Agent — Map of Content

## Mission
Agent autonome (Claude Cowork) qui fait percer le compte Twitter de Paul dans la niche AI/agents/LLM/automation/self-improvement. Browse Twitter via Playwright (computer use), apprend qui est Paul, produit du contenu indistinguable d'un humain.

## Statut
- **Phase** : setup (prompt pret, lancement imminent)
- **Compte Twitter** : a configurer
- **Mode** : Claude Cowork + Playwright (browser natif, zero API)

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
