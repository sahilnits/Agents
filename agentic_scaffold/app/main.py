import streamlit as st
from orchestrator.registry import get_orchestrator
from orchestrator.context import SessionContext
from datetime import datetime

st.set_page_config(page_title="Agentic Control Tower", page_icon="🛰️", layout="wide")

# --- Auth (simplified demo) ---
gh_user = st.experimental_get_query_params().get("user", ["guest"])[0]
user_is_admin = gh_user in (st.secrets.get("ADMIN_GH_LOGINS", "")).split(",")

st.sidebar.title("🚀 Agentic Facilitator")
st.sidebar.markdown(f"**Logged in as:** `{gh_user}`")
if user_is_admin:
    st.sidebar.success("Admin mode: write access enabled")
else:
    st.sidebar.info("Read‑only mode")

# --- Simple chat demo ---
st.title("🗨️ Project Chat")
if "messages" not in st.session_state:
    st.session_state["messages"] = []

for m in st.session_state["messages"]:
    with st.chat_message(m["role"]):
        st.markdown(m["body"])

prompt = st.chat_input("Ask the agents…")
if prompt:
    st.session_state["messages"].append({"role": "user", "body": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # orchestrator call (stub)
    orchestrator = get_orchestrator()
    assistant_reply = orchestrator.handle_chat(prompt, user=gh_user, admin=user_is_admin)

    with st.chat_message("assistant"):
        st.markdown(assistant_reply)

    st.session_state["messages"].append({"role": "assistant", "body": assistant_reply})