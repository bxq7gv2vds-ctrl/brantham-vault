---
date: 2026-04-26
project: brantham
tags: [session, cockpit, supabase, hunters, tui, ux]
duration_h: ~6
---

# Session 2026-04-26 — Cockpit TUI Phase B+C : Supabase, Hunters, Todo Manager, UX

## Quoi
Suite de la session [[brantham/sessions/2026-04-26-cockpit-aj]] (Phase A — TUI triage AJ).
Refonte massive du cockpit pour passer de "tracker solo SQLite" à "plateforme collab Supabase + sourcing repreneurs + task manager".

## Livré

### 1. Scraper Mayday Mag v5 — extraction AJ réel
- **Avant** : 11 opps fourre-tout sous `source_aj="Maydaymag"`, DLDO 0%
- **Après** : 11 opps avec `source_aj` normalisé (STAR, AJ Associés, AJ UP, BCM, CBF, etc.), DLDO 100%, CA + effectif extraits
- **Cabinets nouveaux découverts** :
  - **STAR Administrateurs Judiciaires** (Annecy / Grenoble / Chambéry) — pas de dataroom propre, Mayday est la seule source
  - **AJ Associés** (Me Lebreton + Me Michel) — domaine introuvable, idem Mayday seul
- Module : `cockpit/scraper_aj.py:scrape_maydaymag` v5 + `MAYDAY_AJ_NORMALIZE` table

### 2. Cockpit DB abstraction SQLite ↔ Postgres
- `cockpit/db.py` détecte automatiquement `DATABASE_URL` env → Postgres via psycopg, sinon SQLite local
- **HybridRow custom** : mime `sqlite3.Row` (accès `row[0]` int + `row["col"]` str + `iter` sur values) — résout incompatibilités psycopg dict_row
- Connection persistante singleton (gain ~2.5× vs reconnexion à chaque query)
- Helpers `db.today_iso()` / `db.iso_offset(7)` remplacent `date('now')` SQLite-only

### 3. Migration Supabase
- Projet créé : `brantham-cockpit` sur Supabase, région **eu-west-1** (Ireland)
- DATABASE_URL pooler 6543 (Transaction mode)
- Script `cockpit/migrate.py` : 470 rows migrées (459 opps + 2 deals + 7 events + 2 deal_events)
- Idempotent : ON CONFLICT DO NOTHING sur PK TEXT
- Backup : SQLite local conservé

### 4. Pipeline deals + édition complète
- Schéma `deals` + `deal_events` (stage, assigned_to, fees_buyer/seller, deadline, next_action, notes, outcome)
- 9 stages : `qualification → mandat → sourcing → outreach → due_diligence → offre → closing → won / lost`
- Probabilités par stage (pour pondération pipeline value finance)
- **Modal EditDealModal** : édition complète tous champs (touche `e`), ctrl+s sauve
- Magic Form Levallois seedé (premier deal réel, stage `due_diligence`, deadline 21/05/2026)

### 5. TUI multi-onglets (5 vues)
- **Onglets** : Opps · Pipeline · Deals · Finance · À faire
- **Action bar cliquable** (Button widgets, hover/focus) — pas que des raccourcis clavier
- **Filtre AJ refait** : tableau `[ X ] / [   ]` claire (vs Checkbox illisible avant)
- **Onglet Finance** : KPIs revenus YTD/MTD, Pipeline brut + pondéré, win rate, table 12 mois (réalisé + forecast), breakdown par AJ source

### 6. Moteur de suggestions auto + Todo Manager
- Module `cockpit/suggestions.py` : 7 catégories de détection
  - Deadline urgente (J-3 / J-7 / passée)
  - Pipeline endormi (>10j sans update)
  - Documentation manquante (notes/next_action vides)
  - Opps shortlistées non décidées
  - Veille (scan vieux >2j)
  - Source AJ silencieuse (silent breakage)
- Module `cockpit/todos.py` + table `todos` :
  - Suggestions auto persistées (id stable hash)
  - Tâches custom manuelles (modal NewTodoModal, touche `+`)
  - Actions : ✓ done (espace), ✕ ignored (i), ⏰ snoozed 3j (z), @ assign, F filtre @paul/@soren
  - **State persistant** : done/ignored/snoozed survivent au redémarrage
- Touche `?` = HelpModal qui liste tous les raccourcis

### 7. Hunters repreneurs concurrents
- Stratégie SIMPLIFIÉE : **un seul angle = concurrents** (décision Paul, vs 4 angles initialement proposés)
- Source : `recherche-entreprises.api.gouv.fr` (gratuit, SIRENE officiel, 5 req/s rate-limited)
- Cache `entreprises_cache` (TTL 30j) → re-fetch zéro
- **Score composite** : NAF 40% + Capacité 35% + Géo 25%
  - Sweet spot CA repreneur : 2×–10× cible
  - Géo : même dept (1.0) > région (0.7) > national (0.4)
- **Inférence NAF** depuis secteur+nom (12 patterns FR : sport, boulangerie, resto, hôtellerie...)
- **Dirigeants extraits** depuis api.gouv (filter commissaires aux comptes + personnes morales sans nom)
- Touche `H` sur opp → modal Hunters avec top 30 + panneau dirigeants (mise à jour au curseur)
- Test live Magic Form Levallois → 15 candidats en 5 sec, top 2 score 1.00 (Boulogne-Billancourt + Montrouge)

### 8. UX améliorations
- **Toggle status** (`s` re-pressé enlève la shortlist) — plus de pièges
- **Undo global** `ctrl+z` (status, assign, stage)
- **Reset filtres** `0` — sortir d'un filtre piégé d'un coup
- Filtres badge highlight quand actif (jaune sur fond rouge)
- Notification "(ctrl+z annule)" après chaque action
- Boutons cliquables avec hover visuel

## Bugs résolus (voir vault/brantham/bugs/)
- [[brantham/bugs/2026-04-26-hybridrow-iter-postgres]] — `dict(rows)` itérait les noms de colonnes au lieu des values
- [[brantham/bugs/2026-04-26-postgres-having-alias]] — Postgres ne supporte pas `HAVING n` avec alias (vs SQLite OK)
- [[brantham/bugs/2026-04-26-button-pressed-selector]] — `@on(Button.Pressed)` sans sélecteur ne fire pas dans TabbedContent

## Patterns nouveaux (voir vault/brantham/patterns/)
- [[brantham/patterns/db-abstraction-sqlite-postgres-hybridrow]]
- [[brantham/patterns/hunters-concurrents-api-gouv]]
- [[brantham/patterns/todos-manager-suggestions-auto-plus-manuel]]
- [[brantham/patterns/mayday-mag-detail-parsing]]

## Décisions clés (voir vault/founder/decisions/)
- [[founder/decisions/2026-04-26-supabase-vs-vps-hetzner]] — choix Supabase pour la collab Soren (vs VPS)
- [[founder/decisions/2026-04-26-hunters-concurrents-only]] — restriction à 1 seul angle (vs 4)
- [[founder/decisions/2026-04-26-tui-vers-web-app]] — décision de migrer le cockpit vers app Next.js (TUI a un plafond UX)

## Stack final
| Composant | Tech |
|---|---|
| DB | Supabase Postgres (Ireland) — pooler 6543 |
| Backend Python | psycopg 3.3.3 + abstraction HybridRow |
| TUI | Textual 8.1.1 (transitoire — sera remplacé par Next.js) |
| Sources données | recherche-entreprises.api.gouv.fr (gratuit) |
| Scraping | LightPanda + BeautifulSoup |
| Cron | À mettre en place (launchd) |

## Stats DB après session
- 459 opps (200 actives, 47 J-7 urgentes)
- 2 deals (Magic Form Levallois en DD, MARTECH parasite à nettoyer)
- 21 suggestions auto-générées
- 30 cabinets AJ scrapés (+2 nouveaux : STAR, AJ Associés)

## Next steps
1. **Sécurité immédiate** : reset password Supabase (le précédent a transité par conv)
2. **Onboarding Soren** : envoyer `cockpit/INSTALL_SOREN.md` + nouvelle DATABASE_URL via Signal
3. **Switch web app** : Next.js 15 + Supabase + dnd-kit pour kanban deals (4-6h v1, 8-10h v1 polished)
4. **Cron daily** : launchd job 09:00 pour scraper + import + enrich + diff
5. **Phase B Hunters extension** (si on continue le TUI) : enrichir top 5 candidats via Pappers MCP

## Frustrations user (à mémoriser)
- TUI = plafond UX inévitable (drag-drop impossible, navigation pénible)
- Modals Checkbox Textual = mal lisibles avec >10 items
- Switch d'onglet trop lent (résolu : connexion persistante + refresh ciblé)
- Pas de retour arrière sur les actions (résolu : ctrl+z + toggle status)

## Related
- [[brantham/_MOC]]
- [[brantham/sessions/2026-04-26-cockpit-aj]] (session Phase A précédente)
- [[brantham/bugs/2026-04-26-hybridrow-iter-postgres]]
- [[brantham/bugs/2026-04-26-postgres-having-alias]]
- [[brantham/bugs/2026-04-26-button-pressed-selector]]
- [[brantham/patterns/db-abstraction-sqlite-postgres-hybridrow]]
- [[brantham/patterns/hunters-concurrents-api-gouv]]
- [[brantham/patterns/todos-manager-suggestions-auto-plus-manuel]]
- [[brantham/patterns/mayday-mag-detail-parsing]]
- [[founder/decisions/2026-04-26-supabase-vs-vps-hetzner]]
- [[founder/decisions/2026-04-26-hunters-concurrents-only]]
- [[founder/decisions/2026-04-26-tui-vers-web-app]]
- [[brantham/deals/active/magic-form-levallois/_MOC]]
- [[_system/MOC-master]]
