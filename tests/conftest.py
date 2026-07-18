"""Shared pytest fixtures for headless pygame testing.

SDL reads its driver environment variables *at import/init time*, so these must
be set before ``pygame`` is imported anywhere in the test session. Keeping them
here (the first thing pytest imports) guarantees that ordering.
"""

from __future__ import annotations

import os

# Must run before `import pygame`. `dummy` drivers mean no window, no audio
# device -> tests run on a headless CI box with no display attached.
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

import pygame  # noqa: E402  (import must follow the env setup above)
import pytest  # noqa: E402

HEADLESS = os.environ.get("SDL_VIDEODRIVER") == "dummy"

# Skip marker for the rare test that genuinely needs a real display/renderer.
requires_display = pytest.mark.skipif(HEADLESS, reason="requires a real display")


@pytest.fixture(scope="session", autouse=True)
def _pygame_session():
    """Init pygame once for the whole session; quit at the end.

    Needed by anything that touches pygame C internals (Vector2, Surface,
    fonts, ...) even though no window is created.
    """
    pygame.init()
    yield
    pygame.quit()


@pytest.fixture
def surface() -> pygame.Surface:
    """An off-screen surface — no display required. Use for draw() tests."""
    return pygame.Surface((64, 64))
