---
type: pattern
slug: osint-deanon-cession-anonyme
category: scraping
tags: [osint, m_a, distressed, bodacc, sirene, pappers, actify]
created: 2026-05-13
updated: 2026-05-13
---

# OSINT Deanon — désanonymiser une cession judiciaire

Pattern systématique pour identifier l'entreprise réelle derrière une annonce
anonymisée de cession (Actify, aj-dataroom, repreneurs.com, 2c-partenaires,
teaser AJ). Skill outil : [[~/.claude/skills/osint-deanon/SKILL]] +
[[~/.claude/skills/osint-deanon/playbook]].

## Méthode SCRAPE

1. **S**urface — Scrape page anonymisée, extraire toutes les meta
2. **C**ross-check — Identifier AJ/MJ, **ne PAS confondre adresse contact (étude)
   avec siège (débiteur)**
3. **R**esolve AJ — Annuaire CNAJMJ, site cabinet, dossiers actifs publiés
4. **A**cquire teaser — Télécharger PNG/PDF, décoder apostrophes Unicode
   (U+2019 → %E2%80%99), vision Claude
5. **P**robe BODACC — API open data, filtrer par AJ + activité + année,
   lister TOUS les candidats
6. **E**stablish proof — Cross-check CA exact à l'euro près sur 3 ans, sites,
   dirigeants, dates jugement

## Sources fiables

| Source | Usage | Endpoint |
|---|---|---|
| BODACC open data | RJ/LJ/sauvegarde par AJ | bodacc-datadila.opendatasoft.com/api/records/1.0/search/ |
| SIRENE | Fiche INSEE + établissements | recherche-entreprises.api.gouv.fr |
| Societe.com | CA exact gratuit | societe.com/societe/<slug>-<siren>.html |
| Pappers MCP | Cross-check, comptes annuels | mcp__pappers__informations-entreprise |
| CNAJMJ | Annuaire AJ/MJ officiels | cnajmj.fr/annuaire/ |
| Doctrine | Historique par ville | doctrine.fr/directories/enterprises |
| Qualit'EnR | Certifications solaire RGE | qualit-enr.org/entreprises/ |

## Pièges documentés (cas MONABEE 2026)

1. **Adresse contact = étude AJ**. Le 128 rue Pierre Corneille 69003 Lyon est
   l'adresse SCP AJ Meynet, pas du débiteur.
2. **Champs Actify auto-saisis erronés** : "ancienneté 2-5 ans" pour MONABEE
   créée 2012 (14 ans).
3. **Apostrophes typographiques URLs images** : `'` (U+2019) au lieu de `'`
   (U+0027) → 404 si non décodé.
4. **`departement_nom_officiel` BODACC = juridiction**, pas siège.
5. **Collaborateurs ≠ MJ** : "camille.leprat@etude-meynet" est une collabo de
   l'étude Meynet, pas le MJ officiel (Apollo.io renvoie "ATMP du Rhône" — faux,
   ATMP fait des tutelles).
6. **OCR teaser** : "Vaulx-Meilieu" = "Vaulx-Milieu" (faute frappe AJ).
7. **CA exact à l'euro = empreinte unique**. MONABEE teaser 12 061 109 € = CA
   société.com 12 061 000 € → preuve définitive.
8. **NAF générique trompeur** : MONABEE classé NAF 4321A (installation électrique)
   alors qu'elle fait du photovoltaïque B2C. Le filtre activité BODACC manque
   ces cas. Toujours scanner les "autres" candidats du même AJ.

## Études AJ / MJ usuelles (région ARA)

- **SCP AJ Meynet & Associés** — 128 rue Pierre Corneille 69003 Lyon
  (Robert Louis Meynet, Typhaine Meynet, Arthur Boucaud, David-Emmanuel
  Meynet) + Annecy, Chambéry, Avignon, Grenoble, Thonon
- **SELARL Anasta** — Lyon/Chambéry (Me Marc Chapon)
- **SELARLU Martin** — 20 bd Eugène Deruelle 69003 Lyon (Me Pierre Martin)
- **SELARL Alliance MJ** — Lyon (Me Marie Dubois, Me Patrick Paul Dubois)
- **SELARL MJ Synergie** — Lyon/Annecy/Annonay
- **SCP CBF Associés** — Paris (Me Lou Fléchard)
- **AJUP** — Lyon (Me Etienne-Martin, Me Coquard)

## Scripts opérationnels

- `fetch-teaser.sh <url-annonce>` — récupère HTML + images teaser
- `bodacc-aj-scan.sh <aj> <année> [<regex-activité>]` — liste RJ de l'AJ
- `bodacc-verify.sh <siren>` — historique BODACC complet d'un SIREN
- `sirene-establishments.sh <siren>` — fiche SIRENE + URLs ets secondaires

Tous dans `~/.claude/skills/osint-deanon/scripts/`.

## Cas d'application Brantham

- **MONABEE** (mai 2026) — annonce actify n°14566 → SIREN 788614006,
  Dardilly, RJ 09/04/2026, AJ Meynet, deadline offres 19/06/2026, CA 12M€
  décroissant. Voir [[brantham/deals/identified/2026-05-13-monabee]] (à créer).

## Related

- [[brantham/_MOC]]
- [[_system/MOC-patterns]]
- [[brantham/patterns/scraping-robust]]
- [[brantham/patterns/teaser-pptx-generation]]
- [[brantham/patterns/onboarding-distressed-ma]]
