from fastapi import FastAPI
from app.database import engine, Base
from app.models import incident, resource
from app.routes import incident_routes, resource_routes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(incident_routes.router)
app.include_router(resource_routes.router)

@app.get("/")
def read_root():
    return {"message": "Campus Infrastructure Monitoring System Running"}