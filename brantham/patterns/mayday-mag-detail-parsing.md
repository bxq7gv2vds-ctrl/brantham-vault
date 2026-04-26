---
date: 2026-04-26
project: brantham
tags: [pattern, scraping, mayday, aj-source]
---

# Pattern : Parsing pages détail Mayday Mag pour normaliser AJ source

## Quoi
Scraper Mayday Mag v5 qui ne se contente plus de récupérer les titres d'annonces, mais **fetch chaque page détail** pour extraire :
- Le **vrai cabinet AJ source** (normalisé sur notre table d'IDs internes)
- DLDO (date limite de dépôt des offres)
- CA, effectif, localisation
- Email contact

## Pourquoi
**Avant** (v4) : 11 opps Mayday → toutes sous `source_aj="Maydaymag"` (fourre-tout). DLDO = 0% (juste le titre).
**Après** (v5) : 11 opps réparties sur 8 cabinets distincts (STAR, AJ Associés, AJ UP, BCM, CBF, 2M, AJRS, Abitbol, P2G). DLDO = 100%, CA = 100%, effectif = 80%.

→ **Découverte clé** : 2 nouveaux cabinets AJ qui n'ont PAS de dataroom propre (Mayday est leur seule fenêtre publique) :
- **STAR Administrateurs Judiciaires** (Annecy / Grenoble / Chambéry)
- **AJ Associés** (Me Lebreton + Me Michel)

Sans ce pattern, on aurait raté ces deux cabinets en faux-positif "source = Maydaymag".

## Comment

### 1. Fetch liste annonces (page principale, JS rendered)
Mayday est une SPA WordPress + React. Utilisation de **LightPanda** pour rendre le JS :
```python
html = lp.fetch_html("https://www.maydaymag.fr/les-entreprises-a-reprendre/", timeout=30)
```

### 2. Extraction des URLs d'annonces
Slugs > 25 chars, pas dans skip-list (nous-contacter, le-mag, tag, etc.) :
```python
SKIP = {"nous-contacter","le-mag","tag","recrutement","nos-solutions","base-des-deals", ...}
for a in soup.find_all("a", href=True):
    href = a["href"]
    if "maydaymag.fr/" in href and slug not in SKIP and len(slug) > 25:
        urls.add(href)
```

### 3. Fetch parallèle des détails (4 workers)
```python
with ThreadPoolExecutor(max_workers=4) as ex:
    for entry in ex.map(_process, annonce_urls):
        if entry: results.append(entry)
```

### 4. Parsing du bloc CONTACT
Dans chaque page détail, le bloc CONTACT contient :
```
CONTACT
Abitbol & Rousselet – Maître Frédéric Abitbol – Administrateur judiciaire
Mail : eguilles@fajr.eu
P2G : Maître Céline Pelzer – Administrateur judiciaire
```

Délimité par "CONTACT" en début et "Article précédent" / "Article suivant" / "FICHES" / "VEILLE" en fin.

### 5. Normalisation cabinet → ID interne stable
Table de mapping regex :
```python
MAYDAY_AJ_NORMALIZE = [
    (re.compile(r"\b2M\s*&\s*Associ", re.I),                   "aj2m",         "2M&Associés"),
    (re.compile(r"\bAbitbol\s*&\s*Rousselet\b", re.I),         "abitbol",      "Abitbol & Rousselet"),
    (re.compile(r"\bAJ\s*UP\b|SELAS\s+AJ\s+UP", re.I),         "ajup",         "AJ UP"),
    (re.compile(r"\bSTAR\b\s*(?:Administrateurs|–|-)", re.I),  "star",         "STAR Administrateurs Judiciaires"),
    (re.compile(r"\bAJ\s+Associ[ée]s\b", re.I),                "aj_associes",  "AJ Associés"),
    # ... 18 autres cabinets connus
]
```

→ Permet de **dédupliquer** : si STAR publie le même deal sur Mayday ET (un jour) sur sa propre dataroom, l'ID `make_id("star", nom)` sera identique → upsert sans doublon.

### 6. Extraction structured data
- **DLDO** : pattern "Date limite de dépôt des offres : <DATE>" (regex multi-format, parse FR)
- **Localisation** : "située à VILLE (CP)" → `"Éguilles (13510)"`
- **CA / Effectif** : helpers `extract_ca()` + `extract_effectif()` réutilisés
- **Email** : regex standard pour tracer dans `notes_scraper`

### 7. Site dict virtuel pour make_entry
Au moment de créer l'entrée, on override site["id"] et site["name"] avec le cabinet réel détecté :
```python
sid, sname = _mayday_normalize_aj(d["contact"])
virtual_site = {"id": sid, "name": sname, "url": url}
return make_entry(virtual_site, title, ca=..., effectif=..., url_dataroom=url,
                  notes=f"via Mayday Mag · contact: {email}", date_limite=dldo_iso)
```

## Coverage finale (test 2026-04-26)
| Source détectée | Nb annonces |
|---|---|
| AJ Associés | 2 (NOUVEAU) |
| AJ UP | 2 |
| STAR Administrateurs Judiciaires | 2 (NOUVEAU) |
| 2M&Associés | 1 |
| AJRS | 1 |
| Abitbol & Rousselet | 1 |
| BCM | 1 |
| CBF Associés | 1 |

## Pièges
- **API Mayday peut ralentir** sous charge → max_workers=4 (pas 16)
- **Format date** : "mercredi 27 mai 2026 à 12h00" → parse_date_limite gère via regex multi-format
- **Personne morale dans dirigeants** : skip si nom et prénom vides
- **Cabinet inconnu** : fallback sur `("maydaymag", "Maydaymag")` + log "vérification AJ requise"

## Where
- Code : `cockpit/scraper_aj.py:scrape_maydaymag` v5 + helpers `_mayday_*`
- Cron suggéré : daily 09:00 (launchd) avec import auto

## Related
- [[brantham/sessions/2026-04-26-cockpit-tui-supabase-hunters]]
- [[brantham/_MOC]]
- [[_system/MOC-patterns]]
