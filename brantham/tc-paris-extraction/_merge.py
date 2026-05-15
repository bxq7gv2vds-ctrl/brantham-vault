#!/usr/bin/env python3
"""Merge tous les offres.csv et dossiers.csv des 94 dossiers TC Paris en 2 master CSVs.

Lecture robuste : utilise csv.DictReader pour gérer les multi-line fields,
guillemets, virgules dans cellules. Ajoute colonne 'dossier_folder' pour traçabilité.
"""
import csv
import os
import sys
from pathlib import Path

ROOT = Path("/Users/paul/Downloads/Dossiers Entreprises")
OUT = Path("/Users/paul/vault/brantham/tc-paris-extraction")
RAW = OUT / "raw-csv"

OFFRES_COLS = [
    "offre_id", "dossier_id", "fichier_source", "nom_repreneur",
    "forme_juridique_repreneur", "capital_repreneur", "rcs_repreneur",
    "adresse_repreneur", "dirigeant_repreneur", "groupe_appartenance",
    "type_offre", "date_offre", "societe_cessionnaire", "prix_total_eur",
    "prix_incorporels_eur", "prix_corporels_eur", "emplois_repris",
    "perimetre_actifs", "exclusions", "conditions_suspensives",
    "mode_financement", "ca_repreneur_eur", "resultat_exploitation_repreneur_eur",
    "resultat_net_repreneur_eur", "total_actif_eur", "capitaux_propres_eur",
    "validite_offre", "avocat_repreneur", "notes",
]

DOSSIERS_COLS = [
    "dossier_id", "nom_societe", "forme_juridique", "capital_social_eur",
    "rcs", "adresse_siege", "nom_commercial", "activite", "type_procedure",
    "date_ouverture", "tribunal", "administrateur_judiciaire", "cabinet_aj",
    "adresse_aj", "mandataire_judiciaire", "cabinet_mj", "juge_commissaire",
    "dldo", "effectif_total", "nb_offres_recues", "filiales", "secteur", "notes",
]


def find_csvs(name_prefix: str):
    """Find all CSVs starting with name_prefix (offres or dossiers)."""
    for dossier_dir in sorted(ROOT.iterdir()):
        if not dossier_dir.is_dir():
            continue
        for csv_file in dossier_dir.glob(f"{name_prefix}*.csv"):
            yield dossier_dir.name, csv_file


def merge(name_prefix: str, master_cols: list, out_file: Path):
    rows = []
    nb_files = 0
    nb_rows = 0
    issues = []
    for folder_name, csv_path in find_csvs(name_prefix):
        nb_files += 1
        try:
            with csv_path.open(encoding="utf-8", newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Normalise: keep only known columns, fill missing with empty
                    out_row = {"dossier_folder": folder_name}
                    for col in master_cols:
                        out_row[col] = row.get(col, "") or ""
                    rows.append(out_row)
                    nb_rows += 1
        except Exception as e:
            issues.append(f"{folder_name}: {e}")

    out_cols = ["dossier_folder"] + master_cols
    with out_file.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=out_cols, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    print(f"{out_file.name}: {nb_files} fichiers lus, {nb_rows} lignes écrites")
    if issues:
        print("  Issues:")
        for i in issues:
            print(f"  - {i}")


def copy_individual_csvs():
    """Copie chaque CSV individuel vers raw-csv/ pour archive avec préfixe de dossier."""
    RAW.mkdir(exist_ok=True)
    nb = 0
    for dossier_dir in sorted(ROOT.iterdir()):
        if not dossier_dir.is_dir():
            continue
        slug = dossier_dir.name.replace(" ", "_").replace("/", "_")
        for csv_file in dossier_dir.glob("offres*.csv"):
            dest = RAW / f"{slug}__{csv_file.name}"
            dest.write_bytes(csv_file.read_bytes())
            nb += 1
        for csv_file in dossier_dir.glob("dossiers*.csv"):
            dest = RAW / f"{slug}__{csv_file.name}"
            dest.write_bytes(csv_file.read_bytes())
            nb += 1
    print(f"raw-csv/: {nb} fichiers archivés")


if __name__ == "__main__":
    merge("offres", OFFRES_COLS, OUT / "master-offres.csv")
    merge("dossiers", DOSSIERS_COLS, OUT / "master-dossiers.csv")
    copy_individual_csvs()
