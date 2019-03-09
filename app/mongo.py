from pymongo import MongoClient


class MongoDB:
    def __init__(self):
        client = MongoClient("mongodb://mongo:27017")
        mongo_db = client["mongo"]
        emails_col = mongo_db["customers"]
        data = {"name": "John", "address": "Highway 37"}
        x = emails_col.insert_one(data)
        print(x.inserted_id)