---
date: 2026-04-26
project: brantham
tags: [decision, infra, db, collab]
status: active
---

# Décision : Supabase Postgres pour DB partagée (vs VPS Hetzner)

## Contexte
Le cockpit Brantham (TUI Python triage AJ + deals + sourcing) tournait en SQLite local sur le Mac de Paul. Soren rejoint l'équipe et doit accéder aux mêmes données en temps réel.

## Options évaluées
1. **Postgres sur VPS Hetzner existant** (`95.216.198.143`)
   - Avantage : zéro nouveau compte, infra déjà payée
   - Inconvénient : ouvrir port 5432 publiquement = risque sécurité
   - Inconvénient : tunnel SSH côté Soren = 15 min de friction par poste, alias config
2. **Supabase Postgres** (managé)
   - Avantage : Soren installe rien, juste un `.env` à coller
   - Avantage : backup auto, dashboard, auth si besoin plus tard
   - Avantage : 0 config réseau, 0 maintenance
   - Inconvénient : compte tiers, dépendance externe
3. **Turso** (SQLite distribué)
   - Avantage : moins de code à toucher (compatibilité SQLite)
   - Inconvénient : compte requis + CLI install + token à gérer
4. **SQLite + git sync**
   - Inconvénient : conflits permanents, pas temps réel

## Décision retenue : Supabase
Critère décisif : **simplicité côté Soren**. Onboarding réduit à `pip install + .env + python -m cockpit`. Aucune compétence infra requise.

## Mise en œuvre
- Projet créé : `brantham-cockpit` Supabase, région **eu-west-1** (Ireland)
- DATABASE_URL pooler 6543 (Transaction mode — best perf pour Python avec psycopg)
- Plan **Free** (500 MB DB, 2 GB transfer/mois — largement suffisant pour 459 opps + futurs deals)
- Migration : 470 rows transférées (script `cockpit/migrate.py`)
- SQLite local conservé en backup

## Conséquences
- **Latence** : ~150ms par query (Ireland → France) vs <1ms en local. Atténué par connexion persistante singleton.
- **Sécurité** : password Supabase à rotater régulièrement (premier reset déjà fait)
- **Coût** : 0€/mois pour l'instant. Si on dépasse 500 MB ou 2 GB transfer → ~25€/mois
- **Migration ultérieure** : facile vers self-hosted si besoin (psql dump/restore standard)

## Why
Pour activer la collab Soren ↔ Paul sans friction d'install. Supabase est l'option qui demande **0 effort à l'autre personne** (juste copier-coller un .env).

## How to apply
- Toute nouvelle table dans le cockpit → ajouter au schéma `cockpit/db.py` (idempotent CREATE TABLE IF NOT EXISTS)
- Init auto au démarrage TUI : `db.init()` détecte les colonnes manquantes et fait les ALTER nécessaires
- Pour ajouter un autre poste : juste partager le `.env` avec DATABASE_URL via Signal/WhatsApp

## Related
- [[brantham/sessions/2026-04-26-cockpit-tui-supabase-hunters]]
- [[brantham/_MOC]]
- [[brantham/patterns/db-abstraction-sqlite-postgres-hybridrow]]
- [[_system/MOC-decisions]]
