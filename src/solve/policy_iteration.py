import numpy as np


def policy_iteration(env) -> np.ndarray:
    """Return a simple deterministic policy over offense actions.

    For our tiny game, return a vector that chooses the first action.
    """
    n_actions = len(env.config.offense_actions)
    pi = np.zeros(n_actions)
    if n_actions:
        pi[0] = 1.0
    return pi
