from odmantic import AIOEngine
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "certificates_db"

client = AsyncIOMotorClient(MONGO_URI)
engine = AIOEngine(motor_client=client, database=DATABASE_NAME)
