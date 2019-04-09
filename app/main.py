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