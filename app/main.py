import json
from app.postgres import PostgresDb
from app.mongo import MongoDB


def run_postgres_scripts():
    postgres_db = PostgresDb()
    print("Insert multiple:", postgres_db.run_command(postgres_db.execute, postgres_db.insert_multiple()))
    print("After 11 insert:",
          postgres_db.execute_all("SELECT count(*) FROM emails_with_events WHERE (data ->> 'from') = 'test@test.com';"))

    print("Insert single:", postgres_db.run_command(postgres_db.execute, postgres_db.insert_single()))
    print("After 1 insert:",
          postgres_db.execute_all("SELECT count(*) FROM emails_with_events WHERE (data ->> 'from') = 'test@test.com';"))

    print("Events before insert:",
          postgres_db.execute_all("SELECT count(*) FROM (SELECT json_array_elements(data -> 'events') FROM emails_with_events WHERE id = 0) AS events;"))
    print("Insert event:",
          postgres_db.run_command(postgres_db.execute, postgres_db.insert_event()))
    print("Events after insert:",
          postgres_db.execute_all("SELECT count(*) FROM (SELECT json_array_elements(data -> 'events') FROM emails_with_events WHERE id = 0) AS events;"))

    print("Delete by from:",
          postgres_db.run_command(postgres_db.execute, postgres_db.delete_by_from()))
    print("After delete:",
          postgres_db.execute_all("SELECT count(*) FROM emails_with_events WHERE (data ->> 'from') = 'test@test.com';"))


def run_mongo_scripts():
    mongo_db = MongoDB()


if __name__ == '__main__':
    run_postgres_scripts()
    run_mongo_scripts()
