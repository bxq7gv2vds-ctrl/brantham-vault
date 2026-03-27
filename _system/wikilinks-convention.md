---
name: Obsidian Wikilinks Convention
description: Mandatory linking rules for all vault files to build knowledge graph
type: reference
---

# Obsidian Wikilinks Convention

**Every file in the vault MUST contain `[[wikilinks]]`** to build a compounding knowledge graph.

## Rules (MANDATORY)

### 1. Every file has `## Related` section (end of file)

```markdown
## Related

- [[_system/MOC-X]]  # Parent MOC
- [[project/_MOC]]   # Project MOC
- [optional cross-links]
```

### 2. Backlinks by type

| Type | Minimum Backlinks | Example |
|------|-----------------|---------|
| **decision** | `[[_system/MOC-decisions]]`<br>`[[brantham/_MOC]]` | Links to strategy, assumptions |
| **bug** | `[[_system/MOC-bugs]]`<br>`[[project/_MOC]]` | Links to patterns that fixed it |
| **pattern** | `[[_system/MOC-patterns]]`<br>`[[project/_MOC]]` | Links to bugs it resolves, decisions |
| **session** | `[[project/_MOC]]` | Links to decisions/bugs/patterns made same day |
| **assumption** | `[[_system/MOC-assumptions]]`<br>`[[project/_MOC]]` | Links to decisions validating/invalidating it |

### 3. Cross-day linking (temporal)

Files from **same date** link to each other.

### 4. Causal linking (semantic)

- **Bug → Pattern**: "This pattern was created to fix [[brantham/bugs/YYYY-MM-DD-X]]"
- **Decision ← Assumption**: "Validates assumption [[founder/assumptions/market-size]]"

## Auto-Linking Tool

**Location**: `/Users/paul/vault/_system/vault-linker.py`

```bash
# Audit vault
python3 vault-linker.py

# Apply auto-linking
python3 vault-linker.py fix
```

---

**Updated**: 2026-03-27

## Related

- [[_system/MOC-master]]
- [[brantham/_MOC]]
