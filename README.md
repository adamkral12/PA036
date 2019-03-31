# PA036

## Setup
1) install docker & docker-compose
2) Add data for postgres
    - create postgres/emails_with_events.json
    - create postgres/emails_with_events2.json
2) run ``docker-compose up -d``
    - data should be filled from files above 
3) to stop the containers ``docker-compose down``
4) rebuild images ``docker-compose up --build``
5) If you want to throw out all DB data (even schema), remove `docker/data`
6) add any needed python packages to `requirements.txt`

## Adminer
1) there is an adminer running on `http://localhost:99`
2) you can check the DB there
3) for postgres - fill out everything to `postgres` and connect

