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

    def insert_event(self):
        events = """{events, 0}"""
        element = """{"event_type":"test","user_agent":{"browser":null,"platform":null},"position":{"country":null,"city":null,"geographical":{"lat":null,"long":null}},"received":{"date":"2018-08-01 08:04:27.000000","timezone_type":1,"timezone":"+02:00"},"occurred":{"date":"2018-08-01 07:59:59.000000","timezone_type":1,"timezone":"+02:00"},"email_id":"test"}"""
        return "UPDATE emails_with_events SET data = jsonb_insert(to_jsonb(data), '{0}'::text[], jsonb '{1}') WHERE id = '0'".format(events, element)

    def insert_single(self):
        element = """{"from":"test@test.com","to":"madmike272@hotmail.com","sent":{"date":"2018-08-01 08:00:00.000000","timezone_type":1,"timezone":"+02:00"},"type":"upcoming_journey","events":[{"event_type":"delivery","user_agent":{"browser":null,"platform":null},"position":{"country":null,"city":null,"geographical":{"lat":null,"long":null}},"received":{"date":"2018-08-01 08:04:27.000000","timezone_type":1,"timezone":"+02:00"},"occurred":{"date":"2018-08-01 07:59:59.000000","timezone_type":1,"timezone":"+02:00"},"email_id":"c0b7a14f34d345eda2666d5159c288de"}, {"event_type":"delivery","user_agent":{"browser":null,"platform":null},"position":{"country":null,"city":null,"geographical":{"lat":null,"long":null}},"received":{"date":"2018-08-01 08:04:27.000000","timezone_type":1,"timezone":"+02:00"},"occurred":{"date":"2018-08-01 07:59:59.000000","timezone_type":1,"timezone":"+02:00"},"email_id":"c0b74f34d345eda2666d5159c288de"}],"id":"c0b74f34d345eda2666d5159c288de"}"""
        return "INSERT INTO emails_with_events(id, data) VALUES ('0', '{}')".format(element)

    def insert_multiple(self):
        element_single_event = """{"from":"test@test.com","to":"madmike272@hotmail.com","sent":{"date":"2018-08-01 08:00:00.000000","timezone_type":1,"timezone":"+02:00"},"type":"upcoming_journey","events":[{"event_type":"delivery","user_agent":{"browser":null,"platform":null},"position":{"country":null,"city":null,"geographical":{"lat":null,"long":null}},"received":{"date":"2018-08-01 08:04:27.000000","timezone_type":1,"timezone":"+02:00"},"occurred":{"date":"2018-08-01 07:59:59.000000","timezone_type":1,"timezone":"+02:00"},"email_id":"c0b7a14f34d345eda2666d5159c288de"}],"id":"c0b7a14f34d345eda2666d5159c288de"}"""
        element_multiple_events = """{"from":"test@test.com","to":"madmike272@hotmail.com","sent":{"date":"2018-08-01 08:00:00.000000","timezone_type":1,"timezone":"+02:00"},"type":"upcoming_journey","events":[{"event_type":"delivery","user_agent":{"browser":null,"platform":null},"position":{"country":null,"city":null,"geographical":{"lat":null,"long":null}},"received":{"date":"2018-08-01 08:04:27.000000","timezone_type":1,"timezone":"+02:00"},"occurred":{"date":"2018-08-01 07:59:59.000000","timezone_type":1,"timezone":"+02:00"},"email_id":"c0b7a14f34d345eda2666d5159c288de"}, {"event_type":"delivery","user_agent":{"browser":null,"platform":null},"position":{"country":null,"city":null,"geographical":{"lat":null,"long":null}},"received":{"date":"2018-08-01 08:04:27.000000","timezone_type":1,"timezone":"+02:00"},"occurred":{"date":"2018-08-01 07:59:59.000000","timezone_type":1,"timezone":"+02:00"},"email_id":"c0b74f34d345eda2666d5159c288de"}],"id":"c0b74f34d345eda2666d5159c288de"}"""
        return "INSERT INTO emails_with_events(id, data) VALUES ('11', '{1}'), ('1', '{0}'), ('2', '{1}'), ('3', '{0}'), ('4', '{1}'), ('5', '{0}'), ('6', '{1}'), ('7', '{0}'), ('8', '{1}'), ('9', '{0}'), ('10', '{1}')" \
            .format(element_single_event, element_multiple_events)

    def delete_by_from(self):
        return """DELETE FROM emails_with_events WHERE (data ->> 'from') = 'test@test.com'"""

    def delete_by_event_device(self):
        return """DELETE FROM emails_with_events WHERE id in (SELECT id FROM (SELECT id, json_array_elements(data -> 'events') -> 'user_agent' ->> 'platform' as device FROM emails_with_events) as platforms WHERE device = 'Android')"""

    def delete_event_by_event_device(self):
        return """UPDATE emails_with_events e SET data=jsonb_set(to_jsonb(data), '{events}'::text[], to_jsonb(e2.events)) FROM (SELECT id, json_agg(singleevent) as events FROM (SELECT id, json_array_elements(data -> 'events') as singleevent, json_array_elements(data -> 'events') -> 'user_agent' ->> 'platform' as device FROM emails_with_events) as eventarray WHERE device != 'Linux' GROUP BY id) e2 WHERE e.id = e2.id"""

    def delete_event_by_event_type(self):
        return """UPDATE emails_with_events e SET data=jsonb_set(to_jsonb(data), '{events}'::text[], to_jsonb(e2.events)) FROM (SELECT id, json_agg(singleevent) as events FROM (SELECT id, json_array_elements(data -> 'events') as singleevent, json_array_elements(data -> 'events') ->> 'event_type' as eventtype FROM emails_with_events) as eventarray WHERE eventtype != 'delivery' GROUP BY id) e2 WHERE e.id = e2.id"""
