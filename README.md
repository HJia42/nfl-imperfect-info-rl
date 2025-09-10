# NFL Imperfect-Information RL

A small two-player imperfect-information NFL playcalling game environment and utilities. The offense selects among five play families, the defense selects among four structures. Rewards are EPA deltas, with a simple 4th-down special teams rule: on 4th down, a KICK is a field goal attempt if the ball is at or beyond the opponent's 35 (yardline ≥ Opp35), otherwise a punt.

This repo is a tiny scaffold intended for experimentation with simple solvers (LP-based Nash, policy iteration) and light model components.

## Quickstart

- Python 3.11
- Install: `make install`
- Lint: `make lint`
- Test: `make test`

## Layout

- `src/`
  - `data/` – ingest and simple binning helpers
  - `models/` – action heads, calibration, defense effects, special teams rule
  - `env/` – the football MDP stub (`FootballMDP`)
  - `solve/` – simple solvers (LP Nash stub, policy iteration stub)
  - `eval/` – simple EP curve checks, OPE placeholder
  - `utils/` – config, checks, logging helpers
- `configs/` – small YAML configs for bins and defense effects
- `tests/` – very lightweight tests for basic functionality

## Game sketch

- States: 48 total (abstracted)
- Offense actions: {InsideRun, OutsideRun, Quick, Intermediate, Deep}
- Defense actions: {TwoHigh-Light, OneHigh-Light, OneHigh-Blitz, TwoHigh-Blitz}
- Reward: EPA delta via a small payoff table
- 4th-down: `decide_kick(yardline)` returns `FG` if yardline ≥ Opp35, else `PUNT`

This is not meant to be a realistic simulator; it’s a compact sandbox for imperfect-information algorithms.

