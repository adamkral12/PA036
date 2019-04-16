#!/usr/bin/env bash
docker-compose down &&
docker-compose up -d mongo postgres
for i in {0..1}
do
   docker-compose up app && mv output/data.csv output/data_${i}.csv
   docker-compose down
done