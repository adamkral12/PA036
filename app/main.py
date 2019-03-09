from app.postgres import PostgresDb
from app.mongo import MongoDB


def run_postgres_scripts():
    postgres_db = PostgresDb()


def run_mongo_scripts():
    mongo_db = MongoDB()


if __name__ == '__main__':
    run_postgres_scripts()
    run_mongo_scripts()