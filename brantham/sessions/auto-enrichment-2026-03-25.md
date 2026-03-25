---
type: session
project: brantham
date: 2026-03-25
tags: [scraping, aj, auto-enrichment, pipeline]
---

# Auto-Enrichment AJ -- 2026-03-25

## Scan Summary

| Metric | Value |
|--------|-------|
| Sites scraped | 24/31 (7 vides, 0 erreurs) |
| Opportunites totales | 456 |
| Expirees supprimees | 348 |
| Avec CA identifie | 127/456 |
| CA >= 1M EUR | 75 |
| Avec effectif identifie | 143/456 |
| Procedures cession | 338 |
| Procedures RJ | 112 |
| Procedures LJ | 4 |
| Statut | Toutes "nouveau" (premier scan) |

Fichier JSON: `/tmp/aj_scan_20260325_1704.json`
Cache API: `/Users/paul/Desktop/brantham-partners/api/aj_annonces.json`

## Top 5 Opportunites

### #1 -- Papier et electricite (Score 100/100)

- **Source AJ**: Abitbol & Rousselet
- **CA**: 204,4 M EUR
- **Effectif**: 268 salaries
- **Secteur**: Groupe specialise dans la production papetiere, l'exploitation et la valorisation forestiere, production d'electricite a partir de biomasse (usine pate a papier, turbines)
- **Procedure**: Cession
- **Dataroom**: https://www.abitbol-rousselet.fr/recherche-d-acquereur
- **Analyse**: Tres gros dossier industriel. CA exceptionnel (204M). Potentiel eleve mais complexite certaine (actifs industriels lourds, enjeux environnementaux). A investiguer en priorite.

### #2 -- Produits electroniques (Score 72/100)

- **Source AJ**: Abitbol & Rousselet
- **CA**: 30,7 M EUR
- **Effectif**: 20 salaries
- **Secteur**: Reconditionnement et revente de produits electroniques
- **Procedure**: Recherche d'investisseurs en capital / prepack cession (L.642-2)
- **Dataroom**: https://www.abitbol-rousselet.fr/recherche-d-acquereur
- **Analyse**: Profil tres interessant -- CA/employe eleve (1.5M/tete), secteur porteur (reconditionne/economie circulaire), prepack = processus plus rapide. A contacter rapidement.

### #3 -- GROUPE JOTT - JOTT OPERATIONS (Score 65/100)

- **Source AJ**: Ajilink Provence
- **CA**: Plus de 10 M EUR
- **Effectif**: Plus de 250
- **Secteur**: Commerce d'habillement specialise
- **Localisation**: 13 Bouches-du-Rhone
- **Procedure**: Cession
- **Date limite**: 05/02/2026 (EXPIREE?)
- **Dataroom**: https://provence.ajilink.fr/anonym/reprise/detail/10137672209
- **Analyse**: Marque connue (JOTT = Just Over The Top, doudounes). Gros dossier mais date limite potentiellement passee. Verifier si encore ouvert.

### #4 -- POLYTECHNYL (Score 65/100)

- **Source AJ**: AJ UP
- **CA**: Plus de 10 M EUR
- **Effectif**: Plus de 250
- **Secteur**: Fabrication d'intermediaires chimiques (sel de nylon, polyamide 6.6) et transformation
- **Localisation**: 69 Rhone
- **Procedure**: Cession
- **Date limite**: 23/02/2026 (EXPIREE?)
- **Dataroom**: https://dataroom.ajup.fr/anonym/reprise/detail/10189076469
- **Analyse**: Industrie chimique specialisee, probablement filiale d'un groupe. Date potentiellement passee. A verifier.

### #5 -- Commerce d'articles de sport (Score 47/100)

- **Source AJ**: Ajilink IHDF
- **CA**: Plus de 10 M EUR
- **Effectif**: De 50 a 250
- **Secteur**: Commerce de detail d'articles de sport, nature, loisirs, chasse, peche, equitation
- **Localisation**: 17 Charente-Maritime
- **Procedure**: Cession
- **Date limite**: 07/04/2026 (OUVERTE)
- **Dataroom**: https://ihdf.ajilink.fr/anonym/reprise/detail/10133566369
- **Analyse**: Opportunite encore ouverte (deadline 7 avril). Multi-activite loisirs/sport. Bonne taille (50-250 employes, CA>10M). A prioriser car deadline proche.

## Mentions honorables (#6-10)

| # | Entreprise | CA | Effectif | Procedure | Score |
|---|-----------|-----|----------|-----------|-------|
| 6 | RELAIS COLIS | >10M | 50-250 | Cession | 47 |
| 7 | PSE AR.VAL | >10M | 50-250 | Cession | 47 |
| 8 | SOGRAN | >10M | 50-250 | Cession | 47 |
| 9 | FONDERIE DE NIEDERBRONN | >10M | 50-250 | Cession | 47 |
| 10 | SILICONES ALIMENTAIRES | >10M | 50-250 | Cession | 47 |

## Recommandations

1. **Priorite #1**: Commerce d'articles de sport (#5) -- deadline 7 avril, encore actionnable
2. **Priorite #2**: Produits electroniques (#2) -- prepack, secteur porteur, contacter l'AJ
3. **Investigation**: Papier et electricite (#1) -- verifier si le dossier est a notre portee (204M = gros)
4. **Verification deadlines**: JOTT (#3) et POLYTECHNYL (#4) ont des dates passees -- verifier statut
5. **Batch #6-10**: 5 dossiers CA>10M a screener rapidement

## Next Steps

- [ ] Ouvrir les datarooms des top 5 et evaluer la documentation disponible
- [ ] Qualifier via LLM (`scraper_aj.py --llm`) pour un scoring plus fin
- [ ] Contacter les AJ pour les dossiers prioritaires
- [ ] Integrer dans le pipeline Director pour analyse automatisee
