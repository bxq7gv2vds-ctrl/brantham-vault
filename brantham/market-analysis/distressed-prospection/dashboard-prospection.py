#!/usr/bin/env python3
"""
Dashboard de suivi des prospects M&A distressed
- Tracking des relances multi-canal
- Reporting temps réel
- Alertes automatisées
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import json
import smtplib
from email.mime.text import MIMEText
import logging

class RelanceTracker:
    """Système de tracking et reporting des prospects"""

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # Data storage
        self.prospects = []
        self.relances = []
        self.reponses = []
        self.calendrier_relances = {}

        # Configuration
        self.statuts = {
            'new': 0,        # Nouveau prospect
            'contacted': 1,  # Contacté
            'interested': 2, # Intéressé
            'proposal': 3,   # Proposition envoyée
            'closed_won': 4, # Deal gagné
            'closed_lost': 5 # Deal perdu
        }

        self.modes_contact = ['linkedin', 'email', 'telephone', 'sms']

    def ajouter_prospect(self, deal_data: Dict, source: str = 'bodacc'):
        """Ajouter un nouveau prospect au tracking"""
        prospect = {
            'id': len(self.prospects) + 1,
            'nom_entreprise': deal_data.get('entreprise_nom', ''),
            'siren': deal_data.get('siren', ''),
            'secteur': deal_data.get('code_naf', ''),
            'taille_ca': deal_data.get('chiffre_affaires', 0),
            'statut': self.statuts['new'],
            'date_ajout': datetime.now(),
            'source': source,
            'score_distressed': self._calculer_score_initial(deal_data),
            'segments_cibles': self._identifier_segments(deal_data)
        }

        self.prospects.append(prospect)
        self.calendrier_relances[prospect['id']] = self._generer_calendrier_relances()

        self.logger.info(f"Nouveau prospect ajouté: {prospect['nom_entreprise']}")
        return prospect['id']

    def enregistrer_relance(self, prospect_id: int, mode: str, contenu: str,
                          date_envoi: datetime = None) -> bool:
        """Enregistrer une relance effectuée"""
        if mode not in self.modes_contact:
            self.logger.error(f"Mode de contact invalide: {mode}")
            return False

        if date_envoi is None:
            date_envoi = datetime.now()

        relance = {
            'id': len(self.relances) + 1,
            'prospect_id': prospect_id,
            'mode_contact': mode,
            'contenu': contenu,
            'date_envoi': date_envoi,
            'statut': 'envoyee',
            'response_rate': None
        }

        self.relances.append(relance)

        # Mettre à jour le statut du prospect
        prospect = self._get_prospect(prospect_id)
        if prospect:
            prospect['statut'] = self.statuts['contacted']

        self.logger.info(f"Relance enregistrée pour prospect {prospect_id} via {mode}")
        return True

    def enregistrer_reponse(self, prospect_id: int, type_reponse: str,
                          contenu: str, date_reponse: datetime = None) -> bool:
        """Enregistrer une réponse du prospect"""
        if date_reponse is None:
            date_reponse = datetime.now()

        reponse = {
            'id': len(self.reponses) + 1,
            'prospect_id': prospect_id,
            'type_reponse': type_reponse,  # positive, negative, demande_info
            'contenu': contenu,
            'date_reponse': date_reponse,
            'traitee': False,
            'date_traitement': None
        }

        self.reponses.append(reponse)

        # Mettre à jour le statut du prospect
        self._maj_statut_prospect(prospect_id, type_reponse)

        self.logger.info(f"Réponse enregistrée pour prospect {prospect_id}: {type_reponse}")
        return True

    def _calculer_score_initial(self, deal_data: Dict) -> float:
        """Calculer un score initial de qualité du prospect"""
        score = 0

        # Score sectoriel
        secteurs_prio = ['62.01', '63.11', '69.10', '68.20']  # IT, consulting, ingénierie
        if deal_data.get('code_naf') in secteurs_prio:
            score += 25

        # Score taille (CA optimal: 500K-10M€)
        ca = deal_data.get('chiffre_affaires', 0)
        if 500000 <= ca <= 10000000:
            score += 20
        elif ca > 10000000:
            score += 15

        # Score rentabilité
        if deal_data.get('resultat') and deal_data.get('resultat') < 0:
            score += 25

        # Score urgence (procédure collective récente)
        if deal_data.get('procedure_collective'):
            score += 20

        # Score risques
        if deal_data.get('entreprise_cessee'):
            score -= 10

        return min(100, max(0, score))

    def _identifier_segments(self, deal_data: Dict) -> List[str]:
        """Identifier les segments d'acheteurs pertinents"""
        segments = []

        secteur = deal_data.get('code_naf', '')

        # Segments par secteur
        if secteur in ['62.01', '63.11']:  # IT, consulting
            segments.extend(['strategique', 'fonds_investissement'])
        elif secteur in ['69.10']:  # Ingénierie
            segments.extend(['strategique', 'family_office'])

        # Segments par taille
        ca = deal_data.get('chiffre_affaires', 0)
        if ca > 5000000:
            segments.append('fonds_investissement')
        else:
            segments.append('family_office')

        return list(set(segments))

    def _generer_calendrier_relances(self) -> List[Dict]:
        """Générer un calendrier de relances optimisé"""
        calendrier = []
        base_date = datetime.now()

        # Vue pas de réponse (J+1, J+3, J+7, J+14)
        calendrier.append({
            'type': 'vue_pas_reponse',
            'date': base_date + timedelta(days=1),
            'mode': 'email'
        })
        calendrier.append({
            'type': 'vue_pas_reponse',
            'date': base_date + timedelta(days=3),
            'mode': 'linkedin'
        })
        calendrier.append({
            'type': 'vue_pas_reponse',
            'date': base_date + timedelta(days=7),
            'mode': 'telephone'
        })

        # Vue réponse positive
        calendrier.append({
            'type': 'reponse_pos',
            'date': base_date + timedelta(days=2),
            'mode': 'email'
        })
        calendrier.append({
            'type': 'reponse_pos',
            'date': base_date + timedelta(days=5),
            'mode': 'telephone'
        })

        return calendrier

    def _get_prospect(self, prospect_id: int) -> Optional[Dict]:
        """Récupérer un prospect par ID"""
        for prospect in self.prospects:
            if prospect['id'] == prospect_id:
                return prospect
        return None

    def _maj_statut_prospect(self, prospect_id: int, type_reponse: str):
        """Mettre à jour le statut du prospect selon la réponse"""
        prospect = self._get_prospect(prospect_id)
        if not prospect:
            return

        if type_reponse == 'positive':
            prospect['statut'] = self.statuts['interested']
        elif type_reponse == 'negative':
            prospect['statut'] = self.statuts['closed_lost']
        elif type_reponse == 'demande_info':
            prospect['statut'] = self.statuts['proposal']

    def generer_report(self, format_sortie: str = 'json') -> str:
        """Générer un rapport de performance"""
        # Calcul des KPIs
        total_prospects = len(self.prospects)
        prospects_contacts = [p for p in self.prospects if p['statut'] >= 1]
        prospects_interesses = [p for p in self.prospects if p['statut'] >= 2]

        total_relances = len(self.relances)
        relances_reponses = [r for r in self.reponses if r['type_reponse'] == 'positive']

        # Taux de réponse
        taux_reponse = (len(relances_reponses) / total_relances * 100) if total_relances > 0 else 0

        # Temps moyen
        if prospects_interesses:
            temps_moyen = np.mean([
                (p['date_ajout'] - datetime.now()).days
                for p in prospects_interesses
            ])
        else:
            temps_moyen = 0

        # Score moyen
        if total_prospects > 0:
            score_moyen = np.mean([p['score_distressed'] for p in self.prospects])
        else:
            score_moyen = 0

        report_data = {
            'kpis': {
                'total_prospects': total_prospects,
                'prospects_contacts': len(prospects_contacts),
                'prospects_interesses': len(prospects_interesses),
                'total_relances': total_relances,
                'taux_reponse': round(taux_reponse, 2),
                'temps_moyen_jours': round(temps_moyen, 1),
                'score_moyen': round(score_moyen, 1)
            },
            'segments': self._stats_segments(),
            'statuts': self._stats_statuts(),
            'evolution': self._evolution_recente(),
            'relances_prevues': self._relances_prevues()
        }

        if format_sortie == 'json':
            return json.dumps(report_data, indent=2, default=str)
        elif format_sortie == 'csv':
            df = pd.DataFrame(report_data['kpis'], index=[0])
            return df.to_csv(index=False)
        else:
            return self._format_report_text(report_data)

    def _stats_segments(self) -> Dict[str, int]:
        """Statistiques par segment cible"""
        segments = {}
        for prospect in self.prospects:
            for segment in prospect.get('segments_cibles', []):
                segments[segment] = segments.get(segment, 0) + 1
        return segments

    def _stats_statuts(self) -> Dict[str, int]:
        """Statistiques par statut"""
        statuts = {}
        for prospect in self.prospects:
            statut_name = [k for k, v in self.statuts.items() if v == prospect['statut']][0]
            statuts[statut_name] = statuts.get(statut_name, 0) + 1
        return statuts

    def _evolution_recente(self) -> Dict[str, int]:
        """Évolution récente (7 jours)"""
        date_limite = datetime.now() - timedelta(days=7)

        nouveaux = len([p for p in self.prospects if p['date_ajout'] >= date_limite])
        interesses = len([p for p in self.prospects
                         if p['statut'] >= 2 and p['date_ajout'] >= date_limite])

        return {
            'nouveaux_7j': nouveaux,
            'interesses_7j': interesses
        }

    def _relances_prevues(self) -> List[Dict]:
        """Relances prévies dans les 7 prochains jours"""
        date_limite = datetime.now() + timedelta(days=7)

        prevues = []
        for prospect_id, calendrier in self.calendrier_relances.items():
            for relance in calendrier:
                if relance['date'] <= date_limite:
                    prevues.append({
                        'prospect_id': prospect_id,
                        'type': relance['type'],
                        'date': relance['date'].strftime('%Y-%m-%d'),
                        'mode': relance['mode']
                    })

        return sorted(prevues, key=lambda x: x['date'])[:10]

    def _format_report_text(self, report_data: Dict) -> str:
        """Formatter le rapport en texte lisible"""
        text = []
        text.append("=" * 60)
        text.append("DASHBOARD - Suivi Prospection M&A Distressed")
        text.append("=" * 60)

        # KPIs
        kpis = report_data['kpis']
        text.append(f"\n📊 KPIs Clés:")
        text.append(f"  Total prospects: {kpis['total_prospects']}")
        text.append(f"  Contacts effectués: {kpis['prospects_contacts']}")
        text.append(f"  Prospects intéressés: {kpis['prospects_interesses']}")
        text.append(f"  Taux de réponse: {kpis['taux_reponse']}%")
        text.append(f"  Temps moyen conversion: {kpis['temps_moyen_jours']}j")
        text.append(f"  Score moyen: {kpis['score_moyen']}/100")

        # Segments
        segments = report_data['segments']
        text.append(f"\n🎯 Segments cibles:")
        for segment, count in segments.items():
            text.append(f"  {segment}: {count} prospects")

        # Statuts
        statuts = report_data['statuts']
        text.append(f"\n📈 Statuts distribution:")
        for statut, count in statuts.items():
            text.append(f"  {statut}: {count}")

        # Évolution
        evolution = report_data['evolution']
        text.append(f"\n📈 Évolution 7 jours:")
        text.append(f"  Nouveaux prospects: {evolution['nouveaux_7j']}")
        text.append(f"  Convertis: {evolution['interesses_7j']}")

        # Relances prévues
        prevues = report_data['relances_prevues']
        text.append(f"\n⏰ Relances prévies (7j): {len(prevues)}")

        return "\n".join(text)

    def envoyer_alertes(self, config_email: Dict):
        """Envoyer des alertes email"""
        # Vérifier les relances en retard
        date_limite = datetime.now()
        alertes = []

        for prospect_id, calendrier in self.calendrier_relances.items():
            for relance in calendrier:
                if (relance['date'] < date_limite and
                    relance['date'] > date_limite - timedelta(days=1)):
                    alertes.append(relance)

        if alertes:
            sujet = f"Alerte - {len(alertes)} relances en retard"
            corps = self._generer_corps_alerte(alertes, config_email)

            self._envoyer_email(config_email, sujet, corps)

    def _generer_corps_alerte(self, alertes: List[Dict], config: Dict) -> str:
        """Générer le corps de l'alerte email"""
        corps = []
        corps.append("Bonjour,")
        corps.append(f"\nVous avez {len(alertes)} relances en retard à effectuer:")

        for alerte in alertes:
            corps.append(f"\n- Prospect {alerte['prospect_id']}: {alerte['type']} ({alerte['mode']})")

        corps.append(f"\nConnectez-vous au dashboard pour plus de détails.")
        corps.append(f"\nCordialement,")
        corps.append(f"Assistant Prospection M&A")

        return "\n".join(corps)

    def _envoyer_email(self, config: Dict, sujet: str, corps: str):
        """Envoyer un email de notification"""
        try:
            msg = MIMEText(corps, 'plain', 'utf-8')
            msg['Subject'] = sujet
            msg['From'] = config['email_from']
            msg['To'] = config['email_to']

            with smtplib.SMTP(config['smtp_server'], config['smtp_port']) as server:
                if config['smtp_username']:
                    server.starttls()
                    server.login(config['smtp_username'], config['smtp_password'])
                server.send_message(msg)

            self.logger.info("Email d'alerte envoyé avec succès")

        except Exception as e:
            self.logger.error(f"Erreur envoi email: {str(e)}")


def demo_usage():
    """Démonstration d'utilisation du dashboard"""
    tracker = RelanceTracker()

    # Simuler des prospects
    prospects_sample = [
        {'entreprise_nom': 'TechStartup SAS', 'siren': '123456789', 'code_naf': '62.01',
         'chiffre_affaires': 2000000, 'resultat': -50000, 'procedure_collective': True},
        {'entreprise_nom': 'IngénieriePro', 'siren': '987654321', 'code_naf': '69.10',
         'chiffre_affaires': 8000000, 'resultat': -100000, 'entreprise_cessee': False},
        {'entreprise_nom': 'ConsultingPlus', 'siren': '456789123', 'code_naf': '63.11',
         'chiffre_affaires': 1200000, 'resultat': -30000, 'procedure_collective': True}
    ]

    # Ajouter les prospects
    for prospect_data in prospects_sample:
        tracker.ajouter_prospect(prospect_data)

    # Simuler des relances
    for prospect_id in [1, 2, 3]:
        tracker.enregistrer_relance(prospect_id, 'email', 'Relance initiale', datetime.now())

    # Simuler des réponses
    tracker.enregistrer_reponse(1, 'positive', 'Nous sommes intéressés par votre offre')
    tracker.enregistrer_reponse(2, 'demande_info', 'Pourriez-vous nous envoyer plus de détails ?')

    # Générer rapport
    print(tracker.generer_report('text'))


if __name__ == "__main__":
    demo_usage()