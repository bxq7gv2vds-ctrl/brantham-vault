---
date: 2026-04-27
type: session
projet: brantham
---

# Session auto-enrichment — 2026-04-27

## Résumé

- Fichier AJ: `aj_annonces.json` — 1853 opportunités (âge: 1.9h, pas de re-scrape nécessaire)
- Opportunités qualifiées (CA > 500K ou score > 60): 992 sans dossier existant
- **Top 10 traitées ce cycle**
- Dossiers créés: 10
- Enrichissement Pappers réussi: 1/10
- Repreneurs identifiés: 10 × 1-5 via api.gouv.fr (endpoint local inactif)
- QUEUE.md mis à jour

## Opportunités traitées

| Nom | CA | Statut |
|-----|----|--------|
| Papier et électricité | CA = 151,3 M€ ; REX  | sans SIREN |
| Clinique de soins médicaux et de réadaptation | Entre 5 et 50 M€ | enrichi |
| Editeur du titre de presse professionnelle Le | Entre 5 et 50 M€ | sans SIREN |
| Création de collections de tissu pour l’habil | Entre 5 et 50 M€ | sans SIREN |
| Travaux publics et de VRD ; terrassement spéc | Entre 5 et 50 M€ | sans SIREN |
| Fondation d’utilité publique dédiée à l’actio | Plus de 50 M€ | sans SIREN |
| Transports routiers de personnes et toutes ac | Entre 5 et 50 M€ | sans SIREN |
| Groupe exploitant, sous franchise, 7 fonds de | Entre 5 et 50 M€ | sans SIREN |
| Distribution de chaussures et d’accessoires d | Entre 5 et 50 M€ | sans SIREN |
| Vente de produits de revêtement du sol | Entre 5 et 50 M€ | sans SIREN |

## Observations

- La majorité des annonces Maydaymag sont anonymisées (pas de SIREN) — enrichissement Pappers impossible sans nom exact
- L'API locale (port 8000) est DOWN — fallback api.gouv.fr utilisé pour les repreneurs
- Rate limit Pappers préservé (1 enrichissement utilisé sur ~100 disponibles/jour)
- 992 opportunités qualifiées restantes à traiter lors des prochains cycles

## Related

[[brantham/_MOC]]
[[brantham/pipeline/QUEUE]]
- Deep enrichment termine a 09:50
---
