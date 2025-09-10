import numpy as np


def calc_ope(rewards: np.ndarray, weights: np.ndarray | None = None) -> float:
    if weights is None:
        weights = np.ones_like(rewards)
    weights = weights / (weights.sum() if weights.sum() != 0 else 1.0)
    return float((rewards * weights).sum())

