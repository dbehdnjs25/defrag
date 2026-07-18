"""Tests for the fixed-timestep accumulator (pure logic, no pygame)."""

from __future__ import annotations

import pytest

from game.core.loop import FixedTimestep


def test_accumulates_exact_steps() -> None:
    ts = FixedTimestep(dt=0.1, max_frame_time=1.0)
    assert ts.steps(0.25) == 2  # 0.25 -> two 0.1 steps, 0.05 left over
    assert ts.accumulator == pytest.approx(0.05)


def test_leftover_carries_into_next_frame() -> None:
    ts = FixedTimestep(dt=0.1, max_frame_time=1.0)
    ts.steps(0.05)  # 0 steps, 0.05 banked
    assert ts.steps(0.05) == 1  # 0.05 + 0.05 -> one step


def test_frame_time_clamped_prevents_spiral_of_death() -> None:
    ts = FixedTimestep(dt=0.1, max_frame_time=0.35)
    # A 10s hang must not produce ~100 steps; it's clamped to 0.35 -> 3 steps.
    assert ts.steps(10.0) == 3


def test_negative_frame_time_yields_no_steps() -> None:
    ts = FixedTimestep(dt=0.1, max_frame_time=1.0)
    assert ts.steps(-5.0) == 0


def test_alpha_is_normalised_fraction() -> None:
    ts = FixedTimestep(dt=0.1, max_frame_time=1.0)
    ts.steps(0.15)  # one step, 0.05 remainder
    assert ts.alpha == pytest.approx(0.5)


def test_non_positive_dt_rejected() -> None:
    with pytest.raises(ValueError):
        FixedTimestep(dt=0.0)
