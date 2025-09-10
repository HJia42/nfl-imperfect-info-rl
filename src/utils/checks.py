from typing import Sequence


def is_probability_distribution(x: Sequence[float], tol: float = 1e-6) -> bool:
    if not x:
        return False
    if any(v < -tol for v in x):
        return False
    s = float(sum(x))
    return abs(s - 1.0) <= tol

