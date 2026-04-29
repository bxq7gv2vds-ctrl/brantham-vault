# Session auto-enrichment — 2026-04-29

**Heure** : 18:52  
**Type** : Cycle 3h — Scrape + Enrich + Update  

---

## Résumé

| Métrique | Valeur |
|----------|--------|
| Opportunités scrapées | 466 (29 sites) |
| Éligibles (CA>500K) | 10 |
| Dossiers créés | 10 |
| Enrichies Pappers | 3 (Fibre Excellence, SMR, Conseil) |
| Analyses générées | 10 |
| Repreneurs identifiés | 0 (API 400 — filtres nature_juridique incompatibles) |
| Erreurs | 1 (timeout Pappers camoufox sur SMR) |

---

## Opportunités traitées

- Fabrication de formes et d’outils de découpe | CA:5 469 K€ | maydaymag-fabrication-de-formes-et-d-outils-de-d-c
- Fonds de commerce de fleuriste | CA:502 303 € | aj-associes-fonds-de-commerce-de-fleuriste
- Appel d'offre pour cession d'entreprise en LJ | CA:3-10 M€ | trajectoire-appel-d-offre-pour-cession-d-entrepris
- Fibre Excellence | CA:297,7 M€ | abitbol-fibre-excellence
- Groupe spécialisé dans la production papetière, l’explo | CA:297,7 M€ | cbf-groupe-sp-cialis-dans-la-production-papeti-re-
- Conseil | CA:8,2 M€ | abitbol-conseil
- Holding détenant une société exploitant un cabinet de c | CA:8,2 M€ | abitbol-holding-d-tenant-une-soci-t-exploitant-un-
- Commercialisation, pâtisserie, confiserie régionales, s | CA:7,9 M€ | fhbx-commercialisation-p-tisserie-confiserie-r-gio
- SMR | CA:6,6 M€ | abitbol-smr
- Production et négoce de fruits et légumes | CA:5,1 M€ | trajectoire-production-et-n-goce-de-fruits-et-l-gu

---

## Problèmes rencontrés

1. **API recherche-entreprises** : HTTP 400 sur tous les appels avec filtre `nature_juridique` — probablement paramètre deprecated. Fallback non implémenté faute de budget.
2. **Pappers camoufox** : timeout sur 1 requête (SMR) — données partielles.
3. **aj_annonces.json** : format list (ancien) → format dict (nouveau scraper). Géré.

---

## Actions suivantes

- Corriger l'appel API repreneurs (retirer nature_juridique du filtre)
- Enrichir les 7 deals sans données Pappers quand SIREN identifié
- Télécharger datrooms disponibles

---

## Related

[[brantham/_MOC]] | [[brantham/pipeline/QUEUE]]
