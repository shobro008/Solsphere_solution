from pydantic import BaseModel
from datetime import datetime
from typing import Optional  # Needed for optional fields

class SystemStatusSchema(BaseModel):
    machine_id: str
    os: Optional[str] = None  # ✅ New field to match daemon.py
    encryption: bool
    antivirus: bool
    os_update: bool
    sleep_timeout: int
    last_updated: datetime

    class Config:
        orm_mode = True
