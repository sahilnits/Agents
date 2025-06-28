import importlib.metadata
from typing import Dict

_AGENTS: Dict[str, object] = {}

def _load_agents():
    for entry in importlib.metadata.entry_points(group="agentic_agents"):
        _AGENTS[entry.name] = entry.load()

_loaded = False

def get_agent(name: str):
    global _loaded
    if not _loaded:
        _load_agents()
        _loaded = True
    return _AGENTS.get(name)

class Orchestrator:
    def handle_chat(self, prompt: str, user: str, admin: bool) -> str:
        # naive demo: echo agent names
        if prompt.lower().startswith("list agents"):
            names = ", ".join(_AGENTS.keys())
            return f"Available agents: {names}"
        return "🚧 (Agent response placeholder)"

_orch = Orchestrator()

def get_orchestrator():
    return _orch