---
type: batch-log
batch: 10
dossiers: ["29-RHEA", "31-OCCITANIE", "33-S2NE", "35-DME", "35-SICA"]
date: 2026-05-15
extracted_by: claude-agent
tags: [tc-paris, extraction, batch-10]
---

# Batch 10 — Extraction grilles TC Paris

## Synthese executive

| Dossier | Folder | Offres | Issue | Repreneur retenu |
|---|---|---|---|---|
| 29-RHEA | 29 - SCI RHEA | 6 | en_attente | MUVICO probable (offre globale FHBX, portion RHEA 9,5k) |
| 31-OCCITANIE | 31 - SAS ALPHA CAMPING OCCITANIE | 6 | plan_cession_arrete | SEASONOVA (Lemarchand) sur ALPHA + MAEVA franchises |
| 33-S2NE | 33 - SA SOCIETE NOUVELLE DU NOUVEL ECONOMISTE | 6 | en_attente | NR — Frontline Media (Groupe mind) le plus structure |
| 35-DME | 35 - SARL DME | 3 | en_attente | NR — 3 offres tres heterogenes |
| 35-SICA | 35 - Société d intérêt collectif agricole par actions s | 6 | plan_cession_arrete | LES VERGERS D'ANJOU (cooperative) — offre amelioree 7,04M 28 emplois |

**Total : 5 dossiers + 27 offres extraites.**

## Methode

1. Lecture `_schema.json` + `_workflow.md` + `gagnants-tribunal.md` + `decortique-offres-gagnantes.md` (extrait).
2. Lecture des CSV par-dossier internes (riches en details, format majoritairement standardise sauf S2NE qui utilise points-virgules).
3. Lecture PDFs prioritaires : Frontline Media (33-S2NE-03) et Vergers d'Anjou amelioree (35-SICA-01) extraits via `pdftotext -layout`. Camping PDFs OCR illisible (scans + texte chiffre).
4. Pour dossier 29-RHEA : PDFs MUVICO >5MB non extraits cote pipeline en amont — confidence `partial_pdf_only` declaree honnetement. PDF RHEA-03 marque type UNKNOWN.
5. Croisement avec analyses `gagnants-tribunal.md` pour Seasonova (31) et Vergers d'Anjou (35-SICA).

## Champs prioritaires — synthese

### Issue dossier
- 31-OCCITANIE + 35-SICA : **plan_cession_arrete** avec gagnants confirmes par presse.
- 29-RHEA, 33-S2NE, 35-DME : **en_attente** — aucune source publique post-DLDO.

### Motifs tribunal verbatim (gold)
- **31-OCCITANIE** : "Demantelement accepte par tribunal quand offres consolidees par lots coherents (gestion directe Seasonova vs franchises Maeva). Repreneur sectoriel strategique avec continuite emploi."
- **35-SICA** : "Projet cooperatif local coherent ; capacite de stockage Les Vergers d'Anjou passe de 36 000 t a 49 000 t. Repreneur sectoriel strategique avec continuite d'emploi." Concurrent CASTEL+LEROY+VCAPITAL ecarte (400k vs 7,04M, 4 emplois vs 28 — facteur prix x17, facteur emploi x7).

### Forme repreneur dominante
- 13 offres = `societe_existante_industriel`
- 2 offres = `asso_collectivite` (Vergers d'Anjou cooperative)
- 1 offre = `societe_existante_fournisseur` (Planete Mobil Homes)
- Aucune `pp_seule`, aucune `fonds_pe`, aucune `repreneur_etranger`. Pattern fort = repreneurs sectoriels strategiques.

### Pct reprise / pattern social
- **Gagnants** : Seasonova 100% (5/5), Vergers d'Anjou 57% (28/49) + 200k accompagnement social.
- **Ecartes** : CAMPALDIA (NR sur volet social), CASTEL+LEROY+VCAPITAL 25% (4/16).
- Pattern confirme : continuite emploi > 50% est un seuil pratique TC Paris.

### Prix + charges augmentatives
- Pattern "prix derisoire + dette deguisee" : 35-DME-01 (LINAS) 30 EUR + 350k charges = montage reprise de passif.
- Pattern "abandon de creance comme condition" : 35-DME-03 (Qasti) exige abandon 50% creance Banque Postale 335k.
- Pattern "lots indivisibles" : toutes les offres NEOCAMP (4 offres sur 6) sont indivisibles avec offres ALPHA CAMPING.

### Diagnostic
- `structurel` : Frontline Media (33-S2NE-03), Overlord Group (33-S2NE-06), Vergers d'Anjou amelioree (35-SICA-01), Vergers d'Anjou initiale (35-SICA-03 + 06)
- `operationnel` : majorite offres campings
- `superficiel` : Robert Lafont (33-S2NE-02), Economie Matin (33-S2NE-05), Tancrede France Annonces (33-S2NE-04), LINAS (35-DME-01), LOUTSA (35-DME-02)
- `absent` : (aucun)

### BP 3ans present
- 33-S2NE-03 Frontline Media : CA 1,72M -> 1,94M -> 2,06M ; RN 2028 +258k
- 33-S2NE-06 Overlord : croissance CA 90k -> 2,43M en 2 ans (historique demontre)
- 31-OCCITANIE-02 HPA Mediterraneo : CA 1,18M -> 1,4M, EBE 195k -> 376k

### Aucune CS
- **35-SICA-01 Vergers d'Anjou amelioree** : `aucune_cs = true` (seul un point d'inalienabilite LVL POMANJOU). C'est l'unique offre du batch avec zero condition suspensive — facteur explicatif fort de la selection.
- Tous les autres : 1 a 8 conditions suspensives.

### Agressivite envers dirigeants
- Aucune offre agressive (aucune clause non-sollicitation forte detectee).

### Executive summary present
- 21 oui / 6 non (33-S2NE-02 Lafont, 33-S2NE-04 Tancrede, 33-S2NE-05 Economie Matin, 35-DME-01 LINAS, 35-DME-02 LOUTSA, 35-DME-03 QASTI)

### Personnalisation
- Tres faible globalement. Seuls Vergers d'Anjou (35-SICA-01) et Frontline Media (33-S2NE-03) cumulent visite site + rencontre equipes + etude contrats.

## Anomalies signalees

1. **PDFs MUVICO >5MB non extraits** (29-RHEA-04/05/06) : pipeline en amont ne les a pas traites, confidence partial. Recommander re-extraction manuelle.
2. **PDF 29-RHEA-03 type UNKNOWN** : non identifie.
3. **PDFs 29-RHEA-01/02 mal classes** : doublons physiques avec offre HOUSEBASE cible SNC ADONIA.
4. **DUPLICATAS** : 35-SICA-02 == 35-SICA-04 (CASTEL+LEROY+VCAPITAL, meme Docusign) et 35-SICA-03 == 35-SICA-06 (Vergers d'Anjou initiale, meme Docusign).
5. **PDFs campings (31-OCCITANIE)** : OCR illisible (scans), reconstruction integrale via CSV. Confidence medium.
6. **35-DME-01 LINAS** : structure prix exotique (30 EUR + 350k charges augmentatives) — pourrait etre lue comme `partial_pdf_only` mais CSV detaille fourni.
7. **35-DME-03 QASTI** : phrase "La presente offre ne comporte aucune condition suspensive" contredit 4 conditions listees plus haut — incoherence rhetorique forte.
8. **33-S2NE-04 Tancrede** : prix 1 EUR + exclusion materiels/equipements/contrats + exige acquisition prealable marque par France Annonces. Offre tres faible.

## Suggestions Phase 2

- Renforcer le pattern "lots coherents acceptes par tribunal" (Neocamp + Innatis) avec coda contre-exemple Minelli (deja documente).
- Crystalliser la regle "Aucune CS + pct_reprise >50% + diagnostic structurel = signature gagnante" sur les 7 dossiers decides.
- Ajouter au playbook : "Prix symbolique 1-3 EUR est un signal d'incertitude — preferer prix demontre meme bas (Seasonova 2 EUR retenu mais accompagne d'engagement 12 mois)."

## Related

- [[brantham/tc-paris-extraction/_MOC]]
- [[brantham/tc-paris-extraction/analyses/gagnants-tribunal]]
- [[brantham/tc-paris-extraction/analyses/decortique-offres-gagnantes]]
- [[brantham/tc-paris-extraction/grilles/_workflow]]
- [[brantham/tc-paris-extraction/grilles/_schema]]
- [[_system/MOC-patterns]]
