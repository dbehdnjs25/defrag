import pygame

from game import config
from game.systems.camera import FREE, LOCKED, Camera

VIEW = (960, 540)
WORLD = (2400, 1600)


def _cam(mode=LOCKED):
    return Camera(offset=pygame.Vector2(500, 400), view_size=VIEW, world_size=WORLD, mode=mode)


def test_screen_world_roundtrip():
    cam = _cam()
    p = pygame.Vector2(123, 456)
    assert cam.screen_to_world(cam.world_to_screen(p)) == p


def test_locked_update_centers_on_player():
    cam = _cam(LOCKED)
    cam.update(1 / 60, pygame.Vector2(1200, 800), (0, 0), False)
    assert cam.offset == pygame.Vector2(1200 - 480, 800 - 270)


def test_toggle_from_locked_to_free_keeps_offset():
    cam = _cam(LOCKED)
    before = pygame.Vector2(cam.offset)
    cam.toggle_lock(pygame.Vector2(1200, 800))
    assert cam.mode == FREE
    assert cam.offset == before


def test_toggle_to_locked_snaps_to_player():
    cam = _cam(FREE)
    cam.toggle_lock(pygame.Vector2(1200, 800))
    assert cam.mode == LOCKED
    assert cam.offset == pygame.Vector2(1200 - 480, 800 - 270)


def test_free_pan_at_left_edge_moves_offset_left():
    cam = _cam(FREE)
    cam.update(1.0, pygame.Vector2(1200, 800), (5, 300), False)  # mouse near left edge
    assert cam.offset.x == 500 - config.CAMERA_PAN_SPEED


def test_mining_held_suppresses_pan():
    cam = _cam(FREE)
    cam.update(1.0, pygame.Vector2(1200, 800), (5, 300), True)
    assert cam.offset == pygame.Vector2(500, 400)


def test_offset_clamped_to_world():
    cam = Camera(offset=pygame.Vector2(0, 0), view_size=VIEW, world_size=WORLD, mode=FREE)
    cam.update(1.0, pygame.Vector2(1200, 800), (5, 5), False)  # tries to pan up-left past 0
    assert cam.offset.x == 0
    assert cam.offset.y == 0
