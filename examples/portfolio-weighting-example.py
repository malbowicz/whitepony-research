"""Educational portfolio weighting example with synthetic sleeve returns."""

from __future__ import annotations

import math
import random


def stdev(values: list[float]) -> float:
    mean = sum(values) / len(values)
    variance = sum((value - mean) ** 2 for value in values) / (len(values) - 1)
    return math.sqrt(variance)


def capped_inverse_vol_weights(sleeve_returns: dict[str, list[float]], cap: float) -> dict[str, float]:
    raw = {}
    for name, returns in sleeve_returns.items():
        vol = stdev(returns)
        raw[name] = 0.0 if vol == 0.0 else 1.0 / vol

    total = sum(raw.values())
    weights = {name: value / total for name, value in raw.items()}

    capped = {name: min(weight, cap) for name, weight in weights.items()}
    leftover = 1.0 - sum(capped.values())
    uncapped = [name for name, weight in weights.items() if weight < cap]

    if leftover > 0.0 and uncapped:
        uncapped_total = sum(weights[name] for name in uncapped)
        for name in uncapped:
            capped[name] += leftover * weights[name] / uncapped_total

    total_after = sum(capped.values())
    return {name: weight / total_after for name, weight in capped.items()}


def main() -> None:
    random.seed(11)
    sleeves = {
        "momentum_style": [random.gauss(0.0020, 0.028) for _ in range(104)],
        "reversal_style": [random.gauss(0.0012, 0.020) for _ in range(104)],
        "quality_style": [random.gauss(0.0015, 0.018) for _ in range(104)],
        "defensive_style": [random.gauss(0.0008, 0.012) for _ in range(104)],
    }

    weights = capped_inverse_vol_weights(sleeves, cap=0.40)

    print("Synthetic capped inverse-volatility weights")
    for name, weight in sorted(weights.items()):
        print(f"{name}: {weight:.1%}")
    print("Note: educational example only; not a trading recommendation.")


if __name__ == "__main__":
    main()
