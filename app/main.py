from fastapi import FastAPI
from app.core.config import settings
app = FastAPI(
    title="E-Commerce Backend API",
    version="1.0.0",
    debug = settings.DEBUG
)


from app.api.v1 import auth


app.include_router(auth.router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}
