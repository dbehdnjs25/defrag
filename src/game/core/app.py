"""The application shell: owns the window, the clock and the scene stack.

This is the *only* module that touches `pygame.display` and the event pump, so
it is intentionally thin. Everything worth testing lives in scenes, entities
and `FixedTimestep`; this class just wires them to real pygame I/O.
"""

from __future__ import annotations

import pygame

from game import config
from game.core.loop import FixedTimestep
from game.core.scene import Scene, SceneManager


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption(config.TITLE)
        self.screen = pygame.display.set_mode(config.SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.timestep = FixedTimestep()
        self.scenes = SceneManager()
        self.running = False

    def run(self, initial_scene: Scene) -> None:
        self.scenes.push(initial_scene)
        self.running = True
        while self.running and not self.scenes.is_empty:
            frame_time = self.clock.tick(config.FPS) / 1000.0  # ms -> seconds
            self._process_events()
            for _ in range(self.timestep.steps(frame_time)):
                self.scenes.update(self.timestep.dt)
            self._render()
        pygame.quit()

    def _process_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.scenes.handle_event(event)

    def _render(self) -> None:
        self.screen.fill(config.BACKGROUND)
        self.scenes.draw(self.screen)
        pygame.display.flip()
