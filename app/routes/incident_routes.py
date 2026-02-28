from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.incident import Incident

router = APIRouter()

@router.post("/incidents")
def create_incident(title: str, description: str, db: Session = Depends(get_db)):
    new_incident = Incident(title=title, description=description)
    db.add(new_incident)
    db.commit()
    db.refresh(new_incident)
    return new_incident

@router.get("/incidents")
def get_incidents(db: Session = Depends(get_db)):
    return db.query(Incident).all()
