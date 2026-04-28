---
date: 2026-04-28
project: brantham
type: session
tags: [cockpit-web, outreach, minimalisme, daily-brief, M&A]
---

# Session 2026-04-28 — Cockpit minimalisme + outreach tracker + daily brief

## Contexte
Reprise du cockpit-web après la session 2026-04-27 (build initial). Premier deal Magic Form Levallois en pipeline (deadline 21/05/2026, fees 14k HT). User demande "gros gros chantier" : audit complet + uniformisation process + DA minimaliste.

## Audit (3 agents parallèles)
1. **Minimalisme** : surface combinatoire absurde (9 stages × 5 onglets × 4 status × 4 life), 15 suppressions identifiées
2. **Frictions terrain** : pain point #1 = pas d'outreach tracker (`contacted_at` manquant) → app reste un Excel glorifié sans ça
3. **Workflow idéal** : roadmap 9 étapes (scrape → triage → mandat AJ → mandat repreneur → teaser → sourcing → outreach → NDA → offre/closing/facturation)

## Réalisé — 17 tâches en 3 vagues

### Vague 1 — Minimalisme (T01-T07)
- Stages 9 → 6 (qualif/mandat/offre/closing + won/lost). Migration DB sourcing+outreach→mandat, due_diligence→offre.
- Onglet Pipeline supprimé (fusionné dans Deals).
- Onglet Finance caché si `won_count < 3 && pipeline_brut == 0`.
- Filtres Opps `status × life × showBin` → 1 chip `Vue` (5 options).
- Boutons inline Opps 7 → 3 (★ ✕ →).
- Cursor global (avant per-tab).
- Drawers : Méta replié par défaut (`<details>`).

### Vague 2 — Outreach tracker (T08-T12)
- Migration 006 : `repreneurs.contacted_at | replied_at | relance_count | last_contact_channel` + index sur stale.
- API `/api/repreneurs/[id]` : actions étendues. Timestamps `COALESCE(...)` jamais écrasés.
- RepreneursPanel : filtre `⏰ Sans réponse > 5j` + bouton ↺ "Marquer répondu" + affichage "Contacté il y a Xj" + bordure stale.
- Status `replied` ajouté comme état distinct.
- Cron daily 9h30 `com.brantham.daily-relances.plist` → crée todos auto idempotentes pour stale repreneurs.

### Vague 3 — Daily brief + onboarding (T13-T17)
- Onglet `0` **"Aujourd'hui"** = landing par défaut. 4 counters (Nouvelles 24h / J-7 / Stale / Todos prio.) + 4 cards (Deals actifs / Opps J-7 / Stale / Todos urgent), tout cliquable.
- Filtre `nouveau J-7` + badge `new` sur lignes Opps `created_at < 7j`.
- Glossaire dans HelpModal (DLDO, AJ, NAF, RJ, LJ, DD, LdM, NDA, opp, deal).
- Tooltips sur en-têtes colonnes via `headerTitle` prop.
- Auto-redirect post-promote via event `cockpit:open-deal`.
- Bouton scrape affiche `"🔄 il y a 2h · +12"`.

## Bugs fixés
- **INSEE 401 silencieux** : `INSEE_API_KEY` jamais transmise au subprocess Python depuis Next (pas dans `.env.local`). Fix : `loadPipelineEnv()` dans route.ts charge `.env` du pipeline et l'injecte dans le child env.
- **UPSERT `$N` placeholder cassé** : pipeline.py utilisait `$1..$21` (postgres natif) mais le wrapper db.py ne traduit que `?`→`%s`. Fix : remplacé `$N` par `?`.
- **POST opps body non-JSON HTTP 500** → 400 (try/catch sur `request.json()`).
- **PATCH deal id inconnu HTTP 200 silent no-op** → 404 (RETURNING id + check empty).
- **PreparedStatement Supabase pooler** : scripts Python qui touchent la DB en boucle doivent utiliser `prepare_threshold=None` (pgbouncer txn mode).

## Backfill NAF
- 1/459 → 202/459 opps avec NAF (44% coverage).
- 132 inférées via patterns regex étendus (~50 secteurs).
- 70 manuelles (set_naf depuis panel ou présentes avant).
- 257 restantes : noms d'entreprise trop génériques pour matcher. SIRENE lookup par dénomination a échoué (l'API v3.11 n'expose pas la fulltext).
- **Workaround** : composant `NafFix` dans le panel quand hunt = 0 candidats avec NAF manquant → input + bouton "Sauver et relancer" + liste codes courants.

## DA uniformisée
- 0 couleur vive restante sur 9 fichiers (avant : 48 occurrences).
- Palette : zinc + cyan-400 accent uniquement. Hiérarchie via `font-bold`/`bg-zinc-700`/`line-through`/`opacity` au lieu de couleurs.
- `lib/style.ts` refactor central → cascade automatique sur Opps/Pipeline/Deals/Drawers/Finance/Todo.

## Décisions
- "Aujourd'hui" = onglet shell, pas une route distincte (`/today` n'existe pas, juste `/api/today`).
- Cron J+5 = 5j fixe, paramétrable via `--days N`.
- Status repreneur `replied` ajouté en plus de `contacted` (avant : pas distinct).
- Filtres status/tier persistés en localStorage global, pas par opp.
- Pipeline tab fusionné dans Deals (pas de toggle "groupé" pour le moment, surface minimale).

## Reste à faire — Vague 4 (différé)
- Auth Clerk + `users` (bloquant scaling Soren)
- Table `mandates` + bouton Mandater + génération LdM
- Générateur teaser MD + export PDF
- Table `aj_contacts` annuaire
- `offers` + `invoices`
- Refonte `events` en activity log normalisé
- Tracking ouverture email (pixel + token redirect)

## Action immédiate user
- `launchctl load ~/Library/LaunchAgents/com.brantham.daily-relances.plist` (1×)

## Related
- [[brantham/_MOC]]
- [[brantham/sessions/2026-04-27-cockpit-web-hunters-v2]]
- [[brantham/deals/active/magic-form-levallois/_MOC]]
- [[_system/MOC-decisions]]
