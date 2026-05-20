"""Educational cost and lag stress example with synthetic signals."""

from __future__ import annotations

import random


def apply_costs(returns: list[float], turnover: list[float], cost_bps: float) -> list[float]:
    cost_rate = cost_bps / 10_000.0
    return [ret - turn * cost_rate for ret, turn in zip(returns, turnover)]


def lag_returns(returns: list[float], weeks: int) -> list[float]:
    if weeks <= 0:
        return returns[:]
    return [0.0] * weeks + returns[:-weeks]


def total_return(returns: list[float]) -> float:
    equity = 1.0
    for value in returns:
        equity *= 1.0 + value
    return equity - 1.0


def main() -> None:
    random.seed(23)
    base_returns = [random.gauss(0.0020, 0.020) for _ in range(156)]
    synthetic_turnover = [min(1.0, abs(random.gauss(0.20, 0.08))) for _ in range(156)]

    scenarios = {
        "base": base_returns,
        "cost_10bps": apply_costs(base_returns, synthetic_turnover, cost_bps=10.0),
        "cost_25bps": apply_costs(base_returns, synthetic_turnover, cost_bps=25.0),
        "lag_1w": lag_returns(base_returns, weeks=1),
        "lag_2w": lag_returns(base_returns, weeks=2),
    }

    print("Synthetic stress scenarios")
    for name, returns in scenarios.items():
        print(f"{name}: total_return={total_return(returns):.2%}")
    print("Note: synthetic stress logic only; not production research code.")


if __name__ == "__main__":
    main()
