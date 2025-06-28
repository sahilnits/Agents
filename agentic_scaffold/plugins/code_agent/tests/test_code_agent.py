from agentic_scaffold.plugins.code_agent.agent import CodeAgent


def test_code_agent_runs() -> None:
    agent = CodeAgent()
    assert agent.run() == "CodeAgent ran successfully"

