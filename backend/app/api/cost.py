from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import CostRecord
from typing import List
from datetime import date

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[dict])
def get_costs(start_date: date = None, end_date: date = None, db: Session = Depends(get_db)):
    query = db.query(CostRecord)
    if start_date:
        query = query.filter(CostRecord.date >= start_date)
    if end_date:
        query = query.filter(CostRecord.date <= end_date)
    results = query.all()
    return [
        {
            "date": c.date,
            "service": c.service,
            "amount": c.amount,
            "usage": c.usage
        }
        for c in results
    ]
