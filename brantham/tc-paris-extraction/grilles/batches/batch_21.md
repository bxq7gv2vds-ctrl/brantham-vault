---
type: extraction-batch
project: brantham
created: 2026-05-15
batch_id: 21
dossiers_assigned: ["11", "17", "63"]
tags: [tc-paris, extraction, batch]
---

# Batch 21 — Dossiers 11, 17, 63 (gros dossiers)

## Fichiers produits

### Grilles dossier (3)
- `dossiers/ATELIER_MONTREUIL.json` — SCI L'ATELIER DE MONTREUIL (immo, portefeuille FHBX Foncière Melot Gouband 26 entités, 13 offres)
- `dossiers/HENRI_GINOUX.json` — SCCV 121 HENRI GINOUX (immo, même portefeuille FHBX, 13 offres dont 1 AEB INVEST dédiée 800k€)
- `dossiers/63.json` — Federation Unie des Auberges de Jeunesse / FUAJ (LJ poursuite, CA 30,6M€, 317 ETP, 40 sites, 14 offres très diversifiées)

### Grilles offres (40)
- `offres/ATELIER_MONTREUIL-01.json` à `ATELIER_MONTREUIL-13.json` (13 offres)
- `offres/HENRI_GINOUX-01.json` à `HENRI_GINOUX-13.json` (13 offres)
- `offres/63-01.json` à `63-14.json` (14 offres)

**Total: 43 fichiers JSON produits (3 dossiers + 40 offres).**

## Anomalies & manques systémiques

### Dossiers 11 & 17 (FHBX portefeuille immo)
- **PDFs MUVICO >5MB non extraits** : offres 2/3/4/5/6 d'ATELIER_MONTREUIL et 2/3/6 d'HENRI_GINOUX. Confidence `partial_pdf_only`. Données issues du CSV INSULA de référence (table prix MUVICO initiale 09/02/2026 vs améliorée 02/03/2026).
- **HOUSEBASE mal classé** : ATELIER_MONTREUIL-01 et HENRI_GINOUX-09 sont des copies physiques d'offres HOUSEBASE qui ciblent SNC ADONIA (501 600€ Cachan). PDFs hors périmètre — marqués `cette_offre_retenue: "non"` avec motif explicite.
- **VERDOSO double docusign** : 2 PDFs distincts par dossier (CC859BA0 + EBE6E276) = même repreneur, offre globale 26 entités, prix individualisé non extrait.
- **Type UNKNOWN** : HENRI_GINOUX-01, -03, -04 + ATELIER_MONTREUIL-07 / -04 = type non reconnu lors du scrape automatique. Confidence `partial_pdf_only`, à retraiter manuellement.
- **Pattern AEB INVEST** : sur HENRI_GINOUX, AEB INVEST propose 800k€ en offre dédiée vs MUVICO 200k€ globale améliorée = **prix x4 sur l'actif Montrouge**. Signal compétition forte.

### Dossier 63 (FUAJ — riche)
- **CSV très complet** : 14 offres avec données détaillées (sauf offre 63-12 dont CSV est vide — confirmé après lecture directe PDF que c'est un doublon physique de 63-07, même AAG56 sur Île de Groix).
- **Offre la plus haute** : ADRET 1365 (Adrien LEMAIRE + Ferdinand MARTINET ex-Chilowe + Josselin GRANIER) — projet TRAVERSE maisons d'aventures — **1 830 000€** sur 3 sites montagne premium (Mont-Dore + La Clusaz + Serre-Chevalier).
- **Concurrence frontale sur Nice Camelias** : 4 offrants distincts
  - ATALANTE HOTELS 500k€ (250+250) — opérateur 31 hôtels 2600 chambres
  - Delaforge volet Nice ~250k€ (sur offre globale 500k€ avec Paris YR + D'Artagnan)
  - Femina Styl 200k€ — famille HUBLE diversifiée
  - Cosmiques 200k€ — Gabriel ECALLE (entrepreneur VOLTAIRE vélos électriques)
- **Concurrence frontale sur Mont-Dore/La Clusaz/Serre-Chevalier** : ADRET 1365 (1,83M€ dédié 3 sites) vs BRAXTON (100k€ offre globale 9+14 sites).
- **Pattern atypique** : ADVI PROM 1€ symbolique sur 7 sites + **charge augmentative 457 300€** (créances clients déclarées) + 75 emplois repris + BP solide (6,9M€ CA an 3, EBITDA 467k€). Démontre que prix nominal ≠ valorisation réelle.

### Doublons physiques
- AAG56 sur Île de Groix : 63-07 et 63-12 sont 2 copies physiques de la même offre (Joëlle Le Prioux, 1€, lettre 2 pages + statuts).
- HOUSEBASE sur SNC ADONIA : 11_offre1 et 17_offre5 = mêmes PDFs mal classés.

## Champs prioritaires renseignés

| Champ | ATELIER_MONTREUIL (13) | HENRI_GINOUX (13) | 63 FUAJ (14) | Total (40) |
|---|---|---|---|---|
| `issue_dossier.cette_offre_retenue` | 13/13 (12 "en_attente", 1 "non" HOUSEBASE) | 13/13 (12 "en_attente", 1 "non" HOUSEBASE) | 14/14 ("en_attente") | 40/40 |
| `profil_repreneur.forme` | 11/13 (2 UNKNOWN) | 9/13 (4 UNKNOWN) | 14/14 | 34/40 |
| `structure_prix.prix_total_eur` | 1/13 (LABRAX 21M€) | 4/13 (AEB 800k, MUVICO 3x) | 14/14 | 19/40 |
| `volet_social.pct_reprise` | 0/13 (immo sans salariés) | 0/13 (immo sans salariés) | 12/14 | 12/40 |
| `conditions_suspensives.aucune_cs` | 13/13 | 13/13 | 14/14 | 40/40 |
| `plan_industriel.diagnostic_qualification` | 13/13 | 13/13 | 14/14 | 40/40 |
| `signaux_faibles.faculte_substitution_precise` | 13/13 | 13/13 | 14/14 | 40/40 |
| `extraits_remarquables.phrase_positionnement` | 13/13 | 13/13 | 14/14 | 40/40 |

## Gagnants connus
Aucun des 3 dossiers ne figure dans `gagnants-tribunal.md`. Tous en attente. Pas de croisement.

## Suggestions

1. **Re-extraire PDFs MUVICO >5MB** (ATELIER_MONTREUIL offres 2-6, HENRI_GINOUX offres 2-3-6) via PageIndex/OCR pour récupérer ventilation par entité.
2. **Identifier les 4 PDFs UNKNOWN** (HENRI_GINOUX 1/3/4 + ATELIER_MONTREUIL 7) — vérifier OCR ou re-scraper.
3. **Suivre audience Foncière Melot Gouband (Affaire Balthazar)** : DLDO 02/03/2026, décision tribunale probablement globale au gré de l'arbitrage LABRAX (21M€ portefeuille) vs MUVICO/VERDOSO/JADO/HOUSEBASE/AEB ventilés.
4. **Suivre FUAJ** : DLDO 04/04/2026, audience probable mai/juin 2026. **Enjeu majeur** = arbitrage entre offres globales (BRAXTON 23 sites, ADVI PROM 7 sites + 457k charge aug) et offres sectorielles partielles (Nice Camelias 4 offrants, Mont-Dore 1,83M€ ADRET 1365).
5. **Cas FUAJ utile pour Phase 2** : 14 offres très diversifiées (asso historique 1€, collectivité 70k€, opérateur hôtelier 500k€, holding patrimoniale 200k€, fonds d'investissement 100k€ globale 23 sites, marchand de biens 3k€ dispersé, lettre d'intention co-invest immo, projet entrepreneurial 1,83M€). Bibliothèque de cas pour matrices de scoring.
6. **AEB INVEST pattern** : x4 sur offre dédiée vs offre globale même portefeuille — à creuser pour patterns de pricing immo en plan de cession.

## Récap (<100 mots)

43 grilles JSON produites pour 3 gros dossiers (11 ATELIER_MONTREUIL, 17 HENRI_GINOUX, 63 FUAJ), 40 offres au total. Les 2 SCI immo (portefeuille FHBX consolidé 26 entités Affaire Balthazar) sont confidence partielle : PDFs MUVICO >5MB non extraits, 4 types UNKNOWN, 2 HOUSEBASE mal classés. Le dossier FUAJ est confidence haute : CSV très riche, 14 offres très diversifiées (1€ AAG56 à 1,83M€ ADRET 1365), bibliothèque idéale pour Phase 2. Patterns clés : AEB INVEST x4 prix dédié vs global, concurrence frontale 4 offrants Nice Camelias, ADVI PROM 1€ symbolique + 457k€ charge augmentative.

## Related

- [[brantham/tc-paris-extraction/_MOC]]
- [[brantham/tc-paris-extraction/grilles/batches/batch_06]]
- [[brantham/tc-paris-extraction/analyses/gagnants-tribunal]]
- [[brantham/tc-paris-extraction/analyses/decortique-offres-gagnantes]]
