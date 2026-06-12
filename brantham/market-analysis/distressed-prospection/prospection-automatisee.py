#!/usr/bin/env python3
"""
Pipeline de prospection automatisée M&A distressed
Intégration complète de tous les composants
"""

import sys
import os
import json
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import pandas as pd

# Importer les modules locaux
from data_sources import DataSources
from scoring_distressed import ScoringDistressed
from matching_acheteurs import MatchingAcheteurs
from legal_constraints_l642 import LegalConstraintsL642
from relance_automatisee import RelanceAutomatisee
from dashboard_prospection import RelanceTracker

class ProspectionAutomatiseeMandA:
    """Pipeline complet de prospection M&A distressed"""

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.setup_logging()

        # Initialiser tous les composants
        self.data_sources = DataSources()
        self.scoring = ScoringDistressed()
        self.matching = MatchingAcheteurs()
        self.legal = LegalConstraintsL642()
        self.relances = RelanceAutomatisee()
        self.tracker = RelanceTracker()

        # Configuration
        self.config = {
            'jours_piste': 7,
            'taille_min_ca': 500000,
            'taille_max_ca': 10000000,
            'secteurs_cibles': ['62.01', '63.11', '69.10', '68.20'],
            'nb_relances_max': 4,
            'delai_reponse_jours': 14
        }

    def setup_logging(self):
        """Configuration du logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('prospection_mandA.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )

    def run_pipeline(self, mode: str = 'complet') -> Dict:
        """
        Exécuter le pipeline de prospection

        Args:
            mode: 'complet' ou 'seul_piste' ou 'seul_relances'

        Returns:
            Rapport d'exécution
        """
        self.logger.info(f"Démarrage du pipeline en mode {mode}")
        rapport = {'timestamp': datetime.now(), 'mode': mode, 'etapes': {}}

        try:
            # Phase 1: Intelligence (J-3 à J-1)
            if mode in ['complet', 'seul_piste']:
                rapport['etapes']['intelligence'] = self.phase_intelligence()

            # Phase 2: Activation (J0 à J+3)
            if mode in ['complet', 'seul_piste']:
                rapport['etapes']['activation'] = self.phase_activation()

            # Phase 3: Exécution (J+3 à J+14)
            if mode in ['complet', 'seul_relances']:
                rapport['etapes']['execution'] = self.phase_execution()

            # Phase 4: Reporting
            rapport['etapes']['reporting'] = self.phase_reporting()

            rapport['succes'] = True

        except Exception as e:
            self.logger.error(f"Erreur dans le pipeline: {str(e)}")
            rapport['succes'] = False
            rapport['erreur'] = str(e)

        self.logger.info("Pipeline terminé")
        return rapport

    def phase_intelligence(self) -> Dict:
        """Phase 1: Intelligence - Scanning et qualification"""
        self.logger.info("Phase Intelligence: Scanning des données")

        # Scan BODACC des liquidations judiciaires
        liquidations = self.data_sources.scan_bodacc_liquidations(
            jours=self.config['jours_piste']
        )

        # Filtrage et scoring
        prospects_qualifies = []
        stats = {'total_scan': len(liquidations), 'qualifies': 0, 'rejete': 0}

        for deal in liquidations:
            # Critères de base
            if self._respecte_critères_de_base(deal):
                # Calcul du score
                score_details = self.scoring.score_global(deal)

                if score_details['score_global'] >= 60:  # Seuil de qualité
                    deal.update(score_details)
                    prospects_qualifies.append(deal)
                    stats['qualifies'] += 1
                else:
                    stats['rejete'] += 1
            else:
                stats['rejete'] += 1

        # Ajouter au tracker
        prospects_ajoutes = []
        for prospect in prospects_qualifies:
            prospect_id = self.tracker.ajouter_prospect(prospect)
            prospects_ajoutes.append(prospect_id)

        # Générer rapports
        rapport_intel = {
            'prospects_qualifies': len(prospects_qualifies),
            'prospects_ajoutes': len(prospects_ajoutes),
            'conversion_qualification': stats['qualifies'] / stats['total_scan'] * 100,
            'liste_prospects': prospects_ajoutes,
            'meilleurs_scores': sorted(prospects_qualifies,
                                    key=lambda x: x['score_global'],
                                    reverse=True)[:5]
        }

        self.logger.info(f"Phase Intelligence terminée: {len(prospects_ajoutes)} prospects qualifiés")
        return rapport_intel

    def phase_activation(self) -> Dict:
        """Phase 2: Activation - Premier contact et scoring acheteurs"""
        self.logger.info("Phase Activation: Activation des prospects")

        prospects = self.tracker.prospects
        stats = {'total': len(prospects), 'contacts': 0, 'echec': 0}

        for prospect in prospects:
            if prospect['statut'] == 0:  # Non encore contacté
                try:
                    # Générer séquence de relances
                    sequence = self.relances.generer_sequence(prospect)

                    # Enregistrer la première relance
                    premier_contact = sequence['vue_pas_reponse'][0]
                    self.tracker.enregistrer_relance(
                        prospect['id'],
                        premier_contact['mode'],
                        premier_contact['contenu']
                    )

                    stats['contacts'] += 1

                except Exception as e:
                    self.logger.error(f"Erreur contact prospect {prospect['id']}: {str(e)}")
                    stats['echec'] += 1

        # Calculer scoring acheteurs
        segments = self.matching.acheteurs['segments']
        scoring_segments = {}

        for segment in segments:
            score = self.matching.calculer_matching(segment, prospects)
            scoring_segments[segment] = score

        rapport_activ = {
            'prospects_contacts': stats['contacts'],
            'taux_activation': stats['contacts'] / stats['total'] * 100,
            'scoring_segments': scoring_segments,
            'segment_prio': max(scoring_segments, key=scoring_segments.get)
        }

        self.logger.info(f"Phase Activation terminée: {stats['contacts']}/{stats['total']} contacts")
        return rapport_activ

    def phase_execution(self) -> Dict:
        """Phase 3: Exécution - Relances et monitoring"""
        self.logger.info("Phase Exécution: Monitoring et relances")

        date_limite = datetime.now()
        stats = {'relances': 0, 'reponses': 0, 'conversions': 0}

        # Vérifier et envoyer relances planifiées
        for prospect_id, calendrier in self.tracker.calendrier_relances.items():
            for relance in calendrier:
                if (relance['date'] <= date_limite and
                    relance['date'] > date_limite - timedelta(days=1)):

                    try:
                        prospect = self.tracker._get_prospect(prospect_id)
                        if prospect and prospect['statut'] < 4:  # Pas encore closed
                            # Générer contenu personnalisé
                            contenu = self.relances.generer_contenu(
                                prospect,
                                relance['type'],
                                relance['mode']
                            )

                            # Envoyer relance
                            self.tracker.enregistrer_relance(
                                prospect_id,
                                relance['mode'],
                                contenu,
                                relance['date']
                            )

                            stats['relances'] += 1

                    except Exception as e:
                        self.logger.error(f"Erreur relance {prospect_id}: {str(e)}")

        # Traiter les réponses récentes
        recentes = [r for r in self.tracker.reponses
                   if r['date_reponse'] > date_limite - timedelta(days=7)
                   and not r['traitee']]

        for reponse in recentes:
            try:
                prospect = self.tracker._get_prospect(reponse['prospect_id'])
                if prospect:
                    # Mettre à jour statut
                    self.tracker.enregistrer_reponse(
                        reponse['prospect_id'],
                        reponse['type_reponse'],
                        reponse['contenu'],
                        reponse['date_reponse']
                    )

                    reponse['traitee'] = True
                    reponse['date_traitement'] = datetime.now()

                    if reponse['type_reponse'] == 'positive':
                        stats['conversions'] += 1
                    stats['reponses'] += 1

            except Exception as e:
                self.logger.error(f"Erreur traitement réponse {reponse['id']}: {str(e)}")

        # Générer offres légales pour prospects intéressés
        offres_generees = 0
        for prospect in self.tracker.prospects:
            if prospect['statut'] == 2:  # Interessé
                try:
                    offre = self.legal.generer_offre_legale(prospect)
                    if offre:
                        offres_generees += 1
                except Exception as e:
                    self.logger.error(f"Erreur génération offre {prospect['id']}: {str(e)}")

        rapport_exec = {
            'relances_envoyees': stats['relances'],
            'reponses_traitees': stats['reponses'],
            'conversions': stats['conversions'],
            'offres_generees': offres_generees,
            'taux_conversion': stats['conversions'] / len(self.tracker.prospects) * 100
        }

        self.logger.info(f"Phase Exécution terminée: {stats['reponses']} réponses traitées")
        return rapport_exec

    def phase_reporting(self) -> Dict:
        """Phase 4: Reporting et alertes"""
        self.logger.info("Phase Reporting: Génération des rapports")

        # Générer rapports
        report_text = self.tracker.generer_report('text')
        report_json = self.tracker.generer_report('json')

        # Stocker les rapports
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        with open(f'rapport_prospection_{timestamp}.txt', 'w', encoding='utf-8') as f:
            f.write(report_text)

        with open(f'rapport_prospection_{timestamp}.json', 'w', encoding='utf-8') as f:
            f.write(report_json)

        # Envoyer alertes
        config_email = {
            'smtp_server': 'smtp.gmail.com',
            'smtp_port': 587,
            'smtp_username': os.getenv('EMAIL_USER'),
            'smtp_password': os.getenv('EMAIL_PASS'),
            'email_from': 'prosp@mandistressed.fr',
            'email_to': 'equipe@mandistressed.fr'
        }

        if config_email['smtp_username']:
            try:
                self.tracker.envoyer_alertes(config_email)
            except Exception as e:
                self.logger.warning(f"Alertes email non envoyées: {str(e)}")

        rapport_report = {
            'timestamp': timestamp,
            'rapports_generees': 2,
            'alertes_envoyees': 1 if config_email['smtp_username'] else 0,
            'prospect_actifs': len([p for p in self.tracker.prospects
                                  if p['statut'] >= 1 and p['statut'] <= 3])
        }

        self.logger.info("Phase Reporting terminée")
        return rapport_report

    def _respecte_critères_de_base(self, deal: Dict) -> bool:
        """Vérifier si le deal respecte les critères de base"""
        # Critère de taille (CA)
        ca = deal.get('chiffre_affaires', 0)
        if not (self.config['taille_min_ca'] <= ca <= self.config['taille_max_ca']):
            return False

        # Critère sectoriel
        secteur = deal.get('code_naf', '')
        if secteur not in self.config['secteurs_cibles']:
            return False

        # Critère de procédure collective
        if not deal.get('procedure_collective'):
            return False

        return True

    def exporter_csv(self, filepath: str):
        """Exporter les prospects en CSV"""
        prospects = self.tracker.prospects
        if not prospects:
            return

        df = pd.DataFrame(prospects)
        df.to_csv(filepath, index=False, encoding='utf-8')

    def export_automatique(self):
        """Export automatique des données"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        # Export CSV
        csv_path = f'prospects_distressed_{timestamp}.csv'
        self.exporter_csv(csv_path)

        # Export JSON complet
        rapport = self.run_pipeline('complet')
        json_path = f'pipeline_rapport_{timestamp}.json'
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(rapport, f, indent=2, default=str, ensure_ascii=False)

        return {
            'csv_export': csv_path,
            'json_export': json_path,
            'timestamp': timestamp
        }


def demo_complet():
    """Démonstration du pipeline complet"""
    print("=" * 60)
    print("DÉMONSTRATION - Prospection Automatisée M&A Distressed")
    print("=" * 60)

    pipeline = ProspectionAutomatiseeMandA()

    # Exécuter le pipeline
    rapport = pipeline.run_pipeline()

    # Afficher les résultats
    print(f"\n📊 RÉSULTATS COMPLETS:")
    print(f"   Succès: {rapport['succes']}")

    if rapport['succes']:
        etapes = rapport['etapes']

        if 'intelligence' in etapes:
            intel = etapes['intelligence']
            print(f"\n   🎯 Intelligence:")
            print(f"      Prospects qualifiés: {intel['prospects_qualifies']}")
            print(f"      Taux conversion: {intel['conversion_qualification']:.1f}%")

        if 'activation' in etapes:
            activ = etapes['activation']
            print(f"\n   🚀 Activation:")
            print(f"      Prospects contactés: {activ['prospects_contacts']}")
            print(f"      Segment prioritaire: {activ['segment_prio']}")

        if 'execution' in etapes:
            exec = etapes['execution']
            print(f"\n   ⚡ Exécution:")
            print(f"      Relances envoyées: {exec['relances_envoyees']}")
            print(f"      Réponses traitées: {exec['reponses_traitees']}")
            print(f"      Conversions: {exec['conversions']}")

    if rapport['erreur']:
        print(f"\n❌ ERREUR: {rapport['erreur']}")


if __name__ == "__main__":
    demo_complet()