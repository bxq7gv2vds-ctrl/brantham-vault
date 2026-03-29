# Session auto-enrichment — 2026-03-29

**Date** : 2026-03-29
**Type** : Cycle scrape + enrich + dossiers

## Resultats

| Metrique | Valeur |
|----------|--------|
| Total opportunites dans aj_annonces.json | 460 |
| Eligibles (CA >= 500K ou score >= 60) | 28 |
| Nouvelles (sans dossier existant) | 28 |
| Traitees (top 10) | 10 |
| Dossiers crees | 10 |
| Enrichissements Pappers | 10/10 |
| Acheteurs.json generes | 10/10 |
| Erreurs repreneurs API | 10 (endpoint local et API gouv KO) |

## Opportunites traitees

- **SICA ALPES FRUITS CONDITIONNEMENT** | CA: De 1 à 3 | cession | Ajilink Provence
  Slug: `ajilink-provence-sica-alpes-fruits-conditionnement`
- **Restauration rapide de cuisine indienne - Etablissement de 150 m² et terrasse** | CA: De 1 à 3 | cession | Ajilink IHDF
  Slug: `ajilink-ihdf-restauration-rapide-de-cuisine-indienne-etablis`
- **PHARMACIE DE COUDEKERQUE** | CA: De 1 à 3 | cession | Ajilink IHDF
  Slug: `ajilink-ihdf-pharmacie-de-coudekerque`
- **GARAGE** | CA: De 1 à 3 | cession | Ajilink IHDF
  Slug: `ajilink-ihdf-garage`
- **CANAL** | CA: De 1 à 3 | cession | Ajilink IHDF
  Slug: `ajilink-ihdf-canal`
- **TEREA FLANDRES** | CA: De 1 à 3 | cession | Ajilink IHDF
  Slug: `ajilink-ihdf-terea-flandres`
- **PLUME CANE** | CA: De 1 à 3 | cession | Ajilink IHDF
  Slug: `ajilink-ihdf-plume-cane`
- **ZEGERS-TPS-SCMB** | CA: De 1 à 3 | cession | Ajilink IHDF
  Slug: `ajilink-ihdf-zegers-tps-scmb`
- **ESPACE CUISINES ET BAINS MORÉ** | CA: De 1 à 3 | cession | Ajilink Sud-Ouest
  Slug: `ajilink-sudouest-espace-cuisines-et-bains-mor`
- **UNA DU FUMELOIS** | CA: De 1 à 3 | cession | Ajilink Sud-Ouest
  Slug: `ajilink-sudouest-una-du-fumelois`

## Notes

- Scraper relance (fichier avait 16h)
- Aucun SIREN disponible dans les annonces AJ — enrichissement Pappers par nom
- Endpoint matching-repreneurs local KO — API gouv egalement KO (timeout/erreur)
- Acheteurs.json crees avec structure vide pour traitement ulterieur

## Related

[[brantham/_MOC]]
[[brantham/pipeline/QUEUE]]
- Deep enrichment termine a 16:42
---
