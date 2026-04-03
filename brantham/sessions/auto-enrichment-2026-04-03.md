---
date: 2026-04-03
type: session
projet: brantham
---

# Auto-Enrichment Session — 2026-04-03

## Resume

| Metrique | Valeur |
|----------|--------|
| Opportunites traitees | 10 |
| Dossiers crees | 10 |
| Enrichissements (enrichment.json) | 10 |
| Analyses generees (analyse.md) | 10 |
| SIREN identifies | 3 |
| Erreurs | 0 |

## Contexte

- Fichier aj_annonces.json : date_scraping 2026-04-03, 458 opportunites, 31 sites scrapes
- Critere selection : nouvelles opps (sans dossier deals/) triees par CA desc
- Toutes les opps CA > 500K avaient deja un dossier
- Top 10 selectionnes incluent 2 avec CA connu (401K et 316K) + 8 sans CA renseigne
- Enrichissement via API recherche-entreprises.api.gouv.fr (gratuit)
- 3 SIREN identifies sur 10 (boulangerie Paris 13e, Vaise Sports, articles puericulture)
- Repreneurs potentiels : 5 identifies pour meynet-vaise-sports-monts-d-or

## Deals traites

- **ascagne-boulangerie-situee-a-paris-13e** — BOULANGERIE SITUEE A PARIS 13e (CA: 400 604 €)
- **meynet-vaise-sports-monts-d-or** — VAISE SPORTS MONTS D'OR (CA: 315 720€)
- **ascagne-ventes-d-articles-de-pu-riculture** — Ventes d’articles de puériculture (CA: 238.572 €)
- **ascagne-coiffeur-barbier** — Coiffeur barbier (CA: 175.603 €)
- **ascagne-boutique-atelier-de-bijoux-et-accessoires-situee-a-p** — BOUTIQUE-ATELIER DE BIJOUX ET ACCESSOIRES SITUEE A PARIS 3e (CA: 61.200 €)
- **aja-tous-les-secteursautres-secteursactivit-s-culturellesadm** — Tous les secteursAutres secteursActivités culturellesAdministration – comptabilité – juridiqueAgricultureAlimentation / Agro-AlimentaireArtisanatBeauté / coiffureBoucherieBoulangerieBTP / ConstructionCafés / Bars / discothèquesCommerceCommunication / Evénementiel / DesignHabillement / textile / retailHôtel / tourismeImmobilierIndustrieInformatiqueMédical / Pharma / Para-medicalRestaurantsServices aux particuliersServices aux professionnelsTabac / PresseTech / innovation / Start upTransport / Logistique (CA: )
- **aj2m-d-veloppement-et-commercialisation-de-solutions-naturel** — Développement et commercialisation de solutions naturelles à haut niveau de performance pour la protection des végétaux et des cultures contre les organismes nuisibles et affections (CA: )
- **aj2m-activite-distribution-alimentaire-dediee-a-la-lutte-con** — ACTIVITE : DISTRIBUTION ALIMENTAIRE DEDIEE A LA LUTTE CONTRE LE GASPILLAGE A DESTINATION DE LA RESTAURATION COLLECTIVE // Recherche cession de contrôle ou cession des actifs en RJ (CA: )
- **aj2m-activite-fabrication-de-peintures-et-produits-chimiques** — ACTIVITE : FABRICATION DE PEINTURES ET PRODUITS CHIMIQUES (MAINTENANCE-HYGIENE-ENTRETIEN) // Recherche cession de contrôle, prise de participation ou cession d&rsquo;actifs en RJ (CA: )
- **aj2m-activite-travaux-de-ma-onnerie-generale-et-gros-uvre-de** — ACTIVITE : TRAVAUX DE MAÇONNERIE GENERALE ET GROS ŒUVRE DE BATIMENT / CONSTRUCTION DE MAISONS INDIVIDUELLES et MAITRE D’ŒUVRE EXTENSIONS ET RENOVATIONS // APPEL D’OFFRES (CA: )

## Erreurs / Limites

- API gouvernement ne retourne pas toujours des repreneurs pertinents (query par secteur trop generique)
- Pappers non utilise (pas de SIREN majoritairement + rate limit 100 req/jour)
- 7/10 deals sans CA renseigne dans les annonces AJ

## Related

[[brantham/_MOC]]
[[brantham/pipeline/QUEUE]]
