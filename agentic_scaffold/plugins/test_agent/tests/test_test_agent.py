from agentic_scaffold.plugins.test_agent.agent import TestAgent


def test_test_agent_runs() -> None:
    agent = TestAgent()
    assert agent.run() == "TestAgent ran successfully"

