from fastapi import FastAPI
from app.database import engine, Base
from app.models import incident, resource

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Campus Infrastructure Monitoring System Running"}