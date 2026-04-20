# Calibration report — 2026-04-20

Scope: last 14 days

## Global metrics

- **n** : 1113
- **brier** : 0.0816
- **log_loss** : 0.5719
- **ece** : 0.0576
- **wr_realized** : 0.8176
- **wr_expected** : 0.8417
- **pnl_realized_usdc** : 13324.69

### Reliability diagram

| bucket      |   n |   est_prob_avg |   realized_wr |   miscal | enough   |
|:------------|----:|---------------:|--------------:|---------:|:---------|
| [0.00,0.10) |   6 |          0.082 |         0     |   -0.082 | yes      |
| [0.10,0.20) |  87 |          0.164 |         0.023 |   -0.141 | yes      |
| [0.20,0.30) |  17 |          0.243 |         0     |   -0.243 | yes      |
| [0.30,0.40) |  29 |          0.323 |         0.759 |    0.436 | yes      |
| [0.40,0.50) |  26 |          0.419 |         0.577 |    0.158 | yes      |
| [0.60,0.70) |  11 |          0.692 |         0     |   -0.692 | yes      |
| [0.70,0.80) |   9 |          0.791 |         1     |    0.209 | yes      |
| [0.80,0.90) | 189 |          0.866 |         0.831 |   -0.036 | yes      |
| [0.90,1.00) | 739 |          0.973 |         0.954 |   -0.019 | yes      |

## Per alpha_type

| alpha_type      |    n |   wr_real |   wr_exp |   brier |   log_loss |    ece |   pnl_usdc |
|:----------------|-----:|----------:|---------:|--------:|-----------:|-------:|-----------:|
| CONFIRMED_NO    |   55 |     1     |    1     |  0      |     0      | 0      |     100.06 |
| CONFIRMED_YES   |   31 |     0     |    1     |  1      |    13.8155 | 1      |    -443.88 |
| MODEL_VS_MARKET | 1027 |     0.833 |    0.828 |  0.0583 |     0.2028 | 0.0649 |   13668.5  |

## ⚠️ Flagged (ECE > 0.12)

| alpha_type    |   n |   wr_real |   wr_exp |   ece |
|:--------------|----:|----------:|---------:|------:|
| CONFIRMED_YES |  31 |         0 |        1 |     1 |

Actionable: if ECE stays high across 7 days of sliding window and N > 30, reduce Kelly sizing for that pocket or disable via drift_monitor kill switch.

## Related

- [[_MOC|Hub]]
- [[TODO-pending]]
- [[STATE-HANDOFF]]