from fastapi import FastAPI
from app.api.v1.router import api_router

app=FastAPI(
    title="Athena API",
    description="Backend API for Project Athena",
    version="0.1.0",
)

app.include_router(api_router)

@app.get("/")
def root():
    return {
        "message": "Athena API is running",
        "version": "0.1.0",
    }
