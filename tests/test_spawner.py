import random

import pygame

from game import config
from game.entities.core import Core
from game.entities.fragment import Fragment
from game.systems.spawner import Spawner

CORE = Core(pos=pygame.Vector2(config.WORLD_WIDTH / 2, config.WORLD_HEIGHT / 2))


def test_no_spawn_before_interval():
    sp = Spawner()
    frags = []
    assert sp.update(0.1, frags, CORE, random.Random(1)) is None
    assert frags == []


def test_spawns_after_interval():
    sp = Spawner()
    frags = []
    result = sp.update(config.SPAWN_INTERVAL, frags, CORE, random.Random(1))
    assert result is not None
    assert frags == [result]


def test_respects_max_fragments():
    sp = Spawner(max_fragments=2)
    frags = [
        Fragment(pos=pygame.Vector2(100, 100)),
        Fragment(pos=pygame.Vector2(200, 200)),
    ]  # already at cap
    assert sp.update(config.SPAWN_INTERVAL, frags, CORE, random.Random(1)) is None
    assert len(frags) == 2


def test_deterministic_with_seed():
    a = Spawner().update(config.SPAWN_INTERVAL, [], CORE, random.Random(42))
    b = Spawner().update(config.SPAWN_INTERVAL, [], CORE, random.Random(42))
    assert a.pos == b.pos


def test_spawn_avoids_core_sync_zone():
    sp = Spawner()
    for seed in range(50):
        frags = []
        frag = sp.update(config.SPAWN_INTERVAL, frags, CORE, random.Random(seed))
        if frag is not None:
            assert CORE.pos.distance_to(frag.pos) >= CORE.sync_radius
