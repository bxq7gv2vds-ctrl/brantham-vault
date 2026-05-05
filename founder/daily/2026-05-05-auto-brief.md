---
type: daily-brief
date: 2026-05-05
generated: auto
---

# Brief Matinal -- 2026-05-05

## Pipeline

- **423 dossiers actifs** dans `/deals/` (vs 25 au 25/03 -- pipeline x17 en 6 semaines)
- **90 089 procedures actives** en base (81 362 en_cours + 8 727 plan_en_cours)
- **Valeur estimee** : non calculee (champ prix_cession absent du scan rapide)
- **Statuts deals** : 391 avec analyse, 0 avec teaser, 293 avec acheteurs identifies

## Nouvelles Opportunites

Dernier scraping : 2026-05-03 (aucun scraping aujourd'hui -- a relancer).
452 opportunites detectees lors du cycle 00:23. 923 annonces en base, 82 avec deadline future.

Top 3 avec deadline aujourd'hui (2026-05-05) :

1. **Les Invites au Festin** (AJRS) -- Association loi 1901, CA 1,95M, 39 salaries, Besancon. Deadline : 2026-05-05. Secteur : insertion sociale.
2. **Groupes electrogenes installation/maintenance** (AJRS) -- CA 1,5M, 12 salaries, 78490 Mere. Deadline : 2026-05-05. Actif technique.
3. **Institut de beaute Paris 8eme** (AJRS) -- CA 162 001, 5 salaries, Paris. Deadline : 2026-05-05. Fonds de commerce.

## Deadlines Proches

- 4 annonces avec deadline = 2026-05-05 (dont les 3 ci-dessus + fabrication ossatures bois, FHBX)
- Aucune deadline DB identifiee dans les 7 jours via `date_jugement_ouverture` (ce champ = date ouverture, non date limite)
- Recommande : interroger `annonce_bodacc` pour les vraies dates de depot d'offres

## Actions Recommandees

| Priorite | Action | Impact |
|----------|--------|--------|
| CRITIQUE | Relancer scraper AJ (`python3 scraper_aj.py --output`) -- pas de scraping depuis 48h | Detection nouvelles opportunites |
| CRITIQUE | Generer teasers : 0/423 deals en ont un -- bottleneck total du pipeline | Qualification acheteurs impossible sans teaser |
| HAUTE | Analyser les 32 deals sans analyse (priorite : deals avec acheteurs deja identifies) | Debloquer matching 4D |
| HAUTE | Lancer matching acheteurs sur les 391 deals analyses sans acheteurs (130 manquants) | Pipeline outreach |
| NORMALE | Contacter mandataire pour les 4 deals deadline aujourd'hui (AJRS x3 + FHBX) | Opportunites a ne pas rater |
| NORMALE | Verifier enrichissement Pappers sur top 10 DB (BRANDT, CLINIQUE CHAMPS-ELYSEES, API TECH) | Amelioration scoring |

## Metriques

| Metrique | Valeur | Objectif |
|----------|--------|----------|
| Procedures actives DB | 90 089 | -- |
| Score moyen | 37/100 | -- |
| Score max | 84 (Brandt France) | -- |
| Annonces AJ en base | 923 | > 20/jour |
| Annonces avec deadline future | 82 | -- |
| Deals avec analyse | 391/423 (92%) | 100% |
| Deals avec teaser | 0/423 (0%) | > 80% |
| Deals avec acheteurs | 293/423 (69%) | > 80% |
| Dernier scraping AJ | 2026-05-03 | Quotidien |
| Enrichissement (CA+eff) | 632/923 (68%) | > 80% |

## Related

[[brantham/_MOC]]
[[founder/daily/2026-03-30-auto-brief]]
