# PA036

## Setup
1) install docker & docker-compose
2) Add data for postgres
    - create postgres/emails_with_events.json
3) Add data for mongo
    - create mongo/mongoinit/emails_with_events.json
4) run ``cd mongo && ./init.sh``    - fills mongo db image with data
5) run ``docker-compose build``
6) run ``docker-compose up -d``
    - data should be filled from files above
7) To run test runs, run ``./docker_master.sh`` - choose required number of iterations in the script
7) to stop the containers ``docker-compose down``
## Adminer
1) there is an adminer running on `http://localhost:99`
2) you can check the DB there
3) for postgres - fill out everything to `postgres` and connect

## Notes

When you stop docker-compose with Ctrl+C, it won't delete containers. You need to run `docker-compose down` to do so.

Running `docker-compose build` you populate the databases. Then `docker-compose up` starts the populated database from image. so the database is always fresh = it has all records.