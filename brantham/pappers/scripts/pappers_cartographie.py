#!/usr/bin/env python3
"""
pappers_cartographie.py — Build group cartography from Pappers.

Fetches the cartography endpoint for a company and maps the full group:
parent, subsidiaries, sister companies, shared directors.

Usage:
  uv run pappers_cartographie.py 123456789
  uv run pappers_cartographie.py 123456789 --depth 2  # Follow subsidiaries
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


def fetch_cartographie(siren: str, api_key: str) -> dict:
    resp = requests.get(
        f"{API_BASE}/entreprise/cartographie",
        params={"api_token": api_key, "siren": siren},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def main():
    parser = argparse.ArgumentParser(description="Build group cartography from Pappers")
    parser.add_argument("siren", help="SIREN of target company")
    parser.add_argument("--depth", type=int, default=1, help="Follow subsidiary depth")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    api_key = get_api_key()
    siren = args.siren.replace(" ", "")
    today = date.today().isoformat()

    print(f"Fetching cartography for {siren}...")
    data = fetch_cartographie(siren, api_key)

    if args.dry_run:
        import json
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return

    # Extract main company info
    denom = data.get("denomination", data.get("nom_entreprise", "inconnu"))
    slug = slugify(denom)

    # Extract related entities
    filiales = data.get("filiales", []) or []
    participations = data.get("participations", []) or []
    actionnaires = data.get("actionnaires", []) or []
    dirigeants_communs = data.get("representants_communs", []) or []

    # Also check alternate structure keys
    liens = data.get("liens", []) or []

    all_entities = []

    # Process filiales
    for f in filiales:
        all_entities.append({
            "denom": f.get("denomination", ""),
            "siren": f.get("siren", ""),
            "relation": "Filiale",
            "pct": f.get("pourcentage", ""),
            "ca": f.get("chiffre_affaires", ""),
            "statut": "Active" if not f.get("entreprise_cessee") else "Cessée",
        })

    # Process actionnaires
    for a in actionnaires:
        all_entities.append({
            "denom": a.get("denomination", a.get("nom", "")),
            "siren": a.get("siren", ""),
            "relation": "Actionnaire",
            "pct": a.get("pourcentage", ""),
            "ca": a.get("chiffre_affaires", ""),
            "statut": "Active",
        })

    # Process participations
    for p in participations:
        all_entities.append({
            "denom": p.get("denomination", ""),
            "siren": p.get("siren", ""),
            "relation": "Participation",
            "pct": p.get("pourcentage", ""),
            "ca": p.get("chiffre_affaires", ""),
            "statut": "Active" if not p.get("entreprise_cessee") else "Cessée",
        })

    # Process liens (alternate API structure)
    for l in liens:
        all_entities.append({
            "denom": l.get("denomination", l.get("nom_entreprise", "")),
            "siren": l.get("siren", ""),
            "relation": l.get("type_lien", "Lié"),
            "pct": l.get("pourcentage", ""),
            "ca": l.get("chiffre_affaires", ""),
            "statut": "Active",
        })

    nb_entites = len(all_entities) + 1  # +1 for target company

    # Build entity rows
    entity_rows = []
    for e in all_entities:
        e_slug = slugify(e["denom"])
        e_siren = e["siren"]
        link = f"[[brantham/pappers/entreprises/{e_siren}-{e_slug}]]" if e_siren else ""
        entity_rows.append(
            f"| {e['denom']} | {e_siren} | {e['relation']} | {e['pct']} | {e['ca']} | {e['statut']} | {link} |"
        )

    # Build dirigeants communs rows
    dir_rows = []
    for d in dirigeants_communs:
        d_nom = d.get("nom", "")
        d_prenom = d.get("prenom", "")
        d_slug = slugify(f"{d_prenom}-{d_nom}")
        mandats = d.get("nombre_mandats", d.get("nb_mandats", ""))
        entreprises = ", ".join(e.get("denomination", "")[:20] for e in d.get("entreprises", [])[:3])
        link = f"[[brantham/pappers/dirigeants/{d_slug}]]"
        dir_rows.append(f"| {d_prenom} {d_nom} | {mandats} | {entreprises} | {link} |")

    # Build tree
    tree_lines = [f"{denom} ({siren})"]
    for e in all_entities:
        pct_str = f" — {e['pct']}%" if e['pct'] else ""
        prefix = "  |-- " if e["relation"] in ("Filiale", "Participation") else "  ^-- "
        tree_lines.append(f"{prefix}{e['denom']} ({e['siren']}){pct_str}")

    filepath = PAPPERS_DIR / "cartographie" / f"{slug}.md"

    content = f"""---
type: cartographie
nom_groupe: "{denom}"
siren_tete: "{siren}"
nb_entites: {nb_entites}
ca_consolide:
effectif_consolide:
secteurs: []
regions: []
dirigeant_cle: ""
date_fetch_pappers: "{today}"
tags: []
---

# Cartographie: {denom}

> Cartographie groupe via Pappers. Derniere maj: {today}.

## Tete de Groupe

[[brantham/pappers/entreprises/{siren}-{slug}]]

## Organigramme

```
{chr(10).join(tree_lines)}
```

## Entites du Groupe ({len(all_entities)} entites)

| Denomination | SIREN | Relation | % Detention | CA | Statut | Lien |
|-------------|-------|----------|-------------|-----|--------|------|
{chr(10).join(entity_rows) if entity_rows else '| — | — | — | — | — | — | — |'}

## Dirigeants Communs

| Dirigeant | Mandats | Entites | Lien |
|-----------|---------|---------|------|
{chr(10).join(dir_rows) if dir_rows else '| — | — | — | — |'}

## Pertinence Brantham

- Type: repreneur | cible | ecosysteme
- Appetit M&A:
- Capacite financiere:
- Secteurs cibles:

## Notes

-

## Related

- [[brantham/pappers/_MOC]]
- [[brantham/_MOC]]
- [[brantham/pappers/entreprises/{siren}-{slug}]]
"""

    filepath.write_text(content)
    print(f"  -> {filepath}")
    print(f"  {len(all_entities)} entites liees trouvees")
    print(f"  {len(dirigeants_communs)} dirigeants communs")
    print(f"  1 token consumed")


if __name__ == "__main__":
    main()
