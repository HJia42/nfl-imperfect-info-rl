from src.env.football_mdp import FootballMDP
from src.models.special_teams import decide_kick


def test_env_basic():
    env = FootballMDP()
    assert env.total_states == 48
    s0 = env.initial_state()
    s1, r, info = env.step(s0, "InsideRun", "TwoHigh-Light")
    assert isinstance(r, float)
    assert "epa" in info
    assert s1.yardline >= s0.yardline


def test_special_teams_rule():
    assert decide_kick(30) == "PUNT"
    assert decide_kick(65) == "FG"
    assert decide_kick(80) == "FG"

