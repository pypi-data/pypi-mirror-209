import pymongo.errors
from botocore.exceptions import EndpointConnectionError
from pymongo import MongoClient
from pymongo.database import Database
from enum import Enum
from xm_ai.aws_utils import get_secret


class xMentiumMongoSecret(Enum):
    username = 'username'
    password = 'password'
    address = 'address'
    port = 'port'
    database = 'database'
    production_name: str = 'production'


def get_database(server_name: str) -> Database:
    database_name = server_name
    if server_name == "production" or server_name == "staging":
        secret = get_secret("xmentium_mongo")
        connstring = f"mongodb:" \
                     f"//{secret[xMentiumMongoSecret.username.value]}" \
                     f":{secret[xMentiumMongoSecret.password.value]}" \
                     f"@{secret[xMentiumMongoSecret.address.value]}" \
                     f":{secret[xMentiumMongoSecret.port.value]}" \
                     f"/{secret[xMentiumMongoSecret.database.value]}"
        database_name = secret[
            xMentiumMongoSecret.production_name.value] if server_name == "production" else server_name
    elif server_name == "develop":
        connstring = "mongodb://localhost:27017"
        database_name = "xm"
    elif server_name == "ai":
        secret = get_secret("ai_mongo")
        connstring = f"mongodb+srv:" \
                     f"//{secret[xMentiumMongoSecret.username.value]}" \
                     f":{secret[xMentiumMongoSecret.password.value]}" \
                     f"@{secret[xMentiumMongoSecret.address.value]}" \
                     f"/{secret[xMentiumMongoSecret.database.value]}"
    else:
        raise ValueError("Invalid Option Selected")

    try:
        db = MongoClient(connstring)[database_name]
        try:
            _ = db.templates.find_one({})['name']
            return db
        except TypeError as error:
            print(error)
            raise ValueError(f"You tried to connect to a database: {database_name} that doesn't exist in this server: {server_name}")
        except pymongo.errors.ServerSelectionTimeoutError as error:
            print(error)
            raise pymongo.errors.ServerSelectionTimeoutError("This connection string likely does not have access to the database")

    except EndpointConnectionError as error:
        print(error)
        print("You are offline, so Boto3 could not create a session")
        raise EndpointConnectionError
