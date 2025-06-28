from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime
from datetime import datetime

metadata = MetaData()

change_journal = Table(
    "change_journal",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("project_id", String),
    Column("req_id", String),
    Column("git_sha", String),
    Column("agent", String),
    Column("action", String),
    Column("result_json", String),
    Column("ts", DateTime, default=datetime.utcnow),
)