import os
from time import sleep

from app.postgres import PostgresDb


def run_postgres_scripts():
    postgres_db = PostgresDb()
    postgres_db.init_schema()


if __name__ == '__main__':
    run_postgres_scripts()