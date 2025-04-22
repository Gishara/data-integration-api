from fastapi import APIRouter, Depends, BackgroundTasks, Query
from app.services.ingestion_service import DataIngestionService
from fastapi.responses import JSONResponse
from app.repository.mongo_repo import MongoRepository


router = APIRouter()

def get_data_service() -> DataIngestionService:
    repo = MongoRepository()
    return DataIngestionService(repo)

@router.post(
    "/ingest",
    response_class=JSONResponse,
    summary="Start ingestion from REST & GraphQL sources",
    description="Kicks off a background task to ingest, transform and store data from external sources."
)
async def ingest(background_tasks: BackgroundTasks, service: DataIngestionService = Depends(get_data_service)):
    background_tasks.add_task(service.ingest_data_from_sources)
    return {"message": "Ingestion started in background"}

@router.get(
    "/data",
    summary="Retrieve processed data with pagination and filters",
    description="Returns paginated and filtered processed data."
)
async def get_data(
    value: str = Query(default=None, description="Filter by value (partial match)"),
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=1000),
    service: DataIngestionService = Depends(get_data_service)
):
    filters = {}
    if value:
        filters["value"] = value
    data = await service.get_data(filters=filters, skip=skip, limit=limit)
    return {"data": data, "skip": skip, "limit": limit}

