# PA036

## Setup
1) install docker & docker-compose
2) Add data for postgres
    - create postgres/emails_with_events.json
    - create postgres/emails_with_events2.json
2) run ``docker-compose up -d``
    - data should be filled from files above 
3) to stop the containers ``docker-compose down``
4) If you change the source code, run ``docker-compose up --build`` to propagate changes
5) If you want to throw out all DB data (even schema), remove `docker/data`
6) add any needed python packages to `requirements.txt`
7) To connect to connect to a container e.g. postgres: `docker exec -it pa036_postgres bash`

## Adminer
1) there is an adminer running on `http://localhost:99`
2) you can check the DB there
3) for postgres - fill out everything to `postgres` and connect

