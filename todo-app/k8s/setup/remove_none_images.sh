#!/bin/bash

echo "============================"
echo "Checking for <none> Docker images..."
echo "============================"

none_images=$(docker images --filter "dangling=true" -q)

if [ -z "$none_images" ]; then
    echo "No <none> images found. Nothing to delete."
    exit 0
fi


echo "The following <none> images will be deleted:"
docker images --filter "dangling=true"

read -p "Do you want to delete these images? (y/n): " response

if [[ "$response" =~ ^[Yy]$ ]]; then
    echo "Deleting <none> images..."
    docker rmi $none_images
    echo "Deletion complete."
else
    echo "Deletion aborted. No images were removed."
fi
