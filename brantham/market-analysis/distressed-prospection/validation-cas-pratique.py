#!/usr/bin/env python3
"""
Validation du playbook de prospection automatisée M&A distressed
Cas pratique simulé avec données réalistes
"""

import json
import datetime
from typing import Dict, List
import pandas as pd

from prospection_automatisee import ProspectionAutomatiseeMandA
from data_sources import DataSources
from scoring_distressed import ScoringDistressed
from matching_achateurs import MatchingAcheteurs

class ValidationPlaybook:
    """Validation complète du playbook avec cas pratique"""

    def __init__(self):
        self.pipeline = ProspectionAutomatiseeMandA()
        self.cas_test_realiste = self.creer_cas_test_realiste()

    def creer_cas_test_realiste(self) -> List[Dict]:
        """Créer un cas de test réaliste basé sur données récentes"""
        return [
            {
                'entreprise_nom': 'CyberSecureTech',
                'siren': '123456789',
                'code_naf': '62.01',
                'chiffre_affaires': 3500000,
                'resultat': -120000,
                'procedure_collective': True,
                'date_creation': '2019-03-15',
                'effectif': 25,
                'secteur': 'Cybersécurité',
                'urgency': 'high'
            },
            {
                'entreprise_nom': 'DataVision Analytics',
                'siren': '987654321',
                'code_naf': '63.11',
                'chiffre_affaires': 8500000,
                'resultat': -250000,
                'procedure_collective': True,
                'date_creation': '2018-07-22',
                'effectif': 42,
                'secteur': 'Consulting Data',
                'urgency': 'medium'
            },
            {
                'entreprise_nom': 'Engineering Solutions',
                'siren': '456789123',
                'code_naf': '69.10',
                'chiffre_affaires': 12000000,
                'resultat': -400000,
                'procedure_collective': True,
                'date_creation': '2016-01-10',
                'effectif': 78,
                'secteur': 'Ingénierie logicielle',
                'urgency': 'high'
            },
            {
                'entreprise_nom': 'Digital Marketing Pro',
                'siren': '789123456',
                'code_naf': '63.12',
                'chiffre_affaires': 2000000,
                'resultat': -80000,
                'procedure_collective': True,
                'date_creation': '2020-05-08',
                'effectif': 15,
                'secteur': 'Marketing digital',
                'urgency': 'low'
            },
            {
                'entreprise_nom': 'Cloud Infrastructure Co',
                'siren': '321654987',
                'code_naf': '62.09',
                'chiffre_affaires': 18000000,
                'resultat': -600000,
                'procedure_collective': True,
                'date_creation': '2017-11-30',
                'effectif': 95,
                'secteur': 'Infrastructure cloud',
                'urgency': 'high'
            }
        ]

    def valider_scoring(self) -> Dict:
        """Valider le système de scoring"""
        print("🧪 Validation du système de scoring...")

        scoring = ScoringDistressed()
        resultats = []

        for deal in self.cas_test_realiste:
            score = scoring.score_global(deal)
            resultats.append({
                'entreprise': deal['entreprise_nom'],
                'score_total': score['score_global'],
                'details': score,
                'validation': 'PASS' if score['score_global'] >= 60 else 'FAIL'
            })

        # Vérifier les scores attendus
        scores_attendus = {
            'CyberSecureTech': 85,
            'DataVision Analytics': 80,
            'Engineering Solutions': 75,
            'Digital Marketing Pro': 70,
            'Cloud Infrastructure Co': 78
        }

        validation_ok = True
        for resultat in resultats:
            entreprise = resultat['entreprise']
            score_attendu = scores_attendus[entreprise]
            score_reel = resultat['score_total']

            # Marge d'erreur tolérée: ±15 points
            if abs(score_reel - score_attendu) > 15:
                validation_ok = False
                print(f"  ❌ {entreprise}: Score {score_reel} attendu {score_attendu}")
            else:
                print(f"  ✅ {entreprise}: Score {score_reel} (attendu {score_attendu})")

        return {
            'test': 'scoring',
            'succes': validation_ok,
            'resultats': resultats
        }

    def valider_matching(self) -> Dict:
        """Valider le système de matching acheteurs"""
        print("🧪 Validation du système de matching...")

        matching = MatchingAcheteurs()
        prospects_scoring = []

        for deal in self.cas_test_realiste:
            score = scoring.score_global(deal)
            deal.update(score)
            prospects_scoring.append(deal)

        resultats = {}

        for segment in ['fonds_investissement', 'strategique', 'family_office']:
            score_segment = matching.calculer_matching(segment, prospects_scoring)
            resultats[segment] = {
                'score': score_segment,
                'validation': 'PASS' if score_segment >= 60 else 'FAIL'
            }
            print(f"  🎯 {segment}: Score {score_segment:.1f}")

        # Vérifier que les scores sont cohérents
        validation_ok = all(r['score'] >= 50 for r in resultats.values())

        return {
            'test': 'matching',
            'succes': validation_ok,
            'resultats': resultats
        }

    def valider_pipeline_complet(self) -> Dict:
        """Valider l'exécution complète du pipeline"""
        print("🧪 Validation du pipeline complet...")

        # Initialiser avec nos données de test
        self.pipeline.tracker.prospects = []
        self.pipeline.tracker.relances = []
        self.pipeline.tracker.reponses = []

        # Ajouter nos prospects
        for deal in self.cas_test_realiste:
            self.pipeline.tracker.ajouter_prospect(deal)

        print(f"  ✅ {len(self.cas_test_realiste)} prospects ajoutés")

        # Simuler des relances
        for prospect in self.pipeline.tracker.prospects:
            if prospect['id'] <= 3:  # Premier contact pour 3 prospects
                self.pipeline.tracker.enregistrer_relance(
                    prospect['id'],
                    'email',
                    f"Relance initiale pour {prospect['nom_entreprise']}"
                )

        print(f"  ✅ 3 relances initiales enregistrées")

        # Simuler des réponses
        reponses_test = [
            (1, 'positive', "Nous sommes intéressés par votre proposition"),
            (2, 'demande_info', "Pourriez-vous nous envoyer plus de détails sur le processus ?"),
            (3, 'negative', "Merci, mais nous ne sommes pas intéressés à ce moment")
        ]

        for prospect_id, reponse_type, contenu in reponses_test:
            self.pipeline.tracker.enregistrer_reponse(prospect_id, reponse_type, contenu)

        print(f"  ✅ 3 réponses simulées")

        # Vérifier les statuts
        statuts = self.pipeline.tracker._stats_statuts()
        statuts_attendus = {'new': 2, 'contacted': 3, 'interested': 1, 'closed_lost': 1}

        validation_ok = True
        for statut, count in statuts_attendus.items():
            if statuts.get(statut, 0) != count:
                validation_ok = False
                print(f"  ❌ Statut {statut}: attendu {count}, obtenu {statuts.get(statut, 0)}")
            else:
                print(f"  ✅ Statut {statut}: {count}")

        # Générer rapport
        rapport_texte = self.pipeline.tracker.generer_report('text')
        rapport_json = self.pipeline.tracker.generer_report('json')

        # Vérifier que les rapports contiennent les bonnes infos
        validation_rapport = (
            'total_prospects' in rapport_json and
            'taux_reponse' in rapport_json['kpis'] and
            len(self.pipeline.tracker.prospects) == 5
        )

        print(f"  {'✅' if validation_rapport else '❌'} Rapports générés avec succès")

        return {
            'test': 'pipeline_complet',
            'succes': validation_ok and validation_rapport,
            'statuts': statuts,
            'rapport': rapport_texte.split('\n')[5:15]  # Lignes pertinentes
        }

    def valider_contraintes_legales(self) -> Dict:
        """Valider le respect des contraintes légales"""
        print("🧪 Validation des contraintes légales...")

        legal = LegalConstraintsL642()
        resultats = []

        for deal in self.cas_test_realiste:
            eligible = legal.verifier_eligibilite_repreneur(deal)
            offre = legal.generer_offre_legale(deal) if eligible else None

            resultats.append({
                'entreprise': deal['entreprise_nom'],
                'eligible': eligible,
                'offre_generee': offre is not None,
                'validation': 'PASS' if eligible else 'FAIL'
            })

            print(f"  {'✅' if eligible else '❌'} {deal['entreprise_nom']}: {'Éligible' if eligible else 'Non éligible'}")

        validation_ok = all(r['eligible'] for r in resultats)

        return {
            'test': 'contraintes_legales',
            'succes': validation_ok,
            'resultats': resultats
        }

    def generer_rapport_validation_complet(self) -> Dict:
        """Générer le rapport de validation complet"""
        print("\n📊 Génération du rapport de validation...")

        # Exécuter tous les tests
        tests = [
            self.valider_scoring(),
            self.valider_matching(),
            self.valider_pipeline_complet(),
            self.valider_contraintes_legales()
        ]

        # Calculer le score global
        tests_passes = sum(1 for test in tests if test['succes'])
        score_global = tests_passes / len(tests) * 100

        # Préparer le rapport
        rapport = {
            'date_validation': datetime.datetime.now().isoformat(),
            'score_global': score_global,
            'status': 'VALIDE' if score_global >= 80 else 'A AMELIORER',
            'tests': tests,
            'recommandations': self.generer_recommandations(tests),
            'cas_test': {
                'nombre_entreprises': len(self.cas_test_realiste),
                'secteurs_couverts': list(set(d['code_naf'] for d in self.cas_test_realiste)),
                'ca_range': [min(d['chiffre_affaires'] for d in self.cas_test_realiste),
                           max(d['chiffre_affaires'] for d in self.cas_test_realiste)]
            }
        }

        # Sauvegarder le rapport
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        with open(f'validation_playbook_{timestamp}.json', 'w', encoding='utf-8') as f:
            json.dump(rapport, f, indent=2, default=str, ensure_ascii=False)

        print(f"  ✅ Rapport sauvegardé: validation_playbook_{timestamp}.json")

        return rapport

    def generer_recommandations(self, tests: List[Dict]) -> List[str]:
        """Générer des recommandations basées sur les résultats"""
        recommandations = []

        for test in tests:
            if not test['succes']:
                if test['test'] == 'scoring':
                    recommandations.append("Ajuster les pondérations du scoring pour mieux correspondre au marché réel")
                elif test['test'] == 'matching':
                    recommandations.append("Affiner les critères de segmentation des acheteurs")
                elif test['test'] == 'pipeline_complet':
                    recommandations.append("Optimiser les séquences de relances pour améliorer les taux de réponse")
                elif test['test'] == 'contraintes_legales':
                    recommandations.append("Mettre à jour la base de données juridiques avec les dernières réglementations")

        if not recommandations:
            recommandations = [
                "Le playbook est prêt à être déployé en production",
                "Considérer d'ajouter des indicateurs supplémentaires",
                "Mettre en place un monitoring continu de la performance"
            ]

        return recommandations

    def afficher_rapport_final(self, rapport: Dict):
        """Afficher un rapport final lisible"""
        print("\n" + "="*60)
        print("RAPPORT DE VALIDATION - PLAYBOOK PROSPECTION M&A")
        print("="*60)

        print(f"\n📊 Score Global: {rapport['score_global']:.1f}/100")
        print(f"   Statut: {rapport['status']}")

        print(f"\n🧪 Résultats par test:")
        for test in rapport['tests']:
            print(f"   {test['test'].replace('_', ' ').title()}: {'✅ PASS' if test['succes'] else '❌ FAIL'}")

        print(f"\n💡 Recommandations:")
        for rec in rapport['recommandations']:
            print(f"   • {rec}")

        print(f"\n📈 Cas de test:")
        print(f"   Entreprises testées: {rapport['cas_test']['nombre_entreprises']}")
        print(f"   Secteurs: {', '.join(rapport['cas_test']['secteurs_couverts'])}")
        print(f"   CA: {rapport['cas_test']['ca_range'][0]:,}€ - {rapport['cas_test']['ca_range'][1]:,}€")

        print("\n" + "="*60)


def main():
    """Exécution de la validation complète"""
    print("🚀 DÉMARRAGE DE LA VALIDATION COMPLÈTE")
    print("="*60)

    validation = ValidationPlaybook()

    # Exécuter la validation complète
    rapport = validation.generer_rapport_validation_complet()

    # Afficher les résultats
    validation.afficher_rapport_final(rapport)

    # Retourner le code de sortie
    if rapport['score_global'] >= 80:
        print("\n✅ PLAYBOOK VALIDÉ POUR PRODUCTION")
        return 0
    else:
        print("\n⚠️  PLAYBOOK À AMÉLIORER AVANT PRODUCTION")
        return 1


if __name__ == "__main__":
    exit(main())