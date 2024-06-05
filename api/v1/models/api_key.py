from pydantic import BaseModel
from datetime import datetime
"""
api_key module
API keys for app request authentication
"""

class APIKey(BaseModel):
    """
    Implements an API key
    """
    app_id: str
    api_key: str
    created_at: int = int(datetime.timestamp(datetime.now()))
    updated_at: int = int(datetime.timestamp(datetime.now()))
    active: bool = True