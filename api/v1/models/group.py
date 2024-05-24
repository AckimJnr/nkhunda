"""
Group module
"""
from pydantic import BaseModel
from datetime import datetime


class Group(BaseModel):
    """
    Implements a messaging group
    """
    app_id: str
    creator: str
    group_name: str
    members: list
    created_at: int = int(datetime.timestamp(datetime.now()))
    updated_at: int = int(datetime.timestamp(datetime.now()))