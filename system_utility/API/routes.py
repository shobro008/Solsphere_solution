from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import models, schemas, database
from datetime import datetime
from typing import List

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST /report - Used by daemon.py to send system status
@router.post("/report")
def receive_status(payload: schemas.SystemStatusSchema, db: Session = Depends(get_db)):
    record = db.query(models.SystemStatus).filter(models.SystemStatus.machine_id == payload.machine_id).first()
    if record:
        record.encryption = payload.encryption
        record.antivirus = payload.antivirus
        record.os_update = payload.os_update
        record.sleep_timeout = payload.sleep_timeout
        record.last_updated = datetime.utcnow()
    else:
        record = models.SystemStatus(**payload.dict(), last_updated=datetime.utcnow())
        db.add(record)
    db.commit()
    return {"status": "success"}

# GET /reports - To view all reports
@router.get("/reports", response_model=List[schemas.SystemStatusSchema])
def get_all_reports(db: Session = Depends(get_db)):
    return db.query(models.SystemStatus).all()

# ✅ FIXED: GET /machines - Now returns full status for each machine
@router.get("/machines", response_model=List[schemas.SystemStatusSchema])
def get_all_machines(db: Session = Depends(get_db)):
    return db.query(models.SystemStatus).all()
