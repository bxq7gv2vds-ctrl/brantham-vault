---
date: 2026-04-05
type: session
projet: brantham
---

# Auto-enrichment — 2026-04-05

## Resultats

| Metrique | Valeur |
|----------|--------|
| Scrape AJ | OK - 457 opportunites (24 sites OK, 1 erreur BVP SSL, 6 vides) |
| Nouvelles opportunites (sans dossier) | 311 |
| Opportunites traitees (top signal) | 10 |
| Dossiers crees | 10 |
| Enrichissement Pappers | 0 (aucun SIREN disponible dans les annonces) |
| Repreneurs identifies | 0 (API locale down + API gouv.fr inaccessible) |
| Erreurs | BVP SSL, API FastAPI down, API gouv hors ligne |

## Opportunites traitees

1. IPSOMEDIC (pharmacie R&D) — aj-specialises-ipsomedic
2. BS OUTDOOR (tentes de toit, CA 2,1M€) — aj-specialises-bs-outdoor
3. PROFAST (transport messagerie, CA 1,1M€) — aj-specialises-profast
4. Negoce semi-remorque (transport) — meynet-cession-d-une-activit-de-n-goce-de-semi-remorque
5. EPIFURIEU (boulangerie, CA 733K€) — aj-specialises-epifurieu
6. Chantier naval Bormes (CA 1,3M€) — aj-specialises-1937-chantier-naval-a-bormes-les-mimosas
7. 7 TECH (machines speciales) — aj-specialises-7-tech
8. Minuteurs EDDO (IoT connecte) — aj-specialises-concepteur-et-fabricant-de-minuteurs-de-douch
9. Connectique (composants electroniques) — aj-specialises-vente-d-entreprise-de-connectique
10. BLUE & PASTEL (biotechnologie pigments) — fhbx-blue-pastel-le-reve-bleu

## Fichiers generes par deal

- `enrichment.json` — metadonnees source + secteur estime
- `analyse.md` — analyse basique (forces/faiblesses)
- `acheteurs.json` — vide (API indisponible)

## Points de blocage

- FastAPI localhost:8000 down — matching repreneurs impossible
- API gouv.fr inaccessible au moment de l'execution
- Aucun SIREN dans les nouvelles annonces AJ — Pappers inutilisable
- 311 nouvelles opportunites dont 302 sans CA declare

## Actions recommandees

- Relancer FastAPI : `cd /Users/paul/Desktop/brantham-partners/api && source .venv/bin/activate && uvicorn main:app --host 0.0.0.0 --port 8000`
- Recuperer SIRENs depuis datarooms pour enrichissement Pappers
- Verifier EPIFURIEU, BS OUTDOOR, PROFAST en priorite (CA > 500K)

## Related

[[brantham/_MOC]]
[[brantham/pipeline/QUEUE]]
- Deep enrichment termine a 02:58
---

## Cycle 04:54

- **Scrape AJ** : lancement...
  - OK : 457 opportunites scrapees

## Cycle 13:36

- **Scrape AJ** : lancement...
  - OK : 457 opportunites scrapees

## Deep Enrichment 14:49
