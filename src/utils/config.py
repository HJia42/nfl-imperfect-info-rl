from pydantic import BaseModel
from typing import List


class GameConfig(BaseModel):
    total_states: int = 48
    offense_actions: List[str] = [
        "InsideRun",
        "OutsideRun",
        "Quick",
        "Intermediate",
        "Deep",
    ]
    defense_actions: List[str] = [
        "TwoHigh-Light",
        "OneHigh-Light",
        "OneHigh-Blitz",
        "TwoHigh-Blitz",
    ]
    # Yardline measured from own goal line [1..99]
    # Opp35 ≈ own 65
    field_goal_min_yardline: int = 65


DEFAULT_CONFIG = GameConfig()

