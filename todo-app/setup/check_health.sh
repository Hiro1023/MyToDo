#!/bin/bash

# check if container could be created 
check_container_status() {
  local container_name=$1
  until [ "$(docker inspect --format='{{.State.Health.Status}}' "$container_name")" == "healthy" ]; do
    echo "Waiting for $container_name to be healthy..."
    sleep 2
  done
}