import os

from pymongo import MongoClient

MONGODB_DB_URL = 'mongodb://localhost:27017/'
MONGODB_DB_NAME = 'winners'
 
settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "debug" : True
}

client = MongoClient(MONGODB_DB_URL)
db = client[MONGODB_DB_NAME]
 