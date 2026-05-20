# Portfolio Construction

## Question

How should a research portfolio combine multiple candidate signal families when the strongest standalone signals may be redundant, expensive to trade, or unstable across regimes?

## Current Draft

This paper is about combining signal sleeves after they have been tested individually. The main point is simple: the best standalone signal is not always the best portfolio ingredient.

The public version should stay at the process level:

- start with sleeves that have comparable weekly return histories;
- compare them over a common evaluation window;
- check whether top sleeves are just variations of the same trade;
- look at turnover, costs, lag, and drawdown;
- compare combined portfolios with individual sleeves and simple baselines.

## What I Can Say Publicly

- some high-performing sleeves are redundant;
- lower-correlation sleeves can matter even with moderate standalone metrics;
- cost and lag assumptions can change which portfolios remain plausible;
- allocation rules should not be judged only by headline Sharpe.

## TODO

Add reviewed charts to `charts/portfolio-construction/`.

Useful candidates:

- standalone sleeve equity curves;
- sleeve correlation heatmap;
- combined-portfolio equity and drawdown charts;
- cost sensitivity;
- lag sensitivity;
- rolling correlation checks.

## Do Not Publish

- private weighting equations;
- raw weekly return parquet files;
- current or target holdings;
- private source paths;
- alpha formulas;
- production execution code.
