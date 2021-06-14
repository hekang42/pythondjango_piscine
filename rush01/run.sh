#!/bin/bash

docker rmi -f a
docker build --tag a .
docker-compose rm -f
docker-compose up --build
