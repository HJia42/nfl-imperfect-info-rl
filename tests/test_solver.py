import numpy as np

from src.env.football_mdp import FootballMDP
from src.solve.nash_lp import compute_nash_by_lp
from src.solve.policy_iteration import policy_iteration


def test_nash_lp_uniform():
    payoff = np.zeros((5, 4))
    pi = compute_nash_by_lp(payoff)
    assert pi.shape == (5,)
    assert np.isclose(pi.sum(), 1.0)
    assert np.allclose(pi, 0.2)


def test_policy_iteration_shape():
    env = FootballMDP()
    pi = policy_iteration(env)
    assert pi.shape == (5,)
    assert np.isclose(pi.sum(), 1.0)
    assert pi[0] == 1.0
