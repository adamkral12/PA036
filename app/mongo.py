from pymongo import MongoClient
from time import time
import json


class MongoDB:
    def __init__(self):
        self.client = MongoClient("mongodb://mongo:27017")
        self.mongo_db = self.client["test"]
        self.emails_col = self.mongo_db["emails"]

    def run_query(self, yaml_conf):
        method = yaml_conf["mongo"]["method"]
        query = yaml_conf["mongo"]["query"]

        if "value" in query:
            json_value = json.loads(query["value"])
        if "filter" in query:
            json_filter = json.loads(query["filter"])
        if "arrayFilters" in query:
            json_array_filters = json.loads(query["arrayFilters"])
        else:
            json_array_filters = None

        if method == "INSERT_ONE":
            start = time()
            self.emails_col.insert_one(json_value)
            end = time()
        elif method == "INSERT_MANY":
            start = time()
            self.emails_col.insert_many(json_value)
            end = time()
        elif method == "UPDATE_MANY":
            start = time()
            self.emails_col.update_many(json_filter, json_value, array_filters = json_array_filters)
            end = time()
        elif method == "DELETE_MANY":
            start = time()
            self.emails_col.delete_many(json_filter)
            end = time()
        elif method == "FIND":
            start = time()
            self.emails_col.find(json_filter)
            end = time()
        elif method == "AGGREGATE":
            start = time()
            self.emails_col.aggregate(json_filter, allowDiskUse=True)
            end = time()
        else:
            raise ValueError("Unexpected method in yaml file: " + method)
        return end - start