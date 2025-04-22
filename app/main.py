from fastapi import FastAPI
from app.api.routes import router
from app.core.logging_config import setup_logging

setup_logging()

app = FastAPI(
    title="Scalable Data Integration API",
    description="""
    This API allows ingestion of large datasets from external REST and GraphQL sources, applies transformations, 
    and stores them efficiently in a database. It supports asynchronous operations, parallel processing, and JWT-based security.
    """,
    version="1.0.0",
    contact={
        "name": "Gishara Premarathne",
        "email": "gishara@tikos.com",
    },
    license_info={
        "name": "TIKOS",
    }
)

app.include_router(router)
