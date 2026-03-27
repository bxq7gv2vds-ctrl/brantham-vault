# Erreurs connues & Fixes

## LLM
- **err-003** : GLM-4.7 (NIM) retourne content=null — reponse dans reasoning_content
  - Fix : extraire JSON depuis fin de reasoning_content avec regex. MAX_TOKENS min 3000
  - Tags : `llm`, `api`, `nim`, `glm47`

## Pipeline / Crons
- **err-004** : Crons Writer/Hunter/Enricher/Analyst en erreur 'cron delivery target is missing'
  - Fix : utiliser delivery mode 'silent' pour crons heartbeat (pas 'announce' + 'last')
  - Tags : `pipeline`, `cron`, `openclaw`

## Scraper

### Gemweb
- **err-001** : Table filtre Gemweb (Effectif/Code Postal) parsee comme entreprises
  - Fix : skip tables dont headers contiennent 'effectif' ET 'code postal'
  - Tags : `scraper`, `gemweb`, `false_positive`

### Abitbol
- **err-002** : Site Abitbol configure en type 'gemweb' mais n'utilise pas Gemweb
  - Fix : utiliser type 'abitbol' avec scrape_abitbol() — parse div.sb-bloc > h3
  - Tags : `scraper`, `abitbol`

- **err-008** : Liens Abitbol pointent vers mailto: — url_dataroom malformee
  - Fix : filtrer href.startswith('mailto:') ou 'javascript:'. Fallback = URL page source
  - Tags : `scraper`, `abitbol`, `url_error`

### ADJE
- **err-005** : URL ADJE avec typo /proacedures (404) + page JS-rendered
  - Fix : utiliser API JSON directe api.mh25c.eu avec cle ADJE. URL correcte: /procedures
  - Tags : `scraper`, `adje`, `api`

### SAJ
- **err-006** : SAJ configure en 'custom' — scraper cherche div.card mais SAJ utilise li.post
  - Fix : utiliser type 'saj' avec scrape_saj() — parse li.post > a.subtitle
  - Tags : `scraper`, `saj`

### Scans partiels
- **err-007** : Scans partiels polluent le diff (400+ faux 'disparues')
  - Fix : diff uniquement entre scans COMPLETS. Nommer partiels: scan-[site]-[date].json
  - Tags : `scraper`, `diff`

## Related
- [[brantham/_MOC]]
