---
type: batch-log
batch: 12
agent: claude-agent (opus 4.7 1M)
date: 2026-05-15
dossiers_traites: ["NEW-MINELLI", "NEW-PETRUS", "09", "GM_IMMO", "34"]
nb_offres_extraites: 33
nb_dossiers_extraits: 5
tags: [tc-paris, extraction, batch-12]
---

# Batch 12 — TC Paris extraction

## Périmètre

5 dossiers prioritaires incluant deux cas iconiques :
- **NEW-MINELLI** : LIQUIDATION confirmée 13/05/2026 — contre-exemple cherry-picking refus tribunal
- **34 SAS COSA** : Agence IF GAGNANTE confirmée 05/03/2026 — décortique déjà existant

## Livrables

- 5 dossiers JSON dans `grilles/dossiers/`
- 33 offres JSON dans `grilles/offres/`
- Renommage `dossiers/09.json` → `dossiers/AMIRAL_MAIGRET.json` (collision dossier_id résolue)

## Findings clés

1. **MINELLI** — pattern de refus confirmé : 6 offres dont 5 partielles (4 droits au bail isolés + 1 plan partiel digital Baghaira 9/86 emplois) + 1 globale plancher Sayada PP sans véhicule. Total tribunal refusé en bloc → fermeture 30/05/2026. Reproduit le pattern Minelli déjà documenté dans `gagnants-tribunal.md`.

2. **COSA** — Agence IF GAGNANTE (70k€/16 emplois) vs DATASOLUTION perdant (50k€/28 emplois). Validé contre `decortique-offres-gagnantes.md`. Pattern : prix encaissable supérieur + 13 pages sobres + 3 CS classiques + absorption droits CP intégrale > 25 pages denses + charges augmentatives masquées 745k€ + clauses non-sollicitation imposées aux 4 anciens dirigeants.

3. **PETRUS** — dossier resto haut de gamme avec conflit d'intérêts notable : Gilles MALAFOSSE (7 RODIER/Loulou Groupe) cumule rôle de repreneur ET de bailleur (SCI Petrus Immobilier). Litige marque "Petrus" interdit pour vin (TJ Paris 30/01/2026). Offre SBM/Berkeley exclut explicitement nom Petrus de la reprise — reconnaissance perte valeur marque. Issue en attente.

4. **EZIN & STRAUUS** — pattern reprise interne par salariés (DODO/LIGOT/TOTIER) vs reprise par scaler (OTSAR). Trio interne offre 70k€/7 emplois (intégralité) + EZIN consultant + aucune CS, vs OTSAR 25k€/3 emplois + intégration locaux 17e mais perte adresse Haussmann. Pattern classique en EC : tribunal favorise souvent l'interne en EC quand cohérence financière démontrée. Issue en attente.

5. **GM IMMO** — dossier mono-SCI dans consolidé FHBX 'Affaire Balthazar' 26 entités. Offres globales multi-SCI (MUVICO 400k€, VERDOSO) vs offres dédiées single-actif (HOUSEBASE). Plusieurs PDFs >5MB non extraits — confidence "low/medium" sur GM_IMMO-03/04/05/06/07. PDF-01 mal classé (vise SNC ADONIA pas GM IMMO).

## Anomalies

- **MINELLI offre 05 (Baghaira)** : seul plan partiel chiffré sérieux (300k€, BP 3 ans, 9 emplois). Modèle digital pure-play sur marque retail historique = pari risqué. Repreneur 24 ans (Augustin DUFAURE DE LAJARTE), groupe Baghaira FR 5M€. Tribunal a rejeté car couverture sociale insuffisante (10,5%).
- **PETRUS offres 04 et 05** : trame identique (mêmes prix, mêmes valeurs L.642-12 682 112€) — agence Century 21 Horeca Paris a recyclé template entre 2 clients (Daunou 9 et Noura Beaugrenelle). Signal de standardisation des offres restauration.
- **EZIN offre 03** : document non-offre (état des privilèges OTSAR du Greffe TAE Paris) — pièce annexe au dossier OTSAR.
- **EZIN offre 07** : PDF FIDUCIAIRE VALUE scanné/image — OCR nécessaire pour récupérer prix/périmètre/CS.

## Suggestions

1. OCR systematique des PDFs scannés (FIDUCIAIRE VALUE — EZIN-07).
2. Re-extraction des PDFs MUVICO/VERDOSO >5MB sur GM_IMMO pour ventilation par entité.
3. Suivre BODACC mai-juin 2026 pour PETRUS et EZIN & STRAUUS (audiences en attente).
4. Le pattern Century 21 Horeca Paris (template recyclé sur Petrus 04+05) mérite d'être indexé comme `patterns/agence-template-recycle.md` — signal négatif pour évaluer offres restauration.

## Related

- [[brantham/tc-paris-extraction/_MOC]]
- [[brantham/tc-paris-extraction/analyses/gagnants-tribunal]]
- [[brantham/tc-paris-extraction/analyses/decortique-offres-gagnantes]]
- [[brantham/tc-paris-extraction/grilles/_workflow]]
