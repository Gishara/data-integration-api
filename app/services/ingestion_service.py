import asyncio
import concurrent.futures
from app.ingestion.rest_client import fetch_rest_data
from app.ingestion.graphql_client import fetch_graphql_data
from app.repository.base import BaseRepository
from app.services.transform_service import transform_data

class DataIngestionService:

    def __init__(self, repo: BaseRepository):
        self.repo = repo

    
    async def ingest_data_from_sources(self):
        loop = asyncio.get_event_loop()

        with concurrent.futures.ThreadPoolExecutor() as pool:
            rest_data, gql_data = await asyncio.gather(
                loop.run_in_executor(pool, fetch_rest_data),
                loop.run_in_executor(pool, fetch_graphql_data)
            )

        processed_data = transform_data(rest_data + gql_data)
        await self.repo.save_many(processed_data)


    async def get_data(self, filters: dict = None, skip: int = 0, limit: int = 100):
        return await self.repo.get_all(filters, skip, limit)
