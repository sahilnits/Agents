from agentic_scaffold.orchestrator.registry import get_orchestrator


def test_imports() -> None:
    assert get_orchestrator() is not None

