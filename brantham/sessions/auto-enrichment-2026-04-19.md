# Session auto-enrichment — 2026-04-19

## Résumé

| Métrique | Valeur |
|----------|--------|
| Opportunités scrapées | 466 |
| Fichier aj_annonces.json | Mis à jour (était vieux de 16h) |
| Opportunités sans dossier | 249 |
| Opportunités CA >= 500K | 1 (Joue Club 1,2M€) |
| Opportunités traitées | 10 |
| Dossiers créés | 10 |
| Enrichissements Pappers | 0 (pas de SIREN disponible) |
| Repreneurs identifiés | 10 (via API gouv.fr) |
| Erreurs | 0 |

## Opportunités traitées

| Nom | CA | Type | Slug |
|-----|----|----- |------|
| SOCIETE EXPLOITANT UN MAGASIN DE JOUETS | 1215.0K€ | cession | ajilink-sudouest-societe-exploitant-un-magasin-de- |
| RECHERCHE DE REPRENEURS EN PLAN DE CESSION |  | cession | aj2m-recherche-de-repreneurs-en-plan-de-cession |
| RECHERCHE REPRENEURS EN PLAN DE CESSION |  | cession | aj2m-recherche-repreneurs-en-plan-de-cession |
| RECHERCHE REPRENEURS EN CONCILIATION PREPACK  |  | cession | aj2m-recherche-repreneurs-en-conciliation-prepack- |
| ELEVAGE DE VACHES LAITIERES |  | cession | aj2m-elevage-de-vaches-laitieres |
| CLUB DAUMESNIL |  | cession | aj2m-club-daumesnil |
| ASSOCIATION D’AIDE A LA PERSONNE |  | cession | aj2m-association-d-aide-a-la-personne |
| WETRADELOCAL |  | cession | aj2m-wetradelocal |
| ACTIVITE : RESTAURANT // Appel d&rsquo;offres |  | cession | aj2m-activite-restaurant-appel-d-rsquo-offres |
| RECHERCHE REPRENEURS PLANS DE CESSIONS PARTIE |  | cession | aj2m-recherche-repreneurs-plans-de-cessions-partie |


## Observations

- Toutes les opportunités CA significatif (86 avec CA > 500K) avaient déjà un dossier existant
- Les 249 nouvelles opportunités ont majoritairement le CA vide (données non renseignées par les AJs)
- 1 seule avec CA extrait des notes : SOCIETE EXPLOITANT UN MAGASIN DE JOUETS (Joue Club, 1,215M€, Gironde, deadline 07/05/2026)
- API FastAPI localhost:8000 non disponible — matching repreneurs via API gouvernement gratuite en fallback
- Enrichissement Pappers skippé : SIRENs non disponibles dans les annonces

## Prochaines actions recommandées

1. Accéder aux datarooms des 10 nouveaux dossiers pour extraire CA/effectif réels
2. Priorité absolue : Joue Club (CA confirmé 1,2M€, deadline 7 mai)
3. Relancer FastAPI pour activer le matching 4D natif
4. Enrichissement Pappers des deals une fois les noms d'entreprise précis obtenus

## Related

- [[brantham/_MOC]]
- [[brantham/pipeline/QUEUE]]
