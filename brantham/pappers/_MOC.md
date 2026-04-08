---
type: moc
updated: 2026-04-08
---

# Pappers Intelligence Hub

Cartographie complete des entreprises francaises via [Pappers MCP](https://www.pappers.fr/mcp).
Source unique de data corporate enrichie pour le deal flow Brantham Partners.

## Architecture

```
pappers/
  _MOC.md                  # Ce fichier — index central
  entreprises/             # 1 fiche par SIREN — profil complet
  secteurs/                # 1 fiche par code NAF — analyse sectorielle
  dirigeants/              # 1 fiche par personne — mandats, reseau
  beneficiaires/           # 1 fiche par beneficiaire effectif — participations
  procedures-collectives/  # 1 fiche par procedure — suivi BODACC
  financials/              # 1 fiche par (SIREN, annee) — comptes annuels
  cartographie/            # 1 fiche par groupe — organigramme, liens
  recherches/              # Recherches sauvegardees — snapshots
  scripts/                 # Automatisation fetch/enrich/monitor
```

## Quick Stats

| Metrique | Valeur | Maj |
|----------|--------|-----|
| Entreprises cartographiees | 0 | 2026-04-08 |
| Dirigeants profiled | 0 | 2026-04-08 |
| Secteurs analyses | 0 | 2026-04-08 |
| Procedures suivies | 0 | 2026-04-08 |
| Groupes cartographies | 0 | 2026-04-08 |
| Tokens Pappers restants | 100/mois | 2026-04-08 |

## Workflow

### 1. Recherche & Decouverte
```
/pappers search "BTP liquidation Ile-de-France"
→ vault/brantham/pappers/recherches/2026-04-08-btp-lj-idf.md
```

### 2. Enrichissement Entreprise
```
/pappers fetch 123456789
→ vault/brantham/pappers/entreprises/123456789-nom.md
→ vault/brantham/pappers/dirigeants/prenom-nom.md (auto-cree)
→ vault/brantham/pappers/beneficiaires/prenom-nom.md (auto-cree)
→ vault/brantham/pappers/financials/123456789-2025.md (auto-cree)
```

### 3. Cartographie Groupe
```
/pappers carto 123456789
→ vault/brantham/pappers/cartographie/nom-groupe.md
→ + fiches filiales auto-creees
```

### 4. Analyse Sectorielle
```
/pappers secteur 4520A
→ vault/brantham/pappers/secteurs/4520A-reparation-automobile.md
```

### 5. Monitoring BODACC
```
/pappers monitor --procedure lj,rj --departement 75,92,93,94
→ Nouvelles procedures → fiches auto-creees
→ Scoring deal automatique
```

## Templates

| Template | Usage | Lien |
|----------|-------|------|
| entreprise-pappers | Profil complet entreprise | [[_system/templates/entreprise-pappers]] |
| dirigeant-pappers | Profil dirigeant/mandataire | [[_system/templates/dirigeant-pappers]] |
| secteur-pappers | Analyse sectorielle | [[_system/templates/secteur-pappers]] |
| procedure-collective-pappers | Suivi procedure | [[_system/templates/procedure-collective-pappers]] |
| financial-snapshot-pappers | Comptes annuels | [[_system/templates/financial-snapshot-pappers]] |
| cartographie-pappers | Cartographie groupe | [[_system/templates/cartographie-pappers]] |
| recherche-pappers | Resultats recherche | [[_system/templates/recherche-pappers]] |
| beneficiaire-pappers | Beneficiaire effectif | [[_system/templates/beneficiaire-pappers]] |

## Wikilinks Graph

Chaque entite est interconnectee:

```
Entreprise ←→ Dirigeants (mandats)
Entreprise ←→ Beneficiaires (detention)
Entreprise ←→ Secteur (code NAF)
Entreprise ←→ Financials (comptes annuels)
Entreprise ←→ Procedures (BODACC)
Entreprise ←→ Cartographie (groupe)
Dirigeant ←→ Dirigeant (mandats communs)
Procedure ←→ Deal Brantham (qualification)
Secteur ←→ Knowledge Playbook (expertise)
Cartographie ←→ Repreneurs potentiels
```

## Scripts Automatisation

| Script | Usage | Commande |
|--------|-------|----------|
| `pappers_fetch.py` | Fiche entreprise complete | `uv run pappers_fetch.py 123456789` |
| `pappers_search.py` | Recherche multi-criteres | `uv run pappers_search.py --naf 4520A --dept 75` |
| `pappers_enrich_deals.py` | Enrichir deals existants | `uv run pappers_enrich_deals.py` |
| `pappers_monitor.py` | Monitoring BODACC | `uv run pappers_monitor.py` |
| `pappers_secteur.py` | Analyse sectorielle | `uv run pappers_secteur.py 4520A` |
| `pappers_cartographie.py` | Cartographie groupe | `uv run pappers_cartographie.py 123456789` |

## Integration Deal Flow

```
BODACC/AJ → pappers_monitor.py → procedure-collective fiche
                                      ↓
                              Score deal > 60?
                                      ↓ OUI
                              pappers_fetch.py → entreprise fiche
                                      ↓
                              pappers_cartographie.py → groupe
                                      ↓
                              → Deal pipeline Brantham
                                      ↓
                              pappers_search.py (secteur) → repreneurs
```

## Consommation Tokens

| Action | Tokens | Notes |
|--------|--------|-------|
| Fiche entreprise | 1 | Inclut dirigeants, beneficiaires |
| Page recherche (10 resultats) | 1 | Pagination = +1/page |
| Comptes annuels | 1 | Par SIREN |
| Cartographie | 1 | Par SIREN tete de groupe |
| Document (statuts, etc.) | 1 | Par document |
| Suivi jetons | 0 | Gratuit |

**Budget**: 100 tokens gratuits/mois. Strategie: prioriser les procedures collectives et les repreneurs cibles.

## Related

- [[brantham/_MOC]]
- [[_system/MOC-master]]
- [[_system/MOC-patterns]]
- [[brantham/knowledge/procedures/]]
- [[brantham/patterns/acheteur-mapping]]
- [[brantham/deals/active/]]
