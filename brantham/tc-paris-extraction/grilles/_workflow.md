---
type: workflow
project: brantham
created: 2026-05-15
tags: [tc-paris, extraction, methodology]
---

# Workflow extraction grilles JSON — TC Paris

## Objectif
Produire **une grille JSON détaillée par offre** (~570 offres) selon le schéma `_schema.json`. Cette donnée structurée alimente la Phase 2 (synthèse transversale + grille de scoring).

## Structure
```
grilles/
├── _schema.json              # Schéma JSON validé
├── _workflow.md              # Ce document
├── _schema_dossier.json      # Schéma fiche dossier (si on enrichit côté procédure)
├── batches/                  # Logs par batch
│   ├── batch_01_dossiers_1-5.md
│   ├── batch_02_dossiers_6-10.md
│   └── ...
├── offres/                   # 1 JSON par offre — {offre_id}.json
│   ├── 34-01a.json
│   ├── 34-01b.json
│   └── ...
└── dossiers/                 # 1 JSON par dossier (méta procédure)
    ├── 34.json
    └── ...
```

## Sources
1. **`master-offres.csv`** : 570 offres pré-extraites (champs de base : nom_repreneur, prix, emplois, conditions)
2. **`master-dossiers.csv`** : 107 dossiers (méta procédure)
3. **PDFs originaux** : `/Users/paul/Downloads/Dossiers Entreprises/{folder}/` (300+ PDFs)
4. **`gagnants-tribunal.md`** : issue connue pour 7 dossiers (à enrichir au fur et à mesure)

## Méthodologie par agent

Chaque agent prend un batch de 5 dossiers. Pour chaque dossier :

### Étape 1 — Lire le CSV existant
- Récupérer la liste des `offre_id` pour ce dossier
- Charger les champs déjà remplis (~50% de la grille)

### Étape 2 — Lire les PDFs des offres importantes
- **Toutes les offres** si dossier ≤ 5 PDFs
- **Top 3-5 offres** (gagnante connue + 2-3 perdants représentatifs) si dossier > 5 PDFs
- Extraire les champs qualitatifs : plan industriel, BP, ton, structure, annexes, signaux faibles, extraits remarquables

### Étape 3 — Identifier l'issue (si connue)
- Croiser avec `gagnants-tribunal.md`
- Si gagnant inconnu : marquer `issue_dossier.cette_offre_retenue = "en_attente"`

### Étape 4 — Écrire les JSONs
- 1 fichier `offres/{offre_id}.json` par offre
- 1 fichier `dossiers/{dossier_id}.json` par dossier (méta seulement)
- Valider que les champs `required` sont remplis (sinon "NR" ou null)

### Étape 5 — Reporter
- Écrire un log `batches/batch_NN.md` avec : dossiers traités, nb offres extraites, anomalies, suggestions

## Champs PRIORITAIRES (signal fort)

Tous les champs ne se valent pas. Les agents doivent prioriser ces 15 champs (les plus discriminants pour Phase 2) :

1. `issue_dossier.cette_offre_retenue` (oui/non)
2. `issue_dossier.motifs_tribunal_verbatim` (gold)
3. `profil_repreneur.forme` (PP / société existante / fonds / etc.)
4. `profil_repreneur.track_record_reprises`
5. `profil_repreneur.experience_sectorielle_oui_non`
6. `volet_social.pct_reprise`
7. `volet_social.engagement_maintien_emplois_duree_mois`
8. `structure_prix.prix_total_eur`
9. `structure_prix.charges_augmentatives_eur`
10. `plan_industriel.diagnostic_qualification`
11. `plan_industriel.plan_affaires_3ans_present`
12. `conditions_suspensives.aucune_cs` (booléen)
13. `conditions_suspensives.agressivite_envers_dirigeants`
14. `forme_presentation.executive_summary_present`
15. `signaux_faibles.personnalisation_visite_site`

## Règles d'or

1. **Ne JAMAIS inventer** : si l'info n'est pas dans le PDF/CSV, écrire `null` ou `"NR"`.
2. **Verbatim si possible** : pour les motifs tribunal, citer exactement entre guillemets.
3. **Distinguer déclaratif vs documenté** : `apport_origine_documentee` distingue `"oui_rib_attestation"` vs `"oui_simple_mention"`.
4. **Si <10 cas pour une variable** : marquer `confidence: "low"` dans `meta`.
5. **Pas d'enjolivement** : capter la médiocrité quand elle est là.

## Phase 2 (après extraction)

Une fois les ~500 JSONs produits, lancer agent d'agrégation Python qui :
- Charge tous les JSONs dans un DataFrame
- Produit 10 livrables markdown (stats, anatomie, hiérarchie critères, portraits-robots, recettes rhétoriques, pièges, signaux crédibilité, grille scoring /100, bibliothèque extraits, angles morts)
- Sortie dans `analyses/synthese-phase2/`

## Estimation
- Phase 1 : ~21 agents × 5-10 min = 1-2h runtime cumulé
- Phase 2 : 1 agent agrégation + 1 agent rédaction = 30-45 min
- **Total : ~3h end-to-end**
