from fastapi import FastAPI
from sqlalchemy import text
from sqlalchemy.orm import configure_mappers

import app.models

from app.core.config import settings
from app.core.database import SessionLocal

configure_mappers()

app = FastAPI(
    title=settings.API_NAME,
    version=settings.API_VERSION,
    debug=settings.DEBUG,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)


@app.get("/", tags=["Root"])
def root():
    return {
        "message": settings.API_NAME,
        "version": settings.API_VERSION,
        "status": "online",
    }


@app.get("/health", tags=["Health"])
def health():
    try:
        with SessionLocal() as db:
            db.execute(text("SELECT 1"))

        return {
            "api": "online",
            "database": "connected",
        }

    except Exception as e:
        return {
            "api": "online",
            "database": "disconnected",
            "error": str(e),
        }