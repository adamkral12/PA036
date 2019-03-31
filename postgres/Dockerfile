FROM postgres:latest

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB postgres

COPY schema.sql /docker-entrypoint-initdb.d/
COPY emails_with_events.json /data/postgres/emails_with_events.json
COPY emails_with_events2.json /data/postgres/emails_with_events2.json