---
name: Data Sources Polymarket Hedge Fund
description: Inventaire complet des sources data gratuites best-in-class par région pour forecasting météo et trading Polymarket
type: reference
created: 2026-04-17
tags: [polymarket, data, nwp, observations, radar]
---

# Data Sources — Best-in-Class par Région

**Principe** : utiliser LA meilleure source disponible pour chaque tâche × région. Tout est gratuit.

## NWP (Numerical Weather Prediction)

### Global

| Source | Resolution | Update | Horizon | Access |
|---|---|---|---|---|
| **GFS** (NOAA) | 13-25km | 6h | 384h | NOMADS + Open-Meteo |
| **ECMWF-IFS** (Open Data) | 9km | 6h | 240h | data.ecmwf.int (FREE) |
| **GEFS** ensemble (NOAA) | 25km, 31 members | 6h | 384h | NOMADS |
| **ECMWF ENS** | 9km, 51 members | 12h | 360h | CDS (free registration) |
| **GEM** (Canada) | 15km | 12h | 240h | Open-Meteo |
| **NAVGEM** (US Navy) | 15km | 6h | 180h | Open-Meteo |

### USA (haute-résolution)

| Source | Resolution | Update | Horizon | Notes |
|---|---|---|---|---|
| **HRRR** (NOAA) | **3km** | **1h** | 18h | Meilleur nowcast US |
| **RAP** (NOAA) | 13km | 1h | 51h | Backup plus large |
| **NAM** | 12km | 6h | 84h | Fine-mesh |
| **URMA** analysis | 2.5km | 1h | - | Reanalysis nowcast |

### Europe (haute-résolution)

| Source | Pays | Resolution | Update | Notes |
|---|---|---|---|---|
| **ICON-EU** (DWD) | EU | 6.5km | 3h | Open Data DWD |
| **ICON-D2** (DWD) | DE/AT/CH | 2km | 3h | Alpes focus |
| **AROME** (Météo-France) | FR | **1.3km** | 3h | Le plus fin en France |
| **UKV** (MetOffice) | UK | 1.5km | 3h | UK haute-res |
| **HARMONIE-AROME** | Nordics | 2.5km | 3h | FMI, SMHI |

### Asie

| Source | Pays | Resolution | Update |
|---|---|---|---|
| **JMA MSM** | JP | 5km | 3h |
| **JMA GSM** | global JP | 20km | 6h |
| **KMA LDAPS** | KR | 1.5km | 3h |
| **KMA UM** | global KR | 17km | 12h |
| **CMA GRAPES** | CN | 10km | 12h |

### Accès pratique

**Open-Meteo** (open-meteo.com) — **API GRATUITE jusqu'à 10k req/jour** :
- Agrège 139 membres ensemble : GFS 30 + ICON 39 + GEM 20 + ECMWF 50
- Simple REST API, pas de GRIB parsing
- Modèles individuels accessibles : `gfs_seamless`, `ecmwf_ifs04`, `icon_seamless`, `icon_eu`, `gfs_hrrr`, `arome_france`
- **Recommandé comme primary fetcher**

**Alternatives pour ingestion directe** :
- NOAA NOMADS (http://nomads.ncep.noaa.gov) — GRIB2 files, requires pygrib
- ECMWF Open Data (data.ecmwf.int) — GRIB2, requires ecmwf-opendata client
- DWD Open Data (opendata.dwd.de) — GRIB2 direct
- CDS Copernicus (cds.climate.copernicus.eu) — Python cdsapi

## Observations

### Surface temperature

| Source | Coverage | Update | Access |
|---|---|---|---|
| **METAR** (ASOS) | Global airports | 1h (some 30min) | aviationweather.gov/api/data/metar |
| **Mesonet** (US) | US denser stations | 5-30min | synopticdata.com (free 30d) |
| **OGIMET** | Global historique | daily | ogimet.com |
| **Weather Underground PWS** | 400k+ urban | 5min | wunderground API (paid) |
| **Netatmo** | Home stations | 10min | weathermap.netatmo.com |
| **Davis/Tempest IoT** | Private | 5min | proprietary APIs |
| **MADIS** | US multi-source | 5min | madis.ncep.noaa.gov |

### Upper air

| Source | Notes |
|---|---|
| **Radiosonde TEMP** | Univ. Wyoming weather.uwyo.edu/upperair/ |
| **ADS-B aircraft** | wind + temp aloft, adsb-exchange |
| **AMDAR** | aircraft meteo reports |

### Radar

| Source | Coverage | Update | Format |
|---|---|---|---|
| **NEXRAD Level-II** | US | 4-10min | AWS S3 noaa-nexrad-level2 (FREE) |
| **MRMS** | US composite | 2min | AWS S3 noaa-mrms-pds |
| **OPERA** | EU composite | 15min | EUMETNET |
| **Radar local** | Pays-par-pays | 15min | APIs nationales |

### Satellite

| Source | Coverage | Update | Format |
|---|---|---|---|
| **GOES-16/17/18** | Americas | 5-15min | AWS S3 noaa-goes16 |
| **Meteosat MSG** | Europe/Africa | 15min | EUMETSAT (free reg.) |
| **Himawari** | Asia-Pacific | 10min | JMA (free) |
| **Sentinel-3** | Global | daily | Copernicus |

## Reanalysis (pour training ML)

| Source | Resolution | Period | Notes |
|---|---|---|---|
| **ERA5** (ECMWF) | 31km, 1h | 1940-present | SOTA reanalysis, FREE via Copernicus CDS |
| **MERRA-2** (NASA) | 50km, 1h | 1980-present | Alternative, NASA GES DISC |
| **CFSR** (NOAA) | 38km, 6h | 1979-present | Older |
| **ISD** (NOAA) | stations, 1h | 1901-present | Historical observations only |

**ERA5 recommandé pour training** : download 5 ans × stations Polymarket via `cdsapi` Python client. ~50Go pour 40 stations × 5 ans × 1h.

## Polymarket

| Endpoint | Purpose | Rate Limit |
|---|---|---|
| Gamma API REST | market metadata | 100/min |
| **CLOB WebSocket** | real-time orderbook L2 | per IP |
| CLOB REST | orders, trades | per API key |
| Py Polymarket Client | py-clob-client | - |

**CLOB** est le vrai endpoint à utiliser pour trading latency-sensitive. Gamma est OK pour scan mais trop lent pour execution.

## Priorisation pour implementation

**Phase 1 (J1-J3)** — MVP data hub :
1. Open-Meteo ensemble (primary NWP, 139 members) ✅ déjà codé
2. METAR via aviationweather.gov ✅ déjà codé
3. Polymarket CLOB WebSocket (nouveau — à coder)
4. ERA5 backfill 5 ans (nouveau — script one-shot)

**Phase 2 (J4-J7)** — Régional haute-res :
5. HRRR direct via Open-Meteo `gfs_hrrr` pour US
6. ICON-EU via Open-Meteo `icon_eu` pour Europe
7. AROME via Open-Meteo `arome_france` pour France
8. Mesonet via synopticdata

**Phase 3 (J8-J14)** — Radar + satellite :
9. MRMS composite US via AWS
10. NEXRAD radar nowcast
11. GOES satellite IR

**Phase 4 (J15+)** — Avancé :
12. Direct NOAA NOMADS GRIB parsing (si Open-Meteo quota)
13. ECMWF IFS ensemble complet (51 membres via CDS)
14. PWS réseau pour urban microclimate

## Related

- [[_MOC|Polymarket Hub]]
- [[architecture|Architecture hedge fund grade]]
- [[model-design|Design modèle ML]]
- [[roadmap|Roadmap phased]]
