import requests
from app.core.config import settings
import logging

def fetch_rest_data():
    try:
        response = requests.get("https://external.api/data", headers={"x-api-key": settings.API_KEY})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logging.error(f"REST fetch failed: {e}")
        return []
