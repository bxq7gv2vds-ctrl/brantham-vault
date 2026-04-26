---
date: 2026-04-26
project: brantham
tags: [pattern, sourcing, hunters, api-gouv, sirene]
---

# Pattern : Hunter repreneurs concurrents via api.gouv

## Quoi
Pour une opportunité distressed donnée (PME en RJ/LJ), génère automatiquement une liste de **repreneurs concurrents pertinents** scorés sur 3 critères : NAF, capacité financière, géo.

## Pourquoi
Le différenciateur métier de Brantham : ne pas juste tracker les annonces AJ, mais **identifier qui contacter** côté repreneur en quelques secondes. Sans ça, le cabinet n'apporte pas de valeur ajoutée vs les AJ qui publient eux-mêmes.

## Comment

### Source : recherche-entreprises.api.gouv.fr
- Gratuit, données SIRENE officielles consolidées
- Pas de quota dur (rate limit raisonnable conseillé : 5 req/s)
- Endpoint : `https://recherche-entreprises.api.gouv.fr/search`
- Doc : https://recherche-entreprises.api.gouv.fr/docs/

### Pipeline
```
Opp shortlistée (NAF, CA, dept)
   ↓
Inférence NAF (12 patterns FR si pas déjà détecté)
   ↓
Recherche scope région (api.gouv) — élargit national si <10 résultats
   ↓
Cache SIREN (TTL 30j) — évite re-fetch
   ↓
Score composite par candidat
   ↓
Tri + top 30
   ↓
Insertion table `repreneurs` + display TUI
```

### Inférence NAF depuis secteur+nom
12 patterns FR pour bootstrap (à enrichir au fil du temps) :
```python
inferences = [
    (r"salle\s+sport|fitness|magic\s*form|remise\s+en\s+forme", "93.13Z"),
    (r"boulangerie|patisserie", "10.71C"),
    (r"restaurant|restauration", "56.10A"),
    (r"clinique|hôpital|santé|soins", "86.10Z"),
    (r"transport\s+routier|fret", "49.41A"),
    (r"hôtel|hotellerie", "55.10Z"),
    # ... 6 autres
]
```

⚠ Important : **format API gouv = "93.13Z" avec point**, pas "9313Z". Helper `_normalize_naf()` convertit.

### Scoring composite (somme pondérée 0..1)
```python
score = 0.40 * naf + 0.35 * capacite + 0.25 * geo

# NAF (40%)
- Identique  : 1.0
- Voisin (4 chars) : 0.7
- Même secteur (2 chars) : 0.4
- Distant : 0.1

# Capacité (35%)
- Sweet spot 2×–10× CA cible : 1.0
- 1×-2× ou 10×-20× : 0.6
- Plus petit : 0.2
- >20× : 0.3

# Géo (25%)
- Même dept : 1.0
- Même région : 0.7
- National : 0.4
```

### Estimation CA depuis tranche d'effectif INSEE
api.gouv ne renvoie pas le CA (privé). On l'estime depuis l'effectif (tranche INSEE 00-53) × 175k€/salarié (ratio CA/salarié moyen FR toutes industries).

### Extraction dirigeants
Le payload API contient `dirigeants[]` avec nom/prenoms/qualite. On filtre :
- Skip commissaires aux comptes (pas pertinent M&A)
- Skip personnes morales sans dénomination
- Garde max 8 (Président SAS, DG, gérants)

### Anti-blocage
- Token bucket 5 req/s (largement sous le quota toléré)
- User-Agent transparent : `BranthamPartners-Cockpit/1.0`
- Cache agressif `entreprises_cache` TTL 30j
- Fallback gracieux : si API down → retourne []
- Dirigeants pour "free" (mêmes payload que la recherche)

### Lien client final
Pour chaque candidat : URL annuaire-entreprises officielle :
```
https://annuaire-entreprises.data.gouv.fr/entreprise/{siren}
```
Touche `o` dans la modale Hunters ouvre le browser direct.

## Test live (preuve de valeur)
**Magic Form Levallois** (salle sport, NAF 93.13Z, dept 92, CA ~500k€) :
- 15 candidats trouvés en 5 sec
- Top 2 score 1.00 :
  - VIGNAUD CHRISTIAN (Boulogne-Billancourt 92, EI Président SAS)
  - TUBIANA (Montrouge 92, Marc Tubiana Président SAS)
- Score 0.93 : JPO FORME, WELLIFY, BODY'S PHENIX, ALFORT FITNESS, etc.
- Couverture dirigeants : 4/5 du top (ceux avec personne physique identifiable)

Sans cet outil = ~2-3h de recherche manuelle Pappers/LinkedIn par opp.
Avec = 5 sec, données 100% officielles, prêtes à exporter.

## Where
- Code : `/Users/paul/Downloads/brantham-pipeline/cockpit/hunters/`
  - `api_gouv.py` (client + normalize_entry)
  - `cache.py` (table entreprises_cache)
  - `rate_limit.py` (token bucket)
  - `scoring.py` (composite + estim_ca_from_effectif)
  - `runner.py` (orchestrateur hunt())
- Table DB : `repreneurs` (déjà au schéma) + `entreprises_cache` (créée par init)
- TUI : modal `HuntersModal` (touche `H` sur opp)

## Évolution possible (si on revient sur Pappers)
- Top 5 candidats → enrichissement via Pappers MCP `recherche-dirigeants` pour récupérer email/téléphone légaux
- Coût : 5 tokens × 5 candidats = 25 tokens (sur 100/mois)
- Réservé aux opps confirmées (pas du scan en masse)

## Related
- [[brantham/sessions/2026-04-26-cockpit-tui-supabase-hunters]]
- [[founder/decisions/2026-04-26-hunters-concurrents-only]]
- [[brantham/_MOC]]
- [[_system/MOC-patterns]]
