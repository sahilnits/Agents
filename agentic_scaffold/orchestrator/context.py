from pydantic import BaseModel
from typing import Optional

class SessionContext(BaseModel):
    project_id: str
    user: str
    is_admin: bool