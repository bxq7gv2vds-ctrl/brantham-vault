#!/usr/bin/env python3
"""
pappers_search.py — Search Pappers API and save results to vault.

Creates:
  - recherches/{date}-{query-slug}.md

Usage:
  uv run pappers_search.py "BTP liquidation"
  uv run pappers_search.py --naf 4520A --dept 75 --procedure lj
  uv run pappers_search.py --naf 4520A --ca-min 500000 --ca-max 5000000
  uv run pappers_search.py --dirigeant "Dupont" --dept 75
"""

import argparse
import json
import os
import re
import sys
from datetime import date
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


def search_entreprises(params: dict, api_key: str) -> dict:
    params["api_token"] = api_key
    params.setdefault("par_page", 10)
    resp = requests.get(f"{API_BASE}/recherche", params=params, timeout=30)
    resp.raise_for_status()
    return resp.json()


def search_dirigeants(params: dict, api_key: str) -> dict:
    params["api_token"] = api_key
    params.setdefault("par_page", 10)
    resp = requests.get(f"{API_BASE}/recherche-dirigeants", params=params, timeout=30)
    resp.raise_for_status()
    return resp.json()


def search_publications(params: dict, api_key: str) -> dict:
    params["api_token"] = api_key
    params.setdefault("par_page", 10)
    resp = requests.get(f"{API_BASE}/recherche-publications", params=params, timeout=30)
    resp.raise_for_status()
    return resp.json()


def write_search_results(data: dict, args, query_type: str) -> Path:
    today = date.today().isoformat()

    # Build slug from search params
    parts = []
    if args.query:
        parts.append(args.query)
    if args.naf:
        parts.append(f"naf-{args.naf}")
    if args.dept:
        parts.append(f"dept-{args.dept}")
    if args.procedure:
        parts.append(args.procedure)
    if args.dirigeant:
        parts.append(args.dirigeant)
    slug = slugify("-".join(parts) if parts else "all")

    filename = f"{today}-{slug}.md"
    filepath = PAPPERS_DIR / "recherches" / filename

    resultats = data.get("resultats", []) or []
    total = data.get("total", len(resultats))

    # Build results table
    rows = []
    for i, r in enumerate(resultats, 1):
        siren = r.get("siren", "")
        denom = r.get("denomination", r.get("nom_entreprise", ""))
        naf = r.get("code_naf", "")
        ca = r.get("chiffre_affaires", "")
        eff = r.get("effectif", "")

        # Check for procedures
        procs = r.get("procedures_collectives", []) or []
        proc_str = ""
        if procs:
            proc_str = procs[0].get("type", "")[:20]

        e_slug = slugify(denom)
        link = f"[[brantham/pappers/entreprises/{siren}-{e_slug}]]"
        rows.append(f"| {i} | {denom} | {siren} | {naf} | {ca} | {eff} | {proc_str} | {link} |")

    # Build criteres yaml
    criteres = {}
    if args.query:
        criteres["q"] = args.query
    if args.naf:
        criteres["code_naf"] = args.naf
    if args.dept:
        criteres["departement"] = args.dept
    if args.region:
        criteres["region"] = args.region
    if args.procedure:
        criteres["type_publication"] = args.procedure
    if args.ca_min:
        criteres["chiffre_affaires_min"] = args.ca_min
    if args.ca_max:
        criteres["chiffre_affaires_max"] = args.ca_max
    if args.effectif_min:
        criteres["tranche_effectif_min"] = args.effectif_min
    if args.effectif_max:
        criteres["tranche_effectif_max"] = args.effectif_max
    if args.dirigeant:
        criteres["nom_dirigeant"] = args.dirigeant

    criteres_yaml = "\n".join(f"  {k}: {v}" for k, v in criteres.items())

    content = f"""---
type: recherche_pappers
date: "{today}"
query_type: {query_type}
criteres:
{criteres_yaml}
nb_resultats: {total}
tokens_consommes: 1
tags: []
---

# Recherche Pappers — {today}

> {query_type} | {total} resultats | 1 token

## Criteres

```yaml
{chr(10).join(f'{k}: {v}' for k, v in criteres.items())}
```

## Resultats ({len(resultats)}/{total})

| # | Denomination | SIREN | NAF | CA | Effectif | Procedure | Lien |
|---|-------------|-------|-----|-----|----------|-----------|------|
{chr(10).join(rows) if rows else '| — | — | — | — | — | — | — | — |'}

## Analyse

### Patterns Observes
-

### Entreprises a Approfondir
-

### Actions
- [ ] Creer fiche entreprise pour:
- [ ] Lancer enrichissement financier pour:
- [ ] Qualifier comme deal:

## Notes

-

## Related

- [[brantham/pappers/_MOC]]
- [[brantham/_MOC]]
"""

    filepath.write_text(content)
    print(f"  -> {filepath}")
    print(f"  {len(resultats)}/{total} resultats")
    return filepath


def main():
    parser = argparse.ArgumentParser(description="Search Pappers and save to vault")
    parser.add_argument("query", nargs="?", default="", help="Free text search")
    parser.add_argument("--naf", help="Code NAF filter")
    parser.add_argument("--dept", help="Departement filter")
    parser.add_argument("--region", help="Region filter")
    parser.add_argument("--procedure", help="Procedure type (lj, rj, sauvegarde)")
    parser.add_argument("--ca-min", type=int, help="CA minimum")
    parser.add_argument("--ca-max", type=int, help="CA maximum")
    parser.add_argument("--effectif-min", help="Effectif min")
    parser.add_argument("--effectif-max", help="Effectif max")
    parser.add_argument("--dirigeant", help="Recherche dirigeant")
    parser.add_argument("--publications", action="store_true", help="Search BODACC publications")
    parser.add_argument("--page", type=int, default=1, help="Page number")
    parser.add_argument("--per-page", type=int, default=10, help="Results per page")
    args = parser.parse_args()

    api_key = get_api_key()

    params = {"page": args.page, "par_page": args.per_page}
    if args.query:
        params["q"] = args.query
    if args.naf:
        params["code_naf"] = args.naf
    if args.dept:
        params["departement"] = args.dept
    if args.region:
        params["region"] = args.region
    if args.ca_min:
        params["chiffre_affaires_min"] = args.ca_min
    if args.ca_max:
        params["chiffre_affaires_max"] = args.ca_max
    if args.effectif_min:
        params["tranche_effectif_min"] = args.effectif_min
    if args.effectif_max:
        params["tranche_effectif_max"] = args.effectif_max

    if args.dirigeant:
        params["nom_dirigeant"] = args.dirigeant
        print(f"Searching dirigeants: {args.dirigeant}...")
        data = search_dirigeants(params, api_key)
        query_type = "dirigeant"
    elif args.publications or args.procedure:
        if args.procedure:
            params["type"] = args.procedure
        print(f"Searching BODACC publications...")
        data = search_publications(params, api_key)
        query_type = "publication"
    else:
        print(f"Searching entreprises...")
        data = search_entreprises(params, api_key)
        query_type = "entreprise"

    write_search_results(data, args, query_type)
    print("Done. 1 token consumed.")


if __name__ == "__main__":
    main()
