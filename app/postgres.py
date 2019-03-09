import psycopg2
from time import sleep


class PostgresDb:
    def __init__(self):
        try:
            self.conn = psycopg2.connect("dbname=postgres user=postgres host=postgres password=postgres")
        except psycopg2.OperationalError:
            print("DB is not up yet, retry in 1 second")
            sleep(1)
            self.__init__()

    def init_schema(self):
        cur = self.conn.cursor()
        cur.execute(open("app/schema.sql", "r").read())
        self.conn.commit()
        cur.close()

    def select(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM test;")
        result = cur.fetchone()
        cur.close()
        return result
