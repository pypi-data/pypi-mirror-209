from pymongo import MongoClient
from pymongo.database import Database


def get_database(connstring: str, server_name: str) -> Database:

    if server_name == "staging" or server_name == "production":
        database_name = "ft-01"
    else:
        database_name = "xm"

    db = MongoClient(connstring)[database_name]
    try:
        _ = db.templates.find_one({})['name']
        return db
    except TypeError as error:
        print(error)
        raise ValueError(f"You tried to connect to a database: {database_name} that doesn't exist in this server: {server_name}")
