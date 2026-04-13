---
name: Session TUI Sourcing Brantham
type: session
date: 2026-03-30
project: brantham
duration: "4h"
---

# Session — 2026-03-30 — TUI Sourcing Repreneur

**Date**: 2026-03-30
**Focus**: Construction d'un TUI terminal complet pour sourcer et enrichir les repreneurs potentiels

## What We Did

- Réécriture complète de `bp_tui.py` — TUI Textual dédié au sourcing repreneur
- Remplacement DataTable (sélection peu fiable) par ListView (clic = select immédiat)
- Ajout champ `#` pour sélectionner un repreneur par numéro directement
- Fix UX : clic = affiche fiche, pas d'auto-enrich — enrich explicite seulement
- Intégration Claude Opus pour analyse M&A + accroche cold email par repreneur
- Construction pipeline de recherche dirigeant multi-sources

### Pipeline de recherche dirigeant

Sources intégrées en parallèle (ThreadPoolExecutor) :

| Source | Données | Gratuit |
|--------|---------|---------|
| Pappers (SIREN lookup) | Dirigeants officiels, finances 5 ans | ✅ |
| Societe.com (scraping) | Tel, email supplémentaire | ✅ |
| Verif.com (scraping) | Tel, email complémentaire | ✅ |
| Site web (12 pages) | Emails directs, tels | ✅ |
| crt.sh | Emails dans certificats SSL | ✅ |
| holehe (CLI, 120+ services) | Vérifie si email est réel | ✅ |
| SMTP verify (dnspython) | MX check — bloqué enterprise | ✅ |
| Hunter.io (HUNTER_API_KEY) | Email finder précis | 🔑 optionnel |
| RNE INPI API | Dirigeants registre national | ✅ |
| Pattern generation | 6 variantes prenom.nom@domain | ✅ |
| Google search URLs | Recherche manuelle pré-construite | ✅ liens |

### Scoring email (confiance décroissante)
1. Trouvé sur site (100 pts)
2. Trouvé sur crt.sh (90 pts)
3. Hunter.io (80 pts)
4. Holehe confirme email réel (70 pts)
5. SMTP verify (60 pts)
6. Pattern uniquement (0 pts)

Les emails SMTP-morts (code 550/553) sont éliminés.

### Bugs fixés
- Pappers `lookup(siren=X)` retourne dict truthy même à 0 dirigeants → fallback `lookup(nom=X)` conditionnel
- NAF format `25.41Z` (avec point obligatoire) sinon API retourne 0 résultats
- Threading race condition Pappers → `_pappers_lock`
- holehe bin path → `shutil.which("holehe")` + fallback `/opt/homebrew/bin/holehe`

## Decisions Made

- [[brantham/patterns/tui-sourcing-repreneur]] — pattern pour le TUI
- Choix ListView vs DataTable : ListView plus fiable pour la sélection souris + clavier

## Key Learnings

- **Pappers SIREN first** : toujours chercher par SIREN (exact), fallback nom seulement si 0 dirigeants. Le lookup nom trouve une société homonyme ou filiale.
- **SMTP enterprise bloqué** : 99% des entreprises françaises filtrent les SMTP checks. Inutile comme source principale.
- **holehe** (10s/email) : outil OSINT puissant, confirme qu'un email est utilisé sur 120+ services. Proof-of-life pour un email de dirigeant.
- **crt.sh** : source souvent oubliée — les certificats SSL contiennent parfois des emails admin/contact directs.
- **ListView vs DataTable** : dans Textual, `DataTable.RowSelected` ne fire pas toujours sur clic souris. `ListView.Selected` est fiable dans les 2 cas.
- **Binding("enter") global** écrase la gestion native Enter du DataTable/ListView — ne jamais binder Enter globalement si la liste doit capturer Enter.

## Stack installé

```bash
pip3 install holehe dnspython aiohttp --break-system-packages
# holehe : 120+ services email verification
# dnspython : MX record lookup pour SMTP verify
```

## Fichier principal

`/Users/paul/Downloads/brantham-pipeline/bp_tui.py`

## Next Steps

- [ ] Tester le TUI end-to-end sur une vraie annonce AJ
- [ ] Vérifier que crt.sh retourne des emails (timeout parfois)
- [ ] Ajouter Hunter.io key si résultats insuffisants (export HUNTER_API_KEY=xxx)
- [ ] Exporter CSV après deep enrich Opus pour outreach Soren
- [ ] Tester sur 5 repreneurs réels → valider qualité emails trouvés

## Related

- [[brantham/_MOC]]
- [[brantham/patterns/tui-sourcing-repreneur]]
- [[_system/MOC-patterns]]
