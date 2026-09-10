from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Anomaly
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[dict])
def get_anomalies(db: Session = Depends(get_db)):
    anomalies = db.query(Anomaly).all()
    return [
        {
            "id": a.id,
            "date": a.date,
            "service": a.service,
            "detected_on": a.detected_on,
            "details": a.details
        }
        for a in anomalies
    ]
