import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import logging
import sys

# Suppress motor logging that might leak to stdout
logging.getLogger("pymongo").setLevel(logging.WARNING)
logging.getLogger("motor").setLevel(logging.WARNING)

load_dotenv()

class MongoManager:
    def __init__(self):
        self.client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
        self.db = self.client[os.getenv("DATABASE_NAME")]

    def get_collection(self, collection_name: str):
        return self.db[collection_name]

# Singleton instance for the app
db_manager = MongoManager()