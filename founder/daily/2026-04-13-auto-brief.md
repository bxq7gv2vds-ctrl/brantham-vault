---
type: daily-brief
date: 2026-04-13
generated: auto
---

# Brief Matinal -- 2026-04-13

## Pipeline

- **254 dossiers** dans le workspace deals (`/Downloads/brantham-pipeline/deals/`)
- **0 teaser généré** sur 254 deals -- blocage systémique à traiter en priorité
- **222 deals avec analyse** -- base de travail disponible
- **164 deals avec acheteurs** identifiés
- **32 deals sans rien** (ni analyse, ni teaser, ni acheteurs) -- priorité absolue

Valeur estimée pipeline : non calculable (DB inaccessible ce matin -- Docker daemon down).

## Nouvelles Opportunités

Scrape du 2026-04-13 : **656 annonces** collectées (vs 462 au cycle 00:22 -- delta de 194 nouvelles entrées).

Top 3 par intérêt M&A :

1. **POLYTECHNYL** (AJ UP / ref 57182)
   - Fabrication polyamide 6.6 -- SAINT-FONS (69) + VALENCE (26)
   - 537 salariés -- CA 605M€ (2024), en baisse depuis 1 089M€ (2022)
   - Actif industriel lourd, deux sites de production -- ticket potentiel significatif
   - Deadline : 2026-02-23 (passée -- vérifier si procédure toujours active)

2. **ADIAMAS** (AJ UP / ref 56103)
   - Fabrication lames inox pour préparateurs culinaires -- PALLADUC (63)
   - 58 salariés -- CA 7.67M€ -- propriétaire de son actif immobilier et machines
   - Profil industriel avec actifs corporels -- bon score attendu
   - Deadline : 2026-10-27

3. **TRANSPORTS BALLET** (AJ UP / ref 55687)
   - Transport routier national -- FROTEY-LES-LURE (70)
   - 45 salariés -- CA 5.4M€
   - Couverture Bourgogne-Franche-Comté / Grand-Est / Centre
   - Deadline : 2025-02-07 (passée -- deal historique dans le workspace)

## Deadlines Proches

**41 annonces avec deadline dans les 7 prochains jours.**

Urgences J+0 (aujourd'hui, 2026-04-13) :

| Entreprise | AJ | CA | Effectif |
|---|---|---|---|
| MECANIC WORKER | AJ UP | 2 888K€ | 31 (dont 17 VRP) |
| ERARD TRANSPORT | 2M & Associés | n/c | n/c |
| Papier et électricité | Abitol Rousselet | 151.3M€ | 268 salariés |
| Postes de travail virtualisés | FHBX | n/c | n/c |

J+1 : ECOLE DE CONDUITE PREZEAU (AjIRE, 11 salariés), boulangerie-patisserie (Meynet, CA 3.36M€), TOWT/SO TOWT voile (FHBX).

**Action immédiate** : contacter les AJ pour les dossiers J+0 -- délais de dépôt des offres aujourd'hui.

## Actions Recommandées

| Priorité | Action | Impact |
|---|---|---|
| 1 | Contacter AJ UP + Abitol Rousselet pour MECANIC WORKER, Papier&Elec (J+0) | Éviter les deals ratés |
| 2 | Lancer `generate_teaser.py` sur les 10 deals avec analyse + acheteurs | Débloquer la génération de teasers (0/254) |
| 3 | Lancer analyse sur les 32 deals vierges -- prioriser par CA et effectif | Couvrir le pipeline entrant |
| 4 | Relancer Docker + PostgreSQL -- DB inaccessible ce matin | Restaurer scoring et métriques |
| 5 | Lancer matching acheteurs sur les 90 deals sans `acheteurs.json` | Compléter le funnel Hunter |

## Métriques

| Indicateur | Valeur | Statut |
|---|---|---|
| Annonces AJ scrapées | 656 | Cycle 05h00 complet |
| Deals workspace | 254 | -- |
| Deals avec analyse | 222 (87%) | Correct |
| Deals avec acheteurs | 164 (65%) | A améliorer |
| Deals avec teaser | 0 (0%) | Critique |
| Deals sans aucun fichier | 32 | Priorité max |
| Deadlines J+0 | 4 | Action immédiate |
| Deadlines <7j | 41 | Surveiller |
| Score moyen DB | n/a | DB hors ligne |
| Infrastructure PostgreSQL | Hors ligne | Docker daemon down |
| Infrastructure FastAPI | Hors ligne | Dépend de Docker |

---

*Généré automatiquement le 2026-04-13 -- Sources : aj_annonces.json (656 entrées), workspace deals (254 dossiers), vault/brantham/sessions/auto-enrichment-2026-04-13.md*

## Related

- [[brantham/_MOC]]
- [[brantham/sessions/auto-enrichment-2026-04-13]]
