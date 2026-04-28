# Auto-Enrichment — 2026-04-28

**Heure** : 19h52  
**Budget utilisé** : ~$0.45  

## Résumé

| Métrique | Valeur |
|----------|--------|
| Opportunités identifiées | 10 |
| Dossiers créés | 10 |
| Enrichissements sauvés | 10 |
| Repreneurs trouvés | 0/10 deals |
| Erreurs | 0 |

## Détail pipeline

- Scraper AJ relancé (fichier avait 6h30) → 464 opportunités, 29 sites OK, 4 vides
- 212 nouvelles opportunités sans dossier identifiées
- Top 10 sélectionnées par secteur (transport sanitaire, optique, maroquinerie, restauration rapide, électronique)
- Enrichissement minimal (pas de SIREN — annonces AJ2M anonymisées)
- Repreneurs via recherche-entreprises.api.gouv.fr (API gouvernement gratuite)
- FastAPI locale DOWN (port 8000) — endpoint matching non disponible

## Opportunités traitées

- AMBULANCES TAXIS TRANSPORT PMR (Transport sanitaire et PMR)
- Franchise Atol (Optique) (Commerce optique franchise)
- Réseau maroquinerie bagagerie (Commerce maroquinerie retail)
- Jardinerie Animalerie (Jardinerie et animalerie)
- Franchise Domino's Pizza Seine-Maritime (Restauration rapide franchise)
- Comptoir Electronique d'Armor (CEA) (Commerce équipements électroniques)
- Groupe Domino's Pizza (Restauration rapide franchise (groupe))
- Transport colis VL + Point relais (Transport colis dernier kilomètre)
- CANGIA - Brasserie Rennes (Restauration brasserie)
- PORCLO (Activité non précisée)

## Prochaines étapes

1. Relancer FastAPI : `cd /Users/paul/Desktop/brantham-partners/api && uvicorn main:app --port 8000`
2. Contacter AJ 2M pour les 10 opportunités créées
3. Enrichir via Pappers après obtention SIREN (dataroom)
4. Re-scorer les nouvelles opportunités une fois enrichies

## Related

[[brantham/_MOC]]
[[brantham/pipeline/QUEUE]]
