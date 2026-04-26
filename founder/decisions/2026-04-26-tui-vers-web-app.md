---
date: 2026-04-26
project: brantham
tags: [decision, ui, stack, web]
status: pending-implementation
---

# Décision : migrer le cockpit du TUI Textual vers une app web Next.js

## Contexte
Après ~10h de dev sur le cockpit TUI Textual, Paul exprime de la frustration UX :
- Pas de drag-and-drop dans un terminal
- Modals difficiles à naviguer
- Manque de fluidité ressentie même après optimisations DB
- Filtres pas évidents
- Pas friendly pour les non-techs

## Constat
Un TUI a un **plafond UX inévitable** :
- ASCII only, pas d'animations
- Drag-and-drop impossible
- Mobile inaccessible
- Couleurs limitées
- Navigation au clavier obligatoire (clic souris partiel)

Continuer à patcher le TUI = on tournera en rond. Le user demande des features (drag-drop kanban) qui ne sont pas faisables techniquement.

## Décision : switch vers app web Next.js sur même Supabase

### Stack
- Next.js 15 App Router + Tailwind (Paul connaît, déjà utilisé sur `internal-tool` + `zura-inspired`)
- Supabase auth + queries directes (pas de backend custom)
- shadcn/ui pour composants polish
- dnd-kit pour kanban deals
- Hosted Vercel

### Migration douce
- Le TUI continue de tourner pour la veille / scraping cron + édition rapide en terminal
- L'app web devient le cockpit principal pour le quotidien
- Les 2 tapent dans la même Supabase → zéro perte de données, zéro double saisie
- Soren utilise uniquement la web app (zéro install)

### Estimation
- v1 fonctionnelle (auth + 3 vues : Opps, Pipeline kanban drag-drop, Todos) : 4-6h
- v1 polished UX (animations, responsive, mobile-friendly) : 8-10h
- Comparable au temps déjà investi sur le TUI

## Why
Le TUI était pertinent pour bootstrapper rapidement et valider la mécanique métier (DB schema, suggestions, hunters). Il a fait son job. Mais pour usage quotidien à 2 (Paul + Soren) avec interactions fréquentes, une UI web est l'outil approprié.

## How to apply
- Prochain chantier : scaffold Next.js 15 dans nouveau dossier `brantham-cockpit-web/`
- Réutiliser la même DB Supabase (DATABASE_URL identique)
- Garder le code Python pour : scraping AJ, hunters API gouv, enrich DLDO (= cron jobs server-side)
- Le frontend lit les tables `opportunities`, `deals`, `todos`, `repreneurs` directement via Supabase client JS

## Conséquences
- Le TUI n'est PAS supprimé — coexistence avec la web app
- La table `todos` (auto + manual) marche déjà partout
- L'investissement actions cliquables dans le TUI = pas perdu, le pattern d'actions reste
- Soren n'a plus besoin de Python du tout

## Décisions liées
- [[founder/decisions/2026-04-26-supabase-vs-vps-hetzner]] (DB partagée)
- [[founder/decisions/2026-04-26-hunters-concurrents-only]] (sourcing simplifié)

## Related
- [[brantham/sessions/2026-04-26-cockpit-tui-supabase-hunters]]
- [[brantham/_MOC]]
- [[_system/MOC-decisions]]
