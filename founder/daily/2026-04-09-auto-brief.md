---
type: daily-brief
date: 2026-04-09
generated: auto
---

# Brief Matinal -- 2026-04-09

## Pipeline

- **Procedures actives en DB** : 87 324 (statut en_cours + plan_en_cours)
- **Procedures scorees** : 89 630 | Score moyen : 37/100 | Max : 84/100
- **Deals workspace** : 220 dossiers | 188 avec analyse | 0 avec teaser | 139 avec acheteurs
- **Opportunites AJ** : 1 820 dans aj_annonces.json (dernier scrape 06:06 -- 462 actives)

## Nouvelles Opportunites (top 3 -- ajoutees ce matin)

### 1. trajectoire-g2-meca-concept
- Secteur : Mecanique industrielle / Tolerie
- CA confirme : 1,9M EUR (Pappers)
- SIREN : 450210570 | Dirigeant : Alain Pascal Dudeffend
- Statut dossier : analyse OK, teaser manquant, acheteurs manquants
- Action : generer teaser + lancer matching 4D

### 2. ajilink-ihdf-la-cantine-creteil
- Secteur : Restauration (Centre commercial Creteil)
- CA estime : 1-3M EUR
- SIREN : 850682410 | Dirigeants : Gaby Jabbour, Christian Zeidan Lahoud
- Statut dossier : analyse OK, teaser manquant, acheteurs manquants
- Action : generer teaser + lancer matching 4D

### 3. meynet-programmation-conseil-et-autres-activites-informatiqu
- Secteur : Informatique / Conseil IT (Montfavet 84)
- CA estime : 2,9M EUR
- SIREN : non identifie -- enrichissement Pappers bloque
- Statut dossier : analyse OK, teaser manquant, acheteurs manquants
- Action : sireniser manuellement + teaser + matching

## Top 10 Procedures DB par Score

| Rang | Societe | Score | NAF | Statut | Ouverture |
|------|---------|-------|-----|--------|-----------|
| 1 | BRANDT FRANCE | 84 | 2751Z | en_cours | 2025-10-01 |
| 2 | IDKIDS | 82 | 7010Z | en_cours | 2026-02-03 |
| 3 | CLINIQUE ROND POINT CHAMPS-ELYSEES | 82 | 8610Z | plan_en_cours | 2025-12-01 |
| 4 | API TECH | 82 | 2899B | en_cours | 2025-07-03 |
| 5 | STAR'S SERVICE | 82 | 4941B | en_cours | 2025-01-30 |
| 6 | FTL INTER | 81 | 5229B | en_cours | 2025-11-25 |
| 7 | ESSOR INGENIERIE | 80 | 7112B | en_cours | 2025-07-29 |
| 8 | COLISEE GROUP | 80 | 6420Z | en_cours | 2025-12-22 |
| 9 | STE APPLICATION SILICONES ALIMENTAIRES | 80 | 2893Z | en_cours | 2025-10-01 |
| 10 | TRANSPORTS BONNARD | 80 | 4941A | en_cours | 2025-07-10 |

## Deadlines Proches (< 7 jours)

26 opportunites AJ avec date_limite entre aujourd'hui et le 2026-04-15.

Top 5 urgentes :
- 2026-04-09 : RELAIS COLIS (ajup)
- 2026-04-13 : MECANIC WORKER (ajup)
- 2026-04-14 : ECOLE DE CONDUITE PREZEAU (ajire)
- 2026-04-15 : GARAGE DES STUARTS (ajup)
- 2026-04-15 : CAELI ENERGIE (ajup)

## Actions Recommandees

| Priorite | Action | Impact |
|----------|--------|--------|
| P0 | Relancer FastAPI (port 8000 down) -- bloque matching repreneurs | Debloque 81 deals sans acheteurs |
| P0 | Verifier et agir sur les 26 deadlines <7j (date_limite AJ) | Opportunites qui se ferment cette semaine |
| P1 | Generer teasers pour top 3 nouveaux deals (G2 Meca, La Cantine, Meynet IT) | Prepare outreach AJ |
| P1 | Sireniser meynet-programmation-conseil (Montfavet 84, IT, 2.9M) | Debloque enrichissement Pappers |
| P2 | Lancer matching 4D sur top 10 DB (BRANDT, IDKIDS, API TECH) | Pipeline haute valeur non traite |
| P2 | Analyser 32 deals sans aucun fichier | Nettoyer backlog workspace |
| P3 | Enrichissement bilans BRANDT FRANCE (SIREN 801250531, score 84) | Meilleur dossier DB non enrichi |

## Metriques

| Metrique | Valeur | Objectif |
|----------|--------|----------|
| Opportunites detectees (session) | 462 (scrape 06:06) | > 20/jour |
| Nouvelles annonces AJ | 3 dossiers crees | -- |
| Score moyen pipeline DB | 37/100 | -- |
| Score max disponible | 84/100 (BRANDT FRANCE) | -- |
| Taux enrichissement (analyse) | 85% (188/220) | > 80% |
| Taux teaser | 0% (0/220) | -- |
| Taux matching acheteurs | 63% (139/220) | -- |
| FastAPI | DOWN | UP |
| Enrichissement Pappers | 2/3 ce matin | -- |

## Related

- [[brantham/_MOC]]
- [[brantham/sessions/auto-enrichment-2026-04-09]]
- [[founder/daily/2026-04-09]]
