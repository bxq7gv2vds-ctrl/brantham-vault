---
type: reference
date: 2026-03-27
tags: [vault, obsidian, wikilinks, convention]
---

# Convention Wikilinks — Vault Obsidian

## Principe

Chaque fichier du vault DOIT etre connecte au graph Obsidian via des `[[wikilinks]]`. Un fichier isole = un fichier invisible dans le graph = de la connaissance perdue.

## Format

```markdown
[[path/depuis/racine/vault/sans-extension]]
[[path/vers/fichier|Alias affiche]]
```

Exemples :
- `[[brantham/patterns/teaser-patterns]]`
- `[[_system/MOC-bugs]]`
- `[[founder/decisions/2026-03-18-mirofish-distilled-architecture|Decision MiroFish]]`

## Section Related (obligatoire)

Chaque fichier vault se termine par :

```markdown
## Related
- [[lien-1]]
- [[lien-2]]
- ...
```

## Regles de linking par type

### Bug-fix
| Lien | Obligatoire |
|------|------------|
| `[[_system/MOC-bugs]]` | Oui |
| `[[projet/_MOC]]` | Oui |
| `[[projet/sessions/YYYY-MM-DD]]` | Oui (session ou le bug a ete fixe) |
| `[[projet/patterns/nom]]` | Si un pattern en decoule |

### Decision
| Lien | Obligatoire |
|------|------------|
| `[[_system/MOC-decisions]]` | Oui |
| `[[projet/_MOC]]` | Oui |
| `[[founder/strategy/current-strategy]]` | Si impacte la strategie |
| `[[founder/assumptions/nom]]` | Si basee sur une assumption |
| `[[projet/sessions/YYYY-MM-DD]]` | Oui (session de la decision) |

### Pattern
| Lien | Obligatoire |
|------|------------|
| `[[_system/MOC-patterns]]` | Oui |
| `[[projet/_MOC]]` | Oui |
| `[[projet/bugs/YYYY-MM-DD-nom]]` | Si decouvert via un bug |
| `[[projet/sessions/YYYY-MM-DD]]` | Oui (session de decouverte) |

### Session
| Lien | Obligatoire |
|------|------------|
| `[[projet/_MOC]]` | Oui |
| `[[projet/bugs/...]]` | Tous les bugs fixes ce jour |
| `[[projet/patterns/...]]` | Tous les patterns decouverts ce jour |
| `[[founder/decisions/...]]` | Toutes les decisions du jour |

### Assumption
| Lien | Obligatoire |
|------|------------|
| `[[_system/MOC-assumptions]]` | Oui |
| `[[founder/decisions/...]]` | Decisions basees sur cette assumption |
| `[[founder/strategy/current-strategy]]` | Si impacte la strategie |
| `[[founder/customers/...]]` | Retours clients lies |

### Customer
| Lien | Obligatoire |
|------|------------|
| `[[founder/assumptions/...]]` | Assumptions validees/invalidees |
| `[[brantham/deals/active/...]]` | Deal concerne |
| `[[founder/decisions/...]]` | Decisions influencees |

### Knowledge (brantham/knowledge/)
| Lien | Obligatoire |
|------|------------|
| `[[brantham/_MOC]]` | Oui |
| `[[brantham/knowledge/_knowledge-map]]` | Oui |
| Fichiers knowledge lies | Cross-ref entre articles connexes |

## Inline links

Dans le corps du texte, utiliser des wikilinks quand on mentionne un concept qui a un fichier vault :

```markdown
Le pattern de [[brantham/patterns/teaser-patterns|teaser HTML/PDF]] a ete applique
suite au bug [[brantham/bugs/2026-03-16-probability-matrix-oscillation|oscillation matrice]].
```

## Anti-patterns

- Fichier sans aucun `[[lien]]` = interdit
- Lien mort (fichier cible inexistant) = verifier avant de linker
- Lien generique `[[decision-link]]` placeholder = remplacer par le vrai path
- Duplication du lien dans Related ET dans le corps = ok (Obsidian deduplique dans le graph)

## Maintenance

Script de batch : `vault/_system/scripts/batch-wikilinks.py`
- Scanne tous les fichiers, ajoute `## Related` avec liens intelligents
- A relancer periodiquement : `python3 vault/_system/scripts/batch-wikilinks.py`
- Suivi par `qmd embed` pour re-indexer la recherche semantique

## Related
- [[_system/MOC-master]]
- [[brantham/_MOC]]
- [[website/_MOC]]
- [[founder/decisions/2026-03-27-vault-wikilinks-overhaul]]
