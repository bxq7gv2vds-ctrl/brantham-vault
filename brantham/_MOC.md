---
type: moc
project: brantham
updated: 2026-03-27
---

# Brantham Partners -- Map of Content

## Mission

Cabinet M&A specialise dans les entreprises en difficulte (PME France). Cible les procedures collectives (redressement judiciaire, liquidation judiciaire, sauvegarde) pour identifier les opportunites de cession et les connecter a des repreneurs qualifies.

## Revenue Model

Success fees sur cessions realisees. Commission sur mise en relation vendeur/repreneur. Pre-revenue actuellement.

## Statut

- API FastAPI: operationnelle (3900+ lignes)
- Pipeline Prefect: operationnel (daily + weekly + monthly)
- Agents: 6 agents operationnels, orchestration Director
- 1 deal actif: MLD (Multi Loisirs Distribution)
- 600+ deals archives
- Revenue: **0 EUR** (pre-revenue)

---

## Project Locations

| Composant | Chemin | Stack |
|---|---|---|
| Backend API | `/Users/paul/Desktop/brantham-partners/api/` | FastAPI, 3900 lines |
| Frontend dashboard | `/Users/paul/internal-tool/` | React 19 + Vite + Zustand |
| Data pipeline | `/Users/paul/Desktop/brantham-partners/` | Python, PostgreSQL 16, Redis 7, Docker |
| Agent pipeline | `/Users/paul/Downloads/brantham-pipeline/` | server.js + 6 agents |
| Memory vault (ops) | **MERGED into vault/brantham/** | Markdown |
| Deals archive | `/Users/paul/brantham-vault/` | 600+ deals |
| MiroFish Engine | `/Users/paul/MiroFish/` | Python 3.12, MLX, FastAPI, Vue/Vite |
| Design/Next.js | `/Users/paul/Desktop/brantham-next/` | Next.js |
| SEO | see [[website/_MOC]] | |

---

## Key Links

- [[brantham/architecture]]
- [[brantham/data-pipeline/_MOC]]
- [[brantham/agents/_MOC]]
- [[brantham/dashboard/_MOC]]
- [[brantham/patterns/teaser-patterns]]
- [[brantham/patterns/teaser-onepager-html-pdf]] — One-pager HTML/PDF aligne sur DA site web
- [[brantham/patterns/scoring-patterns]]

## Knowledge Base — Procedures

- [[brantham/knowledge/procedures/mandat-ad-hoc-conciliation]] — Mandat ad hoc, conciliation, pre-pack cession, privilege new money
- [[brantham/knowledge/procedures/sauvegarde]] — Procedure de sauvegarde
- [[brantham/knowledge/procedures/redressement-judiciaire]] — Redressement judiciaire
- [[brantham/knowledge/procedures/liquidation-judiciaire]] — Liquidation judiciaire
- [[brantham/knowledge/procedures/sauvegarde-acceleree-sfa]] — Sauvegarde acceleree et SFA (classes de parties affectees, cram-down cross-class, reforme 2021)
- [[brantham/knowledge/procedures/lj-simplifiee]] — Liquidation judiciaire simplifiee (L644-1+): seuils, obligatoire/facultatif, delais 6 mois/1 an, impact repreneur

## Knowledge Base — Legal

- [[brantham/knowledge/legal/plans-de-cession]] — Plans de cession judiciaire (L642-1+) : offre, criteres, procedure, effets, execution
- [[brantham/knowledge/legal/nullites-periode-suspecte]] — Nullites periode suspecte (L632-1/L632-2), responsabilite dirigeants (L651-2, L653-1+, L654-1+), checklist due diligence repreneur
- [[brantham/knowledge/legal/plans-de-continuation]] — Plans de continuation (sauvegarde L626-1+ / redressement L631-19+): elaboration, classes de parties affectees, vote, execution, resolution, impact repreneur
- [[brantham/knowledge/legal/sanctions-dirigeants]] — Sanctions et responsabilite des dirigeants (L651-2 insuffisance actif, L653-1+ faillite personnelle, L653-8 interdiction gerer, L654-1+ banqueroute, L621-2 extension procedure): conditions, peines, prescription, jurisprudence, checklist DD repreneur
- [[brantham/knowledge/legal/droit-europeen-insolvabilite]] — Droit europeen de l'insolvabilite : reglement UE 2015/848 (COMI, reconnaissance mutuelle, groupes), directive 2019/1023 (restructuration preventive, classes, cram-down), transposition francaise (ordonnance 2021), comparaison Chapter 11/UK/StaRUG, enjeux cross-border M&A distressed
- [[brantham/knowledge/legal/droit-social-restructuration]] — Droit social en restructuration et procedure collective : L1224-1 (transfert, Spijkers/Suzen, exception plan cession L642-5), PSE en RJ/LJ (L1233-58+, delais raccourcis, homologation DREETS, AGS), licenciement eco hors PSE, consultation CSE, convention collective post-cession (L2261-14, survie 15 mois), APC (L2254-2), APLD-R, contentieux prud'homal, IRP post-cession, checklist sociale repreneur
- [[brantham/patterns/acheteur-mapping]]

## Knowledge Base — Process

- [[brantham/knowledge/process/due-diligence-distressed]] — Due diligence distressed exhaustif: checklist financiere/juridique/sociale/fiscale/operationnelle, red flags, timing LJ vs RJ, quick scan 48h, scoring DD
- [[brantham/knowledge/process/structuration-offres-reprise]] — Structuration offres de reprise (L642-2): 9 mentions obligatoires, strategie redaction, prix vs emploi, garanties, checklist pre-depot, erreurs courantes
- [[brantham/knowledge/process/encheres-surencheres]] — Encheres et surencheres: regime encheres LJ, surenchere 10%/10j, differences RJ vs LJ, strategies d'offres, jurisprudence, plateformes veille
- [[brantham/knowledge/process/audience-tribunal]] — Audience de cession tribunal: deroulement, roles (AJ/MJ/procureur/CSE), presentation orale, criteres L642-5, voies de recours, conseils praticiens
- [[brantham/knowledge/process/post-closing-execution]] — Post-closing et execution du plan de cession: effets jugement, purge suretes, transfert contrats/salaries, paiement prix, commissaire execution, modification plan, inexecution/resolution, substitution repreneur, risques post-closing, checklist J+1 a J+90
- [[brantham/knowledge/process/integration-post-acquisition]] — Integration post-acquisition distressed: specificites vs M&A classique, plan 100 jours (4 phases), stabilisation tresorerie/fournisseurs/clients, volet RH/CSE, quick wins, erreurs classiques, KPIs suivi, cas pratiques, template plan integration Brantham

## Knowledge Base — Finance

- [[brantham/knowledge/finance/valorisation-distressed]] — Valorisation distressed exhaustif: 4 methodes, EBITDA normalise, 13-week CF, BP retournement, multiples sectoriels, scoring deals
- [[brantham/knowledge/finance/restructuration-dette]] — Restructuration de dette et financement en crise: standstill/waiver/A&E/DES/haircut/buyback/NPL, new money L611-11/bridge/DIP/BPI/affacturage/sale-leaseback, LBO distressed, cash management 13WCF, BP retournement, 6 suretes, application Brantham
- [[brantham/knowledge/finance/assurance-credit]] — Assurance-credit et risque fournisseur: mecanisme (souscription/agrement/sinistre/subrogation), acteurs (Allianz Trade 35%/Coface 18%/Atradius 25%), cotation BdF/Altares/Ellisphere, retrait couverture (declencheurs/cascade/impact BFR), interaction procedure collective, negociation assureur, alternatives (L/C/garantie/caution/reserve propriete), affacturage complement, marche FR, DD et strategie post-reprise Brantham
- [[brantham/knowledge/finance/financial-modeling-distressed]] — Modelisation financiere distressed: DCF ajuste (WACC distressed/beta releve/PWDCF scenarios), waterfall analysis (rang creances FR/break point/fulcrum), recovery analysis (benchmarks FR/LGD), 13-week CF (structure/revolving/covenants/stress tests), bridge EV-Equity (ajustements distressed), LBO distressed (loan-to-own/debt capacity/IRR), NPL pricing (EL=PDxLGDxEAD/Monte Carlo/recovery curves), scoring model Brantham, workflows par type de deal
- [[brantham/knowledge/finance/fiscalite-restructuration]] — Fiscalite restructuration et procedures collectives: report deficits (209-I, 220 quinquies), changement controle/agrement, abandons creances (commercial/financier), TVA en procedure, plus-values (238 quindecies, 151 septies), regime faveur fusions (210 A), integration fiscale (223 A+), CIR/CII, asset deal vs share deal, checklist fiscale repreneur
- [[brantham/knowledge/finance/comptabilite-crise]] — Comptabilite entreprises en difficulte: continuite exploitation (PCG/IAS 1), NEP 570, rapport CAC, procedure alerte (L234-1), comptes en procedure, provisions/depreciation (IAS 36/37), ecritures LJ, PCG vs IFRS distressed, engagements hors-bilan, role CAC/EC, red flags comptables, ajustements valorisation

## Knowledge Base — Acteurs

- [[brantham/knowledge/acteurs/ecosysteme-restructuring]] — Ecosysteme restructuring France
- [[brantham/knowledge/acteurs/banques-cellules-restructuring]] — Cellules restructuring des banques francaises: DAS/DAEF/DRAS/DECA, organisation front/middle/back, criteres transfert, IFRS 9 staging, provisionnement, strategies (standstill/waiver/abandon/cession NPL), marche secondaire dette, servicers, mediation credit BdF/CCSF, Bale III/IV backstop, approche M&A distressed, negociation abandons, loan-to-own

## Knowledge Base — Skills (Competences Transversales)

- [[brantham/knowledge/skills/negociation-crise]] — Negociation en crise et restructuration: BATNA distressed, AJ/MJ, creanciers, CSE, prix de cession, surencheres, playbook Brantham
- [[brantham/knowledge/skills/communication-parties-prenantes]] — Communication parties prenantes: interne (salaries), clients, fournisseurs, banques, medias, institutionnel, timeline J-7 a J+90, templates
- [[brantham/knowledge/skills/quick-scan-diagnostic]] — Quick scan / diagnostic flash 24-48h: 10 indicateurs critiques, scoring 1-5, red flags eliminatoires, decision framework go/no-go, template memo 1 page
- [[brantham/knowledge/skills/ethique-repreneur]] — Ethique du repreneur: pratiques condamnables, L642-2 obligations, jurisprudence, charte ethique, RSE distressed, positionnement Brantham

## Knowledge Base — Market Intelligence

- [[brantham/knowledge/market/stats-defaillances-2025]] — Statistiques defaillances France 2024-2025: 70K defaillances/an, 267K emplois, secteurs, PGE, previsions 2026, comparaison internationale, application Brantham

## Pipeline Operations

- [[brantham/pipeline/BOARD]] — Kanban pipeline (statuts des deals)
- [[brantham/pipeline/QUEUE]] — File d'attente opportunites
- [[brantham/analyses/INDEX]] — Toutes les analyses IA
- [[brantham/teasers/INDEX]] — Tous les teasers generes

## Strategy

- [[brantham/strategy/2026-03-15-linkedin-personal-brand]]
- [[brantham/strategy/mirofish-vision]] — Vision MiroFish: simulateur de monde M&A distressed (agents autonomes, echelle massive)
- [[brantham/strategy/mirofish-roadmap]] — Roadmap technique MiroFish (v0.1 → v2.0)
- [[brantham/strategy/mirofish-todo]] — TODO executif: World Simulator M&A (7 phases)

### MiroFish v0.3 Status (2026-03-18)
- **995K agents x 100 rounds = 83.4s** (0.83s/round sur M5)
- Modele distille: MLP 4293 params, 83.9% accuracy, 17.2KB
- MLX GPU inference: 0.117s pour 1M agents
- 7 scenarios pre-configures (baseline, crise_2008, boom_2021, hausse_taux, reforme, desert, million_agents)
- API FastAPI + Frontend Vue/Vite operationnels
- Patterns: [[brantham/patterns/distilled-model-scaling]], [[brantham/patterns/numpy-aggregation-over-objects]]
- [[brantham/strategy/webapp-roadmap]] — Roadmap Web App internal-tool (6 phases)

---

## Current Pipeline Status

| Deal | Statut | Deadline | Next Step |
|---|---|---|---|
| MLD (Multi Loisirs Distribution) | teaser_redige | 17/03/2026 | Pret pour Hunter |

- 600+ deals archives dans `/Users/paul/brantham-vault/`
- Dernier scan AJ: [[brantham/sessions/auto-enrichment-2026-03-25]] -- 456 opportunites (24/31 sites), 75 avec CA>=1M, top pick: Papier & electricite (204M), Commerce sport (deadline 07/04)

---

## Revenue

**0 EUR** -- pre-revenue. Premier deal actif en cours (MLD). Fee structure a definir sur premiere cession reussie.
