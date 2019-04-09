import time


class TimeLogger:
    def __init__(self):
        self.log_map = []

    def log(self, mongo_callable, postgres_callable, description):
        start_mongo = time.time()
        mongo_callable()
        end_mongo = time.time()

        start_postgres = time.time()
        postgres_callable()
        end_postgres = time.time()

        log = {
            'mongo_time': end_mongo - start_mongo,
            'postgres_time': end_postgres - start_postgres,
            'description': description,
            'id': len(self.log_map)
        }

        self.log_map.append(log)

    def print_log(self):
        print(self.log_map)