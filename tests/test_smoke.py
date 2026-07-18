"""Headless smoke tests: exercise the rendering path without a real window.

These use the off-screen ``surface`` fixture (from conftest) so they run on a
CI box with no display. They prove pygame is wired up and the draw code runs.
"""

from __future__ import annotations

from game import config
from game.scenes.play import PlayScene


def test_config_screen_size_is_consistent() -> None:
    assert config.SCREEN_SIZE == (config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
    assert config.FIXED_DT == 1.0 / config.FPS


def test_play_scene_draws_something_onto_surface(surface) -> None:
    """After drawing the white ball, at least one pixel is non-background."""
    scene = PlayScene()
    scene.ball.x, scene.ball.y = 32, 32  # centre it on the 64x64 surface
    surface.fill(config.BACKGROUND)

    scene.draw(surface)

    assert surface.get_at((32, 32))[:3] == config.WHITE


def test_play_scene_update_advances_ball(surface) -> None:
    scene = PlayScene()
    start = scene.ball.position
    scene.update(dt=0.1)
    assert scene.ball.position != start
