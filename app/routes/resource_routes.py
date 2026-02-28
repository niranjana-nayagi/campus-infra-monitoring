from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.resource import Resource

router = APIRouter()

@router.post("/resources")
def create_resource(name: str, db: Session = Depends(get_db)):
    new_resource = Resource(name=name)
    db.add(new_resource)
    db.commit()
    db.refresh(new_resource)
    return new_resource

@router.get("/resources")
def get_resources(db: Session = Depends(get_db)):
    return db.query(Resource).all()