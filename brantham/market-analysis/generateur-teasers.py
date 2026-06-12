#!/usr/bin/env python3
"""
Générateur de teasers d'investissement structurés
Automatisation de la création de documents professionnels pour les deals M&A
"""

import json
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from enum import Enum
import datetime

class TypeInvestissement(Enum):
    """Types d'investissement"""
    ACQUISITION = "Acquisition"
    INVESTISSEMENT_MINORITAIRE = "Investissement minoritaire"
    INVESTISSEMENT_MAJORITAIRE = "Investissement majoritaire"
    LBO = "LBO"
    MBO = "MBO"

class SecteurActivite(Enum):
    """Secteurs d'activité"""
    TECH_SaaS = "Tech/SaaS"
    CONSULTING = "Consulting"
    INGENIERIE = "Ingénierie"
    CYBERSECURITE = "Cybersécurité"
    DATA_ANALYTICS = "Data/Analytics"
    AUTRE = "Autre"

@dataclass
class InformationFinanciere:
    """Informations financières de l'entreprise"""
    ca_annuel: float
    ebitda: float
    resultat_net: float
    croissance_ca: float
    marge_ebitda: float
   endettement_net: float
    liquidites: float

@dataclass
class PointsForts:
    """Points forts de l'entreprise"""
    competitivite: List[str]
    equipe: List[str]
    technologie: List[str]
    position_marche: List[str]
    strategie: List[str]

@dataclass class OpportuniteInvestissement:
    """Opportunité d'investissement"""
    description: str
    taille_marche: str
    croissance: str
    avantage_competitif: str
    projections: str

class GenerateurTeasers:
    """
    Générateur professionnel de teasers d'investissement
    Structure standardisée avec sections adaptatives selon le type d'investissement
    """

    def __init__(self):
        self.structure_standard = [
            "header",
            "resume_executif",
            "presentation_entreprise",
            "informations_financieres",
            "points_forts",
            "opportunite",
            "strategie",
            "equipe_dirigeante",
            "projections",
            "structure_transaction",
            "conditions_financieres",
            "risques",
            "contact"
        ]

    def generer_teaser_complet(self, donnees_entreprise: Dict) -> str:
        """
        Génère un teaser d'investissement complet et professionnel

        Args:
            donnees_entreprise: Données complètes de l'entreprise

        Returns:
            Teaser formaté prêt pour partage
        """
        # Validation des données requises
        self._valider_donnees(donnees_entreprise)

        # Extraction et structuration des données
        financiere = self._extraire_financiere(donnees_entreprise)
        points_forts = self._extraire_points_forts(donnees_entreprise)
        opportune = self._extraire_opportunite(donnees_entreprise)

        # Génération du teaser
        teaser = []

        # Header
        teaser.append(self._generer_header(donnees_entreprise))

        # Résumé exécutif
        teaser.append(self._generer_resume_executif(donnees_entreprise, financiere))

        # Présentation entreprise
        teaser.append(self._generer_presentation_entreprise(donnees_entreprise))

        # Informations financières
        teaser.append(self._generer_infos_financieres(financiere))

        # Points forts
        teaser.append(self._generer_points_forts(points_forts))

        # Opportunité
        teaser.append(self._generer_opportunite(opportune, donnees_entreprise))

        # Stratégie
        teaser.append(self._generer_strategie(donnees_entreprise))

        # Équipe dirigeante
        teaser.append(self._generer_equipe(donnees_entreprise))

        # Projections
        teaser.append(self._generer_projections(donnees_entreprise))

        # Structure transaction
        teaser.append(self._generer_structure_transaction(donnees_entreprise))

        # Conditions financières
        teaser.append(self._generer_conditions_financieres(donnees_entreprise))

        # Risques
        teaser.append(self._generer_risques(donnees_entreprise))

        # Contact
        teaser.append(self._generer_contact(donnees_entreprise))

        return "\n\n".join(teaser)

    def _valider_donnees(self, donnees: Dict):
        """Valide les données requises"""
        champs_obligatoires = [
            'nom_entreprise', 'secteur', 'type_investissement',
            'ca_annuel', 'ebitda', 'equipe_dirigeante'
        ]

        for champ in champs_obligatoires:
            if champ not in donnees:
                raise ValueError(f"Champ obligatoire manquant: {champ}")

    def _extraire_financiere(self, donnees: Dict) -> InformationFinanciere:
        """Extrait les informations financières"""
        return InformationFinanciere(
            ca_annuel=donnees['ca_annuel'],
            ebitda=donnees['ebitda'],
            resultat_net=donnees.get('resultat_net',donnees['ebitda']*0.6),
            croissance_ca=donnees.get('croissance_ca', 0),
            marge_ebitda=donnees['ebitda']/donnees['ca_annuel']*100 if donnees['ca_annuel']>0 else 0,
            endettement_net=donnees.get('endettement_net', 0),
            liquidites=donnees.get('liquidites', 0)
        )

    def _extraire_points_forts(self, donnees: Dict) -> PointsForts:
        """Extrait les points forts de l'entreprise"""
        return PointsForts(
            competitivite=donnees.get('points_forts_competitivite', []),
            equipe=donnees.get('points_forts_equipe', []),
            technologie=donnees.get('points_forts_technologie', []),
            position_marche=donnees.get('points_forts_marche', []),
            strategie=donnees.get('points_forts_strategie', [])
        )

    def _extraire_opportunite(self, donnees: Dict) -> OpportuniteInvestissement:
        """Extrait l'opportunité d'investissement"""
        return OpportuniteInvestissement(
            description=donnees.get('description_opportunite', ""),
            taille_marche=donnees.get('taille_marche', ""),
            croissance=donnees.get('croissance_marche', ""),
            avantage_competitif=donnees.get('avantage_competitif', ""),
            projections=donnees.get('projections_futures', "")
        )

    def _generer_header(self, donnees: Dict) -> str:
        """Génère l'en-tête du teaser"""
        type_invest = TypeInvestissement(donnees['type_investissement'])
        secteur = SecteurActivite(donnees['secteur'])

        header = [
            f"{'='*60}",
            f"TEASER D'INVESTISSEMENT",
            f"{'='*60}",
            f"",
            f"Entreprise : {donnees['nom_entreprise']}",
            f"Secteur : {secteur.value}",
            f"Type d'investissement : {type_invest.value}",
            f"Date : {datetime.date.today().strftime('%d %B %Y')}"
        ]

        return "\n".join(header)

    def _generer_resume_executif(self, donnees: Dict, financiere: InformationFinanciere) -> str:
        """Génère le résumé exécutif"""
        resume = [
            f"{'='*40}",
            f"RÉSUMÉ EXÉCUTIF",
            f"{'='*40}",
            f"",
            f"{donnees['nom_entreprise']} est une entreprise spécialisée dans {donnees['secteur']} avec un chiffre d'affaires annuel de {financiere.ca_annuel:,.0f}€ et une EBITDA de {financiere.ebitda:,.0f}€.",
            f"",
            f"L'entreprise présente une croissance de {financiere.croissance_ca:.1f}% et bénéficie d'une position de marché solide dans un segment dynamique."
        ]

        # Ajout des points clés
        if donnees.get('points_forts_resume'):
            resume.append(f"")
            resume.append(f"Points clés :")
            for point in donnees['points_forts_resume']:
                resume.append(f"• {point}")

        return "\n".join(resume)

    def _generer_presentation_entreprise(self, donnees: Dict) -> str:
        """Génère la présentation de l'entreprise"""
        presentation = [
            f"{'='*40}",
            f"PRÉSENTATION DE L'ENTREPRISE",
            f"{'='*40}",
            f"",
            f"{donnees['description_entreprise']}",
            f"",
            f"Activité principale : {donnees.get('activite_principale', 'Non spécifiée')}",
            f"Année de création : {donnees.get('annee_creation', 'Non spécifiée')}",
            f"Nombre d'employés : {donnees.get('nombre_employes', 0)}",
            f"Répartition géographique : {donnees.get('repartition_geo', 'Non spécifiée')}",
            f"",
            f"Position sur le marché :"
        ]

        # Ajout de la position marché
        position = donnees.get('position_marche_detail', [])
        for item in position:
            presentation.append(f"• {item}")

        return "\n".join(presentation)

    def _generer_infos_financieres(self, financiere: InformationFinanciere) -> str:
        """Génère les informations financières"""
        financier = [
            f"{'='*40}",
            f"INFORMATIONS FINANCIÈRES",
            f"{'='*40}",
            f"",
            f"{'':<20} {'Année N':<12} {'Année N-1':<12} {'Évolution':<10}",
            f"{'-'*60}",
        ]

        # Chiffre d'affaires
        ca_precedent = financiere.ca_annuel / (1 + financiere.croissance_ca/100) if financiere.croissance_ca > 0 else financiere.ca_annuel
        financier.append(f"Chiffre d'affaires  {financiere.ca_annuel:,.0f}€{'':<7} {ca_precedent:,.0f}€{'':<7} {'+'+str(financiere.croissance_ca)+'%':<10}")

        # EBITDA
        ebitda_precedent = financiere.ebitda / (1 + financiere.croissance_ca/100) if financiere.croissance_ca > 0 else financiere.ebitda
        financier.append(f"EBITDA              {financiere.ebitda:,.0f}€{'':<7} {ebitda_precedent:,.0f}€{'':<7} {'+'+str(financiere.croissance_ca)+'%':<10}")

        # Ratios clés
        financier.extend([
            f"{'-'*60}",
            f"EBITDA margin       {financiere.marge_ebitda:.1f}%",
            f"Endettement net    {financiere.endettement_net:,.0f}€",
            f"Trésorerie         {financiere.liquidites:,.0f}€",
            f"Ratio de couverture {financiere.liquidites/max(financiere.endettement_net,1):.2f}x"
        ])

        return "\n".join(financier)

    def _generer_points_forts(self, points_forts: PointsForts) -> str:
        """Génère les points forts de l'entreprise"""
        sections = [
            ("Compétitivité", points_forts.competitivite),
            ("Équipe", points_forts.equipe),
            ("Technologie", points_forts.technologie),
            ("Position marché", points_forts.position_marche),
            ("Stratégie", points_forts.strategie)
        ]

        resultats = []
        titre_section = "{'='*40}"
        sous_titre = f"POINTS FORTS DE L'ENTREPRISE"
        titre_separateur = f"{'='*40}"

        resultats.append(f"{titre_section}")
        resultats.append(f"{sous_titre}")
        resultats.append(f"{titre_separateur}")

        for titre, points in sections:
            if points:
                resultats.append(f"")
                resultats.append(f"{titre}:")
                for point in points:
                    resultats.append(f"• {point}")

        return "\n".join(resultats)

    def _generer_opportunite(self, opportune: OpportuniteInvestissement, donnees: Dict) -> str:
        """Génère l'opportunité d'investissement"""
        opportunite_section = [
            f"{'='*40}",
            f"OPPORTUNITÉ D'INVESTISSEMENT",
            f"{'='*40}",
            f"",
            f"{opportune.description}",
            f"",
            f"Taille du marché : {opportune.taille_marche}",
            f"Croissance marché : {opportune.croissance}",
            f"Avantage compétitif : {opportune.avantage_competitif}",
            f"",
            f"Projections :",
            f"{opportune.projections}"
        ]

        return "\n".join(opportunite_section)

    def _generer_strategie(self, donnees: Dict) -> str:
        """Génère la stratégie de l'entreprise"""
        strategie = [
            f"{'='*40}",
            f"STRATÉGIE DE DÉVELOPPEMENT",
            f"{'='*40}",
            f"",
            f"{donnees.get('strategie_developpement', '')}",
            f"",
            f"Objectifs à 3 ans :"
        ]

        objectifs = donnees.get('objectifs_3_ans', [])
        for objectif in objectifs:
            strategie.append(f"• {objectif}")

        return "\n".join(strategie)

    def _generer_equipe(self, donnees: Dict) -> str:
        """Génère l'équipe dirigeante"""
        equipe = [
            f"{'='*40}",
            f"ÉQUIPE DIRIGEANTE",
            f"{'='*40}",
            f"",
        ]

        membres = donnees.get('equipe_dirigeante', [])
        for membre in membres:
            equipe.append(f"• {membre}")

        return "\n".join(equipe)

    def _generer_projections(self, donnees: Dict) -> str:
        """Génère les projections financières"""
        projections = [
            f"{'='*40}",
            f"PROJECTIONS FINANCIÈRES",
            f"{'='*40}",
            f"",
            f"Prévisions pour les 3 prochaines années :",
            f""
        ]

        # Tableau de projections
        projections.extend([
            f"{'':<20} {'N+1':<12} {'N+2':<12} {'N+3':<12}",
            f"{'-'*55}",
        ])

        projections_chiffres = donnees.get('projections_chiffres', {})
        for annee, valeurs in projections_chiffres.items():
            projections.append(f"{annee:<20} {valeurs['ca']:,.0f}€{'':<5} {valeurs['ebitda']:,.0f}€{'':<5} {valeurs['ca']:,.0f}€{'':<5}")

        return "\n".join(projections)

    def _generer_structure_transaction(self, donnees: Dict) -> str:
        """Génère la structure de la transaction"""
        structure = [
            f"{'='*40}",
            f"STRUCTURE DE LA TRANSACTION",
            f"{'='*40}",
            f"",
            f"Type d'opération : {donnees['type_investissement']}",
            f"",
            f"Modalités :",
        ]

        modalites = donnees.get('modalites_transaction', [])
        for modalite in modalites:
            structure.append(f"• {modalite}")

        # Conditions spécifiques
        if donnees.get('conditions_specifiques'):
            structure.extend([
                f"",
                f"Conditions spécifiques :"
            ])
            for condition in donnees['conditions_specifiques']:
                structure.append(f"• {condition}")

        return "\n".join(structure)

    def _generer_conditions_financieres(self, donnees: Dict) -> str:
        """Génère les conditions financières"""
        conditions = [
            f"{'='*40}",
            f"CONDITIONS FINANCIÈRES",
            f"{'='*40}",
            f"",
        ]

        # Valorisation
        conditions.append(f"Valorisation :")
        conditions.append(f"• Enterprise Value : {donnees.get('ev', 0):,.0f}€")
        conditions.append(f• Equity Value : {donnees.get('equity_value', 0):,.0f}€")

        # Multiples
        conditions.extend([
            f"",
            f"Multiples :"
        ])

        multiples = donnees.get('multiples', {})
        for multiple_type, valeur in multiples.items():
            conditions.append(f"• {multiple_type} : {valeur:.1f}x")

        # Conditions de paiement
        if donnees.get('conditions_paiement'):
            conditions.extend([
                f"",
                f"Conditions de paiement :"
            ])
            for condition in donnees['conditions_paiement']:
                conditions.append(f"• {condition}")

        return "\n".join(conditions)

    def _generer_risques(self, donnees: Dict) -> str:
        """Génère l'analyse des risques"""
        risques = [
            f"{'='*40}",
            f"ANALYSE DES RISQUES",
            f"{'='*40}",
            f"",
            f"L'investissement présente les principaux risques suivants :",
            f""
        ]

        # Risques spécifiques
        risques_spécifiques = donnees.get('risques_specifiques', [])
        for risque in risques_spécifiques:
            risques.append(f"• {risque}")

        # Mesures d'atténuation
        if donnees.get('mesures_attenuation'):
            risques.extend([
                f"",
                f"Mesures d'atténuation :"
            ])
            for mesure in donnees['mesures_attenuation']:
                risques.append(f"• {mesure}")

        return "\n".join(risques)

    def _generer_contact(self, donnees: Dict) -> str:
        """Génère les informations de contact"""
        contact = [
            f"{'='*40}",
            f"INFORMATIONS DE CONTACT",
            f"{'='*40}",
            f"",
            f"Pour toute information complémentaire ou pour accéder à la dataroom,",
            f"mercie de contacter :",
            f"",
            f"Nom : {donnees.get('contact_nom', '')}",
            f"Fonction : {donnees.get('contact_fonction', '')}",
            f"Email : {donnees.get('contact_email', '')}",
            f"Téléphone : {donnees.get('contact_telephone', '')}",
            f"",
            f"Cette information est confidentielle et ne peut être",
            f"divulguée à des tiers sans autorisation préalable."
        ]

        return "\n".join(contact)

def demo_teaser():
    """Démonstration du générateur de teasers"""
    print("DÉMONSTRATION - Générateur de Teasers d'Investissement")
    print("="*60)

    # Données d'exemple
    entreprise_exemple = {
        'nom_entreprise': 'TechInnov SAS',
        'secteur': 'Tech/SaaS',
        'type_investissement': 'Acquisition',
        'ca_annuel': 2500000,
        'ebitda': 450000,
        'resultat_net': 300000,
        'croissance_ca': 25,
        'endettement_net': 200000,
        'liquidites': 50000,
        'description_entreprise': 'TechInnov SAS est un éditeur de logiciels spécialisé dans la gestion de projet collaborative pour les PME technologiques.',
        'activite_principale': 'Développement de SaaS de gestion de projet',
        'annee_creation': 2018,
        'nombre_employes': 25,
        'repartition_geo': 'France 60%, Europe 30%, International 10%',
        'position_marche_detail': [
            'Top 3 sur son segment de spécialisation',
            'Plus de 200 clients actifs',
            'Taux de rétention client > 90%'
        ],
        'points_forts_resume': [
            'Équipe technique expérimentée',
            'Portefeuille clients renouvelé',
            'Modèle SaaS récurrent',
            'Croissance organique forte'
        ],
        'equipe_dirigeante': [
            'Jean Dupont - CEO, 15 ans expérience tech',
            'Marie Martin - CTO, ancien Google',
            'Pierre Bernard - CFO, 10 ans audit financier'
        ],
        'strategie_developpement': 'Expansion en Europe et développement de nouvelles fonctionnalités IA',
        'objectifs_3_ans': [
            'Atteindre 5M€ de CA',
            'Doubler la base clients',
            'Internationaliser la marque'
        ],
        'projections_chiffres': {
            'N+1': {'ca': 3100000, 'ebitda': 550000},
            'N+2': {'ca': 3875000, 'ebitda': 680000},
            'N+3': {'ca': 4500000, 'ebitda': 810000}
        },
        'modalites_transaction': [
            'Acquisition 100% des titres',
            'Prix en fonction des performances futures',
            'Période de transition de 6 mois'
        ],
        'conditions_specifiques': [
            'Garantie de chiffre d\'affaires',
            'Clause de non-concurrence',
            'Maintien de l\'équipe dirigeante'
        ],
        'ev': 6750000,
        'equity_value': 6500000,
        'multiples': {
            'EV/CA': 2.7x,
            'EV/EBITDA': 15.0x,
            'CAPEX/EBITDA': 2.2x
        },
        'conditions_paiement': [
            '40% à la signature',
            '40% à 6 mois',
            '20% à 12 mois'
        ],
        'risques_specifiques': [
            'Concurrence accrue sur le marché',
            'Dépendance technologique',
            'Risques réglementaires'
        ],
        'mesures_attenuation': [
            'Investissement continue en R&D',
            'Diversification du portefeuille',
            'Veille réglementaire active'
        ],
        'contact_nom': 'Paul Roulleau',
        'contact_fonction': 'Managing Partner',
        'contact_email': 'paul@brantham.fr',
        'contact_telephone': '+33 1 23 45 67 89'
    }

    # Créer et générer le teaser
    generateur = GenerateurTeasers()
    teaser = generateur.generer_teaser_complet(entreprise_exemple)

    # Afficher le teaser
    print(teaser)

    return teaser

if __name__ == "__main__":
    demo_teaser()