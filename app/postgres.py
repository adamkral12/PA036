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

    def execute(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        cur.close()

    # should measure the amount of time it took to call `callable`
    # return start, end
    def run_command(self, callable, argument):
        start_time = time.time()
        callable(argument)
        return time.time() - start_time

    def insert(self):
        element = """{"from":"sureshot-2@earthlink.net","to":"madmike272@hotmail.com","sent":{"date":"2018-08-01 08:00:00.000000","timezone_type":1,"timezone":"+02:00"},"type":"upcoming_journey","events":[{"event_type":"delivery","user_agent":{"browser":null,"platform":null},"position":{"country":null,"city":null,"geographical":{"lat":null,"long":null}},"received":{"date":"2018-08-01 08:04:27.000000","timezone_type":1,"timezone":"+02:00"},"occurred":{"date":"2018-08-01 07:59:59.000000","timezone_type":1,"timezone":"+02:00"},"email_id":"c0b7a14f34d345eda2666d5159c288de"}],"id":"c0b7a14f34d345eda2666d5159c288de"}"""
        return "INSERT INTO emails_with_events(id, data) VALUES ('0', '{}')".format(element)
