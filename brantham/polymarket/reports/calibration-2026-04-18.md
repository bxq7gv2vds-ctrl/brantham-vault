# Calibration report — 2026-04-18

Scope: last 14 days

## Global metrics

- **n** : 217
- **brier** : 0.0782
- **log_loss** : 0.9552
- **ece** : 0.0587
- **wr_realized** : 0.8387
- **wr_expected** : 0.887
- **pnl_realized_usdc** : 915.14

### Reliability diagram

| bucket      |   n |   est_prob_avg |   realized_wr |   miscal | enough   |
|:------------|----:|---------------:|--------------:|---------:|:---------|
| [0.00,0.10) |   4 |          0.086 |         0     |   -0.086 | low-n    |
| [0.10,0.20) |  17 |          0.125 |         0.118 |   -0.008 | yes      |
| [0.20,0.30) |   1 |          0.292 |         0     |   -0.292 | low-n    |
| [0.70,0.80) |   2 |          0.783 |         1     |    0.217 | low-n    |
| [0.80,0.90) |  15 |          0.887 |         0.933 |    0.046 | yes      |
| [0.90,1.00) | 178 |          0.982 |         0.921 |   -0.061 | yes      |

## Per alpha_type

| alpha_type      |   n |   wr_real |   wr_exp |   brier |   log_loss |    ece |   pnl_usdc |
|:----------------|----:|----------:|---------:|--------:|-----------:|-------:|-----------:|
| CONFIRMED_NO    |  14 |     1     |     1    |  0      |     0      | 0      |      28.16 |
| CONFIRMED_YES   |  14 |     0     |     1    |  1      |    13.8155 | 1      |    -186.78 |
| MODEL_VS_MARKET | 189 |     0.889 |     0.87 |  0.0158 |     0.0734 | 0.0267 |    1073.76 |

## ⚠️ Flagged (ECE > 0.12)

| alpha_type    |   n |   wr_real |   wr_exp |   ece |
|:--------------|----:|----------:|---------:|------:|
| CONFIRMED_YES |  14 |         0 |        1 |     1 |

Actionable: if ECE stays high across 7 days of sliding window and N > 30, reduce Kelly sizing for that pocket or disable via drift_monitor kill switch.

## Related

- [[_MOC|Hub]]
- [[TODO-pending]]
- [[STATE-HANDOFF]]