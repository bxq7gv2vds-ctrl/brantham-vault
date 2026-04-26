---
date: 2026-04-26
projet: brantham
type: bug-fix
tags: [scraper, url, custom]
---

# Bug — AJ Spécialisés URL malformée (slash manquant)

## Symptôme
Toutes les URL `url_dataroom` des opps AJ Spécialisés étaient malformées : `https://www.aj-specialises.frsociete-fiche.php?id=256` au lieu de `https://www.aj-specialises.fr/societe-fiche.php?id=256`. Conséquence : 27 opps sans DLDO (page détail inaccessible).

## Cause
Dans `scrape_custom` (et 3 autres parsers), la concaténation URL relative + base manquait un `/` :

```python
href = base.group(0) + href if base else href
# base.group(0) = "https://www.aj-specialises.fr"  (sans trailing /)
# href         = "societe-fiche.php?id=256"        (sans leading /)
# → "https://www.aj-specialises.frsociete-fiche.php?id=256"
```

## Fix
4 occurrences dans `scraper_aj.py` (lignes 678, 788, 932, 1551) corrigées via `replace_all` :

```python
if base:
    sep = "" if href.startswith("/") else "/"
    href = base.group(0) + sep + href
```

## Résultat
AJ Spécialisés passe de 0% à 100% DLDO coverage après re-scrape.

## Leçon
Quand on concatène URL base + path relative, toujours normaliser le séparateur. Les libs Python `urllib.parse.urljoin` font ça correctement — préférer ça aux concats manuelles.

## Related
- [[_system/MOC-bugs]]
- [[brantham/_MOC]]
- [[brantham/sessions/2026-04-26-cockpit-aj]]
