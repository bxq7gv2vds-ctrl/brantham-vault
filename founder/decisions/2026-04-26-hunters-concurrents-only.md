---
date: 2026-04-26
project: brantham
tags: [decision, sourcing, hunters, repreneurs]
status: active
---

# Décision : Hunters repreneurs limités aux concurrents (vs 4 angles)

## Contexte
Lors de la conception du module sourcing repreneurs (Phase B du cockpit), 4 angles étaient initialement envisagés selon le memory historique :
1. Concurrents directs (même NAF)
2. PE / Holdings sériels (catalog ~80 fonds FR)
3. Acquéreurs sériels (BODACC ≥3 acquisitions/3 ans)
4. Verticaux (clients/fournisseurs)

## Décision retenue : seulement angle #1 (concurrents)
Paul a tranché : "on va être que sur des repreneurs dans le même secteur et donc concurrent".

## Pourquoi
- **Simplicité** : 1 source (api.gouv) vs 4 sources hétérogènes
- **Quota Pappers économisé** (100 tokens/mois) : pas de cartographie groupe massive
- **Pertinence pratique** : pour les PME distressed CA <5M€ ciblées Brantham, les acquéreurs réalistes sont d'abord les concurrents régionaux (M&A buy-side classique)
- **Time-to-value** : ~2h dev vs ~6-8h pour les 4 angles
- **Évolutif** : on peut rajouter PE/Sériels plus tard si le besoin se confirme

## Mise en œuvre
- Module `cockpit/hunters/` :
  - `api_gouv.py` : client recherche-entreprises.api.gouv.fr (gratuit, SIRENE officiel)
  - `cache.py` : table `entreprises_cache` TTL 30j
  - `rate_limit.py` : token bucket 5 req/s
  - `scoring.py` : score composite NAF 40% + Capacité 35% + Géo 25%
  - `runner.py` : orchestrateur `hunt(opp)` avec inférence NAF auto
- Touche `H` sur opp dans le TUI → modal Hunters avec top 30 candidats + dirigeants

## Test live
Magic Form Levallois (salle de sport, NAF 93.13Z, 92, CA 500k€) :
- 15 candidats trouvés en 5 sec
- Top 2 score 1.00 : VIGNAUD CHRISTIAN (Boulogne), TUBIANA (Montrouge) — même dept, NAF identique, capa OK
- Dirigeants extraits automatiquement (Président SAS / DG)

## Why
Karpathy : Simplicity First. Faire 1 chose qui marche bien plutôt que 4 choses moyennes. La donnée la plus pure (SIRENE officiel) sur l'angle le plus pertinent (concurrents).

## How to apply
- Toute nouvelle opp shortlistée → touche `H` lance le hunt automatiquement
- Si NAF non détecté par les 12 patterns d'inférence → ajouter le pattern dans `runner.py:_detect_naf`
- Si on veut élargir un jour : ajouter `cockpit/hunters/pe_catalog.py` ou `acquereurs_serie.py` sur le même modèle

## Related
- [[brantham/sessions/2026-04-26-cockpit-tui-supabase-hunters]]
- [[brantham/patterns/hunters-concurrents-api-gouv]]
- [[brantham/_MOC]]
- [[_system/MOC-decisions]]
