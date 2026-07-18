import pygame
import pytest

from game import config
from game.entities.player import Player


def test_moves_in_direction():
    p = Player(pos=pygame.Vector2(100, 100))
    p.update(1.0, pygame.Vector2(1, 0), (2400, 1600))
    assert p.pos.x == 100 + config.PLAYER_SPEED
    assert p.pos.y == 100


def test_diagonal_is_normalized():
    p = Player(pos=pygame.Vector2(500, 500))
    p.update(1.0, pygame.Vector2(1, 1), (2400, 1600))
    travelled = p.pos.distance_to(pygame.Vector2(500, 500))
    assert travelled == pytest.approx(config.PLAYER_SPEED)


def test_zero_direction_does_not_move():
    p = Player(pos=pygame.Vector2(300, 300))
    p.update(1.0, pygame.Vector2(0, 0), (2400, 1600))
    assert p.pos == pygame.Vector2(300, 300)


def test_clamped_to_bounds():
    p = Player(pos=pygame.Vector2(5, 5))
    p.update(1.0, pygame.Vector2(-1, -1), (2400, 1600))
    assert p.pos.x == config.PLAYER_RADIUS
    assert p.pos.y == config.PLAYER_RADIUS
