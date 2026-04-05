---
type: daily-brief
date: 2026-04-05
generated: auto
---

# Brief Matinal -- 2026-04-05

## Pipeline

- Procedures actives en base : **87 324** (78 597 en_cours + 8 727 plan_en_cours)
- Procedures closes : 99 453
- Deals workspace : **179 dossiers** au total
- Score moyen DB : 37/100 | Score max : 84 (BRANDT FRANCE)
- Enrichissement financier : 0 Pappers aujourd'hui (pas de SIREN dans les annonces AJ)

### Top 5 procedures actives par score

| Raison sociale | Score | NAF | Effectif | Statut | Ouverture |
|---|---|---|---|---|---|
| BRANDT FRANCE | 84 | 2751Z (gros electromenager) | 500-999 | en_cours | 2025-10-01 |
| API TECH | 82 | 2899B (machines speciales) | 250-499 | en_cours | 2025-07-03 |
| CLINIQUE CHAMPS ELYSEES | 82 | 8610Z (clinique) | 50-99 | plan_en_cours | 2025-12-01 |
| STAR'S SERVICE | 82 | 4941B (transport) | 2000-4999 | en_cours | 2025-01-30 |
| IDKIDS | 82 | 7010Z (holding) | 10-19 | en_cours | 2026-02-03 |

## Nouvelles Opportunites

Scrape du jour : **457 annonces** (24 sites OK / 1 erreur BVP SSL / 6 vides). 311 sans dossier existant.

### Top 3 a traiter en priorite (session auto-enrichment 02:58)

**1. BS OUTDOOR** — `aj-specialises-bs-outdoor`
- Secteur : equipements outdoor (tentes de toit)
- CA : 2,1 M€ | Analyse: faite | Teaser: manquant | Acheteurs: identifies
- Signal fort : produit differencie, marche porteur

**2. Chantier naval Bormes-les-Mimosas** — `aj-specialises-1937-chantier-naval-a-bormes-les-mimosas`
- Secteur : nautisme / reparation navale
- CA : 1,3 M€ | Analyse: faite | Teaser: manquant | Acheteurs: identifies
- Signal : actif rare (chantier naval en Mediterranee), actifs corporels importants

**3. PROFAST** — `aj-specialises-profast`
- Secteur : transport messagerie
- CA : 1,1 M€ | Analyse: faite | Teaser: manquant | Acheteurs: identifies
- Signal : CA declare, secteur avec repreneurs actifs

## Deadlines Proches

6 annonces AJ avec date limite dans les 7 prochains jours :

| Date | J+ | Entreprise | CA | Source |
|---|---|---|---|---|
| 2026-04-08 | J+3 | Groupe de formation (cession fonds + participation) | n.c. | AJRS |
| 2026-04-08 | J+3 | MONTE CARLO SNC | 881 k€ | Meynet |
| 2026-04-09 | J+4 | Fonds de commerce Deuil-la-Barre | n.c. | Asteren |
| 2026-04-10 | J+5 | Incorporels Saint-Ouen | n.c. | Asteren |
| 2026-04-10 | J+5 | GERARD VACHER ENTREPRISES (GVE) | n.c. | FHBX |
| 2026-04-10 | J+5 | LES JARDINS D'OLIVIER | n.c. | FHBX |

Urgence immediate : MONTE CARLO SNC (CA declare, J+3) et groupe de formation AJRS (J+3).

## Actions Recommandees

| Priorite | Action | Impact |
|---|---|---|
| 1 - Urgent | Contacter mandataire MONTE CARLO SNC avant le 08/04 | Revenue potentiel, deadline 3 jours |
| 2 - Urgent | Contacter mandataire groupe formation AJRS avant le 08/04 | Deadline 3 jours |
| 3 - Haute | Generer teasers pour BS OUTDOOR, PROFAST, Chantier naval Bormes | 0 teaser dans les 179 dossiers |
| 4 - Haute | Relancer FastAPI (localhost:8000 down) | Bloque matching 4D repreneurs |
| 5 - Moyenne | Lancer analyse sur 26 dossiers sans analyse | Pipe incomplet |
| 6 - Moyenne | Recuperer SIRENs des annonces AJ pour enrichissement Pappers | Taux enrichissement = 0% aujourd'hui |

Commande relance FastAPI :
```
cd /Users/paul/Desktop/brantham-partners/api && source .venv/bin/activate && uvicorn main:app --host 0.0.0.0 --port 8000
```

## Metriques

| Metrique | Valeur | Objectif |
|---|---|---|
| Opportunites scrapees | 457 (31 sites) | > 20 nouvelles/j |
| Nouvelles sans dossier | 311 | -- |
| Dossiers traites ce matin | 10 | -- |
| Score moyen DB | 37/100 | -- |
| Score max actif | 84 (BRANDT FRANCE) | -- |
| Taux enrichissement Pappers | 0% | > 80% sur score > 50 |
| Teasers generes | 0 / 179 dossiers | > 0 |
| Acheteurs identifies | 129 / 179 dossiers | -- |
| Deals sans analyse | 26 / 179 | -- |
| Infrastructure | FastAPI down / PG OK / Redis n.v. | 99% uptime |

## Related

[[brantham/_MOC]]
[[brantham/sessions/auto-enrichment-2026-04-05]]
[[founder/daily/2026-04-05]]
