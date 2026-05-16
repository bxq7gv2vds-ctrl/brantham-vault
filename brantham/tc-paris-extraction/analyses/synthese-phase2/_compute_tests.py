#!/usr/bin/env python3
"""
Livrable 11 — Tests statistiques formels et analyses residuelles.

Couvre 6 analyses sur le corpus EXISTANT (pickles + master CSV) :
  1. Tests chi-deux / Fisher + Mann-Whitney sur les variables discriminantes.
  2. Replication sur sous-corpus fiable (high + medium confidence).
  3. Lien cabinet d'avocats du repreneur <-> succes.
  4. Lien administrateur judiciaire <-> taux de retenue.
  5. Delai v1 -> v2 des offres ameliorees puis retenues.
  6. Contre-verification de la grille /100 par arbre de decision + regression logistique.

Rejouable :
  uv run --with scipy --with pandas --with scikit-learn python _compute_tests.py

Sorties : printees sur stdout + ecrites dans _tests_output.json
"""
import json
import re
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

warnings.filterwarnings("ignore")

BASE = Path(__file__).resolve().parent           # analyses/synthese-phase2
ROOT = BASE.parent.parent                        # tc-paris-extraction

RESULTS = {}


# --------------------------------------------------------------------------
# Chargement et preparation
# --------------------------------------------------------------------------
def load_data():
    o = pd.read_pickle(BASE / "offres.pkl")
    m = pd.read_csv(ROOT / "master-offres.csv")
    md = pd.read_csv(ROOT / "master-dossiers.csv")

    # Statut decide : "retenue" = oui + amelioree_puis_retenue ; "rejetee" = non
    o["statut"] = o["retenue"].map(
        {
            "oui": "retenue",
            "amelioree_puis_retenue": "retenue",
            "non": "rejetee",
        }
    )
    decided = o[o["statut"].isin(["retenue", "rejetee"])].copy()
    return o, m, md, decided


# --------------------------------------------------------------------------
# Helpers stat
# --------------------------------------------------------------------------
def diff_prop_ci(s1, n1, s2, n2, alpha=0.05):
    """IC 95 % sur la difference de proportions (approximation de Wald)."""
    if n1 == 0 or n2 == 0:
        return (np.nan, np.nan)
    p1, p2 = s1 / n1, s2 / n2
    se = np.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    z = stats.norm.ppf(1 - alpha / 2)
    d = p1 - p2
    return (d - z * se, d + z * se)


def binary_test(name, df, col, truthy):
    """Chi-deux ou Fisher exact sur une variable binaire retenue vs rejetee."""
    sub = df[df[col].notna()]
    win = sub[sub["statut"] == "retenue"]
    lose = sub[sub["statut"] == "rejetee"]
    if len(win) < 3 or len(lose) < 3:
        return None

    def is_true(v):
        if isinstance(v, bool):
            return v
        return str(v).strip().lower() in truthy

    w_true = win[col].apply(is_true).sum()
    l_true = lose[col].apply(is_true).sum()
    n_w, n_l = len(win), len(lose)

    table = np.array([[w_true, n_w - w_true], [l_true, n_l - l_true]])
    expected = stats.contingency.expected_freq(table)
    use_fisher = (expected < 5).any()

    if use_fisher:
        _, p = stats.fisher_exact(table)
        test = "Fisher"
    else:
        _, p, _, _ = stats.chi2_contingency(table, correction=False)
        test = "chi2"

    pw, pl = w_true / n_w, l_true / n_l
    delta = (pw - pl) * 100
    lo, hi = diff_prop_ci(w_true, n_w, l_true, n_l)
    return {
        "variable": name,
        "type": "binaire",
        "test": test,
        "pct_win": round(pw * 100, 1),
        "pct_lose": round(pl * 100, 1),
        "delta_pts": round(delta, 1),
        "n_win": int(n_w),
        "n_lose": int(n_l),
        "p_value": float(p),
        "ic95_delta": [round(lo * 100, 1), round(hi * 100, 1)],
        "significatif": bool(p < 0.05),
    }


def numeric_test(name, df, col):
    """Mann-Whitney U + taille d'effet rank-biserial."""
    sub = df[pd.to_numeric(df[col], errors="coerce").notna()].copy()
    sub["_v"] = pd.to_numeric(sub[col], errors="coerce")
    win = sub[sub["statut"] == "retenue"]["_v"]
    lose = sub[sub["statut"] == "rejetee"]["_v"]
    if len(win) < 4 or len(lose) < 4:
        return None
    u, p = stats.mannwhitneyu(win, lose, alternative="two-sided")
    # rank-biserial = 1 - 2U / (n1*n2)  (signe : positif si win > lose)
    rb = 1 - (2 * u) / (len(win) * len(lose))
    return {
        "variable": name,
        "type": "numerique",
        "test": "Mann-Whitney U",
        "med_win": float(np.median(win)),
        "med_lose": float(np.median(lose)),
        "delta_med": float(np.median(win) - np.median(lose)),
        "n_win": int(len(win)),
        "n_lose": int(len(lose)),
        "p_value": float(p),
        "rank_biserial": round(float(rb), 3),
        "significatif": bool(p < 0.05),
    }


def cat_indicator(df, col, classes):
    """Cree une colonne booleenne True si la valeur appartient a `classes`."""
    return df[col].apply(
        lambda v: str(v).strip().lower() in classes if pd.notna(v) else np.nan
    )


# --------------------------------------------------------------------------
# 1. TESTS STATISTIQUES FORMELS
# --------------------------------------------------------------------------
def analysis_1(decided):
    print("\n" + "=" * 70)
    print("1. TESTS STATISTIQUES FORMELS")
    print("=" * 70)

    truthy = {"true", "oui", "1", "vrai"}

    # Variables binaires natives presentes dans les pickles
    binary_cols = [
        ("personnalisation_etude_contrats", "personnalisation_etude_contrats"),
        ("declaration_L642_3_signee", "declaration_L642_3_signee"),
        ("annexes_kbis", "annexes_kbis"),
        ("annexes_attest_bancaire", "annexes_attest_bancaire"),
        ("kbis_en_annexe", "kbis_en_annexe"),
        ("annexes_organigramme_cible", "annexes_organigramme_cible"),
        ("soutien_banques_historiques", "soutien_banques_historiques"),
        ("elements_emotionnels_sociaux", "elements_emotionnels_sociaux"),
        ("aucune_cs", "aucune_cs"),
        ("annexes_cni_dirigeants", "annexes_cni_dirigeants"),
        ("soutien_clients_cles", "soutien_clients_cles"),
        ("annexes_cv_dirigeants", "annexes_cv_dirigeants"),
        ("dette_lettre_confort", "dette_lettre_confort"),
        ("soutien_collectivite_locale", "soutien_collectivite_locale"),
        ("personnalisation_visite_site", "personnalisation_visite_site"),
        ("annexes_comptes_sociaux_3ans", "annexes_comptes_sociaux_3ans"),
        ("annexes_attest_fisc_sociale", "annexes_attest_fisc_sociale"),
        ("differenciation_concurrents_explicite", "differenciation_concurrents_explicite"),
        ("non_demembrement", "non_demembrement"),
        ("personnalisation_rencontre_equipes", "personnalisation_rencontre_equipes"),
        ("annexes_business_plan", "annexes_business_plan"),
        ("annexes_rib", "annexes_rib"),
        ("exec_summary", "exec_summary"),
        ("bp_3ans_present", "bp_3ans"),
        ("faculte_substitution_precise", "faculte_substitution_precise"),
        ("L642_12_al4", "L642_12_al4"),
    ]

    rows = []
    for name, col in binary_cols:
        if col not in decided.columns:
            continue
        r = binary_test(name, decided, col, truthy)
        if r:
            rows.append(r)

    # Variables categorielles transformees en indicateurs binaires
    cat_specs = [
        ("capacite_financiere_forte", "capacite_financiere", {"forte_documentee"}),
        ("qualite_redac_claire", "qualite_redac", {"claire"}),
        ("ton_mixte", "ton", {"mixte"}),
        ("diagnostic_op_ou_struct", "diagnostic_qualif",
         {"operationnel", "structurel"}),
        ("hypotheses_prudentes", "hypotheses_qualif", {"prudentes"}),
        ("coherence_prix_bp_coherent", "coherence_prix_bp", {"coherent"}),
        ("apport_rib_attestation", "apport_origine_doc", {"oui_rib_attestation"}),
        ("maintien_conditions_oui_total", "maintien_conditions", {"oui_total"}),
        ("paiement_comptant_audience", "modalites_paiement", {"comptant_audience"}),
        ("agressivite_cs_aucune", "agressivite_cs", {"aucune"}),
    ]
    for name, col, classes in cat_specs:
        if col not in decided.columns:
            continue
        tmp = decided.copy()
        tmp["_ind"] = cat_indicator(tmp, col, classes)
        r = binary_test(name, tmp, "_ind", {"true"})
        if r:
            rows.append(r)

    # Variables numeriques
    numeric_cols = [
        "prix_total", "incorporels", "corporels", "effectif",
        "nb_concurrents", "nb_salaries_repris", "pct_reprise", "nb_cs",
        "nb_pages_total", "nb_erreurs", "track_record_count", "exp_annees",
        "incessibilite_mois", "apport_fp", "bfr_redemarrage",
        "charges_augmentatives", "ca_an1", "ca_an3",
    ]
    for col in numeric_cols:
        if col not in decided.columns:
            continue
        r = numeric_test(col, decided, col)
        if r:
            rows.append(r)

    # Tri par p-value croissante
    rows.sort(key=lambda x: x["p_value"])

    print(f"\n{'Variable':<38}{'Delta':>10}{'p-value':>12}{'signif':>9}")
    print("-" * 70)
    for r in rows:
        d = r.get("delta_pts", r.get("delta_med"))
        dstr = f"{d:+.1f}" if r["type"] == "binaire" else f"{d:+.0f}"
        sig = "OUI" if r["significatif"] else "non"
        pstr = f"{r['p_value']:.4f}" if r["p_value"] >= 1e-4 else f"{r['p_value']:.1e}"
        print(f"{r['variable']:<38}{dstr:>10}{pstr:>12}{sig:>9}")

    n_sig = sum(r["significatif"] for r in rows)
    print(f"\n{n_sig}/{len(rows)} variables significatives a p<0,05")
    RESULTS["analysis_1"] = rows
    return rows


# --------------------------------------------------------------------------
# 2. REPLICATION SUR SOUS-CORPUS FIABLE (high + medium)
# --------------------------------------------------------------------------
def analysis_2(decided):
    print("\n" + "=" * 70)
    print("2. REPLICATION SOUS-CORPUS FIABLE (high + medium confidence)")
    print("=" * 70)

    reliable = decided[decided["confidence"].isin(["high", "medium"])].copy()
    print(f"n decidees total = {len(decided)} ; n fiables = {len(reliable)}")
    print(f"  retenues fiables = {(reliable['statut']=='retenue').sum()} ;"
          f" rejetees fiables = {(reliable['statut']=='rejetee').sum()}")

    truthy = {"true", "oui", "1", "vrai"}
    top_bin = [
        ("personnalisation_etude_contrats", "personnalisation_etude_contrats"),
        ("declaration_L642_3_signee", "declaration_L642_3_signee"),
        ("annexes_kbis", "annexes_kbis"),
        ("annexes_attest_bancaire", "annexes_attest_bancaire"),
        ("kbis_en_annexe", "kbis_en_annexe"),
        ("soutien_banques_historiques", "soutien_banques_historiques"),
        ("aucune_cs", "aucune_cs"),
        ("elements_emotionnels_sociaux", "elements_emotionnels_sociaux"),
    ]
    top_cat = [
        ("capacite_financiere_forte", "capacite_financiere", {"forte_documentee"}),
        ("qualite_redac_claire", "qualite_redac", {"claire"}),
        ("apport_rib_attestation", "apport_origine_doc", {"oui_rib_attestation"}),
    ]

    rows = []
    for name, col in top_bin:
        full = binary_test(name, decided, col, truthy)
        rel = binary_test(name, reliable, col, truthy)
        if full and rel:
            rows.append((name, full, rel))
    for name, col, classes in top_cat:
        tf, tr = decided.copy(), reliable.copy()
        tf["_ind"] = cat_indicator(tf, col, classes)
        tr["_ind"] = cat_indicator(tr, col, classes)
        full = binary_test(name, tf, "_ind", {"true"})
        rel = binary_test(name, tr, "_ind", {"true"})
        if full and rel:
            rows.append((name, full, rel))

    print(f"\n{'Variable':<36}{'D full':>10}{'D fiable':>10}{'ecart':>9}{'tient':>8}")
    print("-" * 73)
    out = []
    for name, full, rel in rows:
        df_, dr_ = full["delta_pts"], rel["delta_pts"]
        ecart = dr_ - df_
        tient = "OUI" if (abs(ecart) <= 12 and np.sign(df_) == np.sign(dr_)
                          and rel["significatif"]) else "FRAGILE"
        print(f"{name:<36}{df_:>+10.1f}{dr_:>+10.1f}{ecart:>+9.1f}{tient:>8}")
        out.append({"variable": name, "delta_full": df_, "delta_reliable": dr_,
                    "ecart": round(ecart, 1), "p_reliable": rel["p_value"],
                    "verdict": tient})
    RESULTS["analysis_2"] = out
    return out


# --------------------------------------------------------------------------
# 3. CABINET D'AVOCATS DU REPRENEUR <-> SUCCES
# --------------------------------------------------------------------------
def normalize_cabinet(v):
    if pd.isna(v) or not str(v).strip() or str(v).strip().lower() in ("none", "nr"):
        return None
    s = str(v).upper()
    if "FIDAL" in s:
        return "FIDAL"
    if "LEXCAP" in s:
        return "LEXCAP"
    if "MONCEY" in s:
        return "MONCEY AVOCATS"
    if "HADENGUE" in s:
        return "HADENGUE & ASSOCIES"
    if "MAC MAHON" in s or "MACMAHON" in s:
        return "MAC MAHON / CVA"
    if "IKKI" in s:
        return "IKKI PARTNERS"
    if "AGN AVOCAT" in s:
        return "AGN AVOCATS"
    if "PZ AVOCAT" in s or "PZ-AVOCAT" in s or "ZEITOUN" in s:
        return "PZ AVOCATS"
    if "DORLEAC" in s:
        return "DORLEAC AZOULAY"
    if "GUARREL" in s:
        return "GUARREL AVOCAT"
    # Bruit : valeurs parasites du champ avocat_repreneur du master CSV
    # (dates, montants, notes d'extraction, mentions "non mentionne", etc.)
    noise = ("NON MENTION", "NON RENSEIGN", "IDENTIQUE", "JUSQU", "CADUQUE",
             "DÉCISION DU TRIBUNAL", "DETIENT", "DÉTIENT", "% DU CAPITAL",
             ".COM")
    if any(tok in s for tok in noise):
        return None
    if re.fullmatch(r"[\d\s.,/-]+", s.strip()):  # purement numerique / date
        return None
    if "AVOCAT" in s or "SELARL" in s or "AARPI" in s or "CABINET" in s \
            or "SCP" in s or "ASSOCI" in s:
        return s.split(",")[0].split("(")[0].split("—")[0].strip()[:30]
    return None  # tout le reste : non identifiable comme cabinet


def analysis_3(o, m, decided):
    print("\n" + "=" * 70)
    print("3. CABINET D'AVOCATS DU REPRENEUR <-> SUCCES")
    print("=" * 70)

    # Source 1 : avocat_cabinet du pickle ; complete par avocat_repreneur du master
    av = o[["offre_id", "avocat_cabinet"]].copy()
    mm = m[["offre_id", "avocat_repreneur"]].copy()
    merged = decided.merge(av, on="offre_id", how="left", suffixes=("", "_p"))
    merged = merged.merge(mm, on="offre_id", how="left")
    merged["cab_raw"] = merged["avocat_cabinet"].fillna(merged["avocat_repreneur"])
    merged["cabinet"] = merged["cab_raw"].apply(normalize_cabinet)

    filled = merged[merged["cabinet"].notna()]
    print(f"Offres decidees avec cabinet renseigne : {len(filled)}/{len(decided)}"
          f" ({100*len(filled)/len(decided):.0f}%)")

    grp = (filled.groupby("cabinet")["statut"]
           .agg(n="count", n_ret=lambda s: (s == "retenue").sum()))
    grp["taux_retenue_pct"] = (100 * grp["n_ret"] / grp["n"]).round(1)
    grp = grp.sort_values(["n", "taux_retenue_pct"], ascending=False)

    base_rate = 100 * (decided["statut"] == "retenue").mean()
    print(f"Taux de retenue de reference (corpus decide) : {base_rate:.1f}%\n")
    print(f"{'Cabinet':<26}{'n':>5}{'retenues':>11}{'taux %':>10}{'p Fisher':>11}")
    print("-" * 63)
    rows = []
    for cab, r in grp.iterrows():
        flag = "  (n faible)" if r["n"] < 5 else ""
        # Fisher exact : ce cabinet vs reste du corpus decide
        in_cab = filled[filled["cabinet"] == cab]["statut"]
        out_cab = decided[~decided.index.isin(in_cab.index)]["statut"]
        table = np.array([
            [(in_cab == "retenue").sum(), (in_cab == "rejetee").sum()],
            [(out_cab == "retenue").sum(), (out_cab == "rejetee").sum()],
        ])
        _, p = stats.fisher_exact(table)
        pstr = f"{p:.4f}" if r["n"] >= 5 else "  -"
        print(f"{cab:<26}{int(r['n']):>5}{int(r['n_ret']):>11}"
              f"{r['taux_retenue_pct']:>10}{pstr:>11}{flag}")
        rows.append({"cabinet": cab, "n": int(r["n"]),
                     "n_retenues": int(r["n_ret"]),
                     "taux_retenue_pct": float(r["taux_retenue_pct"]),
                     "p_value_vs_reste": float(p),
                     "n_faible": bool(r["n"] < 5)})
    RESULTS["analysis_3"] = {"base_rate": round(base_rate, 1),
                             "n_filled": int(len(filled)),
                             "n_decided": int(len(decided)),
                             "cabinets": rows}
    return rows


# --------------------------------------------------------------------------
# 4. ADMINISTRATEUR JUDICIAIRE <-> TAUX DE RETENUE
# --------------------------------------------------------------------------
def normalize_aj(v):
    if pd.isna(v) or not str(v).strip() or str(v).strip().lower() in ("none", "nr"):
        return None
    s = str(v).upper()
    if "BOURBOULOUX" in s:
        return "Helene BOURBOULOUX"
    if "PACE" in s:
        return "Marine PACE"
    if "BELADJINE" in s:
        return "Sandra BELADJINE"
    if "FLECHARD" in s or "BOUYER" in s or "LANGET" in s:
        return "FLECHARD / BOUYER / LANGET"
    if "LAVOIR" in s:
        return "Julie LAVOIR"
    if "POLI" in s or "BAULAND" in s:
        return "POLI / BAULAND"
    if "LOYER" in s:
        return "Nicolas LOYER"
    if "AUDRAS" in s:
        return "Marine PACE"
    return s.split("(")[0].split("/")[0].strip()[:28]


def analysis_4(decided):
    print("\n" + "=" * 70)
    print("4. ADMINISTRATEUR JUDICIAIRE <-> TAUX DE RETENUE")
    print("=" * 70)

    d = decided.copy()
    d["aj_norm"] = d["aj"].apply(normalize_aj)
    filled = d[d["aj_norm"].notna()]
    base_rate = 100 * (decided["statut"] == "retenue").mean()
    print(f"Offres decidees avec AJ renseigne : {len(filled)}/{len(decided)}")
    print(f"Taux de retenue de reference : {base_rate:.1f}%\n")

    grp = (filled.groupby("aj_norm")["statut"]
           .agg(n="count", n_ret=lambda s: (s == "retenue").sum()))
    grp["taux_retenue_pct"] = (100 * grp["n_ret"] / grp["n"]).round(1)
    grp = grp.sort_values("n", ascending=False)

    print(f"{'Administrateur judiciaire':<32}{'n':>5}{'retenues':>11}{'taux %':>10}")
    print("-" * 58)
    rows = []
    for aj, r in grp.iterrows():
        flag = "  (n faible)" if r["n"] < 8 else ""
        # test exact de Fisher cet AJ vs reste du corpus decide
        in_aj = filled[filled["aj_norm"] == aj]["statut"]
        out_aj = decided[~decided.index.isin(in_aj.index)]["statut"]
        table = np.array([
            [(in_aj == "retenue").sum(), (in_aj == "rejetee").sum()],
            [(out_aj == "retenue").sum(), (out_aj == "rejetee").sum()],
        ])
        _, p = stats.fisher_exact(table)
        print(f"{aj:<32}{int(r['n']):>5}{int(r['n_ret']):>11}"
              f"{r['taux_retenue_pct']:>10}{flag}")
        rows.append({"aj": aj, "n": int(r["n"]), "n_retenues": int(r["n_ret"]),
                     "taux_retenue_pct": float(r["taux_retenue_pct"]),
                     "p_value_vs_reste": float(p),
                     "n_faible": bool(r["n"] < 8)})
    RESULTS["analysis_4"] = {"base_rate": round(base_rate, 1), "ajs": rows}
    return rows


# --------------------------------------------------------------------------
# 5. DELAI v1 -> v2 DES OFFRES AMELIOREES PUIS RETENUES
# --------------------------------------------------------------------------
def analysis_5(o, m):
    print("\n" + "=" * 70)
    print("5. DELAI v1 -> v2 DES OFFRES AMELIOREES PUIS RETENUES")
    print("=" * 70)

    ame = o[o["retenue"] == "amelioree_puis_retenue"][["offre_id", "dossier_id"]]
    print(f"Offres marquees amelioree_puis_retenue : {len(ame)}")

    md = m[["offre_id", "dossier_id", "date_offre", "nom_repreneur"]].copy()
    md["date_offre"] = pd.to_datetime(md["date_offre"], errors="coerce")

    # Approche : pour chaque dossier contenant au moins une offre amelioree,
    # regrouper les offres du meme repreneur et mesurer l'ecart min->max des dates.
    ame_dossiers = set(ame["dossier_id"].dropna())
    sub = md[md["dossier_id"].isin(ame_dossiers) & md["date_offre"].notna()].copy()
    sub["repreneur_key"] = (
        sub["nom_repreneur"].fillna("?").str.upper().str.strip().str[:25]
    )

    delais = []
    detail = []
    for (dossier, rep), g in sub.groupby(["dossier_id", "repreneur_key"]):
        dates = sorted(g["date_offre"].dropna().unique())
        if len(dates) >= 2:
            d = (pd.Timestamp(dates[-1]) - pd.Timestamp(dates[0])).days
            if d > 0:
                delais.append(d)
                detail.append({"dossier": dossier, "repreneur": rep,
                               "v1": str(pd.Timestamp(dates[0]).date()),
                               "v2": str(pd.Timestamp(dates[-1]).date()),
                               "delai_jours": int(d)})

    if delais:
        arr = np.array(delais)
        med, p25, p75 = (np.median(arr), np.percentile(arr, 25),
                         np.percentile(arr, 75))
        print(f"\nPaires v1->v2 datees exploitables : n={len(delais)}")
        print(f"  Delai median  : {med:.0f} jours")
        print(f"  P25 / P75     : {p25:.0f} / {p75:.0f} jours")
        print(f"  Min / Max     : {arr.min()} / {arr.max()} jours")
        RESULTS["analysis_5"] = {
            "n_amelioree": int(len(ame)),
            "n_paires_datees": int(len(delais)),
            "delai_median_j": float(med),
            "p25_j": float(p25), "p75_j": float(p75),
            "min_j": int(arr.min()), "max_j": int(arr.max()),
            "detail": detail,
        }
    else:
        print("\nAucune paire v1->v2 datee exploitable "
              "(dates v1 et v2 non distinguees dans master-offres).")
        RESULTS["analysis_5"] = {"n_amelioree": int(len(ame)),
                                 "n_paires_datees": 0,
                                 "note": "dates non distinctes"}
    return RESULTS["analysis_5"]


# --------------------------------------------------------------------------
# 6. CONTRE-VERIFICATION DE LA GRILLE /100
# --------------------------------------------------------------------------
def analysis_6(decided):
    print("\n" + "=" * 70)
    print("6. CONTRE-VERIFICATION DE LA GRILLE /100 (ML)")
    print("=" * 70)

    from sklearn.tree import DecisionTreeClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import cross_val_score, StratifiedKFold
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import Pipeline

    df = decided.copy()
    truthy = {"true", "oui", "1", "vrai"}

    feats = {}
    # binaires natives
    for col in ["personnalisation_etude_contrats", "declaration_L642_3_signee",
                "annexes_kbis", "annexes_attest_bancaire", "kbis_en_annexe",
                "soutien_banques_historiques", "aucune_cs",
                "elements_emotionnels_sociaux", "annexes_organigramme_cible",
                "exec_summary", "non_demembrement", "annexes_business_plan",
                "differenciation_concurrents_explicite",
                "personnalisation_visite_site"]:
        if col in df.columns:
            feats[col] = df[col].apply(
                lambda v: 1 if (v is True or str(v).strip().lower() in truthy)
                else 0)
    # categorielles -> indicateurs
    for name, col, classes in [
        ("capacite_fin_forte", "capacite_financiere", {"forte_documentee"}),
        ("qualite_claire", "qualite_redac", {"claire"}),
        ("ton_mixte", "ton", {"mixte"}),
        ("diag_op_struct", "diagnostic_qualif", {"operationnel", "structurel"}),
        ("hypo_prudentes", "hypotheses_qualif", {"prudentes"}),
        ("coherence_ok", "coherence_prix_bp", {"coherent"}),
        ("apport_rib", "apport_origine_doc", {"oui_rib_attestation"}),
        ("maintien_total", "maintien_conditions", {"oui_total"}),
        ("paiement_comptant", "modalites_paiement", {"comptant_audience"}),
        ("cs_aucune", "agressivite_cs", {"aucune"}),
    ]:
        if col in df.columns:
            feats[name] = df[col].apply(
                lambda v: 1 if (pd.notna(v) and str(v).strip().lower() in classes)
                else 0)
    # numeriques (NR -> mediane)
    for col in ["pct_reprise", "nb_cs", "track_record_count", "nb_concurrents",
                "incorporels", "prix_total"]:
        if col in df.columns:
            s = pd.to_numeric(df[col], errors="coerce")
            feats[col] = s.fillna(s.median())

    X = pd.DataFrame(feats).reset_index(drop=True)
    y = (df["statut"] == "retenue").astype(int).reset_index(drop=True)
    print(f"n={len(y)} (retenues={int(y.sum())}, rejetees={int((1-y).sum())}),"
          f" {X.shape[1]} features")

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    # Arbre de decision profondeur 3
    tree = DecisionTreeClassifier(max_depth=3, min_samples_leaf=8,
                                  random_state=42, class_weight="balanced")
    tree_acc = cross_val_score(tree, X, y, cv=cv, scoring="accuracy")
    tree_auc = cross_val_score(tree, X, y, cv=cv, scoring="roc_auc")
    tree.fit(X, y)
    tree_imp = sorted(zip(X.columns, tree.feature_importances_),
                      key=lambda t: -t[1])

    # Regression logistique L2
    logit = Pipeline([
        ("sc", StandardScaler()),
        ("lr", LogisticRegression(penalty="l2", C=0.5, max_iter=1000,
                                  class_weight="balanced")),
    ])
    log_acc = cross_val_score(logit, X, y, cv=cv, scoring="accuracy")
    log_auc = cross_val_score(logit, X, y, cv=cv, scoring="roc_auc")
    logit.fit(X, y)
    coefs = logit.named_steps["lr"].coef_[0]
    log_imp = sorted(zip(X.columns, coefs), key=lambda t: -abs(t[1]))

    base = max(y.mean(), 1 - y.mean())
    print(f"\nBaseline (classe majoritaire) : {base:.3f}")
    print(f"Arbre  profondeur 3 : accuracy CV = {tree_acc.mean():.3f}"
          f" +/- {tree_acc.std():.3f} | AUC = {tree_auc.mean():.3f}")
    print(f"Logit  L2 (C=0.5)   : accuracy CV = {log_acc.mean():.3f}"
          f" +/- {log_acc.std():.3f} | AUC = {log_auc.mean():.3f}")

    print("\nArbre - top 8 variables retenues spontanement :")
    for name, imp in tree_imp[:8]:
        if imp > 0:
            print(f"  {name:<30}{imp:.3f}")

    print("\nLogit - top 10 |coefficient| :")
    for name, c in log_imp[:10]:
        print(f"  {name:<30}{c:+.3f}")

    grille08 = {
        "pct_reprise", "engagement_emplois_mois", "maintien_total",
        "diag_op_struct", "hypo_prudentes", "capacite_fin_forte",
        "apport_rib", "cs_aucune", "nb_cs", "personnalisation_etude_contrats",
        "soutien_banques_historiques", "qualite_claire", "ton_mixte",
        "declaration_L642_3_signee", "annexes_kbis", "annexes_attest_bancaire",
        "kbis_en_annexe", "coherence_ok", "paiement_comptant",
    }
    tree_top = {n for n, i in tree_imp[:8] if i > 0}
    log_top = {n for n, c in log_imp[:10]}
    ml_top = tree_top | log_top
    recoupe = ml_top & grille08
    hors = ml_top - grille08
    print(f"\nVariables ML top recoupant la grille 08 : {sorted(recoupe)}")
    print(f"Variables ML top HORS grille 08 (predicteur rate ?) : {sorted(hors)}")

    RESULTS["analysis_6"] = {
        "n": int(len(y)), "n_features": int(X.shape[1]),
        "baseline": round(float(base), 3),
        "tree_acc_mean": round(float(tree_acc.mean()), 3),
        "tree_acc_std": round(float(tree_acc.std()), 3),
        "tree_auc_mean": round(float(tree_auc.mean()), 3),
        "logit_acc_mean": round(float(log_acc.mean()), 3),
        "logit_acc_std": round(float(log_acc.std()), 3),
        "logit_auc_mean": round(float(log_auc.mean()), 3),
        "tree_importance": [(n, round(float(i), 3)) for n, i in tree_imp[:8]],
        "logit_coef": [(n, round(float(c), 3)) for n, c in log_imp[:10]],
        "recoupe_grille08": sorted(recoupe),
        "hors_grille08": sorted(hors),
    }
    return RESULTS["analysis_6"]


# --------------------------------------------------------------------------
def main():
    o, m, md, decided = load_data()
    print(f"Corpus : {len(o)} offres, {len(decided)} decidees "
          f"({(decided['statut']=='retenue').sum()} retenues, "
          f"{(decided['statut']=='rejetee').sum()} rejetees)")
    analysis_1(decided)
    analysis_2(decided)
    analysis_3(o, m, decided)
    analysis_4(decided)
    analysis_5(o, m)
    analysis_6(decided)

    out = BASE / "_tests_output.json"
    out.write_text(json.dumps(RESULTS, indent=2, ensure_ascii=False))
    print(f"\nResultats JSON ecrits dans {out}")


if __name__ == "__main__":
    main()
