from app.repository.base import BaseRepository
from app.core.config import settings
from databases import Database
import logging

class PostgresRepository(BaseRepository):
    def __init__(self):
        self.database = Database(settings.DATABASE_URL)

    async def connect(self):
        if not self.database.is_connected:
            await self.database.connect()

    async def disconnect(self):
        if self.database.is_connected:
            await self.database.disconnect()

    async def save_many(self, data: list[dict]):
        await self.connect()
        query = """
        INSERT INTO data (id, value, timestamp)
        VALUES (:id, :value, :timestamp)
        ON CONFLICT (id) DO UPDATE SET value = EXCLUDED.value, timestamp = EXCLUDED.timestamp
        """
        await self.database.execute_many(query=query, values=data)
        logging.info(f"Saved {len(data)} records to PostgreSQL.")

    async def get_all(self, filters: dict = None, skip: int = 0, limit: int = 100):
        await self.connect()
        where_clause = ""
        values = {}

        if filters and "value" in filters:
            where_clause = "WHERE value ILIKE :value"
            values["value"] = f"%{filters['value']}%"

        query = f"""
        SELECT * FROM data
        {where_clause}
        ORDER BY timestamp DESC
        OFFSET :skip LIMIT :limit
        """
        values.update({"skip": skip, "limit": limit})
        return await self.database.fetch_all(query=query, values=values)
