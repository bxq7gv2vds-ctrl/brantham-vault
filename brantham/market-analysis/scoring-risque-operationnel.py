#!/usr/bin/env python3
"""
Automate de scoring de risque opérationnel pour cibles M&A
Analyse multi-dimensionnelle avec évaluation automatique des risques
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

class NiveauRisque(Enum):
    """Niveaux de risque opérationnel"""
    FAIBLE = 1
    MODERE = 2
    ELEVE = 3
    CRITIQUE = 4

class CritereRisque(Enum):
    """Critères d'évaluation des risques"""
    DEPENDANCE_CLIENTS = "Dépendance clients"
    DEPENDANCE_FOURNISSEURS = "Dépendance fournisseurs"
    ROTATION_PERSONNEL = "Rotation personnel"
    CONFORMITE_REGULATOIRE = "Conformité réglementaire"
    CYBERSECURITE = "Cybersécurité"
    CONTROLES_INTERNES = "Contrôles internes"
    SUCCESSION_DIRIGEANTS = "Succession dirigeants"
    DEPENDANCE_TECHNOLOGIE = "Dépendance technologie"
    EXPOSITION_GEOGRAPHIQUE = "Exposition géographique"
    LIQUIDITE_FINANCIERE = "Liquidité financière"

@dataclass
class ScoreRisque:
    """Score de risque par catégorie"""
    critere: CritereRisque
    score: float
    niveau: NiveauRisque
    details: str
    ponderation: float

class AutomateScoringRisque:
    """
    Automate intelligent de scoring de risque opérationnel
    Pondération automatique selon le secteur et la taille de l'entreprise
    """

    def __init__(self):
        self.seuils_risque = {
            NiveauRisque.FAIBLE: (0, 25),
            NiveauRisque.MODERE: (25, 50),
            NiveauRisque.ELEVE: (50, 75),
            NiveauRisque.CRITIQUE: (75, 100)
        }

        self.sectorspecific_weights = {
            'Tech/SaaS': {
                CritereRisque.CYBERSECURITE: 0.15,
                CritereRisque.DEPENDANCE_TECHNOLOGIE: 0.12,
                CritereRisque.ROTATION_PERSONNEL: 0.10,
                CritereRisque.CONFORMITE_REGULATOIRE: 0.08
            },
            'Consulting': {
                CritereRisque.DEPENDANCE_CLIENTS: 0.18,
                CritereRisque.ROTATION_PERSONNEL: 0.15,
                CritereRisque.CONTROLES_INTERNES: 0.12,
                CritereRisque.SUCCESSION_DIRIGEANTS: 0.10
            },
            'Ingénierie': {
                CritereRisque.DEPENDANCE_FOURNISSEURS: 0.16,
                CritereRisque.CONFORMITE_REGULATOIRE: 0.14,
                CritereRisque.EXPOSITION_GEOGRAPHIQUE: 0.12,
                CritereRisque.CONTROLES_INTERNES: 0.10
            },
            'Cybersécurité': {
                CritereRisque.CYBERSECURITE: 0.20,
                CritereRisque.CONFORMITE_REGULATOIRE: 0.15,
                CritereRisque.DEPENDANCE_TECHNOLOGIE: 0.12,
                CritereRisque.CONTROLES_INTERNES: 0.10
            },
            'Data/Analytics': {
                CritereRisque.CYBERSECURITE: 0.16,
                CritereRisque.CONFORMITE_REGULATOIRE: 0.14,
                CritereRisque.DEPENDANCE_TECHNOLOGIE: 0.13,
                CritereRisque.CONTROLES_INTERNES: 0.11
            }
        }

        self.base_weights = {
            CritereRisque.DEPENDANCE_CLIENTS: 0.10,
            CritereRisque.DEPENDANCE_FOURNISSEURS: 0.08,
            CritereRisque.ROTATION_PERSONNEL: 0.10,
            CritereRisque.CONFORMITE_REGULATOIRE: 0.08,
            CritereRisque.CYBERSECURITE: 0.12,
            CritereRisque.CONTROLES_INTERNES: 0.10,
            CritereRisque.SUCCESSION_DIRIGEANTS: 0.08,
            CritereRisque.DEPENDANCE_TECHNOLOGIE: 0.07,
            CritereRisque.EXPOSITION_GEOGRAPHIQUE: 0.07,
            CritereRisque.LIQUIDITE_FINANCIERE: 0.10
        }

    def calculer_score_global(self, donnees_entreprise: Dict) -> Dict:
        """
        Calcule le score de risque opérationnel global

        Args:
            donnees_entreprise: Données complètes de l'entreprise

        Returns:
            Rapport de scoring complet
        """
        # Identifier le secteur pour la pondération spécifique
        secteur = self._identifier_secteur(donnees_entreprise['code_naf'])

        # Calculer les scores individuels
        scores_individuels = self._calculer_scores_individuels(donnees_entreprise)

        # Appliquer pondération sectorielle
        poids = self._obtenir_poids_sectoriels(secteur)
        scores_pondérés = self._pondérer_scores(scores_individuels, poids)

        # Score global pondéré
        score_global = sum(score.ponderation * score.score
                          for score in scores_pondérés.values())

        # Déterminer niveau de risque global
        niveau_global = self._determiner_niveau_risque(score_global)

        # Analyse des risques majeurs
        risques_majeurs = self._identifier_risques_majeurs(scores_pondérés)

        # Recommandations prioritaires
        recommandations = self._generer_recommandations(scores_pondérés, niveau_global)

        return {
            'score_global': score_global,
            'niveau_risque_global': niveau_global,
            'secteur': secteur,
            'scores_detailles': scores_pondérés,
            'risques_majeurs': risques_majeurs,
            'recommandations': recommandations,
            'date_evaluation': pd.Timestamp.now().strftime('%Y-%m-%d'),
            'facteurs_aggravants': self._identifier_facteurs_aggravants(donnees_entreprise),
            'facteurs_attenuants': self._identifier_facteurs_attenuants(donnees_entreprise)
        }

    def _calculer_scores_individuels(self, donnees: Dict) -> Dict[CritereRisque, float]:
        """Calcule les scores individuels pour chaque critère"""
        scores = {}

        # Dépendance clients (>30% = risque élevé)
        part_max_clients = donnees.get('part_max_clients', 0)
        scores[CritereRisque.DEPENDANCE_CLIENTS] = self._score_dependance_clients(part_max_clients)

        # Dépendance fournisseurs (>25% = risque modéré)
        part_max_fournisseurs = donnees.get('part_max_fournisseurs', 0)
        scores[CritereRisque.DEPENDANCE_FOURNISSEURS] = self._score_dependance_fournisseurs(part_max_fournisseurs)

        # Rotation personnel (>20% = risque élevé)
        taux_rotation = donnees.get('taux_rotation_personnel', 0)
        scores[CritereRisque.ROTATION_PERSONNEL] = self._score_rotation_personnel(taux_rotation)

        # Conformité réglementaire
        score_conformite = donnees.get('score_conformite', 50)
        scores[CritereRisque.CONFORMITE_REGULATOIRE] = 100 - score_conformite

        # Cybersécurité
        score_securite = donnees.get('score_cybersecurite', 50)
        scores[CritereRisque.CYBERSECURITE] = 100 - score_securite

        # Contrôles internes
        score_controles = donnees.get('score_controles_interne', 50)
        scores[CritereRisque.CONTROLES_INTERNES] = 100 - score_controles

        # Succession dirigeants
        score_succession = donnees.get('plan_succession', 50)
        scores[CritereRisque.SUCCESSION_DIRIGEANTS] = 100 - score_succession

        # Dépendance technologie
        score_dependance_tech = donnees.get('dependance_technologie', 30)
        scores[CritereRisque.DEPENDANCE_TECHNOLOGIE] = score_dependance_tech

        # Exposition géographique
        exposition_geo = donnees.get('exposition_geo_risque', 0)
        scores[CritereRisque.EXPOSITION_GEOGRAPHIQUE] = exposition_geo * 100

        # Liquidité financière
        ratio_liquidite = donnees.get('ratio_liquidite', 1.0)
        scores[CritereRisque.LIQUIDITE_FINANCIERE] = self._score_liquidite(ratio_liquidite)

        return scores

    def _score_dependance_clients(self, part_max: float) -> float:
        """Évalue le risque de dépendance client"""
        if part_max > 50:
            return 85
        elif part_max > 30:
            return 65
        elif part_max > 15:
            return 40
        else:
            return 20

    def _score_dependance_fournisseurs(self, part_max: float) -> float:
        """Évalue le risque de dépendance fournisseur"""
        if part_max > 40:
            return 70
        elif part_max > 25:
            return 50
        elif part_max > 15:
            return 30
        else:
            return 20

    def _score_rotation_personnel(self, taux: float) -> float:
        """Évalue le risque lié à la rotation du personnel"""
        if taux > 30:
            return 80
        elif taux > 20:
            return 60
        elif taux > 10:
            return 35
        else:
            return 20

    def _score_liquidite(self, ratio: float) -> float:
        """Évalue le risque lié à la liquidité"""
        if ratio < 0.5:
            return 90
        elif ratio < 1.0:
            return 60
        elif ratio < 1.5:
            return 30
        else:
            return 15

    def _identifier_secteur(self, code_naf: str) -> str:
        """Identifie le secteur à partir du code NAF"""
        naf_secteurs = {
            '62': 'Tech/SaaS',
            '63': 'Consulting',
            '69': 'Ingénierie',
            '64': 'Cybersécurité'
        }
        return naf_secteurs.get(code_naf[:2], 'Autre')

    def _obtenir_poids_sectoriels(self, secteur: str) -> Dict[CritereRisque, float]:
        """Obtient les poids sectoriels spécifiques"""
        if secteur in self.sectorspecific_weights:
            sector_weights = self.sectorspecific_weights[secteur]
            # Normalisation
            total = sum(sector_weights.values())
            return {k: v/total for k, v in sector_weights.items()}
        return self.base_weights

    def _pondérer_scores(self, scores: Dict, poids: Dict) -> Dict[CritereRisque, ScoreRisque]:
        """Pondère les scores selon les poids définis"""
        scores_pondérés = {}

        for critere, score_brut in scores.items():
            ponderation = poids.get(critere, 0.05)  # Poids par défaut
            niveau = self._determiner_niveau_risque(score_brut)

            details = self._generer_details_critere(critere, score_brut, niveau)

            scores_pondérés[critere] = ScoreRisque(
                critere=critere,
                score=score_brut,
                niveau=niveau,
                details=details,
                ponderation=ponderation
            )

        return scores_pondérés

    def _determiner_niveau_risque(self, score: float) -> NiveauRisque:
        """Détermine le niveau de risque selon le score"""
        if score <= 25:
            return NiveauRisque.FAIBLE
        elif score <= 50:
            return NiveauRisque.MODERE
        elif score <= 75:
            return NiveauRisque.ELEVE
        else:
            return NiveauRisque.CRITIQUE

    def _generer_details_critere(self, critere: CritereRisque, score: float, niveau: NiveauRisque) -> str:
        """Génère des détails pour chaque critère"""
        details_map = {
            CritereRisque.DEPENDANCE_CLIENTS: {
                NiveauRisque.FAIBLE: "Diversification clientèle satisfaisante",
                NiveauRisque.MODERE: "Dépendance modérée sur certains clients",
                NiveauRisque.ELEVE: "Dépendance significative identifiable",
                NiveauRisque.CRITIQUE: "Risque critique avec client dominant"
            },
            CritereRisque.DEPENDANCE_FOURNISSEURS: {
                NiveauRisque.FAIBLE: "Fournisseurs diversifiés",
                NiveauRisque.MODERE: "Quelques fournisseurs clés",
                NiveauRisque.ELEVE: "Dépendance envers fournisseurs spécifiques",
                NiveauRisque.CRITIQUE: "Risque d'approvisionnement critique"
            },
            CritereRisque.ROTATION_PERSONNEL: {
                NiveauRisque.FAIBLE: "Stabilité de l'équipe satisfaisante",
                NiveauRisque.MODERE: "Rotation modérée dans certains métiers",
                NiveauRisque.ELEVE: "Problème de rétention identifié",
                NiveauRisque.CRITIQUE: "Rotation excessive affectant la performance"
            }
        }

        return details_map.get(critere, {}).get(niveau, f"Niveau {niveau.name}")

    def _identifier_risques_majeurs(self, scores: Dict) -> List[Dict]:
        """Identifie les 3 risques majeurs"""
        tries_critiques = [s for s in scores.values() if s.niveau in [NiveauRisque.ELEVE, NiveauRisque.CRITIQUE]]

        # Trier par ponderation * score
        tries_critiques.sort(key=lambda x: x.ponderation * x.score, reverse=True)

        return [
            {
                'critere': s.critere.value,
                'score': s.score,
                'niveau': s.niveau.name,
                'ponderation': s.ponderation,
                'details': s.details
            }
            for s in tries_critiques[:3]
        ]

    def _generer_recommandations(self, scores: Dict, niveau_global: NiveauRisque) -> List[str]:
        """Génère des recommandations prioritaires"""
        recommandations = []

        # Recommandations par niveau de risque global
        if niveau_global in [NiveauRisque.ELEVE, NiveauRisque.CRITIQUE]:
            recommandations.append("Évaluation due diligence approfondie recommandée")
            recommandations.append("Plan d'atténuation des risques obligatoire")
        elif niveau_global == NiveauRisque.MODERE:
            recommandations.append("Surveillance continue des risques identifiés")

        # Recommandations spécifiques aux risques majeurs
        risques_urgent = [s for s in scores.values() if s.niveau == NiveauRisque.CRITIQUE]
        for risque in risques_urgent:
            if risque.critere == CritereRisque.CYBERSECURITE:
                recommandations.append("Audit de cybersécurité immédiat")
            elif risque.critere == CritereRisque.DEPENDANCE_CLIENTS:
                recommandations.append("Stratégie de diversification clientèle prioritaire")
            elif risque.critere == CritereRisque.ROTATION_PERSONNEL:
                recommandations.append("Programme de rétention d'urgence")

        return recommandations[:5]  # Maximum 5 recommandations

    def _identifier_facteurs_aggravants(self, donnees: Dict) -> List[str]:
        """Identifie les facteurs aggravants"""
        aggravants = []

        if donnees.get('croissance_ca', 0) < 0:
            aggravants.append("Chiffre d'affaires en décroissance")

        if donnees.get('endettement', 0) > 3:
            aggravants.append("Endettement élevé")

        if donnees.get('litiges_en_cours', 0) > 5:
            aggravants.append("Nombre important de litiges en cours")

        if donnees.get('dependance_unique_client', False):
            aggravants.append("Dépendance à un seul client")

        return aggravants

    def _identifier_facteurs_attenuants(self, donnees: Dict) -> List[str]:
        """Identifie les facteurs atténuants"""
        attenuants = []

        if donnees.get('doodle', None) == 'stable':
            attenuants.append("Direction stable")

        if donnees.get('croissance_ca', 0) > 20:
            attenuants.append("Croissance forte et régulière")

        if donnees.get('nombre_brevets', 0) > 10:
            attenuants.append("Portefeuille de propriété intellectuelle solide")

        if donnees.get('qualite_equipe', 'moyen') == 'excellent':
            attenuants.append("Équipe de direction de qualité")

        return attenuants

    def generer_rapport_risque(self, scoring: Dict) -> str:
        """Génère un rapport lisible du scoring de risque"""
        rapport = []
        rapport.append("="*60)
        rapport.append("RAPPORT DE SCORING DE RISQUE OPÉRATIONNEL")
        rapport.append("="*60)

        # Score global
        niveau = scoring['niveau_risque_global']
        rapport.append(f"\n🎯 Score Global: {scoring['score_global']:.1f}/100")
        rapport.append(f"   Niveau de Risque: {niveau.name}")
        rapport.append(f"   Secteur: {scoring['secteur']}")

        # Risques majeurs
        rapport.append(f"\n⚠️  Risques Majeurs:")
        for risque in scoring['risques_majeurs']:
            rapport.append(f"   • {risque['critere']}: {risque['score']:.1f} ({risque['niveau']})")

        # Recommandations
        rapport.append(f"\n💡 Recommandations:")
        for rec in scoring['recommandations']:
            rapport.append(f"   • {rec}")

        # Facteurs
        if scoring['facteurs_aggravants']:
            rapport.append(f"\n🔴 Facteurs Aggravants:")
            for facteur in scoring['facteurs_aggravants']:
                rapport.append(f"   • {facteur}")

        if scoring['facteurs_attenuants']:
            rapport.append(f"\n🟢 Facteurs Atténuants:")
            for facteur in scoring['facteurs_attenuants']:
                rapport.append(f"   • {facteur}")

        return "\n".join(rapport)

def demo_scoring():
    """Démonstration de l'automate de scoring de risque"""
    print("DÉMONSTRATION - Scoring de Risque Opérationnel")
    print("="*60)

    # Données d'exemple
    entreprise_exemple = {
        'entreprise_nom': 'TechInnov SAS',
        'code_naf': '6201Z',
        'chiffre_affaires': 2500000,
        'part_max_clients': 35,
        'part_max_fournisseurs': 20,
        'taux_rotation_personnel': 18,
        'score_conformite': 70,
        'score_cybersecurite': 60,
        'score_controles_interne': 65,
        'plan_succession': 40,
        'dependance_technologie': 45,
        'exposition_geo_risque': 0.3,
        'ratio_liquidite': 1.2,
        'croissance_ca': 25,
        'endettement': 2.5,
        'litiges_en_cours': 2,
        'dependance_unique_client': False,
        'doodle': 'stable',
        'nombre_brevets': 15,
        'qualite_equipe': 'excellent'
    }

    # Créer et exécuter le scoring
    automate = AutomateScoringRisque()
    scoring = automate.calculer_score_global(entreprise_exemple)

    # Afficher le rapport
    rapport = automate.generer_rapport_risque(scoring)
    print(rapport)

    return scoring

if __name__ == "__main__":
    demo_scoring()