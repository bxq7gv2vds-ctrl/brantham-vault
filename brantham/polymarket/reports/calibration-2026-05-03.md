# Calibration report — 2026-05-03

Scope: last 14 days

## Global metrics

- **n** : 1458
- **brier** : 0.1126
- **log_loss** : 1.2016
- **ece** : 0.1115
- **wr_realized** : 0.81
- **wr_expected** : 0.9006
- **pnl_realized_usdc** : 4250.12

### Reliability diagram

| bucket      |    n |   est_prob_avg |   realized_wr |   miscal | enough   |
|:------------|-----:|---------------:|--------------:|---------:|:---------|
| [0.00,0.10) |   13 |          0.08  |         0     |   -0.08  | yes      |
| [0.10,0.20) |   55 |          0.156 |         0.218 |    0.062 | yes      |
| [0.20,0.30) |   20 |          0.242 |         0     |   -0.242 | yes      |
| [0.30,0.40) |    2 |          0.364 |         0     |   -0.364 | low-n    |
| [0.40,0.50) |   58 |          0.422 |         0     |   -0.422 | yes      |
| [0.70,0.80) |   14 |          0.741 |         0.857 |    0.116 | yes      |
| [0.80,0.90) |  169 |          0.863 |         0.923 |    0.06  | yes      |
| [0.90,1.00) | 1127 |          0.991 |         0.888 |   -0.103 | yes      |

## Per alpha_type

| alpha_type      |   n |   wr_real |   wr_exp |   brier |   log_loss |    ece |   pnl_usdc |
|:----------------|----:|----------:|---------:|--------:|-----------:|-------:|-----------:|
| CONFIRMED_NO    | 710 |     0.845 |    1     |  0.1549 |     2.1404 | 0.1549 |     -14.22 |
| MODEL_VS_MARKET | 748 |     0.777 |    0.806 |  0.0724 |     0.3104 | 0.0703 |    4264.34 |

## ⚠️ Flagged (ECE > 0.12)

| alpha_type   |   n |   wr_real |   wr_exp |    ece |
|:-------------|----:|----------:|---------:|-------:|
| CONFIRMED_NO | 710 |     0.845 |        1 | 0.1549 |

Actionable: if ECE stays high across 7 days of sliding window and N > 30, reduce Kelly sizing for that pocket or disable via drift_monitor kill switch.

## Related

- [[_MOC|Hub]]
- [[TODO-pending]]
- [[STATE-HANDOFF]]