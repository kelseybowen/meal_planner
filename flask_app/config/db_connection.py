from pymongo import MongoClient
from dotenv import load_dotenv
import certifi
import os

load_dotenv()
ca = certifi.where()
username = os.getenv('USER')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')

def connectToDb():

    uri = f"mongodb+srv://{username}:{password}@{host}/?retryWrites=true&w=majority"
    client = MongoClient(uri, tlsCAFile=ca)
    db = client.meals
    coll = db.recipes

    cursor = coll.find()
    for doc in cursor:
        print(doc)

    client.close()
