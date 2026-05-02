# Calibration report — 2026-05-02

Scope: last 14 days

## Global metrics

- **n** : 1729
- **brier** : 0.1114
- **log_loss** : 1.1199
- **ece** : 0.1064
- **wr_realized** : 0.8045
- **wr_expected** : 0.8931
- **pnl_realized_usdc** : 4271.58

### Reliability diagram

| bucket      |    n |   est_prob_avg |   realized_wr |   miscal | enough   |
|:------------|-----:|---------------:|--------------:|---------:|:---------|
| [0.00,0.10) |   13 |          0.08  |         0     |   -0.08  | yes      |
| [0.10,0.20) |   64 |          0.16  |         0.188 |    0.028 | yes      |
| [0.20,0.30) |   22 |          0.24  |         0     |   -0.24  | yes      |
| [0.30,0.40) |   12 |          0.342 |         0.25  |   -0.092 | yes      |
| [0.40,0.50) |   77 |          0.427 |         0     |   -0.427 | yes      |
| [0.50,0.60) |    1 |          0.572 |         0     |   -0.572 | low-n    |
| [0.70,0.80) |   15 |          0.74  |         0.8   |    0.06  | yes      |
| [0.80,0.90) |  241 |          0.86  |         0.913 |    0.053 | yes      |
| [0.90,1.00) | 1284 |          0.99  |         0.891 |   -0.099 | yes      |

## Per alpha_type

| alpha_type      |   n |   wr_real |   wr_exp |   brier |   log_loss |    ece |   pnl_usdc |
|:----------------|----:|----------:|---------:|--------:|-----------:|-------:|-----------:|
| CONFIRMED_NO    | 737 |     0.851 |    1     |  0.1493 |     2.062  | 0.1493 |      36.13 |
| CONFIRMED_YES   |   8 |     0     |    1     |  1      |    13.8155 | 1      |    -133.49 |
| MODEL_VS_MARKET | 984 |     0.776 |    0.812 |  0.0759 |     0.3111 | 0.067  |    4368.94 |

## ⚠️ Flagged (ECE > 0.12)

| alpha_type    |   n |   wr_real |   wr_exp |    ece |
|:--------------|----:|----------:|---------:|-------:|
| CONFIRMED_NO  | 737 |     0.851 |        1 | 0.1493 |
| CONFIRMED_YES |   8 |     0     |        1 | 1      |

Actionable: if ECE stays high across 7 days of sliding window and N > 30, reduce Kelly sizing for that pocket or disable via drift_monitor kill switch.

## Related

- [[_MOC|Hub]]
- [[TODO-pending]]
- [[STATE-HANDOFF]]