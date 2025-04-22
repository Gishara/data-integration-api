import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")
    MONGO_URI = os.getenv("MONGO_URI")
    API_KEY = os.getenv("EXTERNAL_API_KEY")

settings = Settings()
