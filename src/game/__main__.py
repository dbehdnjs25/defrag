"""Entry point: ``python -m game`` (or the ``game`` console script)."""

from __future__ import annotations

from game.core.app import Game
from game.scenes.play import PlayScene


def main() -> None:
    Game().run(PlayScene())


if __name__ == "__main__":
    main()
