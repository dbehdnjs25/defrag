"""The CPU-cache hotbar: a fixed number of slots, only some unlocked. The
selected slot's item is the active tool driving the left mouse button."""

from __future__ import annotations

from dataclasses import dataclass

from game import config


@dataclass
class Hotbar:
    slots: list[object | None]
    unlocked: int = config.HOTBAR_START_UNLOCKED
    selected: int = 0

    @classmethod
    def create(cls) -> Hotbar:
        return cls(slots=[None] * config.HOTBAR_MAX_SLOTS)

    def select(self, index: int) -> None:
        if 0 <= index < self.unlocked:
            self.selected = index

    @property
    def active_tool(self) -> object | None:
        return self.slots[self.selected]
