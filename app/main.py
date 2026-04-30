from fastapi import FastAPI
from app.core.confing import settings
app = FastAPI(
    title="E-Commerce Backend API",
    version="1.0.0",
    debug= settings.debug
)


@app.get("/")
def root():
    return {"message": "API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


