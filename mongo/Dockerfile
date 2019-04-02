FROM mongo:latest

ENV MONGO_INITDB_DATABASE test

COPY init.sh /docker-entrypoint-initdb.d/
COPY emails_with_events.json /data/mongo/emails_with_events.json

