"""Game package.

The architecture deliberately separates *logic* from *rendering* so that the
bulk of the game can be unit-tested without a display or a running event loop.

    - `config`   : plain constants, zero pygame dependency.
    - `core`     : engine primitives (fixed-timestep loop, scene stack).
    - `scenes`   : concrete game states (menu, play, ...).

See CLAUDE.md for the testing conventions this project follows.
"""

__version__ = "0.1.0"
