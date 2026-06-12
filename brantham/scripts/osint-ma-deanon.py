#!/usr/bin/env python3
"""
Script OSINT M&A - Désanonymisation de cibles anonymes
Extraction automatique de SIREN et données métier depuis teasers anonymisés
"""

import re
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import urllib.parse

class OSINTMA:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.results = {}

    def extract_from_teaser(self, teaser_text):
        """
        Extrait les infos clés d'un teaser anonymisé
        """
        patterns = {
            'activite': [
                r'activit[eé]s?\s*:\s*([^.]+)',
                r'secteur[^\w:]*\s*:\s*([^.]+)',
                r'march[ée]?\s*:\s*([^.]+)'
            ],
            'taille': [
                r'effectif[^\w:]*\s*:\s*(\d+)',
                r'(?:dizaines|centaines|milliers)\s*(?:d\')?employ[ée]s?',
                r'(\d+)\s*(?:employ[ée]s?|personnes)'
            ],
            'chiffre_affaires': [
                r'chiffre[ -]d?[ -]affaires[^\w:]*\s*:\s*(\d+)\s*(?:k|k€|millions?|€)',
                r'CA[^\w:]*\s*:\s*(\d+)\s*(?:k|k€|millions?|€)'
            ],
            'localisation': [
                r'(?:situ[ée]|implant[ée])\s*[àe]\s*([^,.]+)',
                r'base[^\w:]*\s*[àe]\s*([^,.]+)',
                r'([^,.]+)\s*(?:paris|lyon|marseille|bordeaux|nantes|strasbourg)'
            ],
            'technologie': [
                r'secteur[^\w:]*:\s*(tech|digital|informatique|software)',
                r'activit[eé][^\w:]*:\s*(solutions?|plateforme|SAAS)',
                r'technologies?\s*:\s*([^,.]+)'
            ]
        }

        extracted = {}

        for category, pattern_list in patterns.items():
            for pattern in pattern_list:
                matches = re.findall(pattern, teaser_text, re.IGNORECASE)
                if matches:
                    extracted[category] = matches[0].strip()
                    break

        return extracted

    def search_actify(self, query):
        """Recherche sur actify.fr"""
        try:
            url = f"https://www.actify.fr/recherche?q={urllib.parse.quote(query)}"
            response = self.session.get(url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')

            results = []
            for item in soup.find_all('div', class_='annonce')[:3]:
                title = item.get_text(strip=True)
                link = item.find('a')['href'] if item.find('a') else ''
                results.append({
                    'source': 'actify.fr',
                    'title': title,
                    'link': link
                })
            return results
        except:
            return []

    def search_aj_dataroom(self, query):
        """Recherche sur AJ Dataroom"""
        try:
            url = f"https://www.aj-dataroom.com/search?q={urllib.parse.quote(query)}"
            response = self.session.get(url, timeout=10)
            return self._parse_aj_results(response.text)
        except:
            return []

    def search_repreneurs_com(self, query):
        """Recherche sur repreneurs.com"""
        try:
            url = f"https://www.repreneurs.com/recherche?mots={urllib.parse.quote(query)}"
            response = self.session.get(url, timeout=10)
            return self._parse_repreneurs_results(response.text)
        except:
            return []

    def search_bodacc(self, activite, localisation=None):
        """Recherche BODACC public"""
        try:
            params = {
                'type': 'CESSION',
                'texte': activite
            }
            if localisation:
                params['departement'] = localisation

            url = "https://www.bodacc.fr"
            response = self.session.get(url, params=params, timeout=15)
            return self._parse_bodacc_results(response.text)
        except:
            return []

    def siren_papers_lookup(self, company_name, localisation=None):
        """Recherche SIREN via Papers"""
        try:
            from mcp_papers_sirenisator import mcp__pappers__sirenisator

            params = {
                'country_code': 'FR',
                'company_name': company_name
            }
            if localisation:
                params['company_city'] = localisation

            result = mcp__pappers__sirenisator(**params)
            return result[0] if result else None
        except:
            return None

    def get_company_details(self, siren):
        """Récupère les détails complets d'une entreprise via SIREN"""
        try:
            from mcp_pappers_informations_entreprise import mcp__pappers__informations_entreprise

            result = mcp__pappers__informations_entreprise(
                siren=siren,
                return_fields=[
                    'siren', 'nom_entreprise', 'code_naf', 'libelle_code_naf',
                    'effectif', 'tranche_effectif', 'date_creation',
                    'categorie_juridique', 'forme_juridique', 'chiffre_affaires',
                    'resultat', 'dettes_financieres', 'capacite_autofinancement'
                ]
            )
            return result[0] if result else None
        except:
            return None

    def generate_report(self, teaser_text):
        """Génère un rapport de désanonymisation complet"""
        print("🔍 Désanonymisation en cours...")

        # Extraction des patterns
        extracted = self.extract_from_teaser(teaser_text)
        print(f"📋 Patterns extraits: {list(extracted.keys())}")

        # Recherche multi-source
        all_results = []

        if 'activite' in extracted:
            # Actify
            actify_results = self.search_actify(extracted['activite'])
            all_results.extend(actify_results)

            # AJ Dataroom
            aj_results = self.search_aj_dataroom(extracted['activite'])
            all_results.extend(aj_results)

            # Repreneurs.com
            repreneurs_results = self.search_repreneurs_com(extracted['activite'])
            all_results.extend(repreneurs_results)

            # BODACC
            bodacc_results = self.search_bodacc(
                extracted['activite'],
                extracted.get('localisation')
            )
            all_results.extend(bodacc_results)

        # SIREN identification
        siren = None
        if 'activite' in extracted:
            siren = self.siren_papers_lookup(
                extracted['activite'],
                extracted.get('localisation')
            )
            if siren:
                print(f"✅ SIREN identifié: {siren}")

                # Détails entreprise
                company_details = self.get_company_details(siren)
                if company_details:
                    print(f"🏢 Entreprise: {company_details.get('nom_entreprise', 'N/A')}")
                    self.results['entreprise'] = company_details

        # Compilation du rapport
        report = {
            'timestamp': datetime.now().isoformat(),
            'teaser_original': teaser_text,
            'patterns_extraits': extracted,
            'recherche_sources': all_results,
            'siren_identifie': siren,
            'entreprise_details': self.results.get('entreprise'),
            'confidence_score': self._calculate_confidence(extracted, siren)
        }

        return report

    def _calculate_confidence(self, extracted, siren):
        """Calcule le score de confiance"""
        score = 0
        if 'activite' in extracted: score += 30
        if 'taille' in extracted: score += 20
        if 'chiffre_affaires' in extracted: score += 25
        if 'localisation' in extracted: score += 15
        if siren: score += 10
        return min(score, 100)

    def save_report(self, report, filename):
        """Sauvegarde le rapport JSON"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        print(f"💾 Rapport sauvegardé: {filename}")

def main():
    """Exemple d'utilisation"""
    osint = OSINTMA()

    # Exemple de teaser anonymisé
    teaser_anonyme = """
    Entreprise de solutions digitales B2B, basée en région parisienne,
    effectif de 25 personnes, CA estimé à 5M€, spécialisée
    dans la transformation cloud pour les PME.
    """

    print("🚀 Début de la désanonymisation")
    print("="*50)

    # Génération du rapport
    rapport = osint.generate_report(teaser_anonyme)

    # Sauvegarde
    filename = f"deanon_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    osint.save_report(rapport, filename)

    print("\n📊 Résultat final:")
    print(f"Score de confiance: {rapport['confidence_score']}%")
    if rapport['siren_identifie']:
        print(f"SIREN: {rapport['siren_identifie']}")
    if rapport['entreprise_details']:
        entreprise = rapport['entreprise_details']
        print(f"Nom: {entreprise.get('nom_entreprise', 'N/A')}")
        print(f"Activité: {entreprise.get('libelle_code_naf', 'N/A')}")
        print(f"Effectif: {entreprise.get('effectif', 'N/A')}")

if __name__ == "__main__":
    main()