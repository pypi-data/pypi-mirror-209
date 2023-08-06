from pymongo import MongoClient
from pymongo.database import Database


def get_database(connstring: str) -> Database:

    db = MongoClient(connstring)
    try:
        _ = db.templates.find_one({})['name']
        return db
    except Exception as error:
        print(error)
