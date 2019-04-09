import json
from app.postgres import PostgresDb
from app.mongo import MongoDB


def run_postgres_scripts():
    postgres_db = PostgresDb()
    print(postgres_db.run_command(postgres_db.execute, postgres_db.insert()))
    print(postgres_db.execute_one("SELECT * FROM emails_with_events WHERE ID = 0;"))
    # with open("app/PostgresQueries.json") as json_file:
    #     print(postgres_db.execute_one("SELECT * FROM emails_with_events;"))
    #     data = json.load(json_file)
    #     for p in data:
    #         print(p["id"], ":", postgres_db.run_command(postgres_db.execute_all, p["query"]))


def run_mongo_scripts():
    mongo_db = MongoDB()


if __name__ == '__main__':
    run_postgres_scripts()
    run_mongo_scripts()
