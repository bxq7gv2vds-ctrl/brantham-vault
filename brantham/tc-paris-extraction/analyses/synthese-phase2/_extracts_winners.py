#!/usr/bin/env python3
"""Extract winners' rhetorical phrases for the library livrable."""
import pandas as pd
from pathlib import Path
import json

BASE = Path("/Users/paul/vault/brantham/tc-paris-extraction")
OUT = BASE / "analyses" / "synthese-phase2"

df = pd.read_pickle(OUT / "offres.pkl")
WIN = df[df["retenue"].isin(["oui", "amelioree_puis_retenue"])].copy()

print("=== POSITIONNEMENT (winners) ===")
for _, r in WIN.dropna(subset=["phrase_positionnement"]).iterrows():
    if r["phrase_positionnement"] and len(str(r["phrase_positionnement"])) > 30:
        print(f"\n[{r['cible'][:40]} | {r['offre_id']}]")
        print(f"  {str(r['phrase_positionnement'])[:400]}")

print("\n\n=== VISION STRATEGIQUE (winners) ===")
for _, r in WIN.dropna(subset=["phrase_vision"]).iterrows():
    if r["phrase_vision"] and len(str(r["phrase_vision"])) > 30:
        print(f"\n[{r['cible'][:40]} | {r['offre_id']}]")
        print(f"  {str(r['phrase_vision'])[:400]}")

print("\n\n=== ENGAGEMENT SOCIAL (winners) ===")
for _, r in WIN.dropna(subset=["phrase_engagement_social"]).iterrows():
    if r["phrase_engagement_social"] and len(str(r["phrase_engagement_social"])) > 30:
        print(f"\n[{r['cible'][:40]} | {r['offre_id']}]")
        print(f"  {str(r['phrase_engagement_social'])[:400]}")

print("\n\n=== JUSTIFICATION PRIX (winners) ===")
for _, r in WIN.dropna(subset=["phrase_prix"]).iterrows():
    if r["phrase_prix"] and len(str(r["phrase_prix"])) > 30:
        print(f"\n[{r['cible'][:40]} | {r['offre_id']}]")
        print(f"  {str(r['phrase_prix'])[:400]}")

# Track records highest
print("\n\n=== Profils winners (track record, exp) ===")
print(WIN[["cible", "forme_repreneur", "track_record_count", "exp_sectorielle", "exp_annees", "capacite_financiere", "prix_total", "pct_reprise", "nb_cs"]].to_string())

# Sector breakdown of winners
print("\n\n=== Winners par dossier (47) ===")
print(WIN[["dossier_id", "cible", "naf", "prix_total", "nb_salaries_repris", "nb_total_salaries", "pct_reprise", "forme_repreneur"]].to_string())
