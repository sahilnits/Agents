from plugins.req_agent.agent import ReqAgent

def test_req_agent_runs():
    agent = ReqAgent()
    assert agent.run() == "ReqAgent ran successfully"