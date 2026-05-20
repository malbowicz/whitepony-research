# Public System Overview

This is a public sketch, not the private system architecture.

## Flow

```text
Research ideas
  -> candidate signal families
  -> validation checks
  -> sleeve-level return streams
  -> portfolio construction
  -> cost, lag, and drawdown tests
  -> reproducibility notes
  -> delayed aggregate reporting
```

## Public Description

| Component | Public Description |
|---|---|
| Signal research | Candidate families are described by category, not by formula. |
| Validation | Candidates are checked under different timing, cost, and sample assumptions. |
| Portfolio construction | Sleeves are combined while watching redundancy, drawdown, and turnover. |
| Reproducibility | Data vintages, retraining choices, and evaluation windows are tracked. |
| Public logging | Any public record should be delayed and aggregate. |

## Boundary

The public repo does not include:

- private production code;
- current model artifacts;
- broker or execution code;
- exact signal formulas;
- proprietary routing rules;
- current holdings or targets.

TODO(public-review): Add a polished architecture diagram after publication review.
