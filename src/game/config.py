"""Global configuration constants.

Kept free of any ``pygame`` import so it can be imported in any test without a
display. Colours are plain RGB tuples for the same reason.
"""

from __future__ import annotations

from typing import Final

# --- Window -----------------------------------------------------------------
TITLE: Final[str] = "Defrag"
SCREEN_WIDTH: Final[int] = 960
SCREEN_HEIGHT: Final[int] = 540
SCREEN_SIZE: Final[tuple[int, int]] = (SCREEN_WIDTH, SCREEN_HEIGHT)

# --- Timing -----------------------------------------------------------------
# The simulation advances in fixed steps for deterministic, testable logic.
FPS: Final[int] = 60
FIXED_DT: Final[float] = 1.0 / FPS  # seconds per logic step
MAX_FRAME_TIME: Final[float] = 0.25  # clamp to avoid the "spiral of death"

# --- Colours (RGB) ----------------------------------------------------------
BLACK: Final[tuple[int, int, int]] = (0, 0, 0)
WHITE: Final[tuple[int, int, int]] = (255, 255, 255)
BACKGROUND: Final[tuple[int, int, int]] = (30, 30, 46)

# --- World ------------------------------------------------------------------
WORLD_WIDTH: Final[int] = 2400
WORLD_HEIGHT: Final[int] = 1600
WORLD_SIZE: Final[tuple[int, int]] = (WORLD_WIDTH, WORLD_HEIGHT)
TILE_SIZE: Final[int] = 32  # visual floor rendering only, not a data grid

# --- Player -----------------------------------------------------------------
PLAYER_SPEED: Final[float] = 220.0  # px/s
PLAYER_RADIUS: Final[float] = 14.0

# --- Mining / fragments -----------------------------------------------------
FRAGMENT_HP: Final[float] = 60.0
FRAGMENT_RADIUS: Final[float] = 10.0
MINING_DPS: Final[float] = 40.0  # hp per second while channelling
MINING_RANGE: Final[float] = 96.0  # player-to-fragment distance
FRAGMENT_MB: Final[int] = 5  # storage size of one fragment

# --- Storage ----------------------------------------------------------------
BACKPACK_CAP_MB: Final[int] = 50  # small field carry -> forces return trips
DOCUMENTS_CAP_MB: Final[int] = 500  # drive store (the "warehouse")

# --- Camera -----------------------------------------------------------------
CAMERA_PAN_SPEED: Final[float] = 400.0  # px/s free-pan speed
CAMERA_EDGE_MARGIN: Final[int] = 40  # px band at screen edge that pans

# --- Spawner ----------------------------------------------------------------
SPAWN_INTERVAL: Final[float] = 2.0  # seconds between spawn attempts
SPAWN_MAX: Final[int] = 30  # max simultaneous fragments

# --- Core -------------------------------------------------------------------
CORE_RADIUS: Final[float] = 40.0
CORE_SYNC_RADIUS: Final[float] = 120.0  # auto-transfer when player within this

# --- Hotbar -----------------------------------------------------------------
HOTBAR_MAX_SLOTS: Final[int] = 7
HOTBAR_START_UNLOCKED: Final[int] = 2

# --- Additional colours (RGB) -----------------------------------------------
FLOOR_A: Final[tuple[int, int, int]] = (26, 26, 40)
FLOOR_B: Final[tuple[int, int, int]] = (32, 32, 48)
FRAGMENT_COLOR: Final[tuple[int, int, int]] = (90, 200, 255)
CORE_COLOR: Final[tuple[int, int, int]] = (120, 255, 180)
PLAYER_COLOR: Final[tuple[int, int, int]] = (240, 240, 255)
