FROM mongo:latest

ENV MONGO_INITDB_DATABASE test

COPY emails_with_events.json /data/mongo/emails_with_events.json
COPY init-database.sh /docker-entrypoint-initdb.d/
