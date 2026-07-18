from game import config
from game.inventory.hotbar import Hotbar
from game.items.tools import MiningTool


def test_create_has_max_empty_slots():
    hb = Hotbar.create()
    assert len(hb.slots) == config.HOTBAR_MAX_SLOTS
    assert all(s is None for s in hb.slots)
    assert hb.unlocked == config.HOTBAR_START_UNLOCKED


def test_active_tool_reflects_selection():
    hb = Hotbar.create()
    tool = MiningTool()
    hb.slots[0] = tool
    assert hb.active_tool is tool


def test_select_ignores_locked_slots():
    hb = Hotbar.create()  # unlocked == 2 -> valid indices 0,1
    hb.select(1)
    assert hb.selected == 1
    hb.select(5)  # locked
    assert hb.selected == 1


def test_mining_tool_defaults():
    t = MiningTool()
    assert t.range == config.MINING_RANGE
    assert t.dps == config.MINING_DPS
