#!/usr/bin/env python3
"""
pappers_monitor.py — Monitor BODACC for new procedures collectives.

Searches for recent publications (LJ, RJ, sauvegarde) and auto-creates
procedure-collective fiches + scoring for deal qualification.

Usage:
  uv run pappers_monitor.py                                    # Default: LJ+RJ in IDF
  uv run pappers_monitor.py --procedure lj,rj --dept 75,92,93,94
  uv run pappers_monitor.py --naf 4520A --ca-min 500000
  uv run pappers_monitor.py --all-france                       # Nationwide
"""

import argparse
import os
import re
import sys
from datetime import date, timedelta
from pathlib import Path

import requests

VAULT = Path(os.environ.get("VAULT_PATH", "/Users/paul/vault"))
PAPPERS_DIR = VAULT / "brantham" / "pappers"
API_BASE = "https://api.pappers.fr/v2"


def get_api_key() -> str:
    key = os.environ.get("PAPPERS_API_KEY", "")
    if not key:
        env_file = PAPPERS_DIR / "scripts" / ".env"
        if env_file.exists():
            for line in env_file.read_text().splitlines():
                if line.startswith("PAPPERS_API_KEY="):
                    key = line.split("=", 1)[1].strip().strip('"').strip("'")
    if not key:
        print("ERROR: Set PAPPERS_API_KEY env var or create scripts/.env")
        sys.exit(1)
    return key


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[àáâãäå]", "a", text)
    text = re.sub(r"[èéêë]", "e", text)
    text = re.sub(r"[ìíîï]", "i", text)
    text = re.sub(r"[òóôõö]", "o", text)
    text = re.sub(r"[ùúûü]", "u", text)
    text = re.sub(r"[ç]", "c", text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:60]


def search_publications(params: dict, api_key: str) -> dict:
    params["api_token"] = api_key
    resp = requests.get(f"{API_BASE}/recherche-publications", params=params, timeout=30)
    resp.raise_for_status()
    return resp.json()


def score_deal(pub: dict) -> int:
    """Quick scoring 0-100 based on available data."""
    score = 0

    # Has SIREN = identifiable
    if pub.get("siren"):
        score += 20

    # Type de procedure
    ptype = (pub.get("type", "") or "").lower()
    if "redressement" in ptype:
        score += 25  # RJ = best for M&A
    elif "liquidation" in ptype:
        score += 15  # LJ = faster but less value
    elif "sauvegarde" in ptype:
        score += 20  # Sauvegarde = good if early

    # Has financial data
    if pub.get("chiffre_affaires"):
        ca = pub.get("chiffre_affaires", 0) or 0
        if ca > 1_000_000:
            score += 25
        elif ca > 500_000:
            score += 20
        elif ca > 200_000:
            score += 10
    else:
        score += 5  # Unknown CA = worth checking

    # Has effectif
    eff = pub.get("effectif", 0) or 0
    if eff > 10:
        score += 15
    elif eff > 5:
        score += 10

    # Sector bonus (can be refined)
    naf = pub.get("code_naf", "") or ""
    high_value_naf = ["25", "28", "29", "10", "11", "43", "41", "45", "46", "47", "56"]
    if any(naf.startswith(prefix) for prefix in high_value_naf):
        score += 15

    return min(score, 100)


def write_procedure(pub: dict, score: int) -> Path:
    """Write a procedure-collective fiche from a BODACC publication."""
    today = date.today().isoformat()
    siren = pub.get("siren", "unknown")
    denom = pub.get("denomination", pub.get("nom_entreprise", "inconnu"))
    ptype = pub.get("type", "procedure")
    pub_date = pub.get("date", today)
    tribunal = pub.get("tribunal", "")

    slug = slugify(f"{pub_date}-{siren}-{ptype}")
    filepath = PAPPERS_DIR / "procedures-collectives" / f"{slug}.md"

    if filepath.exists():
        return filepath

    # Normalize procedure type
    ptype_norm = "autre"
    ptype_lower = (ptype or "").lower()
    if "liquidation" in ptype_lower:
        ptype_norm = "liquidation_judiciaire"
    elif "redressement" in ptype_lower:
        ptype_norm = "redressement_judiciaire"
    elif "sauvegarde" in ptype_lower:
        ptype_norm = "sauvegarde"
    elif "mandat" in ptype_lower:
        ptype_norm = "mandat_ad_hoc"
    elif "conciliation" in ptype_lower:
        ptype_norm = "conciliation"

    code_naf = pub.get("code_naf", "")
    libelle_naf = pub.get("libelle_code_naf", "")
    ca = pub.get("chiffre_affaires", "")
    effectif = pub.get("effectif", "")
    ville = pub.get("ville", "")
    dept = pub.get("departement", "")
    localisation = f"{ville} ({dept})" if ville else dept

    e_slug = slugify(denom)
    secteur_slug = slugify(libelle_naf) if libelle_naf else code_naf

    content = f"""---
type: procedure_collective
siren: "{siren}"
denomination: "{denom}"
type_procedure: {ptype_norm}
tribunal: "{tribunal}"
date_ouverture: "{pub_date}"
date_jugement: ""
date_fin_periode_observation: ""
date_plan: ""
date_cloture: ""
administrateur_judiciaire: ""
mandataire_judiciaire: ""
juge_commissaire: ""
statut: en_cours
est_deal_potentiel: {str(score >= 60).lower()}
score_deal: {score}
code_naf: "{code_naf}"
secteur_brantham: ""
ca_dernier: {ca or ''}
effectif: {effectif or ''}
localisation: "{localisation}"
tags: []
date_fetch_pappers: "{today}"
---

# {ptype_norm} — {denom} ({siren})

> Procedure collective detectee via Pappers/BODACC. Score deal: {score}/100.

## Entreprise

[[brantham/pappers/entreprises/{siren}-{e_slug}]]

| Champ | Valeur |
|-------|--------|
| Denomination | {denom} |
| SIREN | {siren} |
| Secteur | {code_naf} — {libelle_naf} |
| CA dernier | {ca} EUR |
| Effectif | {effectif} |
| Localisation | {localisation} |

## Procedure

| Champ | Valeur |
|-------|--------|
| Type | {ptype_norm} |
| Tribunal | {tribunal} |
| Date ouverture | {pub_date} |
| Statut | en_cours |

## Publication BODACC

| Date | Type | Description |
|------|------|-------------|
| {pub_date} | {ptype} | {(pub.get('description', '') or '')[:200]} |

## Evaluation Deal Brantham (Score: {score}/100)

| Critere | Score | Notes |
|---------|-------|-------|
| Identifiable (SIREN) | {'20' if siren != 'unknown' else '0'}/20 | |
| Type procedure | /20 | {ptype_norm} |
| Taille (CA) | /25 | {ca or 'inconnu'} |
| Effectif | /15 | {effectif or 'inconnu'} |
| Secteur | /15 | {code_naf} |
| **TOTAL** | **{score}/100** | |

### Decision

{'- [x] **QUALIFIER COMME DEAL** (score >= 60)' if score >= 60 else '- [ ] Qualifier comme deal (score < 60)'}
- [ ] Lancer `pappers_fetch.py {siren}` pour fiche complete
- [ ] Rejeter (motif: )

## Notes

-

## Related

- [[brantham/pappers/_MOC]]
- [[brantham/_MOC]]
- [[brantham/pappers/entreprises/{siren}-{e_slug}]]
- [[brantham/pappers/secteurs/{code_naf}-{secteur_slug}]]
"""

    filepath.write_text(content)
    return filepath


def main():
    parser = argparse.ArgumentParser(description="Monitor BODACC for new procedures")
    parser.add_argument("--procedure", default="redressement_judiciaire,liquidation_judiciaire",
                        help="Procedure types (comma-separated)")
    parser.add_argument("--dept", default="75,92,93,94",
                        help="Departements (comma-separated)")
    parser.add_argument("--naf", help="Code NAF filter")
    parser.add_argument("--ca-min", type=int, help="CA minimum")
    parser.add_argument("--ca-max", type=int, help="CA maximum")
    parser.add_argument("--all-france", action="store_true", help="No department filter")
    parser.add_argument("--days", type=int, default=30, help="Look back N days")
    parser.add_argument("--min-score", type=int, default=0, help="Minimum deal score to save")
    parser.add_argument("--page", type=int, default=1)
    parser.add_argument("--per-page", type=int, default=10)
    args = parser.parse_args()

    api_key = get_api_key()

    date_min = (date.today() - timedelta(days=args.days)).isoformat()

    params = {
        "date_publication_min": date_min,
        "page": args.page,
        "par_page": args.per_page,
    }

    if not args.all_france:
        params["departement"] = args.dept

    if args.naf:
        params["code_naf"] = args.naf
    if args.ca_min:
        params["chiffre_affaires_min"] = args.ca_min
    if args.ca_max:
        params["chiffre_affaires_max"] = args.ca_max

    # Search for each procedure type
    proc_types = args.procedure.split(",")
    total_found = 0
    total_qualified = 0
    tokens = 0

    for ptype in proc_types:
        ptype = ptype.strip()
        params["type"] = ptype
        print(f"\nSearching {ptype}...")

        try:
            data = search_publications(params, api_key)
            tokens += 1
            results = data.get("resultats", []) or []
            total = data.get("total", len(results))
            print(f"  {len(results)}/{total} resultats")

            for pub in results:
                score = score_deal(pub)
                if score >= args.min_score:
                    filepath = write_procedure(pub, score)
                    siren = pub.get("siren", "?")
                    denom = pub.get("denomination", "?")
                    marker = "**" if score >= 60 else "  "
                    print(f"  {marker} [{score:3d}] {denom} ({siren}) -> {filepath.name}")
                    total_found += 1
                    if score >= 60:
                        total_qualified += 1

        except Exception as e:
            print(f"  ERROR: {e}")

    print(f"\n{'='*60}")
    print(f"Total: {total_found} procedures, {total_qualified} qualified (>=60)")
    print(f"Tokens consumed: {tokens}")


if __name__ == "__main__":
    main()
