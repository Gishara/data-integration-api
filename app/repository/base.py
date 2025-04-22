from typing import Protocol
    
from abc import ABC, abstractmethod

class BaseRepository(ABC):

    @abstractmethod
    async def save_many(self, data: list[dict]) -> None:
      pass


    @abstractmethod
    async def get_all(self, filters: dict = None) -> list[dict]:
        pass