from agentic_scaffold.plugins.req_agent.agent import ReqAgent


def test_req_agent_runs() -> None:
    agent = ReqAgent()
    assert agent.run() == "ReqAgent ran successfully"

