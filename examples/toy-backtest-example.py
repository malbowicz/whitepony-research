"""Educational toy backtest using synthetic weekly returns.

This script is intentionally simple. It does not contain private White Pony
signals, model code, execution logic, or market data.
"""

from __future__ import annotations

import math
import random


def annualized_return(weekly_returns: list[float]) -> float:
    equity = 1.0
    for value in weekly_returns:
        equity *= 1.0 + value
    years = len(weekly_returns) / 52.0
    return equity ** (1.0 / years) - 1.0


def annualized_volatility(weekly_returns: list[float]) -> float:
    mean = sum(weekly_returns) / len(weekly_returns)
    variance = sum((value - mean) ** 2 for value in weekly_returns) / (len(weekly_returns) - 1)
    return math.sqrt(variance) * math.sqrt(52.0)


def sharpe_ratio(weekly_returns: list[float]) -> float:
    vol = annualized_volatility(weekly_returns)
    if vol == 0.0:
        return 0.0
    return (sum(weekly_returns) / len(weekly_returns) * 52.0) / vol


def max_drawdown(weekly_returns: list[float]) -> float:
    equity = 1.0
    peak = 1.0
    worst = 0.0
    for value in weekly_returns:
        equity *= 1.0 + value
        peak = max(peak, equity)
        worst = min(worst, equity / peak - 1.0)
    return worst


def main() -> None:
    random.seed(7)
    weekly_returns = []
    for _ in range(156):
        market_noise = random.gauss(0.0015, 0.025)
        research_signal = random.gauss(0.0008, 0.010)
        weekly_returns.append(market_noise + research_signal)

    print("Synthetic toy backtest")
    print(f"Weeks: {len(weekly_returns)}")
    print(f"CAGR: {annualized_return(weekly_returns):.2%}")
    print(f"Volatility: {annualized_volatility(weekly_returns):.2%}")
    print(f"Sharpe: {sharpe_ratio(weekly_returns):.2f}")
    print(f"Max drawdown: {max_drawdown(weekly_returns):.2%}")
    print("Note: synthetic data only; not investment advice.")


if __name__ == "__main__":
    main()
