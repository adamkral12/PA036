#!/usr/bin/env bash
docker-compose up mongo postgres &
for i in {0..1}
do
   docker-compose up app && cp output/data.csv output/data_${i}.csv && docker-compose down app
done