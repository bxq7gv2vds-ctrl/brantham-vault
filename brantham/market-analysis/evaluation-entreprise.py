#!/usr/bin/env python3
"""
Modèle d'évaluation d'entreprise M&A basé sur multiples comparables
Analyse multi-critères pour valorisation cibles
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

class MethodeEvaluation(Enum):
    """Méthodes d'évaluation disponibles"""
    DCF = "Discounted Cash Flow"
    MULTIPLES = "Multiples de marché"
    ASSET_BASED = "Basée sur les actifs"
    MARKET_COMPARE = "Comparaison de marché"

@dataclass
class MultipleSectoriel:
    """Multiple sectoriel par segment"""
    secteur: str
    multiple_revenus: float
    multiple_ebitda: float
    multiple_ebit: float
    multiple_bv: float
    nb_transactions: int
    date_maj: str

    def __post_init__(self):
        # Validation des multiples (typiquement 1-50x)
        self.multiple_revenus = max(0.1, min(50, self.multiple_revenus))
        self.multiple_ebitda = max(0.1, min(50, self.multiple_ebitda))
        self.multiple_ebit = max(0.1, min(50, self.multiple_ebit))

class ModeleEvaluationEntreprise:
    """
    Modèle d'évaluation M&A intégrant multiples méthodes
    Pondération automatique selon le secteur et la taille
    """

    def __init__(self):
        self.multiples_sectoriels = self._charger_multiples_sectoriels()
        self.risque_pays = {
            'FR': 1.0, 'DE': 1.05, 'UK': 1.1, 'US': 1.15,
            'ES': 1.2, 'IT': 1.25, 'PL': 1.3
        }

    def _charger_multiples_sectoriels(self) -> Dict[str, MultipleSectoriel]:
        """Multiples sectoriels basés sur données récentes"""
        return {
            'Tech/SaaS': MultipleSectoriel(
                secteur='Tech/SaaS',
                multiple_revenus=3.5,
                multiple_ebitda=12.0,
                multiple_ebit=15.0,
                multiple_bv=2.8,
                nb_transactions=245,
                date_maj='2024-06'
            ),
            'Consulting': MultipleSectoriel(
                secteur='Consulting',
                multiple_revenus=1.8,
                multiple_ebitda=8.5,
                multiple_ebit=10.2,
                multiple_bv=1.5,
                nb_transactions=89,
                date_maj='2024-06'
            ),
            'Ingénierie': MultipleSectoriel(
                secteur='Ingénierie',
                multiple_revenus=1.2,
                multiple_ebitda=6.8,
                multiple_ebit=8.1,
                multiple_bv=0.9,
                nb_transactions=156,
                date_maj='2024-06'
            ),
            'Cybersécurité': MultipleSectoriel(
                secteur='Cybersécurité',
                multiple_revenus=4.2,
                multiple_ebitda=18.0,
                multiple_ebit=22.5,
                multiple_bv=3.5,
                nb_transactions=67,
                date_maj='2024-06'
            ),
            'Data/Analytics': MultipleSectoriel(
                secteur='Data/Analytics',
                multiple_revenus=2.8,
                multiple_ebitda=14.5,
                multiple_ebit=17.8,
                multiple_bv=2.2,
                nb_transactions=93,
                date_maj='2024-06'
            )
        }

    def calculer_evaluation_complet(
        self,
        donnees_entreprise: Dict,
        methodes: List[MethodeEvaluation] = None,
        poids_methodes: Dict = None
    ) -> Dict:
        """
        Évaluation complète avec méthode principale et secondaires

        Args:
            donnees_entreprise: Données financières de l'entreprise
            methodes: Liste des méthodes à utiliser
            poids_methodes: Pondération par méthode

        Returns:
            Rapport d'évaluation détaillé
        """
        if methodes is None:
            methodes = [MethodeEvaluation.MULTIPLES, MethodeEvaluation.DCF]

        if poids_methodes is None:
            poids_methodes = {
                MethodeEvaluation.MULTIPLES: 0.6,
                MethodeEvaluation.DCF: 0.4
            }

        # Validation des poids
        total_poids = sum(poids_methodes.values())
        poids_methodes = {k: v/total_poids for k, v in poids_methodes.items()}

        # Calcul des différentes évaluations
        evaluations = {}
        for methode in methodes:
            if methode == MethodeEvaluation.MULTIPLES:
                evaluations[methode] = self._evaluation_multiples(donnees_entreprise)
            elif methode == MethodeEvaluation.DCF:
                evaluations[methode] = self._evaluation_dcf(donnees_entreprise)
            elif methode == MethodeEvaluation.ASSET_BASED:
                evaluations[methode] = self._evaluation_actif_basee(donnees_entreprise)

        # Pondération finale
        evaluation_ponderee = self._ponderer_evaluations(evaluations, poids_methodes)

        # Analyse de sensibilité
        sensibilite = self._analyse_sensibilite(donnees_entreprise)

        return {
            'evaluation_fondamentale': evaluation_ponderee,
            'evaluations_individuelles': evaluations,
            'methodes_utilisees': methodes,
            'poids_methodes': poids_methodes,
            'analyse_sensibilite': sensibilite,
            'date_evaluation': pd.Timestamp.now().strftime('%Y-%m-%d'),
            'confiance': self._calculer_confiance(donnees_entreprise, evaluations)
        }

    def _evaluation_multiples(self, donnees: Dict) -> Dict:
        """Évaluation par multiples sectoriels"""
        secteur = self._identifier_secteur(donnees['code_naf'])
        multiple = self.multiples_sectoriels.get(secteur)

        if not multiple:
            return {
                'methode': 'Multiples',
                'valeur': 0,
                'erreur': 'Secteur non trouvé dans la base de multiples',
                'multiples_utilises': {}
            }

        # Calcul des différentes valorisations
        revenus = donnees['chiffre_affaires']
        ebitda = donnees.get('ebitda', donnees.get('resultat_oper', 0))
        ebit = donnees.get('ebit', donnees.get('resultat', 0))
        bv = donnees.get('valeur_actif_net', revenus * 0.7)  # Estimation

        valorisations = {
            'revenus': revenus * multiple.multiple_revenus,
            'ebitda': ebitda * multiple.multiple_ebitda,
            'ebit': ebit * multiple.multiple_ebit,
            'bv': bv * multiple.multiple_bv
        }

        # Moyenne pondérée (EBITDA + EBIT + Revenus)
        poids = {'ebitda': 0.5, 'ebit': 0.3, 'revenus': 0.2}
        valeur_finale = sum(valorisations[k] * poids[k] for k in poids.keys())

        # Ajustement selon facteurs qualitatifs
        facteurs_qualitatifs = self._calculer_facteurs_qualitatifs(donnees)
        valeur_finale *= facteurs_qualitatifs['ajustement_multiple']

        return {
            'methode': 'Multiples',
            'valeur': valeur_finale,
            'multiples_utilises': {
                'multiple_revenus': multiple.multiple_revenus,
                'multiple_ebitda': multiple.multiple_ebitda,
                'multiple_ebit': multiple.multiple_ebit
            },
            'secteur': secteur,
            'transaction_reference': multiple.nb_transactions,
            'facteurs_qualitatifs': facteurs_qualitatifs
        }

    def _evaluation_dcf(self, donnees: Dict) -> Dict:
        """Évaluation par DCF simplifiée"""
        # Paramètres DCF
        taux_actualisation = 0.12  # 12% pour PME tech
        croissance_perpetuelle = 0.03  # 3%
        horizon_projection = 5  # 5 ans

        # Flux de trésorerie disponible
        fcf = donnees.get('fcf', donnees.get('ebitda', 0) * 0.7)

        # Projection des flux
        projections = []
        flux_actualise = 0

        for annee in range(1, horizon_projection + 1):
            croissance = 1.15 if annee <= 3 else 1.08  # Croissance forte puis ralentissement
            flux_futur = fcf * (croissance ** annee)
            flux_actualise += flux_futur / ((1 + taux_actualisation) ** annee)
            projections.append(flux_futur)

        # Valeur terminale
        valeur_terminale = projections[-1] * (1 + croissance_perpetuelle) / (taux_actualisation - croissance_perpetuelle)
        valeur_terminale_actualisee = valeur_terminale / ((1 + taux_actualisation) ** horizon_projection)

        valeur_entreprise = flux_actualise + valeur_terminale_actualisee

        # Ajustement dette nette
        dette_nette = donnees.get('dettes_financieres', 0) - donnees.get('liquidites', 0)
        valeur_equite = valeur_entreprise - dette_nette

        return {
            'methode': 'DCF',
            'valeur_entreprise': valeur_entreprise,
            'valeur_equite': max(0, valeur_equite),
            'fcf': fcf,
            'taux_actualisation': taux_actualisation,
            'croissance_perpetuelle': croissance_perpetuelle,
            'projections': projections,
            'valeur_terminale': valeur_terminale
        }

    def _evaluation_actif_basee(self, donnees: Dict) -> Dict:
        """Évaluation basée sur les actifs"""
        valeur_actif = donnees.get('valeur_actif_net', donnees['chiffre_affaires'] * 0.7)

        # Ajustement selon les actifs incorporels
        if donnees.get('actif incorporel') > valeur_actif * 0.3:
            # Forte composante incorporelle
            facteur = 1.2
        else:
            # Principalement actifs corporels
            facteur = 0.9

        valeur_finale = valeur_actif * facteur

        return {
            'methode': 'Actif Base',
            'valeur': valeur_finale,
            'valeur_actif_brut': donnees.get('valeur_actif', 0),
            'valeur_actif_net': valeur_actif,
            'facteur_ajustement': facteur
        }

    def _ponderer_evaluations(self, evaluations: Dict, poids: Dict) -> float:
        """Pondération des différentes évaluations"""
        return sum(evaluations[methode]['valeur'] * poids[methode]
                  for methode in evaluations if methode in poids)

    def _calculer_facteurs_qualitatifs(self, donnees: Dict) -> Dict:
        """Calcul des facteurs qualitatifs d'ajustement"""
        ajustement = 1.0

        # Position de marché
        if donnees.get('part_marche', 0) > 20:
            ajustement *= 1.1
        elif donnees.get('part_marche', 0) < 5:
            ajustement *= 0.9

        # Propriété intellectuelle
        if donnees.get('brevets', 0) > 10:
            ajustement *= 1.15
        elif donnees.get('brevets', 0) == 0:
            ajustement *= 0.95

        # Équipe de direction
        if donnees.get('qualite_equipe', 'moyen') == 'excellent':
            ajustement *= 1.1
        elif donnees.get('qualite_equipe', 'moyen') == 'faible':
            ajustement *= 0.85

        # Croissance récente
        if donnees.get('croissance_ca', 0) > 20:
            ajustement *= 1.05
        elif donnees.get('croissance_ca', 0) < 0:
            ajustement *= 0.9

        return {
            'ajustement_multiple': ajustement,
            'position_marche': donnees.get('part_marche', 0),
            'proprietes_intellectuelles': donnees.get('brevets', 0),
            'qualite_equipe': donnees.get('qualite_equipe', 'moyen'),
            'croissance': donnees.get('croissance_ca', 0)
        }

    def _identifier_secteur(self, code_naf: str) -> str:
        """Identifier le secteur à partir du code NAF"""
        naf_secteurs = {
            '62': 'Tech/SaaS',  # Programmation, conseil tech
            '63': 'Consulting', # Consultance diverses
            '69': 'Ingénierie', # Ingénierie, conseil technique
            '64': 'Cybersécurité' # Services de sécurité
        }

        code = code_naf[:2]
        return naf_secteurs.get(code, 'Autre')

    def _analyse_sensibilite(self, donnees: Dict) -> Dict:
        """Analyse de sensibilité aux variations de paramètres"""
        base_evaluation = self._evaluation_multiples(donnees)['valeur']

        variations = {
            'croissance_-10%': base_evaluation * 0.9,
            'croissance_+10%': base_evaluation * 1.1,
            'multiple_-20%': base_evaluation * 0.8,
            'multiple_+20%': base_evaluation * 1.2,
            'risque_pays': base_evaluation * self.risque_pays.get('FR', 1.0)
        }

        return {
            'evaluation_base': base_evaluation,
            'variations_percent': variations,
            'fourchette_min': min(variations.values()),
            'fourchette_max': max(variations.values()),
            'amplitude': (max(variations.values()) - min(variations.values())) / base_evaluation * 100
        }

    def _calculer_confiance(self, donnees: Dict, evaluations: Dict) -> str:
        """Calcul du niveau de confiance dans l'évaluation"""
        facteurs_confiance = []

        # Qualité des données
        if all(k in donnees for k in ['chiffre_affaires', 'ebitda', 'ebit']):
            facteurs_confiance.append(1)
        else:
            facteurs_confiance.append(0.5)

        # Nombre de méthodes utilisées
        facteurs_confiance.append(min(len(evaluations) / 3, 1))

        # Taille de l'échantillon sectoriel
        secteur = self._identifier_secteur(donnees['code_naf'])
        multiple = self.multiples_sectoriels.get(secteur)
        if multiple and multiple.nb_transactions > 50:
            facteurs_confiance.append(1)
        elif multiple and multiple.nb_transactions > 20:
            facteurs_confiance.append(0.7)
        else:
            facteurs_confiance.append(0.5)

        score_confiance = np.mean(facteurs_confiance)

        if score_confiance >= 0.8:
            return 'Élevée'
        elif score_confiance >= 0.6:
            return 'Moyenne'
        else:
            return 'Faible'

    def generer_rapport_complet(self, evaluation: Dict) -> str:
        """Générer un rapport lisible de l'évaluation"""
        rapport = []
        rapport.append("="*60)
        rapport.append("RAPPORT D'ÉVALUATION M&A")
        rapport.append("="*60)

        # Évaluation fondamentale
        fond = evaluation['evaluation_fondamentale']
        rapport.append(f"\n💰 Évaluation Fondamentale: {fond:,.0f}€")
        rapport.append(f"   Niveau de confiance: {evaluation['confiance']}")

        # Méthodes utilisées
        rapport.append(f"\n📊 Méthodes d'évaluation:")
        for methode, poids in evaluation['poids_methodes'].items():
            eval_indiv = evaluation['evaluations_individuelles'][methode]
            rapport.append(f"   • {methode.value}: {eval_indiv['valeur']:,.0f}€ ({poids*100:.0f}%)")

        # Analyse de sensibilité
        sens = evaluation['analyse_sensibilite']
        rapport.append(f"\n📈 Analyse de sensibilité:")
        rapport.append(f"   Évaluation base: {sens['evaluation_base']:,.0f}€")
        rapport.append(f"   Fourchette: {sens['fourchette_min']:,.0f}€ - {sens['fourchette_max']:,.0f}€")
        rapport.append(f"   Amplitude: ±{sens['amplitude']:.1f}%")

        # Facteurs qualitatifs
        multiples = evaluation['evaluations_individuelles'][MethodeEvaluation.MULTIPLES]
        if 'facteurs_qualitatifs' in multiples:
            facteurs = multiples['facteurs_qualitatifs']
            rapport.append(f"\n🎯 Facteurs qualitatifs:")
            rapport.append(f"   Ajustement multiple: {facteurs['ajustement_multiple']:.2f}x")
            rapport.append(f"   Position marché: {facteurs['position_marche']:.1f}%")
            rapport.append(f"   Brevets: {facteurs['proprietes_intellectuelles']}")

        return "\n".join(rapport)

def demo_evaluation():
    """Démonstration du modèle d'évaluation"""
    print("DÉMONSTRATION - Modèle d'évaluation M&A")
    print("="*60)

    # Données d'exemple
    entreprise_exemple = {
        'entreprise_nom': 'TechInnov SAS',
        'code_naf': '6201Z',
        'chiffre_affaires': 2500000,
        'ebitda': 450000,
        'ebit': 380000,
        'resultat': 250000,
        'dettes_financieres': 200000,
        'liquidites': 50000,
        'valeur_actif_net': 1800000,
        'brevets': 15,
        'part_marche': 12,
        'qualite_equipe': 'excellent',
        'croissance_ca': 25
    }

    # Créer et exécuter l'évaluation
    modele = ModeleEvaluationEntreprise()
    evaluation = modele.calculer_evaluation_complet(entreprise_exemple)

    # Afficher le rapport
    rapport = modele.generer_rapport_complet(evaluation)
    print(rapport)

    return evaluation

if __name__ == "__main__":
    demo_evaluation()