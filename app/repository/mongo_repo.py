from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
import logging

class MongoRepository:
    def __init__(self):
        self.client = AsyncIOMotorClient(settings.MONGO_URI)
        self.collection = self.client.mydb.data

    async def save_many(self, data: list[dict]):
        if data:
            await self.collection.insert_many(data)
            logging.info(f"Saved {len(data)} records to MongoDB.")

    async def get_all(self, filters: dict = None):
        cursor = self.collection.find(filters or {})
        return await cursor.to_list(length=1000)
