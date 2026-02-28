from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Campus Infrastructure Monitoring System Running"}