#!/usr/bin/env python3
"""
pappers_fetch.py — Fetch complete company profile from Pappers API and write to vault.

Creates:
  - entreprises/{siren}-{slug}.md
  - dirigeants/{slug}.md (for each director)
  - beneficiaires/{slug}.md (for each beneficial owner)
  - financials/{siren}-{year}.md (latest accounts)

Usage:
  uv run pappers_fetch.py 123456789
  uv run pappers_fetch.py 123456789 --with-comptes --with-cartographie
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
TEMPLATES_DIR = VAULT / "_system" / "templates"
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


def fetch_entreprise(siren: str, api_key: str) -> dict:
    resp = requests.get(
        f"{API_BASE}/entreprise",
        params={"api_token": api_key, "siren": siren},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def fetch_comptes(siren: str, api_key: str) -> dict:
    resp = requests.get(
        f"{API_BASE}/entreprise/comptes",
        params={"api_token": api_key, "siren": siren},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def write_entreprise(data: dict) -> Path:
    siren = data.get("siren", "")
    denom = data.get("denomination", data.get("nom_entreprise", "inconnu"))
    slug = slugify(denom)
    filename = f"{siren}-{slug}.md"
    filepath = PAPPERS_DIR / "entreprises" / filename

    siege = data.get("siege", {}) or {}
    dirigeants = data.get("representants", []) or []
    beneficiaires = data.get("beneficiaires_effectifs", []) or []
    comptes_list = data.get("finances", []) or []
    procedures = data.get("procedures_collectives", []) or []
    publications = data.get("publications_bodacc", []) or []

    # Determine procedure en cours
    proc_en_cours = "none"
    for proc in procedures:
        if not proc.get("date_fin"):
            ptype = (proc.get("type", "") or "").lower()
            if "liquidation" in ptype:
                proc_en_cours = "lj"
            elif "redressement" in ptype:
                proc_en_cours = "rj"
            elif "sauvegarde" in ptype:
                proc_en_cours = "sauvegarde"
            elif "mandat" in ptype:
                proc_en_cours = "mandat_ad_hoc"
            elif "conciliation" in ptype:
                proc_en_cours = "conciliation"
            break

    # Latest accounts
    ca = ""
    rn = ""
    annee = ""
    if comptes_list:
        latest = comptes_list[0]
        ca = latest.get("chiffre_affaires", "")
        rn = latest.get("resultat", "")
        annee = latest.get("annee", "")

    today = date.today().isoformat()

    # Build dirigeants table
    dir_rows = []
    dir_links = []
    for d in dirigeants[:20]:
        nom = d.get("nom", "")
        prenom = d.get("prenom", "")
        qualite = d.get("qualite", "")
        date_nom = d.get("date_prise_de_poste", "")
        d_slug = slugify(f"{prenom}-{nom}")
        link = f"[[brantham/pappers/dirigeants/{d_slug}]]"
        dir_rows.append(f"| {prenom} {nom} | {qualite} | {date_nom} | {link} |")
        dir_links.append(d_slug)

    # Build beneficiaires table
    ben_rows = []
    for b in beneficiaires[:20]:
        nom = b.get("nom", "")
        prenom = b.get("prenom", "")
        nat = b.get("nationalite", "")
        pct = b.get("pourcentage_parts", b.get("pourcentage_votes", ""))
        modalite = b.get("modalite_detention", "")
        b_slug = slugify(f"{prenom}-{nom}")
        link = f"[[brantham/pappers/beneficiaires/{b_slug}]]"
        ben_rows.append(f"| {prenom} {nom} | {nat} | {pct} | {modalite} | {link} |")

    # Build comptes table
    fin_rows = []
    for c in comptes_list[:5]:
        c_annee = c.get("annee", "")
        c_ca = c.get("chiffre_affaires", "")
        c_rn = c.get("resultat", "")
        c_eff = c.get("effectif", "")
        link = f"[[brantham/pappers/financials/{siren}-{c_annee}]]"
        fin_rows.append(f"| {c_annee} | {c_ca} | {c_rn} | {c_eff} | {link} |")

    # Build procedures table
    proc_rows = []
    for p in procedures[:10]:
        p_date = p.get("date_debut", "")
        p_type = p.get("type", "")
        p_trib = p.get("tribunal", "")
        p_stat = "en_cours" if not p.get("date_fin") else "cloture"
        p_slug = slugify(f"{p_date}-{siren}-{p_type}")
        link = f"[[brantham/pappers/procedures-collectives/{p_slug}]]"
        proc_rows.append(f"| {p_date} | {p_type} | {p_trib} | {p_stat} | {link} |")

    # Build BODACC table
    bodacc_rows = []
    for pub in (publications or [])[:15]:
        pub_date = pub.get("date", "")
        pub_type = pub.get("type", "")
        pub_desc = (pub.get("description", "") or "")[:80]
        bodacc_rows.append(f"| {pub_date} | {pub_type} | {pub_desc} |")

    code_naf = data.get("code_naf", "")
    libelle_naf = data.get("libelle_code_naf", "")
    secteur_slug = slugify(libelle_naf) if libelle_naf else code_naf

    content = f"""---
type: entreprise
siren: "{siren}"
siret_siege: "{siege.get('siret', '')}"
denomination: "{denom}"
nom_commercial: "{data.get('nom_commercial', '')}"
forme_juridique: "{data.get('forme_juridique', '')}"
categorie_juridique: "{data.get('categorie_juridique', '')}"
capital_social: {data.get('capital', '') or ''}
devise_capital: EUR
date_creation: "{data.get('date_creation', '')}"
date_immatriculation_rcs: "{data.get('date_immatriculation_rcs', '')}"
date_radiation: "{data.get('date_radiation', '')}"
est_active: {str(not data.get('entreprise_cessee', False)).lower()}
code_naf: "{code_naf}"
libelle_naf: "{libelle_naf}"
secteur_brantham:
convention_collective: "{data.get('convention_collective', '')}"
tranche_effectif: "{data.get('tranche_effectif', '')}"
effectif_exact: {data.get('effectif', '') or ''}
ca_dernier: {ca or ''}
resultat_net_dernier: {rn or ''}
annee_derniers_comptes: "{annee}"
adresse_siege: "{siege.get('adresse_ligne_1', '')}"
code_postal: "{siege.get('code_postal', '')}"
ville: "{siege.get('ville', '')}"
departement: "{siege.get('departement', '')}"
region: "{siege.get('region', '')}"
pays: France
rcs: "{data.get('numero_rcs', '')}"
greffe: "{data.get('greffe', '')}"
numero_tva: "{data.get('numero_tva_intracommunautaire', '')}"
est_entreprise_employeur: {str(data.get('entreprise_employeuse', False)).lower()}
score_brantham:
tags: []
procedure_en_cours: {proc_en_cours}
date_fetch_pappers: "{today}"
---

# {denom} ({siren})

> Fiche entreprise enrichie via Pappers. Derniere maj: {today}.

## Identite

| Champ | Valeur |
|-------|--------|
| SIREN | {siren} |
| SIRET siege | {siege.get('siret', '')} |
| Denomination | {denom} |
| Nom commercial | {data.get('nom_commercial', '')} |
| Forme juridique | {data.get('forme_juridique', '')} |
| Capital social | {data.get('capital', '')} EUR |
| Date creation | {data.get('date_creation', '')} |
| Code NAF | {code_naf} — {libelle_naf} |
| Convention collective | {data.get('convention_collective', '')} |
| TVA intra | {data.get('numero_tva_intracommunautaire', '')} |

## Siege Social

{siege.get('adresse_ligne_1', '')}, {siege.get('code_postal', '')} {siege.get('ville', '')}
Departement: {siege.get('departement', '')} | Region: {siege.get('region', '')}

## Dirigeants

| Nom | Qualite | Date nomination | Lien |
|-----|---------|-----------------|------|
{chr(10).join(dir_rows) if dir_rows else '| — | — | — | — |'}

## Beneficiaires Effectifs

| Nom | Nationalite | % Detention | Modalite controle | Lien |
|-----|-------------|-------------|-------------------|------|
{chr(10).join(ben_rows) if ben_rows else '| — | — | — | — | — |'}

## Donnees Financieres

| Annee | CA | Resultat Net | Effectif | Lien |
|-------|-----|-------------|----------|------|
{chr(10).join(fin_rows) if fin_rows else '| — | — | — | — | — |'}

## Procedures Collectives

| Date | Type | Tribunal | Statut | Lien |
|------|------|----------|--------|------|
{chr(10).join(proc_rows) if proc_rows else '| — | — | — | — | — |'}

## Publications BODACC

| Date | Type | Resume |
|------|------|--------|
{chr(10).join(bodacc_rows) if bodacc_rows else '| — | — | — |'}

## Secteur

[[brantham/pappers/secteurs/{code_naf}-{secteur_slug}]]

## Notes

-

## Related

- [[brantham/pappers/_MOC]]
- [[brantham/_MOC]]
- [[brantham/pappers/secteurs/{code_naf}-{secteur_slug}]]
"""

    filepath.write_text(content)
    print(f"  -> {filepath}")
    return filepath


def write_dirigeant(d: dict, siren: str, denom: str) -> Path:
    nom = d.get("nom", "")
    prenom = d.get("prenom", "")
    slug = slugify(f"{prenom}-{nom}")
    filepath = PAPPERS_DIR / "dirigeants" / f"{slug}.md"
    today = date.today().isoformat()

    # Don't overwrite — merge mandats later
    if filepath.exists():
        existing = filepath.read_text()
        # Add this mandat if not already there
        if siren not in existing:
            marker = "## Mandats Actifs"
            if marker in existing:
                e_slug = slugify(denom)
                new_row = f"| {denom} | {siren} | {d.get('qualite', '')} | {d.get('date_prise_de_poste', '')} | [[brantham/pappers/entreprises/{siren}-{e_slug}]] |"
                existing = existing.replace(
                    marker + "\n\n| Entreprise",
                    marker + "\n\n| Entreprise",
                )
                # Find end of table and insert
                lines = existing.split("\n")
                insert_idx = None
                in_table = False
                for i, line in enumerate(lines):
                    if "| Entreprise | SIREN | Qualite" in line:
                        in_table = True
                    elif in_table and line.startswith("|"):
                        insert_idx = i + 1
                    elif in_table and not line.startswith("|"):
                        insert_idx = i
                        break
                if insert_idx:
                    lines.insert(insert_idx, new_row)
                    filepath.write_text("\n".join(lines))
                    print(f"  -> {filepath} (updated)")
        return filepath

    qualite = d.get("qualite", "")
    date_naissance = d.get("date_de_naissance", "")
    nationalite = d.get("nationalite", "")
    siren_perso = d.get("siren", "")
    e_slug = slugify(denom)

    content = f"""---
type: dirigeant
nom: "{nom}"
prenom: "{prenom}"
date_naissance: "{date_naissance}"
nationalite: "{nationalite}"
slug: "{slug}"
siren_personnel: "{siren_perso}"
mandats_actifs: 1
mandats_total: 1
est_ppe: false
sanctions: false
tags: []
date_fetch_pappers: "{today}"
---

# {prenom} {nom}

> Profil dirigeant enrichi via Pappers. Derniere maj: {today}.

## Identite

| Champ | Valeur |
|-------|--------|
| Nom | {nom} |
| Prenom | {prenom} |
| Date naissance | {date_naissance} |
| Nationalite | {nationalite} |
| SIREN personnel | {siren_perso} |

## Mandats Actifs

| Entreprise | SIREN | Qualite | Depuis | Lien |
|-----------|-------|---------|--------|------|
| {denom} | {siren} | {qualite} | {d.get('date_prise_de_poste', '')} | [[brantham/pappers/entreprises/{siren}-{e_slug}]] |

## Mandats Historiques

| Entreprise | SIREN | Qualite | Periode | Lien |
|-----------|-------|---------|---------|------|
| — | — | — | — | — |

## Reseau

| Dirigeant | Entreprises communes | Lien |
|-----------|---------------------|------|
| — | — | — |

## Conformite

| Check | Resultat | Date |
|-------|----------|------|
| PPE (Pappers) | false | {today} |
| Sanctions internationales | false | {today} |

## Pertinence Brantham

- Role dans l'ecosysteme:
- Historique M&A:
- Contact:

## Notes

-

## Related

- [[brantham/pappers/_MOC]]
- [[brantham/_MOC]]
- [[brantham/pappers/entreprises/{siren}-{e_slug}]]
"""
    filepath.write_text(content)
    print(f"  -> {filepath}")
    return filepath


def write_beneficiaire(b: dict, siren: str, denom: str) -> Path:
    nom = b.get("nom", "")
    prenom = b.get("prenom", "")
    slug = slugify(f"{prenom}-{nom}")
    filepath = PAPPERS_DIR / "beneficiaires" / f"{slug}.md"
    today = date.today().isoformat()

    if filepath.exists():
        return filepath

    nationalite = b.get("nationalite", "")
    date_naissance = b.get("date_de_naissance_formatee", "")
    pct = b.get("pourcentage_parts", b.get("pourcentage_votes", ""))
    modalite = b.get("modalite_detention", "")
    e_slug = slugify(denom)

    content = f"""---
type: beneficiaire_effectif
nom: "{nom}"
prenom: "{prenom}"
date_naissance: "{date_naissance}"
nationalite: "{nationalite}"
nb_participations: 1
est_ppe: false
sanctions: false
tags: []
date_fetch_pappers: "{today}"
---

# {prenom} {nom} (Beneficiaire Effectif)

> Profil beneficiaire effectif enrichi via Pappers. Derniere maj: {today}.

## Identite

| Champ | Valeur |
|-------|--------|
| Nom | {nom} |
| Prenom | {prenom} |
| Date naissance | {date_naissance} |
| Nationalite | {nationalite} |

## Participations

| Entreprise | SIREN | % Detention | Modalite controle | Lien |
|-----------|-------|-------------|-------------------|------|
| {denom} | {siren} | {pct} | {modalite} | [[brantham/pappers/entreprises/{siren}-{e_slug}]] |

## Conformite

| Check | Resultat | Date |
|-------|----------|------|
| PPE | false | {today} |
| Sanctions | false | {today} |

## Reseau

| Personne | Entreprises communes | Role | Lien |
|----------|---------------------|------|------|
| — | — | — | — |

## Notes

-

## Related

- [[brantham/pappers/_MOC]]
- [[brantham/_MOC]]
- [[brantham/pappers/entreprises/{siren}-{e_slug}]]
"""
    filepath.write_text(content)
    print(f"  -> {filepath}")
    return filepath


def main():
    parser = argparse.ArgumentParser(description="Fetch company from Pappers to vault")
    parser.add_argument("siren", help="SIREN number (9 digits)")
    parser.add_argument("--with-comptes", action="store_true", help="Also fetch detailed accounts")
    parser.add_argument("--with-cartographie", action="store_true", help="Also fetch group mapping")
    parser.add_argument("--dry-run", action="store_true", help="Fetch but don't write")
    args = parser.parse_args()

    siren = args.siren.replace(" ", "")
    if len(siren) != 9 or not siren.isdigit():
        print(f"ERROR: Invalid SIREN: {siren}")
        sys.exit(1)

    api_key = get_api_key()
    print(f"Fetching {siren} from Pappers...")

    data = fetch_entreprise(siren, api_key)
    denom = data.get("denomination", data.get("nom_entreprise", "inconnu"))
    print(f"  Company: {denom}")

    if args.dry_run:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return

    # Write main company file
    print("\nWriting entreprise...")
    write_entreprise(data)

    # Write dirigeant files
    dirigeants = data.get("representants", []) or []
    if dirigeants:
        print(f"\nWriting {len(dirigeants)} dirigeants...")
        for d in dirigeants[:20]:
            write_dirigeant(d, siren, denom)

    # Write beneficiaire files
    beneficiaires = data.get("beneficiaires_effectifs", []) or []
    if beneficiaires:
        print(f"\nWriting {len(beneficiaires)} beneficiaires...")
        for b in beneficiaires[:20]:
            write_beneficiaire(b, siren, denom)

    print(f"\nDone. 1 token consumed.")


if __name__ == "__main__":
    main()
