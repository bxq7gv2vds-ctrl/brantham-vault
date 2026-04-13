# Scraping — Patterns & Notes

## Sources actives (20 sites)

### Gemweb RSS (14 sites)
- Format : RSS feed avec description HTML triple-encode
- Particularite : `</BR>` (pas `<br/>`) → remplacer avant parse
- Double-unescape HTML necessaire
- Table filtre (effectif/code postal) = faux positifs → skipper

### BMA
- Site : bma-aj.com
- Bon format, donnees structurees
- Attention deadlines souvent deja depassees

### AJ2M
- Site : aj-2m.com
- Annonces detaillees
- Verifier date limite (parfois format ambigu)

### AJRS
- HTML statique, blocs separes par #XXXX
- Structure ligne par ligne
- Pas de RSS

### Dates
- Multiples formats : DD MMM. YYYY (fr), DD/MM/YYYY, ISO
- Normalises en YYYY-MM-DD par `_normalize_date()`
- `2100-01-01` = placeholder Gemweb "pas de deadline" → efface

## Performance
- 20 sources → ~182 annonces uniques
- Scan complet : ~2-3 minutes
- Endpoint : `POST /api/aj/scrape` + `GET /api/aj/scrape/status`

## Related
- [[brantham/_MOC]]
