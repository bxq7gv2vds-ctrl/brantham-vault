---
type: protocol
project: brantham
status: active
date: 2026-05-06
tags: [protocol, vault, claude-instructions]
---

# Protocole — Tout Brantham dans le vault

> Décision Paul 2026-05-06 : tout le contenu Brantham vit **dans le vault**, pas dans `~/.claude/.../memory/`.

## Règle

**Aucun nouveau contenu Brantham n'est créé en memory utilisateur.** Tout va dans `vault/brantham/` aux emplacements appropriés.

## Où ça va

| Type de contenu | Location vault |
|---|---|
| Playbooks (call, outreach, etc.) | `vault/brantham/playbooks/` |
| Protocoles Claude | `vault/brantham/protocols/` |
| Living business profile | `vault/brantham/context/business-profile/_PROFILE.md` |
| Voice notes | `vault/brantham/context/voice-notes/` |
| Decisions | `vault/founder/decisions/` (linkées depuis `vault/brantham/_MOC.md`) |
| Assumptions | `vault/founder/assumptions/` |
| Customers / retours repreneurs | `vault/founder/customers/` |
| Patterns | `vault/brantham/patterns/` |
| Bugs / ratés | `vault/brantham/bugs/` |
| Sessions | `vault/brantham/sessions/` |
| Deals | `vault/brantham/deals/active/<slug>/` |
| Templates corporate | `vault/_system/templates/` |

## Memory utilisateur — usage minimal

`MEMORY.md` ne contient que **des pointeurs 1-ligne** vers les locations vault. Les vrais documents vivent dans le vault.

Format des pointeurs en memory :
```
- [Titre court](file.md) — pointer to `vault/brantham/path/file.md`
```

Le fichier `.md` en memory doit être très court (titre + 1 phrase) et pointer vers la vraie source dans le vault.

## Pourquoi

1. **Single source of truth** : pas de duplication, pas de drift entre memory et vault.
2. **Wikilinks Obsidian** : tout le graphe de connaissances Brantham vit dans Obsidian.
3. **QMD search** : tout est indexé via la collection `vault`.
4. **Lisible humainement** : Paul peut tout consulter dans Obsidian sans aller fouiller le dossier `.claude`.
5. **Versionnable** : le vault peut être git-versionné (la memory non).

## Exception

Memory utilisateur reste utilisée pour :
- Profile utilisateur (préférences, contexte personnel non-Brantham).
- Feedback global (ex: pas de tirets cadratins, accents obligatoires).
- Pointeurs vers locations vault.

## Related
- [[brantham/_MOC]]
- [[brantham/protocols/_MOC]]
- [[brantham/protocols/voice-notes-continues]]
