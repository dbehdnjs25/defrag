"""Tests for the Ball entity's physics (pure logic, deterministic)."""

from __future__ import annotations

import pytest

from game.entities.ball import Ball


def test_moves_by_velocity_times_dt() -> None:
    ball = Ball(x=100.0, y=100.0, vx=50.0, vy=-20.0, radius=10.0)
    ball.update(dt=2.0, width=1000, height=1000)
    assert ball.x == pytest.approx(200.0)
    assert ball.y == pytest.approx(60.0)


def test_bounces_off_left_wall_and_reverses_x() -> None:
    ball = Ball(x=5.0, y=100.0, vx=-100.0, vy=0.0, radius=10.0)
    ball.update(dt=1.0, width=500, height=500)
    assert ball.x == pytest.approx(10.0)  # clamped to the radius
    assert ball.vx > 0  # velocity reversed to point inward


def test_bounces_off_bottom_wall_and_reverses_y() -> None:
    ball = Ball(x=100.0, y=495.0, vx=0.0, vy=100.0, radius=10.0)
    ball.update(dt=1.0, width=500, height=500)
    assert ball.y == pytest.approx(490.0)
    assert ball.vy < 0


def test_stays_inside_bounds_over_many_steps() -> None:
    ball = Ball(x=250.0, y=250.0, vx=317.0, vy=-211.0, radius=8.0)
    for _ in range(1000):
        ball.update(dt=1 / 60, width=500, height=500)
        assert 8.0 <= ball.x <= 492.0
        assert 8.0 <= ball.y <= 492.0
