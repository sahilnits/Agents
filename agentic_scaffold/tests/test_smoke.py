def test_imports():
    import orchestrator.registry as r
    assert r.get_orchestrator() is not None