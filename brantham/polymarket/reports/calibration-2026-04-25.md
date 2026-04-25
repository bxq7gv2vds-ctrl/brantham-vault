# Calibration report — 2026-04-25

Scope: last 14 days

## Global metrics

- **n** : 2627
- **brier** : 0.101
- **log_loss** : 0.9234
- **ece** : 0.0801
- **wr_realized** : 0.8112
- **wr_expected** : 0.8743
- **pnl_realized_usdc** : 17685.81

### Reliability diagram

| bucket      |    n |   est_prob_avg |   realized_wr |   miscal | enough   |
|:------------|-----:|---------------:|--------------:|---------:|:---------|
| [0.00,0.10) |   19 |          0.08  |         0     |   -0.08  | yes      |
| [0.10,0.20) |  142 |          0.161 |         0.099 |   -0.062 | yes      |
| [0.20,0.30) |   37 |          0.242 |         0     |   -0.242 | yes      |
| [0.30,0.40) |   34 |          0.324 |         0.735 |    0.412 | yes      |
| [0.40,0.50) |   92 |          0.427 |         0.163 |   -0.264 | yes      |
| [0.50,0.60) |    1 |          0.572 |         0     |   -0.572 | low-n    |
| [0.60,0.70) |   11 |          0.692 |         0     |   -0.692 | yes      |
| [0.70,0.80) |   24 |          0.759 |         0.875 |    0.116 | yes      |
| [0.80,0.90) |  373 |          0.864 |         0.879 |    0.015 | yes      |
| [0.90,1.00) | 1894 |          0.984 |         0.912 |   -0.072 | yes      |

## Per alpha_type

| alpha_type      |    n |   wr_real |   wr_exp |   brier |   log_loss |    ece |   pnl_usdc |
|:----------------|-----:|----------:|---------:|--------:|-----------:|-------:|-----------:|
| CONFIRMED_NO    |  765 |     0.856 |     1    |  0.1438 |     1.9865 | 0.1438 |      85.84 |
| CONFIRMED_YES   |   31 |     0     |     1    |  1      |    13.8155 | 1      |    -443.88 |
| MODEL_VS_MARKET | 1831 |     0.806 |     0.82 |  0.0679 |     0.261  | 0.043  |   18043.8  |

## ⚠️ Flagged (ECE > 0.12)

| alpha_type    |   n |   wr_real |   wr_exp |    ece |
|:--------------|----:|----------:|---------:|-------:|
| CONFIRMED_NO  | 765 |     0.856 |        1 | 0.1438 |
| CONFIRMED_YES |  31 |     0     |        1 | 1      |

Actionable: if ECE stays high across 7 days of sliding window and N > 30, reduce Kelly sizing for that pocket or disable via drift_monitor kill switch.

## Related

- [[_MOC|Hub]]
- [[TODO-pending]]
- [[STATE-HANDOFF]]