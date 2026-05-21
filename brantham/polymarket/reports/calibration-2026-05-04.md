# Calibration report — 2026-05-04

Scope: last 14 days

## Global metrics

- **n** : 1084
- **brier** : 0.137
- **log_loss** : 1.5604
- **ece** : 0.1375
- **wr_realized** : 0.81
- **wr_expected** : 0.9419
- **pnl_realized_usdc** : -745.86

### Reliability diagram

| bucket      |   n |   est_prob_avg |   realized_wr |   miscal | enough   |
|:------------|----:|---------------:|--------------:|---------:|:---------|
| [0.00,0.10) |   3 |          0.059 |         0     |   -0.059 | low-n    |
| [0.10,0.20) |   1 |          0.145 |         0     |   -0.145 | low-n    |
| [0.20,0.30) |  15 |          0.242 |         0     |   -0.242 | yes      |
| [0.40,0.50) |  48 |          0.424 |         0     |   -0.424 | yes      |
| [0.70,0.80) |   9 |          0.736 |         1     |    0.264 | yes      |
| [0.80,0.90) | 102 |          0.866 |         0.873 |    0.006 | yes      |
| [0.90,1.00) | 906 |          0.995 |         0.861 |   -0.134 | yes      |

## Per alpha_type

| alpha_type      |   n |   wr_real |   wr_exp |   brier |   log_loss |    ece |   pnl_usdc |
|:----------------|----:|----------:|---------:|--------:|-----------:|-------:|-----------:|
| CONFIRMED_NO    | 710 |     0.845 |    1     |  0.1549 |     2.1404 | 0.1549 |     -14.22 |
| MODEL_VS_MARKET | 374 |     0.743 |    0.832 |  0.1029 |     0.4591 | 0.1043 |    -731.63 |

## ⚠️ Flagged (ECE > 0.12)

| alpha_type   |   n |   wr_real |   wr_exp |    ece |
|:-------------|----:|----------:|---------:|-------:|
| CONFIRMED_NO | 710 |     0.845 |        1 | 0.1549 |

Actionable: if ECE stays high across 7 days of sliding window and N > 30, reduce Kelly sizing for that pocket or disable via drift_monitor kill switch.

## Related

- [[brantham/polymarket/_MOC|Hub]]
- [[TODO-pending]]
- [[STATE-HANDOFF]]