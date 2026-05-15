---
type: batch_log
project: brantham
batch: 18
created: 2026-05-15
tags: [tc-paris, extraction, batch, fhbx, melot-gouband, balthazar]
---

# Batch 18 — DANTON (04) + ADONIA (05) + MARCEL BONNET (20)

## Dossiers traites

| Dossier | Folder | Nb offres extraites | Confidence |
|---|---|---|---|
| 04-DANTON | 04 - SCI DANTON - LILAS | 10 | high (DANTON-06 VERDOSO + DANTON-10 AEB) / medium (CORTONA, MUVICO, IMMOBAIL via cross-ref) / low (HOUSEBASE mal classe, OCR scanne, JADO certificat) |
| 05-ADONIA | 05 - SNC ADONIA | 10 | high (ADONIA-10 AEB lu) / medium (IMMOBAIL, HOUSEBASE, MUVICO via CSV cross-ref) / low (OCR scanne, JADO Docusign) |
| 20-MARCEL_BONNET | 20 - SCI 60 RUE MARCEL BONNET | 10 | high (MARCEL_BONNET-10 AEB 2,5M lu + bail SIDEXA 2029 + permis bureau-vers-logement) / medium (LABRAX) / low (4 MUVICO PDFs >5MB, 1 UNKNOWN) |

**Total : 30 offres + 3 fiches dossier = 33 JSONs ecrits.**

## Anomalie d'identifiant

`dossiers/20.json` existait deja pour SYM TECH (dossier 20 distinct dans une autre numerotation). Pour eviter collision j'ai utilise des IDs suffixes :
- `dossiers/04-DANTON.json`, `dossiers/05-ADONIA.json`, `dossiers/20-MARCEL_BONNET.json`
- Offres : `DANTON-01..10`, `ADONIA-01..10`, `MARCEL_BONNET-01..10`

Recommandation Phase 2 : reconcilier ce point au moment de l'agregation (rename ou ajout d'un champ `dossier_alias`).

## Cle dossier FHBX Melot/Gouband (meta-dossier)

**Les 3 dossiers font partie du meme meta-dossier consolide** : "Foncieres Melot Gouband / Affaire Balthazar" — 26 entites en RJ ouvertes par jugements 29/04, 03/07, 04/09, 23/12/2025. Groupe de fait constitue par MM. Dominique MELOT et Francois-Regis GOUBAND depuis 1997. Causes structurelles communes :
- Crise immobiliere 2022 (taux 1% -> 4% en 2023, transactions IDF -39% en 2023)
- Endettement crowdfunding + institutionnel non refinancable
- Balthazar Invest (porteuse de la dette externe) RJ 20/02/2025 sur assignation societe de crowdfunding
- 43 autres entites RJ entre avril et decembre 2025

Tous les dossiers FHBX 04/05/20/09/30/12/etc. partagent le meme tribunal (TAE Paris), AJ (BOURBOULOUX FHBX), MJ (LELOUP-THOMAS MJA), JC (PONCET), et DLDO commun 02/03/2026.

## Offres globales partagees (a referencer dans Phase 2)

Sept candidats reapparaissent sur **DANTON + ADONIA + MARCEL_BONNET + autres SCI FHBX** :

| Candidat | Forme | Prix portfeuille | Modus operandi |
|---|---|---|---|
| VERDOSO SAS | Fonds PE (Ullmann) - cap 3,2M EUR | 250 002 EUR (9998/SCI) + valo 10,2M EUR a parfaire | Diagnostic structurel rigoureux 3 axes risque (vacance, cash-flow, CAPEX). 50M EUR dispo. Track record Compte R/Kooples/Geismar. **Aucun salarie repris.** 25 pages + executive summary. |
| LABRAX INVEST | Holding ad hoc | 21M EUR portfolio 26 + appart Paris 16 | "Finale, ferme, indivisible" sous garanties usuelles. Pas de prix individualises. |
| MUVICO (Victor COHEN) | Foncier patrimonial Paris 16 | Variable par SCI (DANTON 520->555k, ADONIA 520 fige) | Multi-PDFs >5MB non extraits. Amelioration entre initiale et DLDO 02/03 pas systematique. |
| CORTONA FRANCE (Molimard / de Haseth-Moller) | EURL/SARL, foncier 1985 FR-NL | Multi-actifs FMG 27 biens | Sous CS - prix individualises non extraits. |
| AEB INVEST (EL Bounaamani) | SAS holding cap 2k EUR | Dediee par SCI (DANTON 720k, ADONIA 650k, MARCEL_BONNET 2,5M) | Lettre INDICATIVE 4 pages. Plus haute offre dediee sur chaque actif. Aucune surete a charge. Mais "ne saurait constituer un engagement ferme d'acquerir". 3 CS dont visite + accord doc + absence MAC. |
| Groupe JADO + PARTNER CONSULTANCY | Consultancy + groupe | Balthazar VMoncey | PDF principal 23p non extrait (certificats Docusign seuls). Avocat Moncey Avocats - Augustin LACCOURS. |
| IMMOBAIL (Jean-Pierre TULLE) | SAS Fontainebleau 25 ans | 500k ADONIA + 750k DANTON + 750k ATELIER URBAIN + 500k JEAN RENAUDIE + 1,5M OKABE | Fonds propres documentes (benefice 2024 1,2M + filiale SCI ARTU 950k). Aucune CS de financement. **Strategie 'bon pere de famille'.** |
| HOUSEBASE (Philippe ZERR) | SAS Rennes cap 49,8k | 501,6k ADONIA dediee | **Offre ferme et irrevocable sans CS de financement**, tenant compte des diligences techniques (toiture champignons, facade fissures, ecart surface). Visite faite. |

## Anomalies detectees

1. **HOUSEBASE PDFs mal classes** : ADONIA-01 (cible reellement ADONIA), DANTON-01 et MARCEL_BONNET-01 (PDFs HOUSEBASE physiquement copies dans les mauvais dossiers — cible ADONIA dans tous les cas, 501 600 EUR).
2. **PDFs scannes illisibles** : DANTON-02 et ADONIA-04 — OCR a effectuer pour analyse de ces offres.
3. **PDFs Docusign uniquement** : DANTON-07 (JADO certificat F0153B8A), DANTON-09 (D2E8DBF3), ADONIA-09 (D2E8DBF3) — le corps de l'offre n'est pas dans le PDF extrait, seulement le certificat de signature.
4. **PDFs >5MB non extraits** : MARCEL_BONNET-04/05/06/07 (4 PDFs MUVICO), ADONIA-06/07, DANTON-04/05 — probablement la meme offre globale MUVICO dupliquee/versionnee.
5. **VERDOSO prix individualises par SCI uniformes** : 9998 EUR immeuble + 1 EUR/1 EUR incorporels/corporels = 10 000 EUR par entite ; 25 SCI x 10k = 250 000 EUR + 2 EUR = 250 002 EUR total. Verbatim : "prix de cession degrade ... a parfaire lors de l'amelioration ... rapprocher de la valorisation economique definitive [10,2M EUR]".
6. **MUVICO ADONIA fige** : 520k initiale = 520k amelioree (vs DANTON 520k -> 555k). Signal de manque d'appetit pour ADONIA dans le panier MUVICO.
7. **MARCEL BONNET est l'actif phare a risque** selon VERDOSO : SIDEXA option sortie aout 2026 (<6 mois), +188k EUR impayes/an, loyer facial +25% au marche, CAPEX remise aux normes lourde requise, +20% vacance Cushman & Wakefield premiere couronne sud.

## Suggestions Phase 2

1. **Traiter les 26 entites FHBX comme un meta-dossier consolide** (cf. recommandation deja faite en batch 22 pour AMIRAL MAIGRET et ADELE FIRMIN). Croiser DANTON + ADONIA + MARCEL_BONNET + AMIRAL MAIGRET + ADELE FIRMIN + INSULA + LE LOFT + COROT + autres SCI. Mapper qui prend quoi dans le portefeuille 21M EUR LABRAX vs 26 individuels VERDOSO vs offres dediees par actif.

2. **Pattern VERDOSO "prix degrade L.642-2 V"** = recette rhetorique reutilisable. Le repreneur depose une offre prix derisoire en s'appuyant sur l'article L.642-2 V (l'offre ne peut etre modifiee que dans un sens favorable, donc le repreneur a interet a sous-payer et ameliorer). A documenter dans `vault/brantham/patterns/cession-prix-degrade-L642-2-V.md`.

3. **Arbitrage prix vs serieux sur ADONIA** : AEB INVEST 650k vs HOUSEBASE 501,6k. AEB +30% vs HOUSEBASE mais HOUSEBASE est "ferme et irrevocable sans CS" tandis qu'AEB est "indicative et avec 3 CS". Cas d'ecole pour le TAE : prefere-t-il le prix ou la certitude d'execution ?

4. **Marcel Bonnet le test critique** : seul actif > 1M dans ce trio, avec 1 seule offre dediee fiable (AEB 2,5M) + 4 PDFs MUVICO non extraits. Si AEB se retire en due diligence (CS visite + MAC), reste LABRAX 21M global et MUVICO. Phase 2 : verifier si MUVICO a une portion Marcel Bonnet >2,5M.

5. **VERDOSO refus reprise salaries** = signal anti-social fort. Verbatim : "Aucun salarie n'a ete porte a la connaissance du Repreneur. En tout etat de cause, le Repreneur n'entend pas reprendre a ce stade d'eventuels contrats de travail." Sur ces SCI sans salaries c'est neutre, mais le pattern Verdoso pourrait penaliser sur d'autres dossiers FHBX avec salaries (SC Balthazar et Idefisc qui ont du personnel).

6. **Champ `dossier_consolide_fhbx`** a introduire dans le schema pour Phase 2 — permettre les regroupements automatiques sur les 26 entites.

## Recap (<100 mots)

30 offres + 3 fiches dossier extraites pour batch 18 : DANTON LILAS, SNC ADONIA, SCI 60 RUE MARCEL BONNET — toutes 3 SCI/SNC du dossier consolide FHBX Foncieres Melot Gouband (26 entites RJ). Memes 8 candidats recurrents (VERDOSO 250k+valo 10,2M / LABRAX 21M global / MUVICO multi-PDFs / CORTONA / AEB INVEST dediees 720k+650k+2,5M / JADO+Moncey / IMMOBAIL multi-actifs 4M / HOUSEBASE 501,6k ferme). Pattern decouvert : VERDOSO prix "degrade L.642-2 V" 9998 EUR/SCI. Marcel Bonnet = actif phare a risque (SIDEXA bail expire 2026, loyer +25% marche, CAPEX lourd). 11 anomalies signalees (PDFs mal classes, scanned, >5MB, Docusign-only).

## Related

- [[brantham/_MOC]]
- [[brantham/tc-paris-extraction/_MOC]]
- [[brantham/tc-paris-extraction/grilles/_schema]]
- [[brantham/tc-paris-extraction/grilles/_workflow]]
- [[brantham/tc-paris-extraction/grilles/batches/batch_22]]
- [[brantham/tc-paris-extraction/analyses/decortique-offres-gagnantes]]
- [[brantham/tc-paris-extraction/analyses/gagnants-tribunal]]
