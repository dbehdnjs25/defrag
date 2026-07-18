import pygame

from game import config
from game.scenes.play import PlayScene


def _key_event(key):
    return pygame.event.Event(pygame.KEYDOWN, key=key)


def test_number_keys_select_hotbar():
    scene = PlayScene()
    scene.handle_event(_key_event(pygame.K_2))
    assert scene.hotbar.selected == 1
    scene.handle_event(_key_event(pygame.K_1))
    assert scene.hotbar.selected == 0


def test_y_toggles_camera_lock():
    scene = PlayScene()
    start_mode = scene.camera.mode
    scene.handle_event(_key_event(pygame.K_y))
    assert scene.camera.mode != start_mode
    scene.handle_event(_key_event(pygame.K_y))
    assert scene.camera.mode == start_mode


def test_movement_key_moves_player():
    scene = PlayScene()
    start_x = scene.player.pos.x
    scene.handle_event(_key_event(pygame.K_d))
    scene.update(config.FIXED_DT)
    assert scene.player.pos.x > start_x


def test_sync_transfers_backpack_at_core():
    scene = PlayScene()
    scene.player.pos = pygame.Vector2(scene.core.pos)  # stand on the core
    scene.backpack.add(3)
    scene.update(config.FIXED_DT)
    assert scene.backpack.count == 0
    assert scene.documents.count == 3


def test_draw_runs_without_error(surface):
    scene = PlayScene()
    scene.draw(surface)  # must not raise on the 64x64 offscreen surface
