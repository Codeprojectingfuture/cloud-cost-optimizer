from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Recommendation
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[dict])
def get_recommendations(db: Session = Depends(get_db)):
    recs = db.query(Recommendation).all()
    return [
        {
            "id": r.id,
            "service": r.service,
            "resource_id": r.resource_id,
            "recommendation": r.recommendation,
            "created_at": r.created_at
        }
        for r in recs
    ]
