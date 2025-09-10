import numpy as np


def compute_nash_by_lp(payoff: np.ndarray) -> np.ndarray:
    """Very small placeholder for a zero-sum offense strategy.

    Returns a uniform distribution over offense actions. Shape: (n_offense,).
    """
    n_offense = payoff.shape[0]
    if n_offense == 0:
        return np.array([])
    return np.full(n_offense, 1.0 / n_offense)

