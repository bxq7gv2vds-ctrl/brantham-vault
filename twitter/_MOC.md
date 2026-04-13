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

## Architecture en 5 couches

```
LAYER 1 — DATA COLLECTION (permanent)
  feed_monitor.py       → scan feed + 16 comptes prioritaires toutes les 5 min
  vault/twitter/feed-learning/  → tweets retenus pour apprentissage

LAYER 2 — INTELLIGENCE (le cerveau)
  brain.py              → stratégie quotidienne (signaux feed + vault + trends)
  angle_engine.py       → 5 prismes worldview → angle le plus tranchant
  persona.md            → worldview de Paul (auto-mis à jour)
  persona_corpus.json   → corpus RAG (drafts + replies postées)
  vault/twitter/persona/ → hot-topics persistés

LAYER 3 — GÉNÉRATION
  orchestrator.py       → 4 tweets originaux/jour via RAG + buzz patterns
  reply_bot.py          → 3 tiers : DEBUNK (2-3/j) / INSIGHT (10-15/j) / REACT (25-35/j)
  thread_generator.py   → 1-2 threads bangers/semaine (cible >500 bookmarks)

LAYER 4 — APPRENTISSAGE
  engagement_tracker.py → lit métriques (likes/RT/BM) → feedback corpus
  persona_builder.py    → rebuild persona toutes les 2h (via feed_monitor)
  vault_writer.py       → persiste TOUT dans Obsidian avec wikilinks

LAYER 5 — DISTRIBUTION
  clix                  → poster sur Twitter/X (cookie auth, zero API key)
  telegram_bot.py       → deals + weekly recap sur Telegram
```

## Fichiers Content Engine
- `~/content-engine/brain.py` — orchestrateur central
- `~/content-engine/angle_engine.py` — 5 prismes worldview
- `~/content-engine/thread_generator.py` — threads hebdo
- `~/content-engine/engagement_tracker.py` — métriques + feedback
- `~/content-engine/vault_writer.py` — persistance Obsidian
- `~/content-engine/reply_bot.py` — 50 replies/jour
- `~/content-engine/feed_monitor.py` — scan permanent
- `~/content-engine/persona_builder.py` — learning loop
- `~/content-engine/persona.md` — worldview de Paul
- `~/content-engine/run.sh` — point d'entrée CLI

## Commandes clés
```bash
bash run.sh --brain         # plan du jour (dry run)
bash run.sh --brain-run     # exécution complète
bash run.sh --brain-status  # état + performances
bash run.sh --full          # brain + replies + tracking
bash run.sh --reply         # scan feed + génère replies
bash run.sh --thread        # génère un thread
bash run.sh --track-daily   # rapport engagement quotidien
bash run.sh --angles "sujet" # teste les 5 angles sur un sujet
bash run.sh --learn         # rebuild persona complet
```

## Les 5 Prismes Worldview (angle_engine)
1. **réaliste_terrain** — Ce que les experts ratent parce qu'ils ne sont pas dans le terrain
2. **marché_broken** — Le marché est broken — mécanisme exact, info asymétrique
3. **ia_opérationnel** — L'IA n'est pas dans les PowerPoint, elle est dans mon pipeline
4. **france_inefficiente** — La France a peur de ce qu'elle ne comprend pas
5. **solo_agilité** — Le solo > le collectif quand les outils sont bons

## Vault Twitter
- `twitter/feed-learning/` — tweets retenus du feed (par date)
- `twitter/drafts/` — tweets générés (par date)
- `twitter/replies/` — replies générées et postées
- `twitter/threads/` — threads bangers
- `twitter/engagement/` — métriques post-posting
- `twitter/persona/` — hot-topics + persona live
- `twitter/weekly/` — recaps hebdo engagement

## Configuration launchd (macOS)
- `com.paul.content-engine.plist` → 8h05 CET (orchestrateur daily)
- `com.paul.content-engine-reply.plist` → toutes les 15 min 8h-23h

## Related
- [[_system/MOC-master]]
- [[twitter/agent/voice-card]]
- [[twitter/agent/accounts/tier-list]]
- [[_system/MOC-patterns]]
