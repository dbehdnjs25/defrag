"""A bouncing ball.

Deliberately a *logic-only* entity: it knows its position, velocity and radius,
and how to advance itself by ``dt`` while bouncing off a rectangular bound. It
does not import pygame, so its physics is trivially unit-testable. Rendering is
the scene's job.

This exists mainly as a worked example of the "testable logic, dumb rendering"
split. Replace or delete it when the real game takes shape.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Ball:
    x: float
    y: float
    vx: float
    vy: float
    radius: float = 12.0

    def update(self, dt: float, width: int, height: int) -> None:
        """Advance the ball by ``dt`` seconds, bouncing inside [0, w] x [0, h]."""
        self.x += self.vx * dt
        self.y += self.vy * dt

        if self.x - self.radius < 0:
            self.x = self.radius
            self.vx = abs(self.vx)
        elif self.x + self.radius > width:
            self.x = width - self.radius
            self.vx = -abs(self.vx)

        if self.y - self.radius < 0:
            self.y = self.radius
            self.vy = abs(self.vy)
        elif self.y + self.radius > height:
            self.y = height - self.radius
            self.vy = -abs(self.vy)

    @property
    def position(self) -> tuple[float, float]:
        return (self.x, self.y)
