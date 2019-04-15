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
            res = self.emails_col.insert_one(json_value)
            end = time()
            print("MongoDB -- inserted id: " + str(res.inserted_id))
        elif method == "INSERT_MANY":
            start = time()
            res = self.emails_col.insert_many(json_value)
            end = time()
            print("MongoDB -- number of inserted items: " + str(len(res.inserted_ids)))
        elif method == "UPDATE_MANY":
            start = time()
            res = self.emails_col.update_many(json_filter, json_value, array_filters = json_array_filters)
            end = time()
            print("MongoDB -- number of modified: " + str(res.modified_count))
        elif method == "DELETE_MANY":
            start = time()
            res = self.emails_col.delete_many(json_filter)
            end = time()
            print("MongoDB -- mongo number of deleted: " + str(res.deleted_count))
        elif method == "FIND":
            start = time()
            res = self.emails_col.find(json_filter)
            end = time()
            print("MongoDB -- number of found: " + str(res.count_documents()))
        elif method == "AGGREGATE":
            start = time()
            res = self.emails_col.aggregate(json_filter, allowDiskUse=True)
            end = time()
            print("MongoDB -- number of found: " + self.count_result(res))
        else:
            raise ValueError("Unexpected method in yaml file: " + method)
        return end - start

    def count_result(self, cursor):
        i = 0
        for doc in cursor:
            i += 1
        return str(i)
