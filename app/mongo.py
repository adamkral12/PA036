from pymongo import MongoClient
import time


class MongoDB:
    def __init__(self):
        self.client = MongoClient("mongodb://mongo:27017")
        self.mongo_db = self.client["test"]
        self.emails_col = self.mongo_db["emails"]

    def run_query(self, yaml_conf):
        start = time.time()
        # TODO: milos if method
        result = self.emails_col.find_one(yaml_conf["mongo"]['query'])
        end = time.time()
        return end - start