"""Scene abstraction and a small stack-based scene manager.

A *scene* is one screen/state of the game (menu, gameplay, pause, ...).

Design goals:
    - `update(dt)` contains only logic and takes the timestep explicitly, so it
      is fully deterministic and unit-testable without a clock or a display.
    - `draw(surface)` contains only rendering. Tests can pass an off-screen
      `pygame.Surface` (no display required) or skip drawing entirely.
    - Scenes never call `pygame.display`, `pygame.quit`, or the event pump
      directly; they receive already-parsed input/events and request
      transitions through the return value of `update`.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover - typing only
    import pygame


class Scene:
    """Base class for all game scenes.

    Subclasses override the hooks they need. The manager that owns the scene is
    injected as `self.manager` when the scene is pushed.
    """

    manager: SceneManager | None = None

    def on_enter(self) -> None:
        """Called once when the scene becomes active."""

    def on_exit(self) -> None:
        """Called once when the scene is removed/replaced."""

    def handle_event(self, event: pygame.event.Event) -> None:
        """Handle a single already-polled pygame event."""

    def update(self, dt: float) -> None:
        """Advance the scene by ``dt`` seconds. Pure logic, no rendering."""

    def draw(self, surface: pygame.Surface) -> None:
        """Render the scene onto ``surface``. No logic, no state mutation."""


class SceneManager:
    """A stack of scenes. The top scene is the active one.

    Using a stack (rather than a single current scene) makes overlays such as a
    pause menu trivial: push the pause scene, pop it to resume.
    """

    def __init__(self) -> None:
        self._stack: list[Scene] = []

    @property
    def current(self) -> Scene | None:
        return self._stack[-1] if self._stack else None

    @property
    def is_empty(self) -> bool:
        return not self._stack

    def push(self, scene: Scene) -> None:
        scene.manager = self
        self._stack.append(scene)
        scene.on_enter()

    def pop(self) -> Scene | None:
        if not self._stack:
            return None
        scene = self._stack.pop()
        scene.on_exit()
        scene.manager = None
        return scene

    def replace(self, scene: Scene) -> None:
        """Swap the top scene for ``scene`` (pop then push)."""
        self.pop()
        self.push(scene)

    # --- Delegation to the active scene -----------------------------------
    def handle_event(self, event: pygame.event.Event) -> None:
        if self.current is not None:
            self.current.handle_event(event)

    def update(self, dt: float) -> None:
        if self.current is not None:
            self.current.update(dt)

    def draw(self, surface: pygame.Surface) -> None:
        if self.current is not None:
            self.current.draw(surface)
