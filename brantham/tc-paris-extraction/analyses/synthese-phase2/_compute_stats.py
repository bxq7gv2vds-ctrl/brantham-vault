#!/usr/bin/env python3
"""Compute all comparative stats between retenues vs rejetees vs en_attente."""
import json
import pandas as pd
import numpy as np
from pathlib import Path
from collections import Counter

BASE = Path("/Users/paul/vault/brantham/tc-paris-extraction")
OUT = BASE / "analyses" / "synthese-phase2"

df = pd.read_pickle(OUT / "offres.pkl")
dd = pd.read_pickle(OUT / "dossiers.pkl")

# Define groupings
df["status"] = df["retenue"].map({
    "oui": "retenue",
    "amelioree_puis_retenue": "retenue",
    "non": "rejetee",
    "en_attente": "en_attente",
    "NR": "NR"
})

print("=== Status groups ===")
print(df["status"].value_counts())

WIN = df[df["status"] == "retenue"].copy()
LOSE = df[df["status"] == "rejetee"].copy()
ALL_DECIDED = df[df["status"].isin(["retenue", "rejetee"])].copy()
print(f"\nWIN n={len(WIN)} | LOSE n={len(LOSE)} | DECIDED n={len(ALL_DECIDED)}")

# ============== STAT FUNCTIONS ==============

def desc_num(series, name=""):
    s = pd.to_numeric(series, errors="coerce").dropna()
    if len(s) == 0:
        return {"n": 0}
    return {
        "n": int(len(s)),
        "median": float(s.median()),
        "mean": float(s.mean()),
        "p25": float(s.quantile(0.25)),
        "p75": float(s.quantile(0.75)),
        "min": float(s.min()),
        "max": float(s.max()),
    }


def desc_cat(series, top_n=10):
    return series.value_counts(dropna=False).head(top_n).to_dict()


def pct_true(series):
    s = series.dropna()
    if len(s) == 0:
        return None
    s_bool = s.astype(bool)
    return round(100 * s_bool.sum() / len(s_bool), 1)


def compare_num(col):
    w = pd.to_numeric(WIN[col], errors="coerce").dropna()
    l = pd.to_numeric(LOSE[col], errors="coerce").dropna()
    return {
        "win_n": len(w), "win_median": float(w.median()) if len(w) else None,
        "win_mean": float(w.mean()) if len(w) else None,
        "lose_n": len(l), "lose_median": float(l.median()) if len(l) else None,
        "lose_mean": float(l.mean()) if len(l) else None,
    }


def compare_bool(col):
    w = WIN[col].dropna()
    l = LOSE[col].dropna()
    return {
        "win_n": len(w), "win_pct_true": pct_true(w),
        "lose_n": len(l), "lose_pct_true": pct_true(l),
    }


def compare_cat(col, vals=None):
    """For categorical: returns pct of each value in each group."""
    out = {}
    w = WIN[col].dropna()
    l = LOSE[col].dropna()
    all_vals = vals or sorted(set(list(w.unique()) + list(l.unique())))
    out["categories"] = {}
    for v in all_vals:
        out["categories"][v] = {
            "win_pct": round(100 * (w == v).sum() / max(len(w), 1), 1),
            "lose_pct": round(100 * (l == v).sum() / max(len(l), 1), 1),
        }
    out["win_n"] = len(w)
    out["lose_n"] = len(l)
    return out


# ============== COMPUTE ALL ==============
report = {}
report["counts"] = {
    "total_offres": len(df),
    "retenues": len(WIN),
    "rejetees": len(LOSE),
    "en_attente": int((df["status"] == "en_attente").sum()),
    "NR": int((df["status"] == "NR").sum()),
    "dossiers": len(dd),
}

# Sector distribution
report["secteur_dist"] = desc_cat(df["naf"], 30)
report["secteur_winners"] = desc_cat(WIN["naf"], 30)

# Procedure
report["procedure_dist"] = desc_cat(df["procedure"])
report["procedure_winners"] = desc_cat(WIN["procedure"])

# Forme repreneur
report["forme_dist"] = desc_cat(df["forme_repreneur"], 20)
report["forme_winners"] = desc_cat(WIN["forme_repreneur"], 20)
report["forme_lose"] = desc_cat(LOSE["forme_repreneur"], 20)

# Effectif / CA distribution
report["ca_global"] = desc_num(df["ca_eur"])
report["ca_winners"] = desc_num(WIN["ca_eur"])
report["effectif_global"] = desc_num(df["effectif"])
report["effectif_winners"] = desc_num(WIN["effectif"])

# Prix
report["prix_global"] = desc_num(df["prix_total"])
report["prix_winners"] = desc_num(WIN["prix_total"])
report["prix_losers"] = desc_num(LOSE["prix_total"])

# Multiple sur CA cible (où on a les deux)
df["multiple_ca"] = df.apply(
    lambda r: r["prix_total"] / r["ca_eur"] if (r["ca_eur"] and r["prix_total"] and r["ca_eur"] > 0) else None,
    axis=1
)
report["multiple_ca_global"] = desc_num(df["multiple_ca"])
report["multiple_ca_winners"] = desc_num(df.loc[df["status"] == "retenue", "multiple_ca"])
report["multiple_ca_losers"] = desc_num(df.loc[df["status"] == "rejetee", "multiple_ca"])

# Pct reprise effectifs
report["pct_reprise_global"] = desc_num(df["pct_reprise"])
report["pct_reprise_winners"] = desc_num(WIN["pct_reprise"])
report["pct_reprise_losers"] = desc_num(LOSE["pct_reprise"])

# Variables comparées entre retenues et rejetées
NUM_COLS = [
    "prix_total", "incorporels", "corporels", "ca_eur", "ebitda_eur",
    "effectif", "nb_sites", "nb_concurrents", "nb_salaries_repris",
    "nb_total_salaries", "pct_reprise", "nb_licenciements",
    "engagement_emplois_mois", "apport_fp", "dette_montant",
    "bfr_redemarrage", "tresorerie_securite", "incessibilite_mois",
    "caution_dirig_montant", "penalites_social", "nb_cs",
    "nb_pages_total", "nb_pages_corps", "nb_pages_annexes",
    "nb_erreurs", "track_record_count", "exp_annees",
    "ca_an1", "ca_an3", "ebitda_an3", "capex", "synergies_chiffrees",
    "charges_augmentatives", "L642_12_montant",
]
report["numeric_compare"] = {c: compare_num(c) for c in NUM_COLS}

BOOL_COLS = [
    "L642_12_al4", "irp_cse", "bp_3ans", "dette_engagement_ferme",
    "dette_lettre_confort", "non_demembrement", "aucune_cs",
    "exec_summary", "annexes_kbis", "annexes_cv_dirigeants",
    "annexes_attest_bancaire", "annexes_lettres_soutien_clients",
    "annexes_lettres_soutien_collectivites", "annexes_business_plan",
    "annexes_organigramme_cible", "annexes_comptes_sociaux_3ans",
    "annexes_attest_fisc_sociale", "annexes_rib", "annexes_cni_dirigeants",
    "signature_docusign", "soutien_collectivite_locale", "soutien_clients_cles",
    "soutien_banques_historiques", "personnalisation_visite_site",
    "personnalisation_rencontre_equipes", "personnalisation_etude_contrats",
    "differenciation_concurrents_explicite", "elements_emotionnels_sociaux",
    "declaration_L642_3_signee", "faculte_substitution_precise",
    "kbis_en_annexe",
]
report["bool_compare"] = {c: compare_bool(c) for c in BOOL_COLS}

CAT_COLS = [
    "forme_repreneur", "exp_sectorielle", "capacite_financiere",
    "type_vehicule", "modalites_paiement", "maintien_conditions",
    "diagnostic_qualif", "hypotheses_qualif", "maintien_site",
    "maintien_marques", "apport_origine_doc", "agressivite_cs",
    "structure_dom", "ton", "qualite_redac", "coherence_prix_bp",
    "procedure", "caution_perso",
]
report["cat_compare"] = {c: compare_cat(c) for c in CAT_COLS}

# Confidence
report["confidence_dist"] = desc_cat(df["confidence"])

# Save full report
with open(OUT / "stats_report.json", "w") as f:
    json.dump(report, f, indent=2, default=str)

# Print summary
print("\n=== KEY DELTAS retenue vs rejetee ===")
for c in NUM_COLS:
    r = report["numeric_compare"][c]
    if r["win_median"] is not None and r["lose_median"] is not None and r["win_n"] >= 5 and r["lose_n"] >= 5:
        wm, lm = r["win_median"], r["lose_median"]
        if lm != 0:
            ratio = wm / lm if lm != 0 else None
        else:
            ratio = None
        print(f"  {c:30s} WIN med={wm:>12.1f} (n={r['win_n']}) | LOSE med={lm:>12.1f} (n={r['lose_n']})")

print("\n=== KEY BOOL DELTAS ===")
for c in BOOL_COLS:
    r = report["bool_compare"][c]
    if r["win_pct_true"] is not None and r["lose_pct_true"] is not None and r["win_n"] >= 5 and r["lose_n"] >= 5:
        d = r["win_pct_true"] - r["lose_pct_true"]
        if abs(d) >= 5:
            print(f"  {c:40s} WIN={r['win_pct_true']:5.1f}% (n={r['win_n']}) | LOSE={r['lose_pct_true']:5.1f}% (n={r['lose_n']}) | delta={d:+.1f}")

print("\nDone. stats_report.json saved.")
