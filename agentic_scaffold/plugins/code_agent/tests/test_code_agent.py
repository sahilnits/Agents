from plugins.code_agent.agent import CodeAgent

def test_code_agent_runs():
    agent = CodeAgent()
    assert agent.run() == "CodeAgent ran successfully"