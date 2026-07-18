"""The central core the player defends and syncs resources to. Logic-only."""

from __future__ import annotations

from dataclasses import dataclass

import pygame

from game import config


@dataclass
class Core:
    pos: pygame.Vector2
    radius: float = config.CORE_RADIUS
    sync_radius: float = config.CORE_SYNC_RADIUS

    def is_in_sync_range(self, point: pygame.Vector2) -> bool:
        return self.pos.distance_to(point) <= self.sync_radius
