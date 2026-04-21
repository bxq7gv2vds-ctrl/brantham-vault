# Calibration report — 2026-04-21

Scope: last 14 days

## Global metrics

- **n** : 1583
- **brier** : 0.0743
- **log_loss** : 0.4669
- **ece** : 0.0379
- **wr_realized** : 0.8193
- **wr_expected** : 0.8328
- **pnl_realized_usdc** : 18631.62

### Reliability diagram

| bucket      |    n |   est_prob_avg |   realized_wr |   miscal | enough   |
|:------------|-----:|---------------:|--------------:|---------:|:---------|
| [0.00,0.10) |   16 |          0.084 |         0     |   -0.084 | yes      |
| [0.10,0.20) |  141 |          0.161 |         0.099 |   -0.062 | yes      |
| [0.20,0.30) |   17 |          0.243 |         0     |   -0.243 | yes      |
| [0.30,0.40) |   34 |          0.324 |         0.735 |    0.412 | yes      |
| [0.40,0.50) |   44 |          0.43  |         0.341 |   -0.089 | yes      |
| [0.50,0.60) |    1 |          0.572 |         0     |   -0.572 | low-n    |
| [0.60,0.70) |   11 |          0.692 |         0     |   -0.692 | yes      |
| [0.70,0.80) |   15 |          0.773 |         0.8   |    0.027 | yes      |
| [0.80,0.90) |  271 |          0.864 |         0.882 |    0.018 | yes      |
| [0.90,1.00) | 1033 |          0.974 |         0.96  |   -0.014 | yes      |

## Per alpha_type

| alpha_type      |    n |   wr_real |   wr_exp |   brier |   log_loss |    ece |   pnl_usdc |
|:----------------|-----:|----------:|---------:|--------:|-----------:|-------:|-----------:|
| CONFIRMED_NO    |   55 |      1    |    1     |  0      |     0      | 0      |     100.06 |
| CONFIRMED_YES   |   31 |      0    |    1     |  1      |    13.8155 | 1      |    -443.88 |
| MODEL_VS_MARKET | 1497 |      0.83 |    0.823 |  0.0579 |     0.2076 | 0.0416 |   18975.4  |

## ⚠️ Flagged (ECE > 0.12)

| alpha_type    |   n |   wr_real |   wr_exp |   ece |
|:--------------|----:|----------:|---------:|------:|
| CONFIRMED_YES |  31 |         0 |        1 |     1 |

Actionable: if ECE stays high across 7 days of sliding window and N > 30, reduce Kelly sizing for that pocket or disable via drift_monitor kill switch.

## Related

- [[_MOC|Hub]]
- [[TODO-pending]]
- [[STATE-HANDOFF]]