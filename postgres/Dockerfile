FROM postgres:latest as data

ENV PGDATA=/pgdata

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB postgres

COPY emails_with_events.json /tmp/emails_with_events.json
COPY schema.sql /docker-entrypoint-initdb.d/
RUN docker-entrypoint.sh --help

FROM postgres:latest

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB postgres

ENV PGDATA=/pgdata

COPY --chown=postgres:postgres --from=data /pgdata /pgdata
