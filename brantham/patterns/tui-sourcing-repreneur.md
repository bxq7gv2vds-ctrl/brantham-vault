---
name: TUI Sourcing Repreneur
type: pattern
project: brantham
date: 2026-03-30
---

# Pattern — TUI Sourcing Repreneur

Pipeline terminal complet pour trouver des repreneurs potentiels à partir d'une annonce AJ et enrichir leurs contacts dirigeants.

## Architecture

```
Annonce (texte ou URL)
    → Claude Haiku → NAF codes + secteur
    → API Entreprises (recherche-entreprises.api.gouv.fr) → 15-30 sociétés/NAF
    → Fallback texte si <10 résultats
    → enrich_one() x32 (parallel, 4 workers) → Pappers SIREN → dirigeants + finances
    → [sélection manuelle dans ListView]
    → deep_enrich() → multi-source parallèle
    → Claude Opus → fiche M&A complète + accroche email
```

## Stack Textual

```python
# Widgets clés
ListView + ListItem + Label  # sélection fiable (vs DataTable)
Input(id="num-input")        # sélection par numéro
RichLog                      # logs temps réel
Static(id="detail")          # panel droit scrollable
Button                       # actions

# Règles UX
# - ListView.Highlighted → affiche fiche basique
# - ListView.Selected (Enter/clic) → affiche fiche (PAS d'auto-enrich)
# - Champ # + Enter → sélectionne + lance deep enrich
# - Bouton ENRICHIR OPUS → lance deep enrich
# - NE JAMAIS binder "enter" globalement si ListView/DataTable présent
```

## Sources de données dirigeants (ordre de fiabilité)

```python
# 1. Pappers (SIREN exact — toujours en premier)
pappers.lookup(siren=siren)   # exact, fiable
pappers.lookup(nom=nom)       # fallback si 0 dirigeants

# 2. Données web (parallèle)
ThreadPoolExecutor(max_workers=4):
    scrape_site()             # 12 pages /contact /equipe /direction...
    _scrape_societecom(siren) # societe.com → tel + email
    _scrape_verifcom(siren)   # verif.com → tel + email
    _crtsh_emails(domain)     # crt.sh → emails dans certs SSL

# 3. Vérification email (séquentiel sur top candidats)
_holehe_check(email)          # 10s, vérifie 120+ services
_smtp_verify(email)           # bloqué entreprise → souvent None
_hunter_find(prenom, nom, domain)  # optionnel, HUNTER_API_KEY

# 4. Scoring email
site > crt.sh > hunter > holehe > smtp✓ > pattern
# SMTP mort (550/553) → éliminer
```

## Scoring email (code)

```python
def escore(em):
    s = 0
    if em in matched:                             s += 100  # trouvé sur site
    if email_sources_global.get(em) == "crt.sh": s += 90   # cert SSL
    if em == hunter_email:                        s += 80   # Hunter.io
    if holehe_res.get(em):                        s += 70   # holehe confirm
    if smtp_res.get(em) is True:                  s += 60   # SMTP ok
    if smtp_res.get(em) is False:                 s -= 999  # SMTP mort
    return s
```

## Bugs connus / pièges

- **Pappers retourne dict truthy même vide** → ne pas faire `lookup() or lookup()`, vérifier `len(dirigeants) > 0`
- **NAF format** : API exige `25.41Z` (avec point). Fonction `_fmt_naf()` gère la conversion.
- **holehe** : parser la sortie brute, filtrer les lignes "Email used," et "twitter" header
- **crt.sh timeout** : parfois >15s, wrapper dans try/except avec timeout=15
- **Threading Pappers** : cloudscraper non thread-safe → `_pappers_lock = threading.Lock()`

## Commande

```bash
cd ~/Downloads/brantham-pipeline && python3 bp_tui.py
# Ctrl+S = lancer recherche
# Flèches = naviguer
# # + Enter = sélectionner par numéro + enrichir
# p = export CSV
```

## Installation dépendances

```bash
pip3 install holehe dnspython aiohttp --break-system-packages
# optionnel : export HUNTER_API_KEY=xxx
```

## Related

- [[brantham/_MOC]]
- [[brantham/sessions/2026-03-30-bp-tui-sourcing]]
- [[_system/MOC-patterns]]
