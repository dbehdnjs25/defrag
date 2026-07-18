"""Tests for the stack-based SceneManager (pure logic, no display)."""

from __future__ import annotations

from game.core.scene import Scene, SceneManager


class RecordingScene(Scene):
    """A scene that records lifecycle calls, for assertions."""

    def __init__(self, name: str, log: list[str]) -> None:
        self.name = name
        self.log = log
        self.updates = 0

    def on_enter(self) -> None:
        self.log.append(f"enter:{self.name}")

    def on_exit(self) -> None:
        self.log.append(f"exit:{self.name}")

    def update(self, dt: float) -> None:
        self.updates += 1


def test_push_sets_current_and_fires_on_enter() -> None:
    log: list[str] = []
    mgr = SceneManager()
    scene = RecordingScene("a", log)

    mgr.push(scene)

    assert mgr.current is scene
    assert scene.manager is mgr
    assert log == ["enter:a"]


def test_pop_fires_on_exit_and_detaches_manager() -> None:
    log: list[str] = []
    mgr = SceneManager()
    scene = RecordingScene("a", log)
    mgr.push(scene)

    popped = mgr.pop()

    assert popped is scene
    assert scene.manager is None
    assert mgr.is_empty
    assert log == ["enter:a", "exit:a"]


def test_stack_returns_to_previous_scene_on_pop() -> None:
    log: list[str] = []
    mgr = SceneManager()
    a, b = RecordingScene("a", log), RecordingScene("b", log)

    mgr.push(a)
    mgr.push(b)
    assert mgr.current is b

    mgr.pop()
    assert mgr.current is a  # overlay popped, previous scene resumes


def test_update_only_targets_top_scene() -> None:
    log: list[str] = []
    mgr = SceneManager()
    a, b = RecordingScene("a", log), RecordingScene("b", log)
    mgr.push(a)
    mgr.push(b)

    mgr.update(0.016)

    assert b.updates == 1
    assert a.updates == 0


def test_replace_swaps_top_scene() -> None:
    log: list[str] = []
    mgr = SceneManager()
    a, b = RecordingScene("a", log), RecordingScene("b", log)
    mgr.push(a)

    mgr.replace(b)

    assert mgr.current is b
    assert log == ["enter:a", "exit:a", "enter:b"]


def test_pop_on_empty_is_safe() -> None:
    mgr = SceneManager()
    assert mgr.pop() is None
    assert mgr.is_empty
