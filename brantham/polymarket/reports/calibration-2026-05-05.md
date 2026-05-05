# Calibration report — 2026-05-05

Scope: last 14 days

## Global metrics

- **n** : 342
- **brier** : 0.1229
- **log_loss** : 1.2413
- **ece** : 0.1593
- **wr_realized** : 0.7193
- **wr_expected** : 0.862
- **pnl_realized_usdc** : -1201.86

### Reliability diagram

| bucket      |   n |   est_prob_avg |   realized_wr |   miscal | enough   |
|:------------|----:|---------------:|--------------:|---------:|:---------|
| [0.00,0.10) |   2 |          0.064 |         0     |   -0.064 | low-n    |
| [0.10,0.20) |   1 |          0.145 |         0     |   -0.145 | low-n    |
| [0.20,0.30) |  13 |          0.242 |         0     |   -0.242 | yes      |
| [0.40,0.50) |  48 |          0.424 |         0     |   -0.424 | yes      |
| [0.70,0.80) |   2 |          0.753 |         1     |    0.247 | low-n    |
| [0.80,0.90) |  17 |          0.862 |         1     |    0.138 | yes      |
| [0.90,1.00) | 259 |          0.984 |         0.876 |   -0.108 | yes      |

## Per alpha_type

| alpha_type      |   n |   wr_real |   wr_exp |   brier |   log_loss |    ece |   pnl_usdc |
|:----------------|----:|----------:|---------:|--------:|-----------:|-------:|-----------:|
| CONFIRMED_NO    |  86 |     0.698 |    1     |  0.3023 |     4.1768 | 0.3023 |    -221.48 |
| MODEL_VS_MARKET | 256 |     0.727 |    0.816 |  0.0626 |     0.2551 | 0.1112 |    -980.38 |

## ⚠️ Flagged (ECE > 0.12)

| alpha_type   |   n |   wr_real |   wr_exp |    ece |
|:-------------|----:|----------:|---------:|-------:|
| CONFIRMED_NO |  86 |     0.698 |        1 | 0.3023 |

Actionable: if ECE stays high across 7 days of sliding window and N > 30, reduce Kelly sizing for that pocket or disable via drift_monitor kill switch.

## Related

- [[_MOC|Hub]]
- [[TODO-pending]]
- [[STATE-HANDOFF]]