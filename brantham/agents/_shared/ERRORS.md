# ERRORS.md — Brantham Partners
_Base de connaissances des erreurs — mise à jour automatiquement_
_Dernière mise à jour : 2026-02-19 15:28_

---

## Erreurs actives (8)

### Llm

- 🟠 **err-20260219-003** — GLM-4.7 (NIM) retourne content=null — la réponse est dans reasoning_content, pas content
  - ✅ Fix : GLM-4.7 est un reasoning model. Extraire le JSON depuis la fin de reasoning_content avec regex. MAX_TOKENS minimum 3000 sinon le raisonnement est tronqué avant la réponse.
  - Tags : `llm`, `api`, `nim`, `glm47`, `reasoning_model`

### Pipeline

- 🟠 **err-20260219-004** — Crons Writer/Hunter/Enricher/Analyst en erreur 'cron delivery target is missing' — delivery mode 'announce' avec channel 'last' non supporté
  - ✅ Fix : Utiliser delivery mode 'silent' pour tous les crons heartbeat. Le mode 'announce' avec channel 'last' est réservé aux sessions actives.
  - Tags : `pipeline`, `orchestration`, `cron`, `openclaw`, `delivery`, `heartbeat`

### Scraper

- 🟠 `[gemweb_all]` **err-20260219-001** — Table filtre Gemweb (Effectif/Code Postal) parsée comme entreprises — faux positifs sur tous les sites Gemweb
  - ✅ Fix : Dans _parse_gemweb_html, skip les tables dont les headers contiennent 'effectif' ET 'code postal' simultanément — c'est la table de filtres de recherche, pas les résultats
  - Tags : `scraper`, `gemweb`, `false_positive`, `scraping`, `filter_table`
- 🟠 `[abitbol]` **err-20260219-002** — Site Abitbol configuré en type 'gemweb' mais n'utilise pas Gemweb — renvoie 0 résultats
  - ✅ Fix : Utiliser type 'abitbol' avec scrape_abitbol() qui parse div.sb-bloc > h3 (nom). Ignorer les blocs courts (duplicates mobiles) et les liens mailto:
  - Tags : `scraper`, `gemweb`, `false_positive`, `scraping`, `custom_structure`
- 🟡 `[adje]` **err-20260219-005** — URL ADJE avec typo /proacedures (404) — et la page est JS-rendered, données vides en scraping HTML
  - ✅ Fix : Utiliser l'API JSON directe api.mh25c.eu avec la clé ADJE. URL correcte: /procedures. Si API retourne '' = vide aujourd'hui, pas une erreur.
  - Tags : `scraper`, `url_error`, `scraping`, `llm`, `api`, `js_render`, `api_json`
- 🟡 `[saj]` **err-20260219-006** — SAJ configuré en 'custom' — scraper cherche div.card/article mais SAJ utilise li.post dans div.module.blog
  - ✅ Fix : Utiliser type 'saj' avec scrape_saj() qui parse li.post > a.subtitle. Strip le préfixe 'RECHERCHE REPRENEURS -' dans les titres.
  - Tags : `scraper`, `custom_structure`, `scraping`, `blog_format`
- 🟡 **err-20260219-007** — Scans partiels (--site=bma, --site=aj2m) polluent le diff — deviennent le 'dernier scan' de référence, causant 400+ faux 'disparues'
  - ✅ Fix : Toujours faire le diff uniquement entre scans COMPLETS (tous sites). Nommer les scans partiels avec un suffixe: scan-[site]-[date].json pour les exclure du diff_scan.py.
  - Tags : `scraper`, `scraping`, `diff`, `partial_scan`
- ⚪ `[abitbol]` **err-20260219-008** — Liens Abitbol pointent vers mailto: — url_dataroom malformée (https://...mailto:...)
  - ✅ Fix : Dans scrape_abitbol, filtrer les liens avec href.startswith('mailto:') ou 'javascript:'. Fallback = URL de la page source.
  - Tags : `scraper`, `url_error`, `scraping`, `mailto`


---

## Usage

**Logger une erreur :**
```bash
python3 log_error.py --type scraper --site [id] --desc "..." --fix "..." --severity medium
```

**Marquer comme résolue :**
```bash
python3 log_error.py --fix-id err-XXXXXXXXXX --fix-note "Ce qui a changé"
```

**Depuis Python :**
```python
from log_error import log_error, get_lessons_for_task
lessons = get_lessons_for_task("scraper BMA avec LLM")
```
