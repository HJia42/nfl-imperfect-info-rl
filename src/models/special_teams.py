from typing import Literal


def decide_kick(
    yardline: int,
    fg_min_yardline: int = 65,
) -> Literal["FG", "PUNT"]:
    """Return FG if yardline >= Opp35, else PUNT.

    Opp35 is ~65 yards from own goal line.
    """
    return "FG" if yardline >= fg_min_yardline else "PUNT"
