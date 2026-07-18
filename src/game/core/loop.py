"""Fixed-timestep accumulator.

The classic "Fix Your Timestep!" pattern (Glenn Fiedler): decouple the logic
update rate from the render rate so the simulation is deterministic regardless
of frame rate. This class is pure Python with no pygame dependency, so the
timing maths can be unit-tested directly.

    accumulator += frame_time (clamped)
    while accumulator >= dt:
        world.update(dt)   # always the same dt
        accumulator -= dt

Reference: https://gafferongames.com/post/fix_your_timestep/
"""

from __future__ import annotations

from game.config import FIXED_DT, MAX_FRAME_TIME


class FixedTimestep:
    """Accumulates real frame time and yields a fixed number of logic steps."""

    def __init__(self, dt: float = FIXED_DT, max_frame_time: float = MAX_FRAME_TIME) -> None:
        if dt <= 0:
            raise ValueError("dt must be positive")
        self.dt = dt
        self.max_frame_time = max_frame_time
        self._accumulator = 0.0

    @property
    def accumulator(self) -> float:
        return self._accumulator

    def steps(self, frame_time: float) -> int:
        """Feed the elapsed real time; return how many fixed steps to run.

        ``frame_time`` is clamped to ``max_frame_time`` to avoid the
        "spiral of death" when a frame hangs (e.g. window drag, breakpoint).
        """
        frame_time = min(max(frame_time, 0.0), self.max_frame_time)
        self._accumulator += frame_time
        n = 0
        while self._accumulator >= self.dt:
            self._accumulator -= self.dt
            n += 1
        return n

    @property
    def alpha(self) -> float:
        """Interpolation factor in [0, 1) for smooth rendering between steps."""
        return self._accumulator / self.dt
