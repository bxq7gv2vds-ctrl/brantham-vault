# QUEUE — Opportunites en attente de traitement

> Mise a jour : 2026-03-30 (auto-enrichment session)

## TOP 10 nouvelles opportunites traitees (2026-03-30)

| Slug | Nom | CA | Source | SIREN | Statut |
|------|-----|-----|--------|-------|--------|
| ajup-michel-liard | MICHEL LIARD | 1-3M€ | AJ UP | 318601507 | enrichi |
| ajup-dome-menuiserie-batiment-dmb | DOME MENUISERIE BATIMENT DMB | 1-3M€ | AJ UP | 342350832 | enrichi |
| ajup-les-affranchis | LES AFFRANCHIS | 1-3M€ | AJ UP | 942314261 | enrichi |
| ajire-pleine-mesure | PLEINE MESURE | 1-3M€ | Ajire | 492009816 | enrichi |
| ajire-psg-loc | PSG LOC | 1-3M€ | Ajire | 819791393 | enrichi |
| ajire-solid-r | SOLID'R | 1-3M€ | Ajire | 928713320 | enrichi |
| p2g-librairie-d-art-et-vente-en-gros-de-livres-soldes | LIBRAIRIE D'ART | 1-3M€ | P2G | N/D | enrichi partiel |
| ascagne-conception-et-fabrication-d-accessoires-et-bijoux-s- | BIJOUX FLORAL | 987K€ | Ascagne | N/D | enrichi partiel |
| ajilink-ihdf-conseil-et-recrutement-de-personnel-pour-l-h-te | Recrutement hotellerie | <1M€ | Ajilink IHDF | N/D | enrichi partiel |
| ajilink-ihdf-groupe-de-promotion-immobili-re | Groupe promotion immo | <1M€ | Ajilink IHDF | 339673410 | enrichi |

## Notes

- 6/10 avec SIREN identifie via Pappers
- Acheteurs identifies via API gouv.fr pour 9/10
- API FastAPI (port 8000) hors ligne — matching 4D non disponible
- Scraper relance en background (fichier avait 7h)
- Plusieurs deadlines depassees (Feb/Mars 2026) — verifier si encore actives

## A faire

- Relancer FastAPI pour matching 4D
- Re-lancer scraper et comparer nouvelles annonces
- Enrichir SIREN manquants manuellement (librairie, bijoux, recrutement)
