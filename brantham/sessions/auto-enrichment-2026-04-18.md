---
date: 2026-04-18
type: session
projet: brantham
---

# Session auto-enrichment — 2026-04-18

## Résumé

| Etape | Résultat |
|-------|----------|
| Scraper AJ (40 sites) | OK — 467 opportunités collectées |
| Opportunités qualifiées (CA>500K ou score>60) | 14 identifiées |
| Nouvelles opportunités sans dossier | 0 — tout déjà traité |
| Enrichissements créés | 0 (rien de nouveau) |
| Erreurs | 0 |

## Détail

- **Scrape** : aj_annonces.json avait 7h48 de retard. Relancé et mis à jour (467 opps, 24 sites OK, 6 vides, 1 erreur).
- **Opportunités qualifiées** : 14 (toutes CA > 500K, scores pertinence = 0 car scraping sans flag --llm).
- **Nouveaux dossiers** : aucun à créer — toutes les 14 opportunités qualifiées ont déjà un dossier + enrichment.json dans deals/.
- **Backlog acheteurs** : 84 dossiers enrichis sans acheteurs.json — prochain cycle deep enrichment.

## État du pipeline

- Dossiers totaux : 319
- Avec enrichment.json : 298
- Avec acheteurs.json : 215
- Avec analyse.md : 285
- **Sans acheteurs (priorité)** : 84

## Actions suivantes recommandées

1. Lancer matching repreneurs sur les 84 dossiers sans acheteurs.json (par batch de 10).
2. Re-scraper avec --llm pour recalculer les scores pertinence.
3. Vérifier les deals en deadline proche via la base PostgreSQL.

## Related

- [[brantham/_MOC]]
- [[brantham/pipeline/QUEUE]]
- Deep enrichment termine a 15:41
---
