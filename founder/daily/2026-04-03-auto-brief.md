---
type: daily-brief
date: 2026-04-03
generated: auto
---

# Brief Matinal -- 2026-04-03

## Pipeline

**Base DB** : 87 203 procedures actives (en_cours + plan_en_cours) — 89 630 scorees.

**Deals workspace** : 149 dossiers actifs

| Statut | Nb | %  |
|--------|----|----|
| Avec analyse | 123 | 83% |
| Avec acheteurs | 99 | 66% |
| Avec enrichissement | 137 | 92% |
| Avec teaser | 0 | 0% |

Valeur estimee pipeline : non calculee (enrichissement CA incomplet sur la majorite des dossiers).

---

## Nouvelles Opportunites

Scrape 02/04 : **460 annonces**, 31 sites (24 ok, 6 vides, 1 erreur). Source dominante : 2M&Associes (193 annonces).
Types : cession 340 (74%), redressement 113 (25%), liquidation 4, sauvegarde 3.
Qualification LLM desactivee — aucun score_pertinence disponible.

**Top 3 opportunites identifiables par CA declare :**

1. **SAS RECOMAT DISTRIBUTION** (Meynet) — CA 1 972 310 EUR, cession, deadline 17/04.
   Deal deja en workspace (meynet-sas-recomat-distribution) : analyse ok, acheteurs ok, teaser manquant.

2. **SOHNEJ** (AJRS) — CA 1 533 000 EUR, redressement, deadline 17/04.
   Deal deja en workspace (ajrs-sohnej) : analyse ok, acheteurs ok, teaser manquant.

3. **MONTE CARLO SNC** (Meynet) — CA 881 000 EUR, cession, deadline 08/04 (dans 5 jours).
   Deal deja en workspace (meynet-monte-carlo-snc) : analyse ok, acheteurs ok, teaser manquant.

---

## Deadlines Proches

**Aujourd'hui (03/04) — 4 expirations imminentes :**

| Entreprise | Source | Type | Workspace |
|------------|--------|------|-----------|
| TECH POWER ELECTRONICS | AJRS | Redressement | Non |
| THIERRY BEURON / TRANSFRIGO 11 SAS | FHBX | Cession | Non |
| Fonds de commerce - Maisons Laffitte | Asteren | Cession | Non |
| Materiel ou mobilier - GAMBAIS | Asteren | Cession | Non |

**Dans 7 jours (jusqu'au 10/04) — 6 deadlines supplementaires :**

| Date | Entreprise | Source | CA | Workspace |
|------|------------|--------|----|-----------|
| 08/04 | Groupe de formation (cession + parts) | AJRS | - | Non |
| 08/04 | MONTE CARLO SNC | Meynet | 881k EUR | Oui |
| 09/04 | Fonds de commerce - Deuil la Barre | Asteren | - | Non |
| 10/04 | GERARD VACHER ENTREPRISES | FHBX | - | Non |
| 10/04 | LES JARDINS D'OLIVIER | FHBX | - | Non |
| 10/04 | Autres incorporels - Saint-Ouen | Asteren | - | Non |

Total 7 jours : **10 deadlines** dont 4 aujourd'hui.

---

## Actions Recommandees

**Priorite critique (aujourd'hui) :**

1. **Generer les teasers** — 0 teaser sur 149 deals. Les 3 deals avec CA identifie et deadline proche (MONTE CARLO, SOHNEJ, RECOMAT) sont prets : analyse + acheteurs en place. Commande : `generate_teaser.py --slug meynet-monte-carlo-snc`.

2. **Traiter les 4 deadlines expirees aujourd'hui** — TECH POWER ELECTRONICS et TRANSFRIGO 11 non dans le workspace. Ajouter au pipeline ou declasser.

**Priorite haute (cette semaine) :**

3. **Analyser les 26 deals bloques** (sans analyse ni teaser ni acheteurs) — purgez les non-qualifies ou relancez l'Analyst sur les deals avec enrichissement disponible.

4. **Activer qualification LLM** sur les 460 annonces AJ — score_pertinence null sur l'integralite du feed. Commande : `scraper_aj.py --llm`.

5. **Completer les 50 deals sans acheteurs** — lancer matching 4D sur les deals avec analyse disponible.

**Priorite normale :**

6. Enrichir les 12 deals sans donnees financieres (Pappers, attention rate limit 100 req/jour).

---

## Metriques

| Indicateur | Valeur | Objectif | Ecart |
|------------|--------|----------|-------|
| Opportunites detectees (scrape 02/04) | 460 | > 20/jour | OK |
| Deals en workspace actif | 149 | > 5 | OK |
| Teasers generes | 0 / 149 | 100% | CRITIQUE |
| Taux enrichissement financier | 92% | > 80% | OK |
| Taux couverture acheteurs | 66% | > 80% | A ameliorer |
| Score moyen DB | 37 / 100 | -- | -- |
| Score max DB | 84 (BRANDT FRANCE) | -- | -- |
| Procedures actives DB | 87 203 | -- | -- |
| Enrichissement session matinale | Partiel (01h07, 456 opp) | Complet | Incomplet |

**Top 3 procedures DB par score :**
1. BRANDT FRANCE — 84 — NAF 2751Z — en_cours depuis 2025-10-01
2. STAR'S SERVICE — 82 — NAF 4941B — en_cours depuis 2025-01-30
3. API TECH — 82 — NAF 2899B — en_cours depuis 2025-07-03

---

## Related

- [[brantham/_MOC]]
- [[founder/daily/2026-04-03]]
