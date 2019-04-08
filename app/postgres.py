import psycopg2
import time

from time import sleep


class PostgresDb:
    def __init__(self):
        try:
            self.conn = psycopg2.connect("dbname=postgres user=postgres host=postgres password=postgres")
        except psycopg2.OperationalError:
            print("DB is not up yet, retry in 1 second")
            sleep(1)
            self.__init__()

    def execute_one(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        result = cur.fetchone()
        cur.close()
        return result

    def execute_all(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        return result

    # should measure the amount of time it took to call `callable`
    # return start, end
    def run_command(self, callable, argument):
        start_time = time.time()
        callable(argument)
        return time.time() - start_time
