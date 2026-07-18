"""Time-based fragment spawner. Randomness comes from an injected
``random.Random`` so tests are deterministic. Spawn spots avoid the core's
sync zone and existing fragments; a capped retry count prevents an infinite
loop when the world is saturated."""

from __future__ import annotations

import random
from dataclasses import dataclass, field

import pygame

from game import config
from game.entities.core import Core
from game.entities.fragment import Fragment

_MARGIN = 64
_SPAWN_ATTEMPTS = 20


@dataclass
class Spawner:
    interval: float = config.SPAWN_INTERVAL
    max_fragments: int = config.SPAWN_MAX
    _accumulator: float = field(default=0.0, init=False)

    def update(
        self,
        dt: float,
        fragments: list[Fragment],
        core: Core,
        rng: random.Random,
    ) -> Fragment | None:
        self._accumulator += dt
        if self._accumulator < self.interval:
            return None
        self._accumulator -= self.interval
        if len(fragments) >= self.max_fragments:
            return None
        spot = self._find_spot(fragments, core, rng)
        if spot is None:
            return None
        fragment = Fragment(pos=spot)
        fragments.append(fragment)
        return fragment

    def _find_spot(
        self,
        fragments: list[Fragment],
        core: Core,
        rng: random.Random,
    ) -> pygame.Vector2 | None:
        for _ in range(_SPAWN_ATTEMPTS):
            point = pygame.Vector2(
                rng.uniform(_MARGIN, config.WORLD_WIDTH - _MARGIN),
                rng.uniform(_MARGIN, config.WORLD_HEIGHT - _MARGIN),
            )
            if core.pos.distance_to(point) < core.sync_radius + config.FRAGMENT_RADIUS:
                continue
            too_close = any(
                f.pos.distance_to(point) < config.FRAGMENT_RADIUS * 2 for f in fragments
            )
            if too_close:
                continue
            return point
        return None
