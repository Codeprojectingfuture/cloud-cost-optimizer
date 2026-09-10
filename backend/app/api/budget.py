from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Budget
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[dict])
def get_budgets(db: Session = Depends(get_db)):
    budgets = db.query(Budget).all()
    return [
        {
            "id": b.id,
            "amount": b.amount,
            "period": b.period
        }
        for b in budgets
    ]
