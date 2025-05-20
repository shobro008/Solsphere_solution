from sqlalchemy import Column, String, DateTime
from .database import Base
from datetime import datetime

class SystemStatus(Base):
    __tablename__ = "system_status"
    machine_id = Column(String, primary_key=True, index=True)
    os = Column(String)
    encryption = Column(String)
    antivirus = Column(String)
    os_update = Column(String)
    sleep_timeout = Column(String)
    last_updated = Column(DateTime, default=datetime.utcnow)
