# Pygame Project

A Pygame starter with a **TDD-first, testable architecture**. The game itself
isn't decided yet — this repo is the scaffolding so implementation can begin
test-first the moment a design is chosen.

Built on **pygame-ce** (Community Edition, imported as `pygame`).

## Quick start

```bash
# 1. Create + activate a virtual environment (already created as .venv)
#    PowerShell:  .venv\Scripts\Activate.ps1
#    Git Bash:    source .venv/Scripts/activate

# 2. Install the project + dev tools (editable)
pip install -e ".[dev]"

# 3. Run the demo (a bouncing ball — replace with the real game)
python -m game

# 4. Run the tests (headless, no window opens)
pytest
```

## Project layout

```
src/game/
├── config.py          # constants only, zero pygame import (safe everywhere)
├── core/
│   ├── app.py         # Game shell: the ONLY module touching display + events
│   ├── loop.py        # FixedTimestep accumulator (pure, deterministic)
│   └── scene.py       # Scene base class + stack-based SceneManager
├── entities/
│   └── ball.py        # example logic-only entity (update(dt), no pygame)
└── scenes/
    └── play.py        # example scene wiring an entity to input + drawing
tests/                 # mirrors src; runs headless via SDL dummy drivers
assets/                # images / sounds / fonts
```

## The core convention: split `update` from `draw`

Everything worth testing is **logic**, and logic lives in `update(dt)` methods
that take the timestep (and input) as explicit arguments — no wall-clock, no
globals, no display. Rendering lives in `draw(surface)` and is the only layer
that touches SDL. This is what makes ~all game logic unit-testable headlessly.

- `update(dt)` → pure, deterministic → tested directly.
- `draw(surface)` → can be tested against an off-screen `pygame.Surface`, or skipped.
- `core/app.py` → the thin shell that talks to `pygame.display` and the event pump.

## Common commands

```bash
pytest                 # tests + coverage report
ruff check .           # lint
ruff format .          # auto-format
mypy                   # static type check (strict)
python -m game         # play the demo
```

See [CLAUDE.md](CLAUDE.md) for architecture rules, testing patterns and references.
