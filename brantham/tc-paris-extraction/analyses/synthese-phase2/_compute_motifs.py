#!/usr/bin/env python3
"""Extract and theme motifs_tribunal_verbatim and motifs_rejet for hierarchy livrable."""
import json
import pandas as pd
import numpy as np
from pathlib import Path
from collections import Counter
import re

BASE = Path("/Users/paul/vault/brantham/tc-paris-extraction")
OUT = BASE / "analyses" / "synthese-phase2"

df = pd.read_pickle(OUT / "offres.pkl")
dd = pd.read_pickle(OUT / "dossiers.pkl")

# 1. Collect all motifs_tribunal_verbatim (from winning offres + dossier)
motifs_win = df.loc[df["retenue"].isin(["oui", "amelioree_puis_retenue"]), ["dossier_id", "cible", "motifs_tribunal"]].dropna(subset=["motifs_tribunal"])
print(f"Motifs tribunal (winners): {len(motifs_win)} entries")
with open(OUT / "motifs_winners.txt", "w") as f:
    for _, r in motifs_win.iterrows():
        f.write(f"\n### {r['cible']} (dossier {r['dossier_id']})\n{r['motifs_tribunal']}\n")

motifs_lose = df.loc[df["retenue"] == "non", ["dossier_id", "cible", "motifs_rejet"]].dropna(subset=["motifs_rejet"])
print(f"Motifs rejet (losers): {len(motifs_lose)} entries")
with open(OUT / "motifs_losers.txt", "w") as f:
    for _, r in motifs_lose.iterrows():
        f.write(f"\n### {r['cible']} (dossier {r['dossier_id']})\n{r['motifs_rejet']}\n")

motifs_dossier = dd[["dossier_id", "cible", "motifs_tribunal_verbatim", "motifs_rejet_synthese", "enseignement_clef"]].dropna(subset=["motifs_tribunal_verbatim"], how="all")
print(f"Dossier-level motifs: {len(motifs_dossier)}")

# 2. Theme detection — simple keyword search in motifs
THEMES = {
    "prix_superieur": [r"prix.{0,30}(superieur|sup\.|plus eleve|plus élevé|le plus eleve|le plus élevé|meilleur prix)",
                      r"offre.{0,30}prix.{0,30}(superieur|haute|elev)", r"\bmieux disant\b"],
    "emplois_max": [r"emplois.{0,40}(maximum|plus eleve|preserves|preserve|sauvegard|repris.{0,10}plus|tous|integralite|intégralité)",
                   r"sauvegarde.{0,20}emplois", r"maintien.{0,20}emplois", r"reprise.{0,20}integrale.{0,20}salari"],
    "perennite": [r"perennite", r"pérennité", r"viabilite", r"viabilité", r"continuite", r"continuité", r"poursuite.{0,20}activite"],
    "credibilite_financiere": [r"capacite financiere", r"capacité financière", r"solidite", r"solidité", r"financement.{0,20}(documente|atteste|ferme|securise)",
                              r"engagement bancaire", r"attestation bancaire", r"fonds propres"],
    "experience_secteur": [r"experience.{0,20}secteur", r"connaissance.{0,20}metier", r"connaissance.{0,20}métier", r"expertise"],
    "industriel": [r"projet industriel", r"plan industriel", r"strategie industrielle", r"vision industrielle", r"plan d.affaires"],
    "synergies": [r"synergies", r"complementarite", r"complémentarité"],
    "garanties": [r"garantie", r"caution", r"engagement.{0,20}ferme"],
    "absence_cs": [r"sans condition", r"aucune condition", r"non conditionnel", r"inconditionnel", r"ferme.{0,20}definitif", r"ferme.{0,20}définitif"],
    "soutien_external": [r"soutien", r"appui", r"lettre.{0,20}intention", r"lettre.{0,20}engagement", r"recommandation"],
    "preservation_marque": [r"marque", r"savoir.faire", r"enseigne", r"identite", r"identité"],
}

def themify(text_series):
    counts = Counter()
    matches = {t: [] for t in THEMES}
    for s in text_series:
        if not isinstance(s, str): continue
        sl = s.lower()
        for theme, pats in THEMES.items():
            for p in pats:
                if re.search(p, sl):
                    counts[theme] += 1
                    matches[theme].append(s[:300])
                    break
    return counts, matches

win_counts, win_matches = themify(motifs_win["motifs_tribunal"])
lose_counts, lose_matches = themify(motifs_lose["motifs_rejet"])

print("\n=== WINNERS — themes invoqués par le tribunal ===")
for t, n in win_counts.most_common():
    print(f"  {t:25s} {n}/{len(motifs_win)} = {100*n/len(motifs_win):.0f}%")

print("\n=== LOSERS — motifs de rejet ===")
for t, n in lose_counts.most_common():
    print(f"  {t:25s} {n}/{len(motifs_lose)} = {100*n/len(motifs_lose):.0f}%")

# Save matches for citation
with open(OUT / "themes_matches.json", "w") as f:
    json.dump({"winners": dict(win_matches), "losers": dict(lose_matches)}, f, indent=2, default=str)

# Pricing multiples
print("\n=== Multiples CA (gagnants seulement) ===")
g = df[df["retenue"].isin(["oui", "amelioree_puis_retenue"])].copy()
g["mult_ca"] = g.apply(lambda r: r["prix_total"]/r["ca_eur"] if (r["ca_eur"] and r["prix_total"] and r["ca_eur"]>0) else None, axis=1)
print(g[["cible", "prix_total", "ca_eur", "mult_ca", "pct_reprise"]].dropna(subset=["mult_ca"]).to_string())

# Sector-level winners
print("\n=== Winners par secteur (NAF) ===")
sector_stats = []
for sec, grp in df.groupby("naf"):
    n = len(grp)
    n_win = (grp["retenue"].isin(["oui","amelioree_puis_retenue"])).sum()
    n_lose = (grp["retenue"] == "non").sum()
    n_dec = n_win + n_lose
    sector_stats.append({"naf": sec, "n_total": n, "n_win": int(n_win), "n_lose": int(n_lose), "n_decided": int(n_dec)})
ss = pd.DataFrame(sector_stats).sort_values("n_total", ascending=False)
print(ss.head(20).to_string())
ss.to_csv(OUT / "sector_stats.csv", index=False)
