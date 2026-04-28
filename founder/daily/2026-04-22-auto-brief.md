---
type: daily-brief
date: 2026-04-22
generated: auto
---

# Brief Matinal -- 2026-04-22

## Pipeline

- **Deals actifs** : 350 dossiers workspace (317 avec analyse, 248 avec acheteurs identifiés)
- **Teasers générés** : 0 / 350 -- blocage critique sur toute la chaîne de valeur
- **Procédures DB** : 80 720 en_cours + 8 727 plan_en_cours = **89 447 actives**
- **Rapport enrichissement** : aucun log aujourd'hui (auto-enrichment-2026-04-22.md absent)

## Nouvelles Opportunités (scrape 05h00 -- 1 364 annonces AJ)

Toutes les 1 364 annonces ont été scrapées ce matin. Top 3 à traiter en priorité :

**1. POLYTECHNYL** -- Chimie polyamide 6.6 (NAF 2016Z)
- Effectif : 537 salariés -- Sites : Saint-Fons (69) + Valence (26)
- CA : 605 M€ (2024), 647 M€ (2023) -- Leader européen polyamide
- Action : pipeline immédiat, taille exceptionnelle pour du M&A distressed
- Source : AJ UP -- ref 57182

**2. ADIAMAS** -- Fabrication lames/disques acier inox (cuisine pro)
- Effectif : 58 sal. -- CA : 7,67 M€ (2024) -- Palladuc (63)
- Actif immobilier propre + parc machines spécialisé -- bon profil cession
- Action : enrichissement Pappers + matching repreneurs équipementiers

**3. TRANSPORTS BALLET** -- Transport routier lots
- Effectif : 45 sal. -- CA : 5,4 M€ -- Frotey-Les-Lure (70 -- Haute-Saône)
- Dessert Bourgogne-Franche-Comté, Grand-Est, Centre-Pays de Loire
- Action : vérifier si doublon avec deals transport existants

## Deadlines Proches

| Entreprise | Date limite | CA | Localisation | Priorité |
|---|---|---|---|---|
| CANGIA | 22/04 (AUJOURD'HUI) | n/d | Rennes | URGENT |
| ERARD TRANSPORT | 22/04 (AUJOURD'HUI) | n/d | Rennes | URGENT |
| Fabrication outillage de presse | 22/04 (AUJOURD'HUI) | n/d | n/d | URGENT |
| GETEX | 24/04 | 3,3 M€ | Challans (85) | Haut |
| CONFIT DE PROVENCE | 24/04 | n/d | n/d | Haut |

3 deals expirent aujourd'hui -- vérifier si offres déposées ou à soumettre.

## Actions Recommandées

**Priorité 1 -- Immédiat (aujourd'hui)**
- Vérifier statut CANGIA, ERARD TRANSPORT, Fabrication outillage : offres déposées ou abandon ?
- Qualifier POLYTECHNYL : deal de 100 M€+ potentiel, contact AJ UP aujourd'hui

**Priorité 2 -- Cette semaine**
- Lancer génération teasers en batch : 317 analyses sans aucun teaser = pipeline bloqué
  Commande : `python3 generate_teaser.py --batch 20` dans `/Users/paul/Downloads/brantham-pipeline/`
- Compléter acheteurs pour les 102 deals sans (350 - 248) : lancer `enrich_v2.py --batch 5 --phase repreneurs`

**Priorité 3 -- Suivi**
- Créer rapport enrichissement du jour (aucun log auto-enrichment aujourd'hui)
- Relancer pipeline daily si non exécuté : `python3 orchestration/daily.py`

## Métriques

| Indicateur | Valeur | Objectif | Statut |
|---|---|---|---|
| Annonces AJ scrapées | 1 364 | > 20/jour | OK |
| Procédures actives scorées | 89 447 | -- | -- |
| Score moyen DB | 37/100 | -- | -- |
| Score max | 84 (BRANDT FRANCE) | -- | -- |
| Deals avec analyse | 317 / 350 | 100% | 91% |
| Deals avec teaser | 0 / 350 | 100% | BLOQUÉ |
| Deals avec acheteurs | 248 / 350 | 100% | 71% |
| Enrichissement du jour | Non exécuté | Cycle 3h | MANQUANT |

**Top scoring (en_cours)** : BRANDT FRANCE (84) -- STAR'S SERVICE (82) -- API TECH (82) -- IDKIDS (82) -- SILICONES ALIMENTAIRES (81)

---
*Généré automatiquement le 2026-04-22 -- Sources : aj_annonces.json (1 364 entrées) + PostgreSQL (89 447 procédures actives) + deals workspace (350 dossiers)*
## Related
## Related
