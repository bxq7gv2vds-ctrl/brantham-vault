# Domain Docs

Comment les skills d'engineering doivent consommer la documentation domaine de Paul lors de l'exploration d'un repo / projet.

## Layout : multi-context

Le vault Obsidian unifié couvre plusieurs projets. Donc layout **multi-context**, indexé par `vault/_system/MOC-master.md`.

```
/Users/paul/vault/
├── _system/
│   ├── MOC-master.md           ← root index (équivalent CONTEXT-MAP.md)
│   ├── MOC-decisions.md
│   ├── MOC-bugs.md
│   ├── MOC-patterns.md
│   ├── adr/                    ← ADRs system-wide (croisent plusieurs projets)
│   └── agents/                 ← config skills (ce dossier)
├── brantham/
│   ├── _MOC.md                 ← context Brantham (équivalent CONTEXT.md)
│   ├── context/                ← realite-business, process, sow
│   └── ...
├── website/
│   ├── _MOC.md
│   └── ...
└── issues/
    └── <feature-slug>/
```

## Avant d'explorer un projet, lire

1. **`/Users/paul/vault/_system/MOC-master.md`** — vue d'ensemble multi-projet
2. **Le `_MOC.md` du projet courant** — détecté depuis le working directory (mapping dans `/Users/paul/CLAUDE.md`)
3. **`vault/_system/adr/`** — ADRs system-wide pertinentes pour le sujet
4. **`vault/<projet>/context/`** ou équivalent — contexte spécifique projet

Si un de ces fichiers n'existe pas, **continuer silencieusement**. Ne pas signaler l'absence ; ne pas proposer de créer en amont. Le skill `/grill-with-docs` les crée paresseusement quand des termes / décisions sont effectivement résolus.

## Mapping working directory → projet vault

| Working dir contient                   | Projet vault           |
| -------------------------------------- | ---------------------- |
| `brantham`, `internal-tool`, `cockpit-web`, `brantham-pipeline` | `vault/brantham/`      |
| `zura-inspired`, `seomachine`          | `vault/website/`       |
| `polymarket-hedge`                     | `vault/brantham/polymarket/` |
| `writing-vault`                        | `/Users/paul/writing-vault/` (vault séparé) |
| Autre                                  | `vault/founder/`       |

## Glossaire

Chaque `_MOC.md` projet définit le vocabulaire du domaine (ex : "deal", "AJ", "repreneur", "teaser" pour Brantham). Quand un output nomme un concept, utiliser le terme tel que défini dans le MOC. Ne pas dériver vers des synonymes.

Si le concept n'est pas encore dans le glossaire : signal — soit invention de langage que le projet n'utilise pas (reconsidérer), soit vrai gap (noter pour `/grill-with-docs`).

## Conflits avec ADR

Si un output contredit une ADR existante de `vault/_system/adr/`, le surfacer explicitement plutôt que d'override silencieusement :

> _Contredit ADR-0007 (event-sourced orders) — mais vaut le coup de rouvrir parce que…_

## Where to write new ADRs

`vault/_system/adr/<NNNN>-<slug>.md` avec frontmatter standard. Mettre à jour `vault/_system/MOC-master.md` avec la ligne d'index.

## Related

- [[_system/MOC-master]]
- [[_system/agents/issue-tracker]]
- [[_system/agents/triage-labels]]
