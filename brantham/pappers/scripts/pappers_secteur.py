#!/usr/bin/env python3
"""
pappers_secteur.py — Build sector analysis from Pappers data.

Searches Pappers for companies in a given NAF sector, aggregates stats,
identifies distressed companies and potential buyers.

Usage:
  uv run pappers_secteur.py 4520A                          # Single NAF code
  uv run pappers_secteur.py 4520A --dept 75 --ca-min 500000
  uv run pappers_secteur.py 56 --prefix                     # All codes starting with 56 (restaurant)
"""

import argparse
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
        print("ERROR: Set PAPPERS_API_KEY")
        sys.exit(1)
    return key


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[àáâãäåèéêëìíîïòóôõöùúûüç]", lambda m: {
        "à":"a","á":"a","â":"a","ã":"a","ä":"a","å":"a",
        "è":"e","é":"e","ê":"e","ë":"e",
        "ì":"i","í":"i","î":"i","ï":"i",
        "ò":"o","ó":"o","ô":"o","õ":"o","ö":"o",
        "ù":"u","ú":"u","û":"u","ü":"u","ç":"c"
    }.get(m.group(), m.group()), text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:60]


def main():
    parser = argparse.ArgumentParser(description="Build sector analysis from Pappers")
    parser.add_argument("naf", help="Code NAF (e.g. 4520A)")
    parser.add_argument("--dept", help="Department filter")
    parser.add_argument("--region", help="Region filter")
    parser.add_argument("--ca-min", type=int, help="CA minimum")
    parser.add_argument("--ca-max", type=int, help="CA maximum")
    parser.add_argument("--prefix", action="store_true", help="Use NAF as prefix (all sub-codes)")
    args = parser.parse_args()

    api_key = get_api_key()
    today = date.today().isoformat()

    # Search active companies in sector
    params = {
        "api_token": api_key,
        "code_naf": args.naf,
        "entreprise_cessee": "false",
        "par_page": 10,
        "page": 1,
    }
    if args.dept:
        params["departement"] = args.dept
    if args.region:
        params["region"] = args.region
    if args.ca_min:
        params["chiffre_affaires_min"] = args.ca_min
    if args.ca_max:
        params["chiffre_affaires_max"] = args.ca_max

    print(f"Fetching sector {args.naf}...")

    # Active companies
    resp = requests.get(f"{API_BASE}/recherche", params=params, timeout=30)
    resp.raise_for_status()
    active_data = resp.json()
    total_active = active_data.get("total", 0)
    top_companies = active_data.get("resultats", [])

    # Companies with procedures
    params_proc = {**params}
    params_proc["type_publication"] = "Jugement d'ouverture de procédure de redressement judiciaire,Jugement d'ouverture de procédure de liquidation judiciaire"
    # Use search with procedures filter
    resp2 = requests.get(f"{API_BASE}/recherche", params={**params, "entreprise_cessee": "true"}, timeout=30)
    resp2.raise_for_status()
    proc_data = resp2.json()
    proc_companies = proc_data.get("resultats", [])[:10]

    libelle_naf = ""
    if top_companies:
        libelle_naf = top_companies[0].get("libelle_code_naf", "")

    slug = slugify(f"{args.naf}-{libelle_naf}")
    filepath = PAPPERS_DIR / "secteurs" / f"{slug}.md"

    # Build top companies table
    top_rows = []
    for i, c in enumerate(top_companies, 1):
        siren = c.get("siren", "")
        denom = c.get("denomination", "")
        ca = c.get("chiffre_affaires", "")
        eff = c.get("effectif", "")
        e_slug = slugify(denom)
        link = f"[[brantham/pappers/entreprises/{siren}-{e_slug}]]"
        top_rows.append(f"| {i} | {denom} | {siren} | {ca} | {eff} | {link} |")

    # Build distressed companies table
    proc_rows = []
    for c in proc_companies:
        siren = c.get("siren", "")
        denom = c.get("denomination", "")
        ca = c.get("chiffre_affaires", "")
        procs = c.get("procedures_collectives", [])
        proc_type = procs[0].get("type", "") if procs else ""
        proc_date = procs[0].get("date_debut", "") if procs else ""
        e_slug = slugify(denom)
        link = f"[[brantham/pappers/entreprises/{siren}-{e_slug}]]"
        proc_rows.append(f"| {denom} | {siren} | {proc_type[:25]} | {proc_date} | {ca} | {link} |")

    # Sector playbook mapping
    sector_map = {
        "10": "agri-food", "11": "agri-food",
        "41": "btp", "42": "btp", "43": "btp",
        "45": "retail", "46": "retail", "47": "retail",
        "56": "restaurant",
        "25": "manufacturing", "28": "manufacturing", "29": "manufacturing",
        "62": "tech", "63": "tech",
        "68": "real-estate",
    }
    secteur_brantham = "autre"
    for prefix, sect in sector_map.items():
        if args.naf.startswith(prefix):
            secteur_brantham = sect
            break

    content = f"""---
type: secteur
code_naf: "{args.naf}"
libelle_naf: "{libelle_naf}"
secteur_brantham: {secteur_brantham}
nb_entreprises_actives: {total_active}
nb_procedures_en_cours:
ca_median:
effectif_median:
taux_defaillance:
date_fetch_pappers: "{today}"
tags: []
---

# Secteur: {libelle_naf} ({args.naf})

> Cartographie sectorielle via Pappers. Derniere maj: {today}.

## Vue d'Ensemble

| Metrique | Valeur | Date |
|----------|--------|------|
| Code NAF | {args.naf} | |
| Entreprises actives | {total_active} | {today} |
| Secteur Brantham | {secteur_brantham} | |

## Top Entreprises du Secteur

| Rang | Entreprise | SIREN | CA | Effectif | Lien |
|------|-----------|-------|-----|----------|------|
{chr(10).join(top_rows) if top_rows else '| — | — | — | — | — | — |'}

## Entreprises en Difficulte

| Entreprise | SIREN | Procedure | Date | CA | Lien |
|-----------|-------|-----------|------|-----|------|
{chr(10).join(proc_rows) if proc_rows else '| — | — | — | — | — | — |'}

## Repreneurs Potentiels

<!-- Top companies du secteur = acheteurs strategiques potentiels -->

| Entreprise | SIREN | CA | Effectif | Historique M&A | Lien |
|-----------|-------|-----|----------|----------------|------|
| — | — | — | — | — | — |

## Dynamique Sectorielle

### Tendances
-

### Signaux Faibles
-

### Risques Specifiques
-

## Playbook Brantham

[[brantham/knowledge/sectors/{secteur_brantham}-playbook]]

## Benchmark Valorisation

| Metrique | Multiple median | Fourchette | Source |
|----------|----------------|-----------|--------|
| EV/CA | | | |
| EV/EBITDA | | | |

## Notes

-

## Related

- [[brantham/pappers/_MOC]]
- [[brantham/_MOC]]
- [[brantham/knowledge/sectors/{secteur_brantham}-playbook]]
"""

    filepath.write_text(content)
    print(f"  -> {filepath}")
    print(f"  {total_active} entreprises actives")
    print(f"  {len(proc_companies)} en difficulte")
    print(f"  2 tokens consumed")


if __name__ == "__main__":
    main()
