from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI) 
db = client.get_database("sample_mflix")
users_collection = db.get_collection("users")
movies_collection = db.get_collection("movies")