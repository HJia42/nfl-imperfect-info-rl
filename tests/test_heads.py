from src.models.heads import (
    DefenseAction,
    OffenseAction,
    list_defense_actions,
    list_offense_actions,
)


def test_action_sets():
    off = list_offense_actions()
    deff = list_defense_actions()
    assert len(off) == 5
    assert len(deff) == 4
    assert OffenseAction.Deep.value in off
    assert DefenseAction.TwoHigh_Blitz.value in deff
