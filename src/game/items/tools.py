"""Usable tools. Only the mining tool exists in this milestone; the weapon
tool arrives with the combat spec."""

from __future__ import annotations

from dataclasses import dataclass

from game import config


@dataclass(frozen=True)
class MiningTool:
    range: float = config.MINING_RANGE
    dps: float = config.MINING_DPS
    name: str = "Mining Beam"
