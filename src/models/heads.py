from enum import Enum
from typing import List


class OffenseAction(str, Enum):
    InsideRun = "InsideRun"
    OutsideRun = "OutsideRun"
    Quick = "Quick"
    Intermediate = "Intermediate"
    Deep = "Deep"


class DefenseAction(str, Enum):
    TwoHigh_Light = "TwoHigh-Light"
    OneHigh_Light = "OneHigh-Light"
    OneHigh_Blitz = "OneHigh-Blitz"
    TwoHigh_Blitz = "TwoHigh-Blitz"


def list_offense_actions() -> List[str]:
    return [a.value for a in OffenseAction]


def list_defense_actions() -> List[str]:
    return [a.value for a in DefenseAction]

