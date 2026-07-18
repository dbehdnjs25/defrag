from game import config


def test_world_is_larger_than_screen():
    assert config.WORLD_WIDTH > config.SCREEN_WIDTH
    assert config.WORLD_HEIGHT > config.SCREEN_HEIGHT


def test_capacities_are_positive_multiples_of_fragment_mb():
    assert config.FRAGMENT_MB > 0
    assert config.BACKPACK_CAP_MB >= config.FRAGMENT_MB
    assert config.DOCUMENTS_CAP_MB > config.BACKPACK_CAP_MB


def test_sync_radius_exceeds_core_radius():
    assert config.CORE_SYNC_RADIUS > config.CORE_RADIUS


def test_hotbar_start_within_max():
    assert 0 < config.HOTBAR_START_UNLOCKED <= config.HOTBAR_MAX_SLOTS
