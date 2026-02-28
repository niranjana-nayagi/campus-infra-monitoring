from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Campus Infrastructure Monitoring System Running"}

from app.routes import incident_routes
app.include_router(incident_routes.router)

from app.routes import resource_routes
app.include_router(resource_routes.router)
