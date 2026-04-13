---
type: daily-brief
date: 2026-03-30
generated: auto
---

# Brief Matinal -- 2026-03-30

## Pipeline

- **Deals workspace** : 102 dossiers actifs dans `/deals/`
- **Analyse completee** : ~75 deals (74%)
- **Teasers generes** : 0 (0%) -- bottleneck critique
- **Acheteurs identifies** : ~65 deals (64%)
- **Completude moyenne** : analyse faite, mais aucun deal n'a atteint le stade teaser

**Valeur estimee pipeline** : non calculable (teasers manquants, pas de prix de cession etablis)

---

## Nouvelles Opportunites (top 3)

### 1. GROUPE JOTT - JOTT OPERATIONS
- Source : Ajilink Provence
- Secteur : Commerce habillement specialise (marque JOTT)
- CA : >10M EUR | Effectif : >250 salaries
- Localisation : Bouches-du-Rhone (13)
- Procedure : cession
- Deadline : 05/02/2026 (deja passee -- verifier si toujours ouverte)
- Deal : `ajilink-provence-groupe-jott-jott-operations` -- analyse faite, acheteurs manquants

### 2. BRANDT FRANCE (score 87/100 -- meilleur score DB)
- NAF : 2751Z (appareils electromenager)
- Effectif : 500-999 salaries
- Statut : en_cours depuis 01/10/2025
- Score : 87 -- top 1 absolu sur 89 630 procedures scorees

### 3. STE D'APPLICATION DES SILICONES ALIMENTAIRES (score 83)
- NAF : 2893Z (IAA, machines alimentaires)
- Effectif : 100-199 salaries
- Statut : en_cours depuis 01/10/2025
- Deal present : `bma-societe-d-application-des-silicones-alimentaires` -- analyse + acheteurs faits, teaser manquant

---

## Deadlines Proches (< 7 jours)

| Date | Societe | CA | AJ | Priorite |
|------|---------|----|----|----------|
| 30/03 AUJOURD'HUI | Bails -- PARIS | n/d | Asteren | URGENT |
| 31/03 demain | Diffusion marques streetwear | 4.1M EUR | AJRS | HAUTE |
| 31/03 demain | LES INVITES AU FESTIN | n/d | AJRS | MOYENNE |
| 31/03 demain | MECADEP SAS | n/d | AJRS | MOYENNE |
| 02/04 | CABASSE SA | n/d | FHBX | HAUTE |
| 03/04 | TECH POWER ELECTRONICS | n/d | AJRS | HAUTE |
| 03/04 | THIERRY BEURON / TRANSFRIGO 11 | n/d | FHBX | MOYENNE |

Aucune deadline < 7j detectee en base BODACC (date_fin_observation).

---

## Actions Recommandees

### Priorite CRITIQUE

1. **Lancer generation teasers en batch** -- 0 teaser sur 102 deals est bloquant. Commencer par les deals avec analyse + acheteurs (>60 eligibles). Commencer par les meilleurs scores : `bma-societe-d-application-des-silicones-alimentaires`, `ajilink-grandest-fonderie-de-niederbronn`, `ajup-aciers-coste`, `nacon`.

2. **Deadline 31/03 -- Diffusion marques streetwear (AJRS, CA 4.1M)** -- Envoyer candidature ou email AJ avant fin de journee. Deal present dans workspace : `ajrs-diffusion-des-marques-et-de-la-culture-streetwear-en-fr` (analyse + acheteurs ok, teaser manquant).

### Priorite HAUTE

3. **BRANDT FRANCE (score 87)** -- Meilleur score DB. Pas de deal dans workspace. Creer dossier, lancer analyse et matching repreneurs en priorite.

4. **Deadline 30/03 -- Bails Paris (Asteren)** -- A traiter aujourd'hui. Verifier si deal present, sinon contacter AJ directement.

5. **Lancer analyse sur les 26 deals sans aucune action** -- Priorite : `aj2m-biosency`, `ajilink-ihdf-commerce-detail-sport`, `aj2m-bretagne-home-service`, `aj2m-depixus`.

### Priorite NORMALE

6. **Enrichissement financier** -- 78 069 procedures en_cours, seulement 48% scorees. Lancer batch enrichissement Pappers sur procedures score > 50 sans bilan.

7. **Groupe JOTT** -- Verifier si la deadline du 05/02 est passee ou si la procedure est toujours ouverte. Si oui, lancer hunter.

---

## Metriques

| Metrique | Valeur | Objectif | Ecart |
|----------|--------|----------|-------|
| Opportunites AJ scrapees | 460 (29/03) | >20/j | OK |
| Procedures actives DB | 86 796 (en_cours + plan) | -- | -- |
| Procedures scorees | 89 630 / 186 249 | 100% | 52% |
| Score moyen | 37/100 | -- | -- |
| Score max | 87/100 (BRANDT) | -- | -- |
| Deals avec analyse | ~75/102 | 100% | 26% |
| Deals avec teaser | 0/102 | 100% | 100% |
| Deals avec acheteurs | ~65/102 | 100% | 36% |
| Sites AJ scrapes | 31/40 | 40 | -9 |
| Enrichissement 30/03 | 459 opps (cycle 01:12) | cycle complet | cycle partiel |

**Infrastructure** : PostgreSQL ok. Scraper AJ actif (31/40 sites).

---

## Related

- [[brantham/_MOC]]
- [[founder/daily/2026-03-30-auto-brief]]
