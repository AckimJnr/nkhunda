from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
"""
db_config module

Connect to our database and create collections
"""

uri = "mongodb+srv://nkhunda:100nkhunda@nkhunda.biarzbj.mongodb.net/?retryWrites=true&w=majority&appName=nkhunda"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.nkhunda_db
collections = db['app', 'user', 'message', 'group', 'chat', 'notification']