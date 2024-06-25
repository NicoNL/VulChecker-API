from fastapi import FastAPI
from .routes import router

app = FastAPI()

app.include_router(router, tags=["Package"])


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Vulnerability Checker API!"}
