# Methodology

Public writeups should describe the research process, not the private implementation.

The simplified workflow is:

1. Start with candidate signal families.
2. Test them under cost, lag, universe, and subperiod assumptions.
3. Combine useful sleeves into portfolios.
4. Check turnover, correlation, drawdown, and timing.
5. Record enough artifact context to explain later changes.

## Data And Timing

The private work is organized around weekly research artifacts. Public summaries should include only:

- weekly alignment;
- out-of-sample or forward-style test windows;
- timing checks;
- aggregate date ranges after review.

Do not publish raw caches, current holdings, target files, or broker-derived records.

## Alpha Research

Alpha families should be described conceptually:

- momentum;
- reversal;
- value or quality;
- volatility or liquidity;
- sector, factor, or regime context.

Avoid exact formulas, thresholds, feature definitions, rank transforms, and private weights.

## Portfolio Construction

Public summaries can discuss:

- correlation and redundancy;
- concentration;
- turnover and costs;
- rolling performance;
- drawdown and timing tests.

Private allocation rules, exact hyperparameters, and proprietary routing logic stay out of the public repo.

## Reproducibility

Each public result should eventually have:

- a date window;
- a metric definition;
- a label: backtest, paper, delayed aggregate, or synthetic example;
- a limitation note.

TODO(public-review): Add metric definitions after final charts are selected.
