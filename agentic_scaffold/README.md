# Agentic Project Facilitator Scaffold

This repository provides a modular, AI‑powered **Project Facilitation Control Tower**.  
It jump‑starts new projects (software, data engineering, AI/ML) by orchestrating a crew of specialized agents
that handle requirements intake, architecture design, code scaffold generation, testing, and analytics.

## Quick start
```bash
# clone your fork
git clone https://github.com/your-org/Agents.git
cd Agents/agentic_scaffold   # contains pyproject.toml

# create virtualenv & install
python -m venv .venv && source .venv/bin/activate
pip install -e .

# run Streamlit UI
streamlit run app/main.py

# alternatively from repo root
# pip install -e ./agentic_scaffold
# streamlit run agentic_scaffold/app/main.py
```
The first page will prompt GitHub OAuth login. Admins (listed in `ADMIN_GH_LOGINS` env var)
may create & edit requirements and trigger agents; others are read‑only.

## Architecture at a glance
```
Streamlit UI  <--->  Orchestrator  <--->  Agent Plugins
                               \--- SQLite Change Journal
                               \--- GitHub Actions CI
```

## Folder layout
* `app/` – Streamlit front‑end
* `orchestrator/` – dependency‑injection kernel + event bus
* `plugins/` – pluggable agents (ReqAgent, CodeAgent, TestAgent)
* `adapters/` – swappable infra adapters (storage, auth, VCS)
* `models/` – SQLAlchemy ORM tables
* `tests/` – pytest suites
* `.github/workflows/` – CI pipeline

## License
MIT
