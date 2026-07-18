"""Global configuration constants.

Kept free of any ``pygame`` import so it can be imported in any test without a
display. Colours are plain RGB tuples for the same reason.
"""

from __future__ import annotations

from typing import Final

# --- Window -----------------------------------------------------------------
TITLE: Final[str] = "Pygame Project"
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
