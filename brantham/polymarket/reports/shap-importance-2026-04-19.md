---
name: SHAP Feature Importance
description: Global mean |SHAP| per feature across XGB models
generated: 2026-04-19T19:16:17.429240+00:00
type: report
---

# SHAP feature importance

## Regional xgb_postproc

| Region | Top-5 features |
|---|---|
| US_EAST | t_yesterday (0.083), lat (0.042), ens_skew (0.038), sin_doy (0.038), ens_mean (0.029) |
| US_WEST | lat (0.275), ens_std (0.047), ens_spread (0.040), t_yday_minus_ens (0.038), sin_doy (0.035) |
| EU_WEST | t_yesterday (0.071), sin_doy (0.053), lon (0.045), ens_skew (0.025), month (0.024) |
| EU_CENTRAL | sin_doy (0.081), ens_mean (0.079), ens_skew (0.068), t_yday_minus_ens (0.050), t_yesterday (0.039) |
| EU_EAST | lat (0.143), ens_skew (0.069), sin_doy (0.053), ens_std (0.052), ens_spread (0.047) |
| CN | lat (0.255), lon (0.198), t_yday_minus_ens (0.117), ens_mean (0.106), sin_doy (0.055) |
| JP_KR | lat (0.865), cos_doy (0.448), ens_spread (0.361), ens_std (0.202), sin_doy (0.181) |
| TW_SEA | lon (0.442), t_yesterday (0.093), sin_doy (0.079), lat (0.076), t_yday_minus_ens (0.051) |
| IN_ME | lon (0.184), sin_doy (0.117), ens_mean (0.045), lat (0.038), cos_doy (0.029) |
| LATAM | t_yday_minus_ens (0.090), ens_std (0.069), cos_doy (0.066), lon (0.048), ens_skew (0.045) |
| OCEANIA | sin_doy (0.008), cos_doy (0.004), ens_std (0.003), t_today_so_far (0.003), t_yday_minus_ens (0.002) |

## Per-station (selected cities)

**KLGA** : t_lag_1d (0.162), neighbour_0_ens_mean_c (0.106), ens_spread (0.080), neighbour_1_ens_mean_c (0.056), sin_doy (0.031)

**KORD** : neighbour_0_ens_mean_c (0.087), ens_mean (0.038), t_lag_7d_anom_c (0.029), t_lag_3d_anom_c (0.021), t_lag_1d_anom_c (0.018)

**KDEN** : t_lag_3d (0.119), ens_std (0.099), climo_std_c (0.082), ens_mean (0.077), sin_doy (0.059)

**KLAX** : anomaly_z (0.241), sin_doy (0.102), t_lag_7d_anom_c (0.064), ens_skew (0.037), ens_mean (0.033)

**KMIA** : sin_doy (0.041), t_lag_1d (0.018), ens_mean (0.011), t_lag_1d_anom_c (0.009), anomaly_z (0.007)

**LFPG** : neighbour_1_ens_mean_c (0.023), sin_doy (0.022), cos_doy (0.020), t_lag_7d (0.019), ens_mean (0.013)

**EGLC** : sin_doy (0.113), t_lag_1d (0.108), climo_std_c (0.066), ens_std (0.023), ens_spread (0.017)

**EFHK** : sin_doy (0.121), cos_doy (0.097), neighbour_1_ens_mean_c (0.080), t_lag_3d_anom_c (0.051), neighbour_0_ens_mean_c (0.045)

**ZBAA** : neighbour_0_ens_mean_c (0.079), anomaly_z (0.015), anomaly_c (0.015), ens_std (0.010), neighbour_1_ens_mean_c (0.008)

**RJTT** : neighbour_1_ens_mean_c (0.078), anomaly_c (0.046), ens_mean (0.041), sin_doy (0.036), t_lag_1d_anom_c (0.035)

**WMKK** : ens_spread (0.118), sin_doy (0.113), ens_std (0.076), ens_skew (0.064), t_lag_1d (0.053)
## Related
## Related
