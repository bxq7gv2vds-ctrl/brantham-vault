---
type: batch-log
batch_id: 17
dossiers_traites: 3
offres_extraites: 18
date: 2026-05-15
agent: claude-agent
tags: [tc-paris, batch, extraction, fhbx, neocamp, fonciere, hpa]
---

# Batch 17 — Dossiers 21B AEDES / 27B GRANDE LISSE / 28B ALPHA CAMPING

## Fichiers JSON crees

### Dossiers (3)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/dossiers/21B-AEDES.json` — SCI fonciere FHBX (portefeuille Melot-Gouband 26 entites)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/dossiers/27B-GD-LISSE.json` — SCI fonciere camping L'Escapade Dordogne (groupe Neocamp pole foncier)
- `/Users/paul/vault/brantham/tc-paris-extraction/grilles/dossiers/28B-ALPHA.json` — SAS exploitation 21 campings Neocamp (Camping Paradis / Bel Air / Ushuaia)

### Offres (18)
**21B AEDES (4 offres distinctes parmi 9 PDFs — 3 doublons MUVICO regroupes, offre 5 hors perimetre, offre 2 non identifiable)** :
- `21B-AEDES-01-MUVICO.json` — Groupe Victor COHEN, offre globale FHBX (90k initiale / 100k amelioree) — confidence partial_pdf_only
- `21B-AEDES-06-VERDOSO.json` — SAS offre globale 26 entites Docusign — prix par entite non extrait
- `21B-AEDES-08-LABRAX.json` — Offre finale 21 M EUR portefeuille global (la plus haute enveloppe)
- `21B-AEDES-09-HOUSEBASE.json` — Philippe ZERR, offre dediee — details non extraits

**27B GRANDE LISSE (5 offres uniques)** :
- `27B-GD-LISSE-01-BOUTONNE.json` — SCI BOUTONNE (Mauvin/Noel, cabinet Concerto 30 ans) — **500 000 EUR comptant cheque banque, AUCUNE CS**
- `27B-GD-LISSE-02-SEASONOVA.json` — Lettre d'intention seule, pas de prix ferme
- `27B-GD-LISSE-03-SHD.json` — KBC/Molin 1 000 EUR symbolique, societe recente, conteste pret LCL
- `27B-GD-LISSE-04-CAMPALDIA.json` — Loic Peron-Magnan, 3 EUR symbolique, indivisible 15 campings Neocamp
- `27B-GD-LISSE-05-FEMINA-MARENGO.json` — Familles HUBLE+WAJSBROT, **1 400 000 EUR (le plus eleve)**, partenariat Le Royon 20 ans

**28B ALPHA CAMPING (9 offres distinctes)** :
- `28B-ALPHA-01-MASSOUTY.json` — Directeur actuel 2 sites Vassiviere, 1 EUR
- `28B-ALPHA-02-HUTTOPIA.json` — 5 sites, 25 000 EUR, 127 campings 8 pays
- `28B-ALPHA-03-HFB.json` — 1 site Roscoff, 3 000 EUR (Groupe Touriste/Gloaguen)
- `28B-ALPHA-04-SEASONOVA.json` — **RETENU** — 9 sites, 2 EUR provisoire puis amelioree, 10 salaries, engagement 12 mois pas de licenciement eco
- `28B-ALPHA-05-CAMPALDIA.json` — 14 sites, 3 EUR symbolique, indivisible 15 campings
- `28B-ALPHA-06-FEMINA-MARENGO.json` — 12 sites, **2 000 000 EUR (le plus eleve)**, 19 salaries
- `28B-ALPHA-07-AGEXCO.json` — Expert-comptable Thiers, 2 fonds Chanterelles+Demeures, 20k + 535k charges augmentatives
- `28B-ALPHA-08-PLANETE-MH.json` — 3 sites Brabois+Giessen+Roscoff, 11 025 EUR, concept Mobil-Home XXL
- `28B-ALPHA-09-SUITCASE.json` — 1 site Roscoff, 20 000 EUR, Groupe LEGENDRE soutien

## Issue connue (source : analyses/gagnants-tribunal.md, presse 28/04/2026)

**Niveau dossier 28B ALPHA — DECIDE 02/04/2026** :
- **SEASONOVA** retenu pour **15 sites** Alpha (Seasonova passe de 21 a 36 campings FR)
- **MAEVA** (Pierre & Vacances–Center Parcs via rachat 5C Developpement) retenu pour franchises **Camping Paradis / Ushuaia Villages / Mistercamp**
- Concurrents ecartes : FEMINA STYL+MARENGO, HOMAIR (ECG), CAMPALDIA, HUTTOPIA, autres

**Niveau dossier 27B GRANDE LISSE — en_attente sur l'arbitrage specifique de la fonciere** :
- Issue niveau groupe = demantelement Seasonova + Maeva (impact direct sur GRANDE LISSE en tant que fonciere du Camping L'Escapade indivisible avec exploitation L'Escapade SAS)
- Arbitrage entre FEMINA STYL+MARENGO 1,4 M EUR (offre la plus elevee) vs offres symboliques + cession titres ILO non trace publiquement

**Niveau dossier 21B AEDES — en_attente** :
- Audience non publiee. 4 offres concurrentes dont LABRAX 21 M EUR enveloppe globale 26 entites. Pattern fonciere Bourbouloux/FHBX confirme.

## Anomalies / Pieges

1. **Collision numerique** : un autre dossier 21 existe (SYM OPTIC) et un autre 28 existe (PRIMEL TREGASTEL — egalement portefeuille FHBX). J'ai utilise les prefixes `21B-` / `27B-` / `28B-` pour eviter collision avec existing files.
2. **AEDES offre 5** : PDF mal classe — cible SNC ADONIA (501 600 EUR, immeuble Cachan). Non traite cote AEDES.
3. **AEDES offre 2** : type UNKNOWN dans CSV — non identifiable.
4. **AEDES MUVICO** : 3 PDFs doublons (offres 1, 3, 4) — fusionnes en une fiche `MUVICO`.
5. **PDFs MUVICO >5MB** : non extraits — prix issus de la table de reference CSV — confidence `partial_pdf_only`.
6. **GRANDE LISSE SHD** : erreur dans objet PDF mentionne 'Narbonne' alors que bien est a Lamonzie-Montastruc (Dordogne) — signal sur la qualite redactionnelle de l'offre.
7. **GRANDE LISSE FEMINA** : date validite '2025-01-28' probable coquille pour 2026-01-28.
8. **ALPHA SEASONOVA** : marquee `amelioree_puis_retenue` selon instruction utilisateur — source presse confirmee 02/04/2026 sur le LOT 15 sites (offre 4 PDF couvre 9 sites — l'amelioration finale a probablement etendu le perimetre).
9. **ALPHA FEMINA potentiel risque L.642-3** : FEMINA STYL est actionnaire minoritaire dormant de SAS ILO (mere d'ALPHA CAMPING). A surveiller dans toute analyse rejet.

## Patterns observes (alimentation Phase 2)

1. **Foncieres Bourbouloux/FHBX** : pattern offres globales multi-entites vs offres dediees + offre finale "ferme et indivisible" enveloppe consolidee (LABRAX 21 M EUR). Repreneurs recurrents : MUVICO (Cohen), VERDOSO, HOUSEBASE (Zerr), LABRAX. Voir aussi 28-PRIMEL et 03-INSULA.
2. **HPA/Neocamp pattern demantelement** : tribunal accepte decoupage par sous-activite quand offres consolidees coherentes (Seasonova exploitation directe + Maeva franchises). Concurrents ecartes systematiquement = offres partielles cherry-picking 1-2 sites sans coherence de groupe.
3. **Prix symbolique 1-3 EUR + amelioration prevue** : strategie courante HPA (Seasonova retenu, CAMPALDIA, HUTTOPIA) — le tribunal arbitre sur le projet industriel et l'engagement social, pas le prix nominal.
4. **Repreneurs sectoriels groupes vs single-site** : tribunal favorise consolidateurs avec capacite financiere demontree + reseau existant (Seasonova 20 campings, HUTTOPIA 127 campings, FEMINA 16 campings 4900 emplacements).
5. **Indivisibilites** : tres frequentes sur dossiers groupes (Neocamp : Boutonne+L'Escapade, Campaldia 7 entites, FEMINA+MARENGO 4-5 offres, HUTTOPIA+ACO).
6. **Prix VERSUS issue** : FEMINA+MARENGO 2 M EUR sur ALPHA = la plus haute, **ecartee**. Seasonova ~symbolique = **retenue**. Confirme que le prix nominal n'est PAS le critere dominant.

## Suggestions

1. **Compiler concepts** : creer pattern markdown `vault/brantham/patterns/hpa-demantelement-lots-coherents.md` synthese sur le pattern Neocamp/Alpha (Seasonova+Maeva).
2. **Repreneur recurrent** : SEASONOVA et HUTTOPIA apparaissent comme **consolidateurs serial HPA** — ajouter a `analyses/repreneurs-recurrents.md` (jusqu'ici AA Investments HK seul confirme).
3. **Croiser avec dossier 27 OKABE** : autre dossier "27" existant (SCI OKABE), verifier si pole foncier Neocamp ou independant.
4. **Croiser avec dossiers FHBX** : `28-PRIMEL` deja extrait + `03-INSULA` reference. Construire fiche groupe `vault/brantham/deals/active/affaire-balthazar-fhbx/_MOC.md` synthese 26 entites Melot-Gouband.

## Related

- [[brantham/tc-paris-extraction/_MOC]]
- [[brantham/tc-paris-extraction/analyses/gagnants-tribunal]]
- [[brantham/tc-paris-extraction/analyses/decortique-offres-gagnantes]]
- [[brantham/tc-paris-extraction/grilles/_workflow]]
- [[brantham/tc-paris-extraction/grilles/_schema]]
