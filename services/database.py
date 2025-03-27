import os

import dotenv
from pymongo import MongoClient

dotenv.load_dotenv()
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = "rag_csv_db"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
files_collection = db["files"]