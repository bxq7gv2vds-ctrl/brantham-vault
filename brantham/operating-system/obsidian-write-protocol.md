---
type: protocol
status: active
updated: 2026-06-03
---

# Protocole écriture Vault + Obsidian

## Règle

Tout fichier créé ou modifié dans `/Users/paul/vault/brantham` doit être ouvert immédiatement dans Obsidian.

Skill local créé:

```text
/Users/paul/.codex/skills/vault-obsidian
```

Commande:

```bash
/Users/paul/.codex/skills/vault-obsidian/scripts/open_in_obsidian.sh /Users/paul/vault/brantham/path/to/file.md
```

## Issue détectée

Le handler `obsidian://open?path=...` n’est pas enregistré correctement.

`/Applications/Obsidian.app` existe, mais macOS retourne:

```text
kLSNoExecutableErr: The executable is missing
```

Donc Obsidian semble présent mais cassé ou incomplet. À corriger côté machine:

1. Réinstaller Obsidian.
2. Ouvrir Obsidian manuellement une fois.
3. Vérifier:

```bash
open "obsidian://open?path=/Users/paul/vault/brantham/_MOC.md"
```

## Organisation cible

Limiter les sous-dossiers profonds. Les emplacements par défaut:

| Type | Emplacement |
|---|---|
| Deal actif | `deals/active/<deal>/` |
| Infra / protocoles / continuité | `operating-system/` |
| Knowledge evergreen | `knowledge/` |
| Patterns réutilisables | `patterns/` |
| Archives / sorties historiques | `sessions/` ou dossier archive dédié après validation |

## À éviter

- Créer de nouveaux dossiers racine sans nécessité durable.
- Écrire les dossiers Brantham dans `/Desktop/.../agent/output` sauf pour tests techniques.
- Déplacer ou supprimer en masse des notes existantes sans validation utilisateur.
## Related
## Related
## Related
## Related
