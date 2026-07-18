"""Headless smoke tests: exercise the rendering path without a real window."""

from __future__ import annotations

from game import config
from game.scenes.play import PlayScene


def test_config_screen_size_is_consistent() -> None:
    assert config.SCREEN_SIZE == (config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
    assert config.FIXED_DT == 1.0 / config.FPS


def test_play_scene_draws_non_background_pixels(surface) -> None:
    """Drawing the world (floor, core, player) paints over the background."""
    scene = PlayScene()
    surface.fill(config.BACKGROUND)

    scene.draw(surface)

    pixels = {surface.get_at((x, y))[:3] for x in range(64) for y in range(64)}
    assert pixels != {config.BACKGROUND}
