"""Example gameplay scene: a single ball bouncing around the window.

This is scaffolding to prove the architecture end-to-end (input -> update ->
draw) and to give ``python -m game`` something to show. Replace it with the
real game once you've decided what to build.
"""

from __future__ import annotations

import pygame

from game import config
from game.core.scene import Scene
from game.entities.ball import Ball


class PlayScene(Scene):
    def __init__(self) -> None:
        self.ball = Ball(
            x=config.SCREEN_WIDTH / 2,
            y=config.SCREEN_HEIGHT / 2,
            vx=220.0,
            vy=160.0,
        )

    def handle_event(self, event: pygame.event.Event) -> None:
        escape = event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        if escape and self.manager is not None:
            self.manager.pop()

    def update(self, dt: float) -> None:
        self.ball.update(dt, config.SCREEN_WIDTH, config.SCREEN_HEIGHT)

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, config.WHITE, self.ball.position, self.ball.radius)
