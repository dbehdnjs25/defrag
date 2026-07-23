import pygame

from game.entities.core import Core


def test_point_inside_sync_range():
    c = Core(pos=pygame.Vector2(1000, 800), sync_radius=100)
    assert c.is_in_sync_range(pygame.Vector2(1050, 800)) is True


def test_point_outside_sync_range():
    c = Core(pos=pygame.Vector2(1000, 800), sync_radius=100)
    assert c.is_in_sync_range(pygame.Vector2(1200, 800)) is False


def test_point_exactly_on_sync_boundary_is_inside():
    # dist == sync_radius must count as in-range (impl uses <=)
    c = Core(pos=pygame.Vector2(1000, 800), sync_radius=100)
    assert c.is_in_sync_range(pygame.Vector2(1100, 800)) is True
