#!/bin/bash

if [ -d ./mongoinit/data ]; then
  echo "Already initialized."
  exit 0
fi

cd mongoinit
docker build --tag mongoinit:latest .
init_ID=$(docker run -d -v $(pwd)/data/db:/data/db mongoinit)
docker logs -f $init_ID | grep -q "init process complete;"

docker stop $(docker ps -f ancestor=mongoinit -q)
docker rm $(docker ps -a -f ancestor=mongoinit -q)
docker rmi $(docker images mongoinit -q)
