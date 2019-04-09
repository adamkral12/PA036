from app.postgres import PostgresDb
from app.mongo import MongoDB
import yaml

if __name__ == '__main__':
    mongo_db = MongoDB()
    postgres_db = PostgresDb()
    log_output = []
    with open("/app/app/data.yaml", 'r') as stream:
        queries = yaml.safe_load(stream)

    i = 0
    for query in queries["config"]:
        mongo_time = mongo_db.run_query(query)
        pg_time = postgres_db.run_query(query)

        log_output.append({
            'mongo_time': mongo_time,
            'postgres_time': pg_time,
            'description': query["description"],
            'id': i
        })

        i += 1

    print(log_output)

    print("Insert multiple:", postgres_db.run_command(postgres_db.execute, postgres_db.insert_multiple()))
    print("After 11 insert:",
          postgres_db.execute_all("SELECT count(*) FROM emails_with_events WHERE (data ->> 'from') = 'test@test.com';"))

    print("Insert single:", postgres_db.run_command(postgres_db.execute, postgres_db.insert_single()))
    print("After 1 insert:",
          postgres_db.execute_all("SELECT count(*) FROM emails_with_events WHERE (data ->> 'from') = 'test@test.com';"))

    print("Events before insert:",
          postgres_db.execute_all("SELECT count(*) FROM (SELECT json_array_elements(data -> 'events') FROM emails_with_events WHERE id = '0') AS events;"))
    print("Insert event:",
          postgres_db.run_command(postgres_db.execute, postgres_db.insert_event()))
    print("Events after insert:",
          postgres_db.execute_all("SELECT count(*) FROM (SELECT json_array_elements(data -> 'events') FROM emails_with_events WHERE id = '0') AS events;"))

    print("Delete by from:",
          postgres_db.run_command(postgres_db.execute, postgres_db.delete_by_from()))
    print("After delete:",
          postgres_db.execute_all("SELECT count(*) FROM emails_with_events WHERE (data ->> 'from') = 'test@test.com';"))

    print("Delete emails by platform device:",
          postgres_db.run_command(postgres_db.execute, postgres_db.delete_by_event_device()))

    print("Delete events by platform device:",
          postgres_db.run_command(postgres_db.execute, postgres_db.delete_event_by_event_device()))

    print("Delete events by event type:",
          postgres_db.run_command(postgres_db.execute, postgres_db.delete_event_by_event_type()))
