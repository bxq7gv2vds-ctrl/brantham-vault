---
type: daily-brief
date: 2026-05-11
generated: auto
---

# Brief Matinal -- 2026-05-11

## Pipeline

- **12 deals actifs** dans le workspace (`/api/data/deals/`)
- **Valeur estimée** : non calculée (enrichissement en cours au moment du brief, 00:36)
- **Statuts** : 12/12 nécessitent action — aucun deal avec teaser ni liste acheteurs finalisée
- Deals avec analyse uniquement : ideal-tiny, smr, almat-bennes-manjot, industrie-meyzieu-12518, cloud-computing-b2b, seralu, patisserie-paris, equipements-thermiques, oogarden, viticulture (10+)
- Rapport enrichissement auto incomplet : cycle 00:36 interrompu au stade scrape

---

## Nouvelles Opportunités

1408 annonces AJ en base (scrape du 11/05). Top 3 par intérêt immédiat (deadline aujourd'hui) :

**1. Viticulture (deadline : 2026-05-11)**
- CA : 14 M€ | Résultat 2024 : 25 K€ | Effectif : ~140 salariés
- Secteur porteur, taille significative. A qualifier en priorité absolue.

**2. Holding groupe 8 sociétés -- production (deadline : 2026-05-11)**
- Localisation : Paris | Effectif : 5 salariés déclarés (holding opérationnel)
- Structure de groupe = potentiel de cession partielle ou totale.

**3. ADIAMAS -- fabrication acier inox (AJ UP, ref 56103)**
- CA : 7,67 M€ | Effectif : 58 | Localisation : Palladuc (63)
- Propriétaire actif immobilier + parc machines. Score de cession élevé potentiel.

---

## Deadlines Proches

**23 annonces avec date_limite <= 2026-05-18**, dont 7 aujourd'hui même :

| Date | Entreprise | CA / Effectif |
|------|-----------|---------------|
| 2026-05-11 | Viticulture | 14 M€ / ~140 sal |
| 2026-05-11 | Holding groupe 8 sociétés production | -- / 5 sal |
| 2026-05-11 | Production bois énergie (IDF) | 3,2 M€ / 17 sal |
| 2026-05-11 | SAS NOVACOR (Chatou) | -- / -- |
| 2026-05-11 | Actifs immo en RJ (Neuilly-sur-Seine) | -- / -- |
| 2026-05-12 | Fabrication murs ossature bois (Iville) | -- / -- |
| 2026-05-12 | Technologie pigments/huiles végétales (Bernay) | -- / -- |

Action requise dès ce matin sur les 3 premières.

---

## Actions Recommandées

| Priorité | Action | Impact |
|----------|--------|--------|
| URGENT | Qualifier Viticulture (14M€, 140 sal, deadline aujourd'hui) | Opportunité rare, secteur défensif |
| URGENT | Qualifier Holding groupe production Paris (deadline aujourd'hui) | Structure groupe = levier |
| HAUTE | Générer teaser + matching acheteurs sur ADIAMAS (58 sal, actif immo) | Deal solide, données disponibles |
| HAUTE | Lancer `generate_teaser.py` + `enrich_v2.py --phase repreneurs` sur les 12 deals actifs | 0 teaser en pipeline = 0 deal possible |
| MOYENNE | Compléter le rapport enrichissement auto (cycle interrompu à 00:36) | Couverture enrichissement inconnue |
| MOYENNE | Identifier les 23 deals deadline < 7j avec SIREN pour enrichissement Pappers | Priorisation scoring |

---

## Métriques

| Métrique | Valeur | Objectif |
|----------|--------|----------|
| Procédures actives en BDD | 91 225 (82 498 en_cours + 8 727 plan_en_cours) | -- |
| Procédures scorées | 89 630 | -- |
| Score moyen (toutes) | 36 / 100 | -- |
| Score max observé | 84 (BRANDT FRANCE) | -- |
| Annonces AJ en base | 1 408 | > 20 nouvelles/j |
| Deals avec teaser | 0 / 12 | > 5 |
| Deals avec acheteurs | 0 / 12 | > 5 |
| Deals complets | 0 / 12 | > 1 |
| Enrichissement aujourd'hui | Partiel (scrape only, 00:36) | -- |

**Top 3 procédures DB par score** : BRANDT FRANCE (84), API TECH (82), CLINIQUE CHAMPS-ELYSÉES (82).
