---
type: pattern
created: 2026-04-27
tags: [html, refactoring, python, regex]
---

# HTML mass corrections — safe replacement pattern

Pattern réutilisable pour appliquer des corrections globales (orthographe, casse, ponctuation) sur un grand corpus HTML statique sans casser URLs, IDs, attributs, scripts.

## Contexte d'origine
Site `branthampartners.fr` (141 pages HTML) — phase A/B/E de l'audit orthographe-cohérence du 2026-04-27. Voir [[website/sessions/2026-04-27-audit-coherence-orthographe-deploy]].

## Problème
Un `sed -i 's/foo/bar/g' *.html` global casse :
- les URLs (`/foo-bar.html` → `/bar-bar.html`)
- les IDs (`id="foo"` → `id="bar"`) sans changer les `href="#foo"`
- les attributs (`name="..."`, `aria-label="..."`)
- les contenus `<script>` (JS, JSON-LD)
- les contenus `<style>`

## Solution : masking + state machine

### Étape 1 — Masquer les motifs à préserver
```python
URL_PATTERNS = re.compile(
    r'(href\s*=\s*["\'][^"\']*["\']'
    r'|src\s*=\s*["\'][^"\']*["\']'
    r'|id\s*=\s*["\'][^"\']*["\']'
    r'|name\s*=\s*["\'][^"\']*["\']'
    r'|content\s*=\s*["\'][^"\']*["\']'
    r'|aria-label\s*=\s*["\'][^"\']*["\']'
    r'|/[a-z0-9\-_]+\.html'
    r'|#[a-z0-9\-_]+'
    r'|"url"\s*:\s*"[^"]*"'
    r'|"@id"\s*:\s*"[^"]*"'
    r'|"item"\s*:\s*"[^"]*"'
    r')',
    re.IGNORECASE,
)

def protect_then_apply(line, replacements):
    masks = []
    def mask(m):
        masks.append(m.group(0))
        return f"\x00{len(masks)-1}\x00"
    masked = URL_PATTERNS.sub(mask, line)
    for ascii_w, accented_w in replacements:
        masked = re.compile(r'\b' + re.escape(ascii_w) + r'\b').sub(accented_w, masked)
    return re.sub(r'\x00(\d+)\x00', lambda m: masks[int(m.group(1))], masked)
```

### Étape 2 — State machine pour scripts/styles
```python
def process(path):
    in_script = in_style = False
    new_lines = []
    for line in path.read_text().splitlines(keepends=True):
        lower = line.lower()
        if '<script' in lower and 'application/ld+json' not in lower:
            in_script = True
        if '<style' in lower:
            in_style = True
        if in_script or in_style:
            new_lines.append(line)
            if '</script' in lower: in_script = False
            if '</style' in lower: in_style = False
            continue
        new_lines.append(protect_then_apply(line, replacements))
    path.write_text(''.join(new_lines))
```

### Étape 3 — Pour les insécables FR (text nodes only)
```python
TAG_RE = re.compile(r'<[^>]+>')
PUNCT_RE = re.compile(r' ([:;!?])(?=\s|<|$|\))')

def process_line(line):
    """Walk text/tag segments, modify text only."""
    result, pos = [], 0
    for m in TAG_RE.finditer(line):
        result.append(PUNCT_RE.sub(r'&nbsp;\1', line[pos:m.start()]))
        result.append(m.group(0))
        pos = m.end()
    result.append(PUNCT_RE.sub(r'&nbsp;\1', line[pos:]))
    return ''.join(result)
```

## Pièges critiques

### 1. Faux positifs verbe/participe-passé en français
Tout verbe en `-e` (présent indicatif) devient un faux participe passé si on ajoute `é` :
- `propose` (verbe) ≠ `proposé` (pp)
- `décide` ≠ `décidé`
- `intègre` ≠ `intégré`
- `identifie` ≠ `identifié`
- `vérifie` ≠ `vérifié`
- etc.

**Règle** : exclure de toute liste auto tout mot finissant en `-e`/`-es` qui est aussi une forme verbale du présent. Garder seulement substantifs, adjectifs, infinitifs en `-er`, et participes passés féminins/pluriels (`-ée`, `-ées`, `-és`).

### 2. Acronymes ≠ noms propres
"AJ" peut être :
- l'acronyme "Administrateur Judiciaire"
- une raison sociale ("AJ Partenaires Marseille")
- un mot anglais
→ **Pas automatisable**, jugement humain requis.

### 3. Best practices web pour IDs
`id="creancier-chirographaire"` (ASCII) est CORRECT et préférable à `id="créancier-chirographaire"`. Un audit qui suggère d'accentuer les IDs est souvent à côté. Vérifier que les `href="#xxx"` correspondent au `id="xxx"` (les deux ASCII = OK).

### 4. Norme typo FR pour institutions
"**Tribunal de commerce**" (T majuscule, c minuscule). Pas "Tribunal de Commerce" (calque anglo-saxon).

## Workflow recommandé

1. **Backup tar.gz** avant tout (les sites statiques n'ont souvent pas de git).
2. **Test sur 1 fichier** : copier l'original, exécuter, differ pour valider.
3. **Itérer la liste** de remplacements en mode small-batch puis full-batch.
4. **Smoke test HTTP** : `curl -s -o /dev/null -w "%{http_code}" http://localhost:PORT/page.html` sur 5-10 pages clés.
5. **Grep résiduel** : vérifier que les motifs cibles ont disparu, et que les motifs préservés (URLs, IDs) sont intacts.
6. **Deploy** : `vercel deploy --prod --yes` (ou équivalent), puis re-grep en prod via `curl`.

## Stats du run d'origine (2026-04-27)
| Phase | Volume |
|---|---|
| Orthographe | 356 lignes / 70 fichiers |
| Casse Tribunal | 595 lignes / 97 fichiers |
| Insécables | 5 933 segments / 141 fichiers |
| Faux positifs détectés | 1 (rollback complet phase A v1) |
| Casses détectées et rollback | 1 (phase D acronyme AJ) |
| Deploy Vercel | 11.1 MB, 19s |

## Related
- [[_system/MOC-patterns]]
- [[website/_MOC]]
- [[website/sessions/2026-04-27-audit-coherence-orthographe-deploy]]
