---
type: reorg-plan
status: proposed
updated: 2026-06-03
---

# Réorganisation Vault Brantham

## Diagnostic

Le Vault fonctionne, mais il est trop plat au niveau racine et trop profond dans certains sous-systèmes.

Problèmes observés:

- Trop de dossiers racine avec des responsabilités proches: `pipeline`, `data-pipeline`, `agents`, `cowork-*`, `pappers`, `dashboard`, `cockpit`.
- Gros blocs historiques très lourds: `linkedin` (~29M), `deals` (~17M), `tc-paris-extraction` (~8.6M).
- Dossiers vides ou quasi vides: `_system`, `acheteurs`, `linkedin-factory`, `soren.md` vide.
- Notes techniques importantes dispersées entre `architecture.md`, `INFRA-COMPLETE.md`, `context/`, `patterns/`, `sessions/`.

## Structure cible légère

```text
brantham/
  _MOC.md
  operating-system/
    _MOC.md
    infra/
    protocols/
    reorg/
  deals/
    active/
    identified/
    closed/
    templates/
  knowledge/
  patterns/
  templates/
  sessions/
  archive/
```

## Règles

- Ne pas créer un dossier racine si un dossier existant couvre déjà le besoin.
- Les deals vivants restent dans `deals/active`.
- Les sorties agent doivent être stockées dans le deal, pas dans `cowork-outputs`, quand elles concernent un deal précis.
- `cowork-outputs` doit devenir une zone temporaire, pas une base de connaissance.
- Les gros corpus (`linkedin`, `tc-paris-extraction`) doivent être gardés mais isolés comme datasets/archives.

## Actions faites le 2026-06-03

- Ajout de `operating-system/_MOC.md`.
- Ajout de `operating-system/infra/osint-distressed-agent.md`.
- Ajout de `operating-system/obsidian-write-protocol.md`.
- Copie du dossier Gesler dans `deals/active/gesler/repreneurs-2026-06-03.md`.
- Mise à jour de `_MOC.md`.
- Création du skill local `vault-obsidian`.

## Déplacements candidats à valider

| Actuel | Proposition | Raison |
|---|---|---|
| `INFRA-COMPLETE.md` | `operating-system/infra/infra-complete.md` | Infra, pas racine |
| `architecture.md` | `operating-system/infra/architecture.md` | Architecture système |
| `COWORK-PROMPT.md` | `operating-system/protocols/cowork-prompt.md` | Protocole |
| `pipeline/` | fusionner avec `data-pipeline/` ou `operating-system/infra/` | Responsabilités proches |
| `cowork-prompts/` | `operating-system/protocols/cowork-prompts/` | Protocole agent |
| `cowork-outputs/` | `archive/cowork-outputs/` sauf deal-specific | Sorties historiques |
| `dashboard/` + `cockpit/` | `operating-system/infra/cockpit/` | Produit interne |
| `pappers/` | `operating-system/infra/pappers/` ou `knowledge/acteurs/pappers/` | À décider selon usage |
| `linkedin/` | `archive/linkedin-content/` | Gros corpus marketing |
| `tc-paris-extraction/` | `archive/datasets/tc-paris-extraction/` | Dataset lourd |

## À ne pas faire sans validation

- Suppression de dossiers.
- Déplacement massif de `linkedin`, `deals`, `knowledge` ou `tc-paris-extraction`.
- Renommage de dossiers qui casseraient les backlinks Obsidian sans migration de liens.
## Related
