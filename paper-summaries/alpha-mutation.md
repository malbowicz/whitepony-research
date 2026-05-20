# Alpha Mutation

## Question

Can controlled signal variants be used to find failure modes instead of just searching for the best-looking backtest?

## Current Draft

This paper is about stress testing variants of signal ideas. The important result is not that some variants look good. The important result is that many variants fail, and the failures are informative.

The public version should emphasize:

- how many variants are rejected;
- whether apparent winners survive cost, lag, universe, and subperiod checks;
- whether survivors are actually different from each other;
- why multiple-testing controls are necessary before making strong claims.

## Method Sketch

1. Start with economically interpretable signal families.
2. Generate controlled variants of broad design choices, without publishing private operators.
3. Apply stress tests before treating any result as meaningful.
4. Track rejected candidates and failure modes.
5. Treat surviving variants as provisional until forward validation is stronger.

## TODO

Add reviewed charts to `charts/alpha-mutation/`

Useful candidates:

- mutation survival funnel;
- distribution of mutation Sharpe values;
- turnover versus Sharpe scatter;
- drawdown versus Sharpe scatter;
- failure-category chart;
- correlation heatmap of surviving mutations;
- rolling performance of representative survivors.

## Missing Before Strong Claims

- formal multiple-testing controls;
- stronger walk-forward validation;
- deflated Sharpe or related overfitting diagnostics;
- capacity analysis;
- clearer separation between exploration and confirmation.

## Do Not Publish

- private mutation operators or parameters;
- formula appendices marked restricted;
- raw result tables that expose private signal names or features;
- code for the private mutation engine.
