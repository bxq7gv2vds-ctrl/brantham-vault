#!/usr/bin/env python3
"""
Phase 2 analysis pipeline — TC Paris distressed M&A corpus.
Loads 566 offre JSONs + 101 dossier JSONs, computes stats, dumps to pickle.
"""
import json
import os
import pandas as pd
import numpy as np
from pathlib import Path
from collections import Counter, defaultdict

BASE = Path("/Users/paul/vault/brantham/tc-paris-extraction")
OFFRES_DIR = BASE / "grilles" / "offres"
DOSSIERS_DIR = BASE / "grilles" / "dossiers"
OUT = BASE / "analyses" / "synthese-phase2"
OUT.mkdir(parents=True, exist_ok=True)


def safe_get(d, path, default=None):
    cur = d
    for k in path:
        if cur is None:
            return default
        if isinstance(cur, dict):
            cur = cur.get(k)
        else:
            return default
    return cur if cur is not None else default


def flatten_offre(o):
    """Flatten nested JSON into a flat row."""
    row = {}
    row["offre_id"] = safe_get(o, ["meta", "offre_id"])
    row["dossier_id"] = safe_get(o, ["meta", "dossier_id"])
    row["dossier_folder"] = safe_get(o, ["meta", "dossier_folder"])
    row["confidence"] = safe_get(o, ["meta", "confidence"])

    # Identification cible
    row["cible"] = safe_get(o, ["identification", "cible_raison_sociale"])
    row["naf"] = safe_get(o, ["identification", "naf_secteur"])
    row["sous_secteur"] = safe_get(o, ["identification", "sous_secteur"])
    row["ca_eur"] = safe_get(o, ["identification", "ca_dernier_exercice_eur"])
    row["ebitda_eur"] = safe_get(o, ["identification", "ebitda_eur"])
    row["effectif"] = safe_get(o, ["identification", "effectif_total"])
    row["nb_sites"] = safe_get(o, ["identification", "nb_sites"])
    row["procedure"] = safe_get(o, ["identification", "type_procedure"])
    row["aj"] = safe_get(o, ["identification", "aj_nom"])

    # Issue
    row["retenue"] = safe_get(o, ["issue_dossier", "cette_offre_retenue"])
    row["issue_dossier"] = safe_get(o, ["issue_dossier", "issue_globale_dossier"])
    row["motifs_tribunal"] = safe_get(o, ["issue_dossier", "motifs_tribunal_verbatim"])
    row["motifs_rejet"] = safe_get(o, ["issue_dossier", "motifs_rejet_verbatim"])
    row["nb_concurrents"] = safe_get(o, ["issue_dossier", "nb_offres_concurrentes"])

    # Repreneur
    row["forme_repreneur"] = safe_get(o, ["profil_repreneur", "forme"])
    row["exp_sectorielle"] = safe_get(o, ["profil_repreneur", "experience_sectorielle_oui_non"])
    row["exp_annees"] = safe_get(o, ["profil_repreneur", "experience_sectorielle_annees"])
    tr = safe_get(o, ["profil_repreneur", "track_record_reprises"], []) or []
    row["track_record_count"] = len(tr) if isinstance(tr, list) else 0
    row["capacite_financiere"] = safe_get(o, ["profil_repreneur", "capacite_financiere_demontree"])
    row["caution_perso"] = safe_get(o, ["profil_repreneur", "cautionnement_personnel"])
    row["type_vehicule"] = safe_get(o, ["profil_repreneur", "vehicule_reprise", "type_vehicule"])
    row["kbis_en_annexe"] = safe_get(o, ["profil_repreneur", "vehicule_reprise", "kbis_present_en_annexe"])

    # Prix
    row["prix_total"] = safe_get(o, ["structure_prix", "prix_total_eur"])
    row["incorporels"] = safe_get(o, ["structure_prix", "decomposition", "incorporels_eur"])
    row["corporels"] = safe_get(o, ["structure_prix", "decomposition", "corporels_eur"])
    row["stocks_eur"] = safe_get(o, ["structure_prix", "decomposition", "stocks_eur"])
    row["modalites_paiement"] = safe_get(o, ["structure_prix", "modalites_paiement"])
    row["cheque_consignation"] = safe_get(o, ["structure_prix", "cheque_consignation_eur"])
    row["charges_augmentatives"] = safe_get(o, ["structure_prix", "charges_augmentatives_eur"])

    # Reprise passif
    row["L642_12_al4"] = safe_get(o, ["reprise_passif", "engagements_L642_12_al4"])
    row["L642_12_montant"] = safe_get(o, ["reprise_passif", "engagement_L642_12_montant_eur"])

    # Social
    row["nb_salaries_repris"] = safe_get(o, ["volet_social", "nb_salaries_repris"])
    row["nb_total_salaries"] = safe_get(o, ["volet_social", "nb_total_salaries"])
    row["pct_reprise"] = safe_get(o, ["volet_social", "pct_reprise"])
    row["maintien_conditions"] = safe_get(o, ["volet_social", "maintien_conditions_anciennete_salaire_lieu"])
    row["nb_licenciements"] = safe_get(o, ["volet_social", "plan_licenciement", "nb"])
    row["engagement_emplois_mois"] = safe_get(o, ["volet_social", "engagement_maintien_emplois_duree_mois"])
    row["sanction_non_respect"] = safe_get(o, ["volet_social", "sanction_non_respect_emplois"])
    row["irp_cse"] = safe_get(o, ["volet_social", "relations_irp_cse_mention"])

    # Plan
    row["diagnostic_qualif"] = safe_get(o, ["plan_industriel", "diagnostic_qualification"])
    row["vision_phrase"] = safe_get(o, ["plan_industriel", "vision_strategique_phrase"])
    row["synergies_chiffrees"] = safe_get(o, ["plan_industriel", "synergies_chiffrees_eur"])
    row["capex"] = safe_get(o, ["plan_industriel", "capex_montant_eur"])
    row["bp_3ans"] = safe_get(o, ["plan_industriel", "plan_affaires_3ans_present"])
    row["ca_an1"] = safe_get(o, ["plan_industriel", "ca_an1_eur"])
    row["ca_an3"] = safe_get(o, ["plan_industriel", "ca_an3_eur"])
    row["ebitda_an3"] = safe_get(o, ["plan_industriel", "ebitda_an3_eur"])
    row["hypotheses_qualif"] = safe_get(o, ["plan_industriel", "hypotheses_qualification"])
    row["maintien_site"] = safe_get(o, ["plan_industriel", "maintien_site"])
    row["maintien_marques"] = safe_get(o, ["plan_industriel", "maintien_marques_savoir_faire"])

    # Financement
    row["apport_fp"] = safe_get(o, ["financement", "apport_fonds_propres_eur"])
    row["apport_origine_doc"] = safe_get(o, ["financement", "apport_origine_documentee"])
    row["dette_engagement_ferme"] = safe_get(o, ["financement", "dette_bancaire_engagement_ferme"])
    row["dette_lettre_confort"] = safe_get(o, ["financement", "dette_bancaire_lettre_confort"])
    row["dette_montant"] = safe_get(o, ["financement", "dette_bancaire_montant_eur"])
    row["bfr_redemarrage"] = safe_get(o, ["financement", "bfr_redemarrage_eur"])
    row["tresorerie_securite"] = safe_get(o, ["financement", "tresorerie_securite_eur"])

    # Engagements specifiques
    row["incessibilite_mois"] = safe_get(o, ["engagements_specifiques", "incessibilite_temporaire_mois"])
    row["caution_dirig_montant"] = safe_get(o, ["engagements_specifiques", "caution_dirigeant_montant_eur"])
    row["caution_dirig_mois"] = safe_get(o, ["engagements_specifiques", "caution_dirigeant_duree_mois"])
    row["penalites_social"] = safe_get(o, ["engagements_specifiques", "penalites_non_respect_social_eur"])
    row["non_demembrement"] = safe_get(o, ["engagements_specifiques", "non_demembrement"])

    # Conditions suspensives
    row["aucune_cs"] = safe_get(o, ["conditions_suspensives", "aucune_cs"])
    row["nb_cs"] = safe_get(o, ["conditions_suspensives", "nb_conditions"])
    row["agressivite_cs"] = safe_get(o, ["conditions_suspensives", "agressivite_envers_dirigeants"])
    cs_items = safe_get(o, ["conditions_suspensives", "items"], []) or []
    row["cs_items"] = cs_items

    # Forme
    row["nb_pages_total"] = safe_get(o, ["forme_presentation", "nb_pages_total"])
    row["nb_pages_corps"] = safe_get(o, ["forme_presentation", "nb_pages_corps_offre"])
    row["nb_pages_annexes"] = safe_get(o, ["forme_presentation", "nb_pages_annexes"])
    row["structure_dom"] = safe_get(o, ["forme_presentation", "structure_dominante"])
    row["ton"] = safe_get(o, ["forme_presentation", "ton_dominant"])
    row["exec_summary"] = safe_get(o, ["forme_presentation", "executive_summary_present"])

    # All annex flags
    for ax in ["annexes_kbis", "annexes_cv_dirigeants", "annexes_attest_bancaire",
               "annexes_lettres_soutien_clients", "annexes_lettres_soutien_collectivites",
               "annexes_business_plan", "annexes_organigramme_cible",
               "annexes_comptes_sociaux_3ans", "annexes_attest_fisc_sociale",
               "annexes_rib", "annexes_cni_dirigeants", "signature_docusign"]:
        row[ax] = safe_get(o, ["forme_presentation", ax])
    row["qualite_redac"] = safe_get(o, ["forme_presentation", "qualite_redactionnelle"])

    # Signaux
    for sf in ["soutien_collectivite_locale", "soutien_clients_cles", "soutien_banques_historiques",
               "personnalisation_visite_site", "personnalisation_rencontre_equipes",
               "personnalisation_etude_contrats", "differenciation_concurrents_explicite",
               "elements_emotionnels_sociaux", "declaration_L642_3_signee",
               "faculte_substitution_precise"]:
        row[sf] = safe_get(o, ["signaux_faibles", sf])
    row["coherence_prix_bp"] = safe_get(o, ["signaux_faibles", "coherence_prix_BP"])
    errs = safe_get(o, ["signaux_faibles", "erreurs_apparentes"], []) or []
    row["nb_erreurs"] = len(errs) if isinstance(errs, list) else 0
    row["erreurs"] = errs

    # Extraits
    row["phrase_positionnement"] = safe_get(o, ["extraits_remarquables", "phrase_positionnement"])
    row["phrase_engagement_social"] = safe_get(o, ["extraits_remarquables", "phrase_engagement_social"])
    row["phrase_vision"] = safe_get(o, ["extraits_remarquables", "phrase_vision_strategique"])
    row["phrase_prix"] = safe_get(o, ["extraits_remarquables", "phrase_justification_prix"])

    # Avocat
    row["avocat_cabinet"] = safe_get(o, ["avocat_repreneur", "cabinet"])
    return row


def load_all():
    offres = []
    for f in sorted(OFFRES_DIR.glob("*.json")):
        try:
            with open(f) as fp:
                d = json.load(fp)
            offres.append(flatten_offre(d))
        except Exception as e:
            print(f"ERR offre {f.name}: {e}")
    df_o = pd.DataFrame(offres)
    print(f"Loaded {len(df_o)} offres")

    dossiers = []
    for f in sorted(DOSSIERS_DIR.glob("*.json")):
        try:
            with open(f) as fp:
                d = json.load(fp)
            row = {
                "dossier_id": safe_get(d, ["meta", "dossier_id"]),
                "dossier_folder": safe_get(d, ["meta", "dossier_folder"]),
                "cible": safe_get(d, ["identification", "cible_raison_sociale"]),
                "naf": safe_get(d, ["identification", "naf_secteur"]),
                "ca_eur": safe_get(d, ["identification", "ca_dernier_exercice_eur"]),
                "effectif": safe_get(d, ["identification", "effectif_total"]),
                "procedure": safe_get(d, ["identification", "type_procedure"]),
                "issue": safe_get(d, ["issue_dossier", "issue_globale_dossier"]),
                "repreneur_retenu": safe_get(d, ["issue_dossier", "repreneur_retenu"]),
                "prix_retenu_eur": safe_get(d, ["issue_dossier", "prix_retenu_eur"]),
                "emplois_repris_retenu": safe_get(d, ["issue_dossier", "emplois_repris_retenu"]),
                "motifs_tribunal_verbatim": safe_get(d, ["issue_dossier", "motifs_tribunal_verbatim"]),
                "motifs_rejet_synthese": safe_get(d, ["issue_dossier", "motifs_rejet_synthese"]),
                "nb_offres_concurrentes": safe_get(d, ["issue_dossier", "nb_offres_concurrentes"]),
                "enseignement_clef": safe_get(d, ["issue_dossier", "enseignement_clef"]),
            }
            dossiers.append(row)
        except Exception as e:
            print(f"ERR dossier {f.name}: {e}")
    df_d = pd.DataFrame(dossiers)
    print(f"Loaded {len(df_d)} dossiers")
    return df_o, df_d


if __name__ == "__main__":
    df_o, df_d = load_all()
    df_o.to_pickle(OUT / "offres.pkl")
    df_d.to_pickle(OUT / "dossiers.pkl")

    # Quick top-level distribution
    print("\n=== Retenue distribution ===")
    print(df_o["retenue"].value_counts(dropna=False))
    print("\n=== Issue globale ===")
    print(df_o["issue_dossier"].value_counts(dropna=False))
    print("\n=== Procedure ===")
    print(df_o["procedure"].value_counts(dropna=False))
    print("\n=== Forme repreneur ===")
    print(df_o["forme_repreneur"].value_counts(dropna=False))
    print("\n=== Confidence ===")
    print(df_o["confidence"].value_counts(dropna=False))
