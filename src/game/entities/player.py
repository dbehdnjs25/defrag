"""Top-down player. Logic-only: movement is a pure function of dt and an
input direction, so it is unit-testable headlessly."""

from __future__ import annotations

from dataclasses import dataclass

import pygame

from game import config


@dataclass
class Player:
    pos: pygame.Vector2
    radius: float = config.PLAYER_RADIUS
    speed: float = config.PLAYER_SPEED

    def update(self, dt: float, move_dir: pygame.Vector2, bounds: tuple[int, int]) -> None:
        """Advance by ``dt`` along ``move_dir`` (unnormalized), clamped to bounds."""
        if move_dir.length_squared() > 0:
            self.pos += move_dir.normalize() * self.speed * dt
        width, height = bounds
        self.pos.x = max(self.radius, min(width - self.radius, self.pos.x))
        self.pos.y = max(self.radius, min(height - self.radius, self.pos.y))
