# Master Quant Meta-Report — 2026-04-22

_Généré : 2026-04-22 18:59 UTC_

## Synthèse globale

- **38** villes analysées
- **17,597** markets
- **9,084,703** trades on-chain
- **$58.85M** volume USDC total
- **4** behavior clusters identifiés (KMeans)

## Tableau master (38 villes, sortées par volume)

| Ville | N | Vol USDC | AUC | Hurst | χ² | GARCH | EV best | Strategy |
|-------|--:|---------:|----:|------:|---:|------:|--------:|----------|
| London | 1,475 | $8.66M | 0.821 | 0.56 | 121.2 | 0.50 | +3938.7% | buy_no_favorites |
| New York | 1,486 | $7.43M | 0.820 | 0.45 | 102.5 | 0.50 | +2237.1% | buy_no_favorites |
| Seoul | 1,013 | $5.92M | 0.794 | 0.62 | 23.2 | 0.50 | +308.7% | buy_no_favorites |
| Dallas | 1,027 | $2.76M | 0.841 | 0.71 | 19.9 | 0.50 | +66.6% | buy_yes_longshot |
| Atlanta | 1,020 | $2.47M | 0.824 | 0.72 | 54.9 | 0.98 | +2128.7% | buy_no_favorites |
| Wellington | 684 | $2.46M | 0.872 | 1.09 | 26.5 | 0.50 | +40.9% | buy_no_uncertain |
| Shanghai | 280 | $2.28M | 0.783 | nan | 4.5 | 0.50 | +53.6% | buy_no_uncertain |
| Miami | 697 | $2.22M | 0.871 | 2.14 | 29.2 | 0.50 | +2574.6% | buy_no_favorites |
| Tel Aviv | 307 | $2.21M | 0.776 | nan | 4.5 | 0.50 | +59.3% | buy_no_uncertain |
| Chicago | 698 | $2.12M | 0.751 | 0.87 | 17.6 | 0.50 | +81.8% | buy_yes_longshot |
| Seattle | 1,011 | $2.11M | 0.837 | 0.80 | 60.9 | 0.96 | +1185.7% | buy_no_favorites |
| Toronto | 1,024 | $2.00M | 0.768 | 0.71 | 70.5 | 0.50 | +2409.5% | buy_no_favorites |
| Buenos Aires | 1,013 | $1.90M | 0.843 | 0.79 | 77.5 | 0.10 | +1051.2% | buy_no_favorites |
| Paris | 521 | $1.88M | 0.852 | 0.79 | 10.9 | 0.50 | +39.0% | buy_no_uncertain |
| Tokyo | 307 | $1.43M | 0.754 | nan | 8.7 | 0.50 | +60.2% | buy_no_uncertain |
| Lucknow | 352 | $1.13M | 0.894 | 0.94 | 12.8 | 1.00 | +21.8% | buy_yes_uncertain |
| Hong Kong | 260 | $1.09M | 0.741 | nan | 11.9 | 0.86 | +56.1% | buy_yes_longshot |
| Sao Paulo | 521 | $1.07M | 0.779 | 1.01 | 23.5 | 0.50 | +52.0% | buy_no_uncertain |
| Shenzhen | 209 | $907k | 0.792 | nan | 3.9 | 0.50 | +64.4% | buy_yes_longshot |
| Singapore | 280 | $823k | 0.878 | nan | 6.3 | 0.50 | +13.9% | buy_yes_uncertain |
| Munich | 352 | $807k | 0.775 | 1.23 | 16.1 | 0.50 | +47.9% | buy_no_uncertain |
| Taipei | 253 | $643k | 0.565 | nan | 28.6 | 0.10 | +155.5% | buy_yes_longshot |
| Beijing | 209 | $546k | 0.851 | nan | 6.1 | 0.50 | +38.3% | buy_no_uncertain |
| Madrid | 253 | $538k | 0.725 | nan | 7.8 | 0.96 | +62.9% | buy_no_uncertain |
| Milan | 253 | $379k | 0.810 | nan | 7.6 | 0.96 | +48.6% | buy_no_uncertain |
| Warsaw | 253 | $360k | 0.755 | nan | 7.7 | 0.99 | +45.3% | buy_yes_uncertain |
| Chongqing | 209 | $313k | 0.689 | nan | 10.1 | 0.50 | +94.7% | buy_no_uncertain |
| San Francisco | 165 | $300k | 0.799 | nan | 2.8 | 0.50 | +3.4% | buy_no_brackets |
| Chengdu | 198 | $295k | 0.701 | nan | 3.6 | 0.50 | +182.4% | buy_yes_longshot |
| Los Angeles | 179 | $294k | 0.679 | nan | 3.3 | 0.96 | +40.8% | buy_yes_longshot |
| Wuhan | 209 | $294k | 0.754 | nan | 3.8 | 0.50 | +58.0% | buy_no_uncertain |
| Denver | 175 | $271k | 0.542 | nan | 9.0 | 0.98 | +55.0% | buy_yes_longshot |
| Austin | 165 | $232k | 0.784 | nan | 14.9 | 0.50 | +1.0% | buy_no_brackets |
| Istanbul | 110 | $226k | 0.572 | nan | 7.8 | 0.50 | +238.5% | buy_yes_longshot |
| Houston | 165 | $212k | 0.724 | nan | 8.4 | 0.50 | +1.2% | buy_no_brackets |
| Moscow | 99 | $138k | 0.511 | nan | 1.6 | nan | +33.3% | buy_yes_uncertain |
| Mexico City | 99 | $80k | 0.553 | nan | 3.4 | nan | +3.1% | buy_no_brackets |
| Busan | 66 | $58k | 0.539 | nan | 1.4 | nan | +10.5% | buy_yes_uncertain |

## Rankings cross-city

### 1. Top 10 prédictibilité ex-ante (AUC XGBoost le plus haut)

| Ville | AUC | Brier | N markets |
|-------|----:|------:|----------:|
| Lucknow | **0.894** | 0.0670 | 352 |
| Singapore | **0.878** | 0.0701 | 280 |
| Wellington | **0.872** | 0.0806 | 684 |
| Miami | **0.871** | 0.0812 | 697 |
| Paris | **0.852** | 0.0998 | 521 |
| Beijing | **0.851** | 0.0700 | 209 |
| Buenos Aires | **0.843** | 0.1025 | 1,013 |
| Dallas | **0.841** | 0.1026 | 1,027 |
| Seattle | **0.837** | 0.0780 | 1,011 |
| Atlanta | **0.824** | 0.0965 | 1,020 |

### 2. Top 10 mal calibrés (χ² le plus haut → edge potential)

| Ville | χ² | p-value | EV best strat | N bets best |
|-------|---:|--------:|--------------:|------------:|
| London | **121.2** | 0.00e+00 | +3938.7% | 12 |
| New York | **102.5** | 0.00e+00 | +2237.1% | 12 |
| Buenos Aires | **77.5** | 5.13e-13 | +1051.2% | 26 |
| Toronto | **70.5** | 1.16e-12 | +2409.5% | 13 |
| Seattle | **60.9** | 1.00e-10 | +1185.7% | 5 |
| Atlanta | **54.9** | 1.27e-08 | +2128.7% | 18 |
| Miami | **29.2** | 5.54e-05 | +2574.6% | 5 |
| Taipei | **28.6** | 2.79e-05 | +155.5% | 155 |
| Wellington | **26.5** | 1.77e-04 | +40.9% | 31 |
| Sao Paulo | **23.5** | 2.74e-04 | +52.0% | 22 |

### 3. Top 10 mean-reverting (Hurst le plus bas)

| Ville | Hurst | half-life steps | best strat |
|-------|------:|----------------:|------------|
| New York | **0.452** | 0.678 | buy_no_favorites |
| London | **0.556** | 0.683 | buy_no_favorites |
| Seoul | **0.620** | 0.690 | buy_no_favorites |
| Dallas | **0.707** | 0.946 | buy_yes_longshot |
| Toronto | **0.713** | 0.650 | buy_no_favorites |
| Atlanta | **0.717** | 0.686 | buy_no_favorites |
| Paris | **0.793** | 0.667 | buy_no_uncertain |
| Buenos Aires | **0.793** | 0.762 | buy_no_favorites |
| Seattle | **0.797** | 0.916 | buy_no_favorites |
| Chicago | **0.870** | 0.672 | buy_yes_longshot |

### 4. Top 10 high vol persistence (GARCH ≥0.95 → vol shocks durent)

| Ville | GARCH persist | Hurst | EV best |
|-------|--------------:|------:|--------:|
| Lucknow | **0.997** | 0.94 | +21.8% |
| Warsaw | **0.986** | nan | +45.3% |
| Denver | **0.980** | nan | +55.0% |
| Atlanta | **0.977** | 0.72 | +2128.7% |
| Los Angeles | **0.961** | nan | +40.8% |
| Milan | **0.961** | nan | +48.6% |
| Madrid | **0.961** | nan | +62.9% |
| Seattle | **0.956** | 0.80 | +1185.7% |

### 5. Best EV/bet par stratégie

_⚠️ EV très élevés (>1000%) sur N petits (<30) à risk de overfit._

| Ville | Strategy | EV/bet | N bets | Sharpe |
|-------|----------|-------:|-------:|-------:|
| London | buy_no_favorites | **+3938.7%** | 12 | 0.999 |
| Miami | buy_no_favorites | **+2574.6%** | 5 | 0.697 |
| Toronto | buy_no_favorites | **+2409.5%** | 13 | 0.665 |
| New York | buy_no_favorites | **+2237.1%** | 12 | 0.788 |
| Atlanta | buy_no_favorites | **+2128.7%** | 18 | 0.573 |
| Seattle | buy_no_favorites | **+1185.7%** | 5 | 0.612 |
| Buenos Aires | buy_no_favorites | **+1051.2%** | 26 | 0.619 |
| Seoul | buy_no_favorites | **+308.7%** | 8 | 0.372 |
| Istanbul | buy_yes_longshot | **+238.5%** | 64 | 0.137 |
| Chengdu | buy_yes_longshot | **+182.4%** | 131 | 0.119 |

## Behavior clusters cross-city (KMeans 6-D)

Clustering sur (calib_chi2, hurst, half-life, GARCH, AUC, Kyle's λ).

### Cluster 0 (5 villes)

**Villes** : London, New York, Seoul, Toronto, Buenos Aires

**Caractéristiques moyennes** : AUC=0.809, Hurst=0.63, χ²=79.0, GARCH=0.42

### Cluster 1 (6 villes)

**Villes** : Dallas, Atlanta, Wellington, Seattle, Paris, Sao Paulo

**Caractéristiques moyennes** : AUC=0.834, Hurst=0.85, χ²=32.8, GARCH=0.66

### Cluster 2 (2 villes)

**Villes** : Chicago, Munich

**Caractéristiques moyennes** : AUC=0.763, Hurst=1.05, χ²=16.8, GARCH=0.50


## Recommandations master pour bucket_router / city_config

### 1. Activer en priorité (haute calib χ² + EV best > 100% + N bets ≥ 10)

- **London** — `buy_no_favorites` : EV +3939% par bet, N=12, χ²=121.2
- **Toronto** — `buy_no_favorites` : EV +2409% par bet, N=13, χ²=70.5
- **New York** — `buy_no_favorites` : EV +2237% par bet, N=12, χ²=102.5
- **Atlanta** — `buy_no_favorites` : EV +2129% par bet, N=18, χ²=54.9
- **Buenos Aires** — `buy_no_favorites` : EV +1051% par bet, N=26, χ²=77.5

### 2. Désactiver / SHADOW (calibrés OK + AUC < 0.6)

- **Moscow** — bookies fair (calibrated p>0.05), AUC=0.511 → pas d'edge ex-ante exploitable
- **Mexico City** — bookies fair (calibrated p>0.05), AUC=0.553 → pas d'edge ex-ante exploitable
- **Busan** — bookies fair (calibrated p>0.05), AUC=0.539 → pas d'edge ex-ante exploitable

### 3. Filtrage régime à activer (GARCH ≥ 0.95)

- **Atlanta** — vol clustering massif (persistence 0.977). Réduire kelly de 50% pendant phases haute-vol (vol > 2× médiane).
- **Seattle** — vol clustering massif (persistence 0.956). Réduire kelly de 50% pendant phases haute-vol (vol > 2× médiane).
- **Lucknow** — vol clustering massif (persistence 0.997). Réduire kelly de 50% pendant phases haute-vol (vol > 2× médiane).
- **Madrid** — vol clustering massif (persistence 0.961). Réduire kelly de 50% pendant phases haute-vol (vol > 2× médiane).
- **Milan** — vol clustering massif (persistence 0.961). Réduire kelly de 50% pendant phases haute-vol (vol > 2× médiane).
- **Warsaw** — vol clustering massif (persistence 0.986). Réduire kelly de 50% pendant phases haute-vol (vol > 2× médiane).
- **Los Angeles** — vol clustering massif (persistence 0.961). Réduire kelly de 50% pendant phases haute-vol (vol > 2× médiane).
- **Denver** — vol clustering massif (persistence 0.980). Réduire kelly de 50% pendant phases haute-vol (vol > 2× médiane).

## Liens vers fiches détaillées

- [[atlanta|Atlanta]] — AUC 0.82, χ² 54.9
- [[austin|Austin]] — AUC 0.78, χ² 14.9
- [[beijing|Beijing]] — AUC 0.85, χ² 6.1
- [[buenos-aires|Buenos Aires]] — AUC 0.84, χ² 77.5
- [[busan|Busan]] — AUC 0.54, χ² 1.4
- [[chengdu|Chengdu]] — AUC 0.70, χ² 3.6
- [[chicago|Chicago]] — AUC 0.75, χ² 17.6
- [[chongqing|Chongqing]] — AUC 0.69, χ² 10.1
- [[dallas|Dallas]] — AUC 0.84, χ² 19.9
- [[denver|Denver]] — AUC 0.54, χ² 9.0
- [[hong-kong|Hong Kong]] — AUC 0.74, χ² 11.9
- [[houston|Houston]] — AUC 0.72, χ² 8.4
- [[istanbul|Istanbul]] — AUC 0.57, χ² 7.8
- [[london|London]] — AUC 0.82, χ² 121.2
- [[los-angeles|Los Angeles]] — AUC 0.68, χ² 3.3
- [[lucknow|Lucknow]] — AUC 0.89, χ² 12.8
- [[madrid|Madrid]] — AUC 0.72, χ² 7.8
- [[mexico-city|Mexico City]] — AUC 0.55, χ² 3.4
- [[miami|Miami]] — AUC 0.87, χ² 29.2
- [[milan|Milan]] — AUC 0.81, χ² 7.6
- [[moscow|Moscow]] — AUC 0.51, χ² 1.6
- [[munich|Munich]] — AUC 0.77, χ² 16.1
- [[new-york|New York]] — AUC 0.82, χ² 102.5
- [[paris|Paris]] — AUC 0.85, χ² 10.9
- [[san-francisco|San Francisco]] — AUC 0.80, χ² 2.8
- [[sao-paulo|Sao Paulo]] — AUC 0.78, χ² 23.5
- [[seattle|Seattle]] — AUC 0.84, χ² 60.9
- [[seoul|Seoul]] — AUC 0.79, χ² 23.2
- [[shanghai|Shanghai]] — AUC 0.78, χ² 4.5
- [[shenzhen|Shenzhen]] — AUC 0.79, χ² 3.9
- [[singapore|Singapore]] — AUC 0.88, χ² 6.3
- [[taipei|Taipei]] — AUC 0.57, χ² 28.6
- [[tel-aviv|Tel Aviv]] — AUC 0.78, χ² 4.5
- [[tokyo|Tokyo]] — AUC 0.75, χ² 8.7
- [[toronto|Toronto]] — AUC 0.77, χ² 70.5
- [[warsaw|Warsaw]] — AUC 0.76, χ² 7.7
- [[wellington|Wellington]] — AUC 0.87, χ² 26.5
- [[wuhan|Wuhan]] — AUC 0.75, χ² 3.8

## Visualisations

- `research/outputs/12_quant_deep_dive/_MASTER_DASHBOARD.html` — 9 panels cross-city + 3D behavior clusters
- `research/outputs/12_quant_deep_dive/<slug>_report.md` — 38 reports détaillés
- `research/outputs/12_quant_deep_dive/viz_<slug>/` — 38 × 3 viz 3D = 114 HTML

## Related

- [[../_MOC|Polymarket Hub MOC]]
- [[../odds-trajectories-v2-findings|Odds Trajectories v2 (global)]]
- [[../per-city-deep-dive/_MOC|Per-city Deep Dive baseline]]
- [[../STATE-HANDOFF|State Handoff]]
- [[../city-optimization|City optimization log]]
- [[../tier-s-v2-hedge-fund-gates|Tier S v2 gates]]