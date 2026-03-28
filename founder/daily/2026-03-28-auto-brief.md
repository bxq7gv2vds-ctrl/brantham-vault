---
type: daily-brief
date: 2026-03-28
generated: auto
---

# Brief Matinal -- 2026-03-28

## Pipeline

- **70 deals actifs** dans le workspace (45 analyses, 0 teasers, 33 acheteurs identifies)
- **0 teaser produit** sur 70 deals -- blocage majeur sur la chaine de valeur
- **25 deals sans analyse** (dont AV.CO. BOIS, TELE MENAGER MORE, USINE DE PANIFICATION)
- Valeur estimee pipeline : non calculable (acces DB indisponible ce matin -- voir Metriques)
- Deals les plus avances : `ajilink-provence-arris`, `ajrs-sohnej`, `ajilink-provence-jott`, `ascagne-*` (analyse + acheteurs, manque teaser)

## Nouvelles Opportunites

Scrape AJ du 28/03 04:17 : **462 opportunites** (31 sites, 25 OK, 6 vides). 345 cessions / 117 redressements.

**1. TECHNISOL** -- BTP terrassement/demolition
- CA : 11.2M€ | SIREN : 508845641
- Source : Meynet | Slug : `meynet-technisol`
- Statut : analyse creee, acheteurs vides (API down)
- Signal fort : taille + secteur (BTP, repreneurs industriels nombreux)

**2. Entreprises de nettoyage** -- Services aux entreprises
- CA : 6.1M€ | 291 salaries | SIREN : 303663991
- Source : Ajilink IHDF | Slug : `ajilink-ihdf-entreprises-de-nettoyage`
- Statut : analyse creee, acheteurs vides
- Signal fort : masse salariale importante, secteur liquide

**3. AV.CO. BOIS** -- Construction ossature bois
- CA : De 3 a 10M€ | 50-250 salaries | Haute-Garonne (31)
- Source : Ajilink Sud-Ouest | Slug : `ajilink-sudouest-av-co-bois`
- Statut : dossier non cree (identifie ce matin), pas d'analyse
- Signal fort : secteur bois/construction en forte demande repreneur

## Deadlines Proches

9 opportunites expirent dans les 7 prochains jours :

| Date | Entreprise | Type | CA | Source |
|------|-----------|------|----|--------|
| **30/03** | Bails -- PARIS | cession | -- | Asteren |
| **31/03** | Diffusion des marques streetwear | redressement | 4.16M€ | AJRS |
| **31/03** | LES INVITES AU FESTIN (association) | redressement | -- | AJRS |
| **31/03** | MECADEP SAS | redressement | -- | AJRS |
| 02/04 | CABASSE SA | cession | -- | FHBX |
| 03/04 | Fonds de commerce -- Maisons Laffitte | cession | -- | Asteren |
| 03/04 | TECH POWER ELECTRONICS | redressement | -- | AJRS |
| 03/04 | THIERRY BEURON / TRANSFRIGO 11 SAS | cession | -- | FHBX |

**Urgence 48h** : "Diffusion des marques streetwear" (CA 4.16M€, deadline 31/03) est le seul avec CA connu -- a contacter aujourd'hui.

## Actions Recommandees

**Priorite 1 -- Critique**
- [ ] Relancer FastAPI : `cd /Users/paul/Desktop/brantham-partners/api && source .venv/bin/activate && uvicorn main:app --host 0.0.0.0 --port 8000`
- [ ] Une fois API up : lancer matching-repreneurs sur TECHNISOL et Entreprises nettoyage (acheteurs vides depuis ce matin)

**Priorite 2 -- Haute**
- [ ] Generer teasers pour les 45 deals avec analyse : aucun teaser produit, c'est le seul output livrable aux repreneurs
- [ ] Commencer par les 5 deals les plus avances : `ascagne-agence-conseil-digital`, `ajrs-sohnej`, `ajilink-provence-arris`, `ajilink-ihdf-entreprises-de-nettoyage`, `ajilink-ihdf-transports-routiers`

**Priorite 3 -- Normal**
- [ ] Creer dossier et analyse pour AV.CO. BOIS (CA 3-10M, 50-250 eff, BTP bois)
- [ ] Contacter AJ Asteren / AJRS pour les 4 deals deadline 30-31/03
- [ ] Resoudre acces Docker/PostgreSQL pour monitoring DB (Docker API version incompatible)

## Metriques

| Metrique | Valeur | Objectif |
|----------|--------|----------|
| Opportunites detectees | 462 (scrape 04:17) | > 20/j |
| Nouvelles qualifiees (session) | 10 (critere CA>500K ou eff>10) | -- |
| Deals en pipeline | 70 | > 5 |
| Taux analyse | 64% (45/70) | > 80% |
| Taux teaser | 0% (0/70) | > 50% |
| Taux acheteurs identifies | 47% (33/70) | > 80% |
| Enrichissement Pappers | 5/10 SIREN resolus | > 80% |
| Score moyen DB | indisponible (DB inaccessible) | -- |
| FastAPI | DOWN | UP |
| Docker / PostgreSQL | inaccessible (API version) | UP |

*Infrastructure : FastAPI down depuis cette nuit (repreneurs non executes). PostgreSQL inaccessible depuis cette session (Docker API 500 -- probablement version mismatch apres update).*

## Related

- [[brantham/_MOC]]
- [[brantham/sessions/auto-enrichment-2026-03-28]]
- [[brantham/pipeline/QUEUE]]
- [[_system/MOC-decisions]]
