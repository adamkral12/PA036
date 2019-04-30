import psycopg2
from time import sleep, time


class PostgresDb:
    def __init__(self):
        try:
            self.conn = psycopg2.connect("dbname=postgres user=postgres host=postgres password=postgres")
        except psycopg2.OperationalError:
            print("DB is not up yet, retry in 1 second")
            sleep(1)
            self.__init__()

    def run_query(self, yaml_conf):
        cur = self.conn.cursor()
        start = time()
        cur.execute(yaml_conf["sql"])
        end = time()
        return end - start
