#!/bin/bash

# go to root directory
cd ..

# activate error message 
set -e

echo "============================"
echo "Starting Docker setup..."
echo "============================"

# build docker-compose and run container
docker-compose up --build -d
echo "============================"
echo "Containers are starting up..."
echo "============================"


#source ./setup/check_health.sh
#check_container_status "mongodb"
#check_container_status "todo-app-backend-1"


# activate logs on time
# docker-compose logs -f
#docker-compose logs > docker_logs.txt







