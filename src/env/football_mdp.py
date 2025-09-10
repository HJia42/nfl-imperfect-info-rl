from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple

import numpy as np

from ..utils.config import DEFAULT_CONFIG


@dataclass
class State:
    down: int = 1  # 1..4
    yards_to_go: int = 10
    yardline: int = 25  # from own GL [1..99]


class FootballMDP:
    """Tiny abstracted MDP for playcalling.

    - 48 total abstract states (we don't enumerate all here;
      `total_states` exposes the count).
    - Offense has 5 actions; defense has 4.
    - Reward is EPA delta from a small table.
    - Minimal deterministic stub to support tests and scaffolding.
    """

    def __init__(self):
        self.config = DEFAULT_CONFIG
        # 5 x 4 EPA deltas (rows: offense actions, cols: defense actions)
        # These numbers are arbitrary but plausible-ish signs.
        self._epa_table: np.ndarray = np.array(
            [
                [0.05, 0.10, -0.10, -0.05],  # InsideRun
                [0.03, 0.08, -0.12, -0.04],  # OutsideRun
                [0.06, -0.02, -0.15, 0.01],  # Quick
                [0.10, 0.05, -0.20, -0.05],  # Intermediate
                [0.20, -0.10, -0.30, -0.15],  # Deep
            ]
        )
        self._off_index: Dict[str, int] = {
            name: i for i, name in enumerate(self.config.offense_actions)
        }
        self._def_index: Dict[str, int] = {
            name: i for i, name in enumerate(self.config.defense_actions)
        }

    @property
    def total_states(self) -> int:
        return self.config.total_states

    def initial_state(self) -> State:
        return State()

    def step(
        self,
        state: State,
        offense_action: str,
        defense_action: str,
    ) -> Tuple[State, float, Dict]:
        oi = self._off_index[offense_action]
        di = self._def_index[defense_action]
        reward = float(self._epa_table[oi, di])
        # Minimal deterministic next state: update if reward is positive
        next_state = State(
            down=(1 if reward > 0 and state.down == 1 else min(4, state.down + 1)),
            yards_to_go=max(1, state.yards_to_go - (5 if reward > 0 else 0)),
            yardline=min(99, state.yardline + (3 if reward > 0 else 0)),
        )
        info = {"epa": reward}
        return next_state, reward, info
