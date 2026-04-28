---
type: daily-brief
date: 2026-04-28
generated: auto
---

# Brief Matinal -- 2026-04-28

## Pipeline (deals actifs)

- **394 dossiers** dans le workspace deals (`/Downloads/brantham-pipeline/deals/`)
- Quasi-totalite sans teaser genere : blocage systématique sur l'étape Writer
- 2 dossiers sans acheteurs identifiés (manque Hunter)
- Rapport d'enrichissement du jour : absent (pipeline auto non déclenché)

## Base de données

- **89 630 procédures actives** (80 903 en_cours + 8 727 plan_en_cours) | 99 453 clos
- **89 630 scorées** | score moyen : **37/100** | score max : **84**

### Top 10 par score (en_cours uniquement)

| Score | Entreprise | NAF | Statut | Ouverture |
|-------|-----------|-----|--------|-----------|
| 84 | BRANDT FRANCE | 2751Z (électroménager) | en_cours | 2025-10-01 |
| 82 | STAR'S SERVICE | 4941B (transport routier) | en_cours | 2025-01-30 |
| 82 | API TECH | 2899B (machines industrielles) | en_cours | 2025-07-03 |
| 82 | IDKIDS | 7010Z (holding) | en_cours | 2026-02-03 |
| 82 | CLINIQUE CHAMPS-ELYSEES | 8610Z (médecine) | plan_en_cours | 2025-12-01 |
| 81 | FTL INTER | 5229B (logistique) | en_cours | 2025-11-25 |
| 81 | STE SILICONES ALIMENTAIRES | 2893Z (équip. alimentaire) | en_cours | 2025-10-01 |
| 80 | COLISEE GROUP | 6420Z (holding) | en_cours | 2025-12-22 |
| 80 | TRANSPORTS BONNARD | 4941A (transport) | en_cours | 2025-07-10 |
| 80 | ESSOR INGENIERIE | 7112B (ingénierie) | en_cours | 2025-07-29 |

## Nouvelles Opportunites (annonces AJ)

**1 128 annonces scrapées** ce matin à 05h07 depuis 23 sources AJ.
Pas de score de pertinence calculé (LLM scoring non activé lors du scrape).

### Top 3 à traiter en urgence (deadline < 7j)

1. **BP METAL** (AjIRE) -- 34 salariés -- deadline **2026-04-30** (dans 2 jours)
   Secteur industriel, effectif significatif. Vérifier SIREN + lancer enrichissement.

2. **Fonds de Commerce -- restaurant/commerce** (Trajectoire) -- deadline **2026-04-30**
   Secteur non précisé, à qualifier manuellement.

3. **VEILLAT** (AJ UP) -- 1 salarié -- CA 216 K€ -- deadline **2026-04-30**
   Trop petit pour le pipeline prioritaire.

**Total deadlines < 7 jours : 35** dont la majorité TPE (< 5 salariés).

## Deadlines Proches

| Date limite | Entreprise | Source AJ | Effectif | CA |
|-------------|-----------|----------|---------|-----|
| 2026-04-29 | (sans nom) | AJ UP | 3 | - |
| 2026-04-30 | LES AFFRANCHIS | AJ UP | 5 | - |
| 2026-04-30 | VEILLAT | AJ UP | 1 | 216 K€ |
| 2026-04-30 | Fonds de Commerce | Trajectoire | - | - |
| 2026-04-30 | BP METAL | AjIRE | 34 | - |

35 procédures au total avec deadline avant le 05/05/2026.

## Actions Recommandees

| Priorité | Action | Impact | Effort |
|---------|--------|--------|--------|
| P1 | Contacter mandataire pour BP METAL (deadline 30/04) | Deal potentiel + 34 salariés | 30 min |
| P1 | Lancer teaser Writer sur top 5 deals avec analyse | Débloquer 392 teasers en attente | Pipeline agent |
| P2 | Activer LLM scoring (`--llm`) sur prochain scrape AJ | Prioriser les 1 128 annonces | Script |
| P2 | Enrichissement Pappers sur BRANDT FRANCE + IDKIDS + API TECH | Compléter données financières top 3 | ~30 req Pappers |
| P3 | Vérifier pourquoi auto-enrichment-2026-04-28.md absent | Infrastructure monitoring | 10 min |

## Metriques

| Indicateur | Valeur | Objectif | Statut |
|-----------|--------|---------|--------|
| Annonces scrapées/jour | 1 128 | > 20 nouvelles | OK (volume) |
| Procédures actives scorées | 89 630 | -- | OK |
| Score moyen DB | 37/100 | -- | Faible |
| Score max DB | 84/100 | -- | Cible atteinte |
| Deals avec teaser | ~2/394 | > 5 | KO |
| Rapport enrichissement | Absent | Quotidien | KO |
| Sources AJ couvertes | 23/40 | 40 | Partiel |

---
*Généré automatiquement le 2026-04-28 | Sources : aj_annonces.json (scrape 05h07) + PostgreSQL brantham + workspace deals*
## Related
